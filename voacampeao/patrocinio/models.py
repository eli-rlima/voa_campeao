from django.db import models

class Patrocinio(models.Model):
	data_intencao =  models.DateTimeField(auto_now_add=True, blank=True)
	#id_patrocinador
	#id_viagem