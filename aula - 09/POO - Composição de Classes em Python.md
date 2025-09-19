# 🐍 Composição de Classes em Python

## 🎯 Objetivo da Aula
- Entender o que é **composição entre classes**.
- Aprender a criar classes onde **um objeto controla a vida de outro**.
- Praticar com exemplos e exercícios.

---

## 1️⃣ O que é Composição?

Em Programação Orientada a Objetos (POO), **composição** é um tipo de **associação mais forte**.  
Aqui, **um objeto é “dono” de outro** e **é responsável por criar e destruir** esse objeto.

➡️ Em outras palavras, **se o objeto “pai” deixar de existir, o objeto “filho” também deixa**.

---

## 2️⃣ Diferença para Associação Simples

| Associação Simples/Agregação | Composição |
|------------------------------|-----------|
| Cada classe pode viver sozinha. | O objeto “filho” depende totalmente do “pai”. |
| Ex.: Pessoa e Celular. | Ex.: Carro e Motor (o motor só existe enquanto o carro existir). |

---

## 3️⃣ Exemplo do Mundo Real

- **Carro** possui um **Motor**.
- **Casa** possui **Cômodos**.
- **Computador** possui **Placa-mãe**.

Nesses casos:
- O **Motor** não faz sentido existir fora de um **Carro** no nosso contexto.
- Quando o **Carro** é destruído, o **Motor** também é.

---

## 4️⃣ Exemplo Prático – Carro e Motor

```python
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia} ligado!")

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        # O carro cria seu próprio motor.
        self.motor = Motor(potencia_motor)

    def ligar_carro(self):
        print(f"Ligando o carro {self.modelo}")
        self.motor.ligar()

meu_carro = Carro("Sedan", "2.0")
meu_carro.ligar_carro()
````

💡 **Explicação:**

* O `Carro` cria o `Motor` dentro do seu construtor.
* Não criamos o motor fora da classe `Carro`.
* Se o `Carro` é apagado, o `Motor` também some.

---

## 5️⃣ Exemplo – Casa e Cômodos

```python
class Comodo:
    def __init__(self, nome, metros):
        self.nome = nome
        self.metros = metros

class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = []  # Lista para guardar os cômodos

    def adicionar_comodo(self, nome, metros):
        # A casa cria os objetos Comodo
        self.comodos.append(Comodo(nome, metros))

    def mostrar_comodos(self):
        print(f"Casa localizada em {self.endereco} possui:")
        for c in self.comodos:
            print(f"- {c.nome} com {c.metros} m²")

casa = Casa("Rua das Flores, 123")
casa.adicionar_comodo("Sala", 20)
casa.adicionar_comodo("Quarto", 15)
casa.mostrar_comodos()
```

💡 **Explicação:**

* A **Casa** é dona dos **Cômodos**.
* Os **Cômodos** só existem dentro da **Casa**.

---

## 6️⃣ Exemplo – Computador e Peças Internas

```python
class PlacaMae:
    def __init__(self, modelo):
        self.modelo = modelo

class Computador:
    def __init__(self, nome_pc, modelo_placa):
        self.nome_pc = nome_pc
        self.placa_mae = PlacaMae(modelo_placa)  # Cria a placa-mãe aqui

    def info(self):
        print(f"PC {self.nome_pc} possui placa-mãe {self.placa_mae.modelo}")

pc1 = Computador("Gamer-X", "Asus ROG")
pc1.info()
```

---

## 7️⃣ Boas Práticas

* Use composição quando **o objeto não faz sentido existir sozinho**.
* Nomeie claramente os atributos para deixar claro quem é o “dono”.
* Crie os objetos dependentes **dentro** da classe principal, normalmente no `__init__`.

---

## 8️⃣ Exercícios

### 📝 Exercício 1

Crie as classes **Livro** e **Pagina**.

* Cada livro cria várias páginas internamente.
* Cada página tem um número e um pequeno texto.
* Mostre o conteúdo do livro listando todas as páginas.

---

### 📝 Exercício 2

Crie as classes **Empresa** e **Funcionario**.

* A empresa cria e gerencia seus funcionários.
* Cada funcionário tem nome e cargo.
* Crie uma empresa e adicione 3 funcionários.
* Mostre o nome de cada funcionário.

---

### 📝 Exercício 3

Crie as classes **Playlist** e **Musica**.

* A playlist cria músicas internamente.
* Cada música tem título e duração.
* Mostre todas as músicas de uma playlist.

---

### 📝 Exercício 4 (Desafio)

Crie as classes **Universidade** e **Departamento**.

* A universidade é responsável por criar departamentos.
* Cada departamento tem nome e quantidade de professores.
* Crie uma universidade com 3 departamentos diferentes e liste-os.

---

## 9️⃣ Conclusão

* **Composição** representa uma **relação de “tem-um”**, mas com **forte dependência**.
* É muito útil para modelar objetos que **fazem parte de um todo**.

> 💡 **Resumo:**
>
> * **Associação**: Objetos se relacionam, mas vivem sozinhos.
> * **Composição**: Um objeto contém e controla o outro.

🎯 **Pratique bastante!** Crie exemplos do seu dia a dia, como **Agenda** com **Compromissos**, ou **Turma** com **Alunos**, sempre pensando: *“Se o pai for destruído, o filho também deve?”*.