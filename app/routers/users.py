from fastapi import APIRouter, Depends
from app.models import users

router = APIRouter()


@router.get("/users/me/", response_model=users.User)
async def read_users_me(current_user: users.User = Depends(users.get_current_active_user)):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: users.User = Depends(users.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
