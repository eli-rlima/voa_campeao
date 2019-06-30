'''Classe que cria views para acesso a usuários no banco.'''
from rest_framework import viewsets
from rest_framework import filters
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class Usuarios(viewsets.ModelViewSet):
    '''Cria view via rest com busca.'''
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    @action(methods=['get'], detail=False)
    def buscaCpf(self, request, pk=None):
        cpf = self.request.query_params.get('cpf',None)
        queryset = Usuario.objects.filter(cpf=cpf)
        usuarios= UsuarioSerializer(queryset, many=True, context={'request': request})
        return Response(usuarios.data)
