from servicos.gerenciador_usuario import GerenciadorUsuario
from servicos.gerenciador_livros import GerenciadorLivro
from servicos.gerenciador_emprestimo import GerenciadorEmprestimo
from repositorios.implementações.livro_em_memoria import LivroRepositorioEmMemoria
from repositorios.usuario_repository import UsuarioRepositorioMemoria

def exibir_menu():
    print("\n=== Sistema de Biblioteca ===")
    print("1. Cadastrar Usuário")
    print("2. Cadastrar Livro")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Listar Livros Disponíveis")
    print("6. Sair")

def main():
    usuario_repo = UsuarioRepositorioMemoria()
    livro_repo = LivroRepositorioEmMemoria()

    ger_usuario = GerenciadorUsuario(usuario_repo)
    ger_livro = GerenciadorLivro(livro_repo)
    ger_emprestimo = GerenciadorEmprestimo(usuario_repo, livro_repo)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do usuário: ")
            try:
                usuario = ger_usuario.cadastrar_usuario(nome)
                print(f"Usuário '{usuario.nome}' cadastrado com sucesso.")
            except Exception as e:
                print(f"Erro ao cadastrar usuário: {e}")    

        elif opcao == "2":
            try:
                titulo = input("Título do livro: ")
                livro = ger_livro.cadastrar_livro(titulo)
                print(f"Livro '{livro.titulo}' cadastrado com sucesso.")
            except Exception as e:
                print(f"Erro ao cadastrar Livro: {e}")

        elif opcao == "3":
            nome = input("Nome do usuário: ")
            titulo = input("Título do livro: ")
            try:
                ger_emprestimo.emprestar_livro(nome, titulo)
                print("Livro emprestado com sucesso.")
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == "4":
            nome = input("Nome do usuário: ")
            titulo = input("Título do livro: ")
            try:
                multa = ger_emprestimo.devolver_livro(nome, titulo)
                if multa > 0:
                    print(f"Livro devolvido com multa de R$ {multa:.2f}")
                else:
                    print("Livro devolvido sem multa.")
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == "5":
            livros = ger_livro.listar_livro_disponiveis()
            if livros:
                print("Livros disponíveis:")
                for titulo in livros:
                    print(f'- {titulo}')
            else:
                print('Nenhum livro disponível.')

        elif opcao == "6":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()