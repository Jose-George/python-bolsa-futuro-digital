# 🧑‍💻 Aula de Algoritmos Clássicos em Python para Iniciantes

Vamos aprender alguns dos algoritmos mais importantes e simples para praticar programação em Python.  

Nesta aula você verá:

1. **Busca linear e binária** em listas
2. **Algoritmos de ordenação simples**
   - Ordenação sem usar `sort()`
   - Ordenação usando `sort()` e `sorted()`
3. **Recursão** (quando uma função chama a si mesma)
4. Uma **lista de exercícios** para praticar

---

## 1. Busca Linear em Lista

A **busca linear** percorre a lista elemento por elemento, até encontrar o valor desejado (ou chegar ao final da lista).

### Exemplo 1: Procurar um número em uma lista
```python
def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  # Retorna a posição onde encontrou
    return -1  # Retorna -1 se não encontrou

# Testando
numeros = [10, 20, 30, 40, 50]
print(busca_linear(numeros, 30))  # Saída: 2
print(busca_linear(numeros, 100)) # Saída: -1
````

### Exemplo 2: Procurar um nome em uma lista de strings

```python
nomes = ["Ana", "Bruno", "Carlos", "Diana"]

pos = busca_linear(nomes, "Carlos")
print(pos)  # Saída: 2

pos = busca_linear(nomes, "Pedro")
print(pos)  # Saída: -1
```

### Exemplo 3: Encontrar **todos os índices** de um valor

```python
def busca_todos(lista, valor):
    indices = []
    for i in range(len(lista)):
        if lista[i] == valor:
            indices.append(i)
    return indices

lista = [1, 2, 3, 2, 4, 2, 5]
print(busca_todos(lista, 2))  # Saída: [1, 3, 5]
```

---

### 1.1. Busca Binária em Lista

A **busca binária** é mais eficiente que a busca linear, mas **só funciona em listas ordenadas**.
A ideia é dividir a lista ao meio e verificar em qual metade o valor pode estar, descartando a outra metade. O processo continua até encontrar o valor ou acabar a lista.

---

### Exemplo 1: Procurar um número em uma lista ordenada

```python
def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio  # Retorna a posição onde encontrou
        elif lista[meio] < valor:
            inicio = meio + 1  # Procura na metade direita
        else:
            fim = meio - 1  # Procura na metade esquerda
    return -1  # Retorna -1 se não encontrou

# Testando
numeros = [10, 20, 30, 40, 50]
print(busca_binaria(numeros, 30))  # Saída: 2
print(busca_binaria(numeros, 100)) # Saída: -1
```

---

### Exemplo 2: Procurar um nome em uma lista ordenada de strings

```python
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

pos = busca_binaria(nomes, "Carlos")
print(pos)  # Saída: 2

pos = busca_binaria(nomes, "Pedro")
print(pos)  # Saída: -1
```

---

### Exemplo 3: Versão recursiva da busca binária

```python
def busca_binaria_recursiva(lista, valor, inicio, fim):
    if inicio > fim:
        return -1  # Não encontrou

    meio = (inicio + fim) // 2

    if lista[meio] == valor:
        return meio
    elif lista[meio] < valor:
        return busca_binaria_recursiva(lista, valor, meio + 1, fim)
    else:
        return busca_binaria_recursiva(lista, valor, inicio, meio - 1)

# Testando
numeros = [10, 20, 30, 40, 50]
print(busca_binaria_recursiva(numeros, 40, 0, len(numeros)-1))  # Saída: 3
print(busca_binaria_recursiva(numeros, 15, 0, len(numeros)-1))  # Saída: -1
```

---


## 2. Algoritmos de Ordenação

### 🔹 Ordenação sem usar `sort()`

#### Exemplo 1: Bubble Sort (ordenar comparando vizinhos)

```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

