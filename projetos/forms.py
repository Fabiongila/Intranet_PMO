from django.forms import ModelForm

from .models import Projeto, Tarefa, Arquivo

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'deadline']

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['descricao', 'responsavel', 'status', 'progresso']

class ArquivoForm(ModelForm):
    class Meta:
        model = Arquivo
        fields = ['arquivo']
