from django.urls import path
from .views import *
urlpatterns = [
    path('listar', listar_usuarios, name='listar_usuarios'),
    path('cadastrar', inserir_cliente, name='inserir_cliente')
]