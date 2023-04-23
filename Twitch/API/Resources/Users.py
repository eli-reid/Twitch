from __imports import *

class GetUsersRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetUsersResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UpdateUserRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class UpdateUserResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetUsersFollowsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetUsersFollowsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetUserBlockListRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetUserBlockListResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class BlockUserRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class BlockUserResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UnblockUserRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class UnblockUserResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetUserExtensionsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetUserExtensionsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetUserActiveExtensionsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetUserActiveExtensionsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UpdateUserExtensionsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class UpdateUserExtensionsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

