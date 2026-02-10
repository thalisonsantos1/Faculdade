## Gabriel Teixeira Santos 007269    
## Thalison de Oliveira Santos 003540

# Gente Control — Gestão de Pessoas e Treinamentos

Projeto simples com backend em FastAPI + SQLAlchemy e frontend estático (HTML/JS + Bootstrap).

**Requisitos**
- Python 3.11+ (o projeto foi testado localmente com Python 3.13).
- Git (opcional)

**Dependências**
As dependências estão listadas em `dependencies.txt`.

Instalação (recomendada em ambiente virtual):

PowerShell (Windows):

```powershell
# criar virtualenv
python -m venv .venv
# ativar (PowerShell)
.\.venv\Scripts\Activate.ps1
# atualizar pip
python -m pip install --upgrade pip
# instalar dependências
pip install -r dependencies.txt
```

macOS / Linux (bash):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r dependencies.txt
```

**Inicializar / Reset do banco de dados**
> Atenção: o script `reset_db.py` remove o arquivo SQLite `banco_de_dados.db` (se existir) e recria as tabelas. Faça backup se necessário.

```powershell
python reset_db.py
```

**Executar servidor FastAPI (backend)**

```powershell
# Iniciar servidor de desenvolvimento
python -m uvicorn app.main:app --reload
```

O backend ficará disponível em `http://localhost:8000`.
A documentação automática do FastAPI está em `http://localhost:8000/docs`.

**Executar frontend (arquivos estáticos)**
O frontend é composto por arquivos estáticos em `frontend/`.
Você pode abrir `frontend/index.html` diretamente no navegador, mas é recomendado servir os arquivos por um HTTP server local para evitar problemas de CORS/paths.

```powershell
# A partir da raiz do projeto, serve a pasta frontend na porta 5500
python -m http.server 5500 --directory frontend
# Frontend disponível em http://localhost:5500
```

> Observação: o frontend usa `BASE_URL = "http://localhost:8000"` no JavaScript. Se o backend roda em outra porta/host, atualize esse valor nos arquivos JS (ex: `frontend/app.js`, `frontend/cargos.js`, etc.) ou use um servidor reverso.

**Testes manuais rápidos**
- Abrir `http://localhost:8000/docs` e testar endpoints CRUD.
- Criar departamentos/cargos/funcionários e registrar treinamentos.
- Testar exclusão de registros (o frontend tem modais de confirmação).

**Notas e recomendações**
- O projeto usa SQLite por padrão (`app/core/config.py`). Para produção, use PostgreSQL ou outro RDBMS.
- Para manter dados entre mudanças de schema, implemente migrations com Alembic.
- Considere centralizar `BASE_URL` do frontend em um arquivo de configuração para facilitar deploy.


