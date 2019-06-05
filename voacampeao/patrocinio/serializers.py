from rest_framework import serializers
from .models import Patrocinio

class PatrocinioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patrocinio
        fields = '__all__'

