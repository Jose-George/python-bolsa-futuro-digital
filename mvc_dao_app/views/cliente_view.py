class ClienteView:
    def menu(self):
        print("\n==== MENU CLIENTES ====")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Sair")
        return input("Escolha: ")

    def solicitar_dados(self):
        nome = input("Nome: ")
        email = input("Email: ")
        return nome, email

    def mostrar_mensagem(self, msg):
        print(msg)

    def mostrar_clientes(self, clientes):
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print("\n=== Lista de Clientes ===")
            for c in clientes:
                print("-", c)
