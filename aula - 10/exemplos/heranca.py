
class Animal:
    def __init__(self, nome, especie, cor):
        self.nome = nome
        self.especie = especie
        self.__cor = cor

    @property
    def cor(self): 
        return self.__cor

    def fazer_som(self):
        print("Algum som genérico")

class Gato(Animal): 
    def __init__(self, escalar, nome, especie, cor):
        self.escalar = escalar
        super().__init__(nome, especie, cor)

    def fazer_som(self):
        print("Miau") 
        
class Cachorro(Animal): 
    def __init__(self, invadir_lixo, nome, especie, cor):
        self.invadir_lixo = invadir_lixo 
        super().__init__(nome, especie, cor)

    def fazer_som(self):
        print("Latido")

class GatoCachorro(Gato, Cachorro): 
    def __init__(self, escalar, invadir_lixo, nome, especie, cor):
        self.escalar = escalar
        self.invadir_lixo = invadir_lixo 
        super().__init__(nome, especie, cor)

    def fazer_som(self):
        print("Miau e Latido")

#gato = Animal("Whiskers", "Gato")
#gato.fazer_som()  

#cachorro = Animal("Rex", "Cachorro")
#cachorro.fazer_som()


gato = Gato(True, "Whiskers", "Gato", "amarelo")
gato.fazer_som()


print("-----")

cachorro = Cachorro(False, "Rex", "Cachorro", "preto")
cachorro.fazer_som()


animal = Animal("Bicho", "Desconhecido", "Cinza")

print(animal.cor)
