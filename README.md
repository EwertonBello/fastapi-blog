# Blog FastAPI

API with Authentication using FastAPI  

FastAPI: (https://fastapi.tiangolo.com/)  
SQLAlchemy: (https://www.sqlalchemy.org/)  
pydantic: (https://pydantic-docs.helpmanual.io/)  

# Running

## Install packages

```bash
pip install -r requirements.txt
```

## Create .env

```bash
cp .env-example .env

# generate secret_key
openssl rand -hex 32
```

## Execute Uvicorn

```bash
uvicorn app.main:app --reload
```

# Endpoints

![Endpoints](./docs.png)
