import sqlite3

# Cria (ou conecta) ao banco de dados local
conn = sqlite3.connect("banco.db")

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria a tabela cliente (caso não exista)
cursor.execute("""
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT,
    telefone TEXT
);
""")

# Função para inserir um cliente
def criar_cliente(nome, email, telefone):
    cursor.execute(
        "INSERT INTO cliente (nome, email, telefone) VALUES (?, ?, ?)",
        (nome, email, telefone)
    )
    conn.commit()
    return cursor.lastrowid

# Função para buscar um cliente pelo ID
def find_cliente(cliente_id):
    cursor.execute("SELECT * FROM cliente WHERE id = ?", (cliente_id,))
    return cursor.fetchone()  # retorna uma tupla (id, nome, email, telefone)

# Exemplo de uso:
if __name__ == "__main__":
    # Inserindo um cliente
    novo_id = criar_cliente("Maria Silva", "maria@email.com", "99999-9999")
    print(f"Cliente criado com ID: {novo_id}")

    # Buscando o cliente inserido
    cliente = find_cliente(novo_id)
    print("Cliente encontrado:", cliente)

# Fecha a conexão
conn.close()
