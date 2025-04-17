from fastapi import Request
from app.server.exceptions import ApiException


def require_auth(request: Request):
    token = request.headers.get("Authorization")
    if not token or "Bearer" not in token:
        raise ApiException(status_code=401, message="Missing or invalid token")

    # Here you'd decode the token, verify user
    user = {"id": "123", "role": "admin"}
    request.state.user = user
    return user
