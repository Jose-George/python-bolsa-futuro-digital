# Aula: Boas Práticas de Engenharia de Software em Python (Orientação a Objetos)

> **Objetivo**: Criar uma **calculadora orientada a objetos** em Python e mostrar, passo a passo, como aplicar práticas de engenharia de software: **organização de pastas**, **modularização**, **versionamento**, **testes automatizados** e **documentação**.

---

## 1. Motivação

Mesmo um projeto simples, como uma calculadora, pode se tornar difícil de manter se não houver organização.  
Aplicar **OOP** (Orientação a Objetos) e boas práticas desde o início facilita:

- **Reuso de código**  
- **Extensão de funcionalidades**  
- **Manutenção e colaboração**

---

## 2. Estrutura de Pastas Recomendada

```

calculadora_oo/
├── src/
│   ├── **init**.py
│   ├── main.py
│   ├── models/
│   │   ├── **init**.py
│   │   └── calculadora.py
│   └── operations/
│       ├── **init**.py
│       ├── adicao.py
│       ├── subtracao.py
│       ├── multiplicacao.py
│       └── divisao.py
├── tests/
│   ├── **init**.py
│   └── test_calculadora.py
├── requirements.txt
└── README.md

````

### Função de Cada Pasta

- **src/**: Código-fonte principal.
- **models/**: Classes centrais, como `Calculadora`.
- **operations/**: Módulos com operações separadas (ex.: `adicao.py`).
- **tests/**: Arquivos de testes automatizados.
- **requirements.txt**: Dependências do projeto.
- **README.md**: Instruções de uso e documentação.

---

## 3. Implementação Orientada a Objetos

### 3.1 Classe Principal

Arquivo: `src/models/calculadora.py`

```python
from src.operations.adicao import Adicao
from src.operations.subtracao import Subtracao
from src.operations.multiplicacao import Multiplicacao
from src.operations.divisao import Divisao

class Calculadora:
    """Classe principal da calculadora orientada a objetos."""

    def __init__(self):
        self.operacoes = {
            "soma": Adicao(),
            "subtracao": Subtracao(),
            "multiplicacao": Multiplicacao(),
            "divisao": Divisao()
        }

    def calcular(self, operacao: str, a: float, b: float) -> float:
        if operacao not in self.operacoes:
            raise ValueError(f"Operação '{operacao}' não suportada.")
        return self.operacoes[operacao].executar(a, b)
````

---

### 3.2 Interface das Operações

Cada operação é um módulo independente, facilitando a adição de novas funcionalidades.

Exemplo: `src/operations/adicao.py`

```python
class Adicao:
    """Classe que representa a operação de adição."""
    def executar(self, a: float, b: float) -> float:
        return a + b
```

`src/operations/subtracao.py`, `multiplicacao.py`, `divisao.py` seguem o mesmo padrão.

---

### 3.3 Arquivo Principal

Arquivo: `src/main.py`

```python
from src.models.calculadora import Calculadora

def main():
    calc = Calculadora()
    print("Calculadora OO")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    operacao = input("Escolha (soma, subtracao, multiplicacao, divisao): ").lower()
    resultado = calc.calcular(operacao, a, b)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
```

---

## 4. Versionamento com Git

1. **Inicialize o repositório**

   ```bash
   git init
   ```
2. **Crie commits descritivos**

   ```bash
   git add .
   git commit -m "Implementa estrutura inicial da calculadora OO"
   ```
3. **Use branches para novas funcionalidades**

   ```bash
   git checkout -b feature/potencia
   ```

---

## 5. Testes Automatizados

Arquivo: `tests/test_calculadora.py`

```python
import pytest
from src.models.calculadora import Calculadora

def test_soma():
    calc = Calculadora()
    assert calc.calcular("soma", 2, 3) == 5

def test_divisao():
    calc = Calculadora()
    assert calc.calcular("divisao", 6, 3) == 2
```

* **Rodar os testes**:

  ```bash
  pip install pytest
  pytest
  ```

---

## 6. Documentação

### 6.1 README.md

Inclua:

* Descrição do projeto
* Como instalar dependências
* Como executar a aplicação e os testes
* Exemplo de uso

### 6.2 Docstrings

Use docstrings em cada classe e método. Exemplo já mostrado em `Calculadora`.

Ferramentas como **Sphinx** podem gerar documentação a partir das docstrings.

---

## 7. Boas Práticas Extras

* **Tipagem**: Use *type hints* para clareza.
* **Linting/Formatadores**:

  * `flake8` para verificar estilo.
  * `black` para formatação automática.
* **CI/CD**: Configure GitHub Actions para rodar testes a cada push.

---

## 8. Exercício Proposto

1. Implemente uma nova operação, como **potência**.
2. Crie uma nova classe em `src/operations/potencia.py`.
3. Adicione a operação ao dicionário `self.operacoes` da classe `Calculadora`.
4. Escreva testes automatizados para a nova operação.

---

## Conclusão

* **Organização em pastas + OOP** = projeto limpo e escalável.
* Git e testes garantem controle de mudanças e qualidade.
* Documentação mantém o projeto compreensível para qualquer pessoa.

> **Mensagem final**: Aplique essas práticas sempre — mesmo em projetos simples — e seu código estará preparado para crescer sem dor de cabeça!