# Aula: Herança em Programação Orientada a Objetos (Python)

## 1. Introdução

Na **Programação Orientada a Objetos (POO)**, **herança** é um dos pilares fundamentais.  
Ela permite **reaproveitar código** e criar relações entre classes, tornando o desenvolvimento mais **organizado, flexível e fácil de manter**.

Nesta aula você vai aprender:
- O que é herança e por que utilizá-la.
- Conceitos importantes: **classe base (pai)** e **classe derivada (filha)**.
- **Sintaxe** para criar herança em Python.
- Uso da função `super()`.
- Sobrescrita de métodos.
- Encapsulamento e níveis de acesso (público, protegido, privado).
- **Herança múltipla**: quando e como usar.
- Boas práticas e exemplos práticos.

---

## 2. Relembrando: O que é uma Classe?

Antes de falar de herança, revise o que é **classe** e **objeto**:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Ana", 25)
p1.apresentar()
````

* **Classe**: um molde que descreve características (atributos) e comportamentos (métodos).
* **Objeto**: uma instância concreta dessa classe.

---

## 3. O que é Herança?

Herança permite que uma **classe filha** receba **atributos e métodos** de uma **classe pai**.

* **Classe Pai/Base/Superclasse**: a classe original.
* **Classe Filha/Derivada/Subclasse**: a classe que herda.

### Analogia do mundo real

Pense em **Veículo** como classe base.
Carro, Moto e Caminhão são subclasses: todos **são veículos**, mas cada um tem características próprias.

---

## 4. Sintaxe da Herança em Python

A herança é definida colocando o **nome da classe pai** entre parênteses na declaração da classe filha:

```python
class ClassePai:
    # atributos e métodos da classe pai

class ClasseFilha(ClassePai):
    # novos atributos e métodos ou sobrescritos
```

* Se não for especificada nenhuma classe pai, a classe herda automaticamente de `object`, a raiz de todas as classes em Python.
* Podemos herdar de **uma ou mais classes** (herança múltipla, veremos depois).

Exemplo simples:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Algum som genérico")

class Cachorro(Animal):
    def latir(self):
        print("Au au!")

dog = Cachorro("Rex")
print(dog.nome)       # herdado de Animal
dog.emitir_som()      # herdado de Animal
dog.latir()           # exclusivo de Cachorro
```

---

## 5. Construtor e `super()`

Se a classe filha precisa de um **construtor próprio**, mas ainda quer aproveitar o da classe pai, usamos `super()`:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)  # chama o __init__ da classe pai
        self.cor = cor

g = Gato("Mimi", "Branca")
print(g.nome, g.cor)
```

O `super()` garante que o código do pai seja executado antes ou junto com o da filha.

---

## 6. Sobrescrevendo Métodos

Podemos criar na classe filha um **método com o mesmo nome** do pai para mudar o comportamento.

```python
class Animal:
    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

dog = Cachorro()
dog.emitir_som()  # "Au au!"
```

*(Isso é sobrescrita simples. Polimorfismo completo será visto em outra aula.)*

---

## 7. Encapsulamento e Níveis de Acesso

Python não tem modificadores de acesso formais, mas segue **convenções**:

* **Público**: `atributo` – acessível de qualquer lugar.
* **Protegido**: `_atributo` – *convenção* para indicar que é interno.
* **Privado**: `__atributo` – o Python aplica *name mangling* para dificultar acesso.

Exemplo:

```python
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular       # público
        self._saldo = saldo          # protegido
        self.__senha = "1234"        # privado

    def mostrar_saldo(self):
        print(f"Saldo: {self._saldo}")

c = Conta("Maria", 1000)
print(c.titular)     # ok
print(c._saldo)      # possível, mas não recomendado
# print(c.__senha)   # ERRO
```

---

## 8. **Herança Múltipla em Python**

**Python permite herança múltipla**:
uma classe pode herdar de **mais de uma classe pai**.

### Sintaxe

Basta listar as classes pais, separadas por vírgula:

```python
class ClasseFilha(ClassePai1, ClassePai2, ...):
    # corpo da classe
```

### Exemplo Prático

```python
class Caminha:
    def dormir(self):
        print("Dormindo...")

class Come:
    def comer(self):
        print("Comendo...")

class Pessoa(Caminha, Come):
    def falar(self):
        print("Falando...")

p = Pessoa()
p.dormir()
p.comer()
p.falar()
```

Aqui, `Pessoa` herda métodos de **Caminha** e **Come**.

### Ordem de Resolução de Métodos (MRO)

Quando duas classes pais têm um método com o mesmo nome,
Python segue a **Method Resolution Order (MRO)** – a ordem em que as classes foram declaradas.

```python
class A:
    def acao(self):
        print("A")

class B:
    def acao(self):
        print("B")

class C(A, B):
    pass

c = C()
c.acao()  # Saída: "A", pois A vem antes de B
```

Podemos ver a ordem de resolução usando:

```python
print(C.mro())
```

---

## 9. Exemplo Completo: Cadastro de Funcionários

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario}")

# Uso
f = Funcionario("João", 30, "Desenvolvedor", 5000)
f.apresentar()
```

---

## 10. Boas Práticas

* **Use herança apenas quando houver relação “é um(a)”**.
  Ex.: um Cachorro **é um** Animal.
  Se for apenas “tem um(a)”, prefira **composição**.
* **Evite herança muito profunda** (várias camadas) para não dificultar a manutenção.
* Em herança múltipla, planeje a hierarquia e entenda bem a **ordem de resolução (MRO)**.

---

## 11. Exercícios

1. Crie uma classe `Veiculo` com atributos `marca` e `ano`.
   Crie subclasses `Carro` e `Moto` com atributos específicos e métodos que descrevam o veículo.

2. Implemente uma classe `Funcionario` com subclasses `Gerente` e `Programador`.
   Cada uma deve ter um método que calcule bônus de forma diferente.

3. Crie duas classes `Nadador` e `Corredor`, cada uma com um método específico.
   Crie uma classe `Triatleta` que herde de ambas e mostre que pode nadar e correr.

---

## 12. Resumo

* **Herança**: permite que uma classe filha reutilize código da classe pai.
* **Sintaxe**: `class Filha(Pai):` ou `class Filha(Pai1, Pai2):` para herança múltipla.
* **super()**: chama métodos da classe pai, útil no construtor.
* **Sobrescrita**: redefinir métodos na classe filha.
* **Encapsulamento**: organize a visibilidade de atributos e métodos.
* **Herança múltipla**: Python permite; use com cuidado.

Pratique bastante! A herança é poderosa, mas deve ser usada com responsabilidade.