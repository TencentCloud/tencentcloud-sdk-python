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


    def DissolveRoom(self, request):
        """接口说明：把房间所有用户从房间踢出，解散房间。支持所有平台，Android、iOS、Windows 和 macOS 需升级到 TRTC SDK 6.6及以上版本。

        :param request: Request instance for DissolveRoom.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DissolveRoomRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DissolveRoomResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DissolveRoom", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DissolveRoomResponse()
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


    def KickOutUser(self, request):
        """接口说明：将用户从房间踢出。支持所有平台，Android、iOS、Windows 和 macOS 需升级到 TRTC SDK 6.6及以上版本。

        :param request: Request instance for KickOutUser.
        :type request: :class:`tencentcloud.trtc.v20190722.models.KickOutUserRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.KickOutUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("KickOutUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.KickOutUserResponse()
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