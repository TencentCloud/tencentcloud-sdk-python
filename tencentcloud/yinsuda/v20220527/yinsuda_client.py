# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.yinsuda.v20220527 import models


class YinsudaClient(AbstractClient):
    _apiVersion = '2022-05-27'
    _endpoint = 'yinsuda.tencentcloudapi.com'
    _service = 'yinsuda'


    def ApplyChorus(self, request):
        """申请合唱相关信息，用于标记用户的演唱是在合唱场景下。

        :param request: Request instance for ApplyChorus.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.ApplyChorusRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.ApplyChorusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyChorus", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyChorusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchDescribeKTVMusicDetails(self, request):
        """批量获取歌曲详细信息，包括：歌词下载链接、播放凭证、音高数据下载链接信息等。

        :param request: Request instance for BatchDescribeKTVMusicDetails.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.BatchDescribeKTVMusicDetailsRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.BatchDescribeKTVMusicDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDescribeKTVMusicDetails", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDescribeKTVMusicDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateKTVRobot(self, request):
        """创建机器人，支持进入 RTC 房间，播放曲库歌曲。

        :param request: Request instance for CreateKTVRobot.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.CreateKTVRobotRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.CreateKTVRobotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKTVRobot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKTVRobotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKTVMatchMusics(self, request):
        """根据输入的规则匹配曲库中的歌曲。

        :param request: Request instance for DescribeKTVMatchMusics.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVMatchMusicsRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVMatchMusicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVMatchMusics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVMatchMusicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKTVMusicAccompanySegmentUrl(self, request):
        """获取歌曲伴奏片段链接，可用于抢唱

        :param request: Request instance for DescribeKTVMusicAccompanySegmentUrl.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVMusicAccompanySegmentUrlRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVMusicAccompanySegmentUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVMusicAccompanySegmentUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVMusicAccompanySegmentUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKTVMusicsByTag(self, request):
        """通过标签过滤歌曲列表。

        :param request: Request instance for DescribeKTVMusicsByTag.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVMusicsByTagRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVMusicsByTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVMusicsByTag", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVMusicsByTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKTVPlaylistDetail(self, request):
        """根据歌单 Id 获取歌单详情。

        :param request: Request instance for DescribeKTVPlaylistDetail.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVPlaylistDetailRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVPlaylistDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVPlaylistDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVPlaylistDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKTVPlaylists(self, request):
        """获取歌单列表。

        :param request: Request instance for DescribeKTVPlaylists.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVPlaylistsRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVPlaylistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVPlaylists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVPlaylistsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKTVRobots(self, request):
        """获取机器人列表，支持 Id、状态等过滤条件。

        :param request: Request instance for DescribeKTVRobots.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVRobotsRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVRobotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVRobots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVRobotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKTVSuggestions(self, request):
        """根据关键词获取联想词列表。

        :param request: Request instance for DescribeKTVSuggestions.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVSuggestionsRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVSuggestionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVSuggestions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVSuggestionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKTVTags(self, request):
        """获取标签分组及分组下的标签列表信息。

        :param request: Request instance for DescribeKTVTags.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVTagsRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DescribeKTVTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKTVTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKTVTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveVipTradeInfos(self, request):
        """批量获取直播会员充值流水详细信息，包括：流水号，订单状态，下订单时间等

        :param request: Request instance for DescribeLiveVipTradeInfos.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DescribeLiveVipTradeInfosRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DescribeLiveVipTradeInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveVipTradeInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveVipTradeInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserInfo(self, request):
        """获取用户信息，包括是否为直播会员，及直播会员信息等

        :param request: Request instance for DescribeUserInfo.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DescribeUserInfoRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DescribeUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyKTVRobot(self, request):
        """销毁机器人，机器人退出 RTC 房间。

        :param request: Request instance for DestroyKTVRobot.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.DestroyKTVRobotRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.DestroyKTVRobotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyKTVRobot", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyKTVRobotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RechargeLiveVip(self, request):
        """充值直播会员，使该用户可以在直播场景使用

        :param request: Request instance for RechargeLiveVip.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.RechargeLiveVipRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.RechargeLiveVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RechargeLiveVip", params, headers=headers)
            response = json.loads(body)
            model = models.RechargeLiveVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchKTVMusics(self, request):
        """根据关键词搜索歌曲，返回相关歌曲列表。

        :param request: Request instance for SearchKTVMusics.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.SearchKTVMusicsRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.SearchKTVMusicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchKTVMusics", params, headers=headers)
            response = json.loads(body)
            model = models.SearchKTVMusicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncKTVRobotCommand(self, request):
        """下发操作机器人指令，支持播放、暂停、恢复、歌单设置等操作指令，实现对机器人行为的控制。

        :param request: Request instance for SyncKTVRobotCommand.
        :type request: :class:`tencentcloud.yinsuda.v20220527.models.SyncKTVRobotCommandRequest`
        :rtype: :class:`tencentcloud.yinsuda.v20220527.models.SyncKTVRobotCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncKTVRobotCommand", params, headers=headers)
            response = json.loads(body)
            model = models.SyncKTVRobotCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)