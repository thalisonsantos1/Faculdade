from app.db.database import Base, engine
from app.models import produto, categoria, estoque_movimento

print(" Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print(" Tabelas criadas com sucesso!")
