# 🐍 Boas Práticas de Desenvolvimento em Python  
## 📘 Guia para Iniciantes com Conceitos de Engenharia de Software

## 🎯 Objetivo
Aprender a escrever **códigos limpos, organizados e profissionais** em Python,  
seguindo princípios básicos de **engenharia de software**.

---

## 1. Escreva Código Simples e Legível

👉 O computador entende qualquer código válido, mas **o código deve ser fácil para pessoas lerem**.  
Um bom programador pensa nos colegas (e em si mesmo no futuro).

### Exemplo ruim ❌
```python
def f(a, b):
    return a+b
````

Se alguém olhar esse código, não vai saber o que é `f`, `a` e `b`.

### Exemplo bom ✅

```python
def somar_dois_numeros(numero1, numero2):
    return numero1 + numero2
```

📌 **Boa prática**: use **nomes descritivos** para funções e variáveis.

---

## 2. Comentários Claros e Objetivos

Comentários servem para **explicar o "porquê"** do código,
não para repetir o óbvio.

### Exemplo ruim ❌

```python
# somando dois números
soma = 2 + 3
```

### Exemplo bom ✅

```python
# Soma fixa usada para exemplo de boas práticas
soma = 2 + 3
```

📌 **Boa prática**: escreva comentários quando o código **não é óbvio**.

---

## 3. Organização do Código

### 3.1 Indentação

Python **usa indentação obrigatória**. Sempre use **4 espaços** (não use TAB misturado com espaço).

```python
def verificar_aprovacao(nota):
    if nota >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
```

### 3.2 Linhas curtas

Evite linhas muito longas. O recomendado é no máximo **79 caracteres**.

---

## 4. Reuso de Código: Funções

Ao invés de repetir código, **crie funções reutilizáveis**.

### Exemplo ruim ❌

```python
print("Área do quadrado 1:", 5 * 5)
print("Área do quadrado 2:", 10 * 10)
print("Área do quadrado 3:", 7 * 7)
```

### Exemplo bom ✅

```python
def calcular_area_quadrado(lado):
    return lado * lado

print("Área do quadrado 1:", calcular_area_quadrado(5))
print("Área do quadrado 2:", calcular_area_quadrado(10))
print("Área do quadrado 3:", calcular_area_quadrado(7))
```

📌 **Boa prática**: funções evitam **duplicação de código**.

---

## 5. Convenções de Nomeclatura (PEP 8)

O Python tem um guia de estilo chamado **PEP 8**.
Seguindo ele, o código fica mais **padronizado** e **profissional**.

* Variáveis e funções → `snake_case`
* Classes → `CamelCase`
* Constantes → `MAIUSCULO_COM_UNDERSCORE`

### Exemplo:

```python
# Variável
idade_aluno = 20

# Função
def calcular_media(notas):
    return sum(notas) / len(notas)

# Classe
class Pessoa:
    pass

# Constante
PI = 3.14159
```

---

## 6. Estrutura do Projeto

Mesmo em projetos pequenos, é bom manter **organização**:

```
meu_projeto/
│── main.py         # Arquivo principal
│── utils.py        # Funções auxiliares
│── models.py       # Estruturas de dados (ex.: classes)
│── README.md       # Explicação do projeto
```

📌 **Boa prática**: separar responsabilidades.

---

## 7. Tratamento de Erros (Exceções)

Nunca deixe seu programa quebrar feio.
Use **try/except** para capturar erros.

### Exemplo ruim ❌

```python
numero = int(input("Digite um número: "))
print(10 / numero)
```

Se o usuário digitar `0` → erro feio.

### Exemplo bom ✅

```python
try:
    numero = int(input("Digite um número: "))
    print(10 / numero)
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ValueError:
    print("Por favor, digite um número válido.")
```

📌 **Boa prática**: trate erros de forma amigável.

---

## 8. Documentação com Docstrings

Docstrings servem para documentar funções.

```python
def calcular_area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.
    
    Parâmetros:
        base (float): valor da base
        altura (float): valor da altura
    
    Retorna:
        float: área calculada
    """
    return base * altura
```

📌 **Boa prática**: quem usar sua função vai entender **como usá-la**.

---

## 🚀 Resumo das Boas Práticas em Python

✅ Use nomes descritivos para variáveis e funções
✅ Escreva comentários claros e úteis
✅ Organize o código com funções e módulos
✅ Siga o padrão **PEP 8** (estilo Python)
✅ Trate erros com `try/except`
✅ Documente com **docstrings**
---

## 🎓 Próximos Passos

* Ler o guia oficial [PEP 8](https://peps.python.org/pep-0008/)
* Praticar escrevendo programas simples **bem organizados**
* Experimentar separar código em arquivos diferentes
