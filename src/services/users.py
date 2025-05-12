from src.repositories.users import UsersRepository
from src.schemas.users import UsersSchemaAdd, UsersSchemaUpdate
from fastapi import Depends, HTTPException
from passlib.context import CryptContext

pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UsersService:
    def __init__(self, user_repo: UsersRepository = Depends()):
        self.user_repo: UsersRepository = user_repo

    async def add_user(self, user: UsersSchemaAdd):
        is_user_exist = await self.user_repo.read_by_email(user.email)
        if is_user_exist:
            raise HTTPException(status_code=409, detail="user already exist")
        hashed_password = pwdContext.hash(user.password)
        user.password = hashed_password
        user_dict = user.model_dump()
        user = await self.user_repo.create(user_dict)
        return user

    async def read_users(self):
        users = await self.user_repo.read()
        return users

    async def read_user_by_id(self, id: str):
        user = await self.user_repo.read_by_id(id)
        return user

    async def delete_user(self, id: str):
        isDeleted = await self.user_repo.delete(id)
        return isDeleted

    async def update_user(self, user_id: str, user: UsersSchemaUpdate):
        is_user_exist = await self.user_repo.read_by_id(user_id)
        if not is_user_exist:
            raise HTTPException(status_code=404)

        user_dict = user.model_dump(exclude_unset=True)
        user = await self.user_repo.update(user_id, user_dict)
        return user
