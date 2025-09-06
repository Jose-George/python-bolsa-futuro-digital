## 📝 Questões

**1. (Conceitual)**
Explique com suas palavras qual é a principal diferença entre a **programação estrutural** e a **programação orientada a objetos**.

---

**2. (Código)**
Observe o código abaixo. Qual é a saída do `print`?

```python
class Carro:
    rodas = 4  # atributo de classe

    def __init__(self, modelo):
        self.modelo = modelo  # atributo de instância

c1 = Carro("Civic")
c2 = Carro("Corolla")
print(c1.rodas, c2.rodas, Carro.rodas)
```

---

**3. (Conceitual)**
Qual a função do método especial `__init__` em uma classe Python? O que acontece se você esquecer de implementá-lo?

---

**4. (Código — armadilha)**
Analise o seguinte código e explique o que acontecerá ao final. Depois, corrija o problema.

```python
class Sala:
    alunos = []  # atributo de classe (mutável)

    def adicionar(self, nome):
        self.alunos.append(nome)

a = Sala()
b = Sala()
a.adicionar("Ana")
print(b.alunos)  # ???
```

---

**5. (Encapsulamento)**
Por que usamos `@property` em Python? Cite uma vantagem em relação a acessar diretamente atributos da instância.

---

**6. (Código)**
Complete a classe abaixo para que `area` e `perimetro` funcionem como propriedades de leitura:

```python
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # complete aqui
```

---

**7. (Classmethod)**
Explique a diferença entre um **método de instância** e um **método de classe**. Dê um exemplo de situação em que `@classmethod` é útil.

---

**8. (Código)**
O código abaixo deve criar uma conta e impedir depósitos inválidos (≤ 0). O que falta para que a validação funcione?

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
```

---

**9. (Situação prática)**
Implemente rapidamente uma classe `Pessoa` que tenha:

* atributos `nome` e `idade`;
* um método `cumprimentar()` que retorna `"Olá, eu sou {nome}"`.

---

**10. (Conceitual — integração)**
Em projetos maiores, por que a POO costuma facilitar manutenção e evolução do código em comparação com a programação estrutural?
