from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict
from .models import Viagem, Patrocinio

class ViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viagem
        fields = ('origem', 'destino', 'data_ida', 'data_volta', 'competicao', 'descricao_comp',
        'modalidade_comp', 'atleta', 'status')

class ViagemSerializerOp(serializers.ModelSerializer):
    class Meta:
        model = Viagem
        fields =  ('origem', 'destino', 'data_ida', 'data_volta', 'competicao', 'descricao_comp',
        'modalidade_comp', 'atleta', 'status')
        depth = 2
class PatrocinioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patrocinio
        fields = ('viagem', 'patrocinadorOp', 'data_intencao', 'ticket', 'status_pat')
