
#idade = 10
#nome = "George"
#eh_professor = False
#dinheiro = 100.50

#lista = [1, 2, 3, 4, 5]
#lista2 = ["a", "b", "c", "d"]

#print(f"O {nome} tem {idade} anos.")

class Celular:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.modelo = modelo

    def get_marca(self):
        return self.__marca
    
class Pessoa:
    def __init__(self, nome, idade, telefone: Celular):
        self.__nome = nome
        self.__idade = idade
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def usar_celular(self, celular):
        print(f"{self.__nome} está usando o celular {celular.get_marca()} {celular.modelo}")

    def get_telefone(self):
        return self.__telefone

  

telefone = Celular("Samsung", "Galaxy S10")
pessoa = Pessoa("George", 10, telefone)

print(f"O {pessoa.get_nome()} tem {pessoa.get_idade()} anos e seu celular é um {pessoa.get_telefone().get_marca()} {pessoa.get_telefone().modelo}.")