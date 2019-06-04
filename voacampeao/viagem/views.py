from rest_framework import viewsets
from .models import Viagem
from .serializers import ViagemSerializer

class Viagens(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer
    