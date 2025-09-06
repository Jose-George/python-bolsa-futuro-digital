# Aula Interativa: Programação Orientada a Objetos (POO) com Python 🐍

**🎯 Objetivo da aula:** entender os fundamentos da POO em Python — por que usar, como modelar problemas com classes/objetos, atributos e métodos (instância/classe/estáticos), o papel do `__init__` e do `self`, e como aplicar encapsulamento com `@property`. 
> **📋 Pré-requisitos:** noções básicas de Python (variáveis, listas/dicionários, funções, fluxo condicional).

---

## 🚀 1. Introdução: Do Estrutural ao Orientado a Objetos

<div class="animation-container" style="border: 1px solid #ccc; padding: 15px; border-radius: 10px; margin: 10px 0;">
  <div class="code-transition">
    <div class="procedural-code" style="color: #ff6b6b;">
      <h4>👨‍💻 Programação Estrutural (Procedural)</h4>
      <p>➡️ Organização em <em>funções</em> que manipulam dados separados</p>
      <p>📊 Dados e comportamentos espalhados</p>
    </div>
    <div class="arrow" style="text-align: center; font-size: 24px;">↓</div>
    <div class="oop-code" style="color: #1dd1a1;">
      <h4>🧩 Programação Orientada a Objetos (POO)</h4>
      <p>➡️ <em>Dados + comportamentos</em> empacotados juntos em <strong>objetos</strong></p>
      <p>📦 Modela "coisas" do mundo real como classes</p>
    </div>
  </div>
</div>

**🎭 Exemplo Rápido: Estrutural vs OOP**

```python
# 🏗️ ESTRUTURAL
contas = []

def criar_conta(nome, saldo):
    contas.append({"nome": nome, "saldo": saldo})

def depositar(nome, valor):
    for c in contas:
        if c["nome"] == nome:
            c["saldo"] += valor

# 🧩 ORIENTADO A OBJETOS
class Conta:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

conta = Conta("Ana", 100)
conta.depositar(50)  # ✅ Mais organizado e intuitivo
```

---

## 📊 2) Estrutural vs Orientado a Objetos: Principais Diferenças

| Aspecto       | 🏗️ Estrutural                               | 🧩 Orientado a Objetos                                 |
| ------------- | ---------------------------------------- | --------------------------------------------------- |
| 📦 Organização   | Arquivos com funções e dados soltos      | **Classes** agrupam dados e comportamentos          |
| 🔁 Reuso         | Funções reutilizáveis                    | **Herança**, **composição** e **polimorfismo**      |
| 🎛️ Estado        | Variáveis passam por funções             | **Objetos** mantêm **estado interno**               |
| 🔗 Acoplamento   | Pode crescer rápido em projetos grandes  | Encapsulamento ajuda a **reduzir acoplamento**      |
| 🧪 Testabilidade | Testa funções isoladas                   | Testa **métodos e interações** entre objetos        |
| 📈 Evolução      | Mudanças podem "vazar" por todo o código | **Responsabilidades claras** e contratos por classe |

> **💡 Regra de bolso:** quando o problema tem "coisas" bem definidas e que **evoluem**, POO tende a simplificar.

---

# 🧠 3. Conceitos Fundamentais

## 3.1 🧩 Classes e Objetos

* **📐 Classe**: molde (blueprint) que define atributos e métodos
* **🎭 Objeto (instância)**: entidade criada a partir da classe

```python
class Pessoa:
    pass

p = Pessoa()  # 🎭 p é um objeto/instância da classe Pessoa
```

### 🎯 Exemplo Concreto

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"👋 Olá, eu sou {self.nome} e tenho {self.idade} anos."

joao = Pessoa("João", 30)
print(joao.cumprimentar())  # 👋 Olá, eu sou João e tenho 30 anos.
```

**📝 Observação:** `Pessoa` é a classe; `joao` é a instância.

---

## 3.2 📦 Atributos (de Instância e de Classe)

### 🎯 Atributos de Instância

* Definidos dentro de `__init__` (ou adicionados a `self`)
* Cada instância tem seus próprios valores

```python
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo  # 🎯 atributo de instância
```

### 🔗 Atributos de Classe

* Definidos diretamente na classe; compartilhados entre todas as instâncias
* Úteis para constantes ou contadores

```python
class Carro:
    rodas = 4  # 🔗 atributo de classe

c1 = Carro("Civic")
c2 = Carro("Corolla")
print(Carro.rodas, c1.rodas, c2.rodas)  # 4 4 4
```

### ⚠️ Exemplo de Armadilha com Objetos Mutáveis

```python
class Exemplo:
    itens = []  # ⚠️ atributo de classe — mutável!

