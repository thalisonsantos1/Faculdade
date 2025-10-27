-- Criando tabelas
create table tbl_autor (
    idautor serial primary key, 
    nomeautor varchar(50) not null,
    sobrenomeautor varchar(60) not null
);

create table tbl_autores (
    idautor serial primary key, 
    nomeautor varchar(50) not null,
    sobrenomeautor varchar(60) not null
);

create table tbl_assunto (
    idassunto serial primary key, 
    nomeassunto varchar(35) not null
);

create table tbl_editora (
    ideditora serial primary key, 
    nomeeditora varchar(50) not null
);

create table tbl_livro (
    idlivro serial primary key, 
    nomelivro varchar(80) not null,
    isbn char(13),
    precolivro decimal(6,2) not null,
    numpaginas smallint not null,
    edicao smallint, -- tinyint não existe no postgres; usamos smallint ou int
    datapub date,
    ideditora smallint not null,
    idassunto smallint not null
);

create table tbl_autor_livro (
    idautor smallint,
    idlivro smallint,
    constraint pk_autor_livro primary key(idautor,idlivro), -- chave primária composta
    
    constraint fk_id_autor foreign key (idautor)
     references tbl_autor(idautor) on delete cascade on update cascade,
     
    constraint fk_id_livro foreign key (idlivro)
     references tbl_livro(idlivro) on delete cascade on update cascade
);