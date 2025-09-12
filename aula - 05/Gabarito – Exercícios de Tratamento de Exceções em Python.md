# 📝 Gabarito – Exercícios de Tratamento de Exceções em Python

---

## ✅ Questão 1 – Tratamento de exceção

**Enunciado:**
Crie uma função `divisao_segura(a, b)` que retorne o resultado da divisão, mas trate o erro de divisão por zero exibindo uma mensagem adequada.

**Solução:**

```python
def divisao_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero não permitida"

print(divisao_segura(10, 2))  # 5.0
print(divisao_segura(10, 0))  # Erro: divisão por zero não permitida
```

---

## ✅ Questão 2 – Exceções personalizadas

**Enunciado:**
Implemente uma função `depositar(valor)` que não permita valores negativos. Caso isso aconteça, dispare uma exceção personalizada `ValorInvalidoError`.

**Solução:**

```python
class ValorInvalidoError(Exception):
    def __init__(self, valor):
        super().__init__(f"O valor {valor} é inválido para depósito.")

def depositar(valor):
    if valor < 0:
        raise ValorInvalidoError(valor)
    print(f"Depósito de {valor} realizado com sucesso!")

try:
    depositar(-50)
except ValorInvalidoError as e:
    print("Erro:", e)
```

Saída esperada:

```
Erro: O valor -50 é inválido para depósito.
```

---

## ✅ Questão 3 – Listas e exceções

**Enunciado:**
Faça um programa que peça ao usuário um índice para acessar uma lista fixa `[10, 20, 30]`. Trate o caso em que o índice não existe.

**Solução:**

```python
lista = [10, 20, 30]

try:
    indice = int(input("Digite o índice que deseja acessar (0 a 2): "))
    print("Valor encontrado:", lista[indice])
except IndexError:
    print("Erro: índice fora do intervalo válido!")
except ValueError:
    print("Erro: digite apenas números inteiros.")
```

---

## ✅ Questão 4 – Manipulação de arquivos

**Enunciado:**
Escreva um programa que tente abrir um arquivo chamado `dados.txt`. Se não existir, o programa deve criar o arquivo e escrever a frase: `"Arquivo criado com sucesso"`.

**Solução:**

```python
try:
    with open("dados.txt", "r") as f:
        conteudo = f.read()
    print("Conteúdo do arquivo:", conteudo)
except FileNotFoundError:
    with open("dados.txt", "w") as f:
        f.write("Arquivo criado com sucesso")
    print("Arquivo não encontrado, mas foi criado com sucesso.")
```

---

## ✅ Questão 5 – Misturando conceitos

**Enunciado:**
Escreva uma função que:

* Peça ao usuário um número inteiro.
* Se o usuário digitar algo inválido (string, vazio etc.), trate o erro.
* Se o número for par, retorne `"Par"`, senão `"Ímpar"`.

**Solução:**

```python
def verificar_par_ou_impar():
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            return "Par"
        else:
            return "Ímpar"
    except ValueError:
        return "Erro: valor digitado não é um número válido."

print(verificar_par_ou_impar())
```
