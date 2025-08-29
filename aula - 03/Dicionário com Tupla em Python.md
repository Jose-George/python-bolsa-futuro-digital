# 📘 Aula: Dicionário com Tupla em Python

## 1. O que é um **dicionário**?

Um **dicionário** em Python é uma estrutura que guarda informações em pares de **chave → valor**.

👉 Pense em um dicionário da vida real:  
- Palavra = **chave**  
- Significado = **valor**

Exemplo simples em Python:  

```python
aluno = {
    "nome": "Maria",
    "idade": 20,
    "curso": "Engenharia"
}
````

* `"nome"` é a **chave** → `"Maria"` é o **valor**
* `"idade"` é a **chave** → `20` é o **valor**
* `"curso"` é a **chave** → `"Engenharia"` é o **valor**

---

## 2. O que é uma **tupla**?

Uma **tupla** é uma sequência de valores que **não muda** depois de criada (imutável).
É parecida com uma lista, mas usa **parênteses**:

```python
coordenadas = (10, 20)
print(coordenadas[0])  # 10
print(coordenadas[1])  # 20
```

---

## 3. O que significa **dicionário com tupla**?

Significa que podemos usar uma **tupla** como **chave** ou como **valor** em um dicionário.

---

### 3.1 Tupla como **chave**

Muito útil quando precisamos identificar algo com **dois ou mais valores juntos**.
Exemplo: mapa de cidades por **coordenadas geográficas** (latitude, longitude).

```python
# Dicionário com tupla como chave
cidades = {
    (40.7128, -74.0060): "Nova York",
    (48.8566, 2.3522): "Paris",
    (35.6895, 139.6917): "Tóquio",
    (-7.2210, -35.8731): "Campina Grande - PB"
}

print(cidades[(48.8566, 2.3522)])   # Paris
print(cidades[(-7.2210, -35.8731)]) # Campina Grande - PB
```

---

### 3.2 Tupla como **valor**

Aqui a tupla guarda várias informações relacionadas a uma mesma chave.

Exemplo: dicionário de alunos com suas notas.

```python
# Dicionário com tupla como valor
notas = {
    "Ana": (8, 7, 9),
    "Bruno": (5, 6, 7),
    "Carla": (10, 9, 9)
}

print(notas["Ana"])      # (8, 7, 9)
print(notas["Ana"][0])   # 8 (primeira nota)
```

---

## 4. Aplicabilidade em problemas do dia a dia

### 🔹 Exemplo 1: Agenda telefônica com várias formas de contato

```python
agenda = {
    "Maria": ("(11) 99999-9999", "maria@email.com"),
    "João": ("(21) 98888-8888", "joao@email.com")
}

print(agenda["Maria"][0])  # Telefone da Maria
print(agenda["Maria"][1])  # Email da Maria
```

---

### 🔹 Exemplo 2: Tabela de preços de produtos por tamanho (P, M, G)

```python
precos = {
    ("Camiseta", "P"): 30,
    ("Camiseta", "M"): 35,
    ("Camiseta", "G"): 40,
    ("Calça", "M"): 80
}

print(precos[("Camiseta", "G")])  # 40
```

---

### 🔹 Exemplo 3: Coordenadas no jogo da velha (tabuleiro 3x3)

```python
tabuleiro = {
    (0, 0): "X",
    (0, 1): "O",
    (1, 1): "X"
}

print(tabuleiro[(0, 0)])  # X
print(tabuleiro.get((2, 2), "-"))  # Se não tiver nada, mostra "-"
```

---

### 🔹 Exemplo 4: Registro de notas de alunos em diferentes disciplinas

```python
# Chave = (nome do aluno, disciplina), valor = nota
notas = {
    ("Ana", "Matemática"): 9,
    ("Ana", "História"): 7,
    ("Bruno", "Matemática"): 6,
    ("Bruno", "História"): 8
}

print(notas[("Ana", "Matemática")])  # 9
```

---

## 5. Por que usar **dicionário com tupla**?

✅ Representar **chaves compostas** (produto + tamanho, aluno + disciplina, latitude + longitude).

✅ Guardar **vários valores juntos** (várias notas, contatos, pacotes de dados).

✅ Organizar dados do dia a dia de forma **clara e estruturada**.

---

## 📝 Resumindo:

* **Dicionário** = chave → valor
* **Tupla** = agrupa valores que não mudam
* **Juntos** = permitem representar dados **compostos e bem organizados**

