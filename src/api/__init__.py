from fastapi import APIRouter
from src.api.students import router as students_router

main_router = APIRouter()
main_router.include_router(students_router)
