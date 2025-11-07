# 🧠 Aula 2 — **Padrão MVC (Model-View-Controller)**

**Turma:** Python Intermediário – Softex PB

**Tema:** Separando responsabilidades no código com o padrão MVC

---

## 🎯 **Objetivos da Aula**

Ao final desta aula, o aluno será capaz de:

* Entender o que é o **padrão MVC**
* Compreender o papel de cada camada (**Model**, **View**, **Controller**)
* Implementar um **mini sistema MVC em Python**
* Reutilizar e manter o código com mais facilidade

---

## 🧩 **1. O que é o Padrão MVC?**

**MVC** significa **Model–View–Controller**.
É um dos padrões mais usados no desenvolvimento de software, especialmente em **sistemas web e desktop**.

Ele separa o programa em **3 camadas principais**:

| Camada         | Responsabilidade                               | Exemplo                         |
| -------------- | ---------------------------------------------- | ------------------------------- |
| **Model**      | Lida com os **dados** e a **regra de negócio** | Classes, acesso ao banco, DAO   |
| **View**       | Mostra informações ao **usuário**              | Interface (terminal, web, etc.) |
| **Controller** | Faz a **ponte entre Model e View**             | Controla o fluxo do programa    |

---

## 🧠 **2. Por que usar MVC?**

Sem MVC, o código tende a ficar **misturado** — a lógica, os dados e a interface se confundem.

Com MVC:

* Cada parte do sistema tem uma **função clara**
* Fica mais fácil de **testar, modificar e reaproveitar**
* Times diferentes podem trabalhar em paralelo (ex: front e back)

---

## 🧩 **3. Estrutura de Projeto MVC em Python**

Vamos criar um projeto simples de **cadastro de clientes**, agora no padrão MVC.

```
/meu_app_mvc
│
├── models/
│   └── cliente.py
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

## 📘 **4. Implementação Passo a Passo**

### 🧱 **Model (dados e regras de negócio)**

📄 `models/cliente.py`

```python
import sqlite3

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class ClienteModel:
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

    def adicionar(self, cliente: Cliente):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO cliente (nome, email) VALUES (?, ?)',
                           (cliente.nome, cliente.email))
            conn.commit()

    def listar(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT nome, email FROM cliente')
            return cursor.fetchall()
```

---

### 🖼️ **View (interação com o usuário)**

📄 `views/cliente_view.py`

```python
class ClienteView:
    def mostrar_menu(self):
        print("\n==== MENU CLIENTES ====")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Sair")
        return input("Escolha: ")

    def solicitar_dados_cliente(self):
        nome = input("Nome: ")
        email = input("Email: ")
        return nome, email

    def mostrar_mensagem(self, msg):
        print(msg)

    def listar_clientes(self, clientes):
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print("\n=== Lista de Clientes ===")
            for nome, email in clientes:
                print(f"- {nome} ({email})")
```

---

### 🧠 **Controller (coordena tudo)**

📄 `controllers/cliente_controller.py`

```python
from models.cliente import Cliente, ClienteModel
from views.cliente_view import ClienteView

class ClienteController:
    def __init__(self):
        self.model = ClienteModel()
        self.view = ClienteView()

    def iniciar(self):
        while True:
            opcao = self.view.mostrar_menu()

            if opcao == "1":
                nome, email = self.view.solicitar_dados_cliente()
                cliente = Cliente(nome, email)
                self.model.adicionar(cliente)
                self.view.mostrar_mensagem("✅ Cliente cadastrado com sucesso!")

            elif opcao == "2":
                clientes = self.model.listar()
                self.view.listar_clientes(clientes)

            elif opcao == "3":
                self.view.mostrar_mensagem("👋 Encerrando o sistema...")
                break

            else:
                self.view.mostrar_mensagem("❌ Opção inválida!")
```

---

### 🚀 **main.py**

```python
from controllers.cliente_controller import ClienteController

if __name__ == "__main__":
    controller = ClienteController()
    controller.iniciar()
```

---

## 🧭 **5. Como o Fluxo Funciona**

1. O usuário escolhe uma opção → **View**
2. O controller interpreta a escolha → **Controller**
3. O controller conversa com o banco de dados → **Model**
4. O resultado volta para a **View**, que exibe ao usuário

---

## 🔁 **6. Benefícios do Padrão MVC**

| Problema Comum                            | Como o MVC Ajuda                          |
| ----------------------------------------- | ----------------------------------------- |
| Código misturado (bagunçado)              | Separa responsabilidades                  |
| Dificuldade para testar                   | Cada camada pode ser testada isoladamente |
| Mudança de interface (ex: terminal → web) | Só muda a View                            |
| Crescimento do sistema                    | Fica modular e escalável                  |

---

## 🧩 **7. Exercícios Práticos**

1. Adicione ao modelo (`ClienteModel`) uma função `buscar_por_nome(nome)` que retorne apenas os clientes com aquele nome.
2. Adicione uma opção no menu para **remover um cliente pelo email**.
3. Crie um novo módulo MVC para **produtos** (reaproveitando a estrutura).
4. Substitua a `View` atual por uma interface de texto mais bonita (menus numerados, cabeçalhos, separadores).
5. Pesquise: como o MVC é usado em frameworks como **Django** e **Flask**?

---

## 💬 **8. Conclusão**

Nesta aula aprendemos:

* O que é o padrão **MVC** e por que ele é tão usado
* Como **separar responsabilidades** entre Model, View e Controller
* Que o **Controller** é o “cérebro” que conecta as outras partes
* Como isso melhora a **organização, manutenção e evolução** do código

---

## 🧩 **Tarefa para Casa**

1. Refaça o sistema de clientes no padrão MVC completo.
2. Crie um diagrama (pode ser à mão ou em ferramenta online) mostrando o fluxo entre Model, View e Controller.

