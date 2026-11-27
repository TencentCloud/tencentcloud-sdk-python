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
from tencentcloud.antiddos.v20250903 import models


class AntiddosClient(AbstractClient):
    _apiVersion = '2025-09-03'
    _endpoint = 'antiddos.tencentcloudapi.com'
    _service = 'antiddos'


    def CreateProtection(self, request):
        r"""<p>创建 DDoS 高防服务防护实例。</p>
        <p>防护实例是高防服务下承载防护策略与防护资源的基本单元。创建后，您可以在实例中配置防护策略，并绑定需要防护的云资源。</p>
        <p><strong>前提条件：</strong>当前腾讯云主账号已订阅 DDoS 高防套餐，具体操作请参见 <a href="https://cloud.tencent.com/document/product/297/137989">购买指引</a>。</p>

        :param request: Request instance for CreateProtection.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.CreateProtectionRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.CreateProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProtection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProtection(self, request):
        r"""<p>删除防护实例。</p>
        <p>删除后，该实例及其绑定的防护策略将不再生效。请确保实例中没有正在使用的防护资源，或已提前将防护资源换绑至其他实例。</p>

        :param request: Request instance for DeleteProtection.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.DeleteProtectionRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DeleteProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSBlockRecords(self, request):
        r"""查询封堵解封记录和解封配额信息。

        :param request: Request instance for DescribeDDoSBlockRecords.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.DescribeDDoSBlockRecordsRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DescribeDDoSBlockRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSBlockRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSBlockRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSProtectionPolicy(self, request):
        r"""<p>按防护实例 ID 查询该实例下的 L3/4 DDoS 防护策略详情。</p>

        :param request: Request instance for DescribeDDoSProtectionPolicy.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.DescribeDDoSProtectionPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DescribeDDoSProtectionPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSProtectionPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSProtectionPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectionResources(self, request):
        r"""<p>按防护实例 ID 查询该实例下绑定的防护资源，支持分页与按资源类型过滤。</p>

        :param request: Request instance for DescribeProtectionResources.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.DescribeProtectionResourcesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DescribeProtectionResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectionResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectionResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtections(self, request):
        r"""<p>按过滤条件查询当前账号下有权限访问的 DDoS 高防服务防护实例，支持分页返回。</p>

        :param request: Request instance for DescribeProtections.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.DescribeProtectionsRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DescribeProtectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceProtections(self, request):
        r"""<p>按资源六段式查询云资源当前绑定的 DDoS 高防服务防护实例。</p>

        :param request: Request instance for DescribeResourceProtections.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.DescribeResourceProtectionsRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DescribeResourceProtectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceProtections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceProtectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDDoSProtectionPolicy(self, request):
        r"""<p>按防护实例 ID 修改该实例下的 L3/4 DDoS 防护策略。</p>

        :param request: Request instance for ModifyDDoSProtectionPolicy.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.ModifyDDoSProtectionPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.ModifyDDoSProtectionPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSProtectionPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDDoSProtectionPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProtection(self, request):
        r"""修改防护实例。支持修改防护实例的名称。

        :param request: Request instance for ModifyProtection.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.ModifyProtectionRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.ModifyProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProtection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProtectionResource(self, request):
        r"""<p>修改防护实例的防护资源。</p>
        <p>向防护实例中添加、替换或移除防护对象（即绑定到该实例进行防护的云资源）。</p>

        :param request: Request instance for ModifyProtectionResource.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.ModifyProtectionResourceRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.ModifyProtectionResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProtectionResource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProtectionResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnblockResources(self, request):
        r"""申请解封资源，可通过 DescribeDDoSBlockRecords 接口获取资源的封堵解封状态。

        :param request: Request instance for UnblockResources.
        :type request: :class:`tencentcloud.antiddos.v20250903.models.UnblockResourcesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.UnblockResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnblockResources", params, headers=headers)
            response = json.loads(body)
            model = models.UnblockResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))