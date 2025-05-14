from fastapi import APIRouter, Depends, HTTPException
from src.schemas.users import UsersSchema, UsersSchemaAdd, UsersSchemaUpdate
from src.services.users import UsersService


router = APIRouter()


@router.post("/users", tags=["users"], summary="create user")
async def create_user(
    new_user: UsersSchemaAdd, users_service: UsersService = Depends()
):
    return await users_service.add_user(new_user)


@router.get("/users", tags=["users"], summary="get all users")
async def get_all_users(users_service: UsersService = Depends()) -> list[UsersSchema]:
    try:
        return await users_service.get_users()

    except Exception as e:
        print(f"An error occurred: {e}")


@router.get("/users/{user_id}", tags=["users"], summary="get user by id")
async def get_user_by_id(
    user_id: str, users_service: UsersService = Depends()
) -> UsersSchema:
    try:
        return await users_service.get_user_by_id(user_id)

    except Exception as e:
        print(f"An error occurred: {e}")


@router.put("/users/{user_id}", tags=["users"], summary="update user")
async def update_user(
    user_id: str, user_data: UsersSchemaUpdate, users_service: UsersService = Depends()
) -> UsersSchema:
    return await users_service.update_user(user_id, user_data)


@router.delete("/users/{user_id}", tags=["users"], summary="delete user by id")
async def delete_user(user_id: str, users_service: UsersService = Depends()):
    try:
        isUserDeleted = await users_service.delete_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

    if not isUserDeleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {"detail": "User deleted successfully"}
