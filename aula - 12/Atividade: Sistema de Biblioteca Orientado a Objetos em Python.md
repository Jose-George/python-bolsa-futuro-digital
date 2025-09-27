# **Atividade: Sistema de Biblioteca Orientado a Objetos em Python**

> **Objetivo**: Criar um **sistema simples de gerenciamento de biblioteca** aplicando **orientação a objetos** e **boas práticas de engenharia de software**, incluindo organização de pastas, modularização, testes e documentação.

---

## 📝 Descrição

Você deve desenvolver uma aplicação que permita:

1. **Cadastrar livros** com título, autor e ano de publicação.
2. **Cadastrar usuários** com nome e ID.
3. **Emprestar livros** a usuários (marcar um livro como emprestado).
4. **Devolver livros** (marcar como disponível novamente).
5. Listar:

   * Todos os livros disponíveis
   * Livros emprestados
   * Usuários e quais livros estão com eles

---

## 💡 Requisitos Técnicos

* **Orientação a Objetos**:

  * Crie classes como `Livro`, `Usuario` e `Biblioteca`.
  * A classe `Biblioteca` será a principal, controlando o cadastro e os empréstimos.
* **Modularização**:

  * Separe classes em módulos dentro de uma pasta `models/`.
  * Coloque a lógica de interação (menu) em `src/main.py`.
* **Organização de Pastas**:
  Siga um padrão parecido com o da aula, por exemplo:

```
biblioteca_oo/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── livro.py
│   │   ├── usuario.py
│   │   └── biblioteca.py
├── tests/
│   ├── __init__.py
│   └── test_biblioteca.py
├── requirements.txt
└── README.md
```

* **EXTRA: Testes Automatizados**:

  * Escreva testes com `pytest` para:

    * Cadastro de livros/usuários
    * Empréstimo e devolução de livros
    * Verificação de livros disponíveis/emprestados
* **Documentação**:

  * Inclua docstrings nas classes e métodos.
  * Crie um `README.md` explicando como rodar o projeto.

---

## 🧩 Funcionalidades Mínimas

* **Menu interativo no terminal** com opções:

  1. Cadastrar livro
  2. Cadastrar usuário
  3. Emprestar livro
  4. Devolver livro
  5. Listar livros disponíveis
  6. Listar livros emprestados
  7. Listar usuários e seus livros
  8. Sair

* Validação:

  * Não permitir empréstimo de um livro que já esteja emprestado.
  * Avisar caso o usuário ou o livro não existam.

---

## 🔧 Desafios Extras (opcional)

* Adicionar persistência em arquivo (ex.: salvar e carregar os dados em JSON).
* Implementar busca de livros por título ou autor.

---

## ✅ Critérios de Avaliação

* **Organização** do código e pastas.
* **Boas práticas** (nomes claros, type hints, docstrings).
* README com instruções claras.

---

### 🎯 Objetivo Pedagógico

Esse exercício força o aluno a pensar em:

* **Relacionamentos entre classes** (ex.: `Biblioteca` contém vários `Livro` e `Usuario`).
* **Regras de negócio** mais ricas que uma simples operação matemática.
* **Escalabilidade**: o código deve ser organizado para futuras expansões.