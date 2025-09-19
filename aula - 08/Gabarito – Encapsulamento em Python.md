# ✅ Gabarito – Lista de Exercícios de Encapsulamento em Python

A seguir, as soluções comentadas para cada exercício proposto.

---

## 1️⃣ Produto
```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            print("❌ O preço não pode ser negativo.")

# Teste
p = Produto("Caneta", 2.50)
print(p.nome, p.preco)   # Caneta 2.5
p.preco = 5.0
print(p.preco)           # 5.0
p.preco = -10            # Mensagem de erro
````

---

## 2️⃣ ContaBancaria

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("❌ Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("❌ Saldo insuficiente ou valor inválido.")

    def ver_saldo(self):
        return self.__saldo

# Teste
c = ContaBancaria("João", 100)
c.depositar(50)
print(c.ver_saldo())  # 150
c.sacar(30)
print(c.ver_saldo())  # 120
c.sacar(500)          # Erro de saldo
```

---

## 3️⃣ Aluno

```python
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = 0
        self.nota = nota  # usa o setter logo na criação

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            print("❌ A nota deve ser entre 0 e 10.")

# Teste
a = Aluno("Maria", 8)
print(a.nome, a.nota)  # Maria 8
a.nota = 11            # Mensagem de erro
a.nota = 9
print(a.nota)          # 9
```

---

## 4️⃣ Carro

```python
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.__velocidade = 0

    def acelerar(self, valor):
        if valor > 0:
            self.__velocidade += valor
        else:
            print("❌ Valor inválido para acelerar.")

    def frear(self, valor):
        if valor > 0:
            self.__velocidade -= valor
            if self.__velocidade < 0:
                self.__velocidade = 0
        else:
            print("❌ Valor inválido para frear.")

    def ver_velocidade(self):
        return self.__velocidade

# Teste
c = Carro("Fusca")
c.acelerar(30)
print(c.ver_velocidade())  # 30
c.frear(10)
print(c.ver_velocidade())  # 20
c.frear(50)
print(c.ver_velocidade())  # 0
```

---

## 5️⃣ Usuario

```python
class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = None
        self.senha = senha  # usa o setter

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
        else:
            print("❌ A senha deve ter pelo menos 6 caracteres.")

    def verificar_senha(self, tentativa):
        return tentativa == self.__senha

# Teste
u = Usuario("teste@email.com", "12345")   # senha inválida
u.senha = "segura123"                     # agora válida
print(u.verificar_senha("12345"))         # False
print(u.verificar_senha("segura123"))     # True
```
