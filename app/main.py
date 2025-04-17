from fastapi import FastAPI, APIRouter
from app.server.router_registry import register_routers
from app.server.middleware_registry import register_middlewares

app = FastAPI()

register_routers(app=app)
register_middlewares(app=app)
