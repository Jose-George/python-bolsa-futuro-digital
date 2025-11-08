from models.cliente import Cliente
from database.connection import DatabaseConnection

class ClienteDAO:
    def __init__(self):
        self._criar_tabela()

    def _criar_tabela(self):
        with DatabaseConnection() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')

    def salvar(self, cliente: Cliente):
        with DatabaseConnection() as cursor:
            cursor.execute(
                'INSERT INTO cliente (nome, email) VALUES (?, ?)',
                (cliente.nome, cliente.email)
            )

    def listar(self):
        with DatabaseConnection() as cursor:
            cursor.execute('SELECT nome, email FROM cliente')
            rows = cursor.fetchall()
            return [Cliente(nome, email) for nome, email in rows]
