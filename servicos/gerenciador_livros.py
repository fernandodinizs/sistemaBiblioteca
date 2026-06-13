from modelos.livro import Livro
from repositorios.livro_repository import LivroRepository

# So cadastra e lista livros

class GerenciadorLivro:
    def __init__(self, livro_repositoy: LivroRepository):
        self.livro_repository = livro_repositoy
        # DIP (Dependency Invesion): Depende de uma abstração (LivroRepository), não da implementação concreta

    def cadastrar_livro(self, titulo: str):
        if self.livro_repository.buscar_por_titulo(titulo):
            raise Exception("Livro já cadastrado.")
        livro = Livro(titulo)
        self.livro_repository.adicionar(livro)
        return livro

    def listar_livro_disponiveis(self):
        return self.livro_repository.listar_disponiveis()