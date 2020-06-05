# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.trtc.v20190722 import models


class TrtcClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'trtc.tencentcloudapi.com'


    def CreateTroubleInfo(self, request):
        """创建异常信息

        :param request: Request instance for CreateTroubleInfo.
        :type request: :class:`tencentcloud.trtc.v20190722.models.CreateTroubleInfoRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CreateTroubleInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTroubleInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTroubleInfoResponse()
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


    def DescribeCallDetail(self, request):
        """查询指定时间内的用户列表及用户通话质量数据。可查询5天内数据，查询起止时间不超过1个小时，查询用户不超过6个

        :param request: Request instance for DescribeCallDetail.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeCallDetailRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeCallDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCallDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCallDetailResponse()
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


    def DescribeDetailEvent(self, request):
        """查询用户某次通话内的进退房，视频开关等详细事件。可查询5天内数据。

        :param request: Request instance for DescribeDetailEvent.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeDetailEventRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeDetailEventResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDetailEvent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDetailEventResponse()
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


    def DescribeHistoryScale(self, request):
        """可查询sdkqppid 每天的房间数和用户数，每分钟1次，可查询最近5天的数据。当天未结束，无法查到当天的房间数与用户数。

        :param request: Request instance for DescribeHistoryScale.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeHistoryScaleRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeHistoryScaleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHistoryScale", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHistoryScaleResponse()
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


    def DescribeRealtimeNetwork(self, request):
        """查询sdkappid维度下实时网络状态，包括上行丢包与下行丢包。可查询24小时内数据，查询起止时间不超过1个小时。

        :param request: Request instance for DescribeRealtimeNetwork.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeNetworkRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeNetworkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealtimeNetwork", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealtimeNetworkResponse()
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


    def DescribeRealtimeQuality(self, request):
        """查询sdkappid维度下实时质量数据，包括：进房成功率，首帧秒开率，音频卡顿率，视频卡顿率。可查询24小时内数据，查询起止时间不超过1个小时。

        :param request: Request instance for DescribeRealtimeQuality.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeQualityRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeQualityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealtimeQuality", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealtimeQualityResponse()
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


    def DescribeRealtimeScale(self, request):
        """查询sdkappid维度下实时规模，可查询24小时内数据，查询起止时间不超过1个小时。

        :param request: Request instance for DescribeRealtimeScale.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeScaleRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeScaleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealtimeScale", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealtimeScaleResponse()
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


    def DescribeRoomInformation(self, request):
        """查询sdkappid下的房间列表。默认返回10条通话，一次最多返回100条通话。可查询5天内的数据。

        :param request: Request instance for DescribeRoomInformation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRoomInformationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRoomInformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRoomInformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRoomInformationResponse()
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


    def DismissRoom(self, request):
        """接口说明：把房间所有用户从房间移出，解散房间。支持所有平台，Android、iOS、Windows 和 macOS 需升级到 TRTC SDK 6.6及以上版本。

        :param request: Request instance for DismissRoom.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DismissRoomRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DismissRoomResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DismissRoom", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DismissRoomResponse()
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


    def RemoveUser(self, request):
        """接口说明：将用户从房间移出，适用于主播/房主/管理员踢人等场景。支持所有平台，Android、iOS、Windows 和 macOS 需升级到 TRTC SDK 6.6及以上版本。

        :param request: Request instance for RemoveUser.
        :type request: :class:`tencentcloud.trtc.v20190722.models.RemoveUserRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RemoveUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveUserResponse()
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


    def StartMCUMixTranscode(self, request):
        """接口说明：启动云端混流，并指定混流画面中各路画面的布局位置。

        TRTC 的一个房间中可能会同时存在多路音视频流，您可以通过此 API 接口，通知腾讯云服务端将多路视频画面合成一路，并指定每一路画面的位置，同时将多路声音进行混音，最终形成一路音视频流，以便用于录制和直播观看。

        您可以通过此接口实现如下目标：
        - 设置最终直播流的画质和音质，包括视频分辨率、视频码率、视频帧率、以及声音质量等。
        - 设置各路画面的位置和布局，您只需要在启动时设置一次，排版引擎会自动完成后续的画面排布。
        - 设置录制文件名，用于二次回放。
        - 设置 CDN 直播流 ID，用于在 CDN 进行直播观看。

        目前已经支持了如下几种布局模板：
        - 悬浮模板：第一个进入房间的用户的视频画面会铺满整个屏幕，其他用户的视频画面从左下角依次水平排列，显示为小画面，最多4行，每行4个，小画面悬浮于大画面之上。最多支持1个大画面和15个小画面，如果用户只发送音频，仍然会占用画面位置。
        - 九宫格模板：所有用户的视频画面大小一致，平分整个屏幕，人数越多，每个画面的尺寸越小。最多支持16个画面，如果用户只发送音频，仍然会占用画面位置。
        - 屏幕分享模板：适合视频会议和在线教育场景的布局，屏幕分享（或者主讲的摄像头）始终占据屏幕左侧的大画面位置，其他用户依次垂直排列于右侧，最多两列，每列最多8个小画面。最多支持1个大画面和15个小画面，如果用户只发送音频，仍然会占用画面位置。

        :param request: Request instance for StartMCUMixTranscode.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartMCUMixTranscodeRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartMCUMixTranscodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartMCUMixTranscode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMCUMixTranscodeResponse()
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


    def StopMCUMixTranscode(self, request):
        """接口说明：结束云端混流

        :param request: Request instance for StopMCUMixTranscode.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopMCUMixTranscodeRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopMCUMixTranscodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopMCUMixTranscode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopMCUMixTranscodeResponse()
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