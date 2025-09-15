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
from tencentcloud.iap.v20240713 import models


class IapClient(AbstractClient):
    _apiVersion = '2024-07-13'
    _endpoint = 'iap.tencentcloudapi.com'
    _service = 'iap'


    def CreateIAPUserOIDCConfig(self, request):
        r"""创建用户OIDC配置。只能创建一个用户OIDC身份提供商，并且创建用户OIDC配置之后会自动关闭用户SAML SSO身份提供商。

        :param request: Request instance for CreateIAPUserOIDCConfig.
        :type request: :class:`tencentcloud.iap.v20240713.models.CreateIAPUserOIDCConfigRequest`
        :rtype: :class:`tencentcloud.iap.v20240713.models.CreateIAPUserOIDCConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIAPUserOIDCConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIAPUserOIDCConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIAPLoginSessionDuration(self, request):
        r"""查询登录会话时长

        :param request: Request instance for DescribeIAPLoginSessionDuration.
        :type request: :class:`tencentcloud.iap.v20240713.models.DescribeIAPLoginSessionDurationRequest`
        :rtype: :class:`tencentcloud.iap.v20240713.models.DescribeIAPLoginSessionDurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIAPLoginSessionDuration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIAPLoginSessionDurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIAPUserOIDCConfig(self, request):
        r"""查询用户OIDC配置

        :param request: Request instance for DescribeIAPUserOIDCConfig.
        :type request: :class:`tencentcloud.iap.v20240713.models.DescribeIAPUserOIDCConfigRequest`
        :rtype: :class:`tencentcloud.iap.v20240713.models.DescribeIAPUserOIDCConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIAPUserOIDCConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIAPUserOIDCConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableIAPUserSSO(self, request):
        r"""禁用用户SSO

        :param request: Request instance for DisableIAPUserSSO.
        :type request: :class:`tencentcloud.iap.v20240713.models.DisableIAPUserSSORequest`
        :rtype: :class:`tencentcloud.iap.v20240713.models.DisableIAPUserSSOResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableIAPUserSSO", params, headers=headers)
            response = json.loads(body)
            model = models.DisableIAPUserSSOResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIAPLoginSessionDuration(self, request):
        r"""修改登录会话时长

        :param request: Request instance for ModifyIAPLoginSessionDuration.
        :type request: :class:`tencentcloud.iap.v20240713.models.ModifyIAPLoginSessionDurationRequest`
        :rtype: :class:`tencentcloud.iap.v20240713.models.ModifyIAPLoginSessionDurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIAPLoginSessionDuration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIAPLoginSessionDurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateIAPUserOIDCConfig(self, request):
        r"""修改用户OIDC配置

        :param request: Request instance for UpdateIAPUserOIDCConfig.
        :type request: :class:`tencentcloud.iap.v20240713.models.UpdateIAPUserOIDCConfigRequest`
        :rtype: :class:`tencentcloud.iap.v20240713.models.UpdateIAPUserOIDCConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateIAPUserOIDCConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateIAPUserOIDCConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))