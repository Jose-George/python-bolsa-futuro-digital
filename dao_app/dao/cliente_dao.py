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