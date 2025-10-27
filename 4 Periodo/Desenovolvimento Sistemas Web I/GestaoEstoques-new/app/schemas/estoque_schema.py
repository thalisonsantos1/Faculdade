from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class TipoMovimento(str, Enum):
    ENTRADA = "entrada"
    SAIDA = "saida"


class EstoqueMovimentoBase(BaseModel):
    produto_id: int
    tipo: TipoMovimento
    quantidade: float
    observacao: str | None = None


class EstoqueMovimentoCreate(EstoqueMovimentoBase):
    pass


class EstoqueMovimentoOut(EstoqueMovimentoBase):
    id: int
    data_movimento: datetime

    class Config:
        orm_mode = True
