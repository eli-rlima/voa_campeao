'''Classe que serializa o Objeto Usuário para acesso via view.'''
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    '''Classe que serializa e cria url para cada usuário no banco.'''
    class Meta:
        model = Usuario
        fields = ('url', 'cpf', 'nome', 'sexo', 'data_nascimento')
