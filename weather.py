import asyncio
import websockets

async def connect():
    async with websockets.connect("ws://localhost:9998/websocket") as websocket:
        await websocket.send("GET");
        print("GET Request Completed");
        JSON = await websocket.recv();
        print(JSON)

# 비동기로 서버에 접속한다.
loop = asyncio.get_event_loop()
loop.run_until_complete(connect())
loop.close()


