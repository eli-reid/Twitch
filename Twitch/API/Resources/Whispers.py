from __imports import *

class SendWhisperRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class SendWhisperResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()