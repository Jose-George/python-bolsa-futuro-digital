
from ContaBancaria import ContaBancaria

conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Bob", 500)

conta1.depositar(200)
conta1.sacar(150)
conta1.transferir_para(conta2, 300)
print(f"Saldo {conta1.titular}: {conta1.saldo}")
print(f"Saldo {conta2.titular}: {conta2.saldo}")

print("Histórico conta1:", conta1.historico)
print("Histórico conta2:", conta2.historico)