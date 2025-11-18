from pydantic import BaseModel, Field
from typing import Optional

class TreinamentoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    carga_horaria: float
    validade_dias: int = Field(gt=0, description="Número de dias de validade do treinamento")

class TreinamentoCreate(TreinamentoBase):
    pass

class TreinamentoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    carga_horaria: Optional[float] = None
    validade_dias: Optional[int] = Field(None, gt=0, description="Número de dias de validade do treinamento")

class Treinamento(TreinamentoBase):
    id: int

    class Config:
        from_attributes = True