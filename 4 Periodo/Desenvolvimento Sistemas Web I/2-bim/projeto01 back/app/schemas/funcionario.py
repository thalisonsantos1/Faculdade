from pydantic import BaseModel, ConfigDict
from typing import Optional

class FuncionarioCreate(BaseModel):
    nome: str
    cargo_id: int

class FuncionarioOut(BaseModel):
    id: int
    nome: str
    cargo_id: int
    model_config = ConfigDict(from_attributes=True)

class FuncionarioUpdate(BaseModel):
    nome: Optional[str] = None
    cargo_id: Optional[int] = None