class Carro: 
    def __init__(self, marca, modelo, ano, cor):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__velocidade = 0
        self.__cor = cor
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca  

    def acelerar(self, valor):
        self.__velocidade += valor

