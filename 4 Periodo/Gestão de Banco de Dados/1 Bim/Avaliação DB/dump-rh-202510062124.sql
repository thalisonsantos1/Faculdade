--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

-- Started on 2025-10-06 21:24:58

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: rhuser
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO rhuser;

--
-- TOC entry 225 (class 1255 OID 66472)
-- Name: fn_funcionarios_acima_salario(numeric); Type: FUNCTION; Schema: public; Owner: rhuser
--

CREATE FUNCTION public.fn_funcionarios_acima_salario(min_salario numeric) RETURNS TABLE(id_funcionario integer, nome character varying, sobrenome character varying, salario numeric)
    LANGUAGE plpgsql
    AS $$
BEGIN
    RETURN QUERY
    SELECT id_funcionario, nome, sobrenome, salario
    FROM funcionarios
    WHERE salario > min_salario;
END;
$$;


ALTER FUNCTION public.fn_funcionarios_acima_salario(min_salario numeric) OWNER TO rhuser;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 219 (class 1259 OID 66448)
-- Name: cargos; Type: TABLE; Schema: public; Owner: rhuser
--

CREATE TABLE public.cargos (
    id_cargo character varying(20) NOT NULL,
    nome_cargo character varying(50) NOT NULL
);


ALTER TABLE public.cargos OWNER TO rhuser;

--
-- TOC entry 218 (class 1259 OID 66442)
-- Name: departamentos; Type: TABLE; Schema: public; Owner: rhuser
--

CREATE TABLE public.departamentos (
    id_departamento integer NOT NULL,
    nome_departamento character varying(50) NOT NULL
);


ALTER TABLE public.departamentos OWNER TO rhuser;

--
-- TOC entry 217 (class 1259 OID 66441)
-- Name: departamentos_id_departamento_seq; Type: SEQUENCE; Schema: public; Owner: rhuser
--

CREATE SEQUENCE public.departamentos_id_departamento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.departamentos_id_departamento_seq OWNER TO rhuser;

--
-- TOC entry 4930 (class 0 OID 0)
-- Dependencies: 217
-- Name: departamentos_id_departamento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rhuser
--

ALTER SEQUENCE public.departamentos_id_departamento_seq OWNED BY public.departamentos.id_departamento;


--
-- TOC entry 221 (class 1259 OID 66454)
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: rhuser
--

CREATE TABLE public.funcionarios (
    id_funcionario integer NOT NULL,
    nome character varying(50) NOT NULL,
    sobrenome character varying(50) NOT NULL,
    data_nascimento date,
    id_cargo character varying(20),
    id_departamento integer,
    salario numeric(10,2)
);


ALTER TABLE public.funcionarios OWNER TO rhuser;

--
-- TOC entry 220 (class 1259 OID 66453)
-- Name: funcionarios_id_funcionario_seq; Type: SEQUENCE; Schema: public; Owner: rhuser
--

CREATE SEQUENCE public.funcionarios_id_funcionario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.funcionarios_id_funcionario_seq OWNER TO rhuser;

--
-- TOC entry 4931 (class 0 OID 0)
-- Dependencies: 220
-- Name: funcionarios_id_funcionario_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rhuser
--

ALTER SEQUENCE public.funcionarios_id_funcionario_seq OWNED BY public.funcionarios.id_funcionario;


--
-- TOC entry 223 (class 1259 OID 66461)
-- Name: treinamentos; Type: TABLE; Schema: public; Owner: rhuser
--

CREATE TABLE public.treinamentos (
    id_treinamento integer NOT NULL,
    nome_treinamento character varying(100) NOT NULL,
    data_inicio date,
    data_fim date,
    carga_horaria integer,
    trei_local character varying(100),
    ministrante character varying(100),
    id_funcionario integer
);


ALTER TABLE public.treinamentos OWNER TO rhuser;

--
-- TOC entry 222 (class 1259 OID 66460)
-- Name: treinamentos_id_treinamento_seq; Type: SEQUENCE; Schema: public; Owner: rhuser
--

CREATE SEQUENCE public.treinamentos_id_treinamento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.treinamentos_id_treinamento_seq OWNER TO rhuser;

--
-- TOC entry 4932 (class 0 OID 0)
-- Dependencies: 222
-- Name: treinamentos_id_treinamento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rhuser
--

ALTER SEQUENCE public.treinamentos_id_treinamento_seq OWNED BY public.treinamentos.id_treinamento;


--
-- TOC entry 224 (class 1259 OID 66468)
-- Name: vw_funcionarios_completo; Type: VIEW; Schema: public; Owner: rhuser
--

CREATE VIEW public.vw_funcionarios_completo AS
 SELECT f.id_funcionario,
    f.nome,
    f.sobrenome,
    c.nome_cargo,
    d.nome_departamento,
    f.salario
   FROM ((public.funcionarios f
     LEFT JOIN public.cargos c ON (((f.id_cargo)::text = (c.id_cargo)::text)))
     LEFT JOIN public.departamentos d ON ((f.id_departamento = d.id_departamento)));


ALTER VIEW public.vw_funcionarios_completo OWNER TO rhuser;

