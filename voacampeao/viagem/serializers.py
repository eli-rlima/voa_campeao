from rest_framework import serializers
from .models import Viagem, Patrocinio

class ViagemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Viagem
        fields = ('url','origem', 'destino', 'data_ida', 'data_volta', 'descricao_comp',
        'modalidade_comp', 'patrocinador', 'atleta')

class PatrocinioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patrocinio
        fields = ('url', 'viagem', 'patrocinadorOp', 'data_intencao')
