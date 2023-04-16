from API.Resources import Utils
from API.Resources import Scope 

"""
Start Commercial

request:

curl -X POST 'https://api.twitch.tv/helix/channels/commercial' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz' \
-H 'Content-Type: application/json' \
--data-raw '{
  "broadcaster_id": "41245072",
  "length": 60
}'

response:

{
  "data": [
    {
      "length" : 60,
      "message" : "",
      "retry_after" : 480
    }
  ] 
}

"""

class StartCommercialRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.POST
    scope = Scope.Channel.Edit.Commercial
    authorization = Utils.AuthRequired.USER
    endPoint = "/channels/commercial"
    def __init__(self, broadcaster_id: str, length: int ) -> None:
        self.broadcaster_id: str = broadcaster_id
        self.length:int = length
        super().__init__()

class StartCommercialItem:
    length: int 
    message: str
    retry_after: int 

class StartCommercialRepsonse(Utils.ResponseBaseClass):
    def __init__(self) -> None:
        super().__init__(StartCommercialItem)
    