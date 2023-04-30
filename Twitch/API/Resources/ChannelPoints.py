from Twitch.API.Resources.__imports import *

"""
    Create Custom Rewards

    curl -X POST 'https:/api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id=274637212' \
    -H 'client-id: gx2pv4208cff0ig9ou7nk3riccffxt' \
    -H 'Authorization: Bearer vjxv3i0l4zxru966wsnwji51tmpkj2' \
    -H 'Content-Type: application/json' \
    -d '{
    "title":"game analysis 1v1",
    "cost":50000
    }'

    {
  "data": [
    {
      "broadcaster_name": "torpedo09",
      "broadcaster_login": "torpedo09",
      "broadcaster_id": "274637212",
      "id": "afaa7e34-6b17-49f0-a19a-d1e76eaaf673",
      "image": null,
      "background_color": "#00E5CB",
      "is_enabled": true,
      "cost": 50000,
      "title": "game analysis 1v1",
      "prompt": "",
      "is_user_input_required": false,
      "max_per_stream_setting": {
        "is_enabled": false,
        "max_per_stream": 0
      },
      "max_per_user_per_stream_setting": {
        "is_enabled": false,
        "max_per_user_per_stream": 0
      },
      "global_cooldown_setting": {
        "is_enabled": false,
        "global_cooldown_seconds": 0
      },
      "is_paused": false,
      "is_in_stock": true,
      "default_image": {
        "url_1x": "https:/static-cdn.jtvnw.net/custom-reward-images/default-1.png",
        "url_2x": "https:/static-cdn.jtvnw.net/custom-reward-images/default-2.png",
        "url_4x": "https:/static-cdn.jtvnw.net/custom-reward-images/default-4.png"
      },
      "should_redemptions_skip_request_queue": false,
      "redemptions_redeemed_current_stream": null,
      "cooldown_expires_at": null
    }
  ]
}
"""

class  MaxPerStreamSetting:
    is_enabled: bool
    max_per_stream: int


class MaxPerUserPerStreamSetting:
    is_enabled: bool
    max_per_user_per_stream: int

class GlobalCoolDownSetting:
    is_enabled: bool
    global_cooldown_seconds: int

class CustomRewardsImageItem:
      url_1x: str
      url_2x: str
      url_4x: str

class CreateCustomRewardsRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.POST
    scope = Scope.Channel.Manage.Redemptions
    authorization = Utils.AuthRequired.USER
    endPoint ="/channel_points/custom_rewards"

    def __init__(self, broadcaster_id: str, 
                 title: str,
                 cost: int,
                 prompt: Optional[str]=None,
                 is_enabled: Optional[bool]=None,
                 background_color: Optional[str]=None,
                 is_user_input_required: Optional[bool]=None,
                 is_max_per_stream_enabled: Optional[bool]=None,
                 max_per_stream: Optional[int]=None,
                 is_max_per_user_per_stream_enabled: Optional[bool]=None,
                 max_per_user_per_stream: Optional[int]=None,
                 is_global_cooldown_enabled: Optional[bool]=None,
                 global_cooldown_seconds: Optional[int]=None,
                 should_redemptions_skip_request_queue: Optional[bool]=None) -> None:
        
        self.title: str = title
        self.cost: int = cost
        self.prompt: Optional[str] = prompt
        self.is_enabled: Optional[bool]= is_enabled
        self.background_color: Optional[str] = background_color
        self.is_user_input_required: Optional[bool] = is_user_input_required
        self.is_max_per_stream_enabled: Optional[bool] = is_max_per_stream_enabled
        self.max_per_stream: Optional[int] = max_per_stream
        self.is_max_per_user_per_stream_enabled: Optional[bool] = is_max_per_user_per_stream_enabled
        self.max_per_user_per_stream: Optional[int] = max_per_user_per_stream
        self.is_global_cooldown_enabled: Optional[bool] = global_cooldown_seconds 
        self.global_cooldown_seconds: Optional[int] = global_cooldown_seconds
        self.should_redemptions_skip_request_queue: Optional[bool] = should_redemptions_skip_request_queue
        super().__init__()

class CustomRewardsItem:
    broadcaster_id: str
    broadcaster_login: str
    broadcaster_name: str
    id: str
    title: str
    prompt: str
    cost: int
    image: CustomRewardsImageItem
    default_image: CustomRewardsImageItem
    background_color: str
    is_enabled: bool
    is_user_input_required: bool
    max_per_stream_setting: MaxPerStreamSetting
    max_per_user_per_stream_setting: MaxPerUserPerStreamSetting
    global_cooldown_setting: GlobalCoolDownSetting
    is_paused: bool
    is_in_stock: bool
    should_redemptions_skip_request_queue: bool
    redemptions_redeemed_current_stream: int
    cooldown_expires_at: str

class CreateCustomRewardsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__(CustomRewardsItem)


class DeleteCustomRewardRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.DELETE
    scope = Scope.Channel.Manage.Redemptions
    authorization = Utils.AuthRequired.USER
    endPoint ="/channel_points/custom_rewards"
    def __init__(self,broadcaster_id: str, id: str) -> None:
          self.broadcaster_id: str = broadcaster_id
          self.id: str = id
          super().__init__()
    
class DeleteCustomRewardResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__(None)

class GetCustomRewardRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.GET
    scope = [Scope.Channel.Manage.Redemptions, Scope.Channel.Read.Redemptions]
    authorization = Utils.AuthRequired.USER
    endPoint ="/channel_points/custom_rewards"
    def __init__(self,broadcaster_id:str, id: Optional[str]=None, only_manageable_rewards: Optional[bool]=None) -> None:
          super().__init__()

class GetCustomRewardResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__(CustomRewardsItem)

class GetCustomRewardRedemptionRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="/channel_points/custom_rewards"
    
    
class GetCustomRewardRedemptionResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UpdateCustomRewardRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="/channel_points/custom_rewards"
    

class UpdateCustomRewardResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UpdateRedemptionStatusRequest(Utils.RequestBaseClass):
        requestType = Utils.HTTPMethod.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="/channel_points/custom_rewards"
    

class UpdateRedemptionStatusResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()