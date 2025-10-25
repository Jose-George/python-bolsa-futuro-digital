# 🐍 Python → MySQL 

Objetivo: conectar, executar consulta simples e exibir resultados.

---

## ✅ O que vamos ver hoje

1. Pré-requisitos e instalação  
2. Criar banco/tabela de exemplo (SQL)  
3. Arquivos mínimos do projeto  
4. Conectar com `mysql-connector-python` (classe simples)  
5. Exemplo: listar clientes e mostrar no console  
6. Passo a passo para apresentação  
7. Exercícios práticos (6)

---

## 🧰 Pré-requisitos

- Python 3.8+ instalado  
- MySQL instalado localmente (ou via container)  
- Conhecimento básico de classes e funções (OOP)  
- No terminal, crie e ative um virtualenv (recomendado)

Instalar dependência:
```bash
pip install mysql-connector-python python-dotenv
````

---

## 🗃️ SQL: criar banco e tabela (execute no MySQL)

```sql
CREATE DATABASE escola_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE escola_demo;

CREATE TABLE cliente (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  telefone VARCHAR(20),
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO cliente (nome, email, telefone) VALUES
('Maria Silva', 'maria.silva@example.com', '11988881234'),
('João Souza', 'joao.souza@example.com', '21999992345');
```

---

## 📁 Estrutura mínima do projeto

```
project/
 ├─ app/
 │   ├─ db.py
 │   ├─ cliente_repo.py
 │   └─ main.py
 ├─ .env
 └─ requirements.txt
```

---

## 🔑 Arquivo `.env` (NUNCA comitar)

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASS=suasenha
DB_NAME=escola_demo
```

Adicione `.env` ao `.gitignore`.

---

## 🧱 `db.py` — classe simples de conexão

```python
# app/db.py
from mysql import connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", ""),
    "database": os.getenv("DB_NAME", "escola_demo"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "charset": "utf8mb4"
}

class Database:
    """Classe simples que abre/fecha conexão."""
    def get_connection(self):
        return connector.connect(**DB_CONFIG)
```

---

## 🧾 `cliente_repo.py` — função para listar clientes

```python
# app/cliente_repo.py
from app.db import Database

class ClienteRepository:
    def __init__(self, db: Database):
        self.db = db

    def listar_todos(self):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente ORDER BY criado_em DESC"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        finally:
            conn.close()
```

---

## 🖥️ `main.py` — exemplo simples que mostra a lista

```python
# app/main.py
from app.db import Database
from app.cliente_repo import ClienteRepository

def main():
    db = Database()
    repo = ClienteRepository(db)

    clientes = repo.listar_todos()
    print("=== Clientes cadastrados ===")
    for c in clientes:
        print(f"{c['id']}: {c['nome']} — {c['email']} — {c['telefone']} — {c['criado_em']}")

if __name__ == "__main__":
    main()
```

---

## 💡 Observações importantes (breve)

* Use parâmetros em queries quando for inserir/atualizar (aula futura).
* Fechar cursor e conexão é obrigatório — aqui fazemos manualmente.
* `.env` mantém credenciais fora do código.

---

## 🧪 Exercícios para a turma (6)

1. **Conectar e listar** — Execute o projeto e mostre a lista de clientes no console.
2. **Adicionar insert simples** — Crie um método `criar(nome, email, telefone)` no `ClienteRepository` que insere um cliente e retorna o id criado. Teste no `main.py`.
3. **Buscar por ID** — Implemente `buscar_por_id(id)` e exiba os dados do cliente solicitado. Trate o caso em que o id não existe.
4. **Atualizar telefone** — Implemente `atualizar_telefone(id, telefone)` que modifica apenas o campo `telefone`. Verifique se `rowcount` > 0.
5. **Remover cliente** — Implemente `remover(id)` que deleta um cliente. No `main.py` peça confirmação antes de remover (`S/N`).
6. **Tratar erro de conexão** — Simule erro (ex.: coloque senha errada no `.env`) e implemente um tratamento que exiba uma mensagem amigável, sem crashar o programa.
