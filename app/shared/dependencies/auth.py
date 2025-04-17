from fastapi import Request, HTTPException, Depends


def require_auth(request: Request):
    token = request.headers.get("Authorization")
    if not token or "Bearer" not in token:
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    # Here you'd decode the token, verify user
    user = {"id": "123", "role": "admin"}
    request.state.user = user
    return user
