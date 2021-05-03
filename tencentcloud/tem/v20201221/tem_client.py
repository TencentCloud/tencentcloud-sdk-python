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
from tencentcloud.tem.v20201221 import models


class TemClient(AbstractClient):
    _apiVersion = '2020-12-21'
    _endpoint = 'tem.tencentcloudapi.com'
    _service = 'tem'


    def CreateCosToken(self, request):
        """生成Cos临时秘钥

        :param request: Request instance for CreateCosToken.
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateCosTokenRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateCosTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCosToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCosTokenResponse()
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


    def CreateNamespace(self, request):
        """创建命名空间

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNamespaceResponse()
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


    def DescribeNamespaces(self, request):
        """获取租户命名空间列表

        :param request: Request instance for DescribeNamespaces.
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeNamespacesRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNamespacesResponse()
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


    def ModifyIngress(self, request):
        """创建或者更新 Ingress 规则

        :param request: Request instance for ModifyIngress.
        :type request: :class:`tencentcloud.tem.v20201221.models.ModifyIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.ModifyIngressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIngress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIngressResponse()
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


    def ModifyNamespace(self, request):
        """编辑命名空间

        :param request: Request instance for ModifyNamespace.
        :type request: :class:`tencentcloud.tem.v20201221.models.ModifyNamespaceRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.ModifyNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNamespaceResponse()
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