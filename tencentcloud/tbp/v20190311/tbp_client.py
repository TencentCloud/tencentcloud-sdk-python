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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tbp.v20190311 import models


class TbpClient(AbstractClient):
    _apiVersion = '2019-03-11'
    _endpoint = 'tbp.tencentcloudapi.com'
    _service = 'tbp'


    def CreateBot(self, request):
        """创建机器人

        :param request: Request instance for CreateBot.
        :type request: :class:`tencentcloud.tbp.v20190311.models.CreateBotRequest`
        :rtype: :class:`tencentcloud.tbp.v20190311.models.CreateBotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Reset(self, request):
        """对当前机器人的会话状态进行复位

        :param request: Request instance for Reset.
        :type request: :class:`tencentcloud.tbp.v20190311.models.ResetRequest`
        :rtype: :class:`tencentcloud.tbp.v20190311.models.ResetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Reset", params, headers=headers)
            response = json.loads(body)
            model = models.ResetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextProcess(self, request):
        """接收调用侧的文本输入，返回应答文本。已废弃，推荐使用最新版TextProcess接口。

        :param request: Request instance for TextProcess.
        :type request: :class:`tencentcloud.tbp.v20190311.models.TextProcessRequest`
        :rtype: :class:`tencentcloud.tbp.v20190311.models.TextProcessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextProcess", params, headers=headers)
            response = json.loads(body)
            model = models.TextProcessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextReset(self, request):
        """会话重置接口。已废弃，推荐使用最新版TextReset接口。

        :param request: Request instance for TextReset.
        :type request: :class:`tencentcloud.tbp.v20190311.models.TextResetRequest`
        :rtype: :class:`tencentcloud.tbp.v20190311.models.TextResetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextReset", params, headers=headers)
            response = json.loads(body)
            model = models.TextResetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))