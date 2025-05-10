from sqlalchemy.orm import Mapped, mapped_column
from src.utils.models import Base
import uuid


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    email: Mapped[str]
    name: Mapped[str]
    age: Mapped[int]