--
-- TOC entry 4761 (class 2604 OID 66445)
-- Name: departamentos id_departamento; Type: DEFAULT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.departamentos ALTER COLUMN id_departamento SET DEFAULT nextval('public.departamentos_id_departamento_seq'::regclass);


--
-- TOC entry 4762 (class 2604 OID 66457)
-- Name: funcionarios id_funcionario; Type: DEFAULT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.funcionarios ALTER COLUMN id_funcionario SET DEFAULT nextval('public.funcionarios_id_funcionario_seq'::regclass);


--
-- TOC entry 4763 (class 2604 OID 66464)
-- Name: treinamentos id_treinamento; Type: DEFAULT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.treinamentos ALTER COLUMN id_treinamento SET DEFAULT nextval('public.treinamentos_id_treinamento_seq'::regclass);


--
-- TOC entry 4920 (class 0 OID 66448)
-- Dependencies: 219
-- Data for Name: cargos; Type: TABLE DATA; Schema: public; Owner: rhuser
--

COPY public.cargos (id_cargo, nome_cargo) FROM stdin;
ANALISTA	Analista de Sistemas
GERENTE	Gerente de Projetos
ESTAGIARIO	Estagiário
ASSISTENTE	Assistente Administrativo
DIRETOR	Diretor
\.


--
-- TOC entry 4919 (class 0 OID 66442)
-- Dependencies: 218
-- Data for Name: departamentos; Type: TABLE DATA; Schema: public; Owner: rhuser
--

COPY public.departamentos (id_departamento, nome_departamento) FROM stdin;
1	Tecnologia da Informação
2	Desenvolvimento
3	Administração
4	Marketing
5	Financeiro
\.


--
-- TOC entry 4922 (class 0 OID 66454)
-- Dependencies: 221
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: rhuser
--

COPY public.funcionarios (id_funcionario, nome, sobrenome, data_nascimento, id_cargo, id_departamento, salario) FROM stdin;
1	João	Silva	1980-01-01	ANALISTA	1	5000.00
2	Maria	Santos	1985-05-15	GERENTE	2	8000.00
4	Ana	Oliveira	1995-08-10	ASSISTENTE	3	2500.00
5	Carlos	Souza	1978-03-20	DIRETOR	3	12000.00
6	Thalison	Santos	1993-08-22	Marketing	1	5500.00
\.


--
-- TOC entry 4924 (class 0 OID 66461)
-- Dependencies: 223
-- Data for Name: treinamentos; Type: TABLE DATA; Schema: public; Owner: rhuser
--

COPY public.treinamentos (id_treinamento, nome_treinamento, data_inicio, data_fim, carga_horaria, trei_local, ministrante, id_funcionario) FROM stdin;
1	Introdução ao SQL	2025-07-01	2025-07-05	20	Sala de treinamento	João Silva	1
2	Gestão de Projetos	2025-08-15	2025-08-20	30	Auditório	Maria Santos	2
3	Desenvolvimento Web	2025-09-10	2025-09-25	40	Laboratório	Pedro Almeida	3
4	Treinamento Avançado PostgreSQL	2025-10-16	2025-10-18	16	Sala de TI	Ana Costa	1
5	Segurança da Informação	2025-10-26	2025-10-28	16	Auditório	Carlos Lima	2
\.


--
-- TOC entry 4933 (class 0 OID 0)
-- Dependencies: 217
-- Name: departamentos_id_departamento_seq; Type: SEQUENCE SET; Schema: public; Owner: rhuser
--

SELECT pg_catalog.setval('public.departamentos_id_departamento_seq', 1, false);


--
-- TOC entry 4934 (class 0 OID 0)
-- Dependencies: 220
-- Name: funcionarios_id_funcionario_seq; Type: SEQUENCE SET; Schema: public; Owner: rhuser
--

SELECT pg_catalog.setval('public.funcionarios_id_funcionario_seq', 7, true);


--
-- TOC entry 4935 (class 0 OID 0)
-- Dependencies: 222
-- Name: treinamentos_id_treinamento_seq; Type: SEQUENCE SET; Schema: public; Owner: rhuser
--

SELECT pg_catalog.setval('public.treinamentos_id_treinamento_seq', 5, true);


--
-- TOC entry 4767 (class 2606 OID 66452)
-- Name: cargos cargos_pkey; Type: CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.cargos
    ADD CONSTRAINT cargos_pkey PRIMARY KEY (id_cargo);


--
-- TOC entry 4765 (class 2606 OID 66447)
-- Name: departamentos departamentos_pkey; Type: CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.departamentos
    ADD CONSTRAINT departamentos_pkey PRIMARY KEY (id_departamento);


--
-- TOC entry 4769 (class 2606 OID 66459)
-- Name: funcionarios funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (id_funcionario);


--
-- TOC entry 4771 (class 2606 OID 66466)
-- Name: treinamentos treinamentos_pkey; Type: CONSTRAINT; Schema: public; Owner: rhuser
--

ALTER TABLE ONLY public.treinamentos
    ADD CONSTRAINT treinamentos_pkey PRIMARY KEY (id_treinamento);


-- Completed on 2025-10-06 21:24:59

--
-- PostgreSQL database dump complete
--

