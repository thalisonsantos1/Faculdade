from sqlalchemy import create_engine # é usada para criar a conexão com o banco de dados
from sqlalchemy.orm import declarative_base # criar classe base para os modelos
from sqlalchemy.orm import sessionmaker # objeto para gerenciar as sessões de conexão com o banco de dados. 

DATABASE_URL = "sqlite:///./produtos.db" # definindo o arquivo do banco de dados e onde será salvo 

# definir o motor que conecta ao banco de dados
engine = create_engine (DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # garante a criação de todos os modelos de dados no banco de dados

