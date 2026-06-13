from modelos.usuario import Usuario
from repositorios.usuario_repository import UsuarioRepositorio

# So Cadastra Usuário

class GerenciadorUsuario:
    def __init__(self, usuario_repository: UsuarioRepositorio):
        self.usuario_repository = usuario_repository

    def cadastrar_usuario(self, nome: str):
        if self.usuario_repository.buscar_por_nome(nome):
            raise Exception("Usúario já cadastrado.")
        usuario = Usuario(nome)
        self.usuario_repository.adicionar(usuario)
        return usuario