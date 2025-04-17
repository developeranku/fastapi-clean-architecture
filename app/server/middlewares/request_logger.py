import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from app.infrastructure.logger import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(request.headers)
        start_time = time.time()

        response: Response = await call_next(request)

        duration = (time.time() - start_time) * 1000
        method = request.method
        path = request.url.path
        status_code = response.status_code
        client_ip = request.client.host
        user_agent = request.headers.get("user-agent", "-")

        logger.info(
            f"{method} {path} - {status_code} - {duration:.2f}ms - {client_ip} - {user_agent}"
        )
        return response
