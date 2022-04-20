import asyncio
import websockets


async def accept(websocket, path):
    data = await websocket.recv();
    print(data);

start_server = websockets.serve(accept, "localhost", 9998);

asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();

