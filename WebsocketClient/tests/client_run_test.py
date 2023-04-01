import asyncio
import threading
import time
from typing import Optional
import unittest
import websockets
from ..WebsocketClient import WebsocketClient

LastMessageSent = ""
lastMessageRecieved = ""
messageQ = []

async def messageHandler(message):
         lastMessageRecieved=message

async def sendmessage():
        if len(messageQ)>0:
            LastMessageSent = messageQ.pop()
            return LastMessageSent
        
class WebSocketTestServer:
    def __init__(self) -> None:
        self.__url: str = 'localhost'
        self.__port: int = 8088
        self.loop = asyncio.new_event_loop()
            
    async def _server(self):
        async with websockets.serve(self.msg_handler, self.__url, self.__port):
            print("server started")
            await asyncio.Future()
            
    async def msg_handler(websock,message):
        await websock.send(message)

    def run(self, url:Optional[str]=None, port:Optional[int]=None):
        self.__url: str = url if url is not None else self.__url
        self.__port: int = port if port is not None else self.__port
        self.loop.create_task(self._server())
        self.loop.run_forever()
        
    def stop(self):
        if self.loop.is_running():
            self.loop.stop()

        
class websocketTestcase  (unittest.TestCase): 
    def setUp(self) -> None:

        print ("starting websocket echo test Server")
        self.wss = WebSocketTestServer()
        self.serverthread = threading.Thread(target=self.wss.run, name="WS_server", daemon=True).start()
        time.sleep(.01)

        print ("starting websocket Client")
        time.sleep(.01)
        self.websocketClient = WebsocketClient("127.0.0.1",8088, messageHandler, sendmessage,ssl=False)
        self.clientThread = threading.Thread(target=self.websocketClient.run, name="WS_client", daemon=True).start()   

        return super().setUp()
    
    def tearDown(self) -> None:
         self.wss.stop()
         self.websocketClient.stop()
         return super().tearDown()

class testWebsocketClient(websocketTestcase):
    def test_Send_Recieve(self):
        time.sleep(.01)
        print("running test")
        messageQ.append("message")
        self.assertEqual(LastMessageSent,  lastMessageRecieved)
            
        
    
