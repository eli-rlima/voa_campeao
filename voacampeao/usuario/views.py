from django.shortcuts import render, redirect

# Create your views here.
from .forms import UsuarioForm
from .models import Usuario


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/listar_usuarios.html',{'usuario': usuarios})

def inserir_cliente(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render (request, 'usuario/form_usuario.html', {'form': form})