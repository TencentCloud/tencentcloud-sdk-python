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
from tencentcloud.tms.v20200713 import models


class TmsClient(AbstractClient):
    _apiVersion = '2020-07-13'
    _endpoint = 'tms.tencentcloudapi.com'
    _service = 'tms'


    def AccountTipoffAccess(self, request):
        r"""举报恶意账号

        :param request: Request instance for AccountTipoffAccess.
        :type request: :class:`tencentcloud.tms.v20200713.models.AccountTipoffAccessRequest`
        :rtype: :class:`tencentcloud.tms.v20200713.models.AccountTipoffAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AccountTipoffAccess", params, headers=headers)
            response = json.loads(body)
            model = models.AccountTipoffAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTextLib(self, request):
        r"""控制台获取用户词库列表

        :param request: Request instance for DescribeTextLib.
        :type request: :class:`tencentcloud.tms.v20200713.models.DescribeTextLibRequest`
        :rtype: :class:`tencentcloud.tms.v20200713.models.DescribeTextLibResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTextLib", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTextLibResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTextStat(self, request):
        r"""控制台识别统计

        :param request: Request instance for DescribeTextStat.
        :type request: :class:`tencentcloud.tms.v20200713.models.DescribeTextStatRequest`
        :rtype: :class:`tencentcloud.tms.v20200713.models.DescribeTextStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTextStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTextStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextModeration(self, request):
        r"""文本内容检测（Text Moderation）服务使用了深度学习技术，识别可能令人反感、不安全或不适宜的文本内容，同时支持用户配置词库黑白名单，打击自定义识别类型的图片。

        :param request: Request instance for TextModeration.
        :type request: :class:`tencentcloud.tms.v20200713.models.TextModerationRequest`
        :rtype: :class:`tencentcloud.tms.v20200713.models.TextModerationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextModeration", params, headers=headers)
            response = json.loads(body)
            model = models.TextModerationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))