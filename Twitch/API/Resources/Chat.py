from __imports import *
class GetChattersRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetChattersResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetChannelEmotesRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetChannelEmotesResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetGlobalEmotesRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetGlobalEmotesResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetEmoteSetsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetEmoteSetsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetChannelChatBadgesRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetChannelChatBadgesResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetGlobalChatBadgesRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetGlobalChatBadgesResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetChatSettingsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetChatSettingsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UpdateChatSettingsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class UpdateChatSettingsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class SendChatAnnouncementRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class SendChatAnnouncementResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class SendaShoutoutRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class SendaShoutoutResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetUserChatColorRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetUserChatColorResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UpdateUserChatColorRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class UpdateUserChatColorResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()