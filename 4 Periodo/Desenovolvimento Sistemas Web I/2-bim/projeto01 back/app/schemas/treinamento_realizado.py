from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class TreinamentoRealizadoCreate(BaseModel):
    funcionario_id: int
    treinamento_id: int
    data_realizacao: date = Field(default_factory=date.today)

class TreinamentoRealizadoUpdate(BaseModel):
    data_realizacao: Optional[date] = None

class TreinamentoRealizadoOut(BaseModel):
    id: int
    funcionario_id: int
    treinamento_id: int
    data_realizacao: date
    data_validade: date

    class Config:
        from_attributes = True