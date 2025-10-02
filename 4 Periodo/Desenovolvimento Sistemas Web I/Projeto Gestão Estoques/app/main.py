from fastapi import FastAPI
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.api.v1.rotas import api_router
from app.routers.v1 import produto, estoque
# criar as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gestao de Estoque API")
app.include_router(produto.router, prefix="/api/v1")
app.include_router(estoque.router, prefix="/api/v1")
app.include_router(api_router, prefix="/api/v1")