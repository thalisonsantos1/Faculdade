from fastapi import APIRouter
from app.api.v1 import produto, estoque, categoria

api_router = APIRouter()

api_router.include_router(produto.router, prefix="/produtos", tags=["produtos"])
api_router.include_router(estoque.router, prefix="/estoque", tags=["estoque"])
api_router.include_router(categoria.router, prefix="/categorias", tags=["categorias"])
