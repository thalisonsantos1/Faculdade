from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
from enum import Enum

class TipoMovimento(str, Enum):
    ENTRADA = "ENTRADA"
    SAIDA = "SAIDA"

class EstoqueMovimentoCreate(BaseModel):
    produto_id: int
    tipo: TipoMovimento
    quantidade: int
    motivo: Optional[str] = None
    
    @validator('quantidade')
    def quantidade_positiva(cls, v):
        if v <= 0:
            raise ValueError('Quantidade deve ser maior que zero')
        return v

class EstoqueMovimentoOut(BaseModel):
    id: int
    produto_id: int
    tipo: TipoMovimento
    quantidade: int
    motivo: Optional[str]
    criado_em: datetime
    
    class Config:
        from_attributes = True

class SaldoOut(BaseModel):
    produto_id: int
    saldo: int
    
    class Config:
        from_attributes = True