# 🐍 Introdução a Diagrama de Classe (UML) com Python

## 🎯 Objetivo da Aula
- Entender **o que é um diagrama de classe**.
- Aprender a **interpretar e criar** diagramas simples.
- Ver **exemplos em Python** que correspondem ao diagrama.

---

## 1️⃣ O que é um Diagrama de Classe?

Um **diagrama de classe** é uma representação visual de como as classes de um sistema **se organizam** e **se relacionam**.

Ele mostra:
- **Nome da Classe**  
- **Atributos** (variáveis)  
- **Métodos** (funções)  
- **Relacionamentos** (como as classes se conectam)

➡️ Faz parte da **UML (Unified Modeling Language)** – uma linguagem padrão para modelar sistemas orientados a objetos.

---

## 2️⃣ Por que Usar Diagramas de Classe?

- **Planejamento**: ajuda a pensar antes de programar.
- **Comunicação**: facilita explicar o sistema para a equipe.
- **Documentação**: registra como o sistema foi projetado.

---

## 3️⃣ Estrutura Básica de um Diagrama

```

+---------------------+
\|      NomeClasse     |
+---------------------+
\| - atributo: tipo    |
\| - outroAtributo: tipo|
+---------------------+
\| + metodo(): tipoRet |
\| + outroMetodo()     |
+---------------------+

```

- **Nome da Classe**: sempre em negrito ou centralizado.
- **Atributos**: começam com sinal:
  - `-` privado
  - `+` público
- **Métodos**: idem (com os parênteses).

💡 Em Python, a visibilidade (público/privado) é **por convenção**, mas usamos `-` e `+` no diagrama para indicar intenção.

---

## 4️⃣ Exemplo Simples – Pessoa

### Diagrama

```

+---------------------+
\|       Pessoa        |
+---------------------+
\| - nome: str         |
\| - idade: int        |
+---------------------+
\| + apresentar(): None|
+---------------------+

````

### Código em Python

```python
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")
````

---

## 5️⃣ Relacionamento Entre Classes

Diagramas também mostram **relações**:

* **Associação**: uma classe usa outra.
* **Composição**: uma classe contém outra, que não vive sozinha.
* **Herança**: uma classe “filha” herda da “mãe”.

### Símbolos mais usados:

* **Linha simples**: associação.
* **Losango preenchido**: composição.
* **Seta com triângulo**: herança.

---

## 6️⃣ Exemplo com Associação

### Situação

* Uma **Pessoa** tem um **Celular**.

### Diagrama

```
+---------+        +---------+
| Pessoa  |1 ---- 1| Celular |
+---------+        +---------+
| nome    |        | marca   |
+---------+        +---------+
| ligar() |        | tocar() |
+---------+        +---------+
```

O `1 ---- 1` significa: **uma pessoa tem um celular** (1 para 1).

### Código em Python

```python
class Celular:
    def __init__(self, marca):
        self.marca = marca

    def tocar(self):
        print(f"{self.marca} está tocando!")

class Pessoa:
    def __init__(self, nome, celular):
        self.nome = nome
        self.celular = celular  # associação

    def ligar(self):
        print(f"{self.nome} está ligando para alguém...")
        self.celular.tocar()

cel = Celular("Samsung")
pessoa = Pessoa("Maria", cel)
pessoa.ligar()
```

---

## 7️⃣ Exemplo com Herança

### Situação

* Um **Animal** é a classe base.
* Um **Cachorro** herda de **Animal**.

### Diagrama

```
        +---------+
        | Animal  |
        +---------+
        | nome    |
        +---------+
        | fazer_som() |
        +---------+
            ^
            |
        +---------+
        | Cachorro|
        +---------+
        | raca    |
        +---------+
        | latir() |
        +---------+
```

### Código em Python

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def latir(self):
        print("Au au!")
```

---

## 8️⃣ Exercícios

### 📝 Exercício 1

Desenhe o diagrama de classe para:

* **Carro**: atributos `modelo`, `ano`, método `ligar`.
* **Motor**: atributo `potencia`, método `funcionar`.
* Mostre no diagrama que **Carro** tem um **Motor** (composição).
  Depois, escreva o código em Python.

---

### 📝 Exercício 2

Crie o diagrama de uma **Loja** que possui vários **Produtos**.

* Cada produto tem `nome` e `preco`.
* A loja tem métodos para adicionar produto e listar todos.

---

### 📝 Exercício 3

Desenhe o diagrama e faça o código para:

* **Professor** (atributo `nome`, método `ensinar`).
* **Curso** (atributo `titulo`, método `adicionar_professor`).
* Mostre no diagrama a associação (um curso tem um professor).

---

## 9️⃣ Dicas para Criar Diagramas

* **Simples é melhor**: só coloque o essencial (atributos e métodos principais).
* Use ferramentas gratuitas como:

  * [draw.io](https://app.diagrams.net/)
  * [PlantUML](https://plantuml.com/)
  * [Lucidchart](https://www.lucidchart.com/)

---

## 🔑 Conclusão

* **links úteis** https://www.cos.ufrj.br/~franklin/xbt246/03-Python-OO.pdf

* **Diagramas de Classe** ajudam a **planejar** e **documentar** antes de programar.
* Em Python, mesmo sem visibilidade rígida, a ideia de atributos e métodos é a mesma.
* Eles mostram **como as classes se conectam**, facilitando a construção do código.

🎯 **Pratique desenhando diagramas para pequenos projetos** que você já criou em Python, como calculadora, jogo da forca ou sistema de cadastro.