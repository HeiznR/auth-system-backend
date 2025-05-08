from sqlalchemy.orm import Mapped, mapped_column
from src.utils.models import Base


class StudentModel(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    name: Mapped[str]
    age: Mapped[int]
