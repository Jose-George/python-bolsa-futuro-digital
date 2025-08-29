# 📘 Lista de Exercícios – Dicionário com Tupla em Python

## 🎯 Objetivo
Praticar o uso de **dicionários** e **tuplas** em situações reais, começando do básico até problemas mais elaborados.

---

## 🟢 Nível Iniciante

### 1. Criando seu primeiro dicionário
Crie um dicionário que guarde informações sobre uma pessoa:
- Nome
- Idade
- Cidade

Depois, **imprima** cada informação na tela.

---

### 2. Tupla como valor no dicionário
Crie um dicionário chamado `agenda` onde cada **nome** da pessoa é a chave,  
e o **telefone e o email** ficam dentro de uma **tupla** como valor.  
Exemplo de saída esperada:

```

Maria → Telefone: (11) 9999-9999 | Email: [maria@email.com](mailto:maria@email.com)

````

---

### 3. Tupla como chave no dicionário
Crie um dicionário chamado `cidades` onde a **chave** seja uma tupla de **(latitude, longitude)**  
e o **valor** seja o nome da cidade.  
Inclua pelo menos 3 cidades brasileiras (ex.: São Paulo, Recife, Campina Grande).

Depois, mostre na tela o nome da cidade a partir de suas coordenadas.

---

## 🟡 Nível Intermediário

### 4. Notas de alunos
Crie um dicionário onde:
- A chave seja o **nome do aluno**
- O valor seja uma **tupla com 3 notas**

Depois, faça:
1. Mostrar todas as notas de um aluno.
2. Calcular a média das notas de cada aluno.

---

### 5. Produtos e preços
Monte um dicionário chamado `precos` onde a **chave** seja uma tupla com:  
`(nome_do_produto, tamanho)`  
e o valor seja o preço.  

Exemplo:
```python
("Camiseta", "M") → 35
("Camiseta", "G") → 40
````

Peça ao usuário para digitar o **produto** e o **tamanho**,
e mostre o preço correspondente.

---

### 6. Jogo da velha (mini-desafio)

Use um dicionário chamado `tabuleiro` para representar as posições de um jogo da velha.

* As chaves devem ser tuplas `(linha, coluna)`
* Os valores devem ser `"X"`, `"O"` ou `"-"` (se vazio)

Exemplo de dicionário inicial:

```python
{
   (0,0): "-", (0,1): "-", (0,2): "-",
   (1,0): "-", (1,1): "-", (1,2): "-",
   (2,0): "-", (2,1): "-", (2,2): "-"
}
```

1. Preencha algumas posições manualmente.
2. Mostre o tabuleiro de forma organizada na tela.

---

## 🔵 Nível Avançando (quase avançado 😁)

### 7. Notas por disciplina

Crie um dicionário onde:

* A **chave** seja uma tupla `(nome_aluno, disciplina)`
* O **valor** seja a nota

Exemplo:

```python
("Ana", "Matemática") → 9
("Ana", "História") → 7
```

Depois, escreva um programa que:

1. Pergunte o nome de um aluno.
2. Mostre todas as disciplinas e notas desse aluno.
3. Calcule a média geral dele.

---

### 8. Banco de dados de coordenadas

Crie um dicionário chamado `pontos_turisticos` onde:

* A **chave** seja `(latitude, longitude)`
* O **valor** seja o nome do ponto turístico

Inclua pontos famosos como:

* Cristo Redentor (RJ)
* Elevador Lacerda (Salvador)
* Açude Velho (Campina Grande - PB)

Depois, faça um programa que:

1. Pergunte as coordenadas ao usuário.
2. Informe qual ponto turístico fica nesse local (ou avise que não existe).

---

## 🚀 Desafio Final

Monte um **sistema simples de cadastro de alunos** usando dicionário com tupla:

* A chave deve ser `(nome_aluno, disciplina)`
* O valor deve ser uma tupla `(nota1, nota2, nota3)`

O programa deve permitir:

1. Cadastrar um novo aluno com suas notas.
2. Consultar todas as notas de um aluno.
3. Calcular a média geral do aluno em todas as disciplinas.

```
📌 Dica: use loops (`for`) e o método `get()` dos dicionários para facilitar.
```
