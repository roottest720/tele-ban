from aiohttp import web

async def handle(request):
    param1 = request.match_info.get('param1', 'default_value1')
    with open('skibidi_0303.txt', 'a') as file:
        # Write data to the file
        file.write(str(param1) + "\n");

    return web.Response(text=f"404 requested web page not found!")

app = web.Application()
app.router.add_get('/{param1}', handle)  # Add a route with two parameters

if __name__ == '__main__':
    web.run_app(app)
