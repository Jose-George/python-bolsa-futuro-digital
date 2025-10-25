from db import Database
from cliente_repo import ClienteRepository

def main():
    db = Database()
    repo = ClienteRepository(db)

    clientes = repo.listar_todos()
    print("=== Clientes cadastrados ===")
    for c in clientes:
        print(f"{c['id']} - {c['nome']} ({c['email']})")

if __name__ == "__main__":
    main()
