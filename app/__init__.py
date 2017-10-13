"""
Docs:
AioHttp: http://aiohttp.readthedocs.io/en/stable/web.html
Cors: https://github.com/aio-libs/aiohttp-cors


"""

import asyncio

from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient

from app.lib.welcome import *

# Setting db
@asyncio.coroutine
def setup_db():
    db = AsyncIOMotorClient('mongodb://localhost:32768').py_async
    return db


loop = asyncio.get_event_loop()
db = loop.run_until_complete(setup_db())

app = web.Application()
app.router.add_get('/', handle)
app['db'] = db

web.run_app(app)
