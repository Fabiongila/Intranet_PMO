from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('editar_usuraio', views.editar_usuario, name="editar_usuario"),
    path('configurar/', views.configurar, name='configurar'),
]
