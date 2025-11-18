from pydantic import BaseModel, ConfigDict
from typing import Optional

class CargoCreate(BaseModel):
    nome: str
    salario: float
    descricao: str
    departamento_id: int

class CargoOut(BaseModel):
    id: int
    nome: str
    salario: float
    descricao: str
    departamento_id: int
    model_config = ConfigDict(from_attributes=True)

class CargoUpdate(BaseModel):
    nome: Optional[str] = None
    salario: Optional[float] = None
    descricao: Optional[str] = None
    departamento_id: Optional[int] = None