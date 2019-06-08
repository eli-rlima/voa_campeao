from django.db import models
from usuario.models import Usuario
from viagem.models import Viagem 

class Patrocinio(models.Model):
	data_intencao =  models.DateTimeField(auto_now_add=True, blank=True)
	viagem = models.ForeignKey(Viagem, related_name='viagem', default="", on_delete=models.PROTECT)
	patrocinador = models.ForeignKey(Usuario, related_name='patrocinador', default="", on_delete=models.PROTECT)
