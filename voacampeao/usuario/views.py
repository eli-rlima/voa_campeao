'''Classe que cria views para acesso a usuários no banco.'''
from rest_framework import viewsets
from rest_framework import filters
from .models import Usuario
from .serializers import UsuarioSerializer

class Usuarios(viewsets.ModelViewSet):
    '''Cria view via rest com busca.'''
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome', 'cpf')
