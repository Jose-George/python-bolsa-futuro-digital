
---

# 📘 Aula: Listas, Filas, Pilhas e Dicionários em Python

## 🎯 Objetivo da aula

* Entender o que são **listas**, **filas**, **pilhas** e **dicionários** em Python.
* Aprender como criar, acessar e manipular esses tipos de dados.
* Praticar com exemplos reais e exercícios.

---

## 1️⃣ Listas em Python

Uma **lista** é uma coleção ordenada de elementos. Você pode armazenar números, textos, booleanos e até outras listas dentro dela.

### 🔹 Criando listas

```python
# Lista de números
numeros = [10, 20, 30, 40]

# Lista de strings
nomes = ["Ana", "Bruno", "Carlos"]

# Lista mista
mistura = [1, "texto", True, 3.14]
````

### 🔹 Acessando elementos

```python
nomes = ["Ana", "Bruno", "Carlos"]

print(nomes[0])  # Ana (primeiro elemento)
print(nomes[2])  # Carlos (terceiro elemento)
```

### 🔹 Alterando valores

```python
nomes[1] = "Beatriz"
print(nomes)  # ["Ana", "Beatriz", "Carlos"]
```

### 🔹 Métodos úteis

```python
frutas = ["maçã", "banana", "uva"]

frutas.append("laranja")  # Adiciona no final
frutas.insert(1, "manga")  # Adiciona na posição 1
frutas.remove("uva")  # Remove um elemento
print(frutas)  # ['maçã', 'manga', 'banana', 'laranja']
```

---

## ✍️ Exercícios de Listas

1. Crie uma lista com 5 números e imprima o maior e o menor valor.
2. Crie uma lista de 5 nomes e troque o último pelo seu próprio nome.
3. Faça um programa que leia 5 notas e calcule a média delas.

---

## 2️⃣ Filas em Python

Uma **fila** segue a regra **FIFO (First In, First Out)** → o primeiro a entrar é o primeiro a sair.

### 🔹 Criando filas com listas

```python
fila = []

# Entrando na fila (append)
fila.append("João")
fila.append("Maria")
fila.append("Pedro")

print(fila)  # ["João", "Maria", "Pedro"]

# Saindo da fila (pop(0))
primeiro = fila.pop(0)
print(primeiro)  # João
print(fila)  # ["Maria", "Pedro"]
```

### 🔹 Usando `collections.deque` (mais eficiente)

```python
from collections import deque

fila = deque(["João", "Maria"])
fila.append("Pedro")  # entra na fila
print(fila)

fila.popleft()  # João sai da fila
print(fila)
```

---

## ✍️ Exercícios de Filas

1. Crie uma fila de atendimento de banco com 4 pessoas. Remova a primeira da fila e mostre quem ainda está aguardando.
2. Faça um programa onde o usuário digite 3 nomes para entrar na fila e depois remova todos, mostrando a ordem de saída.
3. Simule a fila de um parque de diversões com entrada e saída de pessoas.

---

## 3️⃣ Pilhas em Python

Uma **pilha** segue a regra **LIFO (Last In, First Out)** → o último a entrar é o primeiro a sair.
Pense em uma pilha de pratos: o último colocado em cima é o primeiro que será retirado.

### 🔹 Criando pilhas com listas

```python
pilha = []

# Empilhando elementos (append)
pilha.append("Livro A")
pilha.append("Livro B")
pilha.append("Livro C")

print(pilha)  # ["Livro A", "Livro B", "Livro C"]

# Desempilhando (pop)
topo = pilha.pop()
print(topo)  # Livro C
print(pilha)  # ["Livro A", "Livro B"]
```

### 🔹 Usando `collections.deque` como pilha

```python
from collections import deque

pilha = deque()
pilha.append("A")
pilha.append("B")
pilha.append("C")

print(pilha)

pilha.pop()  # Remove C
print(pilha)
```

---

## ✍️ Exercícios de Pilhas

1. Crie uma pilha de 3 tarefas a fazer. Depois remova as tarefas uma a uma.
2. Simule uma pilha de páginas de navegador (entrando em sites e depois voltando com "voltar").
3. Crie uma pilha de números, some todos ao remover cada um.

---

## 🔄 Diferenças entre Lista, Fila e Pilha

* **Lista** → Estrutura genérica para armazenar elementos em ordem. Permite acessar qualquer posição diretamente.
* **Fila (FIFO)** → O primeiro que entra é o primeiro que sai. Ideal para filas de atendimento.
* **Pilha (LIFO)** → O último que entra é o primeiro que sai. Ideal para desfazer ações ou histórico de navegação.

---

## 4️⃣ Dicionários em Python

Um **dicionário** armazena dados no formato **chave: valor**.
É como uma "tabela" onde você busca algo pela chave, e não pela posição.

### 🔹 Criando dicionários

```python
aluno = {
    "nome": "Carlos",
    "idade": 20,
    "curso": "Engenharia"
}
```

### 🔹 Acessando valores

```python
print(aluno["nome"])   # Carlos
print(aluno["curso"])  # Engenharia
```

### 🔹 Alterando valores

```python
aluno["idade"] = 21
print(aluno)
```

### 🔹 Adicionando e removendo itens

```python
aluno["nota"] = 9.5  # adiciona nova chave
del aluno["curso"]   # remove chave
print(aluno)
```

### 🔹 Iterando no dicionário

```python
for chave, valor in aluno.items():
    print(chave, ":", valor)
```

---

## ✍️ Exercícios de Dicionários

1. Crie um dicionário representando um carro com as chaves: `marca`, `modelo`, `ano`. Imprima cada informação.
2. Crie um dicionário para armazenar o nome e a idade de 3 pessoas. Depois mostre somente os nomes.
3. Crie um dicionário com notas de 3 matérias (português, matemática, ciência) e calcule a média.

---

## ✅ Exemplos resolvidos

### Lista

```python
numeros = [5, 8, 2, 10]
print(max(numeros))  # 10
print(min(numeros))  # 2
```

### Fila

```python
from collections import deque

fila = deque(["Ana", "Bruno", "Carlos"])
print(fila.popleft())  # Ana
print(fila)  # ['Bruno', 'Carlos']
```

### Pilha

```python
pilha = []
pilha.append("A")
pilha.append("B")
print(pilha.pop())  # B
print(pilha)  # ['A']
```

### Dicionário

```python
aluno = {"nome": "Maria", "nota": 8}
print(aluno["nome"])  # Maria
print("Aprovado" if aluno["nota"] >= 7 else "Reprovado")  # Aprovado
```

---

## 🚀 Desafio Final

Junte os conceitos:

* Crie uma **fila de atendimento** de alunos, onde cada aluno é representado por um **dicionário** com nome e nota.
* Ao atender (remover da fila), imprima:

  * O nome do aluno
  * A nota
  * Se está aprovado (nota ≥ 7) ou reprovado

Exemplo de dicionário: 

```python
# Cada aluno é um dicionário { "nome": str, "nota": float }
fila_alunos = deque([
    {"nome": "Ana",    "nota": 8.5},
    {"nome": "Bruno",  "nota": 6.0},
    {"nome": "Carla",  "nota": 7.0},
    {"nome": "Diego",  "nota": 9.2},
])
```

Saída esperada: 
```python
01) Ana        | Nota:  8.5 | Aprovado
02) Bruno      | Nota:  6.0 | Reprovado
03) Carla      | Nota:  7.0 | Aprovado
04) Diego      | Nota:  9.2 | Aprovado
```
---

