from fastapi import FastAPI
from app.api.v1 import produto, categoria
from app.api.v1.routes_estoque import router as rotas_estoque

app = FastAPI()

app.include_router(produto.rotas)
app.include_router(categoria.rotas)
app.include_router(rotas_estoque)
