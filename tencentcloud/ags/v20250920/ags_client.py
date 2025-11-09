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
from tencentcloud.ags.v20250920 import models


class AgsClient(AbstractClient):
    _apiVersion = '2025-09-20'
    _endpoint = 'ags.tencentcloudapi.com'
    _service = 'ags'


    def AcquireSandboxInstanceToken(self, request):
        r"""获取访问沙箱工具时所需要使用的访问Token，创建沙箱实例后需调用此接口获取沙箱实例访问Token。
        此Token可用于调用代码沙箱实例执行代码，或浏览器沙箱实例进行浏览器操作等。

        :param request: Request instance for AcquireSandboxInstanceToken.
        :type request: :class:`tencentcloud.ags.v20250920.models.AcquireSandboxInstanceTokenRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.AcquireSandboxInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcquireSandboxInstanceToken", params, headers=headers)
            response = json.loads(body)
            model = models.AcquireSandboxInstanceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAPIKey(self, request):
        r"""创建新的API密钥，用于调用Agent Sandbox接口。相较于腾讯云Secret ID Secret Key支持调用所有接口使用，仅有部分接口支持使用API密钥调用。

        :param request: Request instance for CreateAPIKey.
        :type request: :class:`tencentcloud.ags.v20250920.models.CreateAPIKeyRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CreateAPIKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAPIKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAPIKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSandboxTool(self, request):
        r"""创建沙箱工具

        :param request: Request instance for CreateSandboxTool.
        :type request: :class:`tencentcloud.ags.v20250920.models.CreateSandboxToolRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.CreateSandboxToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSandboxTool", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSandboxToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAPIKey(self, request):
        r"""删除API密钥。注意区别于腾讯云Secret ID Secret Key，本接口删除的是Agent Sandbox专用API key。

        :param request: Request instance for DeleteAPIKey.
        :type request: :class:`tencentcloud.ags.v20250920.models.DeleteAPIKeyRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DeleteAPIKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAPIKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAPIKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSandboxTool(self, request):
        r"""删除沙箱工具

        :param request: Request instance for DeleteSandboxTool.
        :type request: :class:`tencentcloud.ags.v20250920.models.DeleteSandboxToolRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DeleteSandboxToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSandboxTool", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSandboxToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAPIKeyList(self, request):
        r"""获取API密钥列表，包含API密钥简略信息，包含名称、创建时间等。

        :param request: Request instance for DescribeAPIKeyList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeAPIKeyListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeAPIKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPIKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPIKeyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxInstanceList(self, request):
        r"""查询沙箱实例列表

        :param request: Request instance for DescribeSandboxInstanceList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeSandboxInstanceListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeSandboxInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxToolList(self, request):
        r"""查询沙箱工具列表

        :param request: Request instance for DescribeSandboxToolList.
        :type request: :class:`tencentcloud.ags.v20250920.models.DescribeSandboxToolListRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.DescribeSandboxToolListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxToolList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxToolListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartSandboxInstance(self, request):
        r"""启动沙箱实例

        :param request: Request instance for StartSandboxInstance.
        :type request: :class:`tencentcloud.ags.v20250920.models.StartSandboxInstanceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.StartSandboxInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartSandboxInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StartSandboxInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopSandboxInstance(self, request):
        r"""停止沙箱实例

        :param request: Request instance for StopSandboxInstance.
        :type request: :class:`tencentcloud.ags.v20250920.models.StopSandboxInstanceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.StopSandboxInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopSandboxInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StopSandboxInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSandboxInstance(self, request):
        r"""更新沙箱实例

        :param request: Request instance for UpdateSandboxInstance.
        :type request: :class:`tencentcloud.ags.v20250920.models.UpdateSandboxInstanceRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.UpdateSandboxInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSandboxInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSandboxInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSandboxTool(self, request):
        r"""更新沙箱工具

        :param request: Request instance for UpdateSandboxTool.
        :type request: :class:`tencentcloud.ags.v20250920.models.UpdateSandboxToolRequest`
        :rtype: :class:`tencentcloud.ags.v20250920.models.UpdateSandboxToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSandboxTool", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSandboxToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))