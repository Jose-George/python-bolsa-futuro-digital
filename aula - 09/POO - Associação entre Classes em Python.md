# 🐍 Associação entre Classes em Python

## 🎯 Objetivo da Aula
- Entender o que é **associação entre classes**.
- Aprender a criar classes que se relacionam entre si.
- Praticar com exemplos e exercícios.

---

## 1️⃣ O que é Associação entre Classes?

Em Programação Orientada a Objetos (POO), **associação** é a **relação entre duas ou mais classes**, onde **um objeto utiliza outro objeto** para cumprir uma tarefa.

- **Importante:** Na associação, as classes **não dependem totalmente uma da outra para existir**.  
- Elas **trabalham juntas**, mas **cada uma pode existir sozinha**.

### 💡 Exemplos do Mundo Real
- **Pessoa** usa um **Celular**.  
- **Professor** dá aula em uma **Sala**.  
- **Carro** tem um **Motor**.

Esses objetos podem existir independentemente:
- O **Celular** existe sem a **Pessoa**.
- O **Motor** pode existir sem o **Carro** (por exemplo, em estoque).

---

## 2️⃣ Tipos de Associação

Dentro de associação, temos variações:

| Tipo           | Descrição |
|----------------|----------|
| **Simples**    | Uma classe usa a outra apenas temporariamente (ex.: Pessoa usa um Celular emprestado). |
| **Agregação**  | Uma classe tem um atributo que é outro objeto, mas ambos podem viver separados. |
| **Composição** | Uma classe contém outra e controla totalmente sua vida (mais forte que agregação). |

> Nesta aula, vamos focar na **associação simples** e **agregação**

---

## 3️⃣ Exemplo Prático – Associação Simples

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def usar_celular(self, celular):
        print(f"{self.nome} está usando o celular da marca {celular.marca}")

class Celular:
    def __init__(self, marca):
        self.marca = marca

# Criando objetos
celular1 = Celular("Samsung")
pessoa1 = Pessoa("Maria")

# Associação: Pessoa usa Celular
pessoa1.usar_celular(celular1)
````

💡 **Explicação:**

* `Pessoa` e `Celular` são independentes.
* O método `usar_celular` demonstra a relação **temporária**.

---

## 4️⃣ Exemplo – Agregação

Aqui, um objeto **guarda a referência** de outro como **atributo**.

```python
class Professor:
    def __init__(self, nome):
        self.nome = nome

class Sala:
    def __init__(self, numero, professor):
        self.numero = numero
        self.professor = professor  # Sala tem um Professor

prof = Professor("Ana")
sala101 = Sala(101, prof)

print(f"A sala {sala101.numero} é da professora {sala101.professor.nome}")
```

💡 **Explicação:**

* `Sala` possui um atributo `professor`, que é um objeto da classe `Professor`.
* **Ambos podem existir separadamente**.

---

## 5️⃣ Mais um Exemplo: Associação Múltipla

Um objeto pode se associar a vários objetos.

```python
class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []  # Lista para armazenar vários alunos

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

curso_python = Curso("Python Básico")
aluno1 = Aluno("João")
aluno2 = Aluno("Maria")

curso_python.adicionar_aluno(aluno1)
curso_python.adicionar_aluno(aluno2)

print("Alunos no curso:")
for a in curso_python.alunos:
    print("-", a.nome)
```

---

## 6️⃣ Boas Práticas

* **Nomeie bem as classes**: cada uma deve representar um conceito claro.
* **Evite dependências desnecessárias**: cada classe deve ter responsabilidade única.
* **Use listas ou dicionários** quando precisar associar múltiplos objetos.

---

## 7️⃣ Exercícios

### 📝 Exercício 1

Crie duas classes: **Autor** e **Livro**.

* O autor tem nome e nacionalidade.
* O livro tem título e um objeto autor.
* Crie 2 autores e 3 livros.
* Mostre no terminal o nome do livro e o nome do autor.

---

### 📝 Exercício 2

Crie as classes **Cliente** e **ContaBancaria**.

* O cliente tem nome e CPF.
* A conta bancária tem número e um cliente associado.
* Imprima uma mensagem mostrando o titular da conta e o número da conta.

---

### 📝 Exercício 3

Crie as classes **Time** e **Jogador**.

* Um time pode ter vários jogadores.
* Crie 2 times com 3 jogadores cada.
* Mostre a lista de jogadores de cada time.

---

### 📝 Exercício 4 (Desafio)

Crie as classes **Playlist** e **Musica**.

* Uma playlist pode ter várias músicas.
* Cada música tem título e cantor.
* Adicione músicas à playlist e exiba todas.

---

## 8️⃣ Conclusão

* **Associação** é a base para sistemas que representam o mundo real.
* Ela permite **reaproveitar código**, tornando os programas mais organizados e modulares.

> 💡 **Próximo Passo:** Estude **composição**, que é uma forma mais forte de associação, onde um objeto controla totalmente a existência do outro.
