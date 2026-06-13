from abc import ABC, abstractmethod
from modelos.usuario import Usuario

class UsuarioRepositorio(ABC):
    @abstractmethod
    def adicionar (self, usuario: Usuario): pass

    @abstractmethod
    def buscar_por_nome(self, nome: str) -> Usuario: pass

# IMPLEMENTAÇÃO NA MEMORIA
class UsuarioRepositorioMemoria(UsuarioRepositorio):
    def __init__(self):
        self.usuarios = []

    def adicionar(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def buscar_por_nome(self, nome):
        for usuario in self.usuarios:
            if usuario.nome == nome:
                return usuario
        return None