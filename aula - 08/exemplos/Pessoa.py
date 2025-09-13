class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo privado
        self.idade = idade  # Atributo privado


p1 = Pessoa("João", 30)
p2 = Pessoa("Maria", 25)

print(p1.nome)
print(p2.idade)