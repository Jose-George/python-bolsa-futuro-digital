class ContaBancaria:
    taxa_transferencia = 0.5  # 💰 atributo de classe (taxa fixa)

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = float(saldo)  # 🔒 encapsulado com _
        self.historico = []

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("❌ Valor de depósito deve ser positivo")
        self._saldo += valor
        self.historico.append(f"📥 Depósito: +{valor}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("❌ Valor de saque deve ser positivo")
        if valor > self._saldo:
            raise ValueError("❌ Saldo insuficiente")
        self._saldo -= valor
        self.historico.append(f"📤 Saque: -{valor}")

    def transferir_para(self, outra_conta, valor):
        total = valor + ContaBancaria.taxa_transferencia
        if self._saldo < total:
            raise ValueError("❌ Saldo insuficiente para transferência e taxa")
        self._saldo -= total
        outra_conta._saldo += valor
        self.historico.append(f"🔄 Transferência: -{valor} (taxa {ContaBancaria.taxa_transferencia})")