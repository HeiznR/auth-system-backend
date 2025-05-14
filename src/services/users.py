from src.repositories.users import UsersRepository
from src.schemas.users import UsersSchema, UsersSchemaAdd, UsersSchemaUpdate
from fastapi import Depends, HTTPException
from src.utils.configs import pwdContext


class UsersService:
    def __init__(self, user_repo: UsersRepository = Depends()):
        self.user_repo: UsersRepository = user_repo

    async def add_user(self, user: UsersSchemaAdd) -> UsersSchema:
        is_user_exist = await self.get_user_by_email(user.email)
        if is_user_exist:
            raise HTTPException(status_code=409, detail="user already exist")
        hashed_password = pwdContext.hash(user.password)
        user.password = hashed_password
        user_dict = user.model_dump()
        user = await self.user_repo.create(user_dict)
        return user

    async def get_users(self) -> list[UsersSchema]:
        return await self.user_repo.read()

    async def get_user_by_email(self, email: str) -> UsersSchema:
        return await self.user_repo.read_by_email(email)

    async def get_user_by_id(self, id: str) -> UsersSchema:
        return await self.user_repo.read_by_id(id)

    async def delete_user(self, id: str):
        is_deleted = await self.user_repo.delete(id)
        if not is_deleted:
            raise HTTPException(status_code=404, detail="user is not found")
        return {"detail": "user deleted successfuly"}

    async def update_user(self, user_id: str, user: UsersSchemaUpdate) -> UsersSchema:
        is_user_exist = await self.get_user_by_id(user_id)
        if not is_user_exist:
            raise HTTPException(status_code=404, detail="user is not found")

        user_dict = user.model_dump(exclude_unset=True)
        user = await self.user_repo.update(user_id, user_dict)
        return user
