"""
Docs:
AioHttp: http://aiohttp.readthedocs.io/en/stable/web.html
Cors: https://github.com/aio-libs/aiohttp-cors

Mongo DB:
http://motor.readthedocs.io/en/stable/tutorial-asyncio.html

Schemas:
https://webargs.readthedocs.io/en/latest/framework_support.html#aiohttp
"""

import asyncio

from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient

from app.lib.welcome import *

# Setting db
@asyncio.coroutine
def setup_db():
    db = AsyncIOMotorClient('mongodb://localhost:26099').py_async
    return db


loop = asyncio.get_event_loop()
db = loop.run_until_complete(setup_db())

app = web.Application()
app.router.add_get('/', handle)
app['db'] = db

web.run_app(app)

if __name__ == '__main__':
    pass
