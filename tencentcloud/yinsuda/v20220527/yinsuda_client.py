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
            if "Error" not in response["Response"]:
                model = models.BatchDescribeKTVMusicDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            if "Error" not in response["Response"]:
                model = models.CreateKTVRobotResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            if "Error" not in response["Response"]:
                model = models.DescribeKTVMatchMusicsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            if "Error" not in response["Response"]:
                model = models.DescribeKTVPlaylistDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            if "Error" not in response["Response"]:
                model = models.DescribeKTVPlaylistsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            if "Error" not in response["Response"]:
                model = models.DescribeKTVRobotsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            if "Error" not in response["Response"]:
                model = models.DescribeKTVSuggestionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            if "Error" not in response["Response"]:
                model = models.DestroyKTVRobotResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            if "Error" not in response["Response"]:
                model = models.SearchKTVMusicsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            if "Error" not in response["Response"]:
                model = models.SyncKTVRobotCommandResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)