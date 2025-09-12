Perfeito 👍
Aqui está o **gabarito completo** para os exercícios da aula, em **Python**, com soluções comentadas.

---

# 📘 Gabarito dos Exercícios de POO em Python

## 🔹 Nível 1 — Fundamentos

### 1) Classe `Livro`

```python
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def resumo(self):
        return f"{self.titulo} por {self.autor} — {self.paginas} páginas"

    def __repr__(self):
        return f"Livro(titulo={self.titulo!r}, autor={self.autor!r}, paginas={self.paginas})"


# Teste
livro = Livro("Python para Iniciantes", "José", 300)
print(livro.resumo())  
```

---

### 2) Classe `Carro`

```python
class Carro:
    def __init__(self, modelo, velocidade=0):
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade = max(0, self.velocidade - valor)

    def __repr__(self):
        return f"Carro(modelo={self.modelo!r}, velocidade={self.velocidade})"


# Teste
c = Carro("Fusca")
c.acelerar(50)
c.frear(30)
print(c)  
```

---

## 🔹 Nível 2 — Encapsulamento e Propriedades

### 3) Classe `Produto`

```python
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self._preco = None
        self._estoque = None
        self.preco = preco
        self.estoque = estoque

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo")
        self._estoque = valor

    def __repr__(self):
        return f"Produto(nome={self.nome!r}, preco={self.preco}, estoque={self.estoque})"


# Teste
p = Produto("Camiseta", 50, 10)
p.estoque += 5
print(p)  
```

---

### 4) Classe `Funcionario`

```python
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo, forcar=False):
        if novo < self._salario and not forcar:
            raise ValueError("Redução de salário não permitida sem autorização")
        self._salario = novo

    def __repr__(self):
        return f"Funcionario(nome={self.nome!r}, salario={self.salario})"


# Teste
f = Funcionario("Ana", 5000)
f.salario = 6000  # aumento
# f.salario = 4000  # gera erro
f.salario = 4000, True  # forçando reduzir
```

---

## 🔹 Nível 3 — Herança e Polimorfismo

### 5) Meios de Transporte

```python
from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def velocidade_maxima(self):
        pass

class Carro(Transporte):
    def velocidade_maxima(self):
        return 180

class Bicicleta(Transporte):
    def velocidade_maxima(self):
        return 40


# Teste
transportes = [Carro(), Bicicleta()]
for t in transportes:
    print(f"{t.__class__.__name__}: {t.velocidade_maxima()} km/h")
```

---

### 6) Formas geométricas

```python
from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * self.raio**2

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2

def area_total(formas):
    return sum(f.area() for f in formas)


# Teste
formas = [Circulo(3), Retangulo(4, 5), Triangulo(6, 7)]
print("Área total:", area_total(formas))
```

---

## 🔹 Nível 4 — Composição e Mini-projetos

### 7) Biblioteca

```python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if not self.disponivel:
            raise ValueError("Livro já emprestado")
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

    def __repr__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Livro({self.titulo}, {self.autor}, {status})"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def buscar_por_autor(self, autor):
        return [l for l in self.livros if l.autor == autor]

    def emprestar(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.emprestar()
                return
        raise ValueError("Livro não disponível")


# Teste
b = Biblioteca()
b.adicionar(Livro("1984", "George Orwell"))
b.adicionar(Livro("A Revolução dos Bichos", "George Orwell"))
b.emprestar("1984")
print(b.livros)
```

---

### 8) Pedidos

```python
class Item:
    def __init__(self, nome, preco, qtd=1):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def subtotal(self):
        return self.preco * self.qtd

    def __repr__(self):
        return f"{self.nome} x{self.qtd} = R$ {self.subtotal():.2f}"


class Cupom:
    def __init__(self, codigo, desconto_percentual):
        self.codigo = codigo
        self.desconto = desconto_percentual / 100.0

    def aplicar(self, valor):
        return valor * (1 - self.desconto)


class Pedido:
    def __init__(self):
        self.itens = []
        self.cupom = None

    def adicionar_item(self, item: Item):
        self.itens.append(item)

    def aplicar_cupom(self, cupom: Cupom):
        self.cupom = cupom

    def total(self):
        subtotal = sum(i.subtotal() for i in self.itens)
        if self.cupom:
            return self.cupom.aplicar(subtotal)
        return subtotal

    def __repr__(self):
        itens_str = "\n".join(str(i) for i in self.itens)
        return f"Pedido:\n{itens_str}\nTotal: R$ {self.total():.2f}"


# Teste
pedido = Pedido()
pedido.adicionar_item(Item("Camisa", 50, 2))
pedido.adicionar_item(Item("Calça", 120, 1))
pedido.aplicar_cupom(Cupom("DESC10", 10))
print(pedido)
```

---

✅ **Resumo:**

* Todos os exercícios foram resolvidos usando os conceitos de **classes, encapsulamento, propriedades, herança, polimorfismo, abstração e composição**.
* Os exemplos podem ser expandidos em projetos maiores (ex.: sistema bancário, catálogo de cursos, sistema de biblioteca).

