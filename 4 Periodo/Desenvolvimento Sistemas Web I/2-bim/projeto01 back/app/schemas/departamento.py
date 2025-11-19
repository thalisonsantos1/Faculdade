from pydantic import BaseModel, ConfigDict
from typing import Optional

class DepartamentoCreate(BaseModel):
    nome: str
    descricao: str

class DepartamentoOut(BaseModel):
    id: int
    nome: str
    descricao: str
    model_config = ConfigDict(from_attributes=True)

class DepartamentoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
