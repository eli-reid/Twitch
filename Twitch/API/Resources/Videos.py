from __imports import *

class GetVideosRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetVideosResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class DeleteVideosRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class DeleteVideosResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()