a = Exemplo()
b = Exemplo()
a.itens.append(1)
print(b.itens)  # [1]  -> ambos veem a mesma lista
```

**✅ Solução:** usar `None` como padrão em `__init__` e criar uma nova lista por instância:

```python
class Exemplo:
    def __init__(self, itens=None):
        self.itens = [] if itens is None else itens
```

---

## 3.3 ⚙️ Métodos: de Instância, de Classe e Estáticos

### 🎯 Método de Instância

* Primeiro parâmetro `self` — referência à instância
* Acessa atributos da instância

```python
class Conta:
    def sacar(self, valor):
        self.saldo -= valor
```

### 🔗 `@classmethod`

* Recebe `cls` como primeiro parâmetro (referência à classe)
* Útil para construtores alternativos

```python
class Pessoa:
    especie = "Humano"

    @classmethod
    def criar_de_string(cls, texto):
        nome, idade = texto.split(",")
        return cls(nome.strip(), int(idade.strip()))
```

### 🛠️ `@staticmethod`

* Não recebe `self` nem `cls`
* Função utilitária relacionada à classe

```python
class Matematica:
    @staticmethod
    def soma(a, b):
        return a + b
```

**📊 Resumo Rápido:**

| Tipo | Recebe | Uso |
|------|--------|-----|
| 🎯 Instância | `self` | Opera sobre dados da instância |
| 🔗 Classmethod | `cls` | Opera sobre a classe |
| 🛠️ Staticmethod | Nada | Função utilitária |

---

## 3.4 🏗️ Construtor `__init__` e o Papel do `self`

* `__init__(self, ...)` é chamado quando criamos uma instância
* `self` representa a instância corrente
* Use `__init__` para inicializar atributos

```python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
```

**📝 Observações e boas práticas:**

* ❌ Não retornar valor em `__init__`
* ⚠️ Evitar usar objetos mutáveis como valores padrão em parâmetros

---

## 3.5 🔒 Encapsulamento e Propriedades (`@property`)

### 🔒 Encapsulamento

* Em Python não existe `private` rígido, mas há convenções:
  * `_atributo`: sinaliza "interno / protegido" 🛡️
  * `__atributo`: name mangling (menos acessível) 🔐

### 🎯 `@property` (getter) e `@x.setter` (setter)

```python
class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura   # interno
        self._altura = altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        if valor <= 0:
            raise ValueError("❌ Largura deve ser > 0")
        self._largura = valor

    @property
    def area(self):
        return self._largura * self._altura
