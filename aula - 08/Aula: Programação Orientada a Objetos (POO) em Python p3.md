# Aula: Programação Orientada a Objetos (POO) em Python

Bem-vindos!  
Hoje vamos aprender **conceitos fundamentais de POO em Python**, com foco em:

- Construtor `__init__`
- Palavra-chave `self`
- Sobrecarga de métodos
- Escopo de atributos
- Namespaces de instâncias vs. classes
- Uso de `__slots__` para otimizar memória
- Diferença entre **cópia rasa (shallow copy)** e **cópia profunda (deep copy)**

---

## 1. Relembrando: O que é POO?

- **Programação Orientada a Objetos** é um jeito de programar em que organizamos o código em **classes** (modelos) e **objetos** (instâncias).
- Uma **classe** é como uma **planta de uma casa**.
- Um **objeto** é a **casa construída**.

Exemplo básico:

```python
class Pessoa:
    pass

# Criando um objeto (instância)
p1 = Pessoa()
print(type(p1))  # <class '__main__.Pessoa'>
````

---

## 2. O Construtor `__init__`

* O método `__init__` é chamado **automaticamente** quando criamos um objeto.
* Ele serve para **inicializar** os atributos do objeto.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome    # atributo de instância
        self.idade = idade

p1 = Pessoa("Ana", 25)
print(p1.nome)  # Ana
print(p1.idade) # 25
```

### Por que `self`?

* **`self`** é a forma do Python se referir **ao próprio objeto**.
* Você sempre precisa dele nos métodos de instância.

> **Dica:** O nome `self` não é obrigatório, mas é **convenção**.
> Poderia ser `this` ou `obj`, mas quase todo mundo usa `self`.

---

## 3. Sobrecarga de Métodos

Em Python, **não existe** sobrecarga como em outras linguagens (como Java ou C++).
Mas podemos simular passando **valores padrão** ou usando `*args` e `**kwargs`.

```python
class Calculadora:
    def soma(self, a, b=0):
        return a + b

c = Calculadora()
print(c.soma(5))      # 5  (usa b=0)
print(c.soma(5, 10))  # 15
```

Outra forma é verificar os argumentos:

```python
class Mensagem:
    def enviar(self, *args):
        if len(args) == 1:
            print(f"Enviando para: {args[0]}")
        elif len(args) == 2:
            print(f"Enviando para: {args[0]} com assunto: {args[1]}")
        else:
            print("Nenhum argumento válido")

m = Mensagem()
m.enviar("Maria")
m.enviar("Maria", "Aviso")
```

---

## 4. Escopo de Atributos

### Atributo de Instância

* Pertence **a cada objeto**.

### Atributo de Classe

* Compartilhado por **todas as instâncias**.

```python
class Carro:
    rodas = 4  # atributo de classe

    def __init__(self, cor):
        self.cor = cor  # atributo de instância

carro1 = Carro("vermelho")
carro2 = Carro("azul")

print(carro1.rodas, carro2.rodas)  # 4 4
print(carro1.cor, carro2.cor)      # vermelho azul

Carro.rodas = 6
print(carro1.rodas, carro2.rodas)  # 6 6 (mudou para todos!)
```

---

## 5. Namespaces: Instância vs Classe

* Cada **objeto** tem seu **namespace** (espaço de nomes).
* A classe também tem o seu.

```python
class Animal:
    especie = "Desconhecida"

a = Animal()
print(a.__dict__)        # {}  (nenhum atributo de instância)
print(Animal.__dict__)   # mostra atributos da classe
```

Quando você acessa `a.especie`, o Python:

1. Procura em `a.__dict__` (instância).
2. Se não encontrar, procura em `Animal.__dict__` (classe).

---

## 6. Otimizando Memória com `__slots__`

* Por padrão, cada objeto tem um dicionário interno para guardar atributos.
* Isso gasta mais memória.
* Com `__slots__`, você define **quais atributos podem existir**, economizando memória.

```python
class Ponto:
    __slots__ = ("x", "y")  # apenas estes atributos
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Ponto(1, 2)
# p.z = 3  # ERRO! Não é permitido.
```

Útil quando vamos criar **muitos objetos**.

---

## 7. Cópia Rasa (Shallow Copy) vs Cópia Profunda (Deep Copy)

Quando copiamos objetos em Python:

### Cópia Rasa

* Cria uma **nova lista**, mas **os objetos internos são os mesmos** (compartilhados).

```python
import copy

lista1 = [[1, 2], [3, 4]]
copia_rasa = copy.copy(lista1)

copia_rasa[0][0] = 99
print(lista1)  # [[99, 2], [3, 4]]  <- alterou também!
```

### Cópia Profunda

* Cria uma **nova lista** e **novos objetos internos**.

```python
import copy

lista1 = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(lista1)

copia_profunda[0][0] = 99
print(lista1)  # [[1, 2], [3, 4]]   <- não mudou
```

---

## 8. Exercícios Práticos

1. Crie uma classe `Aluno` com atributos `nome` e `nota`.

   * Crie um método que mostre se o aluno foi aprovado (nota >= 6).

2. Implemente uma classe `ContaBancaria`:

   * Construtor com saldo inicial.
   * Métodos `depositar` e `sacar`.
   * Um atributo de classe para taxa de operação.

3. Crie uma classe `Produto` com `__slots__` para `nome` e `preco`.

   * Tente adicionar um atributo `estoque` e veja o que acontece.

---

## Resumo da Aula

* **`__init__`** inicializa objetos.
* **`self`** é a referência ao próprio objeto.
* Python não tem **sobrecarga verdadeira**, mas podemos simular.
* **Atributos de instância** são únicos de cada objeto; **de classe** são compartilhados.
* **Namespaces** mostram onde o Python procura atributos.
* **`__slots__`** limita atributos e economiza memória.
* **Shallow copy** compartilha referências; **deep copy** duplica tudo.

