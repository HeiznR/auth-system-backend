from src.utils.repository import SQLAlchemyRepository
from src.schemas.users import UsersSchema, UsersSchemaAdd, UsersSchemaUpdate
from fastapi import HTTPException


class UsersService:
    def __init__(self, user_repo: SQLAlchemyRepository):
        self.user_repo: SQLAlchemyRepository = user_repo

    async def add_user(self, user: UsersSchemaAdd):
        user_dict = user.model_dump()
        user_id = await self.user_repo.create(user_dict)
        return user_id

    async def read_users(self):
        users = await self.user_repo.read()
        return users

    async def read_user_by_id(self, id: str):
        user = await self.user_repo.read_one(id)
        return user

    async def delete_user(self, id: str):
        isDeleted = await self.user_repo.delete(id)
        return isDeleted

    async def update_user(self, user_id: str, user: UsersSchemaUpdate):
        is_user_exist = await self.user_repo.read_one(user_id)
        if not is_user_exist:
            raise HTTPException(status_code=404)

        user_dict = user.model_dump(exclude_unset=True)
        user = await self.user_repo.update(user_id, user_dict)
        return user
