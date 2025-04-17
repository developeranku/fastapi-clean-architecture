from http import HTTPStatus


class ApiException(Exception):
    def __init__(self, message: str, status_code: int = 400, type=HTTPStatus.INTERNAL_SERVER_ERROR.phrase):
        self.message = message
        self.status_code = status_code
        self.type = type
