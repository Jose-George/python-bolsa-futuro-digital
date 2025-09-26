# Aula: Classes Abstratas e Métodos Abstratos em Python

## 1. Introdução

Quando projetamos sistemas orientados a objetos, às vezes precisamos criar **modelos** que não fazem sentido serem instanciados diretamente, mas que servem como **base** para outras classes.

É aqui que entram:
- **Classe Abstrata**: serve de modelo, não pode ser instanciada.
- **Método Abstrato**: método definido, mas **sem implementação**, que deve ser sobrescrito nas subclasses.

Esses recursos ajudam a:
- **Garantir um contrato**: todas as subclasses devem implementar certos métodos.
- **Organizar e padronizar** o código.

---

## 2. O Problema sem Classes Abstratas

Imagine que você cria uma classe `Forma` para calcular áreas:

```python
class Forma:
    def area(self):
        pass  # intenção de ser implementado depois
````

Se alguém fizer:

```python
f = Forma()
print(f.area())
```

Não faz sentido ter uma “forma genérica” com área indefinida.
Queremos **impedir** a criação direta de `Forma` e **obrigar** as subclasses a implementar `area()`.

---

## 3. Módulo `abc` – Abstract Base Class

Python oferece o módulo `abc` (*Abstract Base Class*).

Para criar classes e métodos abstratos:

1. **Importar**:

   ```python
   from abc import ABC, abstractmethod
   ```
2. Fazer a classe herdar de `ABC`.
3. Decorar os métodos obrigatórios com `@abstractmethod`.

---

## 4. Exemplo Básico

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Subclasse concreta
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

q = Quadrado(5)
print("Área:", q.area())
print("Perímetro:", q.perimetro())
```

Características importantes:

* `Forma` **não pode ser instanciada**.
* `Quadrado` só é instanciável porque **implementou todos os métodos abstratos**.

---

## 5. Classe Abstrata com Construtor

Uma classe abstrata pode ter um `__init__` e métodos **concretos** (normais).

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass

    def apresentar(self):
        print(f"Eu sou {self.nome}")
```

Subclasse concreta:

```python
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

dog = Cachorro("Rex")
dog.apresentar()
dog.emitir_som()
```

* O construtor `__init__` é herdado.
* O método `apresentar()` é **concreto**, usado diretamente.
* `emitir_som()` é abstrato, portanto **obrigatório**.

---

## 6. Várias Classes e Herança

É possível combinar classes abstratas com **herança múltipla**:

```python
from abc import ABC, abstractmethod

class Nadador(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Corredor(ABC):
    @abstractmethod
    def correr(self):
        pass

class Triatleta(Nadador, Corredor):
    def nadar(self):
        print("Nadando...")

    def correr(self):
        print("Correndo...")

t = Triatleta()
t.nadar()
t.correr()
```

O `Triatleta` só pode ser instanciado porque implementou **todos** os métodos abstratos.

---

## 7. Métodos Abstratos com Implementação Padrão

É possível dar **implementação parcial** ao método abstrato.
As subclasses podem usar ou sobrescrever.

```python
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        print("Ligando veículo...")  # implementação padrão

class Carro(Veiculo):
    def ligar(self):
        super().ligar()
        print("Carro ligado!")

c = Carro()
c.ligar()
```

* O método `ligar` tem comportamento padrão.
* A subclasse pode chamar `super().ligar()` para aproveitar.

---

## 8. Verificando Subclasses Abstratas

* `issubclass` e `isinstance` funcionam normalmente:

  ```python
  issubclass(Quadrado, Forma)  # True
  isinstance(q, Forma)        # True
  ```

* Mas instanciar a classe abstrata gera erro:

  ```python
  f = Forma()  # TypeError
  ```

---

## 9. Exemplo Completo: Sistema de Pagamento

```python
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Pagando R${valor} com cartão de crédito.")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Gerando boleto de R${valor}.")

def executar_pagamento(pagamento: Pagamento, valor):
    pagamento.processar(valor)

pagamentos = [CartaoCredito(), Boleto()]
for p in pagamentos:
    executar_pagamento(p, 150)
```

* `Pagamento` garante que **todas as formas de pagamento** tenham o método `processar`.
* `executar_pagamento` aceita qualquer classe que siga o contrato.

---

## 10. Boas Práticas

* Use classes abstratas para **definir contratos claros** entre partes do sistema.
* Prefira métodos abstratos quando **toda subclasse** precisar implementar algo.
* Combine com **herança múltipla** somente quando houver real necessidade.
* Documente bem os métodos para que quem herde a classe saiba **o que precisa implementar**.

---

## 11. Exercícios

1. Crie uma classe abstrata `Funcionario` com um método abstrato `calcular_bonus`.
   Crie subclasses `Gerente` e `Desenvolvedor` que implementem regras diferentes de bônus.

2. Implemente uma classe abstrata `Veiculo` com métodos abstratos `acelerar` e `frear`.
   Crie subclasses `Carro` e `Moto`.

3. Crie uma classe abstrata `Arquivo` com um método `abrir`.
   Implemente subclasses `ArquivoTexto` e `ArquivoImagem` que exibam mensagens diferentes ao abrir.

---

## 12. Resumo

* **Classe abstrata**: não pode ser instanciada; serve como modelo.
* **Método abstrato**: definido mas sem implementação obrigatória.
* Use `from abc import ABC, abstractmethod`.
* Subclasses devem implementar **todos** os métodos abstratos para serem instanciadas.
* Permite organizar, padronizar e garantir contratos no seu código.

As classes abstratas são essenciais em sistemas grandes para manter o código limpo, seguro e extensível.
