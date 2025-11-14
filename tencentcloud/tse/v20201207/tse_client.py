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
from tencentcloud.tse.v20201207 import models


class TseClient(AbstractClient):
    _apiVersion = '2020-12-07'
    _endpoint = 'tse.tencentcloudapi.com'
    _service = 'tse'


    def BindAutoScalerResourceStrategyToGroups(self, request):
        r"""弹性伸缩策略批量绑定网关分组

        :param request: Request instance for BindAutoScalerResourceStrategyToGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.BindAutoScalerResourceStrategyToGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.BindAutoScalerResourceStrategyToGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindAutoScalerResourceStrategyToGroups", params, headers=headers)
            response = json.loads(body)
            model = models.BindAutoScalerResourceStrategyToGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseWafProtection(self, request):
        r"""关闭 WAF 防护

        :param request: Request instance for CloseWafProtection.
        :type request: :class:`tencentcloud.tse.v20201207.models.CloseWafProtectionRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloseWafProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseWafProtection", params, headers=headers)
            response = json.loads(body)
            model = models.CloseWafProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoScalerResourceStrategy(self, request):
        r"""创建弹性伸缩策略

        :param request: Request instance for CreateAutoScalerResourceStrategy.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateAutoScalerResourceStrategyRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateAutoScalerResourceStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoScalerResourceStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoScalerResourceStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGateway(self, request):
        r"""创建云原生API网关实例

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
        r"""创建云原生网关的灰度规则

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


    def CreateCloudNativeAPIGatewayCertificate(self, request):
        r"""创建云原生网关证书

        :param request: Request instance for CreateCloudNativeAPIGatewayCertificate.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayCertificateRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayPublicNetwork(self, request):
        r"""创建公网网络配置

        :param request: Request instance for CreateCloudNativeAPIGatewayPublicNetwork.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayPublicNetworkRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayPublicNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayPublicNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayPublicNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayRoute(self, request):
        r"""创建云原生网关路由

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
        r"""创建云原生网关限流插件(路由)

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
        r"""创建云原生网关服务

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
        r"""创建云原生网关限流插件(服务)

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


    def CreateConfigFile(self, request):
        r"""创建配置文件

        :param request: Request instance for CreateConfigFile.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateConfigFileRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateConfigFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConfigFileGroup(self, request):
        r"""创建服务治理中心配置文件组

        :param request: Request instance for CreateConfigFileGroup.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateConfigFileGroupRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateConfigFileGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigFileGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigFileGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEngine(self, request):
        r"""创建引擎实例

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


    def CreateGovernanceAlias(self, request):
        r"""创建治理中心服务别名

        :param request: Request instance for CreateGovernanceAlias.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateGovernanceAliasRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateGovernanceAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGovernanceAlias", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGovernanceAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGovernanceInstances(self, request):
        r"""创建服务实例

        :param request: Request instance for CreateGovernanceInstances.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateGovernanceInstancesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateGovernanceInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGovernanceInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGovernanceInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGovernanceNamespaces(self, request):
        r"""创建治理中心命名空间

        :param request: Request instance for CreateGovernanceNamespaces.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateGovernanceNamespacesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateGovernanceNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGovernanceNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGovernanceNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGovernanceServices(self, request):
        r"""创建治理中心服务

        :param request: Request instance for CreateGovernanceServices.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateGovernanceServicesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateGovernanceServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGovernanceServices", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGovernanceServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNativeGatewayServerGroup(self, request):
        r"""创建云原生网关引擎分组

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


    def CreateNativeGatewayServiceSource(self, request):
        r"""创建网关服务来源

        :param request: Request instance for CreateNativeGatewayServiceSource.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateNativeGatewayServiceSourceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateNativeGatewayServiceSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNativeGatewayServiceSource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNativeGatewayServiceSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrModifyCloudNativeAPIGatewayIPRestriction(self, request):
        r"""创建或编辑云原生网关访问控制

        :param request: Request instance for CreateOrModifyCloudNativeAPIGatewayIPRestriction.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateOrModifyCloudNativeAPIGatewayIPRestrictionRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateOrModifyCloudNativeAPIGatewayIPRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrModifyCloudNativeAPIGatewayIPRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrModifyCloudNativeAPIGatewayIPRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrUpdateConfigFileAndRelease(self, request):
        r"""创建或更新配置文件并发布配置

        :param request: Request instance for CreateOrUpdateConfigFileAndRelease.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateOrUpdateConfigFileAndReleaseRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateOrUpdateConfigFileAndReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrUpdateConfigFileAndRelease", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrUpdateConfigFileAndReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWafDomains(self, request):
        r"""新建 WAF 防护域名

        :param request: Request instance for CreateWafDomains.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateWafDomainsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateWafDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWafDomains", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWafDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAutoScalerResourceStrategy(self, request):
        r"""删除弹性伸缩策略

        :param request: Request instance for DeleteAutoScalerResourceStrategy.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteAutoScalerResourceStrategyRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteAutoScalerResourceStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoScalerResourceStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAutoScalerResourceStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGateway(self, request):
        r"""删除云原生API网关实例

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
        r"""删除云原生网关的灰度规则

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


    def DeleteCloudNativeAPIGatewayCertificate(self, request):
        r"""删除云原生网关证书

        :param request: Request instance for DeleteCloudNativeAPIGatewayCertificate.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayCertificateRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayIPRestriction(self, request):
        r"""删除云原生网关访问控制

        :param request: Request instance for DeleteCloudNativeAPIGatewayIPRestriction.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayIPRestrictionRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayIPRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayIPRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayIPRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayPublicNetwork(self, request):
        r"""删除公网网络配置

        :param request: Request instance for DeleteCloudNativeAPIGatewayPublicNetwork.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayPublicNetworkRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayPublicNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayPublicNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayPublicNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayRoute(self, request):
        r"""删除云原生网关路由

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
        r"""删除云原生网关的限流插件(路由)

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
        r"""删除云原生网关服务

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
        r"""删除云原生网关的限流插件(服务)

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


    def DeleteConfigFileGroup(self, request):
        r"""删除配置文件分组

        :param request: Request instance for DeleteConfigFileGroup.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteConfigFileGroupRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteConfigFileGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfigFileGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigFileGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConfigFileReleases(self, request):
        r"""删除配置发布

        :param request: Request instance for DeleteConfigFileReleases.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteConfigFileReleasesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteConfigFileReleasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfigFileReleases", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigFileReleasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConfigFiles(self, request):
        r"""删除配置文件

        :param request: Request instance for DeleteConfigFiles.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteConfigFilesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteConfigFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfigFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEngine(self, request):
        r"""删除引擎实例

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


    def DeleteGovernanceAliases(self, request):
        r"""删除治理中心服务别名

        :param request: Request instance for DeleteGovernanceAliases.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceAliasesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceAliasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGovernanceAliases", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGovernanceAliasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGovernanceInstances(self, request):
        r"""删除服务实例

        :param request: Request instance for DeleteGovernanceInstances.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceInstancesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGovernanceInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGovernanceInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGovernanceInstancesByHost(self, request):
        r"""删除治理中心服务实例

        :param request: Request instance for DeleteGovernanceInstancesByHost.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceInstancesByHostRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceInstancesByHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGovernanceInstancesByHost", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGovernanceInstancesByHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGovernanceNamespaces(self, request):
        r"""删除治理中心命名空间

        :param request: Request instance for DeleteGovernanceNamespaces.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceNamespacesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGovernanceNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGovernanceNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGovernanceServices(self, request):
        r"""删除治理中心服务

        :param request: Request instance for DeleteGovernanceServices.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceServicesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGovernanceServices", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGovernanceServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNativeGatewayServerGroup(self, request):
        r"""删除网关实例分组

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


    def DeleteNativeGatewayServiceSource(self, request):
        r"""删除网关服务来源实例

        :param request: Request instance for DeleteNativeGatewayServiceSource.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServiceSourceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServiceSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNativeGatewayServiceSource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNativeGatewayServiceSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWafDomains(self, request):
        r"""删除 WAF 防护域名

        :param request: Request instance for DeleteWafDomains.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteWafDomainsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteWafDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWafDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWafDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllConfigFileTemplates(self, request):
        r"""获取全量配置文件模板列表

        :param request: Request instance for DescribeAllConfigFileTemplates.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeAllConfigFileTemplatesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeAllConfigFileTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllConfigFileTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllConfigFileTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScalerResourceStrategies(self, request):
        r"""查看弹性伸缩策略列表

        :param request: Request instance for DescribeAutoScalerResourceStrategies.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeAutoScalerResourceStrategiesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeAutoScalerResourceStrategiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScalerResourceStrategies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScalerResourceStrategiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScalerResourceStrategyBindingGroups(self, request):
        r"""查看弹性伸缩策略绑定的网关分组

        :param request: Request instance for DescribeAutoScalerResourceStrategyBindingGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeAutoScalerResourceStrategyBindingGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeAutoScalerResourceStrategyBindingGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScalerResourceStrategyBindingGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScalerResourceStrategyBindingGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGateway(self, request):
        r"""获取云原生API网关实例信息

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
        r"""查询云原生网关灰度规则列表

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


    def DescribeCloudNativeAPIGatewayCertificateDetails(self, request):
        r"""查询云原生网关单个证书详情

        :param request: Request instance for DescribeCloudNativeAPIGatewayCertificateDetails.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCertificateDetailsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCertificateDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayCertificateDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayCertificateDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayCertificates(self, request):
        r"""查询云原生网关证书列表

        :param request: Request instance for DescribeCloudNativeAPIGatewayCertificates.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCertificatesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayConfig(self, request):
        r"""获取云原生API网关实例网络配置信息

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


    def DescribeCloudNativeAPIGatewayIPRestriction(self, request):
        r"""查询云原生网关访问控制

        :param request: Request instance for DescribeCloudNativeAPIGatewayIPRestriction.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayIPRestrictionRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayIPRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayIPRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayIPRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayInfoByIp(self, request):
        r"""根据公网IP查询云原生网关实例信息

        :param request: Request instance for DescribeCloudNativeAPIGatewayInfoByIp.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayInfoByIpRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayInfoByIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayInfoByIp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayInfoByIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayNodes(self, request):
        r"""获取云原生网关节点列表

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
        r"""获取云原生API网关实例端口信息

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
        r"""查询云原生网关的限流插件(路由)

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
        r"""查询云原生网关路由列表

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
        r"""查询云原生网关的限流插件(服务)

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
        r"""查询云原生网关服务列表

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


    def DescribeCloudNativeAPIGatewayServicesLight(self, request):
        r"""轻量查询云原生网关服务列表

        :param request: Request instance for DescribeCloudNativeAPIGatewayServicesLight.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServicesLightRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServicesLightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayServicesLight", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayServicesLightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayUpstream(self, request):
        r"""获取云原生网关服务详情下的Upstream列表

        :param request: Request instance for DescribeCloudNativeAPIGatewayUpstream.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayUpstreamRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayUpstreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayUpstream", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayUpstreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGateways(self, request):
        r"""获取云原生API网关实例列表

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


    def DescribeConfigFile(self, request):
        r"""根据命名空间、组、名字查找配置文件

        :param request: Request instance for DescribeConfigFile.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigFileGroups(self, request):
        r"""根据条件分页查询配置文件组

        :param request: Request instance for DescribeConfigFileGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigFileGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigFileGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigFileRelease(self, request):
        r"""获取配置文件发布

        :param request: Request instance for DescribeConfigFileRelease.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileReleaseRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigFileRelease", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigFileReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigFileReleaseHistories(self, request):
        r"""获取配置文件发布历史列表

        :param request: Request instance for DescribeConfigFileReleaseHistories.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileReleaseHistoriesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileReleaseHistoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigFileReleaseHistories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigFileReleaseHistoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigFileReleaseVersions(self, request):
        r"""查询某个配置所有版本信息

        :param request: Request instance for DescribeConfigFileReleaseVersions.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileReleaseVersionsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileReleaseVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigFileReleaseVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigFileReleaseVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigFileReleases(self, request):
        r"""查询配置版本列表

        :param request: Request instance for DescribeConfigFileReleases.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileReleasesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFileReleasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigFileReleases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigFileReleasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigFiles(self, request):
        r"""根据命名空间、组名、名称、标签查询配置文件列表

        :param request: Request instance for DescribeConfigFiles.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFilesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigFilesByGroup(self, request):
        r"""根据group查询配置文件列表

        :param request: Request instance for DescribeConfigFilesByGroup.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFilesByGroupRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeConfigFilesByGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigFilesByGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigFilesByGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGovernanceAliases(self, request):
        r"""查询治理中心服务别名列表

        :param request: Request instance for DescribeGovernanceAliases.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceAliasesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceAliasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGovernanceAliases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGovernanceAliasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGovernanceInstances(self, request):
        r"""查询服务实例

        :param request: Request instance for DescribeGovernanceInstances.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceInstancesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGovernanceInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGovernanceInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGovernanceNamespaces(self, request):
        r"""查询服务治理中心命名空间列表

        :param request: Request instance for DescribeGovernanceNamespaces.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceNamespacesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGovernanceNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGovernanceNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGovernanceServiceContractVersions(self, request):
        r"""查询服务下契约版本列表

        :param request: Request instance for DescribeGovernanceServiceContractVersions.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceServiceContractVersionsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceServiceContractVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGovernanceServiceContractVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGovernanceServiceContractVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGovernanceServiceContracts(self, request):
        r"""查询服务契约定义列表

        :param request: Request instance for DescribeGovernanceServiceContracts.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceServiceContractsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceServiceContractsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGovernanceServiceContracts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGovernanceServiceContractsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGovernanceServices(self, request):
        r"""查询治理中心服务列表

        :param request: Request instance for DescribeGovernanceServices.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceServicesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGovernanceServices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGovernanceServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceTagInfos(self, request):
        r"""查看实例的标签信息

        :param request: Request instance for DescribeInstanceTagInfos.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeInstanceTagInfosRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeInstanceTagInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceTagInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTagInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNacosReplicas(self, request):
        r"""查询Nacos类型引擎实例副本信息

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
        r"""查询nacos服务接口列表

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
        r"""查询云原生网关分组信息

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


    def DescribeNativeGatewayServiceSources(self, request):
        r"""查询网关服务来源实例列表

        :param request: Request instance for DescribeNativeGatewayServiceSources.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeNativeGatewayServiceSourcesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeNativeGatewayServiceSourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNativeGatewayServiceSources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNativeGatewayServiceSourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOneCloudNativeAPIGatewayService(self, request):
        r"""获取云原生网关服务详情

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


    def DescribePublicAddressConfig(self, request):
        r"""查询公网地址信息

        :param request: Request instance for DescribePublicAddressConfig.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribePublicAddressConfigRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribePublicAddressConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicAddressConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicAddressConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicNetwork(self, request):
        r"""查询云原生API网关实例公网详情

        :param request: Request instance for DescribePublicNetwork.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribePublicNetworkRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribePublicNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSREInstanceAccessAddress(self, request):
        r"""查询引擎实例访问地址

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
        r"""用于查询引擎实例列表

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


    def DescribeUpstreamHealthCheckConfig(self, request):
        r"""获取云原生网关服务健康检查配置

        :param request: Request instance for DescribeUpstreamHealthCheckConfig.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeUpstreamHealthCheckConfigRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeUpstreamHealthCheckConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpstreamHealthCheckConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpstreamHealthCheckConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWafDomains(self, request):
        r"""获取 WAF 防护域名

        :param request: Request instance for DescribeWafDomains.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeWafDomainsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeWafDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWafDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWafDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWafProtection(self, request):
        r"""获取 WAF 防护状态

        :param request: Request instance for DescribeWafProtection.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeWafProtectionRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeWafProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWafProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWafProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZookeeperReplicas(self, request):
        r"""查询Zookeeper类型注册引擎实例副本信息

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
        r"""查询zookeeper服务接口列表

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


    def ModifyAutoScalerResourceStrategy(self, request):
        r"""更新弹性伸缩策略

        :param request: Request instance for ModifyAutoScalerResourceStrategy.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyAutoScalerResourceStrategyRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyAutoScalerResourceStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoScalerResourceStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoScalerResourceStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGateway(self, request):
        r"""修改云原生API网关实例基础信息

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
        r"""修改云原生网关的灰度规则

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


    def ModifyCloudNativeAPIGatewayCertificate(self, request):
        r"""更新云原生网关证书

        :param request: Request instance for ModifyCloudNativeAPIGatewayCertificate.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayCertificateRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayRoute(self, request):
        r"""修改云原生网关路由

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
        r"""修改云原生网关限流插件(路由)

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
        r"""修改云原生网关服务

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
        r"""修改云原生网关限流插件(服务)

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


    def ModifyConfigFileGroup(self, request):
        r"""批量修改配置文件组

        :param request: Request instance for ModifyConfigFileGroup.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyConfigFileGroupRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyConfigFileGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConfigFileGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConfigFileGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConfigFiles(self, request):
        r"""修改配置文件

        :param request: Request instance for ModifyConfigFiles.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyConfigFilesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyConfigFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConfigFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConfigFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsoleNetwork(self, request):
        r"""修改网关实例Konga网络配置

        :param request: Request instance for ModifyConsoleNetwork.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyConsoleNetworkRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyConsoleNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsoleNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsoleNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGovernanceAlias(self, request):
        r"""修改治理中心服务别名

        :param request: Request instance for ModifyGovernanceAlias.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyGovernanceAliasRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyGovernanceAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGovernanceAlias", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGovernanceAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGovernanceInstances(self, request):
        r"""修改治理中心服务实例

        :param request: Request instance for ModifyGovernanceInstances.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyGovernanceInstancesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyGovernanceInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGovernanceInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGovernanceInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGovernanceNamespaces(self, request):
        r"""修改治理中心命名空间

        :param request: Request instance for ModifyGovernanceNamespaces.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyGovernanceNamespacesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyGovernanceNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGovernanceNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGovernanceNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGovernanceServices(self, request):
        r"""修改治理中心服务

        :param request: Request instance for ModifyGovernanceServices.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyGovernanceServicesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyGovernanceServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGovernanceServices", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGovernanceServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNativeGatewayServerGroup(self, request):
        r"""修改云原生API网关实例分组基础信息

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


    def ModifyNativeGatewayServiceSource(self, request):
        r"""修改网关服务来源

        :param request: Request instance for ModifyNativeGatewayServiceSource.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyNativeGatewayServiceSourceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyNativeGatewayServiceSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNativeGatewayServiceSource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNativeGatewayServiceSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkAccessStrategy(self, request):
        r"""修改云原生API网关实例Kong访问策略，支持白名单或者黑名单。

        :param request: Request instance for ModifyNetworkAccessStrategy.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyNetworkAccessStrategyRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyNetworkAccessStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkAccessStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkAccessStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkBasicInfo(self, request):
        r"""修改云原生API网关实例网络基本信息，例如带宽以及描述、规格升级，只支持修改客户端公网/内网的信息。

        :param request: Request instance for ModifyNetworkBasicInfo.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyNetworkBasicInfoRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyNetworkBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUpstreamNodeStatus(self, request):
        r"""修改云原生网关上游实例节点健康状态

        :param request: Request instance for ModifyUpstreamNodeStatus.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyUpstreamNodeStatusRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyUpstreamNodeStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUpstreamNodeStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUpstreamNodeStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenWafProtection(self, request):
        r"""开启 WAF 防护

        :param request: Request instance for OpenWafProtection.
        :type request: :class:`tencentcloud.tse.v20201207.models.OpenWafProtectionRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.OpenWafProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenWafProtection", params, headers=headers)
            response = json.loads(body)
            model = models.OpenWafProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishConfigFiles(self, request):
        r"""发布配置文件

        :param request: Request instance for PublishConfigFiles.
        :type request: :class:`tencentcloud.tse.v20201207.models.PublishConfigFilesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.PublishConfigFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishConfigFiles", params, headers=headers)
            response = json.loads(body)
            model = models.PublishConfigFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartSREInstance(self, request):
        r"""重启微服务引擎实例

        :param request: Request instance for RestartSREInstance.
        :type request: :class:`tencentcloud.tse.v20201207.models.RestartSREInstanceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.RestartSREInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartSREInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestartSREInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackConfigFileReleases(self, request):
        r"""回滚配置发布

        :param request: Request instance for RollbackConfigFileReleases.
        :type request: :class:`tencentcloud.tse.v20201207.models.RollbackConfigFileReleasesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.RollbackConfigFileReleasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackConfigFileReleases", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackConfigFileReleasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindAutoScalerResourceStrategyFromGroups(self, request):
        r"""弹性伸缩策略批量解绑网关分组

        :param request: Request instance for UnbindAutoScalerResourceStrategyFromGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.UnbindAutoScalerResourceStrategyFromGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UnbindAutoScalerResourceStrategyFromGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindAutoScalerResourceStrategyFromGroups", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindAutoScalerResourceStrategyFromGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCloudNativeAPIGatewayCertificateInfo(self, request):
        r"""修改云原生网关证书信息

        :param request: Request instance for UpdateCloudNativeAPIGatewayCertificateInfo.
        :type request: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewayCertificateInfoRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewayCertificateInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCloudNativeAPIGatewayCertificateInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCloudNativeAPIGatewayCertificateInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCloudNativeAPIGatewaySpec(self, request):
        r"""修改云原生API网关实例的节点规格信息，例如节点扩缩容或者升降配

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
        r"""修改引擎公网访问配置

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


    def UpdateUpstreamHealthCheckConfig(self, request):
        r"""更新云原生网关健康检查配置

        :param request: Request instance for UpdateUpstreamHealthCheckConfig.
        :type request: :class:`tencentcloud.tse.v20201207.models.UpdateUpstreamHealthCheckConfigRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateUpstreamHealthCheckConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUpstreamHealthCheckConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUpstreamHealthCheckConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUpstreamTargets(self, request):
        r"""更新网关上游实例列表，仅支持IPList服务类型

        :param request: Request instance for UpdateUpstreamTargets.
        :type request: :class:`tencentcloud.tse.v20201207.models.UpdateUpstreamTargetsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateUpstreamTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUpstreamTargets", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUpstreamTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))