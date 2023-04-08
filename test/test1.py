import Twitch
import unittest
def message(sender, msg):
    print (msg)
class chat_con(unittest.TestCase):
    def setUp(self) -> None:
        
        settings={
        "server": "irc.chat.twitch.tv",
        "port": 6697,
        "user": "edog0049a",
        "password":"oauth:uqyosuh6zf54is2me2jl5l8qgahtlz",
        "channels": ["alilfoxz","edog0049a"],
        "caprequest" :"twitch.tv/tags twitch.tv/commands twitch.tv/membership" 
        }
        self.chat = Twitch.Chat(settings)
        self.chat.onConnected(message)
        
        self.chat.run()

        return super().setUp()
    
    def test(self):
        self.chat.connect()