```

**💡 Uso:**

```python
r = Retangulo(3, 4)
print(r.area)      # 12 (sem parênteses — property)
r.largura = 5      # ✅ chama setter
# r.area = 10  -> ❌ AttributeError (se não houver setter)
```

---

# 🎯 Exemplos Práticos Comentados

## Exemplo 1 — `ContaBancaria` (com métodos, encapsulamento e property)

```python
class ContaBancaria:
    taxa_transferencia = 0.5  # 💰 atributo de classe (taxa fixa)

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = float(saldo)  # 🔒 encapsulado com _
        self.historico = []

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("❌ Valor de depósito deve ser positivo")
        self._saldo += valor
        self.historico.append(f"📥 Depósito: +{valor}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("❌ Valor de saque deve ser positivo")
        if valor > self._saldo:
            raise ValueError("❌ Saldo insuficiente")
        self._saldo -= valor
        self.historico.append(f"📤 Saque: -{valor}")

    def transferir_para(self, outra_conta, valor):
        total = valor + ContaBancaria.taxa_transferencia
        if self._saldo < total:
            raise ValueError("❌ Saldo insuficiente para transferência e taxa")
        self._saldo -= total
        outra_conta._saldo += valor
        self.historico.append(f"🔄 Transferência: -{valor} (taxa {ContaBancaria.taxa_transferencia})")
```

**💡 Uso:**

```python
c1 = ContaBancaria("Ana", 100)
c2 = ContaBancaria("Bruno", 50)
c1.transferir_para(c2, 20)
print(c1.saldo)  # 100 - 20 - 0.5 = 79.5
print(c2.saldo)  # 70
```

---

## Exemplo 2 — `@classmethod` como Construtor Alternativo

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def from_dict(cls, data):
        return cls(data['nome'], data['idade'])

p = Pessoa.from_dict({"nome": "Lia", "idade": 22})
```

---

# 🧪 Exercícios

> **📝 Instrução:** tente resolver sem colar; leia as dicas. Algumas respostas já estão resolvidas com explicação passo-a-passo.

---

## 🎯 Exercício 1 — (Resolvê-lo) `Retangulo`

Crie uma classe `Retangulo` que:

* receba `largura` e `altura` no `__init__`;
* exponha `area` como `@property` (leitura);
* exponha `perimetro` como `@property`;
* valide que largura e altura são > 0 (levantar `ValueError` caso contrário);
* implemente `__repr__` para exibir `Retangulo(largura=..., altura=...)`.

**💡 Dica:** use `_largura` e `_altura` internamente e `@property`/`@setter` para validar.

---

## 🎯 Exercício 2 — (Resolvido) `Aluno` com média e situação

**📋 Enunciado:** implemente a classe `Aluno` com:

* `nome` (instância), `notas` (lista de floats).
* método `adicionar_nota(nota)`.
* `@property` `media` (média das notas).
* `@property` `situacao` que retorna `"Aprovado"` se `media >= 7`, `"Recuperação"` se `5 <= media < 7`, `"Reprovado"` caso contrário.

**✅ Solução e explicação passo-a-passo:**

```python
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []  # 📊 lista por instância

    def adicionar_nota(self, nota):
        if not (0 <= nota <= 10):
            raise ValueError("❌ Nota deve estar entre 0 e 10")
        self.notas.append(float(nota))

    @property
    def media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    @property
    def situacao(self):
        m = self.media
        if m >= 7:
            return "✅ Aprovado"
        elif m >= 5:
            return "⚠️ Recuperação"
        else:
            return "❌ Reprovado"

# 🧪 Teste:
a = Aluno("Carlos")
a.adicionar_nota(8)
a.adicionar_nota(6.5)
print(a.media)      # (8 + 6.5) / 2 = 7.25
print(a.situacao)   # "✅ Aprovado"
```

**📝 Explicação:** `adicionar_nota` valida a nota; `media` calcula e lida com lista vazia; `situacao` usa a média determinada.

---

## 🎯 Exercício 3 — (Para fazer) `Estoque` com atributo de classe

Crie `Produto` com:

* `nome`, `preco`, `quantidade` (por instância).
* uma classe `Estoque` que mantém `produtos` (dicionário `nome -> Produto`) e tem método `adicionar_produto(produto)` e `total_em_stock()` (soma de `preco * quantidade`).
* implemente também um *contador* de quantos produtos já foram adicionados como atributo de classe.

**💡 Dica:** o contador deve ser incrementado quando se adiciona um produto novo.

---

## 🎯 Exercício 4 — (Resolvido) `Conta` com histórico e segurança básica

Crie uma classe `Conta` que:

* tenha `titular`, `_saldo` (encapsulado), `historico` (lista).
* `depositar(valor)`, `sacar(valor)` com validações.
* `saldo` exposto via `@property` de leitura.
* `sacar` registra ação no histórico.
* trate `valor <= 0` com `ValueError`.

**✅ Solução:**

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = float(saldo)
        self.historico = []

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("❌ Valor de depósito deve ser positivo")
        self._saldo += valor
        self.historico.append(f"📥 Depósito: {valor}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("❌ Valor de saque deve ser positivo")
        if valor > self._saldo:
            raise ValueError("❌ Saldo insuficiente")
        self._saldo -= valor
        self.historico.append(f"📤 Saque: {valor}")
```

**🧪 Teste:**

```python
c = Conta("Ana", 100)
c.depositar(50)
c.sacar(30)
print(c.saldo)       # 120
print(c.historico)   # ['📥 Depósito: 50', '📤 Saque: 30']
```

---

## 🎯 Exercício 5 — (Para fazer) `Biblioteca` com métodos de busca estáticos

Crie `Livro` e `Biblioteca`:

* `Livro(title, autor, ano)`.
* `Biblioteca` mantém lista de livros.
* implemente `buscar_por_autor(autor)` (instância) e um `@staticmethod` `normalizar_texto(texto)` que remove maiúsculas/minúsculas e espaços extras — use `normalizar_texto` dentro de `buscar_por_autor`.

---

## 🎯 Exercício 6 — (Resolvido / passo-a-passo) Demonstrando `@classmethod` e `@staticmethod`

**📋 Enunciado:** implemente `Usuario` com:

* `nome`, `email`.
* `@classmethod` `from_string("nome<email>")` que cria usuário a partir de string: `"Joao<joao@ex.com>"`.
* `@staticmethod` `validar_email(email)` que retorna `True` se a string contém `"@"`.

**✅ Solução:**

```python
class Usuario:
    def __init__(self, nome, email):
        if not Usuario.validar_email(email):
            raise ValueError("❌ Email inválido")
        self.nome = nome
        self.email = email

    @classmethod
    def from_string(cls, s):
        # 📧 formato: Nome<email@ex.com>
        if "<" in s and ">" in s:
            nome, resto = s.split("<", 1)
            email = resto.rstrip(">")
            return cls(nome.strip(), email.strip())
        raise ValueError("❌ Formato inválido")

    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email  # 🔍 simplificação

# 🧪 Teste:
u = Usuario.from_string("João <joao@ex.com>")
print(u.nome, u.email)
```

**📝 Explicação:** `validar_email` é utilitário simples; `from_string` é construtor alternativo.

---

## 🎯 Exercício 7 — (Para fazer) `Agenda` com proteção de atributos

Implemente `Contato` com `_telefone` interno e uma propriedade `telefone` que:

* ao definir, valida se tem 10–11 dígitos (apenas números);
* ao ler, retorna o telefone formatado (`(xx) xxxx-xxxx` ou `(xx) xxxxx-xxxx`).
* 💡 Dica: aceite string e remova caracteres não numéricos internamente.

---

## 🎯 Exercício 8 — (Para fazer) Evitando armadilhas de atributos de classe mutáveis

Explique o que acontece no código abaixo e corrija:

```python
class Sala:
    alunos = []

    def adicionar(self, nome):
        self.alunos.append(nome)
```

**📝 Resposta esperada (resuma):** `alunos` é compartilhado — ao adicionar em uma instância, afeta todas. ✅ Correção: usar `def __init__(self): self.alunos = []`.

---

## 🎯 Exercício 9 — (Projeto final pequeno — para fazer) Mini-sistema de tarefas (todo)

Crie classes:

* `Tarefa` com `titulo`, `descricao`, `concluida` e método `marcar_concluida()`.
* `ListaTarefas` com lista de `Tarefa`s e métodos: `adicionar`, `remover_por_titulo`, `tarefas_pendentes`, `tarefas_concluidas`.
* 🎁 Bônus: salve e carregue as tarefas para um arquivo JSON (use `to_dict()`/`from_dict()` nas classes).

---

# 📋 Gabarito (respostas / códigos completados)

> Aqui estão os códigos completos dos exercícios que marcamos como resolvidos. Você pode copiá-los, executar e brincar.

**✅ Exercício 2 — `Aluno`** (já mostrado acima).
**✅ Exercício 4 — `Conta`** (já mostrado acima).
**✅ Exercício 6 — `Usuario`** (já mostrado acima).

**✅ Implementação sugerida do Ex.1 — `Retangulo`** (modelo de resolução):

```python
class Retangulo:
    def __init__(self, largura, altura):
        self._largura = None
        self._altura = None
        self.largura = largura  # ✅ usa setter para validar
        self.altura = altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, v):
        if v <= 0:
            raise ValueError("❌ Largura deve ser > 0")
        self._largura = v

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, v):
        if v <= 0:
            raise ValueError("❌ Altura deve ser > 0")
        self._altura = v

    @property
    def area(self):
        return self._largura * self._altura

    @property
    def perimetro(self):
        return 2 * (self._largura + self._altura)

    def __repr__(self):
        return f"📐 Retangulo(largura={self._largura}, altura={self._altura})"

