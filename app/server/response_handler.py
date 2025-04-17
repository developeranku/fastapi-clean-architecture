from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.infrastructure.logger import logger
from app.server.exceptions import ApiException
from typing import Optional, Any

"""
Standard API response structure (used across success and error responses):

Error Example:
{
  "success": false,
  "error": {
    "message": "Invalid token",
    "status_code": 401,
    "type": "UNAUTHORIZED"
  }
}

Success responses follow a similar structure with:
{
  "success": true,
  "data": {...},
  "message": "Optional success message"
}
"""


def success_response(data: Any = {}, message: Optional[str] = "Request resolved") -> dict:
    return {
        "success": True,
        "data": data,
        "message": message
    }


async def api_exception_handler(request: Request, exc: ApiException):

    logger.warning(f"[ApiException] {exc.status_code} - {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "message": exc.message,
                "status_code": exc.status_code,
                "type": exc.type
            }
        }
    )
