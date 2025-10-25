from db import Database

class ClienteRepository:
    def __init__(self, db: Database):
        self.db = db

    def listar_todos(self):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente"
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
