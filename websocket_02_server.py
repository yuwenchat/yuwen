import asyncio
import websockets


async def hello(websocket, path):
    name = await websocket.recv()
    if name == "hello server!":
        await websocket.send("hello client!")

start_server = websockets.serve(hello, "0.0.0.0", 39444)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()