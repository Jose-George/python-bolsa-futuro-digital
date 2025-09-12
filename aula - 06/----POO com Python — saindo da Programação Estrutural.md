# Aula: POO com Python — saindo da Programação Estrutural

> **Contexto:** até aqui, trabalhamos com **programação estrutural** (funções, variáveis globais/locais, condicionais, laços). Agora vamos ver **outro paradigma** — **Programação Orientada a Objetos (POO)** — que organiza o código em **classes** e **objetos**.

---

## 📑 Índice Geral

1. Introdução rápida: do estrutural ao orientado a objetos
2. Estrutural vs Orientado a Objetos: principais diferenças
3. Conceitos fundamentais

   * Classes e objetos
   * Atributos (de instância e de classe)
   * Métodos (de instância, de classe, estáticos)
   * Construtor `__init__` e o papel do `self`
   * Encapsulamento e propriedades (`@property`) --
   * Herança (simples e múltipla), `super()`
   * Polimorfismo e *duck typing*
   * Abstração e classes abstratas (`abc`)
   * Composição vs. herança
4. POO na prática (exemplos guiados)

   * Modelo “ContaBancaria”
   * Mini-sistema “Catálogo de Cursos” com herança e polimorfismo
5. Dicas, boas práticas e erros comuns
6. Exercícios propostos (com níveis)
7. Próximos passos e caminhos de estudo

---

## 1) Introdução rápida: do estrutural ao orientado a objetos

* **Programação estrutural:** você resolve problemas quebrando em **passos** (funções e fluxos). O foco é **o que fazer** e **em que ordem**.
* **POO:** você modela **coisas** (objetos) com **estado** (dados) e **comportamentos** (métodos). O foco é **quem faz** e **com quais responsabilidades**.

**Por que migrar?**
POO facilita **organização**, **reuso**, **evolução** e **manutenção** em sistemas médios/grandes. Você aproxima o código do **domínio do problema** (ex.: Conta, Aluno, Pedido, Fatura).

---

## 2) Estrutural vs Orientado a Objetos: principais diferenças

| Aspecto       | Estrutural                               | Orientado a Objetos                                 |
| ------------- | ---------------------------------------- | --------------------------------------------------- |
| Organização   | Arquivos com funções e dados soltos      | **Classes** agrupam dados e comportamentos          |
| Reuso         | Funções reutilizáveis                    | **Herança**, **composição** e **polimorfismo**      |
| Estado        | Variáveis passam por funções             | **Objetos** mantêm **estado interno**               |
| Acoplamento   | Pode crescer rápido em projetos grandes  | Encapsulamento ajuda a **reduzir acoplamento**      |
| Testabilidade | Testa funções isoladas                   | Testa **métodos e interações** entre objetos        |
| Evolução      | Mudanças podem “vazar” por todo o código | **Responsabilidades claras** e contratos por classe |

> **Regra de bolso:** quando o problema tem “coisas” bem definidas e que **evoluem**, POO tende a simplificar.

---

## 3) Conceitos fundamentais 

### 3.1 Classes e objetos

* **Classe** = molde/definição do que um objeto **é** e **faz**.
* **Objeto** = instância concreta dessa classe em tempo de execução.

```python
class Pessoa:
    """Modelo de uma pessoa com nome e idade."""
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa("Ana", 28)  # objeto/instância
```

**Dica:** pense na classe como **substantivo** (Pessoa, Conta, Pedido) e nos métodos como **verbos** (falar, sacar, fechar).

---

### 3.2 Atributos (de instância e de classe)

* **Atributos de instância:** pertencem **a cada objeto**.
* **Atributos de classe:** pertencem **à classe** (compartilhados por todas as instâncias).

```python
class Config:
    versao = "1.0.0"           # atributo de classe

class Conta:
    taxa_adm = 0.01            # atributo de classe
    def __init__(self, numero, saldo=0):
        self.numero = numero   # atributo de instância
        self.saldo = saldo     # atributo de instância
```

> **Cuidado:** alterar `Classe.atributo` muda para todos; alterar `obj.atributo` muda apenas para aquela instância.

---

### 3.3 Métodos (instância, classe e estáticos)

* **Método de instância:** recebe `self` (o próprio objeto).
* **Método de classe:** recebe `cls` (a própria classe), usa `@classmethod`.
* **Método estático:** não recebe `self` nem `cls`, usa `@staticmethod`.

```python
class Moeda:
    fator = 5.0

    def __init__(self, valor):
        self.valor = valor

    def em_reais(self):
        return self.valor * Moeda.fator

    @classmethod
    def atualizar_fator(cls, novo):
        cls.fator = float(novo)

    @staticmethod
    def eh_numero(v):
        return isinstance(v, (int, float))
```

**Dica prática:** comece com **métodos de instância**; crie `@classmethod` quando precisar **fabricar** objetos (construtores alternativos) ou alterar **estado da classe**; use `@staticmethod` para utilidades **relacionadas** à classe.

