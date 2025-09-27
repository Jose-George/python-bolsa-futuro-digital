from operations.adicao import Adicao

class Calculadora:
    """Classe principal da calculadora orientada a objetos."""

    def __init__(self):
        self.operacoes = {
            "soma": Adicao()
        }

    def calcular(self, operacao: str, numero01: float, numero02: float) -> float:
        if operacao not in self.operacoes:
            raise ValueError(f"Operação '{operacao}' não suportada.")
        return self.operacoes[operacao].executar(numero01, numero02)