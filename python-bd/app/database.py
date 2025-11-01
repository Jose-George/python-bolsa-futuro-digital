import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()  

DB_PATH = os.getenv("DB_PATH", "escola_demo.db")

class Database:

    def __init__(self, path: str = None):
        self.path = path or DB_PATH

    def get_connection(self):
        conn = sqlite3.connect(self.path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conn.row_factory = sqlite3.Row
        return conn