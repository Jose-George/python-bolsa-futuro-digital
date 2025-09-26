
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass

    def apresentar(self):
        print(f"Eu sou {self.nome}")


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

dog = Cachorro("Rex")
dog.apresentar()
dog.emitir_som()