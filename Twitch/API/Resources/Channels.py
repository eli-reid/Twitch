from __imports import *
"""
Get Channel Information

request

curl -X GET 'https://api.twitch.tv/helix/channels?broadcaster_id=141981764' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz'


response
{
  "data": [
    {
      "broadcaster_id": "141981764",
      "broadcaster_login": "twitchdev",
      "broadcaster_name": "TwitchDev",
      "broadcaster_language": "en",
      "game_id": "509670",
      "game_name": "Science & Technology",
      "title": "TwitchDev Monthly Update // May 6, 2021",
      "delay": 0,
      "tags": ["DevsInTheKnow"]
    }
  ]
}

"""


class ChannelInformationRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.GET
    scope = None
    authorization = Utils.AuthRequired.CLIENT
    endPoint = "/channels"
    def __init__(self, broadcaster_ids: list[str], userAuth: bool=False) -> None:
        if userAuth:
            self.authorization = Utils.AuthRequired.USER
  
        self.broadcaster_ids: list[str] = broadcaster_ids
        super().__init__()
@dataclass
class ChannelInformationItem:
    broadcaster_id: str
    broadcaster_login: str
    broadcaster_name: str
    broadcaster_language: str
    game_name: str
    game_id: str
    title: str
    delay: int
    tags: list

class ChannelInformationResponse(Utils.ResponseBaseClass):
   def __init__(self) -> None:
       super().__init__(ChannelInformationItem) 

"""
Modify Channel Information

scope:  channel:manage:broadcast 

request
curl -X PATCH 'https://api.twitch.tv/helix/channels?broadcaster_id=41245072' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz' \
-H 'Content-Type: application/json' \
--data-raw '{"game_id":"33214", "title":"there are helicopters in the game? REASON TO PLAY FORTNITE found", "broadcaster_language":"en", "tags":["LevelingUp"]}'

response 
204 success
400 bad request data
401 Unauthorized
500 Internal server error

"""

class ModifyChannelInformationRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.PATCH
    scope = Scope.Channel.Manage.Broadcast
    authorization = Utils.AuthRequired.USER
    endPoint = "/channels"

    def __init__(self,
                 broadcaster_id: str,
                 game_id:Optional[str] =None,
                 broadcaster_language:Optional[str]=None,
                 title:Optional[str]=None,
                 delay:Optional[int]=None,
                 tags:Optional[list[str]]=None
                 ) -> None:
        self.broadcaster_id = broadcaster_id
        self.game_id = game_id
        self.broadcaster_language = broadcaster_language
        self.title = title
        self.delay = delay
        self.tags = tags
        super().__init__()
@dataclass
class ModifyChannelItem:
    status: Utils.HTTPMethod
class ModifyChannelInformationResponse(Utils.ResponseBaseClass):
    def __init__(self) -> None:
        super().__init__(ModifyChannelItem)


"""
Get Channel Editors

Scope: channel:read:editors

request:
curl -X GET 'https://api.twitch.tv/helix/channels/editors?broadcaster_id=141981764' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz' \

response:

{
  "data": [
    {
      "user_id": "182891647",
      "user_name": "mauerbac",
      "created_at": "2019-02-15T21:19:50.380833Z"
    },
    {
      "user_id": "135093069",
      "user_name": "BlueLava",
      "created_at": "2018-03-07T16:28:29.872937Z"
    }
  ]
}

"""
class ChannelEditorsRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.GET
    scope = Scope.Channel.Read.Editors
    authorization = Utils.AuthRequired.USER
    endPoint = "/channels/editors"

    def __init__(self, broadcaster_id: str) -> None:
        self.broadcaster_id = broadcaster_id
        super().__init__()

@dataclass
class ChannelEditorItem:
    user_id:str
    user_name: str
    created_at: str

class ChannelEditorsResponse(Utils.ResponseBaseClass):
    def __init__(self) -> None:
        super().__init__(ChannelEditorItem)

