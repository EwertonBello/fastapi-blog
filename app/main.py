from fastapi import FastAPI
from app.database import engine, Base

from app.users.routers import authentication as users_authentication
from app.users.routers import user as users_router
from app.blogs.routers import blog as blogs_router
from app.config import get_settings


app = FastAPI(title=get_settings().app_name)

Base.metadata.create_all(engine)

app.include_router(users_authentication.router)
app.include_router(users_router.router)
app.include_router(blogs_router.router)
