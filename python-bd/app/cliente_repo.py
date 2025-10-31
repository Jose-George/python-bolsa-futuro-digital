from database import Database

class ClienteRepository:
    def __init__(self, database: Database):
        self.database = database

    def listar_todos(self):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente"
        conn = self.database.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
