from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projeto/novo/', views.novo_projeto, name='novo_projeto'),
    path('projeto/<int:projeto_id>/', views.detalhes_projeto, name='detalhes_projeto'),
    path('projeto/<int:projeto_id>/tarefa/', views.nova_tarefa, name='nova_tarefa'),
    path('<int:projeto_id>/upload/', views.upload_arquivo, name='upload_arquivo'),
    ]
