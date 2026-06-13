from abc import ABC, abstractmethod
from modelos.livro import Livro

class LivroRepository(ABC):
    @abstractmethod
    def adicionar(self, livro: Livro): pass

    @abstractmethod
    def buscar_por_titulo(self, titulo: str) -> Livro: pass

    @abstractmethod
    def listar_disponiveis(self) -> list[str]:pass
    