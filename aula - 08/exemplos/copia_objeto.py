
import copy 

lista1 = [[1, 2], [3, 4]]

copia_rasa = copy.copy(lista1)  # Cópia rasa (shallow copy)

copia_rasa[0][0] = 'X'  # Modificando um elemento interno da cópia rasa

print("Lista original:", lista1)
print("Cópia rasa:", copia_rasa)


copia_profunda = copy.deepcopy(lista1)  # Cópia profunda (deep copy)
copia_profunda[0][0] = 'Y'  # Modificando um elemento interno da cópia profunda
print("Lista profunda:", copia_profunda)


lista2 = lista1

print("Lista 2:", lista2)
lista2[0][0] = 'Z'  # Modificando um elemento interno da lis
print("Lista 2 após modificação:", lista2)
print("Lista original após modificação via lista2:", lista1)

