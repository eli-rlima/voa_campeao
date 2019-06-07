from rest_framework import serializers
from .models import Viagem

class ViagemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Viagem
        fields = ('url','origem', 'destino', 'data_ida', 'data_volta', 'descricao_comp', 'modalidade_comp')
