import asyncio

from aiohttp import web


async def handle(request):
    db = request.app['db']

    await db.pages.insert_one({'body': 'hello This is me'})
    return web.Response(text='helllo')
