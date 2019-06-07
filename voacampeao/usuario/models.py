'''Essa classe define um objeto Usuario.'''
from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Usuario(models.Model):
    '''Discionario do gênero do usuario.'''
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("N", "Não informar")
    )
    '''Limitador de tamanho 11 e validador de tamanho'''
    cpf = models.CharField(primary_key=True, max_length=11, null=False, blank=False,
                           validators=[MinLengthValidator(11)])
    nome = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, null=False, blank=False, choices=SEXO_CHOICES)
    data_nascimento = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.cpf
