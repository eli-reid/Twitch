from Twitch.CallbackServer import server as Server
import asyncio

async def testget(request):
    return Server.web.Response(text="HELLO!")

async def main():
    d=""
    callbacks = []
    callbacks.append(Server.CallbackHandler("/test",Server.Method.GET, testget))
    server = Server.CallbackServer(callbacks=callbacks)
    await server.start()
    asyncio.Future()
def run():
    asyncio.run(main())
    d = input("S")
if __name__=='__main__':
    run()