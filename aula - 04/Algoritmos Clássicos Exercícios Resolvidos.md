
## 1. O que é um algoritmo?

Um algoritmo é uma sequência de passos bem definidos para resolver um problema.  
Na programação, escrevemos algoritmos em código para que o computador execute.

---

## 2. Busca Linear em Lista

### Exemplo: Procurar número
```python
def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

numeros = [10, 20, 30, 40, 50]
print(busca_linear(numeros, 30))  # Saída: 2
print(busca_linear(numeros, 100)) # Saída: -1
````

---

## 3. Algoritmos de Ordenação

### Bubble Sort

```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
```

---

## 4. Recursão

### Fatorial

```python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5))  # Saída: 120
```

---

## 5. Exercícios Resolvidos 📝

### 1. Busca linear para verificar se um número existe

```python
def existe(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False

numeros = [3, 7, 9, 2, 5]
print(existe(numeros, 7))  # True
print(existe(numeros, 10)) # False
```

---

### 2. Busca linear que conta quantas vezes o valor aparece

```python
def contar_ocorrencias(lista, valor):
    cont = 0
    for item in lista:
        if item == valor:
            cont += 1
    return cont

lista = [1, 2, 3, 2, 4, 2, 5]
print(contar_ocorrencias(lista, 2))  # Saída: 3
```

---

### 3. Bubble Sort em ordem decrescente

```python
def bubble_sort_decrescente(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1]:  # só inverte o sinal
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

print(bubble_sort_decrescente([5, 1, 4, 2, 8]))  
# Saída: [8, 5, 4, 2, 1]
```

---

### 4. Ordenar nomes em ordem alfabética inversa

```python
nomes = ["Carlos", "Ana", "Bruno", "Diana"]
nomes.sort(reverse=True)
print(nomes)  # Saída: ['Diana', 'Carlos', 'Bruno', 'Ana']
```

---

### 5. Função recursiva para potência

```python
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

print(potencia(2, 3))  # Saída: 8
```

---

### 6. Função recursiva que conta elementos de uma lista

```python
def contar_elementos(lista):
    if lista == []:
        return 0
    else:
        return 1 + contar_elementos(lista[1:])

print(contar_elementos([10, 20, 30, 40]))  # Saída: 4
```

---

### 7. Programa interativo com lista de números

```python
# Lê 5 números do usuário
numeros = []
for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

print("Lista original:", numeros)
print("Lista ordenada com sort():", sorted(numeros))

# Busca linear
valor = int(input("Digite um número para buscar: "))
if existe(numeros, valor):
    print("O número está na lista!")
else:
    print("O número não está na lista!")
```

---

### 8. Função recursiva que soma os dígitos de um número

```python
def soma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + soma_digitos(n // 10)

print(soma_digitos(123))  # Saída: 6
```

---

### 9. Fibonacci iterativo e recursivo

#### Recursivo

```python
def fibonacci_rec(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

for i in range(10):
    print(fibonacci_rec(i), end=" ")
```

#### Iterativo

```python
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci_iter(10)
```

---

### 10. Desafio 🎯

```python
def programa_completo():
    lista = []
    qtd = int(input("Quantos números deseja inserir? "))
    for i in range(qtd):
        n = int(input(f"Digite o {i+1}º número: "))
        lista.append(n)

    print("\nLista original:", lista)
    print("Lista ordenada:", sorted(lista))

    valor = int(input("\nDigite um valor para buscar na lista: "))
    if existe(lista, valor):
        print(f"O número {valor} está na lista!")
        print(f"Fatorial de {valor} é {fatorial(valor)}")
    else:
        print(f"O número {valor} não está na lista.")

programa_completo()
```

---

