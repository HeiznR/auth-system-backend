from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentSchema(BaseModel):
    id: str
    email: EmailStr
    name: str = Field(max_length=30)
    age: int = Field(ge=0, le=130)

    model_config = ConfigDict(extra="forbid")


class StudentSchemaAdd(BaseModel):
    email: EmailStr
    name: str = Field(max_length=30)
    age: int = Field(ge=0, le=130)
