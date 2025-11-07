from models.cliente import Cliente
from dao.cliente_dao import ClienteDAO

dao = ClienteDAO()

while True:
    print("\n1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        cliente = Cliente(nome, email)
        dao.salvar(cliente)
        print("✅ Cliente cadastrado!")
    elif opcao == "2":
        clientes = dao.listar()
        for c in clientes:
            print(c)
    elif opcao == "3":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")
