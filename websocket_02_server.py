import asyncio
import websockets


async def hello(websocket, path):
    name = await websocket.recv()
    if name == "hello server!":
        await websocket.send("hello client!")
    else:
        content = name.split("\n")
        if content[0] == "login":
            user = content[1]
            pwd = content[2]
            await  websocket.send(f"user's name is:{user}\npassword is:{pwd}")

start_server = websockets.serve(hello, "0.0.0.0", 39444)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()