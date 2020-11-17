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
from tencentcloud.sts.v20180813 import models


class StsClient(AbstractClient):
    _apiVersion = '2018-08-13'
    _endpoint = 'sts.tencentcloudapi.com'
    _service = 'sts'


    def AssumeRole(self, request):
        """申请扮演角色

        :param request: Request instance for AssumeRole.
        :type request: :class:`tencentcloud.sts.v20180813.models.AssumeRoleRequest`
        :rtype: :class:`tencentcloud.sts.v20180813.models.AssumeRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssumeRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssumeRoleResponse()
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


    def AssumeRoleWithSAML(self, request):
        """本接口（AssumeRoleWithSAML）用于根据 SAML 断言申请角色临时凭证。

        :param request: Request instance for AssumeRoleWithSAML.
        :type request: :class:`tencentcloud.sts.v20180813.models.AssumeRoleWithSAMLRequest`
        :rtype: :class:`tencentcloud.sts.v20180813.models.AssumeRoleWithSAMLResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssumeRoleWithSAML", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssumeRoleWithSAMLResponse()
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


    def GetFederationToken(self, request):
        """获取联合身份临时访问凭证

        :param request: Request instance for GetFederationToken.
        :type request: :class:`tencentcloud.sts.v20180813.models.GetFederationTokenRequest`
        :rtype: :class:`tencentcloud.sts.v20180813.models.GetFederationTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFederationToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFederationTokenResponse()
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


    def QueryApiKey(self, request):
        """拉取API密钥列表

        :param request: Request instance for QueryApiKey.
        :type request: :class:`tencentcloud.sts.v20180813.models.QueryApiKeyRequest`
        :rtype: :class:`tencentcloud.sts.v20180813.models.QueryApiKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryApiKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryApiKeyResponse()
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