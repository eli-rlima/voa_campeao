'''Classe que define o objeto Viagem.'''
from django.db import models
from usuario.models import Usuario

class Viagem(models.Model):
    '''Atributos e integração com o banco.'''
    STATUS_CHOICES = (('1', 'EM AVALIAÇÃO'), ('2', 'ABERTO'), ('3', 'EM PATROCINIO'),
    ('4', 'PATROCINADA'), ('5', 'VENCIDA'))
    origem = models.CharField(max_length=30, null=False, blank=False)
    destino = models.CharField(max_length=30, null=False, blank=False)
    data_ida = models.DateField(auto_now=False, auto_now_add=False)
    data_volta = models.DateField(auto_now=False, auto_now_add=False)
    descricao_comp = models.TextField(null=False, blank=False)
    modalidade_comp = models.CharField(max_length=30, null=False)
    path_documento = models.FilePathField(null=False, blank=False)
    status = models.CharField(max_length=1, null=False, blank=False, choices=STATUS_CHOICES, default=1)
    atleta = models.ForeignKey(Usuario, related_name='atleta', default="", on_delete=models.PROTECT)

    def criar_patrocinio(self, novo_patrocinador):
      Patrocinio(viagem=self, patrocinadorOp=novo_patrocinador).save()

class Patrocinio(models.Model):
    STATUS_CHOICES_PAT = (('1', 'PENDENTE'), ('2', 'ENVIADO'), ('3', 'CONFIRMADO'),
     ('4', 'RECUSADO'))
    data_intencao =  models.DateTimeField(auto_now_add=True, blank=True)
    viagem = models.ForeignKey(Viagem, related_name='viagem_opened', default="", on_delete=models.PROTECT)
    patrocinadorOp = models.ForeignKey(Usuario, related_name='patrocinador_opened', default="", on_delete=models.PROTECT)
    status_pat = models.CharField(max_length=1, null=False, blank=False, choices=STATUS_CHOICES_PAT, default=1)
    ticket = models.CharField(max_length=6, default="", null=False)

    def enviarTicket(self, novo_ticket):
      self.ticket = novo_ticket
      self.status_pat = 2
      self.save()

    def confirmarTicket(self):
      self.status_pat = 3
      
    def recusarTicket(self):
      self.status_pat = 4

