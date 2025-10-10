import textwrap
from models.ContaCorrente import ContaCorrente
from models.PessoaFisica import PessoaFisica
from models.Deposito import Deposito
from models.Saque import Saque

def menu():
    menu = """\n
    ================ MENU ================
    
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [6]\tListar contas
    [7]\tSair
    
    ======================================

    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    transacao_valida(clientes, "Informe o valor do depósito: ", Deposito)
    # cpf = input("Informe o CPF do cliente: ")
    # cliente = filtrar_cliente(cpf, clientes)

    # if not cliente:
    #     print("\n@@@ Cliente não encontrado! @@@")
    #     return

    # valor = float(input("Informe o valor do depósito: "))
    # transacao = Deposito(valor)

    # conta = recuperar_conta_cliente(cliente)
    # if not conta:
    #     return

    # cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    transacao_valida(clientes, "Informe o valor do saque: ", Saque)
    # cpf = input("Informe o CPF do cliente: ")
    # cliente = filtrar_cliente(cpf, clientes)

    # if not cliente:
    #     print("\n@@@ Cliente não encontrado! @@@")
    #     return

    # valor = float(input("Informe o valor do saque: "))
    # transacao = Saque(valor)

    # conta = recuperar_conta_cliente(cliente)
    # if not conta:
    #     return

    # cliente.realizar_transacao(conta, transacao)

def transacao_valida(clientes, input_valor, valor_transacao):

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input(input_valor))
    transacao = valor_transacao(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n\t{transacao['data']}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    if (contas != []):
        for conta in contas:
          print("=" * 100)
          print(textwrap.dedent(str(conta)))
    else:
        print("\n=== Não existe conta! ===")        


def main():
    clientes = [] 
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            criar_cliente(clientes)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()


print("=== Obrigado por usar nosso sistema! ===")