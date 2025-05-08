from src.models.students import StudentModel
from src.utils.repository import SQLAlchemyRepository


class StudentsRepository(SQLAlchemyRepository):
    model = StudentModel
