from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, usuario, livro, dias_para_devolver=7):
        self.usuario = usuario   #  ASSOCIAAÇÃO: referncia direta ao usuario
        self.livro = livro       #  ASSOCIAÇÃO: referncia direta ao livro
        self.data_emprestimo = datetime.now()
        self.data_limite = self.data_emprestimo + timedelta(days=dias_para_devolver)
        self.data_devolucao = None
        self.multa = 0.0

    def devolver(self):
        self.data_devolucao = datetime.now()
        if self.data_devolucao > self.data_limite:
            dias_atraso = (self.data_devolucao - self.data_limite).days
            self.multa = dias_atraso * 1.0 # R$ 1,00 por dia
        else:
            self.multa = 0.0
        self.livro.devolver()

    def calcular_multa(self):
        if not self.data_devolucao:
            hoje = datetime.now()
            if hoje > self.data_limite:
                dias_atraso = (hoje - self.data_limite).days
                return dias_atraso * 1.0
        return 0.0