from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cpf', 'nome', 'sexo', 'data_nascimento']
