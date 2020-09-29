from typing import Optional
from tortoise.contrib.pydantic import PydanticModel


class AbstractUserSchema(PydanticModel):
    id: int


class UserSchema(PydanticModel):
    name: Optional[str] = None
    username: str
    email: str
    password: str
    avatar: Optional[str] = None
    is_active: Optional[bool] = False
    is_admin: Optional[bool] = False
    is_superuser: Optional[bool] = False
    is_staff: Optional[bool] = False

    class Config:
        orm_mode = True
