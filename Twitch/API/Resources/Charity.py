from __imports import *
class GetCharityCampaignRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetCharityCampaignResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetCharityCampaignDonationsRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetCharityCampaignDonationsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()