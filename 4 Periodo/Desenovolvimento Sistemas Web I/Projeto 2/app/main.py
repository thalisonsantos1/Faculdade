from fastapi import FastAPI
from app.routes import categorias, produtos, estoque
from app.db.base import engine, Base

# Criar tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Gestão de Estoques")

# Incluir rotas
app.include_router(categorias.router)
app.include_router(produtos.router)
app.include_router(estoque.router)

@app.get("/")
def read_root():
    return {"message": "Sistema de Gestão de Estoques API"}