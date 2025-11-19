from fastapi import FastAPI
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.api.v1.rotas import api_rotas
from fastapi.middleware.cors import CORSMiddleware
from app.models import * 




# criar as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_rotas)