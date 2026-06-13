from repositorios.livro_repository import LivroRepository
from modelos.livro import Livro

class LivroRepositorioEmMemoria(LivroRepository):
    def __init__(self):
        self.livros = []

    def adicionar(self, livro: Livro):
        self.livros.append(livro)

    def buscar_por_titulo(self, titulo: str):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    def listar_disponiveis(self):
        return [livro.titulo for livro in self.livros if livro.disponivel]    