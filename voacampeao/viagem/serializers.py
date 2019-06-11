from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict
from .models import Viagem, Patrocinio

class ViagemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Viagem
        fields = ('url','origem', 'destino', 'data_ida', 'data_volta', 'descricao_comp',
        'modalidade_comp', 'atleta', 'status')

class PatrocinioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patrocinio
        fields = ('url', 'viagem', 'patrocinadorOp', 'data_intencao', 'ticket', 'status_pat')
