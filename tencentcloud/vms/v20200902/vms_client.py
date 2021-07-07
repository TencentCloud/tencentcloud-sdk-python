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
from tencentcloud.vms.v20200902 import models


class VmsClient(AbstractClient):
    _apiVersion = '2020-09-02'
    _endpoint = 'vms.tencentcloudapi.com'
    _service = 'vms'


    def SendCodeVoice(self, request):
        """给用户发语音验证码（仅支持数字）。

        :param request: Request instance for SendCodeVoice.
        :type request: :class:`tencentcloud.vms.v20200902.models.SendCodeVoiceRequest`
        :rtype: :class:`tencentcloud.vms.v20200902.models.SendCodeVoiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendCodeVoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendCodeVoiceResponse()
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


    def SendTtsVoice(self, request):
        """给用户发送指定模板的语音通知。

        :param request: Request instance for SendTtsVoice.
        :type request: :class:`tencentcloud.vms.v20200902.models.SendTtsVoiceRequest`
        :rtype: :class:`tencentcloud.vms.v20200902.models.SendTtsVoiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendTtsVoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendTtsVoiceResponse()
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