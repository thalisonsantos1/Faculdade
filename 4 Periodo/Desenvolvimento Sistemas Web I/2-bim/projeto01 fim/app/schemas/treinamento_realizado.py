from pydantic import BaseModel, field_validator
from datetime import date, datetime
from typing import Optional

class TreinamentoRealizadoCreate(BaseModel):
    funcionario_id: int
    treinamento_id: int
    data_realizacao: datetime  # Recebe como datetime ou string ISO
    
    @field_validator('data_realizacao', mode='before')
    @classmethod
    def validate_date(cls, v):
        """Garante que a data esteja em formato ISO YYYY-MM-DD"""
        # Accept date string, date or datetime
        if isinstance(v, str):
            # If only date part provided, parse as date and convert to midnight datetime
            try:
                # Try parsing full datetime ISO first
                return datetime.fromisoformat(v)
            except Exception:
                d = date.fromisoformat(v.split('T')[0])
                return datetime.combine(d, datetime.min.time())
        elif isinstance(v, datetime):
            return v
        elif isinstance(v, date):
            return datetime.combine(v, datetime.min.time())
        return v

class TreinamentoRealizadoUpdate(BaseModel):
    data_realizacao: Optional[datetime] = None
    
    @field_validator('data_realizacao', mode='before')
    @classmethod
    def validate_date(cls, v):
        """Garante que a data esteja em formato ISO YYYY-MM-DD"""
        if v is None:
            return None
        if isinstance(v, str):
            try:
                return datetime.fromisoformat(v)
            except Exception:
                d = date.fromisoformat(v.split('T')[0])
                return datetime.combine(d, datetime.min.time())
        elif isinstance(v, datetime):
            return v
        elif isinstance(v, date):
            return datetime.combine(v, datetime.min.time())
        return v

class TreinamentoRealizadoOut(BaseModel):
    id: int
    funcionario_id: int
    treinamento_id: int
    data_realizacao: datetime  # Retorna como datetime ISO
    data_validade: datetime    # Retorna como datetime ISO

    class Config:
        from_attributes = True