# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.ame.v20190916 import models
from typing import Dict


class AmeClient(AbstractClient):
    _apiVersion = '2019-09-16'
    _endpoint = 'ame.tencentcloudapi.com'
    _service = 'ame'

    async def BatchDescribeKTVMusicDetails(
            self,
            request: models.BatchDescribeKTVMusicDetailsRequest,
            opts: Dict = None,
    ) -> models.BatchDescribeKTVMusicDetailsResponse:
        """
        根据 Id 列表查询歌曲的详细信息，包含基础信息及播放信息。
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDescribeKTVMusicDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDescribeKTVMusicDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKTVRobot(
            self,
            request: models.CreateKTVRobotRequest,
            opts: Dict = None,
    ) -> models.CreateKTVRobotResponse:
        """
        创建机器人，支持进入 RTC 房间，播放直播互动曲库歌曲。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKTVRobot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKTVRobotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuthInfo(
            self,
            request: models.DescribeAuthInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAuthInfoResponse:
        """
        获取授权项目信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuthInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuthInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudMusic(
            self,
            request: models.DescribeCloudMusicRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudMusicResponse:
        """
        获取云音乐播放信息接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudMusic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudMusicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudMusicPurchased(
            self,
            request: models.DescribeCloudMusicPurchasedRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudMusicPurchasedResponse:
        """
        获取授权项目下已购云音乐列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudMusicPurchased"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudMusicPurchasedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeItemById(
            self,
            request: models.DescribeItemByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeItemByIdResponse:
        """
        根据歌曲ID查询歌曲信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeItemById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeItemByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeItems(
            self,
            request: models.DescribeItemsRequest,
            opts: Dict = None,
    ) -> models.DescribeItemsResponse:
        """
        该服务后续会停用，不再建议使用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeItems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeItemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVMusicDetail(
            self,
            request: models.DescribeKTVMusicDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVMusicDetailResponse:
        """
        根据 Id 查询歌曲的详细信息，包含基础信息及播放信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVMusicDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVMusicDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVMusicTags(
            self,
            request: models.DescribeKTVMusicTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVMusicTagsResponse:
        """
        获取直播互动曲库标签分组信息和标签信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVMusicTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVMusicTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVPlaylistDetail(
            self,
            request: models.DescribeKTVPlaylistDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVPlaylistDetailResponse:
        """
        根据歌单 Id 获取歌单详情，包括歌单的基础信息以及歌曲列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVPlaylistDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVPlaylistDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVPlaylists(
            self,
            request: models.DescribeKTVPlaylistsRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVPlaylistsResponse:
        """
        获取直播互动曲库推荐歌单列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVPlaylists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVPlaylistsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVRobots(
            self,
            request: models.DescribeKTVRobotsRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVRobotsResponse:
        """
        获取机器人列表，支持 Id、状态等过滤条件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVRobots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVRobotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVSingerCategories(
            self,
            request: models.DescribeKTVSingerCategoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVSingerCategoriesResponse:
        """
        获取直播互动曲库歌手分类信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVSingerCategories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVSingerCategoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVSingerMusics(
            self,
            request: models.DescribeKTVSingerMusicsRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVSingerMusicsResponse:
        """
        根据歌手id，返回该歌手下歌曲列表。


        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVSingerMusics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVSingerMusicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVSingers(
            self,
            request: models.DescribeKTVSingersRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVSingersResponse:
        """
        根据过滤条件，返回匹配的歌手列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVSingers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVSingersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVSuggestions(
            self,
            request: models.DescribeKTVSuggestionsRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVSuggestionsResponse:
        """
        获取直播互动曲库联想词
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVSuggestions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVSuggestionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVTopList(
            self,
            request: models.DescribeKTVTopListRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVTopListResponse:
        """
        获取直播互动曲库歌曲的周榜和月榜
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVTopList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVTopListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLyric(
            self,
            request: models.DescribeLyricRequest,
            opts: Dict = None,
    ) -> models.DescribeLyricResponse:
        """
        根据接口的模式及歌曲ID来取得歌词信息或者波形图信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLyric"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLyricResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMusic(
            self,
            request: models.DescribeMusicRequest,
            opts: Dict = None,
    ) -> models.DescribeMusicResponse:
        """
        获取曲库包歌曲播放信息接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMusic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMusicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMusicSaleStatus(
            self,
            request: models.DescribeMusicSaleStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeMusicSaleStatusResponse:
        """
        根据音乐信息查询音乐是否在售
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMusicSaleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMusicSaleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePackageItems(
            self,
            request: models.DescribePackageItemsRequest,
            opts: Dict = None,
    ) -> models.DescribePackageItemsResponse:
        """
        获取曲库包下已核销歌曲列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePackageItems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePackageItemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePackages(
            self,
            request: models.DescribePackagesRequest,
            opts: Dict = None,
    ) -> models.DescribePackagesResponse:
        """
        获取已购曲库包列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePkgOfflineMusic(
            self,
            request: models.DescribePkgOfflineMusicRequest,
            opts: Dict = None,
    ) -> models.DescribePkgOfflineMusicResponse:
        """
        根据购买曲库包用户可查询已回退的歌曲信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePkgOfflineMusic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePkgOfflineMusicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStations(
            self,
            request: models.DescribeStationsRequest,
            opts: Dict = None,
    ) -> models.DescribeStationsResponse:
        """
        该服务后续会停用，不再建议使用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyKTVRobot(
            self,
            request: models.DestroyKTVRobotRequest,
            opts: Dict = None,
    ) -> models.DestroyKTVRobotResponse:
        """
        销毁机器人，机器人退出 RTC 房间。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyKTVRobot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyKTVRobotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMusicOnShelves(
            self,
            request: models.ModifyMusicOnShelvesRequest,
            opts: Dict = None,
    ) -> models.ModifyMusicOnShelvesResponse:
        """
        根据资源方，需要变更的参数，请求该接口进行变更，为空的参数默认为无变更
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMusicOnShelves"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMusicOnShelvesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutMusicOnTheShelves(
            self,
            request: models.PutMusicOnTheShelvesRequest,
            opts: Dict = None,
    ) -> models.PutMusicOnTheShelvesResponse:
        """
        根据资源方所传歌曲信息，进行歌曲上架，多个歌曲同时请求时，需构造复合结构进行请求
        """
        
        kwargs = {}
        kwargs["action"] = "PutMusicOnTheShelves"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutMusicOnTheShelvesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportData(
            self,
            request: models.ReportDataRequest,
            opts: Dict = None,
    ) -> models.ReportDataResponse:
        """
        客户上报用户数据功能，为了更好地为用户提供优质服务
        """
        
        kwargs = {}
        kwargs["action"] = "ReportData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchKTVMusics(
            self,
            request: models.SearchKTVMusicsRequest,
            opts: Dict = None,
    ) -> models.SearchKTVMusicsResponse:
        """
        根据搜索条件，返回匹配的歌曲列表。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchKTVMusics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchKTVMusicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncKTVRobotCommand(
            self,
            request: models.SyncKTVRobotCommandRequest,
            opts: Dict = None,
    ) -> models.SyncKTVRobotCommandResponse:
        """
        下发操作机器人指令，支持播放、暂停、恢复、歌单设置等操作指令，实现对机器人行为的控制。
        """
        
        kwargs = {}
        kwargs["action"] = "SyncKTVRobotCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncKTVRobotCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TakeMusicOffShelves(
            self,
            request: models.TakeMusicOffShelvesRequest,
            opts: Dict = None,
    ) -> models.TakeMusicOffShelvesResponse:
        """
        根据资源方所传MusicId进行将歌曲进行下架，多个MusicId使用逗号隔开
        """
        
        kwargs = {}
        kwargs["action"] = "TakeMusicOffShelves"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TakeMusicOffShelvesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)