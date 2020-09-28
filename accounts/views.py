from accounts.models import User
from tortoise.contrib.pydantic import pydantic_model_creator

userPydantic = pydantic_model_creator(User)


class AuthView():

    async def get(id: int = None):
        if(id is not None):
            return await userPydantic.from_queryset_single(User.get(id=id))
        return await userPydantic.from_queryset(User.all())
