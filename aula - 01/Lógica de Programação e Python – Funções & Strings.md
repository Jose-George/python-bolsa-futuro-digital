

# 📘 Lógica de Programação e Python – Funções & Strings

## 1. O que são Funções?
**Definição:** Blocos de código que executam uma tarefa específica.

**Vantagens:**
- Reutilização de código.
- Organização do programa.
- Facilidade de manutenção.

**Exemplo básico:**
```python
def saudacao():
    print("Olá! Seja bem-vindo ao mundo do Python!")

saudacao()
````

---

## 2. Funções com Parâmetros e Retorno

Funções podem receber dados (parâmetros) e devolver resultados (retorno).

```python
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("Resultado:", resultado)
```

---

## 3. Escopo de Variáveis

* **Variável local:** existe apenas dentro da função.
* **Variável global:** pode ser acessada em qualquer parte do programa.

```python
x = 10  # global

def exemplo():
    y = 5  # local
    print("Dentro da função:", x + y)

exemplo()
print("Fora da função:", x)
```

---

## 4. Manipulação de Strings

Python oferece várias funções úteis para trabalhar com textos:

```python
texto = " Python é incrível! "

print(texto.strip())       # Remove espaços extras
print(texto.upper())       # MAIÚSCULAS
print(texto.lower())       # minúsculas
print(texto.replace("incrível", "poderoso"))  # Substituir palavras
print(len(texto))          # Tamanho da string
print(texto[0:6])          # Fatiamento
```

---

## 5. Entrada de Dados com Strings

```python
nome = input("Digite seu nome: ")
print("Olá,", nome)
print("Seu nome tem", len(nome), "letras")
```

---

## 6. Estruturas Combinadas (Funções + Strings)

Exemplo: verificar se uma palavra é palíndromo.

```python
def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

print(eh_palindromo("arara"))    # True
print(eh_palindromo("Python"))   # False
```

---

## 7. Outros Conceitos Importantes

Além de funções e strings, é essencial conhecer:

**Conversão de tipos**

```python
num = "123"
print(int(num) + 10)  # converte string para inteiro
```

**Funções internas (built-in functions)**

```python
print(max(5, 10, 2))   # maior valor
print(min(5, 10, 2))   # menor valor
print(round(3.14159, 2))  # arredondar
```

**Boas práticas:**

* Nomes de funções devem ser claros e descritivos.
* Comentários ajudam a entender o código.
* Quebrar problemas grandes em funções menores.

---

## 8. Exercícios para Praticar

1. Crie uma função que receba um nome e exiba uma saudação personalizada.
2. Crie uma função que receba dois números e retorne a média deles.
3. Faça uma função que receba uma frase e devolva quantas vogais ela possui.
4. Crie uma função que receba uma string e retorne essa string invertida.
5. Desenvolva uma função que receba uma lista de nomes e retorne apenas os que começam com a letra **"A"**.

---

## 9. Conclusão

* Funções deixam o código mais organizado, reutilizável e legível.
* Manipulação de strings é essencial em quase todo programa.
* Aprender programação é como aprender um idioma: prática diária faz toda diferença.
