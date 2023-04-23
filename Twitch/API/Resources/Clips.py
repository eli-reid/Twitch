from __imports import *
class CreateClipRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class CreateClipResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetClipsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetClipsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()
