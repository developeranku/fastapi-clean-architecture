from fastapi import FastAPI, APIRouter
from app.domains.auth.router import auth_router


def register_routers(app: FastAPI):
    root_router = APIRouter(
        prefix="/api/v1"
    )
    root_router.include_router(router=auth_router)
    app.include_router(root_router)
