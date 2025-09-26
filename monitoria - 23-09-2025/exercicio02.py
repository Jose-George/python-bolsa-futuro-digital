
compras = []

while True:
  item = input("Digite o nome do item (ou 'fim' para encerrar): ")
  
  if item.lower() == 'fim':
    break

  compras.append(item)


print("A quantidade total de itens na lista de compras é:", len(compras))

for item in sorted(compras):
  print(" - ",item)

