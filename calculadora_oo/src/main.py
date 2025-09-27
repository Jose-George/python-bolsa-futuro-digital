
from models.calculadora import Calculadora

def main():
    calc = Calculadora()
    print("Calculadora OO")
    numero01 = float(input("Digite o primeiro número: "))
    numero02 = float(input("Digite o segundo número: "))
    operacao = input("Escolha (soma, subtracao, multiplicacao, divisao): ").lower()
    resultado = calc.calcular(operacao, numero01, numero02)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()