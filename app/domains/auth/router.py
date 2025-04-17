from fastapi import APIRouter, Depends
from app.shared.dependencies.auth import require_auth

auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.get('/session', dependencies=[Depends(require_auth)])
def controller():
    return {
        "token": "API_TOKEN"
    }
