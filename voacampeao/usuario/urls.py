from django.urls import path
from .views import *
urlpatterns = [
    path('listar', listar_usuarios, name='listar_usuarios'),
    path('cadastrar', cadastrar_usuario, name='cadastrar_usuario'),
    path('listar/<str:cpf>', listar_usuario_id, name='listar_usuario_id'),
    path('editar/<str:cpf>', editar_usuario, name='editar_usuario'),
    path('remover/<str:cpf>', remover_usuario, name='remover_usuario')
]