from database import Database
from cliente_repo import ClienteRepository

import os
import sqlite3

def ensure_schema(db_path: str):
    """Cria o banco/tabela caso não exista (útil para aula/exemplos)."""
    need_create = not os.path.exists(db_path)
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        if need_create:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                telefone TEXT,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
            # inserir alguns dados exemplo (se desejar)
            cur.execute("INSERT INTO cliente (nome, email, telefone) VALUES (?, ?, ?)",
                        ("Maria Silva", "maria.silva@example.com", "11988881234"))
            cur.execute("INSERT INTO cliente (nome, email, telefone) VALUES (?, ?, ?)",
                        ("João Souza", "joao.souza@example.com", "21999992345"))
            conn.commit()
    finally:
        conn.close()

def main():
    db = Database()  # usa DB_PATH do .env ou escola_demo.db
    # cria esquema/dados iniciais se necessário (apenas para facilitar a aula)
    ensure_schema(db.path)

    repo = ClienteRepository(db)

    print("=== Lista inicial de clientes ===")
    for c in repo.listar_todos():
        print(f"{c['id']} - {c['nome']} ({c['email']})")

    # Inserir novo cliente
    #novo_id = repo.criar("Ana Pereira", "ana.pereira@example.com", "31988887777")
    #print(f"\nNovo cliente criado com ID: {novo_id}")

    # Atualizar por id
    #id_modificado = repo.atualizar_telefone(novo_id, "31988887778")
    #print("\Telefone atualizado:", id_modificado)

if __name__ == "__main__":
    main()