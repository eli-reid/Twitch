import asyncio
import json
from aiohttp import  web
from typing import Callable, Optional

class CallbackServer():
    def __init__(self, path:str, callbacks:dict[str, Callable], host:Optional[str]=None, port:Optional[int]=None) -> None:
        """
        callbacks dict[method as string, callback function]
        """
        self._webserver:web.Application = web.Application()
        self._routes: list = []
        self._host: str = host if host else "localhost"
        self._port: int = port if port else 8880
        self._run: bool = True
        self._runner = web.AppRunner(self._webserver)
        self._server: web.TCPSite
        for method, handler in callbacks:
            self._webserver.router.add_route(method=method.upper(), path=path, handler=handler)

    async def start(self) -> None:
        await self._runner.setup()
        self._server = web.TCPSite(runner=self._runner, host=self._host, port=self._port)
        await self._server.start()
        while self._run:
            await asyncio.sleep(120) 
   
    async def stop(self):
        await self._server.stop()
        self._run = False