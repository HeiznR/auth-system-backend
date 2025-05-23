from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional


class UsersSchemaLogin(BaseModel):
    email: EmailStr
    password: str


class UsersSchemaAdd(UsersSchemaLogin):
    name: str = Field(max_length=30)
    age: int = Field(ge=0, le=130)


class UsersSchema(UsersSchemaAdd):
    id: str

    model_config = ConfigDict(extra="forbid")


class UsersSchemaUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    age: Optional[int] = None
