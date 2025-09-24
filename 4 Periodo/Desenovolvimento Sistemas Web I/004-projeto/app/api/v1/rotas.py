from fastapi import APIRouter
from . import categoria, produto #está dentro da mesma pasta

api_rotas = APIRouter()
api_rotas.include_router(categoria.rotas)
api_rotas.include_router(produto.rotas)