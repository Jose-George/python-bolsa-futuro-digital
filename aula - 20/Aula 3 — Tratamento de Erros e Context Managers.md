# 🧠 Aula 3 — Tratamento de Erros e Context Managers

Turma: Softex PB - Iniciantes em Programação  
Tema: Tornando o código Python + MySQL mais **seguro e limpo**

---

## 📘 Revisão da Aula 2

Na última aula aprendemos a:

✅ Inserir (`INSERT`)  
✅ Atualizar (`UPDATE`)  
✅ Excluir (`DELETE`)  
✅ Confirmar ações e commits  

👉 Agora vamos deixar o código **mais robusto e profissional.**

---

## 🎯 Objetivos da Aula

1. Compreender o uso de `try / except`  
2. Tratar erros de conexão e execução SQL  
3. Entender o conceito de **context manager (`with`)**  
4. Aplicar boas práticas de fechamento automático da conexão

---

## ⚠️ Por que tratar erros?

Ao lidar com banco de dados, **erros são inevitáveis**:

- Banco desligado  
- Usuário ou senha incorretos  
- Query mal escrita  
- Campo duplicado (violação UNIQUE)  
- Problemas de rede  

Sem tratamento, o programa **quebra** e mostra mensagens feias para o usuário 😬

---

## 🧱 Estrutura básica do tratamento

```python
try:
    # código que pode dar erro
except TipoDeErro as e:
    # o que fazer se o erro acontecer
finally:
    # (opcional) sempre executa, com erro ou sem erro
````

---

## 🧩 Exemplo prático: conexão com erro

```python
from mysql import connector

try:
    conn = connector.connect(
        host="localhost",
        user="root",
        password="senha_errada",  # 💣 proposital
        database="escola_demo"
    )
    print("Conexão bem-sucedida!")
except connector.Error as e:
    print("❌ Erro de conexão:", e)
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Conexão encerrada com segurança.")
```

🟢 **Explicação:**

* `connector.Error` captura qualquer erro do MySQL.
* `finally` garante o fechamento da conexão, mesmo se houver falha.

---

## 💡 Por que isso é importante?

Sem `try/except`, o programa **para na primeira exceção**.
Com tratamento, podemos:

✅ Mostrar mensagens mais claras
✅ Continuar o programa sem travar
✅ Fazer log de erros (em aulas futuras)

---

## 🧱 Aplicando no repositório

Vamos refatorar o método `listar_todos()`:

```python
from mysql import connector

class ClienteRepository:
    def __init__(self, db):
        self.db = db

    def listar_todos(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM cliente")
            resultados = cursor.fetchall()
            return resultados
        except connector.Error as e:
            print("Erro ao buscar clientes:", e)
            return []
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()
```

🟢 **Explicação didática:**

* `finally` é o “limpador” — sempre fecha cursor e conexão.
* O `return []` evita crash caso o banco falhe.

---

## 🧰 Melhorando com Context Manager (`with`)

O Python tem um recurso que **automaticamente fecha recursos**: o `with`.

### Exemplo simples:

```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
# o arquivo já está fechado aqui ✅
```

---

## ⚙️ Usando `with` para conexão de banco

Podemos criar uma **classe utilitária** que implementa `__enter__` e `__exit__`, para ser usada com `with`.

```python
from mysql import connector
from app.db import DB_CONFIG

class Connection:
    def __enter__(self):
        self.conn = connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)
        return self.conn, self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
```

---

## 🧩 Usando o `with` na prática

```python
from app.connection import Connection

def listar_clientes():
    with Connection() as (conn, cursor):
        cursor.execute("SELECT * FROM cliente")
        return cursor.fetchall()
```

✅ O `with` fecha automaticamente a conexão.
✅ Menos código repetido.
✅ Mais difícil de esquecer o `close()`.

---


## ⚠️ Erros comuns e soluções

| Erro                         | Causa                             | Solução                              |
| ---------------------------- | --------------------------------- | ------------------------------------ |
| `AttributeError: 'NoneType'` | Tentou usar `cursor` sem conexão  | Verificar se `conn` foi criada       |
| `Access denied`              | Usuário/senha incorretos          | Corrigir `.env`                      |
| `__enter__` não chamado      | Classe não tem método `__enter__` | Implementar `__enter__` corretamente |
| MySQL parado                 | Servidor desligado                | Reiniciar MySQL antes do teste       |

---

## 💡 Boas práticas apresentadas

✅ Sempre fechar conexão (`finally` ou `with`)
✅ Tratar erros de forma clara
✅ Nunca deixar o código travar sem feedback
✅ Preparar o código para o “mundo real” (falhas acontecem)

---

## 🧪 Exercícios da Aula 3

1. Adapte o método `criar()` para usar o padrão `try/finally`.
2. Crie um método `buscar_por_email(email)` com tratamento de erro.
3. Implemente a classe `Connection` e use `with` no método `listar_todos()`.
4. Desafio bônus 💥 — combine `try/except` e `with` no mesmo método!

---

## 🧠 Conclusão

Hoje aprendemos a:

✅ Tratar erros com `try / except`
✅ Usar `finally` para garantir limpeza
✅ Aplicar `with` para automatizar fechamento
✅ Tornar o código mais seguro e profissional

📘 Próxima aula:
👉 **Parâmetros, transações e boas práticas de segurança (SQL Injection).**

