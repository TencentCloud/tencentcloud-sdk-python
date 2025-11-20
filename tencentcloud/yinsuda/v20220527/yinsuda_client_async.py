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
from tencentcloud.yinsuda.v20220527 import models
from typing import Dict


class YinsudaClient(AbstractClient):
    _apiVersion = '2022-05-27'
    _endpoint = 'yinsuda.tencentcloudapi.com'
    _service = 'yinsuda'

    async def ApplyChorus(
            self,
            request: models.ApplyChorusRequest,
            opts: Dict = None,
    ) -> models.ApplyChorusResponse:
        """
        申请合唱相关信息，用于标记用户的演唱是在合唱场景下。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyChorus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyChorusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDescribeKTVMusicDetails(
            self,
            request: models.BatchDescribeKTVMusicDetailsRequest,
            opts: Dict = None,
    ) -> models.BatchDescribeKTVMusicDetailsResponse:
        """
        批量获取歌曲详细信息，包括：歌词下载链接、播放凭证、音高数据下载链接信息等。
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
        创建机器人，支持进入 RTC 房间，播放曲库歌曲。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKTVRobot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKTVRobotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVMatchMusics(
            self,
            request: models.DescribeKTVMatchMusicsRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVMatchMusicsResponse:
        """
        根据输入的规则匹配曲库中的歌曲。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVMatchMusics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVMatchMusicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVMusicAccompanySegmentUrl(
            self,
            request: models.DescribeKTVMusicAccompanySegmentUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVMusicAccompanySegmentUrlResponse:
        """
        获取歌曲伴奏片段链接，可用于抢唱
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVMusicAccompanySegmentUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVMusicAccompanySegmentUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVMusicAccompanySegmentUrlVip(
            self,
            request: models.DescribeKTVMusicAccompanySegmentUrlVipRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVMusicAccompanySegmentUrlVipResponse:
        """
        获取歌曲伴奏高潮的开始、结束时间，可用于抢唱
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVMusicAccompanySegmentUrlVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVMusicAccompanySegmentUrlVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVMusicsByTag(
            self,
            request: models.DescribeKTVMusicsByTagRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVMusicsByTagResponse:
        """
        通过标签过滤歌曲列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVMusicsByTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVMusicsByTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVPlaylistDetail(
            self,
            request: models.DescribeKTVPlaylistDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVPlaylistDetailResponse:
        """
        根据歌单 Id 获取歌单详情。
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
        获取歌单列表。
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
        
    async def DescribeKTVSuggestions(
            self,
            request: models.DescribeKTVSuggestionsRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVSuggestionsResponse:
        """
        根据关键词获取联想词列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVSuggestions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVSuggestionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKTVTags(
            self,
            request: models.DescribeKTVTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeKTVTagsResponse:
        """
        获取标签分组及分组下的标签列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKTVTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKTVTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveVipTradeInfos(
            self,
            request: models.DescribeLiveVipTradeInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveVipTradeInfosResponse:
        """
        批量获取直播会员充值流水详细信息，包括：流水号，订单状态，下订单时间等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveVipTradeInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveVipTradeInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserInfo(
            self,
            request: models.DescribeUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserInfoResponse:
        """
        获取用户信息，包括是否为直播会员，及直播会员信息等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVipUserInfo(
            self,
            request: models.DescribeVipUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVipUserInfoResponse:
        """
        获取会员信息：获取用户是否开通会员
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVipUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVipUserInfoResponse
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
        
    async def RechargeLiveVip(
            self,
            request: models.RechargeLiveVipRequest,
            opts: Dict = None,
    ) -> models.RechargeLiveVipResponse:
        """
        充值直播会员，使该用户可以在直播场景使用
        """
        
        kwargs = {}
        kwargs["action"] = "RechargeLiveVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RechargeLiveVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RechargeVip(
            self,
            request: models.RechargeVipRequest,
            opts: Dict = None,
    ) -> models.RechargeVipResponse:
        """
        充值会员
        """
        
        kwargs = {}
        kwargs["action"] = "RechargeVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RechargeVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchKTVMusics(
            self,
            request: models.SearchKTVMusicsRequest,
            opts: Dict = None,
    ) -> models.SearchKTVMusicsResponse:
        """
        根据关键词搜索歌曲，返回相关歌曲列表。
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