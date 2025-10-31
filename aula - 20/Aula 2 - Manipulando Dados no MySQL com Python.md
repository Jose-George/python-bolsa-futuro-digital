# 🐍 Aula 2 — Manipulando Dados no MySQL com Python

Turma: Iniciantes em Programação  
Objetivo: Aprender a **inserir, atualizar e excluir** dados do banco via Python.

---

## 🧭 Relembrando a aula anterior

Na última aula aprendemos a:

✅ Conectar o Python ao MySQL  
✅ Ler dados com `SELECT`  
✅ Exibir no console uma lista de clientes

Hoje vamos **manipular os dados** diretamente pelo Python.

---

## 🎯 Objetivos da aula

1. Revisar a conexão com o banco  
2. Criar métodos para:
   - Inserir um cliente (`INSERT`)
   - Atualizar telefone (`UPDATE`)
   - Remover um cliente (`DELETE`)
3. Tratar erros e confirmar ações  
4. Praticar com exercícios guiados

---

## 🧱 Estrutura do projeto (mesma da aula anterior)

```

project/
├─ app/
│   ├─ **init**.py
│   ├─ db.py
│   ├─ cliente_repo.py
│   └─ main.py
├─ .env
└─ requirements.txt

````

> Nenhuma mudança estrutural — só adicionaremos novos métodos.

---

## 🧾 Relembrando o método `criar()`

```python
def criar(self, nome, email, telefone):
    sql = """
    INSERT INTO cliente (nome, email, telefone)
    VALUES (%s, %s, %s)
    """
    conn = self.db.get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, (nome, email, telefone))
    conn.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return novo_id
````

✅ **Resumo:** insere um cliente e retorna o `id` criado.

---

## ✏️ Atualizando um cliente

Agora vamos criar o método `atualizar_telefone(id, novo_telefone)`:

```python
def atualizar_telefone(self, id, novo_telefone):
    sql = "UPDATE cliente SET telefone = %s WHERE id = %s"
    conn = self.db.get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, (novo_telefone, id))
    conn.commit()
    linhas = cursor.rowcount  # quantas linhas foram afetadas
    cursor.close()
    conn.close()
    return linhas
```

🟢 **Explicação didática:**

* `rowcount` mostra se o registro foi alterado (1 = sucesso, 0 = não encontrado).
* Sempre dar `commit()` após `UPDATE`.

---

## 🗑️ Removendo um cliente

Criar o método `remover(id)`:

```python
def remover(self, id):
    sql = "DELETE FROM cliente WHERE id = %s"
    conn = self.db.get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
    linhas = cursor.rowcount
    cursor.close()
    conn.close()
    return linhas
```

💡 Dica: use `(id,)` com vírgula — é uma tupla com um único valor.
Retorna quantas linhas foram excluídas.

---

## 🧪 Testando no `main.py`

```python
from app.db import Database
from app.cliente_repo import ClienteRepository

def main():
    db = Database()
    repo = ClienteRepository(db)

    # ✅ Criar cliente
    novo_id = repo.criar("Carlos Lima", "carlos.lima@example.com", "81988887777")
    print(f"Novo cliente criado com ID: {novo_id}")

    # ✏️ Atualizar telefone
    linhas = repo.atualizar_telefone(novo_id, "81999998888")
    if linhas:
        print(f"Telefone do cliente {novo_id} atualizado com sucesso!")
    
    # 🗑️ Remover cliente
    remover = input(f"Deseja remover o cliente {novo_id}? (s/n) ").lower()
    if remover == "s":
        repo.remover(novo_id)
        print(f"Cliente {novo_id} removido do banco!")

if __name__ == "__main__":
    main()
```

---

## ⚠️ Erros comuns e soluções

| Erro                              | Motivo                      | Solução                       |
| --------------------------------- | --------------------------- | ----------------------------- |
| `IntegrityError`                  | Email duplicado             | Use um email diferente        |
| `TypeError: not enough arguments` | Faltou a vírgula em `(id,)` | Corrigir o tuple              |
| `rowcount = 0`                    | ID não encontrado           | Verifique se o cliente existe |
| `ProgrammingError`                | Query mal formatada         | Revise a string SQL           |

---

## 💡 Boas práticas

✅ Sempre fechar `cursor` e `conn`
✅ Usar parâmetros (`%s`) — **nunca concatenar strings SQL**
✅ Fazer `commit()` após alterações
✅ Mostrar mensagens claras no terminal
✅ Usar `try/except` para capturar erros (nas próximas aulas)

---

## 🧠 Exercícios práticos (6)

1. **Buscar por ID** — crie um método `buscar_por_id(id)` que retorna o cliente
2. **Contar clientes** — crie um método `contar()` que retorna o total de registros
3. **Desafio bônus** — peça confirmação antes de excluir (`input("Confirma exclusão?")`)


