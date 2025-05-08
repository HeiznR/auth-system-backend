from src.schemas.students import StudentSchemaAdd
from src.utils.repository import AbstractRepository


class StudentsService:
    def __init__(self, student_repo: AbstractRepository):
        self.student_repo: AbstractRepository = student_repo

    async def add_student(self, student: StudentSchemaAdd):
        student_dict = student.model_dump()
        student_id = await self.student_repo.create(student_dict)
        return student_id

    async def read_students(self):
        students = await self.student_repo.read()
        return students
