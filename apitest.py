from Twitch.secretkeys import apikeys
import Twitch
import asyncio

async def main() -> None:
    USER_CREDS: Twitch.Credentials = Twitch.Credentials(None,None,None)
    CLIENT_CREDS: Twitch.Credentials = Twitch.Credentials(apikeys.CLIENT_ID,apikeys.CLIENT_TOKEN,[])
    apicaller = Twitch.Api(CLIENT_CREDS,USER_CREDS)
    resp: Twitch.Types.GetUsersResponse = await apicaller.GetUsers(login=['alilfoxz', 'edog0049a'])
    for item in resp.data:
        print(f"{item.id} | {item.display_name}")
        print(item.__dict__.items())
        
    
        rsp = await apicaller.GetCheermotes(item.id)
        for item in rsp.data:
            print(item.__dict__.items())
    await apicaller.APIconnector.close()

asyncio.run(main())
