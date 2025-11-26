from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

class TreinamentoRealizadoCreate(BaseModel):
    funcionario_id: int
    treinamento_id: int
    data_realizacao: str  # Recebe como string ISO "YYYY-MM-DD"
    
    @field_validator('data_realizacao', mode='before')
    @classmethod
    def validate_date(cls, v):
        """Garante que a data esteja em formato ISO YYYY-MM-DD"""
        if isinstance(v, str):
            # Remove informações de hora se houver
            v = v.split('T')[0]
            # Valida que é uma data válida
            date.fromisoformat(v)
            return v
        elif isinstance(v, date):
            return v.isoformat()
        return v

class TreinamentoRealizadoUpdate(BaseModel):
    data_realizacao: Optional[str] = None
    
    @field_validator('data_realizacao', mode='before')
    @classmethod
    def validate_date(cls, v):
        """Garante que a data esteja em formato ISO YYYY-MM-DD"""
        if v is None:
            return None
        if isinstance(v, str):
            v = v.split('T')[0]
            date.fromisoformat(v)
            return v
        elif isinstance(v, date):
            return v.isoformat()
        return v

class TreinamentoRealizadoOut(BaseModel):
    id: int
    funcionario_id: int
    treinamento_id: int
    data_realizacao: str  # Retorna como string ISO
    data_validade: str    # Retorna como string ISO

    class Config:
        from_attributes = True