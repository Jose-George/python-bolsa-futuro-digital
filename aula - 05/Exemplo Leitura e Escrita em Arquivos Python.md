1. **Gerar um arquivo `clientes.txt` com 200 linhas de dados** (nome, saldo, dívida).
2. **Ler o arquivo, atualizar os saldos conforme as dívidas e salvar o resultado em outro arquivo** (`clientes_atualizados.txt`).

---

## 📝 Código completo

```python
import random

# 1. Gerar arquivo com 200 clientes
with open("clientes.txt", "w") as arquivo:
    for i in range(1, 201):
        nome = f"Cliente{i}"
        saldo = random.randint(500, 5000)   # saldo entre 500 e 5000
        divida = random.randint(100, 6000)  # dívida entre 100 e 6000
        arquivo.write(f"{nome},{saldo},{divida}\n")

print("Arquivo clientes.txt gerado com sucesso!")


# 2. Ler arquivo e atualizar saldos
clientes_atualizados = []

with open("clientes.txt", "r") as arquivo:
    for linha in arquivo:
        nome, saldo, divida = linha.strip().split(",")
        saldo = int(saldo)
        divida = int(divida)

        # Comparar saldo e dívida
        if saldo >= divida:
            saldo -= divida   # paga toda a dívida
            divida = 0
        else:
            divida -= saldo   # reduz a dívida pelo saldo disponível
            saldo = 0

        clientes_atualizados.append((nome, saldo, divida))


# 3. Salvar resultados em outro arquivo
with open("clientes_atualizados.txt", "w") as arquivo:
    arquivo.write("Nome,Saldo Atual,Divida Atual\n")
    for nome, saldo, divida in clientes_atualizados:
        arquivo.write(f"{nome},{saldo},{divida}\n")

print("Arquivo clientes_atualizados.txt criado com os saldos atualizados!")
```

---

## 📂 Estrutura dos arquivos

### Arquivo **clientes.txt** (exemplo das primeiras linhas)

```
Cliente1,2480,560
Cliente2,1300,4000
Cliente3,5000,3000
...
```

### Arquivo **clientes\_atualizados.txt** (resultado depois do cálculo)

```
Nome,Saldo Atual,Divida Atual
Cliente1,1920,0
Cliente2,0,2700
Cliente3,2000,0
...
```

---

## 🔎 Explicação do cálculo

* Se o **saldo** ≥ **dívida** → o cliente paga tudo, dívida = 0.
* Se o **saldo** < **dívida** → usa todo o saldo para abater a dívida, saldo = 0.

---

👉 COM VOCÊS: Adicione uma **estatística final no programa** (ex: quantos clientes ficaram sem dívida, quantos ainda devem, e o valor total de dívidas antes/depois)?
