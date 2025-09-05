# 📘 Aula: Tratamento de Exceções em Python

## 1. O que são Exceções?

* Uma **exceção** ocorre quando o programa encontra um erro durante a execução.
* Se não tratarmos a exceção, o programa será interrompido e exibirá uma mensagem de erro.

Exemplo sem tratamento:

```python
# Tentando dividir por zero
print(10 / 0)  # Gera ZeroDivisionError
```

Saída:

```
ZeroDivisionError: division by zero
```

---

## 2. Estrutura Básica: try e except

Usamos `try` para envolver o código que pode gerar erro e `except` para tratar o erro.

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except:
    print("Ocorreu um erro.")
```

---

## 3. Tratando Erros Específicos

Podemos capturar tipos específicos de exceções:

```python
try:
    x = int("abc")  # Erro de conversão
except ValueError:
    print("Erro: valor inválido para conversão em inteiro!")
```

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida!")
```

---

## 4. Vários Tipos de Exceções

```python
try:
    lista = [1, 2, 3]
    print(lista[5])  # Índice inválido
except ZeroDivisionError:
    print("Divisão por zero!")
except IndexError:
    print("Índice fora do intervalo da lista!")
except Exception as erro:
    print("Outro erro ocorreu:", erro)
```

---

## 5. else e finally

* `else`: executado se **não houver erro**.
* `finally`: sempre executado, **com ou sem erro**.

```python
try:
    numero = int(input("Digite um número positivo: "))
    if numero < 0:
        raise ValueError("Número negativo não permitido!")
except ValueError as e:
    print("Erro:", e)
else:
    print("Número válido:", numero)
finally:
    print("Execução finalizada!")
```

---

## 6. Criando Exceções Personalizadas com `raise`

Às vezes os erros padrões do Python não são suficientes. Podemos criar nossas **próprias exceções** para representar regras de negócio ou condições específicas.

### 6.1. Usando `raise` com exceções existentes

```python
def sacar(valor):
    if valor < 0:
        raise ValueError("Valor de saque não pode ser negativo!")
    print("Saque realizado:", valor)

try:
    sacar(-100)
except ValueError as e:
    print("Erro:", e)
```

---

### 6.2. Criando classes de exceção

Podemos criar exceções personalizadas herdando de `Exception`.

```python
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para saque!")
    return saldo - valor

try:
    saldo = 500
    saldo = sacar(saldo, 800)
except SaldoInsuficienteError as e:
    print("Erro:", e)
```

---

### 6.3. Exceções com atributos

Podemos enriquecer a exceção com informações extras.

```python
class LimiteExcedidoError(Exception):
    def __init__(self, valor, limite):
        self.valor = valor
        self.limite = limite
        super().__init__(f"Valor {valor} excede o limite de {limite}")

def transferir(valor, limite=1000):
    if valor > limite:
        raise LimiteExcedidoError(valor, limite)
    print(f"Transferência de {valor} realizada com sucesso!")

try:
    transferir(1500)
except LimiteExcedidoError as e:
    print("Erro:", e)
    print("Valor:", e.valor)
    print("Limite:", e.limite)
```

---

### 6.4. Vários tipos de exceções personalizadas

```python
class ValorNegativoError(Exception):
    pass

class DivisaoPorZeroCustomError(Exception):
    pass

def calcular(a, b):
    if a < 0 or b < 0:
        raise ValorNegativoError("Não é permitido usar números negativos!")
    if b == 0:
        raise DivisaoPorZeroCustomError("Não é permitido dividir por zero!")
    return a / b

try:
    print(calcular(-5, 2))
except ValorNegativoError as e:
    print("Erro:", e)
except DivisaoPorZeroCustomError as e:
    print("Erro:", e)
```

---

## 7. Exemplos Práticos

### Exemplo 1: Tratamento em divisão

```python
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"

print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # Erro: divisão por zero
```

### Exemplo 2: Leitura de arquivo

```python
try:
    with open("arquivo.txt", "r") as f:
        conteudo = f.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: arquivo não encontrado!")
```

### Exemplo 3: Conversão de dados

```python
valores = ["10", "20", "abc", "30"]

for v in valores:
    try:
        numero = int(v)
        print(f"Convertido: {numero}")
    except ValueError:
        print(f"Erro ao converter '{v}' para inteiro.")
```

---

# 📝 Exercícios

### Questão 1 – Tratamento de exceção

Crie uma função `divisao_segura(a, b)` que retorne o resultado da divisão, mas trate o erro de divisão por zero exibindo uma mensagem adequada.

---

### Questão 2 – Exceções personalizadas

Implemente uma função `depositar(valor)` que não permita valores negativos. Caso isso aconteça, dispare uma exceção personalizada `ValorInvalidoError`.

---

### Questão 3 – Listas e exceções

Faça um programa que peça ao usuário um índice para acessar uma lista fixa `[10, 20, 30]`. Trate o caso em que o índice não existe.

---

### Questão 4 – Manipulação de arquivos

Escreva um programa que tente abrir um arquivo chamado `dados.txt`. Se não existir, o programa deve criar o arquivo e escrever a frase: `"Arquivo criado com sucesso"`.

---

### Questão 5 – Misturando conceitos

Escreva uma função que:

* Peça ao usuário um número inteiro.
* Se o usuário digitar algo inválido (string, vazio etc.), trate o erro.
* Se o número for par, retorne `"Par"`, senão `"Ímpar"`.
