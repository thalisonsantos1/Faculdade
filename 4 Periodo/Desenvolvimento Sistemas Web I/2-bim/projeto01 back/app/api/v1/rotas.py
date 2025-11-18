from fastapi import APIRouter
from app.api.v1 import cargo, departamento, funcionario, treinamento, treinamento_realizado

api_rotas = APIRouter()
api_rotas.include_router(cargo.rotas)
api_rotas.include_router(departamento.rotas)
api_rotas.include_router(funcionario.rotas)
api_rotas.include_router(treinamento.rotas)
api_rotas.include_router(treinamento_realizado.rotas)