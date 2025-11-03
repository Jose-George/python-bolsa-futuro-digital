# 🧾 **Prova 2 – Banco de Dados MySQL (2ª Chamada)**

**Nome:** ___________________________________________
**Data:** ****/****/______
**Pontuação:** __________ / 20

---

#### **1.** Qual comando é usado para **selecionar um banco de dados** no MySQL?

a) `USE nome_do_banco;`

b) `SELECT DATABASE nome_do_banco;`

c) `OPEN DATABASE nome_do_banco;`

d) `START nome_do_banco;`

e) `LOAD DATABASE nome_do_banco;`

---

#### **2.** Para criar um novo banco de dados chamado `escola`, qual comando é correto?

a) `CREATE DATABASE TABLE escola;`

b) `CREATE DATABASE escola;`

c) `NEW DATABASE escola;`

d) `CREATE TABLE escola;`

e) `INSERT DATABASE escola;`

---

#### **3.** O que representa a **chave primária (PRIMARY KEY)**?

a) Um campo que identifica exclusivamente cada registro.

b) Um campo que pode ter valores duplicados.

c) Um campo que liga duas tabelas diferentes.

d) Um campo opcional de uma tabela.

e) Um campo usado apenas em consultas.

---

#### **4.** Para **adicionar uma restrição de chave primária** em uma tabela já existente, utiliza-se:

a)

```sql
ALTER TABLE tabela ADD PRIMARY KEY (coluna);
```

b)

```sql
CREATE PRIMARY KEY tabela(coluna);
```

c) `ALTER DATABASE ADD PRIMARY KEY;`
d) `UPDATE TABLE SET PRIMARY KEY;`
e) `ADD KEY PRIMARY tabela(coluna);`

---

#### **5.** Qual comando cria corretamente uma tabela `produtos` com os campos `id`, `nome` e `preco`?

a) `CREATE TABLE produtos (id INT, nome TEXT, preco FLOAT);`

b) `CREATE TABLE produtos id INT nome TEXT preco FLOAT;`

c) `NEW TABLE produtos (id, nome, preco);`

d) `CREATE produtos TABLE (id INT, nome VARCHAR, preco DECIMAL);`

e) `MAKE TABLE produtos (id, nome, preco);`

---

#### **6.** Qual comando **insere um novo registro** na tabela `clientes`?

a) `INSERT INTO clientes VALUES (1, 'João');`

b) `ADD INTO clientes (1, 'João');`

c) `UPDATE clientes SET nome='João';`

d) `NEW clientes (1, 'João');`

e) `APPEND clientes (1, 'João');`

---

#### **7.** Para **atualizar o preço** de um produto com `id = 3` para `50.00`, o comando correto é:

a)

```sql
UPDATE produtos SET preco = 50.00 WHERE id = 3;
```

b)

```sql
ALTER produtos SET preco = 50.00 WHERE id = 3;
```

c)

```sql
CHANGE produtos preco = 50.00 WHERE id = 3;
```

d)

```sql
SET preco = 50.00 FROM produtos WHERE id = 3;
```

e) `UPDATE preco = 50.00 IN produtos WHERE id = 3;`

---

#### **8.** O comando `DELETE FROM produtos WHERE id = 2;` faz o quê?

a) Apaga todos os registros da tabela.

b) Apaga apenas o registro cujo id é 2.

c) Apaga a tabela inteira.

d) Apaga a estrutura da tabela.

e) Apaga o banco de dados.

---

#### **9.** Qual diferença principal entre `DELETE` e `TRUNCATE`?

a) `DELETE` remove estrutura, `TRUNCATE` remove dados.

b) `DELETE` apaga dados específicos, `TRUNCATE` apaga todos os dados.

c) Ambos fazem o mesmo.

d) `TRUNCATE` pode ter cláusula WHERE.

e) `DELETE` é mais rápido que `TRUNCATE`.

---

#### **10.** Para **excluir uma tabela completa**, o comando correto é:

a) `DROP TABLE tabela;`

b) `DELETE TABLE tabela;`

c) `REMOVE TABLE tabela;`

d) `CLEAR TABLE tabela;`

e) `TRUNCATE DATABASE tabela;`

---

#### **11.** Qual comando exibe **todas as tabelas** de um banco de dados?

a) `SHOW TABLES;`

b) `LIST TABLES;`

c) `VIEW TABLES;`

d) `DISPLAY TABLES;`

e) `SELECT TABLES;`

---

#### **12.** Para renomear uma tabela `usuarios` para `pessoas`, usa-se:

