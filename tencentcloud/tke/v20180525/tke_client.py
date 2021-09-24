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
            body = self.call("AcquireClusterAdminRole", params)
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
            body = self.call("AddClusterCIDR", params)
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
            body = self.call("AddExistedInstances", params)
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
            body = self.call("AddNodeToNodePool", params)
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
            body = self.call("AddVpcCniSubnets", params)
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


    def CheckInstancesUpgradeAble(self, request):
        """检查给定节点列表中哪些是可升级的

        :param request: Request instance for CheckInstancesUpgradeAble.
        :type request: :class:`tencentcloud.tke.v20180525.models.CheckInstancesUpgradeAbleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CheckInstancesUpgradeAbleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckInstancesUpgradeAble", params)
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
            body = self.call("CreateCluster", params)
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


    def CreateClusterAsGroup(self, request):
        """为已经存在的集群创建伸缩组

        :param request: Request instance for CreateClusterAsGroup.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterAsGroupRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterAsGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClusterAsGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterAsGroupResponse()
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
        """创建集群访问端口(独立集群开启内网/外网访问，托管集群支持开启内网访问)

        :param request: Request instance for CreateClusterEndpoint.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterEndpointRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterEndpointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClusterEndpoint", params)
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
            body = self.call("CreateClusterEndpointVip", params)
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
            body = self.call("CreateClusterInstances", params)
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
            body = self.call("CreateClusterNodePool", params)
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
            body = self.call("CreateClusterNodePoolFromExistingAsg", params)
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


    def CreateClusterRoute(self, request):
        """创建集群路由

        :param request: Request instance for CreateClusterRoute.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClusterRoute", params)
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
            body = self.call("CreateClusterRouteTable", params)
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


    def CreateEKSCluster(self, request):
        """创建弹性集群

        :param request: Request instance for CreateEKSCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateEKSClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateEKSClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEKSCluster", params)
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
            body = self.call("CreateEKSContainerInstances", params)
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


    def CreatePrometheusAlertRule(self, request):
        """创建告警规则

        :param request: Request instance for CreatePrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePrometheusAlertRule", params)
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


    def CreatePrometheusDashboard(self, request):
        """创建grafana监控面板

        :param request: Request instance for CreatePrometheusDashboard.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusDashboardRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusDashboardResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePrometheusDashboard", params)
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


    def CreatePrometheusTemplate(self, request):
        """创建一个云原生Prometheus模板实例

        :param request: Request instance for CreatePrometheusTemplate.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusTemplateRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePrometheusTemplate", params)
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


    def DeleteCluster(self, request):
        """删除集群(YUNAPI V3版本)

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCluster", params)
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
            body = self.call("DeleteClusterAsGroups", params)
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
        """删除集群访问端口(独立集群开启内网/外网访问，托管集群支持开启内网访问)

        :param request: Request instance for DeleteClusterEndpoint.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterEndpointRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterEndpointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteClusterEndpoint", params)
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
            body = self.call("DeleteClusterEndpointVip", params)
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
            body = self.call("DeleteClusterInstances", params)
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
            body = self.call("DeleteClusterNodePool", params)
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
            body = self.call("DeleteClusterRoute", params)
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
            body = self.call("DeleteClusterRouteTable", params)
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


    def DeleteEKSCluster(self, request):
        """删除弹性集群(yunapiv3)

        :param request: Request instance for DeleteEKSCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteEKSClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteEKSClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEKSCluster", params)
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
            body = self.call("DeleteEKSContainerInstances", params)
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


    def DeletePrometheusAlertRule(self, request):
        """删除告警规则

        :param request: Request instance for DeletePrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePrometheusAlertRule", params)
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


    def DeletePrometheusTemplate(self, request):
        """删除一个云原生Prometheus配置模板

        :param request: Request instance for DeletePrometheusTemplate.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusTemplateRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePrometheusTemplate", params)
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
            body = self.call("DeletePrometheusTemplateSync", params)
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


    def DescribeAvailableClusterVersion(self, request):
        """获取集群可以升级的所有版本

        :param request: Request instance for DescribeAvailableClusterVersion.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeAvailableClusterVersionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeAvailableClusterVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAvailableClusterVersion", params)
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


    def DescribeClusterAsGroupOption(self, request):
        """集群弹性伸缩配置

        :param request: Request instance for DescribeClusterAsGroupOption.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAsGroupOptionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAsGroupOptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterAsGroupOption", params)
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
            body = self.call("DescribeClusterAsGroups", params)
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


    def DescribeClusterCommonNames(self, request):
        """获取指定子账户在RBAC授权模式中对应kube-apiserver客户端证书的CommonName字段，如果没有客户端证书，将会签发一个，此接口有最大传入子账户数量上限，当前为50

        :param request: Request instance for DescribeClusterCommonNames.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterCommonNamesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterCommonNamesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterCommonNames", params)
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
            body = self.call("DescribeClusterControllers", params)
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
            body = self.call("DescribeClusterEndpointStatus", params)
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
            body = self.call("DescribeClusterEndpointVipStatus", params)
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


    def DescribeClusterInstances(self, request):
        """查询集群下节点实例信息

        :param request: Request instance for DescribeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterInstances", params)
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
            body = self.call("DescribeClusterKubeconfig", params)
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


    def DescribeClusterNodePoolDetail(self, request):
        """查询节点池详情

        :param request: Request instance for DescribeClusterNodePoolDetail.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterNodePoolDetailRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterNodePoolDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterNodePoolDetail", params)
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
            body = self.call("DescribeClusterNodePools", params)
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
            body = self.call("DescribeClusterRouteTables", params)
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
            body = self.call("DescribeClusterRoutes", params)
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
            body = self.call("DescribeClusterSecurity", params)
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


    def DescribeClusters(self, request):
        """查询集群列表

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusters", params)
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


    def DescribeEKSClusterCredential(self, request):
        """获取弹性容器集群的接入认证信息

        :param request: Request instance for DescribeEKSClusterCredential.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEKSClusterCredentialRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEKSClusterCredentialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEKSClusterCredential", params)
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
            body = self.call("DescribeEKSClusters", params)
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
            body = self.call("DescribeEKSContainerInstanceEvent", params)
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
            body = self.call("DescribeEKSContainerInstanceRegions", params)
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
            body = self.call("DescribeEKSContainerInstances", params)
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


    def DescribeEksContainerInstanceLog(self, request):
        """查询容器实例中容器日志

        :param request: Request instance for DescribeEksContainerInstanceLog.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEksContainerInstanceLogRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEksContainerInstanceLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEksContainerInstanceLog", params)
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
            body = self.call("DescribeEnableVpcCniProgress", params)
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
            body = self.call("DescribeExistedInstances", params)
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
            body = self.call("DescribeExternalClusterSpec", params)
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


    def DescribeImages(self, request):
        """获取镜像信息

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImages", params)
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
            body = self.call("DescribePrometheusAgentInstances", params)
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
            body = self.call("DescribePrometheusAgents", params)
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
            body = self.call("DescribePrometheusAlertHistory", params)
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


    def DescribePrometheusAlertRule(self, request):
        """获取告警规则列表

        :param request: Request instance for DescribePrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrometheusAlertRule", params)
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


    def DescribePrometheusInstance(self, request):
        """获取实例详细信息

        :param request: Request instance for DescribePrometheusInstance.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusInstanceRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrometheusInstance", params)
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


    def DescribePrometheusOverviews(self, request):
        """获取实例列表

        :param request: Request instance for DescribePrometheusOverviews.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusOverviewsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusOverviewsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrometheusOverviews", params)
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


    def DescribePrometheusTargets(self, request):
        """获取targets信息

        :param request: Request instance for DescribePrometheusTargets.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTargetsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrometheusTargets", params)
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


    def DescribePrometheusTemplateSync(self, request):
        """获取模板同步信息

        :param request: Request instance for DescribePrometheusTemplateSync.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTemplateSyncRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusTemplateSyncResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrometheusTemplateSync", params)
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
            body = self.call("DescribePrometheusTemplates", params)
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
            body = self.call("DescribeRegions", params)
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


    def DescribeRouteTableConflicts(self, request):
        """查询路由表冲突列表

        :param request: Request instance for DescribeRouteTableConflicts.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeRouteTableConflictsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeRouteTableConflictsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRouteTableConflicts", params)
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


    def DescribeVersions(self, request):
        """获取集群版本信息

        :param request: Request instance for DescribeVersions.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeVersionsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeVersionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVersions", params)
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
            body = self.call("DescribeVpcCniPodLimits", params)
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


    def DisableVpcCniNetworkType(self, request):
        """提供给附加了VPC-CNI能力的Global-Route集群关闭VPC-CNI

        :param request: Request instance for DisableVpcCniNetworkType.
        :type request: :class:`tencentcloud.tke.v20180525.models.DisableVpcCniNetworkTypeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DisableVpcCniNetworkTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableVpcCniNetworkType", params)
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


    def EnableVpcCniNetworkType(self, request):
        """GR集群可以通过本接口附加vpc-cni容器网络插件，开启vpc-cni容器网络能力

        :param request: Request instance for EnableVpcCniNetworkType.
        :type request: :class:`tencentcloud.tke.v20180525.models.EnableVpcCniNetworkTypeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.EnableVpcCniNetworkTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableVpcCniNetworkType", params)
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


    def GetUpgradeInstanceProgress(self, request):
        """获得节点升级当前的进度

        :param request: Request instance for GetUpgradeInstanceProgress.
        :type request: :class:`tencentcloud.tke.v20180525.models.GetUpgradeInstanceProgressRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.GetUpgradeInstanceProgressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetUpgradeInstanceProgress", params)
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


    def ModifyClusterAsGroupAttribute(self, request):
        """修改集群伸缩组属性

        :param request: Request instance for ModifyClusterAsGroupAttribute.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAsGroupAttributeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAsGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterAsGroupAttribute", params)
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
            body = self.call("ModifyClusterAsGroupOptionAttribute", params)
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
            body = self.call("ModifyClusterAttribute", params)
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


    def ModifyClusterEndpointSP(self, request):
        """修改托管集群外网端口的安全策略（老的方式，仅支持托管集群外网端口）

        :param request: Request instance for ModifyClusterEndpointSP.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterEndpointSPRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterEndpointSPResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterEndpointSP", params)
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
            body = self.call("ModifyClusterNodePool", params)
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
            body = self.call("ModifyNodePoolDesiredCapacityAboutAsg", params)
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
            body = self.call("ModifyNodePoolInstanceTypes", params)
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


    def ModifyPrometheusAlertRule(self, request):
        """修改告警规则

        :param request: Request instance for ModifyPrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPrometheusAlertRule", params)
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


    def ModifyPrometheusTemplate(self, request):
        """修改模板内容

        :param request: Request instance for ModifyPrometheusTemplate.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusTemplateRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPrometheusTemplate", params)
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
            body = self.call("RemoveNodeFromNodePool", params)
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
            body = self.call("RestartEKSContainerInstances", params)
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


    def SetNodePoolNodeProtection(self, request):
        """仅能设置节点池中处于伸缩组的节点

        :param request: Request instance for SetNodePoolNodeProtection.
        :type request: :class:`tencentcloud.tke.v20180525.models.SetNodePoolNodeProtectionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.SetNodePoolNodeProtectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetNodePoolNodeProtection", params)
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


    def SyncPrometheusTemplate(self, request):
        """同步模板到实例或者集群

        :param request: Request instance for SyncPrometheusTemplate.
        :type request: :class:`tencentcloud.tke.v20180525.models.SyncPrometheusTemplateRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.SyncPrometheusTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SyncPrometheusTemplate", params)
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


    def UpdateClusterVersion(self, request):
        """升级集群 Master 组件到指定版本

        :param request: Request instance for UpdateClusterVersion.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpdateClusterVersionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpdateClusterVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateClusterVersion", params)
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
            body = self.call("UpdateEKSCluster", params)
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
            body = self.call("UpdateEKSContainerInstance", params)
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


    def UpgradeClusterInstances(self, request):
        """给集群的一批work节点进行升级

        :param request: Request instance for UpgradeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpgradeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpgradeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeClusterInstances", params)
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