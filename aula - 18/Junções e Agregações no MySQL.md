# 🧠 Junções e Agregações no MySQL**

> **Tema:** `JOIN`, `GROUP BY`, `ORDER BY` e **Funções de Agregação**
> **Nível:** Iniciante
> **Objetivo:** Compreender como unir dados de tabelas diferentes e como resumir informações com agrupamentos e funções de agregação.

---

## 📘 **1. Revisão rápida: por que JOIN?**

Em bancos de dados relacionais, os dados geralmente são distribuídos em **várias tabelas**.
Para combinar as informações, usamos **junções (JOINs)**.

### 🧩 Exemplo de cenário

```sql
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    cidade VARCHAR(100)
);

CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    valor DECIMAL(10,2),
    data_pedido DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);
```

---

## 🔗 **2. Tipos de JOIN**

### **INNER JOIN**

> Retorna apenas os registros que têm correspondência nas duas tabelas.

```sql
SELECT c.nome, p.valor, p.data_pedido
FROM clientes c
INNER JOIN pedidos p ON c.id_cliente = p.id_cliente;
```

🗒️ *Mostra apenas os clientes que fizeram pedidos.*

---

### **LEFT JOIN**

> Retorna **todos os registros da tabela da esquerda** e os correspondentes da direita.

```sql
SELECT c.nome, p.valor, p.data_pedido
FROM clientes c
LEFT JOIN pedidos p ON c.id_cliente = p.id_cliente;
```

🗒️ *Mostra todos os clientes, mesmo que não tenham feito pedidos.*

---

### **RIGHT JOIN**

> Retorna todos os registros da tabela da **direita**, mesmo sem correspondência na esquerda.

```sql
SELECT c.nome, p.valor, p.data_pedido
FROM clientes c
RIGHT JOIN pedidos p ON c.id_cliente = p.id_cliente;
```

---

## 📊 **3. ORDER BY — Ordenando resultados**

> Serve para **organizar** os resultados da consulta.

```sql
SELECT nome, cidade
FROM clientes
ORDER BY nome ASC;  -- ASC = crescente / DESC = decrescente
```

```sql
SELECT nome, cidade
FROM clientes
ORDER BY cidade DESC;
```

---

## 📦 **4. Funções de Agregação**

As funções de agregação permitem **resumir dados numéricos**.

| Função    | Descrição                   | Exemplo      |
| --------- | --------------------------- | ------------ |
| `COUNT()` | Conta o número de registros | `COUNT(*)`   |
| `SUM()`   | Soma os valores             | `SUM(valor)` |
| `AVG()`   | Calcula a média             | `AVG(valor)` |
| `MAX()`   | Retorna o maior valor       | `MAX(valor)` |
| `MIN()`   | Retorna o menor valor       | `MIN(valor)` |

### 🧮 Exemplo prático:

```sql
SELECT COUNT(*) AS total_pedidos FROM pedidos;
SELECT SUM(valor) AS total_vendas FROM pedidos;
SELECT AVG(valor) AS media_pedidos FROM pedidos;
```

---

## 📂 **5. GROUP BY — Agrupando resultados**

> Usado junto com funções de agregação para **agrupar registros por categoria**.

### Exemplo:

```sql
SELECT c.nome, SUM(p.valor) AS total_gasto
FROM clientes c
INNER JOIN pedidos p ON c.id_cliente = p.id_cliente
GROUP BY c.nome;
```

🗒️ *Mostra quanto cada cliente gastou no total.*

---

## ⚙️ **6. Combinando tudo**

```sql
SELECT c.cidade,
       COUNT(p.id_pedido) AS qtd_pedidos,
       SUM(p.valor) AS total_vendas
FROM clientes c
LEFT JOIN pedidos p ON c.id_cliente = p.id_cliente
GROUP BY c.cidade
ORDER BY total_vendas DESC;
```

🗒️ *Mostra o total de pedidos e o valor total por cidade, ordenado do maior para o menor.*

---

## 🧠 **7. Exercícios práticos**

1. Liste o **nome do cliente e o valor do pedido** usando `INNER JOIN`.
2. Liste **todos os clientes e seus pedidos**, mostrando `NULL` quando não houver pedido (`LEFT JOIN`).
3. Mostre o **total de pedidos por cliente** usando `GROUP BY`.
4. Mostre a **média do valor dos pedidos** de cada cliente.
5. Liste o **nome do cliente, total gasto e cidade**, **ordenando** do que mais gastou para o que menos gastou.
6. Exiba o **total de pedidos por cidade**, ordenado em ordem **decrescente** de quantidade.
7. Encontre o **pedido de maior valor** e o **de menor valor**.
8. Exiba **quantos pedidos foram feitos** no total e a **soma geral dos valores**.

---

## 🔗 **Referência prática**

💻 Teste seus códigos online:
[https://www.mycompiler.io/pt/new/mysql](https://www.mycompiler.io/pt/new/mysql)

