from repositorios.usuario_repository import UsuarioRepositorio
from repositorios.livro_repository import LivroRepository

# Gerencia Emprestimo e Devolução

class GerenciadorEmprestimo:
    def __init__(self, usuario_repository: UsuarioRepositorio, livro_repository: LivroRepository):
        self.usuario_repository = usuario_repository
        self.livro_repository = livro_repository


    def emprestar_livro(self, nome_usuario: str, titulo_livro: str):
        usuario = self.usuario_repository.buscar_por_nome(nome_usuario)
        # Associa usuário ao buscar ele no repositorio para realizar o emprestimo

        if not usuario:
            raise Exception("Usuário não encontrado.")
        livro = self.livro_repository.buscar_por_titulo(titulo_livro)
        # Associa livro ao buscar ele no repositorio para realizar o emprestimo

        if not livro:
            raise Exception("Livro não encontrado.")

        if not livro.disponivel:
            raise Exception("Livro não está disponível.")
        usuario.emprestar_livro(livro)
        return True
        
    
    def devolver_livro(self, nome_usuario: str, titulo_livro: str):
        usuario = self.usuario_repository.buscar_por_nome(nome_usuario)
        if not usuario:
            raise Exception("Usuário Não encontrado.")
        multa = usuario.devolver_livro(titulo_livro)
        if multa is None:
            raise Exception("Empréstimo não encontrado")
        return multa
    
    def consultar_multa(self, nome_usuario: str):
        usuario = self.usuario_repository.buscar_por_nome(nome_usuario)
        if not usuario:
            raise Exception("Usuário não encontrado.")
        return usuario.calcular_multas_ativas()
