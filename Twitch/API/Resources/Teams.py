from __imports import *

class GetChannelTeamsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetChannelTeamsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetTeamsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetTeamsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()