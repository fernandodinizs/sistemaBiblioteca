# SISTEMA DE GERENCIAMENTO DE BIBLIOTECA PARA PRÁTICA DE POO

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OOP](https://img.shields.io/badge/Paradigma-POO-blue?style=for-the-badge)
![Unittest](https://img.shields.io/badge/Testes-Unittest-green?style=for-the-badge)

---

## Sobre o Projeto

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido em Python para fins de estudo de Programação Orientada a Objetos (POO). 

Por ser um projeto voltado exclusivamente para fins acadêmicos e prática pessoal, ele não conta com nenhuma licença comercial restritiva, sendo livre para uso, estudo e modificação de qualquer pessoa interessada.

A proposta é treinar a criação de classes, divisão de responsabilidades em camadas, relacionamentos entre objetos, testes automatizados e conceitos como o Princípio de Inversão de Dependência (DIP).

---

## O que o Sistema Faz?

A aplicação fornece um menu interativo no terminal que permite realizar as principais operações de uma biblioteca real.

O sistema gerencia as seguintes funcionalidades:

* Cadastro de usuários
* Cadastro de livros
* Empréstimo de livros (alterando a disponibilidade do livro)
* Devolução de livros
* Cálculo automático de multas por atraso (R$ 1,00 por dia)
* Listagem de livros disponíveis para empréstimo

---

## Tecnologias Utilizadas

O projeto foi desenvolvido utilizando:

* Python 3.10+
* Unittest (módulo nativo para testes unitários)
* Datetime (módulo nativo para manipulação de datas e cálculo de prazos de empréstimos)

---

## Conceitos de POO Aplicados

O projeto exercita conceitos fundamentais de modelagem e design orientado a objetos:

* **Classes e Objetos**: Definição de entidades do domínio como `Livro`, `Usuario` e `Emprestimo`.
* **Associação**: Empréstimos associam de forma direta um objeto `Usuario` e um objeto `Livro`.
* **Encapsulamento**: Atributos e comportamentos centralizados em suas respectivas classes (por exemplo, as regras de cálculo de multa dentro da classe `Emprestimo`).
* **Responsabilidade Única (SRP)**: Separação de fluxo entre camadas de modelo (regras de negócio), serviço (orquestração de ações) e repositório (persistência de dados).

---

## Padrões de Projeto Utilizados

Foi utilizado o padrão **Repository Pattern** em conjunto com a **Inversão de Dependência (DIP)**.

### Por que Inversão de Dependência?

As classes gerenciadoras (serviços) não dependem de implementações de armazenamento concretas, mas sim de abstrações/interfaces (`LivroRepository` e `UsuarioRepositorio`).

Essa separação facilita:

* A troca do meio de persistência (como migrar de um repositório em memória para um banco de dados real SQLite ou MySQL) sem alterar as regras de negócio.
* A criação de mocks e dublês de teste para testes unitários mais confiáveis.
* A manutenção e a escalabilidade geral do sistema de biblioteca.

---

## Estrutura do Projeto

```text
SistemaBiblioteca/
│
├── modelos/
│   ├── emprestimo.py
│   ├── livro.py
│   └── usuario.py
│
├── repositorios/
│   ├── implementações/
│   │   └── livro_em_memoria.py
│   ├── livro_repository.py
│   └── usuario_repository.py
│
├── servicos/
│   ├── gerenciador_emprestimo.py
│   ├── gerenciador_livros.py
│   └── gerenciador_usuario.py
│
├── testes/
│   └── test_sistema_biblioteca.py
│
├── main.py
│
├── README.md
│
└── requirements.txt
```

---

## Objetivo

Consolidar o aprendizado prático de Programação Orientada a Objetos em Python através de um projeto com arquitetura de software desacoplada, limpa e testável.

---

## Instrução de Instalação

### Pré-requisitos

* Python 3.10 ou superior

---

### Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

```bash
cd seu-repositorio
```

---

## Dependências

### Instalar Dependências

Como este projeto utiliza exclusivamente a biblioteca padrão do Python, não há dependências de pacotes de terceiros.

```bash
pip install -r requirements.txt
```

*(O arquivo `requirements.txt` está presente apenas por questões de estrutura organizacional).*

---

## Instrução de Uso

1. Abra o diretório do projeto em seu terminal.
2. Execute o arquivo principal do projeto:

```bash
python main.py
```

3. Utilize as opções do menu interativo exibidas no console para realizar as operações:

```text
=== Sistema de Biblioteca ===
1. Cadastrar Usuário
2. Cadastrar Livro
3. Emprestar Livro
4. Devolver Livro
5. Listar Livros Disponíveis
6. Sair
Escolha uma opção:
```

---

## Executando os Testes

O projeto conta com testes de unidade automatizados escritos utilizando a biblioteca nativa `unittest`. Eles validam os fluxos de cadastros, empréstimos, devoluções normais e devoluções com cálculo de multas.

Para executar os testes:

```bash
python -m unittest testes/test_sistema_biblioteca.py
```

---

## Contribuição

Por se tratar de um projeto com fins puramente educacionais e de estudo individual, qualquer contribuição é bem-vinda para fins de aprendizado mútuo. Sinta-se livre para refatorar o código, adicionar novos recursos ou propor melhorias arquiteturais.
