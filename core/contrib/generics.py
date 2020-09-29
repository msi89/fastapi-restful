
from tortoise.models import Model
from tortoise.contrib.pydantic import PydanticModel
from tortoise.contrib.pydantic import pydantic_model_creator
from typing import Dict


class BaseView():
    model: Model = None
    pydantic: PydanticModel = None

    def __init__(self):
        if(self.pydantic is None):
            self.pydantic = pydantic_model_creator(self.model)

    async def list(self):
        return await self.pydantic.from_queryset(self.model.all())

    async def find(self,  *args: None, **kwargs: None):
        return await self.pydantic.from_queryset_single(self.model.get(*args, **kwargs))

    async def get(self,  *args: None, **kwargs: None):
        return await self.pydantic.from_queryset(self.model.get(*args, **kwargs))

    async def store(self, schema: Dict):
        data = await self.model.create(schema)
        return self.pydantic.from_orm(data)

    async def update(self, id: int, schema: Model):
        await self.model.filter(id=id).update(**schema.dict(exclude_unset=True))
        return await self.pydantic.from_queryset_single(self.model.get(id=id))

    async def delete(self, id: int):
        return await self.model.filter(id=id).delete()
