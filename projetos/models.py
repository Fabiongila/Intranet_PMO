# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    deadline = models.DateField()
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.nome

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    progresso = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.descricao


class Arquivo(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='uploads/')
    enviado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    enviado_em = models.DateTimeField(auto_now_add=True)