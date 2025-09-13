# 🐍 Aula: Encapsulamento em Python (Orientação a Objetos)

## 🎯 Objetivo da Aula
Nesta aula, vamos aprender **o que é encapsulamento** em Programação Orientada a Objetos (POO) usando Python.  
Você vai entender:
- O que é encapsulamento  
- Como **proteger** atributos e métodos  
- Como **controlar** o acesso aos dados de um objeto  
- Como criar **getters** e **setters** em Python  

---

## 1️⃣ O que é Encapsulamento?

Imagine que você tem uma **caixa de ferramentas**.  
Dentro dela, você guarda itens importantes e **não quer que qualquer pessoa mexa diretamente**.  
Em vez disso, você permite que as pessoas **peçam** para usar a ferramenta.

👉 Encapsulamento é isso: **esconder os detalhes internos de um objeto** e **controlar como esses detalhes são acessados e modificados**.

Em POO, usamos **modificadores de acesso** (público, protegido, privado) para controlar quem pode usar ou alterar cada parte do objeto.

---

## 2️⃣ Modificadores de Acesso em Python

No Python, não existe palavra-chave como `private` (igual a outras linguagens).  
Mas usamos **convenções**:

| Tipo de Acesso | Como escrever | Significado |
|----------------|--------------|------------|
| **Público**    | `atributo`   | Todos podem acessar (padrão). |
| **Protegido**  | `_atributo`  | Convenção: só a classe e subclasses **deveriam** acessar. |
| **Privado**    | `__atributo` | Python faz *name mangling* para dificultar o acesso direto. |

---

## 3️⃣ Exemplo Básico: Atributo Público

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome      # público
        self.idade = idade    # público

p = Pessoa("Ana", 20)
print(p.nome)   # ✅ Acessível
print(p.idade)  # ✅ Acessível
````

💡 Aqui, qualquer um pode mudar `p.idade` diretamente:

```python
p.idade = 100  # 😬 Pode alterar sem controle
```

Isso pode ser um problema!

---

## 4️⃣ Encapsulando com Atributo Protegido

Usamos um **underscore** (`_`) para indicar que **não é para mexer diretamente**.

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo  # protegido

    def ver_saldo(self):
        return self._saldo

conta = ContaBancaria("João", 500)
print(conta.ver_saldo())   # ✅ Maneira certa
print(conta._saldo)        # 😬 Possível, mas não recomendado
```

Python **não impede**, mas a convenção avisa outros programadores: “não mexa aqui!”.

---

## 5️⃣ Encapsulamento com Atributo Privado

Para **dificultar ainda mais o acesso**, usamos `__` (dois underlines).

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # privado

    def ver_saldo(self):
        return self.__saldo

conta = ContaBancaria("João", 500)
print(conta.ver_saldo())   # ✅ OK
print(conta.__saldo)       # ❌ ERRO: AttributeError
```

💡 Se tentar acessar `__saldo` diretamente, o Python não deixa.

---

## 6️⃣ Getters e Setters

Para **controlar alterações**, criamos métodos para *pegar* e *atualizar* valores.

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    # Getter
    def get_saldo(self):
        return self.__saldo

    # Setter
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:        # validação
            self.__saldo = novo_saldo
        else:
            print("Saldo não pode ser negativo!")

conta = ContaBancaria("João", 500)
print(conta.get_saldo())   # ✅ 500
conta.set_saldo(1000)      # ✅ altera para 1000
print(conta.get_saldo())
conta.set_saldo(-200)      # ❌ Não permitido
```

---

## 7️⃣ Usando `@property` (Jeito Pythonico)

Python tem um jeito mais elegante para getters e setters.

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo!")
```

Uso:

```python
conta = ContaBancaria("João", 500)
print(conta.saldo)     # ✅ Getter
conta.saldo = 800      # ✅ Setter
print(conta.saldo)
conta.saldo = -50      # ❌ Mensagem de erro
```

---

## 8️⃣ Exercícios Práticos

Tente criar sozinho:

1. **Classe Produto**

   * Atributos: `__preco`, `nome`
   * Getter e setter para `__preco` (não aceitar preço negativo).

2. **Classe Aluno**

   * Atributos: `__nota`
   * Getter e setter para `__nota` (só aceitar 0 a 10).

3. **Classe Carro**

   * Atributo: `__velocidade`
   * Métodos: `acelerar(valor)` e `frear(valor)`
   * A velocidade não pode ser menor que 0.

---

## 📝 Resumo

* Encapsulamento = **proteger dados** e controlar acesso.
* Python usa **convenções**:

  * Público: `atributo`
  * Protegido: `_atributo`
  * Privado: `__atributo`
* **Getters e Setters** garantem controle.
* Use `@property` para código mais limpo.

---

💡 **Dica Final:**
Encapsular não é apenas “esconder”, é garantir que os dados sejam **seguros** e **consistentes**, evitando que alguém quebre as regras do seu programa.
