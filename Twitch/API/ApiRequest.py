from typing import Optional,Callable
import asyncio
import aiohttp
import json
from aiohttp import ClientResponse, web

from CallbackServer import CallbackServer

class APIRequest():
    def __init__(self, apiURL:str, returnURL:Optional[str]=None, returnPort: Optional[int]=None) -> None:
        self._httpClientSession = aiohttp.ClientSession()
        self._apiURL = apiURL
        self._returnURL = returnURL if returnURL else "http://localhost" 
        self._returnPort = returnPort if returnPort else 8880

    async def getRequest(self, endPoint:str, headers:Optional[dict[str,str]]=None, callbacks:dict[str,Callable]=None, **kwargs) -> ClientResponse:
        """
        getRequest
            * endPoint -> str: location  of api call 
            * headers -> dict[str, str]: for any haeaders reqiured by api 
            * callbacks -> dict[Method, function] 
                * method: str  "GET", "POST", ...
                * funcion: async callback(request) - request accepts a aiohttp.web.Request
        """
        if callbacks is not None:
            callbackServer = CallbackServer("/callback", callbacks, self._returnURL, self._returnPort)
            await callbackServer.start()
        response = await self._httpClientSession.get(f"{self._apiURL + endPoint}",headers=headers)
        await self._httpClientSession.close()
        return response

    async def postRequest(self, endPoint:str, headers:Optional[dict]=None, callbacks:dict[str,Callable]=None, **kwargs) -> ClientResponse:
        """
        postRequest
            * endPoint -> str: location  of api call 
            * headers -> dict[str, str]: for any haeaders reqiured by api 
            * callbacks -> dict[Method, function] 
                * method: str  "GET", "POST", ...
                * funcion: async callback(request) - request accepts a aiohttp.web.Request
        """
        if len(callbacks.keys()):
            callbackServer = CallbackServer("/callback", callbacks, self._returnURL, self._returnPort)
            await callbackServer.start()
        response = await self._httpClientSession.post(url=self._apiURL + endPoint, headers=headers, kwargs=kwargs)
        await self._httpClientSession.close()
        return response

    async def patchRequest(self, endPoint:str, headers:Optional[dict[str,str]]=None, callbacks:dict[str,Callable]=None, **kwargs) -> ClientResponse:
        """
        getRequest
            * endPoint -> str: location  of api call 
            * headers -> dict[str, str]: for any haeaders reqiured by api 
            * callbacks -> dict[Method, function] 
                * method: str  "GET", "POST", ...
                * funcion: async callback(request) - request accepts a aiohttp.web.Request
        """
        if len(callbacks.keys()):
            callbackServer = CallbackServer("/callback", callbacks, self._returnURL, self._returnPort)
            await callbackServer.start()
        response = await self._httpClientSession.patch(url=self._apiURL + endPoint, headers=headers, kwargs=kwargs)
        await self._httpClientSession.close()
        return response 

    async def deleteRequest(self, endPoint:str, headers:Optional[dict[str,str]]=None, callbacks:dict[str,Callable]=None, **kwargs) -> ClientResponse:
        """
        getRequest
            * endPoint -> str: location  of api call 
            * headers -> dict[str, str]: for any haeaders reqiured by api 
            * callbacks -> dict[Method, function] 
                * method: str  "GET", "POST", ...
                * funcion: async callback(request) - request accepts a aiohttp.web.Request
        """
        if len(callbacks.keys()):
            callbackServer = CallbackServer("/callback", callbacks, self._returnURL, self._returnPort)
            await callbackServer.start()
        response = await self._httpClientSession.delete(url=self._apiURL + endPoint, headers=headers, kwargs=kwargs)
        await self._httpClientSession.close()
        return response 

    async def putRequest(self, endPoint:str, headers:Optional[dict[str,str]]=None, callbacks:dict[str,Callable]=None, **kwargs) -> ClientResponse:
        """
        getRequest
            * endPoint -> str: location  of api call 
            * headers -> dict[str, str]: for any haeaders reqiured by api 
            * callbacks -> dict[Method, function] 
                * method: str  "GET", "POST", ...
                * funcion: async callback(request) - request accepts a aiohttp.web.Request
        """
        if len(callbacks.keys()):
            callbackServer = CallbackServer("/callback", callbacks, self._returnURL, self._returnPort)
            await callbackServer.start()
        response = await self._httpClientSession.put(url=self._apiURL + endPoint, headers=headers, kwargs=kwargs)
        
        self._httpClientSession.close()
        return response       

    async def close(self):
        await self._httpClientSession.close();
