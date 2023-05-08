from Twitch.API.Resources.__imports import *

"""
Get Chatters
"""
class GetChattersRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.GET
        scope = Scope.Moderator.Read.Chatters
        authorization = Utils.AuthRequired.USER
        endPoint ="/chat/chatters"
        def __init__(self, broadcaster_id:str, moderator_id:str, first: Optional[int]= None, after: Optional[str]=None ) -> None:
              self.broadcaster_id = broadcaster_id
              self.moderator_id = moderator_id
              self.first = first
              self.after = after
              super().__init__()
    
class ChatterItem:
    user_id: str 
    user_login: str 
    user_name: str 
class GetChattersResponse(Utils.PagenationMixin, Utils.ResponseBaseClass):
    total: int
    def __init__(self) -> None:
        super().__init__(ChatterItem)

"""
Get Channel Emotes
"""
class GetChannelEmotesRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.GET
        scope = None
        authorization = Utils.AuthRequired.CLIENT
        endPoint ="/chat/emotes"
        def __init__(self, broadcaster_id: str, userAuth: bool=False ) -> None:
              if userAuth:
                    self.authorization = Utils.AuthRequired.USER
              super().__init__()

class Images:
    url_1x: str 
    url_2x: str 
    url_4x: str 

class ChannelEmoteItem:
    id: str 
    name: str 
    images: Images 
    tier: str 
    emote_type: str 
    emote_set_id: str 
    format: list[str] 
    scale: list[str] 
    theme_mode: list[str] 
    template: str 

class GetChannelEmotesResponse(Utils.ResponseBaseClass):
    def __init__(self) -> None:
        super().__init__(ChannelEmoteItem)

"""
Get Global Emotes
"""
class GetGlobalEmotesRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.GET
    scope = None
    authorization = Utils.AuthRequired.CLIENT
    endPoint ="/chat/emotes/global"
    def __init__(self, userAuth: bool=False) -> None:
        if userAuth:
            self.authorization = Utils.AuthRequired.USER
        super().__init__()
    
class GlobalEmoteItem:
    id: str 
    name: str 
    images: Images
    format: list[str] 
    scale: list[str] 
    theme_mode: list[str] 

class GetGlobalEmotesResponse(Utils.ResponseBaseClass):
    template: str
    def __init__(self) -> None:
        super().__init__(GlobalEmoteItem)

"""
Get Emote Sets
"""

class GetEmoteSetsRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.GET
    scope = None
    authorization = Utils.AuthRequired.CLIENT
    endPoint ="/chat/emotes/set"
    def __init__(self, emote_set_id: str, userAuth: bool=False ) -> None:
        if userAuth:
            self.authorization.USER
        self.emote_set_id = emote_set_id    
        super().__init__()

class EmoteSetItem:
    id: str 
    name: str 
    images: Images
    emote_type: str 
    emote_set_id: str 
    owner_id: str 
    format: list[str] 
    scale: list[str] 
    theme_mode: list[str] 

class GetEmoteSetsResponse(Utils.ResponseBaseClass):
        template: str
        def __init__(self) -> None:
            super().__init__(EmoteSetItem)

class GetChannelChatBadgesRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetChannelChatBadgesResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetGlobalChatBadgesRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetGlobalChatBadgesResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetChatSettingsRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetChatSettingsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UpdateChatSettingsRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class UpdateChatSettingsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class SendChatAnnouncementRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class SendChatAnnouncementResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class SendaShoutoutRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class SendaShoutoutResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetUserChatColorRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetUserChatColorResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UpdateUserChatColorRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class UpdateUserChatColorResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()