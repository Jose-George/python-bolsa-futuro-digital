# Aula: Introdução à Programação Orientada a Objetos em Python

*Referência: “Introdução à programação orientada a objetos”, MAC1222 – Marcilio, USP.* ([IME-USP][1])

---

## Objetivos

Ao fim desta aula você deverá ser capaz de:

* Entender a diferença entre programação tradicional/estruturada e programação orientada a objetos (POO).
* Saber o que são classes, objetos, atributos e métodos em Python.
* Construir classes simples, com construtor (`__init__`), atributos, métodos.
* Usar métodos especiais (“dunder methods”) para sobrecarga de operadores (`__add__`, `__str__`, etc.).
* Compreender herança, sobrescrita de métodos, superclasses/subclasses.
* Entender escopo de atributos, namespaces de instâncias vs classes, uso de `__slots__` para otimizar memória.
* Saber a diferença entre cópia rasa (shallow copy) e cópia profunda (deep copy).

---

## 1. Por que usar POO?

### Programação tradicional vs POO

* Na programação “tradicional” ou estruturada, os dados (variáveis, estruturas) ficam separados das funções que operam sobre eles. Isso pode facilitar erros, porque qualquer função pode alterar os dados de qualquer modo. ([IME-USP][1])
* Em POO, cada objeto encapsula dados **e** o comportamento (métodos) que opera sobre estes dados. Isso permite:

  1. **Robustez** – controlamos melhor quem pode modificar o quê.
  2. **Adaptabilidade** – mudar partes sem quebrar tudo.
  3. **Reusabilidade** – aproveitar classes em diferentes contextos. ([IME-USP][1])

### Princípios importantes

* **Modularidade** – dividir o sistema em partes bem definidas.
* **Abstração** – identificar os conceitos essenciais que queremos representar (dados, operações) sem nos preocupar inicialmente com os detalhes de implementação.
* **Encapsulamento** – esconder os detalhes internos; disponibilizar uma interface clara.

---

## 2. Classes e Objetos

### Classe, objeto, atributos, métodos

* **Classe** é o modelo, definição de tipo (variáveis + operações).
* **Objeto** é uma instância da classe: contém seus próprios valores de atributos, mas compartilha a estrutura (métodos).

Exemplo:

```python
class Produto:
    """Define a classe Produto."""
    
    def __init__(self, nome, codigo, preco, quantidade):
        """Construtor da classe Produto."""
        self._nome = nome
        self._codigo = codigo
        self._preco = preco
        self._quantidade = quantidade

    def obtem_nome(self):
        return self._nome

    def obtem_codigo(self):
        return self._codigo

    def obtem_preco(self):
        return self._preco

    def altera_preco(self, novo_preco):
        preco_antigo = self._preco
        self._preco = novo_preco
        return novo_preco > preco_antigo

    def altera_quantidade(self, novo_pedido):
        if novo_pedido > self._quantidade:
            return False
        self._quantidade -= novo_pedido
        return True
```

* O `__init__` é o **método construtor**, chamado quando criamos uma nova instância.
* `self` refere-se ao objeto concreto. Sempre aparece como primeiro parâmetro nos métodos (embora o nome `self` seja apenas convenção). ([IME-USP][1])

### Exemplos de uso

```python
if __name__ == "__main__":
    p1 = Produto("Camisa Social", 123456, 45.56, 1000)
    p2 = Produto("Calça Jeans", 423564, 98.12, 500)

    print("Oferta do dia:", p1.obtem_nome())
    print("Oferta da semana:", p2.obtem_nome())

    if p1.altera_preco(40.00):
        print("Preço alterado hoje")
    else:
        print("Atenção - baixou o preço")

    if p2.altera_quantidade(100):
        print("Pode fazer a venda - valor total =", p2.obtem_preco() * 100)
    else:
        print("Não tem produto suficiente para esta venda")
```

---

## 3. Detalhes de sintaxe, parâmetros, self

* O primeiro parâmetro de qualquer método de instância é `self` (ou outro nome, mas convenção é `self`). É assim que dentro do método você acessa atributos do objeto. ([IME-USP][1])

* No uso/call do método, você **não** passa `self`. Por exemplo, `p1.altera_preco(40.00)` chama o método e internamente o objeto `p1` vira o `self`.

* Métodos podem ter parâmetros com valores padrão, ex:

