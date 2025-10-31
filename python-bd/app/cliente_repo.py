from database import Database

class ClienteRepository:
    def __init__(self, database: Database):
        self.db = database

    def listar_todos(self):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return [dict(row) for row in resultados]

    def criar(self, nome, email, telefone):
        sql = """
        INSERT INTO cliente (nome, email, telefone)
        VALUES (?, ?, ?)
        """
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (nome, email, telefone))
        conn.commit()
        novo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return novo_id

    def atualizar_telefone(self, id, novo_telefone):
        sql = "UPDATE cliente SET telefone = ? WHERE id = ?"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (novo_telefone, id))
        conn.commit()
        linhas = cursor.rowcount  # quantas linhas foram afetadas
        cursor.close()
        conn.close()
        return linhas

        