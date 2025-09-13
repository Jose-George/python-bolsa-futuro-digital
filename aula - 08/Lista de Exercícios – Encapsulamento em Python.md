## 📝 Lista de Exercícios – Encapsulamento em Python

### 1️⃣ Classe **Produto**

Crie uma classe chamada `Produto` com os atributos:

* `nome` (público)
* `__preco` (privado)

**Requisitos:**

* Crie um **getter** e um **setter** para `__preco`.
* O preço não pode ser negativo.
* Crie um objeto da classe e tente:

  * Alterar o preço para um valor válido.
  * Alterar para um valor negativo e exibir a mensagem de erro.

---

### 2️⃣ Classe **ContaBancaria**

Implemente uma classe `ContaBancaria` com:

* `titular` (público)
* `__saldo` (privado)

**Requisitos:**

* Métodos:

  * `depositar(valor)`: aumenta o saldo.
  * `sacar(valor)`: diminui o saldo apenas se houver dinheiro suficiente.
  * `ver_saldo()`: retorna o saldo.
* Teste depositar, sacar um valor válido e tentar sacar mais do que o saldo disponível.

---

### 3️⃣ Classe **Aluno**

Crie uma classe `Aluno` com:

* `nome` (público)
* `__nota` (privado)

**Requisitos:**

* Use a anotação `@property` para criar getter e setter de `nota`.
* A nota deve ser um número entre **0 e 10**.
* Crie um objeto e tente definir a nota para valores dentro e fora do intervalo.

---

### 4️⃣ Classe **Carro**

Implemente uma classe `Carro` com:

* `modelo` (público)
* `__velocidade` (privado)

**Requisitos:**

* Método `acelerar(valor)`: aumenta a velocidade.
* Método `frear(valor)`: diminui a velocidade, mas **não pode ficar negativa**.
* Crie um objeto, acelere e freie várias vezes, mostrando a velocidade atual.

---

### 5️⃣ Classe **Usuario**

Crie uma classe `Usuario` com:

* `__senha` (privado)
* `email` (público)

**Requisitos:**

* Crie um setter para `senha` que só aceita senhas com pelo menos **6 caracteres**.
* Crie um método `verificar_senha(tentativa)` que retorna `True` se a tentativa for igual à senha, caso contrário `False`.
* Teste a criação de um usuário com senha válida e outra inválida.

---

💡 **Dica para os alunos:**

* Usem `@property` e `@nome.setter` quando quiserem um código mais “pythônico”.
* Lembrem-se: encapsulamento não é só “esconder”, é **validar e proteger os dados**.
