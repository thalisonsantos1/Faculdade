#!/usr/bin/env python3
"""
Script para resetar o banco de dados
Executa antes de iniciar o servidor FastAPI
"""
import os
from app.db.base import Base
from app.db.session import engine

# Remove o arquivo de banco de dados se existir
db_path = "banco_de_dados.db"
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"✓ Banco de dados {db_path} removido")

# Cria as tabelas novamente com o novo schema
Base.metadata.create_all(bind=engine)
print("✓ Tabelas recriadas com sucesso")
print("Agora você pode iniciar o servidor com: python -m uvicorn app.main:app --reload")
