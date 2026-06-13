# Gerencia se esta disponivel ou não
class Livro:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.disponivel = True

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True