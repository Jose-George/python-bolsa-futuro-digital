## ✅ Gabarito das Questões

**1. (Conceitual)**
Na programação **estrutural**, o código é organizado em **funções** e **dados separados**, o que pode dificultar a manutenção em sistemas grandes.
Na **orientada a objetos (POO)**, os dados e comportamentos relacionados ficam agrupados em **classes e objetos**, permitindo melhor organização, reuso e encapsulamento.

---

**2. (Código)**

```python
class Carro:
    rodas = 4

    def __init__(self, modelo):
        self.modelo = modelo

c1 = Carro("Civic")
c2 = Carro("Corolla")
print(c1.rodas, c2.rodas, Carro.rodas)
```

➡️ Saída:

```
4 4 4
```

📌 Porque `rodas` é um **atributo de classe**, compartilhado por todas as instâncias.

---

**3. (Conceitual)**
O `__init__` é o **construtor** da classe. Ele é chamado automaticamente na criação de uma instância (`obj = Classe(...)`) e serve para **inicializar atributos**.
Se não o implementarmos, Python cria um `__init__` padrão que não faz nada além de aceitar `self`.

---

**4. (Código — armadilha)**
No código:

```python
class Sala:
    alunos = []

    def adicionar(self, nome):
        self.alunos.append(nome)

a = Sala()
b = Sala()
a.adicionar("Ana")
print(b.alunos)  # ['Ana']
```

➡️ Saída: `['Ana']`

📌 Porque `alunos` é um **atributo de classe** (compartilhado).
✅ Correção (usar atributo de instância no `__init__`):

```python
class Sala:
    def __init__(self):
        self.alunos = []

    def adicionar(self, nome):
        self.alunos.append(nome)
```

Agora, cada instância terá sua própria lista.

---

**5. (Encapsulamento)**
O `@property` permite criar **atributos calculados ou controlados** com a mesma sintaxe de acesso (`obj.atributo`) sem expor diretamente os atributos internos.
👉 Vantagem: podemos validar valores ou proteger atributos sem mudar a forma como são acessados.

---

**6. (Código)**
Implementação de `Retangulo` com `@property`:

```python
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura

    @property
    def perimetro(self):
        return 2 * (self.largura + self.altura)
```

---

**7. (Classmethod)**

* **Método de instância** (`def metodo(self, ...)`) atua sobre uma **instância específica**.
* **Método de classe** (`@classmethod`) atua sobre a **classe inteira** (recebe `cls`), útil para **construtores alternativos**.

📌 Exemplo:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_string(cls, texto):
        nome, idade = texto.split(",")
        return cls(nome.strip(), int(idade.strip()))

p = Pessoa.criar_de_string("Ana, 25")
```

---

**8. (Código)**
O método `depositar` não valida valores. Correção:

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("❌ Depósito deve ser positivo")
        self._saldo += valor
```

---

**9. (Situação prática)**
Classe `Pessoa`:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, eu sou {self.nome}"

p = Pessoa("Carlos", 30)
print(p.cumprimentar())  # Olá, eu sou Carlos
```

---

**10. (Conceitual)**
A POO facilita a manutenção porque:

* Agrupa dados e comportamentos em **objetos bem definidos**;
* Reduz **acoplamento** por meio do encapsulamento;
* Promove **reuso** com herança e composição;
* Permite evoluir sistemas grandes de forma mais organizada e previsível.

