from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional


class UsersSchema(BaseModel):
    id: str
    email: EmailStr
    name: str = Field(max_length=30)
    age: int = Field(ge=0, le=130)

    model_config = ConfigDict(extra="forbid")


class UsersSchemaAdd(BaseModel):
    email: EmailStr
    name: str = Field(max_length=30)
    age: int = Field(ge=0, le=130)


class UsersSchemaUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    age: Optional[int] = None
