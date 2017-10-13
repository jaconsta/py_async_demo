import asyncio

from aiohttp import web


@asyncio.coroutine
def handle(request):
    db = request.app['db']

    yield from db.pages.insert_one({'body': 'hello This is me'})
    return web.Response(text='helllo')
