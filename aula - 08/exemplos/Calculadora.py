class Calculadora: 
  def somar(self, valor1, valor2=0): 
    return valor1 + valor2
  
calc = Calculadora()
print(calc.somar(10, 5))
print(calc.somar(10))  # Usando o valor padrão para valor2