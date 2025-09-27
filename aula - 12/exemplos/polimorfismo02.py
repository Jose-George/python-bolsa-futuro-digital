
print(3 + 5)          # soma numérica
print("Hello " + "World")  # concatenação de strings
print([1, 2] + [3, 4])     # junção de listas


class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __repr__(self):
        return f"Vetor({self.x}, {self.y})"

v1 = Vetor(1, 2)
v2 = Vetor(3, 4)
print(v1 + v2)  # Vetor(4, 6)