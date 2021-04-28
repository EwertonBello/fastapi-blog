# Blog FastAPI

API with Authentication using FastAPI  

FastAPI: (https://fastapi.tiangolo.com/)  
SQLAlchemy: (https://www.sqlalchemy.org/)  
pydantic: (https://pydantic-docs.helpmanual.io/)  

# Running

## Create .env

```bash
cp .env-example .env

# generate secret_key
openssl rand -hex 32
```

## Run docker with database

```bash
docker-compose build
docker-compose up
```

# Endpoints

![Endpoints](./docs.png)
