from django.db import models
from django.core.validators import MinLengthValidator
import re
from django.core.exceptions import ValidationError

# Create your models here.


class Usuario(models.Model):
    SEXO_CHOICES = (
        ("M","Masculino"),
        ("F","Feminino"),
        ("N","Não informar")
    )
    cpf = models.CharField(primary_key=True,max_length=11,null=False,blank=False,
                           validators=[MinLengthValidator(11)])
    nome = models.CharField(max_length=100, null=False,blank=False)
    sexo = models.CharField(max_length=1, null=False, blank=False, choices=SEXO_CHOICES)
    data_nascimento = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.cpf


