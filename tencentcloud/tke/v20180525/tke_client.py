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
from tencentcloud.tke.v20180525 import models


class TkeClient(AbstractClient):
    _apiVersion = '2018-05-25'
    _endpoint = 'tke.tencentcloudapi.com'
    _service = 'tke'


    def AcquireClusterAdminRole(self, request):
        """通过此接口，可以获取集群的tke:admin的ClusterRole，即管理员角色，可以用于CAM侧高权限的用户，通过CAM策略给予子账户此接口权限，进而可以通过此接口直接获取到kubernetes集群内的管理员角色。

        :param request: Request instance for AcquireClusterAdminRole.
        :type request: :class:`tencentcloud.tke.v20180525.models.AcquireClusterAdminRoleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.AcquireClusterAdminRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcquireClusterAdminRole", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AcquireClusterAdminRoleResponse()
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


    def AddClusterCIDR(self, request):
        """给GR集群增加可用的ClusterCIDR

        :param request: Request instance for AddClusterCIDR.
        :type request: :class:`tencentcloud.tke.v20180525.models.AddClusterCIDRRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.AddClusterCIDRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddClusterCIDR", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddClusterCIDRResponse()
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


    def AddExistedInstances(self, request):
        """添加已经存在的实例到集群

        :param request: Request instance for AddExistedInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.AddExistedInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.AddExistedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddExistedInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddExistedInstancesResponse()
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


    def AddNodeToNodePool(self, request):
        """将集群内节点移入节点池

        :param request: Request instance for AddNodeToNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.AddNodeToNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.AddNodeToNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNodeToNodePool", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddNodeToNodePoolResponse()
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


    def AddVpcCniSubnets(self, request):
        """针对VPC-CNI模式的集群，增加集群容器网络可使用的子网

        :param request: Request instance for AddVpcCniSubnets.
        :type request: :class:`tencentcloud.tke.v20180525.models.AddVpcCniSubnetsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.AddVpcCniSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddVpcCniSubnets", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddVpcCniSubnetsResponse()
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


    def CheckEdgeClusterCIDR(self, request):
        """检查边缘计算集群的CIDR是否冲突

        :param request: Request instance for CheckEdgeClusterCIDR.
        :type request: :class:`tencentcloud.tke.v20180525.models.CheckEdgeClusterCIDRRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CheckEdgeClusterCIDRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckEdgeClusterCIDR", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckEdgeClusterCIDRResponse()
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


    def CheckInstancesUpgradeAble(self, request):
        """检查给定节点列表中哪些是可升级的

        :param request: Request instance for CheckInstancesUpgradeAble.
        :type request: :class:`tencentcloud.tke.v20180525.models.CheckInstancesUpgradeAbleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CheckInstancesUpgradeAbleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckInstancesUpgradeAble", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckInstancesUpgradeAbleResponse()
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


    def CreateCluster(self, request):
        """创建集群

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterResponse()
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


    def CreateClusterEndpoint(self, request):
        """创建集群访问端口

        :param request: Request instance for CreateClusterEndpoint.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterEndpointRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterEndpoint", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterEndpointResponse()
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


    def CreateClusterEndpointVip(self, request):
        """创建托管集群外网访问端口（老的方式，仅支持托管集群外网端口）

        :param request: Request instance for CreateClusterEndpointVip.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterEndpointVipRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterEndpointVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterEndpointVip", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterEndpointVipResponse()
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


    def CreateClusterInstances(self, request):
        """扩展(新建)集群节点

        :param request: Request instance for CreateClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterInstancesResponse()
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


    def CreateClusterNodePool(self, request):
        """创建节点池

        :param request: Request instance for CreateClusterNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterNodePool", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterNodePoolResponse()
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


    def CreateClusterNodePoolFromExistingAsg(self, request):
        """从伸缩组创建节点池

        :param request: Request instance for CreateClusterNodePoolFromExistingAsg.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterNodePoolFromExistingAsgRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterNodePoolFromExistingAsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterNodePoolFromExistingAsg", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterNodePoolFromExistingAsgResponse()
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


    def CreateClusterRelease(self, request):
        """在应用市场中给集群创建应用

        :param request: Request instance for CreateClusterRelease.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterReleaseRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterRelease", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterReleaseResponse()
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


    def CreateClusterRoute(self, request):
        """创建集群路由

        :param request: Request instance for CreateClusterRoute.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterRoute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterRouteResponse()
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


    def CreateClusterRouteTable(self, request):
        """创建集群路由表

        :param request: Request instance for CreateClusterRouteTable.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteTableRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterRouteTable", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterRouteTableResponse()
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


    def CreateECMInstances(self, request):
        """创建边缘计算ECM机器

        :param request: Request instance for CreateECMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateECMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateECMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateECMInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateECMInstancesResponse()
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


    def CreateEKSCluster(self, request):
        """创建弹性集群

        :param request: Request instance for CreateEKSCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateEKSClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateEKSClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEKSCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEKSClusterResponse()
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


    def CreateEKSContainerInstances(self, request):
        """创建容器实例

        :param request: Request instance for CreateEKSContainerInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateEKSContainerInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateEKSContainerInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEKSContainerInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEKSContainerInstancesResponse()
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


    def CreateEdgeCVMInstances(self, request):
        """创建边缘容器CVM机器

        :param request: Request instance for CreateEdgeCVMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateEdgeCVMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateEdgeCVMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeCVMInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEdgeCVMInstancesResponse()
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


    def CreateEdgeLogConfig(self, request):
        """创建边缘集群日志采集配置

        :param request: Request instance for CreateEdgeLogConfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateEdgeLogConfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateEdgeLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeLogConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEdgeLogConfigResponse()
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


    def CreateImageCache(self, request):
        """创建镜像缓存的接口。创建过程中，请勿删除EKSCI实例和云盘，否则镜像缓存将创建失败。

        :param request: Request instance for CreateImageCache.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateImageCacheRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateImageCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageCache", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImageCacheResponse()
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


    def CreatePrometheusAlertPolicy(self, request):
        """创建告警策略

        :param request: Request instance for CreatePrometheusAlertPolicy.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusAlertPolicyRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusAlertPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusAlertPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusAlertPolicyResponse()
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


    def CreatePrometheusAlertRule(self, request):
        """创建告警规则

        :param request: Request instance for CreatePrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusAlertRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusAlertRuleResponse()
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


    def CreatePrometheusClusterAgent(self, request):
        """与云监控融合的2.0实例关联集群

        :param request: Request instance for CreatePrometheusClusterAgent.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusClusterAgentRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusClusterAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusClusterAgent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusClusterAgentResponse()
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


    def CreatePrometheusConfig(self, request):
        """创建prometheus配置

        :param request: Request instance for CreatePrometheusConfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusConfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusConfigResponse()
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


    def CreatePrometheusDashboard(self, request):
        """创建grafana监控面板

        :param request: Request instance for CreatePrometheusDashboard.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusDashboardRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusDashboard", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusDashboardResponse()
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


    def CreatePrometheusGlobalNotification(self, request):
        """创建全局告警通知渠道

        :param request: Request instance for CreatePrometheusGlobalNotification.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusGlobalNotificationRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusGlobalNotificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusGlobalNotification", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusGlobalNotificationResponse()
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


    def CreatePrometheusRecordRuleYaml(self, request):
        """以Yaml的方式创建聚合规则

        :param request: Request instance for CreatePrometheusRecordRuleYaml.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusRecordRuleYamlRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusRecordRuleYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusRecordRuleYaml", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusRecordRuleYamlResponse()
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


    def CreatePrometheusTemp(self, request):
        """创建一个云原生Prometheus模板

        :param request: Request instance for CreatePrometheusTemp.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusTempRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusTempResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusTemp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusTempResponse()
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


    def CreatePrometheusTemplate(self, request):
        """创建一个云原生Prometheus模板实例

        :param request: Request instance for CreatePrometheusTemplate.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusTemplateRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusTemplateResponse()
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


    def CreateTKEEdgeCluster(self, request):
        """创建边缘计算集群

        :param request: Request instance for CreateTKEEdgeCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateTKEEdgeClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateTKEEdgeClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTKEEdgeCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTKEEdgeClusterResponse()
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


    def DeleteCluster(self, request):
        """删除集群(YUNAPI V3版本)

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterResponse()
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


    def DeleteClusterAsGroups(self, request):
        """删除集群伸缩组

        :param request: Request instance for DeleteClusterAsGroups.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterAsGroupsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterAsGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterAsGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterAsGroupsResponse()
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


    def DeleteClusterEndpoint(self, request):
        """删除集群访问端口

        :param request: Request instance for DeleteClusterEndpoint.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterEndpointRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterEndpoint", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterEndpointResponse()
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


    def DeleteClusterEndpointVip(self, request):
        """删除托管集群外网访问端口（老的方式，仅支持托管集群外网端口）

        :param request: Request instance for DeleteClusterEndpointVip.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterEndpointVipRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterEndpointVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterEndpointVip", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterEndpointVipResponse()
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


    def DeleteClusterInstances(self, request):
        """删除集群中的实例

        :param request: Request instance for DeleteClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterInstancesResponse()
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


    def DeleteClusterNodePool(self, request):
        """删除节点池

        :param request: Request instance for DeleteClusterNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterNodePool", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterNodePoolResponse()
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


    def DeleteClusterRoute(self, request):
        """删除集群路由

        :param request: Request instance for DeleteClusterRoute.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterRoute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterRouteResponse()
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


    def DeleteClusterRouteTable(self, request):
        """删除集群路由表

        :param request: Request instance for DeleteClusterRouteTable.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteTableRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterRouteTable", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterRouteTableResponse()
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


    def DeleteECMInstances(self, request):
        """删除ECM实例

        :param request: Request instance for DeleteECMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteECMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteECMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteECMInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteECMInstancesResponse()
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


    def DeleteEKSCluster(self, request):
        """删除弹性集群(yunapiv3)

        :param request: Request instance for DeleteEKSCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteEKSClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteEKSClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEKSCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEKSClusterResponse()
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


    def DeleteEKSContainerInstances(self, request):
        """删除容器实例，可批量删除

        :param request: Request instance for DeleteEKSContainerInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteEKSContainerInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteEKSContainerInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEKSContainerInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEKSContainerInstancesResponse()
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


    def DeleteEdgeCVMInstances(self, request):
        """删除边缘容器CVM实例

        :param request: Request instance for DeleteEdgeCVMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteEdgeCVMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteEdgeCVMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeCVMInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEdgeCVMInstancesResponse()
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


    def DeleteEdgeClusterInstances(self, request):
        """删除边缘计算实例

        :param request: Request instance for DeleteEdgeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteEdgeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteEdgeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeClusterInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEdgeClusterInstancesResponse()
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


    def DeleteImageCaches(self, request):
        """批量删除镜像缓存

        :param request: Request instance for DeleteImageCaches.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteImageCachesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteImageCachesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageCaches", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImageCachesResponse()
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


    def DeletePrometheusAlertPolicy(self, request):
        """删除2.0实例告警策略

        :param request: Request instance for DeletePrometheusAlertPolicy.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusAlertPolicyRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusAlertPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusAlertPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrometheusAlertPolicyResponse()
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


    def DeletePrometheusAlertRule(self, request):
        """删除告警规则

        :param request: Request instance for DeletePrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusAlertRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrometheusAlertRuleResponse()
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


    def DeletePrometheusClusterAgent(self, request):
        """解除TMP实例的集群关联

        :param request: Request instance for DeletePrometheusClusterAgent.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusClusterAgentRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusClusterAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusClusterAgent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrometheusClusterAgentResponse()
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


    def DeletePrometheusConfig(self, request):
        """删除Prometheus配置，如果目标不存在，将返回成功

        :param request: Request instance for DeletePrometheusConfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusConfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrometheusConfigResponse()
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


    def DeletePrometheusRecordRuleYaml(self, request):
        """删除聚合实例

        :param request: Request instance for DeletePrometheusRecordRuleYaml.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusRecordRuleYamlRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusRecordRuleYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusRecordRuleYaml", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrometheusRecordRuleYamlResponse()
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


    def DeletePrometheusTemp(self, request):
        """删除一个云原生Prometheus配置模板

        :param request: Request instance for DeletePrometheusTemp.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusTempRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusTempResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusTemp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrometheusTempResponse()
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


    def DeletePrometheusTempSync(self, request):
        """解除模板同步，这将会删除目标中该模板所生产的配置，针对V2版本实例

        :param request: Request instance for DeletePrometheusTempSync.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusTempSyncRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusTempSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusTempSync", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrometheusTempSyncResponse()
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


    def DeletePrometheusTemplate(self, request):
        """删除一个云原生Prometheus配置模板

        :param request: Request instance for DeletePrometheusTemplate.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusTemplateRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrometheusTemplateResponse()
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


    def DeletePrometheusTemplateSync(self, request):
        """取消模板同步，这将会删除目标中该模板所生产的配置

        :param request: Request instance for DeletePrometheusTemplateSync.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusTemplateSyncRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusTemplateSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusTemplateSync", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrometheusTemplateSyncResponse()
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


    def DeleteTKEEdgeCluster(self, request):
        """删除边缘计算集群

        :param request: Request instance for DeleteTKEEdgeCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteTKEEdgeClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteTKEEdgeClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTKEEdgeCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTKEEdgeClusterResponse()
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


    def DescribeAvailableClusterVersion(self, request):
        """获取集群可以升级的所有版本

        :param request: Request instance for DescribeAvailableClusterVersion.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeAvailableClusterVersionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeAvailableClusterVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableClusterVersion", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailableClusterVersionResponse()
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


    def DescribeAvailableTKEEdgeVersion(self, request):
        """边缘计算支持版本和k8s版本

        :param request: Request instance for DescribeAvailableTKEEdgeVersion.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeAvailableTKEEdgeVersionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeAvailableTKEEdgeVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableTKEEdgeVersion", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailableTKEEdgeVersionResponse()
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


    def DescribeClusterAsGroupOption(self, request):
        """集群弹性伸缩配置

        :param request: Request instance for DescribeClusterAsGroupOption.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAsGroupOptionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAsGroupOptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAsGroupOption", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterAsGroupOptionResponse()
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


    def DescribeClusterAsGroups(self, request):
        """集群关联的伸缩组列表

        :param request: Request instance for DescribeClusterAsGroups.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAsGroupsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAsGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAsGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterAsGroupsResponse()
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


    def DescribeClusterAuthenticationOptions(self, request):
        """查看集群认证配置

        :param request: Request instance for DescribeClusterAuthenticationOptions.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAuthenticationOptionsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAuthenticationOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAuthenticationOptions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterAuthenticationOptionsResponse()
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


    def DescribeClusterCommonNames(self, request):
        """获取指定子账户在RBAC授权模式中对应kube-apiserver客户端证书的CommonName字段，如果没有客户端证书，将会签发一个，此接口有最大传入子账户数量上限，当前为50

        :param request: Request instance for DescribeClusterCommonNames.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterCommonNamesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterCommonNamesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterCommonNames", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterCommonNamesResponse()
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


    def DescribeClusterControllers(self, request):
        """用于查询Kubernetes的各个原生控制器是否开启

        :param request: Request instance for DescribeClusterControllers.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterControllersRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterControllersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterControllers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterControllersResponse()
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


    def DescribeClusterEndpointStatus(self, request):
        """查询集群访问端口状态(独立集群开启内网/外网访问，托管集群支持开启内网访问)

        :param request: Request instance for DescribeClusterEndpointStatus.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointStatusRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterEndpointStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterEndpointStatusResponse()
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


    def DescribeClusterEndpointVipStatus(self, request):
        """查询集群开启端口流程状态(仅支持托管集群外网端口)

        :param request: Request instance for DescribeClusterEndpointVipStatus.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointVipStatusRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointVipStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterEndpointVipStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterEndpointVipStatusResponse()
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


    def DescribeClusterEndpoints(self, request):
        """获取集群的访问地址，包括内网地址，外网地址，外网域名，外网访问安全策略

        :param request: Request instance for DescribeClusterEndpoints.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterEndpoints", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterEndpointsResponse()
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


    def DescribeClusterInstances(self, request):
        """查询集群下节点实例信息

        :param request: Request instance for DescribeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterInstancesResponse()
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


    def DescribeClusterKubeconfig(self, request):
        """获取集群的kubeconfig文件，不同子账户获取自己的kubeconfig文件，该文件中有每个子账户自己的kube-apiserver的客户端证书，默认首次调此接口时候创建客户端证书，时效20年，未授予任何权限，如果是集群所有者或者主账户，则默认是cluster-admin权限。

        :param request: Request instance for DescribeClusterKubeconfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterKubeconfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterKubeconfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterKubeconfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterKubeconfigResponse()
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


    def DescribeClusterLevelAttribute(self, request):
        """获取集群规模

        :param request: Request instance for DescribeClusterLevelAttribute.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterLevelAttributeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterLevelAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterLevelAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterLevelAttributeResponse()
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


    def DescribeClusterLevelChangeRecords(self, request):
        """查询集群变配记录

        :param request: Request instance for DescribeClusterLevelChangeRecords.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterLevelChangeRecordsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterLevelChangeRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterLevelChangeRecords", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterLevelChangeRecordsResponse()
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


    def DescribeClusterNodePoolDetail(self, request):
        """查询节点池详情

        :param request: Request instance for DescribeClusterNodePoolDetail.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterNodePoolDetailRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterNodePoolDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodePoolDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterNodePoolDetailResponse()
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


    def DescribeClusterNodePools(self, request):
        """查询节点池列表

        :param request: Request instance for DescribeClusterNodePools.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterNodePoolsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterNodePoolsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodePools", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterNodePoolsResponse()
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


    def DescribeClusterRouteTables(self, request):
        """查询集群路由表

        :param request: Request instance for DescribeClusterRouteTables.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRouteTablesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterRouteTables", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterRouteTablesResponse()
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


    def DescribeClusterRoutes(self, request):
        """查询集群路由

        :param request: Request instance for DescribeClusterRoutes.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRoutesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterRoutes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterRoutesResponse()
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


    def DescribeClusterSecurity(self, request):
        """集群的密钥信息

        :param request: Request instance for DescribeClusterSecurity.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterSecurityRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterSecurityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterSecurity", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterSecurityResponse()
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


    def DescribeClusterStatus(self, request):
        """查看集群状态列表

        :param request: Request instance for DescribeClusterStatus.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterStatusRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterStatusResponse()
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


    def DescribeClusters(self, request):
        """查询集群列表

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClustersResponse()
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


    def DescribeECMInstances(self, request):
        """获取ECM实例相关信息

        :param request: Request instance for DescribeECMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeECMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeECMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeECMInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeECMInstancesResponse()
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


    def DescribeEKSClusterCredential(self, request):
        """获取弹性容器集群的接入认证信息

        :param request: Request instance for DescribeEKSClusterCredential.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEKSClusterCredentialRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEKSClusterCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEKSClusterCredential", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEKSClusterCredentialResponse()
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


    def DescribeEKSClusters(self, request):
        """查询弹性集群列表

        :param request: Request instance for DescribeEKSClusters.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEKSClustersRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEKSClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEKSClusters", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEKSClustersResponse()
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


    def DescribeEKSContainerInstanceEvent(self, request):
        """查询容器实例的事件

        :param request: Request instance for DescribeEKSContainerInstanceEvent.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEKSContainerInstanceEventRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEKSContainerInstanceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEKSContainerInstanceEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEKSContainerInstanceEventResponse()
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


    def DescribeEKSContainerInstanceRegions(self, request):
        """查询容器实例支持的地域

        :param request: Request instance for DescribeEKSContainerInstanceRegions.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEKSContainerInstanceRegionsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEKSContainerInstanceRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEKSContainerInstanceRegions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEKSContainerInstanceRegionsResponse()
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


    def DescribeEKSContainerInstances(self, request):
        """查询容器实例

        :param request: Request instance for DescribeEKSContainerInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEKSContainerInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEKSContainerInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEKSContainerInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEKSContainerInstancesResponse()
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


    def DescribeEdgeAvailableExtraArgs(self, request):
        """查询边缘容器集群可用的自定义参数

        :param request: Request instance for DescribeEdgeAvailableExtraArgs.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeAvailableExtraArgsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeAvailableExtraArgsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeAvailableExtraArgs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEdgeAvailableExtraArgsResponse()
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


    def DescribeEdgeCVMInstances(self, request):
        """获取边缘容器CVM实例相关信息

        :param request: Request instance for DescribeEdgeCVMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeCVMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeCVMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeCVMInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEdgeCVMInstancesResponse()
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


    def DescribeEdgeClusterExtraArgs(self, request):
        """查询边缘集群自定义参数

        :param request: Request instance for DescribeEdgeClusterExtraArgs.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterExtraArgsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterExtraArgsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeClusterExtraArgs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEdgeClusterExtraArgsResponse()
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


    def DescribeEdgeClusterInstances(self, request):
        """查询边缘计算集群的节点信息

        :param request: Request instance for DescribeEdgeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeClusterInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEdgeClusterInstancesResponse()
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


    def DescribeEdgeClusterUpgradeInfo(self, request):
        """可以查询边缘集群升级信息，包含可以升级的组件，当前升级状态和升级错误信息

        :param request: Request instance for DescribeEdgeClusterUpgradeInfo.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterUpgradeInfoRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterUpgradeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeClusterUpgradeInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEdgeClusterUpgradeInfoResponse()
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


    def DescribeEdgeLogSwitches(self, request):
        """获取事件、审计和日志的状态接口

        :param request: Request instance for DescribeEdgeLogSwitches.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeLogSwitchesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeLogSwitchesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeLogSwitches", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEdgeLogSwitchesResponse()
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


    def DescribeEksContainerInstanceLog(self, request):
        """查询容器实例中容器日志

        :param request: Request instance for DescribeEksContainerInstanceLog.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEksContainerInstanceLogRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEksContainerInstanceLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEksContainerInstanceLog", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEksContainerInstanceLogResponse()
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


    def DescribeEnableVpcCniProgress(self, request):
        """本接口用于查询开启vpc-cni模式的任务进度

        :param request: Request instance for DescribeEnableVpcCniProgress.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEnableVpcCniProgressRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEnableVpcCniProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnableVpcCniProgress", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnableVpcCniProgressResponse()
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


    def DescribeExistedInstances(self, request):
        """查询已经存在的节点，判断是否可以加入集群

        :param request: Request instance for DescribeExistedInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeExistedInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeExistedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExistedInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExistedInstancesResponse()
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


    def DescribeExternalClusterSpec(self, request):
        """获取导入第三方集群YAML定义

        :param request: Request instance for DescribeExternalClusterSpec.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeExternalClusterSpecRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeExternalClusterSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExternalClusterSpec", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExternalClusterSpecResponse()
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


    def DescribeImageCaches(self, request):
        """查询镜像缓存信息接口

        :param request: Request instance for DescribeImageCaches.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeImageCachesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeImageCachesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageCaches", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageCachesResponse()
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


    def DescribeImages(self, request):
        """获取镜像信息

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImages", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImagesResponse()
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


    def DescribePrometheusAgentInstances(self, request):
        """获取关联目标集群的实例列表

        :param request: Request instance for DescribePrometheusAgentInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAgentInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAgentInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusAgentInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusAgentInstancesResponse()
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


    def DescribePrometheusAgents(self, request):
        """获取被关联集群列表

        :param request: Request instance for DescribePrometheusAgents.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAgentsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAgentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusAgents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusAgentsResponse()
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


    def DescribePrometheusAlertHistory(self, request):
        """获取告警历史

        :param request: Request instance for DescribePrometheusAlertHistory.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAlertHistoryRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAlertHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusAlertHistory", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusAlertHistoryResponse()
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


    def DescribePrometheusAlertPolicy(self, request):
        """获取2.0实例告警策略列表

        :param request: Request instance for DescribePrometheusAlertPolicy.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAlertPolicyRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAlertPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusAlertPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusAlertPolicyResponse()
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


    def DescribePrometheusAlertRule(self, request):
        """获取告警规则列表

        :param request: Request instance for DescribePrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusAlertRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusAlertRuleResponse()
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


    def DescribePrometheusClusterAgents(self, request):
        """获取TMP实例关联集群列表

        :param request: Request instance for DescribePrometheusClusterAgents.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusClusterAgentsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusClusterAgentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusClusterAgents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusClusterAgentsResponse()
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


    def DescribePrometheusConfig(self, request):
        """拉取Prometheus配置

        :param request: Request instance for DescribePrometheusConfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusConfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusConfigResponse()
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


    def DescribePrometheusGlobalConfig(self, request):
        """获得实例级别抓取配置

        :param request: Request instance for DescribePrometheusGlobalConfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusGlobalConfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusGlobalConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusGlobalConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusGlobalConfigResponse()
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


    def DescribePrometheusGlobalNotification(self, request):
        """查询全局告警通知渠道

        :param request: Request instance for DescribePrometheusGlobalNotification.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusGlobalNotificationRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusGlobalNotificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusGlobalNotification", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusGlobalNotificationResponse()
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


    def DescribePrometheusInstance(self, request):
        """获取实例详细信息

        :param request: Request instance for DescribePrometheusInstance.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusInstanceRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusInstanceResponse()
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


    def DescribePrometheusInstanceInitStatus(self, request):
        """获取2.0实例初始化任务状态

        :param request: Request instance for DescribePrometheusInstanceInitStatus.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusInstanceInitStatusRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusInstanceInitStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusInstanceInitStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusInstanceInitStatusResponse()
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


    def DescribePrometheusInstancesOverview(self, request):
        """获取与云监控融合实例列表

        :param request: Request instance for DescribePrometheusInstancesOverview.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusInstancesOverviewRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusInstancesOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusInstancesOverview", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusInstancesOverviewResponse()
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


    def DescribePrometheusOverviews(self, request):
        """获取实例列表

        :param request: Request instance for DescribePrometheusOverviews.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusOverviewsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusOverviewsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusOverviews", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusOverviewsResponse()
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


    def DescribePrometheusRecordRules(self, request):
        """获取聚合规则列表，包含关联集群内crd资源创建的record rule

        :param request: Request instance for DescribePrometheusRecordRules.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusRecordRulesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusRecordRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusRecordRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusRecordRulesResponse()
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


    def DescribePrometheusTargets(self, request):
        """获取targets信息

        :param request: Request instance for DescribePrometheusTargets.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTargetsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusTargets", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusTargetsResponse()
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


    def DescribePrometheusTemp(self, request):
        """拉取模板列表，默认模板将总是在最前面

        :param request: Request instance for DescribePrometheusTemp.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTempRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTempResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusTemp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusTempResponse()
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


    def DescribePrometheusTempSync(self, request):
        """获取模板关联实例信息，针对V2版本实例

        :param request: Request instance for DescribePrometheusTempSync.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTempSyncRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTempSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusTempSync", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusTempSyncResponse()
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


    def DescribePrometheusTemplateSync(self, request):
        """获取模板同步信息

        :param request: Request instance for DescribePrometheusTemplateSync.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTemplateSyncRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTemplateSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusTemplateSync", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusTemplateSyncResponse()
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


    def DescribePrometheusTemplates(self, request):
        """拉取模板列表，默认模板将总是在最前面

        :param request: Request instance for DescribePrometheusTemplates.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTemplatesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusTemplates", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusTemplatesResponse()
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


    def DescribeRegions(self, request):
        """获取容器服务支持的所有地域

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def DescribeResourceUsage(self, request):
        """获取集群资源使用量

        :param request: Request instance for DescribeResourceUsage.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeResourceUsageRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeResourceUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceUsage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceUsageResponse()
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


    def DescribeRouteTableConflicts(self, request):
        """查询路由表冲突列表

        :param request: Request instance for DescribeRouteTableConflicts.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeRouteTableConflictsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeRouteTableConflictsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteTableConflicts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRouteTableConflictsResponse()
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


    def DescribeTKEEdgeClusterCredential(self, request):
        """获取边缘计算集群的认证信息

        :param request: Request instance for DescribeTKEEdgeClusterCredential.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClusterCredentialRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClusterCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTKEEdgeClusterCredential", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTKEEdgeClusterCredentialResponse()
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


    def DescribeTKEEdgeClusterStatus(self, request):
        """获取边缘计算集群的当前状态以及过程信息

        :param request: Request instance for DescribeTKEEdgeClusterStatus.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClusterStatusRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClusterStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTKEEdgeClusterStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTKEEdgeClusterStatusResponse()
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


    def DescribeTKEEdgeClusters(self, request):
        """查询边缘集群列表

        :param request: Request instance for DescribeTKEEdgeClusters.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClustersRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTKEEdgeClusters", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTKEEdgeClustersResponse()
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


    def DescribeTKEEdgeExternalKubeconfig(self, request):
        """获取边缘计算外部访问的kubeconfig

        :param request: Request instance for DescribeTKEEdgeExternalKubeconfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeExternalKubeconfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeExternalKubeconfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTKEEdgeExternalKubeconfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTKEEdgeExternalKubeconfigResponse()
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


    def DescribeTKEEdgeScript(self, request):
        """获取边缘脚本链接，此接口用于添加第三方节点，通过下载脚本从而将节点添加到边缘集群。

        :param request: Request instance for DescribeTKEEdgeScript.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeScriptRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTKEEdgeScript", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTKEEdgeScriptResponse()
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


    def DescribeVersions(self, request):
        """获取集群版本信息

        :param request: Request instance for DescribeVersions.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeVersionsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVersions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVersionsResponse()
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


    def DescribeVpcCniPodLimits(self, request):
        """本接口查询当前用户和地域在指定可用区下的机型可支持的最大 TKE VPC-CNI 网络模式的 Pod 数量

        :param request: Request instance for DescribeVpcCniPodLimits.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeVpcCniPodLimitsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeVpcCniPodLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcCniPodLimits", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcCniPodLimitsResponse()
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


    def DisableClusterAudit(self, request):
        """关闭集群审计

        :param request: Request instance for DisableClusterAudit.
        :type request: :class:`tencentcloud.tke.v20180525.models.DisableClusterAuditRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DisableClusterAuditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableClusterAudit", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableClusterAuditResponse()
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


    def DisableClusterDeletionProtection(self, request):
        """关闭集群删除保护

        :param request: Request instance for DisableClusterDeletionProtection.
        :type request: :class:`tencentcloud.tke.v20180525.models.DisableClusterDeletionProtectionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DisableClusterDeletionProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableClusterDeletionProtection", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableClusterDeletionProtectionResponse()
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


    def DisableEventPersistence(self, request):
        """关闭事件持久化功能

        :param request: Request instance for DisableEventPersistence.
        :type request: :class:`tencentcloud.tke.v20180525.models.DisableEventPersistenceRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DisableEventPersistenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableEventPersistence", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableEventPersistenceResponse()
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


    def DisableVpcCniNetworkType(self, request):
        """提供给附加了VPC-CNI能力的Global-Route集群关闭VPC-CNI

        :param request: Request instance for DisableVpcCniNetworkType.
        :type request: :class:`tencentcloud.tke.v20180525.models.DisableVpcCniNetworkTypeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DisableVpcCniNetworkTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableVpcCniNetworkType", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableVpcCniNetworkTypeResponse()
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


    def EnableClusterAudit(self, request):
        """开启集群审计

        :param request: Request instance for EnableClusterAudit.
        :type request: :class:`tencentcloud.tke.v20180525.models.EnableClusterAuditRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.EnableClusterAuditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableClusterAudit", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableClusterAuditResponse()
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


    def EnableClusterDeletionProtection(self, request):
        """启用集群删除保护

        :param request: Request instance for EnableClusterDeletionProtection.
        :type request: :class:`tencentcloud.tke.v20180525.models.EnableClusterDeletionProtectionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.EnableClusterDeletionProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableClusterDeletionProtection", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableClusterDeletionProtectionResponse()
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


    def EnableEventPersistence(self, request):
        """开启事件持久化功能

        :param request: Request instance for EnableEventPersistence.
        :type request: :class:`tencentcloud.tke.v20180525.models.EnableEventPersistenceRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.EnableEventPersistenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableEventPersistence", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableEventPersistenceResponse()
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


    def EnableVpcCniNetworkType(self, request):
        """GR集群可以通过本接口附加vpc-cni容器网络插件，开启vpc-cni容器网络能力

        :param request: Request instance for EnableVpcCniNetworkType.
        :type request: :class:`tencentcloud.tke.v20180525.models.EnableVpcCniNetworkTypeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.EnableVpcCniNetworkTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableVpcCniNetworkType", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableVpcCniNetworkTypeResponse()
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


    def ForwardApplicationRequestV3(self, request):
        """操作TKE集群的addon

        :param request: Request instance for ForwardApplicationRequestV3.
        :type request: :class:`tencentcloud.tke.v20180525.models.ForwardApplicationRequestV3Request`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ForwardApplicationRequestV3Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForwardApplicationRequestV3", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForwardApplicationRequestV3Response()
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


    def ForwardTKEEdgeApplicationRequestV3(self, request):
        """操作TKEEdge集群的addon

        :param request: Request instance for ForwardTKEEdgeApplicationRequestV3.
        :type request: :class:`tencentcloud.tke.v20180525.models.ForwardTKEEdgeApplicationRequestV3Request`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ForwardTKEEdgeApplicationRequestV3Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForwardTKEEdgeApplicationRequestV3", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForwardTKEEdgeApplicationRequestV3Response()
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


    def GetClusterLevelPrice(self, request):
        """获取集群规模价格

        :param request: Request instance for GetClusterLevelPrice.
        :type request: :class:`tencentcloud.tke.v20180525.models.GetClusterLevelPriceRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.GetClusterLevelPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetClusterLevelPrice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetClusterLevelPriceResponse()
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


    def GetMostSuitableImageCache(self, request):
        """根据镜像列表，查询匹配的镜像缓存

        :param request: Request instance for GetMostSuitableImageCache.
        :type request: :class:`tencentcloud.tke.v20180525.models.GetMostSuitableImageCacheRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.GetMostSuitableImageCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMostSuitableImageCache", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetMostSuitableImageCacheResponse()
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


    def GetTkeAppChartList(self, request):
        """获取TKE支持的App列表

        :param request: Request instance for GetTkeAppChartList.
        :type request: :class:`tencentcloud.tke.v20180525.models.GetTkeAppChartListRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.GetTkeAppChartListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTkeAppChartList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTkeAppChartListResponse()
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


    def GetUpgradeInstanceProgress(self, request):
        """获得节点升级当前的进度

        :param request: Request instance for GetUpgradeInstanceProgress.
        :type request: :class:`tencentcloud.tke.v20180525.models.GetUpgradeInstanceProgressRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.GetUpgradeInstanceProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUpgradeInstanceProgress", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUpgradeInstanceProgressResponse()
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


    def InstallEdgeLogAgent(self, request):
        """在tke@edge集群的边缘节点上安装日志采集组件

        :param request: Request instance for InstallEdgeLogAgent.
        :type request: :class:`tencentcloud.tke.v20180525.models.InstallEdgeLogAgentRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.InstallEdgeLogAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallEdgeLogAgent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InstallEdgeLogAgentResponse()
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


    def InstallLogAgent(self, request):
        """在TKE集群中安装CLS日志采集组件

        :param request: Request instance for InstallLogAgent.
        :type request: :class:`tencentcloud.tke.v20180525.models.InstallLogAgentRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.InstallLogAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallLogAgent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InstallLogAgentResponse()
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


    def ModifyClusterAsGroupAttribute(self, request):
        """修改集群伸缩组属性

        :param request: Request instance for ModifyClusterAsGroupAttribute.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAsGroupAttributeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAsGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterAsGroupAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterAsGroupAttributeResponse()
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


    def ModifyClusterAsGroupOptionAttribute(self, request):
        """修改集群弹性伸缩属性

        :param request: Request instance for ModifyClusterAsGroupOptionAttribute.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAsGroupOptionAttributeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAsGroupOptionAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterAsGroupOptionAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterAsGroupOptionAttributeResponse()
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


    def ModifyClusterAttribute(self, request):
        """修改集群属性

        :param request: Request instance for ModifyClusterAttribute.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAttributeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterAttributeResponse()
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


    def ModifyClusterAuthenticationOptions(self, request):
        """修改集群认证配置

        :param request: Request instance for ModifyClusterAuthenticationOptions.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAuthenticationOptionsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAuthenticationOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterAuthenticationOptions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterAuthenticationOptionsResponse()
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


    def ModifyClusterEndpointSP(self, request):
        """修改托管集群外网端口的安全策略（老的方式，仅支持托管集群外网端口）

        :param request: Request instance for ModifyClusterEndpointSP.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterEndpointSPRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterEndpointSPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterEndpointSP", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterEndpointSPResponse()
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


    def ModifyClusterNodePool(self, request):
        """编辑节点池

        :param request: Request instance for ModifyClusterNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterNodePool", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterNodePoolResponse()
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


    def ModifyNodePoolDesiredCapacityAboutAsg(self, request):
        """修改节点池关联伸缩组的期望实例数

        :param request: Request instance for ModifyNodePoolDesiredCapacityAboutAsg.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyNodePoolDesiredCapacityAboutAsgRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyNodePoolDesiredCapacityAboutAsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNodePoolDesiredCapacityAboutAsg", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNodePoolDesiredCapacityAboutAsgResponse()
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


    def ModifyNodePoolInstanceTypes(self, request):
        """修改节点池的机型配置

        :param request: Request instance for ModifyNodePoolInstanceTypes.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyNodePoolInstanceTypesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyNodePoolInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNodePoolInstanceTypes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNodePoolInstanceTypesResponse()
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


    def ModifyPrometheusAgentExternalLabels(self, request):
        """修改被关联集群的external labels

        :param request: Request instance for ModifyPrometheusAgentExternalLabels.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusAgentExternalLabelsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusAgentExternalLabelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusAgentExternalLabels", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrometheusAgentExternalLabelsResponse()
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


    def ModifyPrometheusAlertPolicy(self, request):
        """修改2.0实例告警策略

        :param request: Request instance for ModifyPrometheusAlertPolicy.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusAlertPolicyRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusAlertPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusAlertPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrometheusAlertPolicyResponse()
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


    def ModifyPrometheusAlertRule(self, request):
        """修改告警规则

        :param request: Request instance for ModifyPrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusAlertRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrometheusAlertRuleResponse()
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


    def ModifyPrometheusConfig(self, request):
        """修改prometheus配置，如果配置项不存在，则会新增

        :param request: Request instance for ModifyPrometheusConfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusConfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrometheusConfigResponse()
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


    def ModifyPrometheusGlobalNotification(self, request):
        """修改全局告警通知渠道

        :param request: Request instance for ModifyPrometheusGlobalNotification.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusGlobalNotificationRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusGlobalNotificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusGlobalNotification", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrometheusGlobalNotificationResponse()
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


    def ModifyPrometheusRecordRuleYaml(self, request):
        """通过yaml的方式修改Prometheus聚合实例

        :param request: Request instance for ModifyPrometheusRecordRuleYaml.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusRecordRuleYamlRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusRecordRuleYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusRecordRuleYaml", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrometheusRecordRuleYamlResponse()
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


    def ModifyPrometheusTemp(self, request):
        """修改模板内容

        :param request: Request instance for ModifyPrometheusTemp.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusTempRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusTempResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusTemp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrometheusTempResponse()
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


    def ModifyPrometheusTemplate(self, request):
        """修改模板内容

        :param request: Request instance for ModifyPrometheusTemplate.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusTemplateRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrometheusTemplateResponse()
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


    def RemoveNodeFromNodePool(self, request):
        """移出节点池节点，但保留在集群内

        :param request: Request instance for RemoveNodeFromNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.RemoveNodeFromNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.RemoveNodeFromNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveNodeFromNodePool", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveNodeFromNodePoolResponse()
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


    def RestartEKSContainerInstances(self, request):
        """重启弹性容器实例，支持批量操作

        :param request: Request instance for RestartEKSContainerInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.RestartEKSContainerInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.RestartEKSContainerInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartEKSContainerInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartEKSContainerInstancesResponse()
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


    def RunPrometheusInstance(self, request):
        """初始化TMP实例，开启集成中心时调用

        :param request: Request instance for RunPrometheusInstance.
        :type request: :class:`tencentcloud.tke.v20180525.models.RunPrometheusInstanceRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.RunPrometheusInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunPrometheusInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunPrometheusInstanceResponse()
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


    def ScaleInClusterMaster(self, request):
        """缩容独立集群master节点

        :param request: Request instance for ScaleInClusterMaster.
        :type request: :class:`tencentcloud.tke.v20180525.models.ScaleInClusterMasterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ScaleInClusterMasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleInClusterMaster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScaleInClusterMasterResponse()
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


    def ScaleOutClusterMaster(self, request):
        """扩容独立集群master节点

        :param request: Request instance for ScaleOutClusterMaster.
        :type request: :class:`tencentcloud.tke.v20180525.models.ScaleOutClusterMasterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ScaleOutClusterMasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutClusterMaster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScaleOutClusterMasterResponse()
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


    def SetNodePoolNodeProtection(self, request):
        """仅能设置节点池中处于伸缩组的节点

        :param request: Request instance for SetNodePoolNodeProtection.
        :type request: :class:`tencentcloud.tke.v20180525.models.SetNodePoolNodeProtectionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.SetNodePoolNodeProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetNodePoolNodeProtection", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetNodePoolNodeProtectionResponse()
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


    def SyncPrometheusTemp(self, request):
        """同步模板到实例或者集群，针对V2版本实例

        :param request: Request instance for SyncPrometheusTemp.
        :type request: :class:`tencentcloud.tke.v20180525.models.SyncPrometheusTempRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.SyncPrometheusTempResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncPrometheusTemp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncPrometheusTempResponse()
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


    def SyncPrometheusTemplate(self, request):
        """同步模板到实例或者集群

        :param request: Request instance for SyncPrometheusTemplate.
        :type request: :class:`tencentcloud.tke.v20180525.models.SyncPrometheusTemplateRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.SyncPrometheusTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncPrometheusTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncPrometheusTemplateResponse()
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


    def UninstallEdgeLogAgent(self, request):
        """从tke@edge集群边缘节点上卸载日志采集组件

        :param request: Request instance for UninstallEdgeLogAgent.
        :type request: :class:`tencentcloud.tke.v20180525.models.UninstallEdgeLogAgentRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UninstallEdgeLogAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallEdgeLogAgent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UninstallEdgeLogAgentResponse()
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


    def UninstallLogAgent(self, request):
        """从TKE集群中卸载CLS日志采集组件

        :param request: Request instance for UninstallLogAgent.
        :type request: :class:`tencentcloud.tke.v20180525.models.UninstallLogAgentRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UninstallLogAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallLogAgent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UninstallLogAgentResponse()
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


    def UpdateClusterVersion(self, request):
        """升级集群 Master 组件到指定版本

        :param request: Request instance for UpdateClusterVersion.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpdateClusterVersionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpdateClusterVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateClusterVersion", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateClusterVersionResponse()
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


    def UpdateEKSCluster(self, request):
        """修改弹性集群名称等属性

        :param request: Request instance for UpdateEKSCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpdateEKSClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpdateEKSClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEKSCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateEKSClusterResponse()
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


    def UpdateEKSContainerInstance(self, request):
        """更新容器实例

        :param request: Request instance for UpdateEKSContainerInstance.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpdateEKSContainerInstanceRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpdateEKSContainerInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEKSContainerInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateEKSContainerInstanceResponse()
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


    def UpdateEdgeClusterVersion(self, request):
        """升级边缘集群组件到指定版本，此版本为TKEEdge专用版本。

        :param request: Request instance for UpdateEdgeClusterVersion.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpdateEdgeClusterVersionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpdateEdgeClusterVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEdgeClusterVersion", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateEdgeClusterVersionResponse()
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


    def UpdateImageCache(self, request):
        """更新镜像缓存接口

        :param request: Request instance for UpdateImageCache.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpdateImageCacheRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpdateImageCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateImageCache", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateImageCacheResponse()
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


    def UpdateTKEEdgeCluster(self, request):
        """修改边缘计算集群名称等属性

        :param request: Request instance for UpdateTKEEdgeCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpdateTKEEdgeClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpdateTKEEdgeClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTKEEdgeCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateTKEEdgeClusterResponse()
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


    def UpgradeClusterInstances(self, request):
        """给集群的一批work节点进行升级

        :param request: Request instance for UpgradeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpgradeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpgradeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeClusterInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeClusterInstancesResponse()
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