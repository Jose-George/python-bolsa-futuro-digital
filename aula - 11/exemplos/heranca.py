
#classe pai -> superclasse
class Veiculo: 
  def __init__(self, marca, modelo, ano):
    self.marca = marca 
    self.modelo = modelo 
    self.ano = ano 
    self.ligado = False

  def ligar(self): 
    self.ligado = True
    print(f"{self.marca} {self.modelo} {self.ano} está ligado")
  
  def desligar(self): 
    self.ligado = False
    print(f"{self.marca} {self.modelo} {self.ano} está desligado")

  def informacao(self): 
    return(f"{self.marca} - {self.modelo} - {self.ano} - {self.ligado}")

#classe filha ou subclasse
class Carro(Veiculo):
  def __init__(self, marca, modelo, ano, portas):
    super().__init__(marca, modelo, ano)
    self.portas = portas

  def informacao_portas(self):
    return(f"O carro possui {self.portas}")

  def informacao(self):
    return (f"Carro - " + super().informacao() + " qtd de portas: "+ self.informacao_portas())

class Onibus(Veiculo): 
  def __init__(self, marca, modelo, ano, roleta):
    super().__init__(marca, modelo, ano)
    self.roleta = roleta
  
  def informacao_roleta(self):
    print(f"A roleta do onibus: {self.portas}")
  
  def informacao(self):
    return (f"Onibus - " + super().informacao() + " Estado da roleta: "+ self.roleta)


meu_carro = Carro("honda","civic", "2022", "4")
meu_onibus = Onibus("marcopolo wv", "urbano", "2025", "operacional")

meu_carro.ligar()
meu_onibus.ligar()

print(meu_carro.informacao())
print(meu_onibus.informacao())