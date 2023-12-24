from aiohttp import web

async def handle(request):
    param1 = request.match_info.get('param1', 'default_value1')
    param2 = request.match_info.get('param2', 'default_value2')

    return web.Response(text=f"Param1: {param1}, Param2: {param2}")

app = web.Application()
app.router.add_get('/{param1}/{param2}', handle)  # Add a route with two parameters

if __name__ == '__main__':
    web.run_app(app)
