# 📘 Gabarito – Lista de Exercícios: Dicionário com Tupla em Python

## 🟢 Nível Iniciante


### 1. Criando seu primeiro dicionário
```python
# Criando um dicionário simples
pessoa = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "Campina Grande"
}

# Acessando os valores
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
````

✅ Aqui usamos **strings** como chaves (`"nome"`, `"idade"`, `"cidade"`)
e associamos cada uma a um **valor**.

---

### 2. Tupla como valor no dicionário

```python
agenda = {
    "Maria": ("(11) 99999-9999", "maria@email.com"),
    "João": ("(21) 98888-8888", "joao@email.com")
}

# Acessando os dados
print("Maria → Telefone:", agenda["Maria"][0], "| Email:", agenda["Maria"][1])
print("João  → Telefone:", agenda["João"][0],  "| Email:", agenda["João"][1])
```

✅ O valor é uma **tupla** `(telefone, email)`
👉 A posição `[0]` pega o telefone e `[1]` pega o email.

---

### 3. Tupla como chave no dicionário

```python
cidades = {
    (-23.5505, -46.6333): "São Paulo",
    (-8.0476, -34.8770): "Recife",
    (-7.2210, -35.8731): "Campina Grande"
}

# Consultando pelo par de coordenadas
print(cidades[(-7.2210, -35.8731)])  # Campina Grande
```

✅ Aqui a **chave** é uma **tupla** `(latitude, longitude)`.
👉 Isso é ótimo para representar **coordenadas** ou chaves compostas.

---

## 🟡 Nível Intermediário

---

### 4. Notas de alunos

```python
notas = {
    "Ana": (8, 7, 9),
    "Bruno": (5, 6, 7),
    "Carla": (10, 9, 9)
}

# Mostrar notas e calcular média
for aluno, notas_aluno in notas.items():
    media = sum(notas_aluno) / len(notas_aluno)
    print(f"{aluno} → Notas: {notas_aluno} | Média: {media:.2f}")
```

✅ `sum(notas_aluno)` soma os valores da tupla.
✅ `len(notas_aluno)` conta quantas notas existem.
👉 Dividindo um pelo outro obtemos a **média**.

---

### 5. Produtos e preços

```python
precos = {
    ("Camiseta", "P"): 30,
    ("Camiseta", "M"): 35,
    ("Camiseta", "G"): 40,
    ("Calça", "M"): 80
}

produto = input("Digite o produto: ")
tamanho = input("Digite o tamanho: ")

# Usamos uma tupla como chave para buscar o preço
chave = (produto, tamanho)

if chave in precos:
    print(f"O preço do {produto} tamanho {tamanho} é R$ {precos[chave]}")
else:
    print("Produto não encontrado!")
```

✅ A chave aqui é `(produto, tamanho)`.
👉 Isso permite diferenciar "Camiseta P" de "Camiseta G".

---

### 6. Jogo da velha (mini-desafio)

```python
# Tabuleiro vazio
tabuleiro = {
   (0,0): "-", (0,1): "-", (0,2): "-",
   (1,0): "-", (1,1): "-", (1,2): "-",
   (2,0): "-", (2,1): "-", (2,2): "-"
}

# Preenchendo algumas jogadas
tabuleiro[(0,0)] = "X"
tabuleiro[(1,1)] = "O"
tabuleiro[(2,2)] = "X"

# Mostrando o tabuleiro
for linha in range(3):
    for coluna in range(3):
        print(tabuleiro[(linha, coluna)], end=" ")
    print()
```

✅ Cada posição do tabuleiro é uma **chave tupla** `(linha, coluna)`.
👉 Usamos dois `for` aninhados para imprimir o tabuleiro.

---

## 🔵 Nível Avançando

---

### 7. Notas por disciplina

```python
notas = {
    ("Ana", "Matemática"): 9,
    ("Ana", "História"): 7,
    ("Bruno", "Matemática"): 6,
    ("Bruno", "História"): 8
}

aluno = input("Digite o nome do aluno: ")

soma = 0
quantidade = 0

print(f"Notas de {aluno}:")
for (nome, disciplina), nota in notas.items():
    if nome == aluno:
        print(f"{disciplina}: {nota}")
        soma += nota
        quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"Média geral de {aluno}: {media:.2f}")
else:
    print("Aluno não encontrado.")
```

✅ A chave é `(nome, disciplina)`.
👉 Filtramos no loop apenas as notas do aluno digitado.

---

### 8. Banco de dados de coordenadas

```python
pontos_turisticos = {
    (-22.9519, -43.2105): "Cristo Redentor (RJ)",
    (-12.9714, -38.5108): "Elevador Lacerda (Salvador)",
    (-7.2210, -35.8731): "Açude Velho (Campina Grande - PB)"
}

lat = float(input("Digite a latitude: "))
lon = float(input("Digite a longitude: "))

chave = (lat, lon)

if chave in pontos_turisticos:
    print("Ponto turístico encontrado:", pontos_turisticos[chave])
else:
    print("Nenhum ponto turístico registrado nessa coordenada.")
```

✅ Aqui usamos a tupla `(lat, lon)` como chave.
👉 Boa prática: usar `float()` no input para permitir números decimais.

---

## 🚀 Desafio Final – Cadastro de alunos

```python
# Cadastro de alunos: (nome, disciplina) → (nota1, nota2, nota3)

cadastro = {
    ("Ana", "Matemática"): (8, 7, 9),
    ("Ana", "História"): (6, 8, 7),
    ("Bruno", "Matemática"): (5, 6, 6)
}

# Consultar um aluno
aluno = input("Digite o nome do aluno: ")

soma = 0
quantidade = 0

print(f"Notas de {aluno}:")
for (nome, disciplina), notas in cadastro.items():
    if nome == aluno:
        media = sum(notas) / len(notas)
        print(f"{disciplina}: {notas} → Média: {media:.2f}")
        soma += media
        quantidade += 1

if quantidade > 0:
    media_geral = soma / quantidade
    print(f"Média geral de {aluno}: {media_geral:.2f}")
else:
    print("Aluno não encontrado.")
```

✅ Cada disciplina tem uma tupla com 3 notas.
✅ Usamos `sum(notas)/len(notas)` para calcular médias.
👉 No final, também mostramos a **média geral** do aluno em todas as disciplinas.

---
