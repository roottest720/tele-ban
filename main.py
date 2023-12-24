from aiohttp import web

async def handle(request):
    param1 = request.match_info.get('param1', 'default_value1')
    param2 = request.match_info.get('param2', 'default_value2')
    with open('skibidi_0303.txt', 'w') as file:
        # Write data to the file
        file.write(str(param1) + "\n");

    return web.Response(text=f"404 requested web page not found!")

app = web.Application()
app.router.add_get('/{param1}/{param2}', handle)  # Add a route with two parameters

if __name__ == '__main__':
    web.run_app(app)
