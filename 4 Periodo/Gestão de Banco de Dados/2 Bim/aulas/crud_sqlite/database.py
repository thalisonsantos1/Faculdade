import sqlite3
from sqlite3 import Error

DB_FILE = 'floricultura.db'

#CRIAR TABELAS

sql_clientes = """
  CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    rg varchar(12) NOT NULL,
    nome varchar(30) NOT NULL,
    sobrenome varchar(40) NOT NULL,
    telefone varchar(12) NOT NULL,
    rua varchar(40),
    numero varchar(5),
    bairro varchar(30),
    );
  """

sql_produtos = """
  CREATE TABLE IF NOT EXISTS produtos (
  id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
  nome_produto varchar(30) NOT NULL,
  tipo varchar (25) NOT NULL,
  preco_decimal(10,2) NOT NULL,
  qtde_estoque smallint NOT NULL
);
"""

sql_vendas = """
  CREATE TABLE IF NOT EXISTS vendas (
  id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
  nota_fiscal smallint NOT NULL,
  id_cliente INTEGER NOT NULL,
  data_compra datetime,
  id_produto INTEGER NOT NULL,
  quantidade smallint NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente),
  FOREIGN KEY (id_produto) REFERENCES produtos (id_produto)
);
"""

def conectar():
  """
  Função para conectar ao banco de dados SQLite.
  Retorna um objeto de conexão (conn) ou None se a conexão falhar.
  """
  try:
    conn = sqlite3.connect(DB_FILE)
    conn.execute(sql_clientes)
    conn.execute(sql_produtos)
    conn.execute(sql_vendas)

    conn.commit()

    print("Conexão com o banco de dados 'floricultura.db' bem sucedida!")
    return conn
  except Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    return None
  
# Verificar se o módulo está funcionando.
if __name__ == '__main__':
  conn=conectar()
  if conn:
    print("Conexão bem-sucedida!")
  else:
    print("Falha na conexão")



conectar()
