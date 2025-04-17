from app.shared.repositories.auth import AuthRepository


class AuthService:
    def __init__(self, auth_repo: AuthRepository):
        self.auth_repo = auth_repo

    def validate_usr(self):
        return self.auth_repo.usr_exist()
