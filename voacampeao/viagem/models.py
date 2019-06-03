from django.db import models

class Viagem(models.Model):
    STATUS_CHOICES=(('1','EM AVALIAÇÃO'),
                    ('2','ABERTO'),
                    ('3','EM PATROCINIO'),
                    ('4', 'PATROCINADA'))
    origem = models.CharField(max_length=30, null=False, blank=False)
    destino = models.CharField(max_length=30, null=False, blank=False)
    data_ida = models.DateField(auto_now= False, auto_now_add = False)
    data_volta = models.DateField(auto_now= False, auto_now_add = False)
    descricao_comp = models.TextField(null=False, blank=False)
    modalidade_comp = models.CharField(max_length=30, null=False)
    path_documento = models.FilePathField(null=False, blank=False)
    status = models.CharField(max_length=1, null=False, blank=False, choices=STATUS_CHOICES)
    #id_atleta
    #id_patrocinador


