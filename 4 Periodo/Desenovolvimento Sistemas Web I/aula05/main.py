from fastapi import FastAPI
from modelos import Produto
from typing import List

app = FastAPI()
#bd em memoria - lista

bd_produtos: list[Produto] = []

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.post("/produtos")
def adicionar (prod: Produto):
    bd_produtos.append(prod)
    return {"message": "Produto adicionado com sucesso"}

@app.get("/produtos", response_model=List[Produto])
def lista_todos():
    return bd_produtos