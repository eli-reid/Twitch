import asyncio
from typing import Awaitable, Coroutine
import websockets
from websockets.client import WebSocketClientProtocol

class WebsocketClient:
    def __init__(self, address: str, port: int, consumer: Awaitable, producer: Awaitable, ssl: bool = True) -> None:
        self._connection: WebSocketClientProtocol = None
        self._consumer: Awaitable = consumer
        self._producer: Awaitable = producer
        self._address: str = address
        self._port: int = port
        self._url: str = f"{'wss' if ssl else 'ws'}://{self._address}:{self._port}"
    
    def run(self):
        loop = asyncio.new_event_loop()
        loop.create_task(self._connect())
        loop.run_forever()

    async def connect(self) -> Coroutine:
        return self._connect  
    
    async def _connect(self):
        async with websockets.connect(self._url) as self._connection:
            try:
                print ("connected")
                await asyncio.gather(
                    self._consumerHandler(),
                    self._producerHandler()
                    )
            except websockets.ConnectionClosed:
                print("CLOSED")
                await self._connect()

                

    async def _consumerHandler(self):
            async for message in self._connection:
                await self._consumer(message)
                await asyncio.sleep(0)
                
    
    async def _producerHandler(self):
        while True:
            message = await self._producer()
            if message is not None:
                await self._connection.send(message)
            await asyncio.sleep(0)    


