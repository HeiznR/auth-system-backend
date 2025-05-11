from fastapi import APIRouter, HTTPException, Request
from src.repositories.users import UsersRepository
from src.schemas.users import UsersSchema, UsersSchemaAdd
from src.services.users import UsersService


router = APIRouter()


@router.get("/users", tags=["users"], summary="get all users")
async def get_all_users() -> list[UsersSchema]:
    try:
        users = await UsersService(UsersRepository()).read_users()
        return users
    except Exception as e:
        print(f"an error occured: {e}")


@router.get("/users/{user_id}", tags=["users"], summary="get user by id")
async def get_user_by_id(user_id: str) -> UsersSchema:
    try:
        user = await UsersService(UsersRepository()).read_user_by_id(user_id)
        return user
    except Exception as e:
        print(f"an error occured: {e}")


@router.post("/users", tags=["users"], summary="create user")
async def create_user(new_user: UsersSchemaAdd):
    user_id = await UsersService(UsersRepository()).add_user(new_user)
    return user_id


@router.delete("/users/{user_id}", tags=["users"], summary="delete user by id")
async def delete_user(user_id: str):
    try:
        isUserDeleted = await UsersService(UsersRepository()).delete_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

    if not isUserDeleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {"detail": "User deleted successfully"}


# @router.put("/users/{user_id}", tags=["users"], summary="update user")
# async def update_user(user_id: str, request: Request):
#     user_data = await request.json()
#     print(f"Received body: {user_data}")
#     user_id = await UsersService(UsersRepository()).update_user(user_id, user_data)
#     return user_id
