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
from tencentcloud.ga2.v20250115 import models


class Ga2Client(AbstractClient):
    _apiVersion = '2025-01-15'
    _endpoint = 'ga2.tencentcloudapi.com'
    _service = 'ga2'


    def CreateAccelerateAreas(self, request):
        r"""创建加速地域

        :param request: Request instance for CreateAccelerateAreas.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateAccelerateAreasRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateAccelerateAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccelerateAreas", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccelerateAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEndpointGroup(self, request):
        r"""创建终端节点组。

        :param request: Request instance for CreateEndpointGroup.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateEndpointGroupRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateEndpointGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEndpointGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEndpointGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateForwardingRule(self, request):
        r"""创建七层转发规则

        :param request: Request instance for CreateForwardingRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateForwardingRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateForwardingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateForwardingRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateForwardingRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlobalAccelerator(self, request):
        r"""创建全球加速实例

        :param request: Request instance for CreateGlobalAccelerator.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateGlobalAcceleratorRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateGlobalAcceleratorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlobalAccelerator", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlobalAcceleratorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateListener(self, request):
        r"""创建监听器

        :param request: Request instance for CreateListener.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateListenerRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateListener", params, headers=headers)
            response = json.loads(body)
            model = models.CreateListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccelerateAreas(self, request):
        r"""删除加速地域

        :param request: Request instance for DeleteAccelerateAreas.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteAccelerateAreasRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteAccelerateAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccelerateAreas", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccelerateAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEndpointGroups(self, request):
        r"""删除终端节点组。

        :param request: Request instance for DeleteEndpointGroups.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteEndpointGroupsRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteEndpointGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEndpointGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEndpointGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteForwardingRule(self, request):
        r"""删除七层转发规则

        :param request: Request instance for DeleteForwardingRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteForwardingRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteForwardingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteForwardingRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteForwardingRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlobalAccelerator(self, request):
        r"""删除全球加速实例

        :param request: Request instance for DeleteGlobalAccelerator.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteGlobalAcceleratorRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteGlobalAcceleratorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlobalAccelerator", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlobalAcceleratorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteListener(self, request):
        r"""删除监听器

        :param request: Request instance for DeleteListener.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteListenerRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteListener", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccelerateAreas(self, request):
        r"""查询加速地域

        :param request: Request instance for DescribeAccelerateAreas.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeAccelerateAreasRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeAccelerateAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccelerateAreas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccelerateAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccelerateRegions(self, request):
        r"""查询可选加速区域

        :param request: Request instance for DescribeAccelerateRegions.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeAccelerateRegionsRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeAccelerateRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccelerateRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccelerateRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossBorderSettlement(self, request):
        r"""查询跨境账单

        :param request: Request instance for DescribeCrossBorderSettlement.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeCrossBorderSettlementRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeCrossBorderSettlementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossBorderSettlement", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossBorderSettlementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEndpointGroups(self, request):
        r"""查询终端节点组。

        :param request: Request instance for DescribeEndpointGroups.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeEndpointGroupsRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeEndpointGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEndpointGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEndpointGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeForwardingRule(self, request):
        r"""查看七层转发规则

        :param request: Request instance for DescribeForwardingRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeForwardingRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeForwardingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeForwardingRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeForwardingRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalAccelerators(self, request):
        r"""修改全球加速实例

        :param request: Request instance for DescribeGlobalAccelerators.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeGlobalAcceleratorsRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeGlobalAcceleratorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalAccelerators", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalAcceleratorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListeners(self, request):
        r"""查询监听器

        :param request: Request instance for DescribeListeners.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeListenersRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccelerateAreas(self, request):
        r"""修改加速地域

        :param request: Request instance for ModifyAccelerateAreas.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyAccelerateAreasRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyAccelerateAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccelerateAreas", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccelerateAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEndpointGroup(self, request):
        r"""修改终端节点组。

        :param request: Request instance for ModifyEndpointGroup.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyEndpointGroupRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyEndpointGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEndpointGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEndpointGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyForwardingRule(self, request):
        r"""修改七层转发规则

        :param request: Request instance for ModifyForwardingRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyForwardingRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyForwardingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyForwardingRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyForwardingRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalAccelerator(self, request):
        r"""修改全球加速实例

        :param request: Request instance for ModifyGlobalAccelerator.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyGlobalAcceleratorRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyGlobalAcceleratorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalAccelerator", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalAcceleratorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyListener(self, request):
        r"""修改监听器

        :param request: Request instance for ModifyListener.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyListenerRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyListener", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))