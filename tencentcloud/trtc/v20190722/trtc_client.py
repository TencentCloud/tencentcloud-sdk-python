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


    def DescribeCallDetail(self, request):
        """查询指定时间内的用户列表及用户通话质量数据。

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
        """查询sdkappid下的房间列表。默认返回10条通话，一次最多返回100条通话。可查询最近5天的数据。

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