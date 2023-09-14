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
from tencentcloud.tse.v20201207 import models


class TseClient(AbstractClient):
    _apiVersion = '2020-12-07'
    _endpoint = 'tse.tencentcloudapi.com'
    _service = 'tse'


    def CreateCloudNativeAPIGateway(self, request):
        """创建云原生API网关实例

        :param request: Request instance for CreateCloudNativeAPIGateway.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayCanaryRule(self, request):
        """创建云原生网关的灰度规则

        :param request: Request instance for CreateCloudNativeAPIGatewayCanaryRule.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayCanaryRuleRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayCanaryRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayCanaryRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayCanaryRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayRoute(self, request):
        """创建云原生网关路由

        :param request: Request instance for CreateCloudNativeAPIGatewayRoute.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayRouteRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayRoute", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayRouteRateLimit(self, request):
        """创建云原生网关限流插件(路由)

        :param request: Request instance for CreateCloudNativeAPIGatewayRouteRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayRouteRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayRouteRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayRouteRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayRouteRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayService(self, request):
        """创建云原生网关服务

        :param request: Request instance for CreateCloudNativeAPIGatewayService.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServiceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayServiceRateLimit(self, request):
        """创建云原生网关限流插件(服务)

        :param request: Request instance for CreateCloudNativeAPIGatewayServiceRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServiceRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServiceRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayServiceRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayServiceRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEngine(self, request):
        """创建引擎实例

        :param request: Request instance for CreateEngine.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateEngineRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEngine", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNativeGatewayServerGroup(self, request):
        """创建云原生网关引擎分组

        :param request: Request instance for CreateNativeGatewayServerGroup.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateNativeGatewayServerGroupRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateNativeGatewayServerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNativeGatewayServerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNativeGatewayServerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGateway(self, request):
        """删除云原生API网关实例

        :param request: Request instance for DeleteCloudNativeAPIGateway.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayCanaryRule(self, request):
        """删除云原生网关的灰度规则

        :param request: Request instance for DeleteCloudNativeAPIGatewayCanaryRule.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayCanaryRuleRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayCanaryRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayCanaryRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayCanaryRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayRoute(self, request):
        """删除云原生网关路由

        :param request: Request instance for DeleteCloudNativeAPIGatewayRoute.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayRouteRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayRouteRateLimit(self, request):
        """删除云原生网关的限流插件(路由)

        :param request: Request instance for DeleteCloudNativeAPIGatewayRouteRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayRouteRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayRouteRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayRouteRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayRouteRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayService(self, request):
        """删除云原生网关服务

        :param request: Request instance for DeleteCloudNativeAPIGatewayService.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayServiceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayServiceRateLimit(self, request):
        """删除云原生网关的限流插件(服务)

        :param request: Request instance for DeleteCloudNativeAPIGatewayServiceRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayServiceRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayServiceRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayServiceRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayServiceRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEngine(self, request):
        """删除引擎实例

        :param request: Request instance for DeleteEngine.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteEngineRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEngine", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNativeGatewayServerGroup(self, request):
        """删除网关实例分组

        :param request: Request instance for DeleteNativeGatewayServerGroup.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServerGroupRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNativeGatewayServerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNativeGatewayServerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGateway(self, request):
        """获取云原生API网关实例信息

        :param request: Request instance for DescribeCloudNativeAPIGateway.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayCanaryRules(self, request):
        """查询云原生网关灰度规则列表

        :param request: Request instance for DescribeCloudNativeAPIGatewayCanaryRules.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCanaryRulesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCanaryRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayCanaryRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayCanaryRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayConfig(self, request):
        """获取云原生API网关实例网络配置信息

        :param request: Request instance for DescribeCloudNativeAPIGatewayConfig.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayConfigRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayNodes(self, request):
        """获取云原生网关节点列表

        :param request: Request instance for DescribeCloudNativeAPIGatewayNodes.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayPorts(self, request):
        """获取云原生API网关实例端口信息

        :param request: Request instance for DescribeCloudNativeAPIGatewayPorts.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayPortsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayPortsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayPorts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayPortsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayRouteRateLimit(self, request):
        """查询云原生网关的限流插件(路由)

        :param request: Request instance for DescribeCloudNativeAPIGatewayRouteRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayRouteRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayRouteRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayRouteRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayRouteRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayRoutes(self, request):
        """查询云原生网关路由列表

        :param request: Request instance for DescribeCloudNativeAPIGatewayRoutes.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayServiceRateLimit(self, request):
        """查询云原生网关的限流插件(服务)

        :param request: Request instance for DescribeCloudNativeAPIGatewayServiceRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServiceRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServiceRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayServiceRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayServiceRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayServices(self, request):
        """查询云原生网关服务列表

        :param request: Request instance for DescribeCloudNativeAPIGatewayServices.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServicesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayServices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGateways(self, request):
        """获取云原生API网关实例列表

        :param request: Request instance for DescribeCloudNativeAPIGateways.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewaysRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNacosReplicas(self, request):
        """查询Nacos类型引擎实例副本信息

        :param request: Request instance for DescribeNacosReplicas.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeNacosReplicasRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeNacosReplicasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNacosReplicas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNacosReplicasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNacosServerInterfaces(self, request):
        """查询nacos服务接口列表

        :param request: Request instance for DescribeNacosServerInterfaces.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeNacosServerInterfacesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeNacosServerInterfacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNacosServerInterfaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNacosServerInterfacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNativeGatewayServerGroups(self, request):
        """查询云原生网关分组信息

        :param request: Request instance for DescribeNativeGatewayServerGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeNativeGatewayServerGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeNativeGatewayServerGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNativeGatewayServerGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNativeGatewayServerGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOneCloudNativeAPIGatewayService(self, request):
        """获取云原生网关服务详情

        :param request: Request instance for DescribeOneCloudNativeAPIGatewayService.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeOneCloudNativeAPIGatewayServiceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeOneCloudNativeAPIGatewayServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOneCloudNativeAPIGatewayService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOneCloudNativeAPIGatewayServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSREInstanceAccessAddress(self, request):
        """查询引擎实例访问地址

        :param request: Request instance for DescribeSREInstanceAccessAddress.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeSREInstanceAccessAddressRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeSREInstanceAccessAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSREInstanceAccessAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSREInstanceAccessAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSREInstances(self, request):
        """用于查询引擎实例列表

        :param request: Request instance for DescribeSREInstances.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeSREInstancesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeSREInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSREInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSREInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZookeeperReplicas(self, request):
        """查询Zookeeper类型注册引擎实例副本信息

        :param request: Request instance for DescribeZookeeperReplicas.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeZookeeperReplicasRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeZookeeperReplicasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZookeeperReplicas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZookeeperReplicasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZookeeperServerInterfaces(self, request):
        """查询zookeeper服务接口列表

        :param request: Request instance for DescribeZookeeperServerInterfaces.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeZookeeperServerInterfacesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeZookeeperServerInterfacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZookeeperServerInterfaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZookeeperServerInterfacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGateway(self, request):
        """修改云原生API网关实例基础信息

        :param request: Request instance for ModifyCloudNativeAPIGateway.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGateway", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayCanaryRule(self, request):
        """修改云原生网关的灰度规则

        :param request: Request instance for ModifyCloudNativeAPIGatewayCanaryRule.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayCanaryRuleRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayCanaryRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayCanaryRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayCanaryRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayRoute(self, request):
        """修改云原生网关路由

        :param request: Request instance for ModifyCloudNativeAPIGatewayRoute.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayRouteRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayRoute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayRouteRateLimit(self, request):
        """修改云原生网关限流插件(路由)

        :param request: Request instance for ModifyCloudNativeAPIGatewayRouteRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayRouteRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayRouteRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayRouteRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayRouteRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayService(self, request):
        """修改云原生网关服务

        :param request: Request instance for ModifyCloudNativeAPIGatewayService.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayServiceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayServiceRateLimit(self, request):
        """修改云原生网关限流插件(服务)

        :param request: Request instance for ModifyCloudNativeAPIGatewayServiceRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayServiceRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayServiceRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayServiceRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayServiceRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNativeGatewayServerGroup(self, request):
        """修改云原生API网关实例分组基础信息

        :param request: Request instance for ModifyNativeGatewayServerGroup.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyNativeGatewayServerGroupRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyNativeGatewayServerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNativeGatewayServerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNativeGatewayServerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCloudNativeAPIGatewaySpec(self, request):
        """修改云原生API网关实例的节点规格信息，比如节点扩缩容或者升降配

        :param request: Request instance for UpdateCloudNativeAPIGatewaySpec.
        :type request: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewaySpecRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewaySpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCloudNativeAPIGatewaySpec", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCloudNativeAPIGatewaySpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEngineInternetAccess(self, request):
        """修改引擎公网访问配置

        :param request: Request instance for UpdateEngineInternetAccess.
        :type request: :class:`tencentcloud.tse.v20201207.models.UpdateEngineInternetAccessRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateEngineInternetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEngineInternetAccess", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEngineInternetAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))