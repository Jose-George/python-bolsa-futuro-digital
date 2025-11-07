# 🧠 Aula — **Padrões de Desenvolvimento de Software (Introdução)**

**Turma:** Python Intermediário – Softex PB

**Tema:** Boas práticas e padrões que tornam o código mais limpo, reutilizável e fácil de manter.

---

## 🎯 **Objetivos da Aula**

Ao final desta aula, o aluno será capaz de:

* Entender o que são **padrões de desenvolvimento de software**
* Identificar **boas práticas** que melhoram a qualidade do código
* Reconhecer e aplicar **padrões simples** em Python
* Utilizar o **padrão DAO** (Data Access Object) para organizar código com banco de dados

---

## 🧩 **1. O que são Padrões de Desenvolvimento?**

Padrões de desenvolvimento são **soluções reutilizáveis** para problemas comuns que surgem no desenvolvimento de software.

> 💡 Eles não são regras fixas, mas **boas práticas testadas** por desenvolvedores ao longo do tempo.

### Exemplo:

Quando você separa o código em **funções**, **classes** e **módulos**, está aplicando padrões como **modularização** e **separação de responsabilidades**.

---

## 🧱 **2. Boas Práticas Fundamentais**

| Padrão / Princípio                        | Descrição                                        | Exemplo                                 |
| ----------------------------------------- | ------------------------------------------------ | --------------------------------------- |
| **DRY** (Don’t Repeat Yourself)           | Evite duplicar código                            | Crie funções reutilizáveis              |
| **KISS** (Keep It Simple, Stupid)         | Mantenha o código simples e direto               | Evite soluções complexas                |
| **SRP** (Single Responsibility Principle) | Cada classe deve ter apenas uma responsabilidade | Classe `ClienteDAO` só cuida do banco   |
| **Encapsulamento**                        | Protege os dados e esconde detalhes internos     | Atributos privados e getters/setters    |
| **Separação de camadas**                  | Divide o sistema em partes independentes         | Ex: camada de dados, lógica e interface |

---

## 🧮 **3. Estruturando um Projeto Simples**

Vamos imaginar um pequeno sistema de **cadastro de clientes**.
Sem padrão, o código costuma ficar **tudo junto**:

```python
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)')

nome = input("Nome: ")
email = input("Email: ")

cursor.execute('INSERT INTO cliente (nome, email) VALUES (?, ?)', (nome, email))
conn.commit()
conn.close()
```

Funciona, mas é **difícil de manter** — tudo está misturado:

* lógica de negócio
* interação com o usuário
* manipulação de banco

---

## 🧠 **4. Aplicando o Padrão DAO (Data Access Object)**

O padrão **DAO** separa o código que acessa o banco de dados do restante da aplicação.

### 🔹 Estrutura do Projeto

```
/meu_app
│
├── dao/
│   └── cliente_dao.py
│
├── models/
│   └── cliente.py
│
└── main.py
```

---

### 📄 **models/cliente.py**

```python
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.nome} ({self.email})"
```

---

### 📄 **dao/cliente_dao.py**

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
            cursor.execute('INSERT INTO cliente (nome, email) VALUES (?, ?)',
                           (cliente.nome, cliente.email))
            conn.commit()

    def listar(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT nome, email FROM cliente')
            rows = cursor.fetchall()
            return [Cliente(nome, email) for nome, email in rows]
```

---

### 📄 **main.py**

```python
from models.cliente import Cliente
from dao.cliente_dao import ClienteDAO

dao = ClienteDAO()

while True:
    print("\n1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        cliente = Cliente(nome, email)
        dao.salvar(cliente)
        print("✅ Cliente cadastrado!")
    elif opcao == "2":
        clientes = dao.listar()
        for c in clientes:
            print(c)
    elif opcao == "3":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")
```

---

## 🧰 **5. O que Melhorou com o Padrão DAO**

| Antes                      | Depois                                                  |
| -------------------------- | ------------------------------------------------------- |
| Código confuso e misturado | Código organizado por responsabilidade                  |
| Dificuldade de manutenção  | Fácil de alterar o banco ou adicionar novas operações   |
| Repetição de código SQL    | Centralização das operações no DAO                      |
| Pouca reutilização         | DAO e classes podem ser reutilizados em outros projetos |

---

## 💬 **6. Outros Padrões que Você Verá Mais Adiante**

| Padrão                          | Descrição                                         |
| ------------------------------- | ------------------------------------------------- |
| **MVC (Model-View-Controller)** | Divide a aplicação em modelo, visão e controle    |
| **Repository**                  | Abstrai o acesso aos dados, semelhante ao DAO     |
| **Factory Method**              | Cria objetos de forma padronizada                 |
| **Singleton**                   | Garante que só exista uma instância de uma classe |
| **Observer**                    | Permite que objetos "observem" eventos em outros  |

---

## 🧩 **7. Exercícios Práticos**

1. Adapte o código para incluir o campo **telefone** no cadastro de cliente.
2. Crie uma classe `Produto` e um `ProdutoDAO` seguindo o mesmo padrão.
3. No `main.py`, adicione uma opção para listar **clientes e produtos**.
4. Tente mover a lógica do menu para uma função separada (aplicando SRP).
5. Reflita: o que aconteceria se você quisesse trocar o SQLite por MySQL?
   → Com o padrão DAO, bastaria alterar uma única camada!

---

## 🧭 **Conclusão**

Nesta aula aprendemos que:

* Padrões de desenvolvimento **tornam o código mais profissional**
* Separar responsabilidades evita confusão e facilita a manutenção
* O padrão **DAO** é ideal para organizar o acesso ao banco de dados
* Esses princípios são a base para frameworks maiores (como Django e Flask)

---

## 🧩 **Tarefa para Casa**

Pesquise sobre o padrão **MVC** e escreva um pequeno resumo (5 linhas) explicando:

* O que é o padrão
* Onde ele é usado
* Como ele se relaciona com o que aprendemos hoje

