from fastapi import APIRouter, HTTPException
from accounts.views import AuthView
from accounts.schemas import UserSchema

router = APIRouter()

auth = AuthView()


@router.get("/users")
async def get_users():
    return await auth.list()


@router.post("/register")
async def create_user(user: UserSchema):
    return await auth.store(user)
