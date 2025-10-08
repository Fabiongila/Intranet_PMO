# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tarefa, Arquivo
from .forms import ProjetoForm, TarefaForm, ArquivoForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    projetos = Projeto.objects.filter(criado_por=request.user)
    return render(request, 'projetos/dashboard.html', {'projetos': projetos})


@login_required
def novo_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.criado_por = request.user
            projeto.save()
            return redirect('dashboard')
    else:
        form = ProjetoForm()
    return render(request, 'projetos/novo_projeto.html', {'form': form})


@login_required
def detalhes_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    tarefas = Tarefa.objects.filter(projeto=projeto)
    arquivos = Arquivo.objects.filter(projeto=projeto)
    return render(request, 'projetos/detalhes.html', {
        'projeto': projeto,
        'tarefas': tarefas,
        'arquivos': arquivos,
    })


@login_required
def nova_tarefa(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        form_nt = TarefaForm(request.POST)
        if form_nt.is_valid():
            tarefa = form_nt.save(commit=False)
            tarefa.projeto = projeto
            tarefa.save()
            return redirect('detalhes_projeto', projeto_id=projeto.id)
    else:
        form_nt = TarefaForm()
    return render(request, 'projetos/nova_tarefa.html', {'form_nt': form_nt, 'projeto': projeto})


@login_required
def upload_arquivo(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, criado_por=request.user)
    if request.method == 'POST':
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.projeto = projeto
            arquivo.enviado_por = request.user
            arquivo.save()
            return redirect('detalhes_projeto', projeto_id=projeto.id)
    else:
        form = ArquivoForm()
    return render(request, 'projetos/upload_arquivo.html', {'form': form, 'projeto': projeto})


@login_required
def contactos(request):
    return render(request, 'projetos/contactos.html')

@login_required
def sobre(request):
    return render(request, 'projetos/sobre.html')

@login_required
def faqs(request):
    return render(request, 'projetos/faqs.html')


#
def index(request):
    return render(request, 'projetos/index.html')