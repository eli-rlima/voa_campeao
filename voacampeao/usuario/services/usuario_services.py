from ..models import Usuario

def listar_usuarios():
    usuarios = Usuario.objects.all()
    return usuarios

def listar_usuario_id(id):
    usuario = Usuario.objects.get(cpf=id)
    return usuario

def remover_usuario(usuario):
    usuario.delete()

# def cadastrar_usuario(usuario):
#     Usuario.objects.create(cpf=usuario.cpf, nome=usuario.nome, sexo=usuario.sexo,
#                            data_nascimento=usuario.data_nascimento)
#
# def editar_usuario(usuario,usuario_novo):
#     usuario.nome = usuario_novo.nome
#     usuario.sexo = usuario_novo.sexo
#     usuario.data_nascimento = usuario_novo.data_nascimento
#     usuario.cpf = usuario_novo.cpf
#     usuario.save(force_update=True) #atualizar o usuario com os novos dados.