a) `ALTER TABLE usuarios RENAME pessoas;`

b) `CHANGE usuarios TO pessoas;`

c) `UPDATE TABLE usuarios TO pessoas;`

d) `RENAME DATABASE usuarios TO pessoas;`

e) `SET TABLE usuarios = pessoas;`

---

#### **13.** Qual das opções abaixo retorna **apenas os nomes dos clientes**?

a) `SELECT nome FROM clientes;`

b) `SELECT clientes.nome;`

c) `SHOW nome FROM clientes;`

d) `FIND nome clientes;`

e) `SELECT * nome FROM clientes;`

---

#### **14.** Para **ordenar os produtos pelo preço do maior para o menor**, o comando correto é:

a) `SELECT * FROM produtos ORDER BY preco DESC;`

b) `SELECT * FROM produtos ORDER preco DESC;`

c) `SELECT produtos SORT preco DESC;`

d) `ORDER BY preco DESC produtos;`

e) `SELECT preco DESC FROM produtos;`

---

#### **15.** Qual das opções representa corretamente um **INNER JOIN** entre `clientes` e `pedidos`?

a)

```sql
SELECT * FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.id_cliente;
```

b)

```sql
SELECT * FROM clientes + pedidos;
```

c)

```sql
SELECT * FROM clientes JOIN pedidos;
```

d)

```sql
JOIN clientes.id = pedidos.id_cliente;
```

e)

```sql
SELECT * FROM clientes MERGE pedidos;
```

---

## Questões com base na tabela `funcionarios`

```
ID | NOME             | CARGO          | SALARIO
---|------------------|----------------|---------
1  | Maria Souza      | Gerente        | 8500
2  | João Oliveira    | Analista       | 5500
3  | Ana Costa        | Assistente     | 3500
4  | Pedro Mendes     | Estagiário     | 1800
```

---

#### **16.** Qual comando retorna **todos os registros** da tabela?

a) `SELECT ALL FROM funcionarios;`

b) `SELECT * FROM funcionarios;`

c) `GET * funcionarios;`

d) `SHOW funcionarios;`

e) `LIST * FROM funcionarios;`

---

#### **17.** Qual consulta exibe **apenas o nome e o salário** dos funcionários?

a) `SELECT nome, salario FROM funcionarios;`

b) `SHOW nome, salario funcionarios;`

c) `GET nome, salario FROM funcionarios;`

d) `SELECT * FROM funcionarios WHERE nome, salario;`

e) `SELECT funcionarios(nome, salario);`

---

#### **18.** Como listar apenas os funcionários com **salário acima de 5000**?

a) `SELECT * FROM funcionarios WHERE salario > 5000;`

b) `SELECT funcionarios WHERE salario > 5000;`

c) `FILTER funcionarios salario > 5000;`

d) `SELECT ALL FROM funcionarios SALARIO > 5000;`

e) `SHOW * FROM funcionarios WHERE SALARIO > 5000;`

---

#### **19.** Qual comando retorna apenas os funcionários com o cargo de **“Analista”**?

a) `SELECT * FROM funcionarios WHERE cargo = 'Analista';`

b) `SELECT cargo = Analista FROM funcionarios;`

c) `SELECT * FROM funcionarios HAVING cargo = 'Analista';`

d) `SHOW * FROM funcionarios WHERE cargo == Analista;`

e) `FILTER funcionarios BY cargo = Analista;`

---

#### **20.** Para exibir os funcionários **em ordem alfabética do nome**, o comando correto é:

a) `SELECT * FROM funcionarios ORDER BY nome ASC;`

b) `SELECT * FROM funcionarios ORDER nome ASC;`

c) `ORDER funcionarios BY nome;`

d) `SELECT nome SORT FROM funcionarios;`

e) `SORT * FROM funcionarios BY nome;`

---

# 📄 **GABARITO – Para Entrega ao Professor**

**Nome do(a) Aluno(a):** _______________________________________

| Nº | Resposta | Nº | Resposta |
| -- | -------- | -- | -------- |
| 1  | ____     | 11 | ____     |
| 2  | ____     | 12 | ____     |
| 3  | ____     | 13 | ____     |
| 4  | ____     | 14 | ____     |
| 5  | ____     | 15 | ____     |
| 6  | ____     | 16 | ____     |
| 7  | ____     | 17 | ____     |
| 8  | ____     | 18 | ____     |
| 9  | ____     | 19 | ____     |
| 10 | ____     | 20 | ____     |

