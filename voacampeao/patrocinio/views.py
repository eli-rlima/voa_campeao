from rest_framework import viewsets
from .models import Patrocinio
from .serializers import PatrocinioSerializer
from rest_framework import filters

class Patrocinios(viewsets.ModelViewSet):
    queryset = Patrocinio.objects.all()
    serializer_class = PatrocinioSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('data_intencao', 'viagem', 'patrocinador')
# Create your views here.
