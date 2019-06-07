from rest_framework import viewsets
from rest_framework import filters
from .models import Viagem
from .serializers import ViagemSerializer

class Viagens(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('origem', 'destino', 'modalidade_comp')
