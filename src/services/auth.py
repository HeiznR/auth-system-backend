from src.schemas.users import UsersSchemaLogin, UsersSchemaAdd
from src.services.users import UsersService
from fastapi import Depends, HTTPException
from src.utils.jwt import TokenResponse, generate_jwt
from src.utils.configs import pwdContext


class AuthService:
    def __init__(self, users_service: UsersService = Depends()):
        self.users_service: UsersService = users_service

    async def signup(self, user_data: UsersSchemaAdd) -> TokenResponse:
        try:
            user = await self.users_service.add_user(user_data)
            return generate_jwt(user)
        except Exception as e:
            print(f"error {e}")

    async def login(self, credentials: UsersSchemaLogin) -> TokenResponse:
        user = await self.users_service.get_user_by_email(credentials.email)
        if not user:
            raise HTTPException(status_code=404, detail="wrong credentials")

        is_password_correct = pwdContext.verify(credentials.password, user.password)

        if not is_password_correct:
            raise HTTPException(status_code=401, detail="wrong credentials")

        return generate_jwt(user)
