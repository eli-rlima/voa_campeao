from django.shortcuts import render, redirect
from .services import usuario_services
from .entidades import usuario

# Create your views here.
from .forms import UsuarioForm
from .models import Usuario


def listar_usuarios(request):
    usuarios = usuario_services.listar_usuarios()
    return render(request, 'usuario/listar_usuarios.html',{'usuarios': usuarios})

def cadastrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
            # nome = form.cleaned_data["nome"]
            # sexo = form.cleaned_data["sexo"]
            # cpf = form.cleaned_data["cpf"]
            # data_nascimento = form.cleaned_data["data_nascimento"]
            # usuario_novo = usuario.Usuario(cpf=cpf, nome=nome, sexo=sexo, data_nascimento=data_nascimento)
            # usuario_services.cadastrar_usuario(usuario_novo)
    else:
        form = UsuarioForm()
    return render (request, 'usuario/form_usuario.html', {'form': form})

def listar_usuario_id(request, cpf):
    usuario = usuario_services.listar_usuario_id(cpf)
    return render(request,'usuario/listar_usuario.html', {'usuario':usuario})

def editar_usuario(request, cpf):
    usuario_antigo = usuario_services.listar_usuario_id(cpf)
    form = UsuarioForm(request.POST or None, instance=usuario_antigo)
    if form.is_valid():
        form.save()
        # nome = form.cleaned_data["nome"]
        # sexo = form.cleaned_data["sexo"]
        # cpf = form.cleaned_data["cpf"]
        # data_nascimento = form.cleaned_data["data_nascimento"]
        # usuario_novo = usuario.Usuario(cpf=cpf, nome=nome, sexo=sexo, data_nascimento=data_nascimento)
        # usuario_services.editar_usuario(usuario_antigo, usuario_novo)
        return redirect("listar_usuarios")
    return render(request,'usuario/form_usuario.html',{'form':form})

def remover_usuario(request,cpf):
    usuario = usuario_services.listar_usuario_id(cpf)
    if request.method == "POST":
        usuario_services.remover_usuario(usuario)
        return redirect('listar_usuarios')
    return render(request, 'usuario/confirma_exclusao.html',{'usuario':usuario})