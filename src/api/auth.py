from fastapi import APIRouter, Depends
from src.schemas.users import UsersSchemaAdd, UsersSchemaLogin
from src.services.auth import AuthService


router = APIRouter()


@router.post("/signup", tags=["Auth"], summary="sign up")
async def signup(user_data: UsersSchemaAdd, auth_service: AuthService = Depends()):
    result = await auth_service.signup(user_data)
    return result


@router.post("/login", tags=["Auth"], summary="log in")
async def login(credentials: UsersSchemaLogin, auth_service: AuthService = Depends()):
    result = await auth_service.login(credentials)
    return result