```python
class Duplas:
    def __init__(self, p1=0, p2=0):
        self.primeiro = p1
        self.segundo = p2

    def mostra(self):
        print(f"/ {self.primeiro} {self.segundo} /")
```

Uso:

```python
x = Duplas(3, 4)
x.mostra()  # imprime "/ 3 4 /"
y = Duplas(2)
y.mostra()  # "/ 2 0 /"
z = Duplas()
z.mostra()  # "/ 0 0 /"
```

---

## 4. Métodos Especiais / Sobrecarga de Operadores

Python permite redefinir ou “sobrecargar” operadores comuns para objetos personalizados, via métodos especiais (“dunder methods”, com dois underlines: `__metodo__`).

Alguns exemplos:

* `__str__(self)`: define como objeto é convertido em string (`str(obj)`, `print(obj)`).
* `__add__(self, other)`: define o comportamento de `self + other`.
* Outros: `__sub__`, `__mul__`, `__len__`, `__getitem__`, `__setitem__`, `__eq__`, `__ne__`, etc. ([IME-USP][1])

### Exemplo: classe Duplas com `__add__` e `__str__`

```python
class Duplas:
    """Define a classe Duplas com sobrecarga de operadores."""
    def __init__(self, p1=0, p2=0):
        self.primeiro = p1
        self.segundo = p2

    def __add__(self, other):
        # soma de duas Duplas → retorna nova Duplas
        return Duplas(self.primeiro + other.primeiro,
                      self.segundo + other.segundo)

    def __str__(self):
        return f"/{self.primeiro} {self.segundo}/"
```

Uso:

```python
x = Duplas(3, 4)
print(x)          # /3 4/
y = Duplas(2)
print(y)          # /2 0/
z = x + y
print(z)          # /5 4/
print(x + x + y)  # permite compor várias somas
```

---

## 5. Herança (Inheritance)

Permite criar uma nova classe (subclasse / filha) que herda atributos e métodos de uma classe existente (classe base / superclasse).

### Exemplo: Produto e ProdutoCrítico

```python
class ProdutoCritico(Produto):
    """Define a classe Produto Crítico."""
    def __init__(self, nome, codigo, preco, quantidade, estoque_minimo):
        super().__init__(nome, codigo, preco, quantidade)
        self._estoque_minimo = estoque_minimo

    def altera_quantidade(self, novo_pedido):
        # rejeita se a venda deixaria abaixo do estoque mínimo
        if novo_pedido + self._estoque_minimo > self._quantidade:
            return False
        return super().altera_quantidade(novo_pedido)

    def altera_preco(self, novo_preco):
        pp = self._preco
        # permitir mudança de preço apenas até ±10%
        if novo_preco > 1.1 * pp or novo_preco < 0.9 * pp:
            return False
        super().altera_preco(novo_preco)
        return True
```

* A subclasse `ProdutoCritico` herda tudo de `Produto` (atributos e métodos), mas especializa/completa algumas funcionalidades.
* Uso de `super()` para chamar métodos da classe base dentro da classe filha.

---

## 6. Atributos de Classe, `__slots__` e Namespace

### Atributos de classe

* Você pode definir valores que são compartilhados por todas as instâncias da classe — constantes ou valores padrão.
* Exemplo no material: definir algo como `PRECO_MINIMO` ou `ESTOQUE_MINIMO_POSSIVEL` diretamente na classe. ([IME-USP][1])

```python
class Produto:
    PRECO_MINIMO = 1.00
    ESTOQUE_MINIMO_POSSIVEL = 5
    ...
```

### `__slots__`

* Por padrão, cada instância de classe em Python tem um dicionário interno (`__dict__`) para guardar atributos. Isso consome memória.
* Se você sabe de antemão quais serão os atributos usados, pode definir `__slots__ = (…)` para restringir quais atributos a instância pode ter, evitando o dicionário comum. Isso reduz uso de memória. ([IME-USP][1])

```python
class Produto:
    __slots__ = ('_nome', '_codigo', '_preco', '_quantidade')
    ...
```

E na classe filha:

```python
class ProdutoCritico(Produto):
    __slots__ = ('_estoque_minimo',)
    ...
```

---

## 7. Namespace, Escopo, Resolução de Nomes

Quando você acessa um atributo ou método de um objeto (via `obj.alguma_coisa`), a procura (“lookup”) segue esta ordem:

