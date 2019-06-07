'''classe para registro de apps.'''
from django.contrib import admin
from usuario.models import Usuario
from .models import Viagem
# Register your models here.
admin.site.register(Viagem)
admin.site.register(Usuario)
