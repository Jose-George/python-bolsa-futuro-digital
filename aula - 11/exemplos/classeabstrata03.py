
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Pagando R${valor} com cartão de crédito.")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Gerando boleto de R${valor}.")

class Pix(Pagamento):
    def processar(self, valor):
        print(f"Pagamento PIX: R${valor}.")


def executar_pagamento(pagamento: Pagamento, valor):
    pagamento.processar(valor)

pagamentos = [CartaoCredito(), Boleto(), Pix()]
for pagamento in pagamentos:
    executar_pagamento(pagamento, 150)