"""
Get Followed Channels - BETA

Scope: user:read:follows

request: Gets the list of broadcasters that the specified user follows.

curl -X GET 'https://api.twitch.tv/helix/channels/followed?user_id=123456' \
-H 'Authorization: Bearer kpvy3cjboyptmiacwr0c19hotn5s' \
-H 'Client-Id: hof5gwx0su6owfn0nyan9c87zr6t'

response
{
  "total": 8
  "data": [
    {
      "broadcaster_id": "11111",
      "broadcaster_login": "userloginname",
      "broadcaster_name": "UserDisplayName",
      "followed_at": "2022-05-24T22:22:08Z",
    },
    ...
  ],
  "pagination": {
    "cursor": "eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6NX19"
  }
}


request: Checks whether the specified user follows the specified broadcaster.

curl -X GET 'https://api.twitch.tv/helix/channels/followers?user_id=123456&broadcaster_id=654321' \
-H 'Authorization: Bearer kpvy3cjboyptmiacwr0c19hotn5s' \
-H 'Client-Id: hof5gwx0su6owfn0nyan9c87zr6t'

response:

{
  "total": 8
  "data": [
    {
      "broadcaster_id": "654321",
      "broadcaster_login": "basketweaver101",
      "broadcaster_name": "BasketWeaver101",
      "followed_at": "2022-05-24T22:22:08Z",
    }
  ],
  "pagination": {}
}

"""
class FollowedChannelsRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.GET
    scope = Scope.User.Read.Follows
    authorization = Utils.AuthRequired.USER
    endPoint ="channels/followed"
    def __init__(self, user_id: str, 
                 broadcaster_id: Optional[str]=None, 
                 first: Optional[int]=None, 
                 after:Optional[str]=None) -> None:
        
        self.user_id: str = user_id
        self.broadcaster_id: str = broadcaster_id
        self.first: int = first
        self.after: str = after
        super().__init__()

@dataclass
class FollowedChannelItem:
    broadcaster_id: str
    broadcaster_login: str
    broadcaster_name: str
    followed_at: str 

class FollowedChannelsResponse(Utils.PagenationMixin, Utils.ResponseBaseClass):
    total:int = 0
    def __init__(self) -> None:
        super().__init__(FollowedChannelItem)

   
"""
Get Channel Followers - BETA

scope: moderator:read:followers

requirements --
The ID in the broadcaster_id query parameter must match the user ID in the access token or the user must be a moderator for the specified broadcaster. If a scope is not provided, only the total follower account will be included in the response.

request: - Gets the list of users that follow the specified broadcaster.

curl -X GET 'https://api.twitch.tv/helix/channels/followers?broadcaster_id=123456' \
-H 'Authorization: Bearer kpvy3cjboyptmiacwr0c19hotn5s' \
-H 'Client-Id: hof5gwx0su6owfn0nyan9c87zr6t'

response:

{
  "total": 8
  "data": [
    {
      "user_id": "11111",
      "user_name": "UserDisplayName",
      "user_login": "userloginname",
      "followed_at": "2022-05-24T22:22:08Z",
    },
    ...
  ],
  "pagination": {
    "cursor": "eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6NX19"
  }
}

request: - Checks whether the specified user follows the specified broadcaster.

curl -X GET 'https://api.twitch.tv/helix/channels/followers?broadcaster_id=123456&user_id=654321' \
-H 'Authorization: Bearer kpvy3cjboyptmiacwr0c19hotn5s' \
-H 'Client-Id: hof5gwx0su6owfn0nyan9c87zr6t'

response: - The data field is an empty array, which means the user doesn't follow the specified broadcaster.

{
  "total": 8
  "data": [],
  "pagination": {}
}
"""

class ChannelFollowersRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.GET
    scope = Scope.Moderator.Read.Followers
    authorization = Utils.AuthRequired.USER
    endPoint = "/channels/followers"
    def __init__(self, broadcaster_id: str, 
                 user_id: Optional[str]=None, 
                 first: Optional[int]=None,  
                 after: Optional[str]=None) -> None:
        self.broadcaster_id: str = broadcaster_id
        self.user_id: str = user_id
        self.first: int = first
        self.after: str = after
        super().__init__()

@dataclass
class ChannelFollowerItem:
    followed_at: str    #UTC timestamp
    user_id: str        #ID that uniquely identifies the user that’s following the broadcaster.
    user_login: str     #user’s login name.
    user_name: str      #user’s display name.

class ChannelFollowersResponse(Utils.PagenationMixin,Utils.ResponseBaseClass):
    total: int = 0
    def __init__(self) -> None:
        super().__init__(ChannelFollowerItem)