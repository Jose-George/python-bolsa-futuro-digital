
# 📘 Introdução à Lógica de Programação com Python

## 1. O que é lógica de programação?
**Definição:** Conjunto de regras e passos organizados para resolver um problema.  

**Objetivo:** Transformar uma ideia em uma sequência de instruções que o computador entenda.  

**Exemplo cotidiano:** Fazer um café (passos lógicos: ferver água → colocar pó no filtro → despejar água quente → servir).  

---

## 2. Pensamento Computacional
- **Decomposição:** Quebrar o problema em partes menores.  
- **Reconhecimento de padrões:** Identificar repetições e semelhanças.  
- **Abstração:** Focar apenas no que é importante.  
- **Algoritmos:** Criar instruções passo a passo.  

---

## 3. Python: a linguagem escolhida
- Linguagem simples, legível e popular.  
- Muito usada em ciência de dados, inteligência artificial, automação e desenvolvimento web.  

**Exemplo simples:**
```python
print("Olá, mundo!")
````

---

## 4. Variáveis e Tipos de Dados

* **Variáveis:** espaços de memória para guardar valores.

**Tipos básicos:**

* `int` → números inteiros
* `float` → números decimais
* `str` → textos
* `bool` → verdadeiro ou falso

**Exemplo:**

```python
idade = 20
altura = 1.75
nome = "Maria"
estudante = True
```

---

## 5. Estruturas Condicionais (Decisão)

Usamos para tomar decisões no programa.

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
```

---

## 6. Estruturas de Repetição (Laços)

Permitem executar um bloco várias vezes.

**Exemplo com `for`:**

```python
for i in range(5):
    print("Número:", i)
```

**Resultado:**

```
Número: 0
Número: 1
Número: 2
Número: 3
Número: 4
```

**Exemplo com `while`:**

```python
contador = 1
while contador <= 3:
    print("Contagem:", contador)
    contador += 1
```

**Resultado:**

```
Contagem: 1
Contagem: 2
Contagem: 3
```

---

## 7. Manipulação de Strings

Textos podem ser tratados de várias formas:

```python
frase = "Aprender Python é divertido!"
print(frase.upper())   # Maiúsculas
print(frase.lower())   # Minúsculas
print(frase[0:8])      # Fatiamento
```

**Resultado:**

```
APRENDER PYTHON É DIVERTIDO!
aprender python é divertido!
Aprender
```

---

## 8. Exercícios para praticar

1. Escreva um programa que peça o nome e a idade de uma pessoa e diga se ela pode votar.
2. Faça um programa que peça um número e mostre a tabuada desse número (de 1 a 10).
3. Crie um programa que conte de 1 a 100 e exiba apenas os números pares.
4. Peça ao usuário uma palavra e verifique se ela é um palíndromo (ex: “arara”).

---

## 9. Conclusão

* Lógica de Programação é pensar em como resolver problemas de forma estruturada.
* Python ajuda a aprender lógica porque tem uma sintaxe simples.
* O mais importante é praticar: quanto mais você resolve problemas, mais natural fica programar.
