from src.schemas.users import UsersSchemaAdd
from src.services.users import UsersService
from src.utils.config import Settings
from fastapi import Depends

import jwt

settings = Settings()


class AuthService:
    def __init__(self, users_service: UsersService = Depends()):
        self.users_service: UsersService = users_service

    async def signup(self, user_data: UsersSchemaAdd):
        try:
            user = await self.users_service.add_user(user_data)
            payload = {"sub": user.name, "name": user.name}
            jwt_token = jwt.encode(
                payload=payload, key=settings.JWT_SECRET_KEY, algorithm="HS256"
            )
            return {"access_token": jwt_token}
        except Exception as e:
            print(f"error {e}")
