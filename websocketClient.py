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




>>>
 {"JSON": "[{\"baseDate\": \"20220422\", \"baseTime\": \"0700\", \"category\": \"PTY\", \"nx\": 59, \"ny\": 126, \"obsrValue\": \"0\"}, 
  {\"baseDate\": \"20220422\", \"baseTime\": \"0700\", \"category\": \"REH\", \"nx\": 59, \"ny\": 126, \"obsrValue\": \"64\"}, 
  {\"baseDate\": \"20220422\", \"baseTime\": \"0700\", \"category\": \"RN1\", \"nx\": 59, \"ny\": 126, \"obsrValue\": \"0\"}, 
 {\"baseDate\": \"20220422\", \"baseTime\": \"0700\", \"category\": \"T1H\", \"nx\": 59, \"ny\": 126, \"obsrValue\": \"15.9\"}, 
  {\"baseDate\": \"20220422\", \"baseTime\": \"0700\", \"category\": \"UUU\", \"nx\": 59, \"ny\": 126, \"obsrValue\": \"2.4\"},
   {\"baseDate\": \"20220422\", \"baseTime\": \"0700\", \"category\": \"VEC\", \"nx\": 59, \"ny\": 126, \"obsrValue\": \"221\"}, 
    {\"baseDate\": \"20220422\", \"baseTime\": \"0700\", \"category\": \"VVV\", \"nx\": 59, \"ny\": 126, \"obsrValue\": \"2.7\"}, 
     {\"baseDate\": \"20220422\", \"baseTime\": \"0700\", \"category\": \"WSD\", \"nx\": 59, \"ny\": 126, \"obsrValue\": \"3.6\"}]", "TC": "Coordinate", "SC": "res"}
