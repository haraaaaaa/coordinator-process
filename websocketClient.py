import asyncio
import websockets
import json

async def hello(): # 웹 소켓에 접속
    uri = 'ws://192.168.56.22:8080'
    async with websockets.connect(uri) as websocket:
        req_items = json.dumps({'TC':'Coordinate','SC':'req','returned':True})
        await websocket.send(req_items)
        print(f"> Requested")

        res_items = await websocket.recv()
        print(f"< {res_items}")

asyncio.get_event_loop().run_until_complete(hello())