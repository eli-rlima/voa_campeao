from django import forms
from django.core.validators import RegexValidator

from .models import Usuario


class UsuarioForm(forms.ModelForm):
    cpf = forms.CharField(min_length=11, max_length=11,validators=[RegexValidator(regex='^[0-9]{11}$')])
    class Meta:
        model = Usuario
        fields = ['cpf','nome','sexo','data_nascimento']