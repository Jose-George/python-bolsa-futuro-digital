from collections import Counter
#interpolar - inserir variaveis dentro de strings
#refatorar - reescrever o codigo para ficar mais simples e legivel

frase = input("Digite uma frase: ")

palavras = frase.split()

dicionario_de_palavras = Counter(palavras)

print("Contagem de palavras ")

for palavra, qtd in dicionario_de_palavras.items(): 
  print(f"{palavra}: {qtd}")







