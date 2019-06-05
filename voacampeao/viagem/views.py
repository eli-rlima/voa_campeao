from rest_framework import viewsets
from .models import Viagem
from .serializers import ViagemSerializer
from rest_framework import filters

class Viagens(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('origem', 'destino')

