
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro: 
    def __init__(self, marca, modelo, potencia):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(potencia*2)

    def get_motor(self):
        return self.motor

carro = Carro("Ford", "Ka", 2)


print(f"O carro é um {carro.marca} {carro.modelo} com motor de {carro.get_motor().potencia} cavalos.")
