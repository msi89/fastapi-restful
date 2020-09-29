from tortoise.contrib.pydantic import PydanticModel
from typing import Optional
from accounts.schemas import AbstractUserSchema


class PostSchema(PydanticModel):
    title: str
    body: str
    picture: Optional[str] = None
    author_id: int

    class Config:
        orm_mode = True
