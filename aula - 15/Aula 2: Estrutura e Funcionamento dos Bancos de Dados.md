# 🧩 Aula 2: Estrutura e Funcionamento dos Bancos de Dados

## 🎯 Objetivo da Aula

Compreender **como os dados são organizados dentro de um banco de dados**, o que são **tabelas, registros e campos**, e como isso se relaciona com o **modelo relacional**.
Vamos também dar os **primeiros passos no raciocínio lógico dos bancos de dados**, preparando o terreno para aprender **SQL** futuramente.

---

## 🧱 1. Relembrando a Base

Na aula anterior, aprendemos que um **banco de dados** é como um **armário digital** onde guardamos informações de maneira estruturada.

Agora, vamos abrir esse armário e entender **como as coisas são organizadas lá dentro.**

---

## 📊 2. Estrutura Básica de um Banco de Dados Relacional

O modelo mais comum é o **banco de dados relacional**, e ele se baseia em **tabelas**.

Pense assim:

| Conceito                         | Explicação                                                      | Exemplo               |
| -------------------------------- | --------------------------------------------------------------- | --------------------- |
| **Tabela**                       | É como uma planilha do Excel, que guarda dados de um mesmo tipo | Tabela de clientes    |
| **Linha (Registro)**             | Representa um item ou entidade individual                       | Um cliente específico |
| **Coluna (Campo)**               | Representa uma característica (atributo) de cada registro       | Nome, Idade, Email    |
| **Chave Primária (Primary Key)** | É o identificador único de cada registro                        | ID do cliente         |

---

### 🧠 Exemplo Prático

Imagine uma **tabela de clientes**:

| id_cliente | nome       | idade | email                                             |
| ---------- | ---------- | ----- | ------------------------------------------------- |
| 1          | Maria Lima | 30    | [maria@gmail.com](mailto:maria@gmail.com)         |
| 2          | João Souza | 25    | [joao@gmail.com](mailto:joao@gmail.com)           |
| 3          | Ana Costa  | 28    | [ana.costa@yahoo.com](mailto:ana.costa@yahoo.com) |

➡️ Cada linha é um **registro** (um cliente).
➡️ Cada coluna é um **campo** (nome, idade, email).
➡️ A coluna `id_cliente` é a **chave primária** — ela **nunca se repete**.

---

## 🔗 3. Relacionamentos entre Tabelas

Em um banco de dados relacional, as tabelas **podem se conectar entre si**.

Por exemplo:

* Uma **tabela de clientes**.
* Uma **tabela de pedidos**.

| id_pedido | id_cliente | produto        | valor |
| --------- | ---------- | -------------- | ----- |
| 1         | 1          | Celular        | 2500  |
| 2         | 1          | Fone de Ouvido | 300   |
| 3         | 2          | Notebook       | 4200  |

O campo **id_cliente** aparece nas duas tabelas — é o que chamamos de **chave estrangeira (Foreign Key)**.
Ela **liga** um cliente aos seus pedidos.

📌 Assim o banco sabe **quem comprou o quê**, sem precisar repetir todas as informações do cliente a cada compra.

---

## ⚙️ 4. Como o Banco Organiza Tudo Isso

Os bancos de dados possuem um **Sistema Gerenciador de Banco de Dados (SGBD)** — o software responsável por controlar:

* Como os dados são **armazenados**;
* Quem pode **acessar**;
* Como fazer **buscas rápidas**;
* E como **garantir a integridade** das informações.

Exemplos de SGBDs:

| Tipo                        | Exemplos                          |
| --------------------------- | --------------------------------- |
| **Relacionais**             | MySQL, PostgreSQL, SQLite, Oracle |
| **Não Relacionais (NoSQL)** | MongoDB, Firebase, Redis          |

---

## 🧩 5. Benefícios do Modelo Relacional

| Vantagem                     | Explicação                                                                          |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| **Organização**              | Os dados são divididos em tabelas e relacionados entre si.                          |
| **Evita redundância**        | Não precisamos repetir informações (por exemplo, o nome do cliente em cada pedido). |
| **Facilidade de busca**      | Podemos encontrar e combinar dados de várias tabelas.                               |
| **Segurança e consistência** | O sistema garante que os dados fiquem corretos e sincronizados.                     |

---

## 🧮 6. Pensando em Termos de Banco de Dados

Antes de aprender a programar em SQL, é importante **pensar como o banco de dados pensa**.

👉 Se você fosse criar um sistema de escola, que tabelas teria?

Talvez:

* **Alunos** (id, nome, idade, turma)
* **Professores** (id, nome, disciplina)
* **Turmas** (id, nome, ano)
* **Notas** (id, id_aluno, id_turma, nota)

Perceba que as tabelas **se conectam** e formam uma rede lógica de dados.

---

## 🧠 7. Resumo da Aula

| Conceito          | Descrição                                |
| ----------------- | ---------------------------------------- |
| Tabela            | Conjunto de dados sobre um mesmo assunto |
| Registro          | Linha da tabela (uma ocorrência)         |
| Campo             | Coluna que descreve uma característica   |
| Chave Primária    | Identifica cada registro de forma única  |
| Chave Estrangeira | Liga uma tabela a outra                  |
| SGBD              | Sistema que gerencia os bancos de dados  |

---

## 🧩 8. Exercícios de Fixação

1. **Identifique as partes:**
   Dada a tabela abaixo, diga:

   * Qual é a chave primária?
   * Quais são os campos?
   * Quantos registros existem?

   | id_produto | nome_produto | preco | estoque |
   | ---------- | ------------ | ----- | ------- |
   | 1          | Caderno      | 15.00 | 200     |
   | 2          | Caneta       | 3.50  | 500     |
   | 3          | Mochila      | 80.00 | 50      |

---

2. **Relacione as tabelas:**
   Imagine que você tem as tabelas abaixo:

   **Clientes**

   | id_cliente | nome  |
   | ---------- | ----- |
   | 1          | Lucas |
   | 2          | Paula |

   **Pedidos**

   | id_pedido | id_cliente | produto |
   | --------- | ---------- | ------- |
   | 1         | 1          | Celular |
   | 2         | 1          | Teclado |
   | 3         | 2          | Fone    |

   * Qual cliente fez mais pedidos?
   * Qual campo faz a ligação entre as duas tabelas?

---

3. **Raciocínio lógico:**

   * Se você fosse criar um sistema para uma biblioteca, quais tabelas existiriam?
   * Quais campos cada uma delas teria?
   * Qual seria a chave primária e as chaves estrangeiras?

---

## 🗝️ Conclusão

Nesta aula, você aprendeu **como os dados são estruturados dentro de um banco de dados** — o que são tabelas, registros e relacionamentos.
Esses conceitos são a **base do modelo relacional**, que é usado na maioria dos bancos do mundo.

Na próxima aula, vamos **entrar no SQL**, a linguagem usada para **criar, consultar e manipular** bancos de dados.
