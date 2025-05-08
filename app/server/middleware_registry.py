from fastapi import FastAPI
from app.server.middlewares.request_logger import RequestLoggingMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import ALLOWED_ORIGINS
from app.server.response_handler import api_exception_handler, unhandled_exception_handler
from app.server.exceptions import ApiException


def register_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(RequestLoggingMiddleware)
    app.add_exception_handler(ApiException, api_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)
