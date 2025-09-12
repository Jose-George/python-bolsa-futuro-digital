
numero: int = 10
texto: str = "Olá, Mundo!"
decimal: float = 3.14
booleano: bool = True 

print(type(numero))


# print(numero)
# print(texto)
# print(decimal)
# print(booleano)

def minha_funcao(valor: int) -> str:
    valor: int = 20
    local = "texto qualquer"
    print(local + " e meu valor é: " + str(valor))
    return valor

# print("Chamando a função:" )
# minha_funcao()

#print(numero + texto)

numero = "texto"

# print(numero + " concatenado")

print(type(numero))


#print(type(minha_funcao(5)))