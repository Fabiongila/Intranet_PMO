from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import ConfiguracaoPlataforma

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class CadastroForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)
    class Meta:
            model = User
            fields = ['username', 'email']

    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('As senhas não coincidem.')
        return self.cleaned_data['password2']


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username' ,'email', 'password']

class ConfiguracaoForm(ModelForm):
    class Meta:
        model = ConfiguracaoPlataforma
        fields = ['logotipo']