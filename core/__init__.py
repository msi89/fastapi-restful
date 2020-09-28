
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from core import settings, router
import logging

app = FastAPI()


register_tortoise(
    app,
    config=settings.DATABASE,
    generate_schemas=True,
    add_exception_handlers=True
)

app.include_router(router.router)


@app.on_event('startup')
async def onstartup():
    logging.info('Tortoise-ORM started, %s, %s',
                 Tortoise._connections, Tortoise.apps)


@app.on_event('shutdown')
async def onshutdown():
    await Tortoise.close_connections()
    logging.info('Tortoise-ORM shutting down.')
