from datetime import datetime
from aiohttp import ClientResponse, http_exceptions
from Twitch.API.Exceptions import (
    TwitchApiBadRequstException, 
    TwitchApiNotFoundException, 
    TwitchApiTooManyRequestsException, 
    TwitchApiUnauthorizedException,
    TwitchApiInvalidRequestType,
    TwitchApiIvalidUserScope)
from Twitch.API.Resources.Utils import pagenation, dateRange, RequestBaseClass, ResponseBaseClass
from Twitch.API.Resources import Analytics, Ads, Bits, Channels
from Twitch.API._ApiRequest import APIRequest
from typing import Callable, Optional
from API.Resources import Utils

class Credentials:
    def __init__(self, id: str, OauthToken: str, scopes: list) -> None:
        self.id = id
        self.Oauth = OauthToken
        self.scopes = scopes
class twitchAPI:

    def __init__(self, clientCreds: Credentials, userCreds:Credentials) -> None:

        self._APIRequest: APIRequest = APIRequest("https://api.twitch.tv/helix")

        self._credentials:dict[Utils.AuthRequired, Credentials] = {
            Utils.AuthRequired.CLIENT: clientCreds,
            Utils.AuthRequired.USER : userCreds,
        }

        self._RequestFunc: dict = {
            Utils.HTTPMethod.DELETE : self._APIRequest.deleteRequest,
            Utils.HTTPMethod.GET : self._APIRequest.getRequest,
            Utils.HTTPMethod.PATCH : self._APIRequest.patchRequest,
            Utils.HTTPMethod.POST : self._APIRequest.postRequest,
            Utils.HTTPMethod.PUT : self._APIRequest.putRequest,
            
        }

        self._APIReqestFailedExcptions: dict = {
            Utils.HTTPStatus.BAD_REQUEST : TwitchApiBadRequstException,
            Utils.HTTPStatus.UNAUTHORIZED : TwitchApiUnauthorizedException,
            Utils.HTTPStatus.NOT_FOUND : TwitchApiNotFoundException,
            Utils.HTTPStatus.TOO_MANY_REQUESTS : TwitchApiTooManyRequestsException
        }
        self._ApiRequestSuccess: list= [
            Utils.HTTPStatus.OK,
            Utils.HTTPStatus.ACCEPTED,
            Utils.HTTPStatus.NO_CONTENT,
            Utils.HTTPStatus.CREATED,

        ]
    
    def getParams(self, request: RequestBaseClass) -> list[tuple]:
        """
            turns request class variables into a list of tuples contains key/value pairs if variables are not None
        """
        params = list()
        for key, value in request.__dict__.items():
            if value is None:
                continue
            if isinstance(value, list):
                for item in value:
                    params.append((key, item))
            else:
                params.append((key,value))
        return params

    async def _twitchAPICall(self, request: RequestBaseClass, response: ResponseBaseClass, **kwargs) -> None:
        """
        Raises APIReqestFailedException(APIresponse)
        Raises TwitchApiIvalidUserScope
        """
        if request.scope is not None and request.scope not in self._credentials[Utils.AuthRequired.USER].scopes:
            raise TwitchApiIvalidUserScope("User doesn't have required scope!")    
        
        headers = {
            #set Authorization token based on api call required user 
            'Authorization': f'Bearer {self._credentials[request.authorization].Oauth}',
            'Client-Id': self._client_id
        }

        APIresponse: ClientResponse = await self._RequestFunc[request.requestType](request.endPoint, headers=headers, params=self.getParams(request), kwargs=kwargs)
        if APIresponse.status in self._ApiRequestSuccess:
            response.raw = await APIresponse.json()
            for key, value in response.raw.items():
                    response.__setattr__(key, value)
            return
        raise await self._APIReqestFailedExcptions[APIresponse.status](await response.json())

    async def StartCommercial(self, length: int) -> Ads.StartCommercialRepsonse:
        request = Ads.StartCommercialRequest(self._credentials[Utils.UserType.BROADCASTER].id, length)
        response = Ads.StartCommercialRepsonse()
        await self._twitchAPICall(request, response)
        return response

    async def GetExtensionAnalytics(self) -> Analytics.ExtensionAnalyticsResponse: 
        request = Analytics.ExtensionAnalyticsRequest()       
        response = Analytics.ExtensionAnalyticsResponse()
        await self._twitchAPICall(request, response)
        return response
    
    async def GetGameAnalytics(self, game_id: str, date_range: dateRange) -> Analytics.GameAnalyticsResponse:
        request = Analytics.GameAnalyticsRequest(game_id, date_range)
        response = Analytics.GameAnalyticsResponse()
        await self._twitchAPICall(request, response)
        return response

    async def GetBitsLeaderboard(self, count:Optional[int] = 10, period: Optional[str] = "all", started_at: Optional[datetime] = "", user_id: Optional[str]= "") -> Bits.BitsLeaderboardResponse:
        request = Bits.BitsLeaderboardRequest(count, period, started_at, user_id)
        response = Bits.BitsLeaderboardResponse()
        await self._twitchAPICall(request, response)
        return response

    async def GetCheermotes(self, broadcaster_id: Optional[str] = None) -> Bits.CheermotesResponse:
        request = Bits.CheermotesRequest(broadcaster_id)
        response = Bits.CheermotesResponse()
        await self._twitchAPICall(request, response)
        return response

    async def GetExtensionTransactions(self, extension_id:str, id: Optional[str]=None, first: Optional[int]=None, after: Optional[str]=None) -> Bits.ExtensionTransactionsResponse:
        request = Bits.ExtensionTransactionsRequest(extension_id, id, first, after)
        response = Bits.ExtensionTransactionsResponse()
        await self._twitchAPICall(request, response)
        return response

    async def GetChannelInformation(self, broadcaster_ids:list, userAuth=False) -> Channels.ChannelInformationResponse:
        request = Channels.ChannelInformationRequest(broadcaster_ids,userAuth)
        response = Channels.ChannelInformationResponse()
        await self._twitchAPICall(request, response)
        return response
    
    async def ModifyChannelInformation(self, title:Optional[str]=None, delay:Optional[int]=None, tags:Optional[list[str]]=None) -> Channels.ModifyChannelInformationResponse:
        request = Channels.ModifyChannelInformationRequest(self._credentials[Utils.AuthRequired.USER].id, title, delay, tags)
        response = Bits.ExtensionTransactionsResponse()
        await self._twitchAPICall(request, response)
        return response