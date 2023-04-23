from __imports import * 

class GetAllStreamTagsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetAllStreamTagsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetStreamTagsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetStreamTagsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()