# 🧾 Prova – Banco de Dados MySQL

**Nome:** ___________________________________________
**Data:** ****/****/______
**Pontuação:** __________ / 20

---

#### **1.** Qual comando é usado para criar uma nova tabela no MySQL?

a) `CREATE DATABASE`
b) `CREATE TABLE`
c) `NEW TABLE`
d) `INSERT TABLE`
e) `MAKE TABLE`

---

#### **2.** Qual das opções abaixo representa corretamente a criação de uma tabela chamada `clientes` com os campos `id` (inteiro) e `nome` (texto)?

a) `CREATE TABLE clientes (id INT, nome CHAR);`
b) `CREATE TABLE clientes id INT, nome VARCHAR(50);`
c) `CREATE TABLE clientes (id INT, nome VARCHAR(50));`
d) `NEW TABLE clientes (id INTEGER, nome TEXT);`
e) `CREATE TABLE clientes VALUES (id INT, nome VARCHAR(50));`

---

#### **3.** O que é uma chave estrangeira (FOREIGN KEY)?

a) Um campo que identifica unicamente cada linha em uma tabela.
b) Um campo que faz referência a uma chave primária em outra tabela.
c) Um campo que não pode receber valores nulos.
d) Um campo usado apenas em consultas complexas.
e) Um campo criado automaticamente pelo MySQL.

---

#### **4.** Qual comando é usado para adicionar uma nova coluna a uma tabela existente?

a) `ALTER TABLE ... ADD COLUMN`
b) `UPDATE TABLE ... ADD`
c) `CREATE COLUMN ...`
d) `ALTER DATABASE ... ADD`
e) `INSERT COLUMN ...`

---

#### **5.** Para modificar o tipo de dado de uma coluna existente, utiliza-se:

a) `ALTER COLUMN TYPE`
b) `UPDATE TYPE`
c) `ALTER TABLE ... MODIFY`
d) `CHANGE DATATYPE`
e) `ALTER DATABASE ... MODIFY`

---

#### **6.** Qual comando apaga todos os registros de uma tabela **sem excluir sua estrutura**?

a) `DELETE * FROM tabela;`
b) `TRUNCATE TABLE tabela;`
c) `DROP TABLE tabela;`
d) `CLEAR TABLE tabela;`
e) `REMOVE * FROM tabela;`

---

#### **7.** O comando `UPDATE` serve para:

a) Inserir novos registros.
b) Excluir registros.
c) Atualizar dados existentes.
d) Criar tabelas.
e) Consultar dados.

---

#### **8.** Qual comando é usado para excluir registros específicos de uma tabela?

a) `DELETE FROM tabela WHERE condição;`
b) `DROP FROM tabela WHERE condição;`
c) `REMOVE FROM tabela WHERE condição;`
d) `TRUNCATE FROM tabela WHERE condição;`
e) `DESTROY FROM tabela WHERE condição;`

---

#### **9.** Para alterar o nome de uma tabela, podemos usar:

a) `RENAME TABLE tabela_velha TO tabela_nova;`
b) `ALTER TABLE tabela_velha RENAME tabela_nova;`
c) Ambas as alternativas acima estão corretas.
d) `CHANGE TABLE tabela_velha tabela_nova;`
e) Nenhuma das anteriores.

---

#### **10.** Qual dos tipos de dados abaixo é mais apropriado para armazenar números inteiros?

a) `CHAR`
b) `INT`
c) `FLOAT`
d) `DATE`
e) `TEXT`

---

#### **11.** Qual comando remove uma tabela inteira, incluindo todos os dados?

a) `DELETE TABLE tabela;`
b) `REMOVE TABLE tabela;`
c) `DROP TABLE tabela;`
d) `TRUNCATE TABLE tabela;`
e) `CLEAR TABLE tabela;`

---

#### **12.** Para consultar todos os registros da tabela `produtos`, o comando correto é:

a) `SELECT * FROM produtos;`
b) `SELECT produtos ALL;`
c) `FIND * IN produtos;`
d) `SHOW produtos;`
e) `GET * produtos;`

---

#### **13.** Para consultar apenas o nome e o preço da tabela `produtos`:

