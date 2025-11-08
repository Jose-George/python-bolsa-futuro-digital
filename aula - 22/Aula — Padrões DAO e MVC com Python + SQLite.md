# 🧠 Aula — Padrões DAO e MVC com Python + SQLite

**Turma:** Python Intermediário – Softex PB  
**Tema:** Organização do código com DAO e MVC  
**Duração:** 2h  
**Pré-requisitos:**  
✅ Conhecimento básico de POO  
✅ Uso de SQLite com Python (`sqlite3`)  

---

## 🎯 Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Entender o que são e para que servem os padrões **DAO** e **MVC**
- Separar responsabilidades no código
- Criar uma aplicação Python organizada e escalável
- Aplicar os conceitos de **camadas de software** (dados, lógica, interface)

---

## 🧩 1. O que é o Padrão DAO?

**DAO (Data Access Object)** é um padrão que **organiza o acesso ao banco de dados**.

Ele cria uma **camada intermediária** entre a aplicação e o banco, responsável por:

- Criar tabelas e conexões  
- Inserir, atualizar e buscar dados  
- Proteger o resto do sistema de mudanças no banco  

### 📊 Estrutura Simplificada

```

Aplicação  →  DAO  →  Banco de Dados

````

### 📦 Exemplo de DAO

```python
import sqlite3

class ClienteDAO:
    def __init__(self, db_name='clientes.db'):
        self.db_name = db_name
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')

    def salvar(self, nome, email):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO cliente (nome, email) VALUES (?, ?)', (nome, email))
            conn.commit()

    def listar(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT nome, email FROM cliente')
            return cursor.fetchall()
````

---

## 🧠 2. O que é o Padrão MVC?

**MVC (Model–View–Controller)** é um padrão de arquitetura que **separa o código** em três partes:

| Camada         | Função                             | Exemplo                     |
| -------------- | ---------------------------------- | --------------------------- |
| **Model**      | Regras de negócio e acesso a dados | Classes, DAO                |
| **View**       | Interface com o usuário            | Entrada e saída de dados    |
| **Controller** | Faz a ponte entre Model e View     | Coordena o fluxo do sistema |

### 💡 O DAO geralmente está **dentro da camada Model**!

---

## 🧭 3. Estrutura de Projeto MVC + DAO

```
/meu_app_mvc_dao
│
├── models/
│   ├── cliente.py
│   └── cliente_dao.py
│
├── views/
│   └── cliente_view.py
│
├── controllers/
│   └── cliente_controller.py
│
└── main.py
```

---

## 🧱 4. Implementação Prática

### 🧩 Model — `models/cliente.py`

```python
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.nome} ({self.email})"
```

---

### 🧩 DAO — `models/cliente_dao.py`

```python
import sqlite3
from models.cliente import Cliente

class ClienteDAO:
    def __init__(self, db_name='clientes.db'):
        self.db_name = db_name
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')

    def salvar(self, cliente: Cliente):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO cliente (nome, email) VALUES (?, ?)',
                (cliente.nome, cliente.email)
            )
            conn.commit()

    def listar(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT nome, email FROM cliente')
            rows = cursor.fetchall()
            return [Cliente(nome, email) for nome, email in rows]
```

---

### 🖼️ View — `views/cliente_view.py`

```python
class ClienteView:
    def menu(self):
        print("\n==== MENU CLIENTES ====")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Sair")
        return input("Escolha: ")

    def solicitar_dados(self):
        nome = input("Nome: ")
        email = input("Email: ")
        return nome, email

    def mostrar_mensagem(self, msg):
        print(msg)

    def mostrar_clientes(self, clientes):
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print("\n=== Lista de Clientes ===")
            for c in clientes:
                print("-", c)
```

---

### ⚙️ Controller — `controllers/cliente_controller.py`

```python
from models.cliente import Cliente
from models.cliente_dao import ClienteDAO
from views.cliente_view import ClienteView

class ClienteController:
    def __init__(self):
        self.dao = ClienteDAO()
        self.view = ClienteView()

    def iniciar(self):
        while True:
            opcao = self.view.menu()

            if opcao == "1":
                nome, email = self.view.solicitar_dados()
                cliente = Cliente(nome, email)
                self.dao.salvar(cliente)
                self.view.mostrar_mensagem("✅ Cliente cadastrado com sucesso!")

            elif opcao == "2":
                clientes = self.dao.listar()
                self.view.mostrar_clientes(clientes)

            elif opcao == "3":
                self.view.mostrar_mensagem("👋 Encerrando o sistema...")
                break

            else:
                self.view.mostrar_mensagem("❌ Opção inválida!")
```

---

### 🚀 main.py

```python
from controllers.cliente_controller import ClienteController

if __name__ == "__main__":
    app = ClienteController()
    app.iniciar()
```

---

## 🧭 5. Como Tudo se Conecta

```text
+-----------------+       +-------------------+       +-----------------+
|      View       | <---> |    Controller     | <---> |      Model      |
| (Interface)     |       | (Coordena ações)  |       | (DAO e regras)  |
+-----------------+       +-------------------+       +-----------------+
```

* **A View** mostra o menu e coleta informações.
* **O Controller** interpreta o que o usuário quer e aciona o Model.
* **O Model (via DAO)** salva ou busca dados no banco.
* O resultado volta para a View, que exibe ao usuário.

---

## ✅ 6. Benefícios de Combinar MVC + DAO

| Benefício                          | Explicação                                             |
| ---------------------------------- | ------------------------------------------------------ |
| **Separação de responsabilidades** | Código dividido em camadas independentes               |
| **Reutilização**                   | O DAO pode ser usado em outros projetos                |
| **Facilidade de manutenção**       | Alterar o banco não afeta a View                       |
| **Escalabilidade**                 | É fácil adicionar novas telas, modelos e controladores |
| **Base para frameworks**           | MVC + DAO são a base do Django e Flask                 |

---

## 🧩 7. Exercícios Práticos

1. Adicione um campo **telefone** no cadastro de cliente.
2. Crie uma nova entidade `Produto` com os atributos: id, preco, nome e qtd_estoque, com seu próprio DAO, View e Controller.
3. Faça uma função `buscar_por_email(email)` no DAO e exiba o resultado.
4. Adicione uma opção no menu para remover clientes.
5. Crie funções para adicionar produto e remove e buscar por id;

---

## 💬 8. Conclusão

* O **DAO** cuida do acesso ao banco.
* O **MVC** organiza o fluxo da aplicação.
* Juntos, tornam o código **modular, limpo e profissional**.

Esses padrões são a base de sistemas reais — e aprender a aplicá-los em projetos simples é o primeiro passo para trabalhar com frameworks modernos como **Flask**, **Django** e **FastAPI**.

