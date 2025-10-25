from mysql import connector
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME", "escola_demo"),
    "port": int(os.getenv("DB_PORT", 3306))
}

class Database:
    def get_connection(self):
        return connector.connect(**DB_CONFIG)
