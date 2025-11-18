from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Cargo(Base):
    __tablename__ = "cargos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255))
    salario = Column(Float)
    departamento_id = Column(Integer, ForeignKey("departamentos.id"), nullable=False)
    
    departamento = relationship("Departamento", back_populates="cargos")
    funcionarios = relationship("Funcionario", back_populates="cargo")