# 🧪 Teste
r = Retangulo(3, 4)
print(r.area, r.perimetro, repr(r))  # 12 14 📐 Retangulo(largura=3, altura=4)
```

---

# 💡 Boas Práticas e Dicas Rápidas

* ✅ Prefira nomes claros (`saldo`, `depositar`) e siga PEP8
* ✅ Use `@property` para manter compatibilidade de API
* ⚠️ Evite atributos de classe mutáveis (listas/dicts)
* ✅ Use `__repr__` para facilitar debugging
* ✅ Valide entradas nos setters/constructors
* ✅ Favor composição sobre herança quando possível
* ✅ Documente suas classes e métodos com docstrings

---

# 🚀 Próximos Passos Sugeridos (para estudar depois)

* 📚 Herança e polimorfismo (extends — `class Cachorro(Animal): ...`)
* 🔄 Sobrescrita de métodos e `super()`
* 🦆 Protocolos/duck typing e typing (`typing.Protocol`)
* 🗃️ `dataclasses` para classes de dados simplificadas
* 🎨 Padrões de projeto (Factory, Strategy, Observer)
* 🧪 Testes unitários (`unittest`/`pytest`) para classes

---

# 🏆 Exercícios Extras (Desafio)

1. Implemente `Logger` como `@classmethod` que mantém contagem de mensagens por nível (`info`, `warning`, `error`) e imprime resumo.
2. Crie uma classe `Frota` que mantém veículos; permita `buscar_por_modelo` com correspondência case-insensitive.

---

**🎉 Parabéns por completar esta aula! Agora você tem uma base sólida em POO com Python.**