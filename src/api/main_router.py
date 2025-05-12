from fastapi import APIRouter
from src.api.users import router as users_router
from src.api.database import router as db_router
from src.api.auth import router as auth_router

main_router = APIRouter()
main_router.include_router(users_router)
main_router.include_router(db_router)
main_router.include_router(auth_router)
