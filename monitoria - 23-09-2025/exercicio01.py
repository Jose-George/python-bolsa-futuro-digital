
nome = input("Nome do aluno: ")

notas = []

for i in range(4):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

media = sum(notas)/len(notas) 

print(f"A média do aluno {nome} é {media:.2f}")

if media >= 7:
    print("Aluno aprovado")
else: 
    print("Aluno reprovado")