a) `SELECT nome, preco FROM produtos;`
b) `SELECT FROM produtos (nome, preco);`
c) `SHOW nome, preco IN produtos;`
d) `GET nome, preco FROM produtos;`
e) `SELECT * FROM produtos WHERE nome, preco;`

---

#### **14.** Suponha as tabelas `clientes(id_cliente, nome)` e `pedidos(id_pedido, id_cliente, valor)`.

Qual comando lista o nome do cliente e o valor do pedido, **sem usar JOIN**?

a)

```sql
SELECT nome, valor
FROM clientes, pedidos
WHERE clientes.id_cliente = pedidos.id_cliente;
```

b) `SELECT nome, valor FROM clientes JOIN pedidos;`
c) `SELECT nome, valor FROM clientes + pedidos;`
d) `SELECT nome, valor FROM clientes, pedidos;`
e) `SELECT nome, valor FROM pedidos WHERE nome = clientes.nome;`

---

#### **15.** Para adicionar uma chave estrangeira na tabela `pedidos` que referencia `clientes(id_cliente)`, o comando correto é:

a)

```sql
ALTER TABLE pedidos
ADD FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);
```

b)

```sql
ALTER TABLE pedidos
CREATE FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);
```

c) `CREATE FOREIGN KEY pedidos.id_cliente REFERENCES clientes(id_cliente);`
d) `ALTER TABLE pedidos REFERENCES clientes(id_cliente);`
e) `FOREIGN KEY pedidos(id_cliente) REFERENCES clientes(id_cliente);`

---

## Questões com base na tabela `usuarios`

```
ID | NOME                 | DATA_NASCIMENTO | NACIONALIDADE
---|----------------------|-----------------|---------------
1  | Pio de Pietrelcina   | 25/05/1887      | Itália
2  | Karol Józef Wojtyła  | 18/05/1920      | Polônia
3  | José de Anchieta     | 19/03/1534      | Espanha
```

---

#### **16.** Qual comando retorna **todos os registros** dessa tabela?

a) `SELECT ALL usuarios;`
b) `SELECT * FROM usuarios;`
c) `GET * usuarios;`
d) `SHOW TABLE usuarios;`
e) `DISPLAY usuarios;`

---

#### **17.** Qual consulta mostra apenas os nomes dos usuários?

a) `SELECT NOME FROM usuarios;`
b) `SELECT * NOME usuarios;`
c) `SELECT usuarios.NOME;`
d) `SHOW NOME IN usuarios;`
e) `GET NOME FROM usuarios;`

---

#### **18.** Como listar apenas os usuários **nascidos antes de 1900**?

a) `SELECT * FROM usuarios WHERE DATA_NASCIMENTO < '1900-01-01';`
b) `SELECT * FROM usuarios WHERE DATA_NASCIMENTO < 1900;`
c) `SELECT * FROM usuarios WHERE DATA_NASCIMENTO < 01/01/1900;`
d) `SELECT * FROM usuarios HAVING DATA_NASCIMENTO < 1900;`
e) `FILTER usuarios BY DATA_NASCIMENTO < 1900;`

---

#### **19.** Qual comando retorna apenas os usuários de **nacionalidade italiana**?

a) `SELECT * FROM usuarios WHERE NACIONALIDADE = 'Itália';`
b) `SELECT * FROM usuarios HAVING NACIONALIDADE = 'Itália';`
c) `SELECT usuarios WHERE país = 'Itália';`
d) `FILTER usuarios BY NACIONALIDADE = 'Itália';`
e) `SHOW * FROM usuarios WHERE NACIONALIDADE == Itália;`

---

#### **20.** Para ordenar a lista dos usuários **por data de nascimento (mais antigo primeiro)**, o comando correto é:

a) `SELECT * FROM usuarios ORDER BY DATA_NASCIMENTO ASC;`
b) `SELECT * FROM usuarios SORT DATA_NASCIMENTO;`
c) `SELECT * FROM usuarios BY DATA_NASCIMENTO ASC;`
d) `ORDER usuarios BY DATA_NASCIMENTO ASC;`
e) `SELECT * FROM usuarios DATE ORDER;`

---

# 📄 GABARITO – Para Entrega ao Professor

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

