# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField(max_length=25, null=True)
    nome_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.TextField(max_length=12)

    def __str__(self):
        return self.nome

class ConfiguracaoPlataforma(models.Model):
    nome_empresa = models.CharField(max_length=100)
    logotipo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.nome_empresa