import unittest
from datetime import datetime, timedelta
from repositorios.usuario_repository import UsuarioRepositorioMemoria
from repositorios.implementações.livro_em_memoria import LivroRepositorioEmMemoria
from servicos.gerenciador_usuario import GerenciadorUsuario
from servicos.gerenciador_livros import GerenciadorLivro
from servicos.gerenciador_emprestimo import GerenciadorEmprestimo

class TestSistemaBiblioteca(unittest.TestCase):
    def setUp(self):
        self.usuario_repo = UsuarioRepositorioMemoria()
        self.livro_repo = LivroRepositorioEmMemoria()
        self.ger_usuario = GerenciadorUsuario(self.usuario_repo)
        self.ger_livro = GerenciadorLivro(self.livro_repo)
        self.ger_emprestimo = GerenciadorEmprestimo(self.usuario_repo, self.livro_repo)

    def test_cadastrar_usuario_e_livro(self):
        usuario = self.ger_usuario.cadastrar_usuario('Ana')
        livro = self.ger_livro.cadastrar_livro("Python Básico")
        self.assertEqual(usuario.nome, "Ana")
        self.assertEqual(livro.titulo, "Python Básico")
        self.assertTrue(livro.disponivel)

    def test_emprestar_e_devolver_livro_sem_multa(self):
        self.ger_usuario.cadastrar_usuario("João")
        self.ger_livro.cadastrar_livro("Java Avançado")
        self.ger_emprestimo.emprestar_livro("João", "Java Avançado")
        multa = self.ger_emprestimo.devolver_livro("João", "Java Avançado")
        self.assertEqual(multa, 0.0)

    def test_devolver_com_atraso_e_calcular_multa(self):
        usuario = self.ger_usuario.cadastrar_usuario("Maria")
        livro = self.ger_livro.cadastrar_livro("Estrutura de Dados")
        self.ger_emprestimo.emprestar_livro("Maria", "Estrutura de Dados")

        # Força o atraso
        emprestimo = usuario.emprestimos[0]
        emprestimo.data_emprestimo = datetime.now() - timedelta(days=20)
        emprestimo.data_limite = emprestimo.data_emprestimo + timedelta(days=14)

        multa = self.ger_emprestimo.devolver_livro("Maria", "Estrutura de Dados")
        self.assertEqual(multa, 6.0)  # 6 dias de atraso (20 - 14) * R$1.00

if __name__ == '__main__':
    unittest.main()