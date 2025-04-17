from fastapi import FastAPI
from app.server.middlewares.request_logger import RequestLoggingMiddleware


def register_middlewares(app: FastAPI):
    app.add_middleware(RequestLoggingMiddleware)