valores = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(valores))  # Saída: [11, 12, 22, 25, 34, 64, 90]
```

#### Exemplo 2: Selection Sort (escolhe o menor e coloca na frente)

```python
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range(i+1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

valores = [29, 10, 14, 37, 13]
print(selection_sort(valores))  # Saída: [10, 13, 14, 29, 37]
```

---

### 🔹 Ordenação usando `sort()` ou `sorted()`

#### Exemplo 1: Usando `.sort()` (altera a lista original)

```python
numeros = [5, 3, 8, 6, 7, 2]
numeros.sort()
print(numeros)  # Saída: [2, 3, 5, 6, 7, 8]
```

#### Exemplo 2: Usando `sorted()` (não altera a lista original)

```python
numeros = [5, 3, 8, 6, 7, 2]
ordenada = sorted(numeros)
print("Original:", numeros)      # Saída: [5, 3, 8, 6, 7, 2]
print("Ordenada:", ordenada)     # Saída: [2, 3, 5, 6, 7, 8]
```

#### Exemplo 3: Ordenando strings

```python
nomes = ["Carlos", "Ana", "Bruno", "Diana"]
nomes.sort()
print(nomes)  # Saída: ['Ana', 'Bruno', 'Carlos', 'Diana']
```

#### Exemplo 4: Ordenar do **maior para o menor**

```python
numeros = [10, 40, 30, 20]
numeros.sort(reverse=True)
print(numeros)  # Saída: [40, 30, 20, 10]
```

---

## 3. Recursão

Um algoritmo recursivo é aquele em que **a função chama a si mesma**.
Mas atenção: sempre deve ter um **caso base** para evitar chamadas infinitas.

### Exemplo 1: Fatorial (n!)

```python
def fatorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5))  # Saída: 120
```

### Exemplo 2: Contagem regressiva

```python
def contagem_regressiva(n):
    if n == 0:
        print("🚀 Lançar foguete!")
    else:
        print(n)
        contagem_regressiva(n-1)

contagem_regressiva(5)
```

### Exemplo 3: Sequência de Fibonacci

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=" ")
# Saída: 0 1 1 2 3 5 8 13 21 34
```

### Exemplo 4: Soma de lista usando recursão

```python
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

print(soma_lista([1, 2, 3, 4, 5]))  # Saída: 15
```

---

## 5. Exercícios para Praticar 📝

Agora é sua vez! Resolva os exercícios abaixo.

1. Implemente a **busca linear** que diga **se o elemento existe ou não** em uma lista de números.
2. Modifique a busca linear para mostrar **quantas vezes** o valor aparece na lista.
3. Implemente o **Bubble Sort** em ordem **decrescente**.
4. Crie uma lista de nomes e ordene-os em ordem **alfabética inversa**.
5. Escreva uma função recursiva que calcule a **potência** (ex.: `2^3 = 8`).
6. Escreva uma função recursiva que conte quantos elementos existem em uma lista.
7. Crie um programa que pergunte ao usuário 5 números, salve em uma lista e:

   * Mostre a lista ordenada (usando `sort()` e `sorted()`)
   * Procure um número escolhido pelo usuário na lista usando **busca linear**
8. Crie uma função recursiva que some os dígitos de um número (ex.: `123 → 1+2+3 = 6`).
9. Implemente a sequência de Fibonacci de forma **iterativa** e compare com a recursiva.
10. Desafio 🎯: Crie um programa que peça uma lista de números ao usuário e:

    * Ordene a lista
    * Pergunte um valor e faça a busca linear
    * Mostre o fatorial desse número (se existir na lista)

---

## 🚀 Conclusão

* Você aprendeu a **buscar valores** em listas com busca linear.
* Viu como **ordenar listas** manualmente e com funções prontas.
* Descobriu o poder da **recursão** com exemplos clássicos como fatorial e Fibonacci.
* Agora é hora de praticar com os exercícios propostos!

---

💡 **Dica:** Quanto mais você praticar escrevendo código, mais vai entender a lógica dos algoritmos.
