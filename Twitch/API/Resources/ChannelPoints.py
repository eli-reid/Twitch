from __imports import *

"""
    Create Custom Rewards

    curl -X POST 'https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id=274637212' \
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
        "url_1x": "https://static-cdn.jtvnw.net/custom-reward-images/default-1.png",
        "url_2x": "https://static-cdn.jtvnw.net/custom-reward-images/default-2.png",
        "url_4x": "https://static-cdn.jtvnw.net/custom-reward-images/default-4.png"
      },
      "should_redemptions_skip_request_queue": false,
      "redemptions_redeemed_current_stream": null,
      "cooldown_expires_at": null
    }
  ]
}
"""

class CreateCustomRewardsRequest(Utils.RequestBaseClass):
    requestType = Utils.RequestMethods.POST
    scope = Scope.Channel.Manage.Redemptions
    authorization = Utils.AuthRequired.USER
    endPoint ="/channel_points/custom_rewards"

    def __init__(self, title: str,) -> None:
        super().__init__()

class CreateCustomRewardsResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class DeleteCustomRewardRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"

class DeleteCustomRewardResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetCustomRewardRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class GetCustomRewardResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class GetCustomRewardRedemptionRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    
    
class GetCustomRewardRedemptionResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UpdateCustomRewardRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class UpdateCustomRewardResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()

class UpdateRedemptionStatusRequest(Utils.RequestBaseClass):
        requestType = Utils.RequestMethods.POST
        scope = Scope.Channel.Manage.Redemptions
        authorization = Utils.AuthRequired.USER
        endPoint ="//channel_points//custom_rewards"
    

class UpdateRedemptionStatusResponse(Utils.ResponseBaseClass):
        def __init__(self) -> None:
            super().__init__()