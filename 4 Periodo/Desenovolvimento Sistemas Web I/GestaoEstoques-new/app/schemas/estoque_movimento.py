from pydantic import BaseModel
from enum import Enum

class TipoMovimento(str, Enum):
    ENTRADA = "entrada"
    SAIDA = "saida"

class EstoqueMovimentoBase(BaseModel):
    produto_id: int
    tipo: TipoMovimento
    quantidade: int
    observacao: str | None = None

class EstoqueMovimentoCreate(EstoqueMovimentoBase):
    pass

class EstoqueMovimentoResponse(EstoqueMovimentoBase):
    id: int

    class Config:
        orm_mode = True