---

### 3.4 Construtor `__init__` e o papel do `self`

* `__init__` roda **após** a criação do objeto e inicializa o estado.
* `self` é a **referência** à instância (como `this` em outras linguagens).

```python
class Usuario:
    def __init__(self, email, ativo=True):
        self.email = email
        self.ativo = ativo
```

> **Erro comum:** esquecer `self` como primeiro parâmetro de métodos de instância.

---

### 3.5 Encapsulamento e propriedades (`@property`)

Python usa **convenções**:

* `_privado`: “uso interno” (protegido por convenção).
* `__muito_privado`: *name mangling* (evita colisão em herança).

Use `@property` para **controlar acesso** (getters/setters elegantes):

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = 0.0
        self.preco = preco  # usa o setter

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = float(valor)
```

**Benefício:** você expõe `obj.preco`, mas mantém validação e pode mudar a implementação sem quebrar quem usa.

---

### 3.6 Herança (simples e múltipla), `super()`

* **Herança**: classe filha **reaproveita** e **especializa** a classe base.
* Use `super()` para **aproveitar** inicialização e comportamento do pai.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        return "..."

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)    # chama Animal.__init__
        self.raca = raca
    def falar(self):
        return "Au au!"
```

> **Regra de ouro:** prefira **composição** (ter um objeto dentro de outro) quando a relação não for “é um”, e sim “tem um”.

---

### 3.7 Polimorfismo e *duck typing*

* **Polimorfismo:** objetos diferentes respondem ao **mesmo método**.
* **Duck typing:** “se anda como pato e grasna como pato… é um pato”; foque em **comportamentos**, não no tipo.

```python
def emitir_som(animal):
    # Não me importo se é Cachorro, Gato ou Pato: só preciso de .falar()
    print(animal.falar())
```

**Dica:** escreva funções que dependem de **interfaces comportamentais**, não de classes específicas.

---

### 3.8 Abstração e classes abstratas (`abc`)

* Abstração: expor **o essencial** e esconder detalhes.
* Use `abc.ABC` e `@abstractmethod` para **contratos**.

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self): ...

class Retangulo(Forma):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
```

---

### 3.9 Composição vs. herança

* **Herança:** `Cachorro` **é um** `Animal`.
* **Composição:** `Pedido` **tem** `Itens`.
  Composição reduz acoplamento e evita hierarquias profundas.

```python
class Item:
    def __init__(self, nome, preco): ...
class Pedido:
    def __init__(self):
        self.itens = []  # composição
```

---

## 4) POO na prática (exemplos guiados)

### 4.1 Modelo “ContaBancaria” (encapsulamento + propriedades)

```python
class ContaBancaria:
    def __init__(self, numero, titular, saldo=0.0, limite=500.0):
        self.numero = str(numero)
        self.titular = titular
        self._saldo = float(saldo)
        self._limite = float(limite)

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, novo_limite):
        if novo_limite < 0:
            raise ValueError("Limite não pode ser negativo.")
        self._limite = float(novo_limite)

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Saque deve ser positivo.")
        if valor > self._saldo + self._limite:
            raise ValueError("Saldo insuficiente considerando o limite.")
        self._saldo -= valor

    def transferir(self, valor, outra_conta: "ContaBancaria"):
        self.sacar(valor)
        outra_conta.depositar(valor)

    def __repr__(self):
        return f"ContaBancaria(numero={self.numero!r}, titular={self.titular!r}, saldo={self.saldo:.2f})"
```

**Pontos didáticos:**

* `@property` protege e valida.
* `__repr__` ajuda no *debug* (representação legível).
* Métodos mantêm **invariantes** (ex.: sem saldo negativo sem limite).

---

### 4.2 Mini-sistema “Catálogo de Cursos” (herança + polimorfismo + composição)

```python
from abc import ABC, abstractmethod

class Curso(ABC):
    def __init__(self, titulo, carga_horaria):
        self.titulo = titulo
        self.carga_horaria = carga_horaria

    @abstractmethod
    def preco(self):
        ...

    def descricao(self):
        return f"{self.titulo} ({self.carga_horaria}h)"

class CursoLivre(Curso):
    def __init__(self, titulo, carga_horaria, preco_base):
        super().__init__(titulo, carga_horaria)
        self.preco_base = preco_base
    def preco(self):
        return self.preco_base

class CursoProfissionalizante(Curso):
    def __init__(self, titulo, carga_horaria, preco_base, certificacao=True):
        super().__init__(titulo, carga_horaria)
        self.preco_base = preco_base
        self.certificacao = certificacao
    def preco(self):
        return self.preco_base * (1.2 if self.certificacao else 1.0)

class Catalogo:
    def __init__(self):
        self._cursos = []  # composição
    def adicionar(self, curso: Curso):
        self._cursos.append(curso)
    def listar(self):
        for c in self._cursos:
            print(f"- {c.descricao()} | R$ {c.preco():.2f}")

