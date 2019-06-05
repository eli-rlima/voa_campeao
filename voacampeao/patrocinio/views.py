from rest_framework import viewsets
from .models import Patrocinio
from .serializers import PatrocinioSerializer

class Patrocinios(viewsets.ModelViewSet):
    queryset = Patrocinio.objects.all()
    serializer_class = PatrocinioSerializer

# Create your views here.
