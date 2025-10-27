CREATE DATABASE rh;

create user rhuser with password 'Libert@as';

grant all privileges on database rh to rhuser;

alter database rh owner to rhuser;

grant all privileges on schema public to rhuser;

alter schema public owner to rhuser;


CREATE TABLE departamentos (
  id_departamento SERIAL PRIMARY KEY, 
  nome_departamento VARCHAR(50) NOT NULL
);

CREATE TABLE cargos (
  id_cargo VARCHAR(20) PRIMARY KEY,
  nome_cargo VARCHAR(50) NOT NULL
);

CREATE TABLE funcionarios (
  id_funcionario SERIAL PRIMARY KEY, 
  nome VARCHAR(50) NOT NULL,
  sobrenome VARCHAR(50) NOT NULL,
  data_nascimento DATE,
  id_cargo VARCHAR(20),
  id_departamento INT,
  salario DECIMAL(10,2)
);

CREATE TABLE treinamentos (
  id_treinamento SERIAL PRIMARY KEY, 
  nome_treinamento VARCHAR(100) NOT NULL,
  data_inicio DATE,
  data_fim DATE,
  carga_horaria INT,
  trei_local VARCHAR(100),
  ministrante VARCHAR(100),
  id_funcionario INT,

  CONSTRAINT fk_treinamento_funcionario
    FOREIGN KEY (id_funcionario)
    REFERENCES funcionarios (id_funcionario)
    ON UPDATE NO ACTION
    ON DELETE RESTRICT
);



insert into funcionarios (nome, sobrenome, data_nascimento, id_cargo, id_departamento, salario)
values
	('Hermenegildo', 'Silva', '1985-08-22', 'Marketing', 1, 5500),
	('Maria', 'Engomada', '1796-08-10', 'Financeiro', 2, 10000);



INSERT INTO treinamentos (nome_treinamento, data_inicio, data_fim, carga_horaria, trei_local, ministrante, id_funcionario)
VALUES
  ('Introdução ao SQL', '2025-07-01', '2025-07-05', 20, 'Sala de treinamento', 'João Silva', 1),
  ('Gestão de Projetos', '2025-08-15', '2025-08-20', 30, 'Auditório', 'Maria Santos', 2),
  ('Desenvolvimento Web', '2025-09-10', '2025-09-25', 40, 'Laboratório', 'Pedro Almeida', 3);


INSERT INTO treinamentos (nome_treinamento, data_inicio, data_fim, carga_horaria, trei_local, ministrante, id_funcionario)
VALUES
  ('Treinamento Avançado PostgreSQL', CURRENT_DATE + INTERVAL '10 days', CURRENT_DATE + INTERVAL '12 days', 16, 'Sala de TI', 'Ana Costa', 1),
  ('Segurança da Informação', CURRENT_DATE + INTERVAL '20 days', CURRENT_DATE + INTERVAL '22 days', 16, 'Auditório', 'Carlos Lima', 2);


SELECT * FROM cargos;
SELECT * FROM departamentos;
SELECT * FROM funcionarios;
SELECT * FROM treinamentos;


SELECT f.nome, f.sobrenome, c.nome_cargo, d.nome_departamento, f.salario
FROM funcionarios f
LEFT JOIN cargos c ON f.id_cargo = c.id_cargo
LEFT JOIN departamentos d ON f.id_departamento = d.id_departamento;


SELECT *
FROM funcionarios
WHERE id_funcionario IN (1,7);


DELETE FROM funcionarios
WHERE id_funcionario = 7;


SELECT MAX(salario) AS maior_salario, MIN(salario) AS menor_salario
FROM funcionarios;


SELECT CONCAT(nome, ' ', sobrenome) AS nome_completo, salario
FROM funcionarios;

SELECT f.*
FROM funcionarios f
JOIN departamentos d ON f.id_departamento = d.id_departamento
WHERE d.nome_departamento = 'Tecnologia da Informação';


SELECT AVG(salario) AS media_salarial
FROM funcionarios;


SELECT (DATE '2025-12-25' - CURRENT_DATE) AS dias_para_natal;


CREATE OR REPLACE VIEW vw_funcionarios_completo AS
SELECT f.id_funcionario, f.nome, f.sobrenome, c.nome_cargo, d.nome_departamento, f.salario
FROM funcionarios f
LEFT JOIN cargos c ON f.id_cargo = c.id_cargo
LEFT JOIN departamentos d ON f.id_departamento = d.id_departamento;


CREATE OR REPLACE FUNCTION fn_funcionarios_acima_salario(min_salario NUMERIC)
RETURNS TABLE(id_funcionario INT, nome VARCHAR, sobrenome VARCHAR, salario NUMERIC) AS $$
BEGIN
    RETURN QUERY
    SELECT id_funcionario, nome, sobrenome, salario
    FROM funcionarios
    WHERE salario > min_salario;
END;
$$ LANGUAGE plpgsql;


