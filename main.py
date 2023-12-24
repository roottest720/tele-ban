import aiohttp
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = f"Hello, {name}!"
    return web.Response(text=text)

app = web.Application()
app.router.add_get('/{name}', handle)

if __name__ == '__main__':
    web.run_app(app)