1. Verifica se esse nome existe nos atributos da instância (`obj`).
2. Se não, procura na classe da instância.
3. Se ainda não, vai subindo nas classes herdadas (superclasses) até encontrar ou dar erro. ([IME-USP][1])

Isso explica como a sobrescrita de métodos funciona: se uma subclasse define um método com o mesmo nome de sua superclasse, o método da subclasse “oculta” (overrides) o da superclasse para instâncias dessa subclasse.

---

## 8. Cópias de Objetos: shallow vs deep

* Atribuir `x = y` não cria uma nova cópia de objeto — apenas cria um novo nome/sinônimo para o mesmo objeto. ([IME-USP][1])
* **Shallow copy**: cria uma nova instância ou estrutura “externa”, mas os componentes internos ainda são referências aos mesmos objetos.
* **Deep copy**: duplica tudo recursivamente, para que nada seja compartilhado (se for objeto mutável). Usamos o módulo `copy` de Python: `copy.copy()` (shallow) e `copy.deepcopy()` (profundo). ([IME-USP][1])

Exemplo:

```python
import copy

x = [[32, 45], [81, 37, 75]]
y = list(x)    # shallow copy
x[0][0] = -1
print(x, y)    # y também vai “ver” a alteração

x2 = [[32, 45], [81, 37, 75]]
y2 = copy.deepcopy(x2)
x2[0][0] = -1
print(x2, y2)  # y2 permanece intacto
```

---

## 9. Exemplos Práticos Adicionais

Aqui vão mais exemplos para fixar os conceitos.

### Exemplo A: Classe para representar um “Aluno”

```python
class Aluno:
    def __init__(self, nome, matricula, notas=None):
        self.nome = nome
        self.matricula = matricula
        # notas é uma lista de floats
        if notas is None:
            self.notas = []
        else:
            self.notas = list(notas)

    def adiciona_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            raise ValueError("Nota deve estar entre 0 e 10")

    def media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"Aluno: {self.nome} ({self.matricula}), Média: {self.media():.2f}"
```

Uso:

```python
a = Aluno("Maria", "2021001", [8.5, 7.0, 9.0])
print(a)  # Aluno: Maria (2021001), Média: 8.17
a.adiciona_nota(10)
print(a.media())  # 8.625
```

### Exemplo B: Classe para representar um **vetor** com mais operações

```python
class Vetor:
    def __init__(self, coords):
        # coords deve ser lista de números
        self._coords = list(coords)

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, index):
        return self._coords[index]

    def __setitem__(self, index, valor):
        self._coords[index] = valor

    def __add__(self, outro):
        if len(self) != len(outro):
            raise ValueError("Vetores devem ter mesma dimensão")
        soma = [self[i] + outro[i] for i in range(len(self))]
        return Vetor(soma)

    def __eq__(self, outro):
        return self._coords == outro._coords

    def __str__(self):
        return f"Vetor({self._coords})"
```

Uso:

```python
v1 = Vetor([1, 2, 3])
v2 = Vetor([4, 5, 6])
v3 = v1 + v2
print(v1, v2, v3)  # Vetor([1,2,3]) etc.
print(v3 == Vetor([5,7,9]))  # True
```

---

## 10. Exercícios sugeridos

Aqui vão alguns exercícios para praticar:

1. **Extender a classe Duplas**

   * Adicione métodos para subtração, multiplicação e divisão (`__sub__`, `__mul__`, `__truediv__`).
   * Teste comportamentos como `x - y`, `x * y`, etc.

2. **Classe Racional**

   * Crie uma classe `Racional` que representa frações (numerador/denominador).
   * Métodos: soma, subtração, multiplicação, divisão, simplificação automática (usar o máximo divisor comum).
   * Redefinir `__str__` para mostrar “a/b”.
   * Comparações (`__eq__`, `__lt__`, etc.) para poder ordenar racionais.

3. **Classe Banco/Conta**

   * Classe base `Conta` com métodos `depositar`, `sacar` etc.
   * Classe `ContaEspecial` que herda de `Conta` e tem limite de cheque especial.
   * Validar saldo/limite antes de permitir saque.

4. **Implementar cópia profunda**

   * Crie uma classe que contenha atributos mutáveis (listas, outras estruturas).
   * Mostre que uma shallow copy causa “vazamento” de modificações.
   * Use `deepcopy` para evitar isso.

