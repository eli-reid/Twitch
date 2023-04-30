
import Twitch
import webbrowser
from Twitch.secretkeys import apikeys
def message(sender, msg:Twitch.MessageType):
    print (msg)
def connected(sender,msg):
    print("connected")
def join(sender, msg):
    print(f"JOIN: {msg}")
def main():
    
    scopes = [Twitch.Scope.Analytics.Read.Extensions, 
              Twitch.Scope.User.Manage.Whispers, 
              Twitch.Scope.Channel.Manage.Moderators]
    at = Twitch.Oauth(apikeys.CLIENT_ID, apikeys.CLIENT_SECRET,scopes,"http://localhost:8000/twitch/oauth/code")
    webbrowser.open_new(at.getCodeURL(""))
    
    settings={
        "server": "irc.chat.twitch.tv",
        "port": 6697,
        "ssl": True,
        "user": "edog0049aBot",
        "password":f"oauth:{apikeys.BOT_OAUTH}",
        "channels": ["edog0049a"],
        "caprequest" :"twitch.tv/tags twitch.tv/commands twitch.tv/membership" 
        }
    
    chat = Twitch.Chat(settings)
    chat.onReceived(message)
    chat.onConnected(connected)
    chat.onJoin(join)
    chat.run()
    chat.connect()
    d =""
    while d != "q":
        d = input(":")
        if(d =="m"):
           msg = input("msg:")
           chat.sendMessage("edog0049a",msg)
        if(d == "j"):
           j=input("room:")
           chat.join([j])

if __name__=='__main__':
    main()