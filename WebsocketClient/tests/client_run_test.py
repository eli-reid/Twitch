import asyncio
import time
import unittest
from WebsocketClient import WebsocketClient
messageQ = []
async def messageHandler(message):
    print(message)

async def sendmessage():
    if len(messageQ)>0:
        return messageQ.pop()
  
socket = WebsocketClient("127.0.0.1",8080,consumer=messageHandler,producer=sendmessage,ssl=False)
messageQ.append("hello")
messageQ.append("hello")
messageQ.append("hello")
messageQ.append("hello")

socket.run()
print("UUUU")