cat = Catalogo()
cat.adicionar(CursoLivre("Python do Zero", 20, 99.0))
cat.adicionar(CursoProfissionalizante("POO com Python", 40, 199.0, certificacao=True))
cat.listar()
```

**Observe:**

* `Curso` define **contrato** (`preco()` abstrato).
* Subclasses **polimórficas** implementam `preco()` diferente.
* `Catalogo` **compõe** cursos sem saber detalhes internos (*duck typing*).

---

## 5) Dicas, boas práticas e erros comuns

### Boas práticas

* **Nomeação:** `CamelCase` para classes (`MinhaClasse`), `snake_case` para métodos/atributos (`meu_metodo`).
* **SRP (Responsabilidade Única):** uma classe deve ter **um motivo** para mudar.
* **`__repr__` e `__str__`:** implemente pelo menos `__repr__` para facilitar *debug*.
* **`dataclasses`:** para modelos “de dados” simples.

```python
from dataclasses import dataclass

@dataclass
class Endereco:
    rua: str
    numero: int
    cidade: str
```

* **Evite** usar herança para “reuso preguiçoso”; prefira **composição**.
* **Documente** com *docstrings* e tipos (anotações `->`), isso ajuda IDEs e *linters*.
* **Teste** comportamentos públicos (métodos), não detalhes internos.

### Erros comuns

* Esquecer `self` nos métodos de instância.
* Expor todos os atributos publicamente sem necessidade (falta de `@property`).
* Usar herança onde composição seria melhor.
* Colocar “regras de negócio” fora dos objetos (perdendo encapsulamento).
* Criar “*God Objects*” (classes gigantes com muitas responsabilidades).

---

## 6) Exercícios propostos

**Nível 1 — Fundamentos**

1. **Livro**: crie `Livro(titulo, autor, paginas)` com `__repr__` e método `resumo()` que mostra “`<titulo>` por `<autor>` — `<paginas>` páginas”.
2. **Carro**: com `velocidade_atual`, `acelerar(v)`, `frear(v)` (não permitir velocidade negativa).

**Nível 2 — Encapsulamento e propriedades**
3\. **Produto**: validar `preco >= 0` e `estoque >= 0` com `@property`.
4\. **Funcionario**: `salario` não pode reduzir via setter sem autorização (parâmetro `forcar=False`).

**Nível 3 — Herança e polimorfismo**
5\. **Meios de Transporte**: `Transporte.velocidade_maxima()` abstrato; `Carro` e `Bicicleta` implementam com regras próprias.
6\. **Formas**: `Forma.area()` abstrato; `Circulo`, `Retangulo`, `Triangulo` implementam. Uma função `area_total(formas)` soma áreas polimorficamente.

**Nível 4 — Composição e mini-projeto**
7\. **Biblioteca**: `Biblioteca` contém `Livros`; métodos `adicionar`, `buscar_por_autor`, `emprestar` (mudar estado).
8\. **Pedidos**: `Pedido` com itens (`Item`), calcular total, aplicar cupom (objeto `Cupom` com regra própria).

> **Desafio extra:** reimplemente um exercício usando **dataclasses** e outro usando **`@classmethod`** como construtor alternativo (ex.: `from_dict`).

---

## 7) Próximos passos e caminhos de estudo

1. **Refatorar** scripts estruturais antigos em POO (ex.: “planilha de alunos” → `Aluno`, `Turma`, `Boletim`).
2. Estudar:

   * **PEP 8** (estilo de código) e *type hints* (`mypy`).
   * **`abc`**, **`dataclasses`**, **`functools.total_ordering`** (comparações), **`enum`** (constantes simbólicas).
   * **Padrões de Projeto (Design Patterns)**: Strategy, Factory, Adapter, Observer (aplicados em Python).
3. **Projetos guiados**:

   * **Sistema financeiro simples**: `Conta`, `Cliente`, `Transacao` com histórico.
   * **Gerenciador de tarefas**: tarefas com estados, filtros e persistência em JSON.
   * **Catálogo de produtos**: com preços, estoque, carrinho e cupons.
4. **Teste automatizado**: `pytest` para validar comportamentos de classes.
5. **Leitura recomendada**: busque por “Python OOP tutorial”, “PEP 8”, “Python dataclasses”, “ABC module”. (Foquem em fontes oficiais e tutoriais reconhecidos.)

---

### 🧭 Checklist rápido antes de seguir

* [ ] Sei explicar **classe**, **objeto**, **atributo**, **método**
* [ ] Diferencio **atributo de classe** vs **de instância**
* [ ] Sei usar `@property` e validar dados
* [ ] Entendo **herança** e quando **evitar** (preferir composição)
* [ ] Sei aplicar **polimorfismo** (*duck typing*)
* [ ] Consigo modelar um mini-projeto com 2–3 classes

