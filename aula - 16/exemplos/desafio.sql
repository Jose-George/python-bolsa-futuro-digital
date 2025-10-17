CREATE DATABASE biblioteca; --cria

USE biblioteca; -- usar o banco de dados biblioteca

CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    ano_publicacao INT
);

INSERT INTO livros (titulo, autor, ano_publicacao)
VALUES
('Dom Casmurro', 'Machado de Assis', 1899),
('O Alienista', 'Machado de Assis', 1882),
('Memórias Póstumas de Brás Cubas', 'Machado de Assis', 1881),
('Capitães da Areia', 'Jorge Amado', 1937);

SELECT * FROM livros;


INSERT INTO livros (titulo, autor, ano_publicacao)
VALUES
('Capitães da Areia versão 2', '', 1937);


select titulo, autor from livros where autor = 'Machado de Assis';


UPDATE livros
SET autor = 'Jorge Amado'
WHERE id = 5;


DELETE FROM livros where id in (5, 6);


CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    serie VARCHAR(20)
);

INSERT INTO alunos (nome, idade, serie)
VALUES
('Humberto', 22, '3 serie'),
('Joao Victor', 22, '1 ano'),
('Jose George', 22, '8 serie');

select nome, idade from alunos where serie = '8 serie';

UPDATE alunos
SET idade = 40
WHERE id = 3;

delete from alunos where id = 3;