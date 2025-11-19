from app.schemas.cargo import CargoCreate
from fastapi import HTTPException, status

def criar_cargo(payload: CargoCreate):
    if payload.salario <= 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Salario deve ser maior que zero")
    