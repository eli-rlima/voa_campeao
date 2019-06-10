'''Classe que cria views para acesso a viagens no banco.'''
from functools import partial

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Viagem, Patrocinio
from .serializers import ViagemSerializer, PatrocinioSerializer
from datetime import datetime
from datetime import timedelta

class Viagens(viewsets.ModelViewSet):
    '''cria view via rest com filtros para busca.'''
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('origem', 'destino', 'modalidade_comp')

    @action(methods=['get'],detail=False)
    def viagemPorUsuario(self, request, pk=None):
        cpf = self.request.query_params.get('atleta',None)
        queryset = Viagem.objects.filter(atleta=cpf)
        viagens = ViagemSerializer(queryset, many=True, context={'request': request})
        return Response(viagens.data)

    @action(methods=['get'], detail=False)
    def viagenStatus(self, request, pk=None):
        status = self.request.query_params.get('status', None)
        queryset = Viagem.objects.filter(status=status)
        viagens = ViagemSerializer(queryset, many=True, context={'request': request})
        return Response(viagens.data)
    
    @action(methods=['get'], detail=False)
    def viagemProximidade(self, request, pk=None):
        dias = self.request.query_params.get('dias', None)
        dateProx = datetime.today() + timedelta(days=int (dias))
        queryset = Viagem.objects.exclude(data_ida__gt=dateProx)
        viagens = ViagemSerializer(queryset, many=True, context={'request': request})
        return Response(viagens.data)
        

class Patrocinios(viewsets.ModelViewSet):
    queryset = Patrocinio.objects.all()
    serializer_class = PatrocinioSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('patrocinadorOp')


    @action(methods=['get'], detail=False)
    def viagensPatrocinador(self, request, pk=None):
        cpf = self.request.query_params.get('cpf', None)
        queryset = Patrocinio.objects.filter(patrocinadorOp=cpf)
        patrocinador = PatrocinioSerializer(queryset, many=True, context={'request': request})
        return Response(patrocinador.data)
