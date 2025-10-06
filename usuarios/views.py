# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CadastroForm, EditUserForm, ConfiguracaoForm
from django.contrib.auth.decorators import login_required
from .models import ConfiguracaoPlataforma

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('dashboard')

    return render(request, 'usuarios/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})


def editar_usuario(request):
    if request.method == 'POST':
        usuario_form = EditUserForm(request.POST, instance=request.user)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('dashboard')
    else:
        usuario_form = EditUserForm(instance=request.user)
    return render(request, 'usuarios/editar_usuario.html', {'form': usuario_form})    


def configurar(request):
    config, created = ConfiguracaoPlataforma.objects.get_or_create(id=1)
    if request.method == 'POST':
        config_form = ConfiguracaoForm(request.POST, request.FILES, instance=config)
        if config_form.is_valid():
            config_form.save()
            return redirect('dashboard')
    else:
        config_form = ConfiguracaoForm(instance=config)
    return render(request, 'usuarios/configurar.html', {'form':config_form, 'config': config})
