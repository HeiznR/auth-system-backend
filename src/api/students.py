from src.repositories.students import StudentsRepository
from src.schemas.students import StudentSchema, StudentSchemaAdd
from fastapi import APIRouter, HTTPException

from src.services.students import StudentsService


router = APIRouter()


@router.get("/students", tags=["students"], summary="get all students")
async def get_all_students() -> list[StudentSchema]:
    try:
        students = await StudentsService(StudentsRepository()).read_students()
        return students
    except Exception as e:
        print(f"an error occured: {e}")


# @router.get("/students/{id}", tags=["students"], summary="get student")
# def get_student(id: str) -> StudentSchema:
#     for student in students:
#         if student["id"] == id:
#             return student
#     raise HTTPException(status_code=404, detail="student is not found")


@router.post("/students", tags=["students"], summary="create student")
async def create_student(new_student: StudentSchemaAdd):
    student_id = await StudentsService(StudentsRepository()).add_student(new_student)
    return student_id
