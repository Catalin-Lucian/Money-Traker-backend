import services.user_service as user_service
from fastapi import APIRouter, Depends

users = APIRouter()


# add a user
@users.post("/api/auth/register", status_code=201)
async def add_user(res: dict = Depends(user_service.register_user)):
    return res


# login a user
@users.post("/api/auth/login", status_code=200)
async def login_user(res: dict = Depends(user_service.login_user)):
    return res
