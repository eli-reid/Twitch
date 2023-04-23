from __imports import *
"""
Get Extension Analytics

requset:

curl -X GET 'https://api.twitch.tv/helix/analytics/extensions' \
-H 'Authorization: Bearer cfabdegwdoklmawdzdo98xt2fo512y' \
-H 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'

response:

{
   "data": [
      {
         "extension_id": "efgh",
         "URL": "https://twitch-piper-reports.s3-us-west-2.amazonaws.com/dynamic/LoL%20ADC...",
         "type": "overview_v2",
         "date_range": {
            "started_at": "2018-03-01T00:00:00Z",
            "ended_at": "2018-06-01T00:00:00Z"
         }
      },
      ...
   ],
   "pagination": {"cursor": "eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6NX19"}
}


"""

class ExtensionAnalyticsRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.GET
    scope = Scope.Analytics.Read.Extensions
    authorization = Utils.AuthRequired.USER
    endPoint = "/analytics/extensions"

    def __init__(self, 
                extension_id: Optional[str]= None, 
                type: Optional[str]= None,
                started_at: Optional[datetime] = None,
                ended_at: Optional[datetime] = None,
                first: Optional[int] = None,
                after: Optional[str] = None
                    ) -> None:
        
        self.extension_id = extension_id
        self.type = type
        self.started_at = started_at.isoformat("T") if isinstance(started_at, datetime) else started_at
        self.ended_at = ended_at.isoformat("T") if isinstance(ended_at, datetime) else started_at
        self.first = first
        self.after = after 
        super().__init__()
@dataclass
class ExtensionAnalyticsItem(Utils.DateRangeMixin):
    extension_id:str
    URL:str
    type:str

class ExtensionAnalyticsResponse(Utils.PagenationMixin, Utils.ResponseBaseClass):
    def __init__(self) -> None:
        super().__init__(ExtensionAnalyticsItem)

"""
Get Game Analytics

requset:
curl -X GET 'https://api.twitch.tv/helix/analytics/games?game_id=493057&started_at=2018-01-01T00:00:00Z&ended_at=2018-03-01T00:00:00Z' \
-H 'Authorization: Bearer cfabdegwdoklmawdzdo98xt2fo512y' \
-H 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'

response:
{
  "data": [
    {
      "game_id" : "493057",
      "URL" : "https://twitch-piper-reports.s3-us-west-2.amazonaws.com/games/66170/overview/15183...",
      "type" : "overview_v2",
      "date_range" : {
        "started_at" : "2018-01-01T00:00:00Z",
        "ended_at" : "2018-03-01T00:00:00Z"
      }
    }
  ]
}

"""


        
class GameAnalyticsRequest(Utils.RequestBaseClass):
    requestType = Utils.HTTPMethod.GET
    scope = Scope.Analytics.Read.Extensions
    authorization = Utils.AuthRequired.USER
    endPoint = "/analytics/extensions"
    game_id: str
    date_range: Utils.dateRange

    def __init__(self, 
                 game_id: Optional[str] = None,
                 type: Optional[str]= None,
                 started_at: Optional[datetime] = None,
                 ended_at: Optional[datetime] = None,
                 first: Optional[int] = None,
                 after: Optional[str] = None
                    ) -> None:
        
        self.game_id = game_id
        self.type = type
        self.started_at = started_at.isoformat("T") if isinstance(started_at, datetime) else started_at
        self.ended_at = ended_at.isoformat("T") if isinstance(ended_at, datetime) else started_at
        self.first = first
        self.after = after 
        super().__init__()

class GameAnalyticsItem(Utils.DateRangeMixin):
    def __init__(self) -> None:
        self.game_id:str
        self.URL:str
        self.type:str
class GameAnalyticsResponse(Utils.PagenationMixin, Utils.ResponseBaseClass):
    def __init__(self) -> None:
        super().__init__(GameAnalyticsItem)