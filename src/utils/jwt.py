import jwt
from src.schemas.users import UsersSchema
from src.utils.configs import Settings

settings = Settings()


class TokenResponse:
    access_token: str


def generate_jwt(user: UsersSchema) -> TokenResponse:
    payload = {"sub": user.id, "name": user.name}
    jwt_token = jwt.encode(
        payload=payload, key=settings.JWT_SECRET_KEY, algorithm="HS256"
    )
    return {"access_token": jwt_token}
