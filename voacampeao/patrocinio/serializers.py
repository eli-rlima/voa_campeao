from rest_framework import serializers
from .models import Patrocinio

class PatrocinioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patrocinio
        fields = ('data_intencao', 'viagem', 'patrocinador')

