from app.db.database import Base, engine
from app.models import categoria, produto 

print("Criando tabelas no banco...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
