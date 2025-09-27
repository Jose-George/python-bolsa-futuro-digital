# Aula: Polimorfismo em Programação Orientada a Objetos (Python)

## 1. Introdução

O **Polimorfismo** é um dos quatro pilares da Programação Orientada a Objetos (POO), junto com **abstração**, **encapsulamento** e **herança**.

A palavra vem do grego:
- **Poly** = muitos
- **Morphos** = formas

Em POO, significa que **objetos diferentes podem responder ao mesmo método de maneiras distintas**.  
Ou seja, **um único nome de método pode ter comportamentos diferentes**, dependendo do objeto que o invoca.

Nesta aula você vai aprender:
- O que é polimorfismo e sua utilidade.
- Polimorfismo com herança e sobrescrita de métodos.
- Polimorfismo com *duck typing* (estilo Python).
- Uso de classes abstratas e métodos abstratos.
- Boas práticas e exemplos práticos.

---

## 2. Por que usar Polimorfismo?

Imagine que você precisa criar uma função que execute a ação `emitir_som` em vários tipos de animais:  
Cachorro late, Gato mia, Vaca muge…

Sem polimorfismo, você teria que fazer vários `if` ou `match`.  
Com polimorfismo, basta **chamar o método**, e cada objeto se encarrega de responder corretamente.

---

## 3. Polimorfismo com Herança e Sobrescrita

O jeito mais comum é sobrescrevendo métodos em subclasses.

```python
class Animal:
    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

# Função que usa polimorfismo
def fazer_barulho(animal):
    animal.emitir_som()

# Uso
animais = [Cachorro(), Gato(), Animal()]
for a in animais:
    fazer_barulho(a)
````

Saída:

```
Au au!
Miau!
Som genérico
```

Observe:

* `fazer_barulho` não se importa com **qual** tipo de animal é.
* Cada objeto sabe **como** deve emitir seu som.

---

## 4. Polimorfismo e o "Duck Typing" em Python

Python é **dinamicamente tipado**.
Ele segue o princípio: *“Se anda como um pato e grasna como um pato, deve ser um pato”*.

Isso significa que **não precisamos de herança** para polimorfismo:
basta que o objeto tenha o **método necessário**.

```python
class Pato:
    def fazer_som(self):
        print("Quack!")

class Pessoa:
    def fazer_som(self):
        print("Olá!")

def reproduzir_som(objeto):
    objeto.fazer_som()  # Não importa a classe

pato = Pato()
pessoa = Pessoa()

for o in (pato, pessoa):
    reproduzir_som(o)
```

Saída:

```
Quack!
Olá!
```

Aqui, `reproduzir_som` não sabe (nem precisa saber) que `pato` é um Pato ou que `pessoa` é uma Pessoa.
O que importa é que ambos têm o método `fazer_som`.

---

## 5. Polimorfismo com Classes Abstratas

Às vezes, você quer garantir que **todas as subclasses implementem um método específico**.
Para isso, usamos **classes abstratas**, com o módulo `abc`.

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

formas = [Quadrado(4), Circulo(3)]
for f in formas:
    print(f"Área: {f.area()}")
```

* `Forma` é abstrata: não pode ser instanciada diretamente.
* `area()` é **método abstrato**: toda subclasse deve implementá-lo.

---

## 6. Polimorfismo em Funções e Operadores

Em Python, até **operadores** são polimórficos: o sinal `+` funciona para números, strings, listas…

```python
print(3 + 5)          # soma numérica
print("Hello " + "World")  # concatenação de strings
print([1, 2] + [3, 4])     # junção de listas
```

Isso é possível porque cada tipo tem sua **própria implementação** do método especial `__add__`.

Você pode criar seu próprio comportamento para operadores sobrescrevendo métodos especiais:

```python
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __repr__(self):
        return f"Vetor({self.x}, {self.y})"

v1 = Vetor(1, 2)
v2 = Vetor(3, 4)
print(v1 + v2)  # Vetor(4, 6)
```

---

## 7. Exemplo Completo: Sistema de Pagamento

```python
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor} com cartão de crédito.")

class Boleto(Pagamento):
    def pagar(self, valor):
        print(f"Gerando boleto no valor de R${valor}.")

class Pix(Pagamento):
    def pagar(self, valor):
        print(f"Enviando Pix de R${valor}.")

def processar_pagamento(pagamento: Pagamento, valor):
    pagamento.pagar(valor)

pagamentos = [CartaoCredito(), Boleto(), Pix()]
for p in pagamentos:
    processar_pagamento(p, 100)
```

Cada classe lida com o pagamento de forma diferente, mas a função `processar_pagamento` é **genérica**.

---

## 8. Boas Práticas

* **Nomeie métodos com clareza**: o polimorfismo se baseia em nomes consistentes.
* Use **classes abstratas** quando quiser garantir que subclasses tenham certos métodos.
* Aproveite o **duck typing** quando quiser flexibilidade, mas documente o contrato esperado.
* Evite if/else desnecessários: deixe o objeto decidir **como** agir.

---

## 9. Exercícios

1. Crie uma classe abstrata `Funcionario` com um método `calcular_bonus()`.
   Implemente subclasses `Gerente` e `Desenvolvedor`, cada uma com sua própria lógica de bônus.

2. Crie uma função `desenhar_forma` que receba diferentes classes (`Circulo`, `Quadrado`, `Triangulo`)
   e chame um método `desenhar()` polimorficamente.

3. Implemente um programa que use polimorfismo de operador:
   Crie uma classe `Moeda` que permita somar duas moedas (`m1 + m2`) e retorne uma nova instância.

---

## 10. Resumo

* **Polimorfismo**: objetos diferentes respondem de maneiras diferentes ao **mesmo método**.
* Em Python:

  * **Com herança**: sobrescrevendo métodos das subclasses.
  * **Duck typing**: basta que o objeto tenha o método esperado, independentemente da hierarquia.
  * **Classes abstratas**: garantem a implementação de métodos.
  * **Operadores**: comportam-se de forma polimórfica via métodos especiais (`__add__`, `__mul__`, etc.).
* O polimorfismo torna o código mais flexível, limpo e fácil de manter.

Pratique bastante! O polimorfismo é essencial para criar sistemas extensíveis e reutilizáveis.