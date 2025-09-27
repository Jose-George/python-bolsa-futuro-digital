class Pato:
    def fazer_som(self):
        print("Quack!")

class Pessoa:
    def fazer_som(self):
        print("Olá!")

class Fluminense:
  def fazer_som(self): 
      print("qualuer coisa")

def reproduzir_som(objeto):
    objeto.fazer_som()  # Não importa a classe

pato = Pato()
pessoa = Pessoa()
time = Fluminense()

for o in (pato, pessoa, time):
    reproduzir_som(o)