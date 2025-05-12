from fastapi import APIRouter, Depends
from src.schemas.users import UsersSchemaAdd
from src.services.auth import AuthService


router = APIRouter()


@router.post("/signup", tags=["Auth"], summary="authenticate")
async def signup(user_data: UsersSchemaAdd, auth_service: AuthService = Depends()):
    result = await auth_service.signup(user_data)
    return result
