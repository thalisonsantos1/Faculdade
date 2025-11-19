# app/models/__init__.py
from app.models.departamento import Departamento
from app.models.cargo import Cargo
from app.models.funcionario import Funcionario
from app.models.treinamento import Treinamento
from app.models.treinamento_realizado import TreinamentoRealizado

__all__ = ["Departamento", "Funcionario", "Treinamento", "Cargo", "TreinamentoRealizado"]