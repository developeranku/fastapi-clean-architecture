from fastapi import APIRouter, Depends
from app.shared.dependencies.auth import require_auth
from app.shared.repositories.auth import AuthRepository
from app.domains.auth.service import AuthService
from app.server.response_handler import success_response

auth_router = APIRouter(
    prefix="/auth"
)


def get_auth_service():
    return AuthService(AuthRepository())


@auth_router.get('/session', dependencies=[Depends(require_auth)])
def session(auth_service: AuthService = Depends(get_auth_service)):
    result = auth_service.validate_usr()
    return success_response(
        data=result
    )
