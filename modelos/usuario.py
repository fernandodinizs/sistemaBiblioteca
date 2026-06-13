from modelos.emprestimo import Emprestimo

# Responsavel por gerenciar seus emprestimos e multas
class Usuario:
    def __init__(self, nome: str):
        self.nome = nome
        self.emprestimos = []


    # EMPRESTAR LIVRO
    def emprestar_livro(self, livro):
        livro.emprestar()
        emprestimo = Emprestimo(self,livro)
        self.emprestimos.append(emprestimo)
    
    # DEVOLVER LIVRO
    def devolver_livro(self, titulo):
        for emprestimo in self.emprestimos:
            if emprestimo.livro.titulo == titulo and not emprestimo.data_devolucao:
                emprestimo.devolver()
                return emprestimo.multa
        return None
            
    def calcular_multas_ativas(self):
        return sum(e.calcular_multa() for e in self.emprestimos if not e.data_devolucao)