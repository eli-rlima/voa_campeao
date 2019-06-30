'''Classe que serializa o Objeto Usuário para acesso via view.'''
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    '''Classe que serializa e cria url para cada usuário no banco.'''
    class Meta:
        model = Usuario
        fields = ('cpf', 'nome', 'sexo', 'data_nascimento')
        
