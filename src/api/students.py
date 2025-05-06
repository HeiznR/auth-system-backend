from src.schemas.students import StudentSchema
from fastapi import APIRouter, HTTPException


students = [
    {"id": "1", "email": "test@gmail.com", "name": "Vlad", "age": 26},
    {"id": "2", "email": "test2@gmail.com", "name": "Lora", "age": 24},
]

router = APIRouter()


@router.get("/students", tags=["students"], summary="get all students")
def get_all_students() -> list[StudentSchema]:
    return students


@router.get("/students/{id}", tags=["students"], summary="get student")
def get_student(id: str) -> StudentSchema:
    for student in students:
        if student["id"] == id:
            return student
    raise HTTPException(status_code=404, detail="student is not found")


@router.post("/students", tags=["students"], summary="create student")
def create_student(new_student: StudentSchema):
    students.append(new_student)
    return students
