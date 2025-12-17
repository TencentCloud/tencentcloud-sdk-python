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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.tke.v20180525 import models
from typing import Dict


class TkeClient(AbstractClient):
    _apiVersion = '2018-05-25'
    _endpoint = 'tke.tencentcloudapi.com'
    _service = 'tke'

    async def AcquireClusterAdminRole(
            self,
            request: models.AcquireClusterAdminRoleRequest,
            opts: Dict = None,
    ) -> models.AcquireClusterAdminRoleResponse:
        """
        通过此接口，可以获取集群的tke:admin的ClusterRole，即管理员角色，可以用于CAM侧高权限的用户，通过CAM策略给予子账户此接口权限，进而可以通过此接口直接获取到kubernetes集群内的管理员角色。
        """
        
        kwargs = {}
        kwargs["action"] = "AcquireClusterAdminRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcquireClusterAdminRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddClusterCIDR(
            self,
            request: models.AddClusterCIDRRequest,
            opts: Dict = None,
    ) -> models.AddClusterCIDRResponse:
        """
        给GR集群增加可用的ClusterCIDR（开白才能使用此功能，如需要请联系我们）
        """
        
        kwargs = {}
        kwargs["action"] = "AddClusterCIDR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddClusterCIDRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddExistedInstances(
            self,
            request: models.AddExistedInstancesRequest,
            opts: Dict = None,
    ) -> models.AddExistedInstancesResponse:
        """
        添加已经存在的实例到集群
        """
        
        kwargs = {}
        kwargs["action"] = "AddExistedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddExistedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNodeToNodePool(
            self,
            request: models.AddNodeToNodePoolRequest,
            opts: Dict = None,
    ) -> models.AddNodeToNodePoolResponse:
        """
        将集群内节点移入节点池
        """
        
        kwargs = {}
        kwargs["action"] = "AddNodeToNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNodeToNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddVpcCniSubnets(
            self,
            request: models.AddVpcCniSubnetsRequest,
            opts: Dict = None,
    ) -> models.AddVpcCniSubnetsResponse:
        """
        针对VPC-CNI模式的集群，增加集群容器网络可使用的子网
        """
        
        kwargs = {}
        kwargs["action"] = "AddVpcCniSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddVpcCniSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelClusterRelease(
            self,
            request: models.CancelClusterReleaseRequest,
            opts: Dict = None,
    ) -> models.CancelClusterReleaseResponse:
        """
        在应用市场中取消安装失败的应用
        """
        
        kwargs = {}
        kwargs["action"] = "CancelClusterRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelClusterReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelUpgradePlan(
            self,
            request: models.CancelUpgradePlanRequest,
            opts: Dict = None,
    ) -> models.CancelUpgradePlanResponse:
        """
        取消升级计划
        """
        
        kwargs = {}
        kwargs["action"] = "CancelUpgradePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelUpgradePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckEdgeClusterCIDR(
            self,
            request: models.CheckEdgeClusterCIDRRequest,
            opts: Dict = None,
    ) -> models.CheckEdgeClusterCIDRResponse:
        """
        检查边缘计算集群的CIDR是否冲突
        """
        
        kwargs = {}
        kwargs["action"] = "CheckEdgeClusterCIDR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckEdgeClusterCIDRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckInstancesUpgradeAble(
            self,
            request: models.CheckInstancesUpgradeAbleRequest,
            opts: Dict = None,
    ) -> models.CheckInstancesUpgradeAbleResponse:
        """
        检查给定节点列表中哪些是可升级的
        """
        
        kwargs = {}
        kwargs["action"] = "CheckInstancesUpgradeAble"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckInstancesUpgradeAbleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupStorageLocation(
            self,
            request: models.CreateBackupStorageLocationRequest,
            opts: Dict = None,
    ) -> models.CreateBackupStorageLocationResponse:
        """
        创建备份仓库，指定了存储仓库类型（如COS）、COS桶地区、名称等信息，当前最多允许创建100个仓库， 注意此接口当前是全局接口，多个地域的TKE集群如果要备份到相同的备份仓库中，不需要重复创建备份仓库
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupStorageLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupStorageLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCLSLogConfig(
            self,
            request: models.CreateCLSLogConfigRequest,
            opts: Dict = None,
    ) -> models.CreateCLSLogConfigResponse:
        """
        创建日志采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCLSLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCLSLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        创建集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterEndpoint(
            self,
            request: models.CreateClusterEndpointRequest,
            opts: Dict = None,
    ) -> models.CreateClusterEndpointResponse:
        """
        创建集群访问端口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterEndpointVip(
            self,
            request: models.CreateClusterEndpointVipRequest,
            opts: Dict = None,
    ) -> models.CreateClusterEndpointVipResponse:
        """
        创建托管集群外网访问端口（不再维护，准备下线）请使用新接口：CreateClusterEndpoint
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterEndpointVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterEndpointVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterInstances(
            self,
            request: models.CreateClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateClusterInstancesResponse:
        """
        扩展(新建)集群节点
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterMaintenanceWindowAndExclusions(
            self,
            request: models.CreateClusterMaintenanceWindowAndExclusionsRequest,
            opts: Dict = None,
    ) -> models.CreateClusterMaintenanceWindowAndExclusionsResponse:
        """
        创建集群维护时间窗口和排除项
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterMaintenanceWindowAndExclusions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterMaintenanceWindowAndExclusionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterNodePool(
            self,
            request: models.CreateClusterNodePoolRequest,
            opts: Dict = None,
    ) -> models.CreateClusterNodePoolResponse:
        """
        创建节点池
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterRelease(
            self,
            request: models.CreateClusterReleaseRequest,
            opts: Dict = None,
    ) -> models.CreateClusterReleaseResponse:
        """
        集群创建应用
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterRoute(
            self,
            request: models.CreateClusterRouteRequest,
            opts: Dict = None,
    ) -> models.CreateClusterRouteResponse:
        """
        创建集群路由
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterRouteTable(
            self,
            request: models.CreateClusterRouteTableRequest,
            opts: Dict = None,
    ) -> models.CreateClusterRouteTableResponse:
        """
        创建集群路由表
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterVirtualNode(
            self,
            request: models.CreateClusterVirtualNodeRequest,
            opts: Dict = None,
    ) -> models.CreateClusterVirtualNodeResponse:
        """
        创建按量计费超级节点
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterVirtualNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterVirtualNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterVirtualNodePool(
            self,
            request: models.CreateClusterVirtualNodePoolRequest,
            opts: Dict = None,
    ) -> models.CreateClusterVirtualNodePoolResponse:
        """
        创建超级节点池
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterVirtualNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterVirtualNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateECMInstances(
            self,
            request: models.CreateECMInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateECMInstancesResponse:
        """
        创建边缘计算ECM机器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateECMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateECMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEKSCluster(
            self,
            request: models.CreateEKSClusterRequest,
            opts: Dict = None,
    ) -> models.CreateEKSClusterResponse:
        """
        创建弹性集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEKSCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEKSClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEKSContainerInstances(
            self,
            request: models.CreateEKSContainerInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateEKSContainerInstancesResponse:
        """
        创建容器实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEKSContainerInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEKSContainerInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdgeCVMInstances(
            self,
            request: models.CreateEdgeCVMInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateEdgeCVMInstancesResponse:
        """
        创建边缘容器CVM机器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdgeCVMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdgeCVMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdgeLogConfig(
            self,
            request: models.CreateEdgeLogConfigRequest,
            opts: Dict = None,
    ) -> models.CreateEdgeLogConfigResponse:
        """
        创建边缘集群日志采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdgeLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdgeLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEksLogConfig(
            self,
            request: models.CreateEksLogConfigRequest,
            opts: Dict = None,
    ) -> models.CreateEksLogConfigResponse:
        """
        为弹性集群创建日志采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEksLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEksLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalMaintenanceWindowAndExclusions(
            self,
            request: models.CreateGlobalMaintenanceWindowAndExclusionsRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalMaintenanceWindowAndExclusionsResponse:
        """
        创建全局维护时间窗口和排除项
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalMaintenanceWindowAndExclusions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalMaintenanceWindowAndExclusionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageCache(
            self,
            request: models.CreateImageCacheRequest,
            opts: Dict = None,
    ) -> models.CreateImageCacheResponse:
        """
        创建镜像缓存的接口。创建过程中，请勿删除EKSCI实例和云盘，否则镜像缓存将创建失败。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusAlertPolicy(
            self,
            request: models.CreatePrometheusAlertPolicyRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusAlertPolicyResponse:
        """
        创建告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusAlertPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusAlertPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusAlertRule(
            self,
            request: models.CreatePrometheusAlertRuleRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusAlertRuleResponse:
        """
        创建告警规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusClusterAgent(
            self,
            request: models.CreatePrometheusClusterAgentRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusClusterAgentResponse:
        """
        与云监控融合的2.0实例关联集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusClusterAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusClusterAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusConfig(
            self,
            request: models.CreatePrometheusConfigRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusConfigResponse:
        """
        创建集群采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusDashboard(
            self,
            request: models.CreatePrometheusDashboardRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusDashboardResponse:
        """
        创建grafana监控面板
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusGlobalNotification(
            self,
            request: models.CreatePrometheusGlobalNotificationRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusGlobalNotificationResponse:
        """
        创建全局告警通知渠道
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusGlobalNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusGlobalNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusRecordRuleYaml(
            self,
            request: models.CreatePrometheusRecordRuleYamlRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusRecordRuleYamlResponse:
        """
        创建聚合规则yaml方式
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusRecordRuleYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusRecordRuleYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusTemp(
            self,
            request: models.CreatePrometheusTempRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusTempResponse:
        """
        创建一个云原生Prometheus模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusTemp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusTempResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusTemplate(
            self,
            request: models.CreatePrometheusTemplateRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusTemplateResponse:
        """
        创建一个云原生Prometheus模板实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReservedInstances(
            self,
            request: models.CreateReservedInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateReservedInstancesResponse:
        """
        预留券实例的购买会预先扣除本次实例购买所需金额，在调用本接口前请确保账户余额充足。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReservedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReservedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRollOutSequence(
            self,
            request: models.CreateRollOutSequenceRequest,
            opts: Dict = None,
    ) -> models.CreateRollOutSequenceResponse:
        """
        创建集群发布序列
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRollOutSequence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRollOutSequenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTKEEdgeCluster(
            self,
            request: models.CreateTKEEdgeClusterRequest,
            opts: Dict = None,
    ) -> models.CreateTKEEdgeClusterResponse:
        """
        创建边缘计算集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTKEEdgeCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTKEEdgeClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAddon(
            self,
            request: models.DeleteAddonRequest,
            opts: Dict = None,
    ) -> models.DeleteAddonResponse:
        """
        删除一个addon
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAddon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAddonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackupStorageLocation(
            self,
            request: models.DeleteBackupStorageLocationRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupStorageLocationResponse:
        """
        删除备份仓库
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackupStorageLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupStorageLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        删除集群(YUNAPI V3版本)
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterAsGroups(
            self,
            request: models.DeleteClusterAsGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterAsGroupsResponse:
        """
        删除集群伸缩组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterAsGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterAsGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterEndpoint(
            self,
            request: models.DeleteClusterEndpointRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterEndpointResponse:
        """
        删除集群访问端口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterEndpointVip(
            self,
            request: models.DeleteClusterEndpointVipRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterEndpointVipResponse:
        """
        删除托管集群外网访问端口（老的方式，仅支持托管集群外网端口）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterEndpointVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterEndpointVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterInstances(
            self,
            request: models.DeleteClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterInstancesResponse:
        """
        删除集群中的实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterMaintenanceWindowAndExclusion(
            self,
            request: models.DeleteClusterMaintenanceWindowAndExclusionRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterMaintenanceWindowAndExclusionResponse:
        """
        删除集群维护时间窗口和排除项
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterMaintenanceWindowAndExclusion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterMaintenanceWindowAndExclusionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterNodePool(
            self,
            request: models.DeleteClusterNodePoolRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterNodePoolResponse:
        """
        删除节点池
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterRoute(
            self,
            request: models.DeleteClusterRouteRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterRouteResponse:
        """
        删除集群路由
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterRouteTable(
            self,
            request: models.DeleteClusterRouteTableRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterRouteTableResponse:
        """
        删除集群路由表
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterVirtualNode(
            self,
            request: models.DeleteClusterVirtualNodeRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterVirtualNodeResponse:
        """
        删除超级节点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterVirtualNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterVirtualNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterVirtualNodePool(
            self,
            request: models.DeleteClusterVirtualNodePoolRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterVirtualNodePoolResponse:
        """
        删除超级节点池
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterVirtualNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterVirtualNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteECMInstances(
            self,
            request: models.DeleteECMInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteECMInstancesResponse:
        """
        删除ECM实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteECMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteECMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEKSCluster(
            self,
            request: models.DeleteEKSClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteEKSClusterResponse:
        """
        删除弹性集群(yunapiv3)
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEKSCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEKSClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEKSContainerInstances(
            self,
            request: models.DeleteEKSContainerInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteEKSContainerInstancesResponse:
        """
        删除容器实例，可批量删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEKSContainerInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEKSContainerInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEdgeCVMInstances(
            self,
            request: models.DeleteEdgeCVMInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteEdgeCVMInstancesResponse:
        """
        删除边缘容器CVM实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEdgeCVMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEdgeCVMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEdgeClusterInstances(
            self,
            request: models.DeleteEdgeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteEdgeClusterInstancesResponse:
        """
        删除边缘计算实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEdgeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEdgeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalMaintenanceWindowAndExclusion(
            self,
            request: models.DeleteGlobalMaintenanceWindowAndExclusionRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalMaintenanceWindowAndExclusionResponse:
        """
        删除全集维护时间窗口和排除项
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalMaintenanceWindowAndExclusion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalMaintenanceWindowAndExclusionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageCaches(
            self,
            request: models.DeleteImageCachesRequest,
            opts: Dict = None,
    ) -> models.DeleteImageCachesResponse:
        """
        批量删除镜像缓存
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageCaches"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageCachesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogConfigs(
            self,
            request: models.DeleteLogConfigsRequest,
            opts: Dict = None,
    ) -> models.DeleteLogConfigsResponse:
        """
        删除集群内采集规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusAlertPolicy(
            self,
            request: models.DeletePrometheusAlertPolicyRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusAlertPolicyResponse:
        """
        删除2.0实例告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusAlertPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusAlertPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusAlertRule(
            self,
            request: models.DeletePrometheusAlertRuleRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusAlertRuleResponse:
        """
        删除告警规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusClusterAgent(
            self,
            request: models.DeletePrometheusClusterAgentRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusClusterAgentResponse:
        """
        解除TMP实例的集群关联
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusClusterAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusClusterAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusConfig(
            self,
            request: models.DeletePrometheusConfigRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusConfigResponse:
        """
        删除集群采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusRecordRuleYaml(
            self,
            request: models.DeletePrometheusRecordRuleYamlRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusRecordRuleYamlResponse:
        """
        删除聚合规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusRecordRuleYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusRecordRuleYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusTemp(
            self,
            request: models.DeletePrometheusTempRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusTempResponse:
        """
        删除一个云原生Prometheus配置模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusTemp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusTempResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusTempSync(
            self,
            request: models.DeletePrometheusTempSyncRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusTempSyncResponse:
        """
        解除模板同步，这将会删除目标中该模板所生产的配置，针对V2版本实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusTempSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusTempSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusTemplate(
            self,
            request: models.DeletePrometheusTemplateRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusTemplateResponse:
        """
        删除一个云原生Prometheus配置模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusTemplateSync(
            self,
            request: models.DeletePrometheusTemplateSyncRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusTemplateSyncResponse:
        """
        取消模板同步，这将会删除目标中该模板所生产的配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusTemplateSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusTemplateSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReservedInstances(
            self,
            request: models.DeleteReservedInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteReservedInstancesResponse:
        """
        预留券实例如符合退还规则，可通过本接口主动退还。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReservedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReservedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRollOutSequence(
            self,
            request: models.DeleteRollOutSequenceRequest,
            opts: Dict = None,
    ) -> models.DeleteRollOutSequenceResponse:
        """
        删除集群发布序列
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRollOutSequence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRollOutSequenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTKEEdgeCluster(
            self,
            request: models.DeleteTKEEdgeClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteTKEEdgeClusterResponse:
        """
        删除边缘计算集群
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTKEEdgeCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTKEEdgeClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddon(
            self,
            request: models.DescribeAddonRequest,
            opts: Dict = None,
    ) -> models.DescribeAddonResponse:
        """
        获取addon列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddonValues(
            self,
            request: models.DescribeAddonValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeAddonValuesResponse:
        """
        获取一个addon的参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddonValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddonValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableClusterVersion(
            self,
            request: models.DescribeAvailableClusterVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableClusterVersionResponse:
        """
        获取集群可以升级的所有版本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableClusterVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableClusterVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableTKEEdgeVersion(
            self,
            request: models.DescribeAvailableTKEEdgeVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableTKEEdgeVersionResponse:
        """
        边缘计算支持版本和k8s版本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableTKEEdgeVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableTKEEdgeVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupStorageLocations(
            self,
            request: models.DescribeBackupStorageLocationsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupStorageLocationsResponse:
        """
        查询备份仓库信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupStorageLocations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupStorageLocationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchModifyTagsStatus(
            self,
            request: models.DescribeBatchModifyTagsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchModifyTagsStatusResponse:
        """
        查询批量修改标签状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchModifyTagsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchModifyTagsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAsGroupOption(
            self,
            request: models.DescribeClusterAsGroupOptionRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAsGroupOptionResponse:
        """
        集群弹性伸缩配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAsGroupOption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAsGroupOptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAsGroups(
            self,
            request: models.DescribeClusterAsGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAsGroupsResponse:
        """
        集群关联的伸缩组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAsGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAsGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAuthenticationOptions(
            self,
            request: models.DescribeClusterAuthenticationOptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAuthenticationOptionsResponse:
        """
        查看集群认证配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAuthenticationOptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAuthenticationOptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAvailableExtraArgs(
            self,
            request: models.DescribeClusterAvailableExtraArgsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAvailableExtraArgsResponse:
        """
        查询集群可用的自定义参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAvailableExtraArgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAvailableExtraArgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterCommonNames(
            self,
            request: models.DescribeClusterCommonNamesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterCommonNamesResponse:
        """
        获取指定子账户在RBAC授权模式中对应kube-apiserver客户端证书的CommonName字段，如果没有客户端证书，将会签发一个，此接口有最大传入子账户数量上限，当前为50
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterCommonNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterCommonNamesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterControllers(
            self,
            request: models.DescribeClusterControllersRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterControllersResponse:
        """
        用于查询Kubernetes的各个原生控制器是否开启
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterControllers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterControllersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterEndpointStatus(
            self,
            request: models.DescribeClusterEndpointStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterEndpointStatusResponse:
        """
        查询集群访问端口状态(独立集群开启内网/外网访问，托管集群支持开启内网访问)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterEndpointStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterEndpointStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterEndpointVipStatus(
            self,
            request: models.DescribeClusterEndpointVipStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterEndpointVipStatusResponse:
        """
        查询集群开启端口流程状态(仅支持托管集群外网端口)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterEndpointVipStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterEndpointVipStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterEndpoints(
            self,
            request: models.DescribeClusterEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterEndpointsResponse:
        """
        获取集群的访问地址，包括内网地址，外网地址，外网域名，外网访问安全策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterExtraArgs(
            self,
            request: models.DescribeClusterExtraArgsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterExtraArgsResponse:
        """
        查询集群自定义参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterExtraArgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterExtraArgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInspectionResultsOverview(
            self,
            request: models.DescribeClusterInspectionResultsOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInspectionResultsOverviewResponse:
        """
        查询用户单个Region下的所有集群巡检结果概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInspectionResultsOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInspectionResultsOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInstances(
            self,
            request: models.DescribeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInstancesResponse:
        """
        查询集群下节点实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterKubeconfig(
            self,
            request: models.DescribeClusterKubeconfigRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterKubeconfigResponse:
        """
        获取集群的kubeconfig文件，不同子账户获取自己的kubeconfig文件，该文件中有每个子账户自己的kube-apiserver的客户端证书，默认首次调此接口时候创建客户端证书，时效20年，未授予任何权限，如果是集群所有者或者主账户，则默认是cluster-admin权限。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterKubeconfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterKubeconfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterLevelAttribute(
            self,
            request: models.DescribeClusterLevelAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterLevelAttributeResponse:
        """
        获取集群规模
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterLevelAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterLevelAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterLevelChangeRecords(
            self,
            request: models.DescribeClusterLevelChangeRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterLevelChangeRecordsResponse:
        """
        查询集群变配记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterLevelChangeRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterLevelChangeRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterMaintenanceWindowAndExclusions(
            self,
            request: models.DescribeClusterMaintenanceWindowAndExclusionsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterMaintenanceWindowAndExclusionsResponse:
        """
        获取集群维护时间窗口和排除项
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterMaintenanceWindowAndExclusions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterMaintenanceWindowAndExclusionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNodePoolDetail(
            self,
            request: models.DescribeClusterNodePoolDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNodePoolDetailResponse:
        """
        查询节点池详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNodePoolDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNodePoolDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNodePools(
            self,
            request: models.DescribeClusterNodePoolsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNodePoolsResponse:
        """
        查询节点池列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNodePools"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNodePoolsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterPendingReleases(
            self,
            request: models.DescribeClusterPendingReleasesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterPendingReleasesResponse:
        """
        在应用市场中查询正在安装中的应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterPendingReleases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterPendingReleasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterReleaseDetails(
            self,
            request: models.DescribeClusterReleaseDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterReleaseDetailsResponse:
        """
        查询通过应用市场安装的某个应用详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterReleaseDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterReleaseDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterReleaseHistory(
            self,
            request: models.DescribeClusterReleaseHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterReleaseHistoryResponse:
        """
        查询集群在应用市场中某个已安装应用的版本历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterReleaseHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterReleaseHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterReleases(
            self,
            request: models.DescribeClusterReleasesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterReleasesResponse:
        """
        查询集群在应用市场中已安装应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterReleases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterReleasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterRollOutSequenceTags(
            self,
            request: models.DescribeClusterRollOutSequenceTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterRollOutSequenceTagsResponse:
        """
        查询集群发布序列标签
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterRollOutSequenceTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterRollOutSequenceTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterRouteTables(
            self,
            request: models.DescribeClusterRouteTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterRouteTablesResponse:
        """
        查询集群路由表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterRoutes(
            self,
            request: models.DescribeClusterRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterRoutesResponse:
        """
        查询集群路由
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterSecurity(
            self,
            request: models.DescribeClusterSecurityRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterSecurityResponse:
        """
        集群的密钥信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterSecurity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterSecurityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterStatus(
            self,
            request: models.DescribeClusterStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterStatusResponse:
        """
        查看集群状态列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterVirtualNode(
            self,
            request: models.DescribeClusterVirtualNodeRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterVirtualNodeResponse:
        """
        查看超级节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterVirtualNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterVirtualNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterVirtualNodePools(
            self,
            request: models.DescribeClusterVirtualNodePoolsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterVirtualNodePoolsResponse:
        """
        查看超级节点池列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterVirtualNodePools"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterVirtualNodePoolsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        查询集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeControlPlaneLogs(
            self,
            request: models.DescribeControlPlaneLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeControlPlaneLogsResponse:
        """
        查询插件日志采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeControlPlaneLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeControlPlaneLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeECMInstances(
            self,
            request: models.DescribeECMInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeECMInstancesResponse:
        """
        获取ECM实例相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeECMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeECMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEKSClusterCredential(
            self,
            request: models.DescribeEKSClusterCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeEKSClusterCredentialResponse:
        """
        获取弹性容器集群的接入认证信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEKSClusterCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEKSClusterCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEKSClusters(
            self,
            request: models.DescribeEKSClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeEKSClustersResponse:
        """
        查询弹性集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEKSClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEKSClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEKSContainerInstanceEvent(
            self,
            request: models.DescribeEKSContainerInstanceEventRequest,
            opts: Dict = None,
    ) -> models.DescribeEKSContainerInstanceEventResponse:
        """
        查询容器实例的事件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEKSContainerInstanceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEKSContainerInstanceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEKSContainerInstanceRegions(
            self,
            request: models.DescribeEKSContainerInstanceRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeEKSContainerInstanceRegionsResponse:
        """
        查询容器实例支持的地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEKSContainerInstanceRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEKSContainerInstanceRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEKSContainerInstances(
            self,
            request: models.DescribeEKSContainerInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeEKSContainerInstancesResponse:
        """
        查询容器实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEKSContainerInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEKSContainerInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeAvailableExtraArgs(
            self,
            request: models.DescribeEdgeAvailableExtraArgsRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeAvailableExtraArgsResponse:
        """
        查询边缘容器集群可用的自定义参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeAvailableExtraArgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeAvailableExtraArgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeCVMInstances(
            self,
            request: models.DescribeEdgeCVMInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeCVMInstancesResponse:
        """
        获取边缘容器CVM实例相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeCVMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeCVMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeClusterExtraArgs(
            self,
            request: models.DescribeEdgeClusterExtraArgsRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeClusterExtraArgsResponse:
        """
        查询边缘集群自定义参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeClusterExtraArgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeClusterExtraArgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeClusterInstances(
            self,
            request: models.DescribeEdgeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeClusterInstancesResponse:
        """
        查询边缘计算集群的节点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeClusterUpgradeInfo(
            self,
            request: models.DescribeEdgeClusterUpgradeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeClusterUpgradeInfoResponse:
        """
        可以查询边缘集群升级信息，包含可以升级的组件，当前升级状态和升级错误信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeClusterUpgradeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeClusterUpgradeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeLogSwitches(
            self,
            request: models.DescribeEdgeLogSwitchesRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeLogSwitchesResponse:
        """
        获取事件、审计和日志的状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeLogSwitches"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeLogSwitchesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEksContainerInstanceLog(
            self,
            request: models.DescribeEksContainerInstanceLogRequest,
            opts: Dict = None,
    ) -> models.DescribeEksContainerInstanceLogResponse:
        """
        查询容器实例中容器日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEksContainerInstanceLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEksContainerInstanceLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnableVpcCniProgress(
            self,
            request: models.DescribeEnableVpcCniProgressRequest,
            opts: Dict = None,
    ) -> models.DescribeEnableVpcCniProgressResponse:
        """
        本接口用于查询开启vpc-cni模式的任务进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnableVpcCniProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnableVpcCniProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEncryptionStatus(
            self,
            request: models.DescribeEncryptionStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeEncryptionStatusResponse:
        """
        查询etcd数据是否进行加密
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEncryptionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEncryptionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExistedInstances(
            self,
            request: models.DescribeExistedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeExistedInstancesResponse:
        """
        查询已经存在的节点，判断是否可以加入集群
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExistedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExistedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExternalNodeSupportConfig(
            self,
            request: models.DescribeExternalNodeSupportConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeExternalNodeSupportConfigResponse:
        """
        查看开启第三方节点池配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExternalNodeSupportConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExternalNodeSupportConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalMaintenanceWindowAndExclusions(
            self,
            request: models.DescribeGlobalMaintenanceWindowAndExclusionsRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalMaintenanceWindowAndExclusionsResponse:
        """
        获取全局维护时间窗口和排除项
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalMaintenanceWindowAndExclusions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalMaintenanceWindowAndExclusionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPAMD(
            self,
            request: models.DescribeIPAMDRequest,
            opts: Dict = None,
    ) -> models.DescribeIPAMDResponse:
        """
        获取eniipamd组件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPAMD"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPAMDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageCaches(
            self,
            request: models.DescribeImageCachesRequest,
            opts: Dict = None,
    ) -> models.DescribeImageCachesResponse:
        """
        查询镜像缓存信息接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageCaches"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageCachesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImages(
            self,
            request: models.DescribeImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeImagesResponse:
        """
        获取镜像信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogConfigs(
            self,
            request: models.DescribeLogConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogConfigsResponse:
        """
        查询日志采集规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogSwitches(
            self,
            request: models.DescribeLogSwitchesRequest,
            opts: Dict = None,
    ) -> models.DescribeLogSwitchesResponse:
        """
        查询集群日志（审计、事件、普通日志）开关列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogSwitches"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogSwitchesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMasterComponent(
            self,
            request: models.DescribeMasterComponentRequest,
            opts: Dict = None,
    ) -> models.DescribeMasterComponentResponse:
        """
        进行master组件停机故障演练时，获取master组件运行状态，支持kube-apiserver、kube-scheduler、kube-controller-manager
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMasterComponent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMasterComponentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOSImages(
            self,
            request: models.DescribeOSImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeOSImagesResponse:
        """
        获取OS聚合信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOSImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOSImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpenPolicyList(
            self,
            request: models.DescribeOpenPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeOpenPolicyListResponse:
        """
        查询opa策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpenPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpenPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePodChargeInfo(
            self,
            request: models.DescribePodChargeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePodChargeInfoResponse:
        """
        查询正在运行中Pod的计费信息。可以通过 Namespace 和 Name 来查询某个 Pod 的信息，也可以通过 Pod 的 Uid 批量查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePodChargeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePodChargeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePodDeductionRate(
            self,
            request: models.DescribePodDeductionRateRequest,
            opts: Dict = None,
    ) -> models.DescribePodDeductionRateResponse:
        """
        查询各个规格的 Pod 的抵扣率
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePodDeductionRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePodDeductionRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePodsBySpec(
            self,
            request: models.DescribePodsBySpecRequest,
            opts: Dict = None,
    ) -> models.DescribePodsBySpecResponse:
        """
        查询可以用预留券抵扣的 Pod 信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePodsBySpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePodsBySpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePostNodeResources(
            self,
            request: models.DescribePostNodeResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribePostNodeResourcesResponse:
        """
        包括 Pod 资源统计和绑定的预留券资源统计。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePostNodeResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePostNodeResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusAgentInstances(
            self,
            request: models.DescribePrometheusAgentInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusAgentInstancesResponse:
        """
        获取关联目标集群的实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAgentInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAgentInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusAgents(
            self,
            request: models.DescribePrometheusAgentsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusAgentsResponse:
        """
        获取被关联集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAgents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAgentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusAlertHistory(
            self,
            request: models.DescribePrometheusAlertHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusAlertHistoryResponse:
        """
        获取告警历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAlertHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAlertHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusAlertPolicy(
            self,
            request: models.DescribePrometheusAlertPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusAlertPolicyResponse:
        """
        获取2.0实例告警策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAlertPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAlertPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusAlertRule(
            self,
            request: models.DescribePrometheusAlertRuleRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusAlertRuleResponse:
        """
        获取告警规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusClusterAgents(
            self,
            request: models.DescribePrometheusClusterAgentsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusClusterAgentsResponse:
        """
        获取TMP实例关联集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusClusterAgents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusClusterAgentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusConfig(
            self,
            request: models.DescribePrometheusConfigRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusConfigResponse:
        """
        获取集群采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusGlobalConfig(
            self,
            request: models.DescribePrometheusGlobalConfigRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusGlobalConfigResponse:
        """
        获得实例级别抓取配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusGlobalConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusGlobalConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusGlobalNotification(
            self,
            request: models.DescribePrometheusGlobalNotificationRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusGlobalNotificationResponse:
        """
        查询全局告警通知渠道
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusGlobalNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusGlobalNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstance(
            self,
            request: models.DescribePrometheusInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstanceResponse:
        """
        获取实例详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstanceInitStatus(
            self,
            request: models.DescribePrometheusInstanceInitStatusRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstanceInitStatusResponse:
        """
        获取2.0实例初始化任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstanceInitStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstanceInitStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstancesOverview(
            self,
            request: models.DescribePrometheusInstancesOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstancesOverviewResponse:
        """
        获取与云监控融合实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstancesOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstancesOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusOverviews(
            self,
            request: models.DescribePrometheusOverviewsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusOverviewsResponse:
        """
        获取实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusOverviews"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusOverviewsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusRecordRules(
            self,
            request: models.DescribePrometheusRecordRulesRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusRecordRulesResponse:
        """
        获取聚合规则列表，包含关联集群内crd资源创建的record rule
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusRecordRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusRecordRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusTargets(
            self,
            request: models.DescribePrometheusTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusTargetsResponse:
        """
        获取targets信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusTemp(
            self,
            request: models.DescribePrometheusTempRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusTempResponse:
        """
        拉取模板列表，默认模板将总是在最前面
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusTemp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusTempResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusTempSync(
            self,
            request: models.DescribePrometheusTempSyncRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusTempSyncResponse:
        """
        获取模板关联实例信息，针对V2版本实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusTempSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusTempSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusTemplateSync(
            self,
            request: models.DescribePrometheusTemplateSyncRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusTemplateSyncResponse:
        """
        获取模板同步信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusTemplateSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusTemplateSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusTemplates(
            self,
            request: models.DescribePrometheusTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusTemplatesResponse:
        """
        拉取模板列表，默认模板将总是在最前面
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRIUtilizationDetail(
            self,
            request: models.DescribeRIUtilizationDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRIUtilizationDetailResponse:
        """
        预留实例用量查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRIUtilizationDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRIUtilizationDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        获取容器服务支持的所有地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReservedInstanceUtilizationRate(
            self,
            request: models.DescribeReservedInstanceUtilizationRateRequest,
            opts: Dict = None,
    ) -> models.DescribeReservedInstanceUtilizationRateResponse:
        """
        查询各种规格类型的预留券使用率
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReservedInstanceUtilizationRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReservedInstanceUtilizationRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReservedInstances(
            self,
            request: models.DescribeReservedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeReservedInstancesResponse:
        """
        查询预留实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReservedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReservedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceUsage(
            self,
            request: models.DescribeResourceUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceUsageResponse:
        """
        获取集群资源使用量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRollOutSequences(
            self,
            request: models.DescribeRollOutSequencesRequest,
            opts: Dict = None,
    ) -> models.DescribeRollOutSequencesResponse:
        """
        查询集群发布序列
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRollOutSequences"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRollOutSequencesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteTableConflicts(
            self,
            request: models.DescribeRouteTableConflictsRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteTableConflictsResponse:
        """
        查询路由表冲突列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteTableConflicts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteTableConflictsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportedRuntime(
            self,
            request: models.DescribeSupportedRuntimeRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportedRuntimeResponse:
        """
        根据K8S版本获取可选运行时版本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportedRuntime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportedRuntimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTKEEdgeClusterCredential(
            self,
            request: models.DescribeTKEEdgeClusterCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeTKEEdgeClusterCredentialResponse:
        """
        获取边缘计算集群的认证信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTKEEdgeClusterCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTKEEdgeClusterCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTKEEdgeClusterStatus(
            self,
            request: models.DescribeTKEEdgeClusterStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTKEEdgeClusterStatusResponse:
        """
        获取边缘计算集群的当前状态以及过程信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTKEEdgeClusterStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTKEEdgeClusterStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTKEEdgeClusters(
            self,
            request: models.DescribeTKEEdgeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeTKEEdgeClustersResponse:
        """
        查询边缘集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTKEEdgeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTKEEdgeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTKEEdgeExternalKubeconfig(
            self,
            request: models.DescribeTKEEdgeExternalKubeconfigRequest,
            opts: Dict = None,
    ) -> models.DescribeTKEEdgeExternalKubeconfigResponse:
        """
        获取边缘计算外部访问的kubeconfig
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTKEEdgeExternalKubeconfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTKEEdgeExternalKubeconfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTKEEdgeScript(
            self,
            request: models.DescribeTKEEdgeScriptRequest,
            opts: Dict = None,
    ) -> models.DescribeTKEEdgeScriptResponse:
        """
        获取边缘脚本链接，此接口用于添加第三方节点，通过下载脚本从而将节点添加到边缘集群。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTKEEdgeScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTKEEdgeScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        查询任务相关信息，只会查询对应任务类型的最新的一条任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpgradeTaskDetail(
            self,
            request: models.DescribeUpgradeTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeUpgradeTaskDetailResponse:
        """
        查询计划升级任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpgradeTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpgradeTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpgradeTasks(
            self,
            request: models.DescribeUpgradeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeUpgradeTasksResponse:
        """
        查询计划升级任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpgradeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpgradeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVersions(
            self,
            request: models.DescribeVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeVersionsResponse:
        """
        获取集群版本信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcCniPodLimits(
            self,
            request: models.DescribeVpcCniPodLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcCniPodLimitsResponse:
        """
        本接口查询当前用户和地域在指定可用区下的机型可支持的最大 TKE VPC-CNI 网络模式的 Pod 数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcCniPodLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcCniPodLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableClusterAudit(
            self,
            request: models.DisableClusterAuditRequest,
            opts: Dict = None,
    ) -> models.DisableClusterAuditResponse:
        """
        关闭集群审计
        """
        
        kwargs = {}
        kwargs["action"] = "DisableClusterAudit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableClusterAuditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableClusterDeletionProtection(
            self,
            request: models.DisableClusterDeletionProtectionRequest,
            opts: Dict = None,
    ) -> models.DisableClusterDeletionProtectionResponse:
        """
        关闭集群删除保护
        """
        
        kwargs = {}
        kwargs["action"] = "DisableClusterDeletionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableClusterDeletionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableControlPlaneLogs(
            self,
            request: models.DisableControlPlaneLogsRequest,
            opts: Dict = None,
    ) -> models.DisableControlPlaneLogsResponse:
        """
        删除插件日志采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "DisableControlPlaneLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableControlPlaneLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableEncryptionProtection(
            self,
            request: models.DisableEncryptionProtectionRequest,
            opts: Dict = None,
    ) -> models.DisableEncryptionProtectionResponse:
        """
        关闭加密信息保护
        """
        
        kwargs = {}
        kwargs["action"] = "DisableEncryptionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableEncryptionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableEventPersistence(
            self,
            request: models.DisableEventPersistenceRequest,
            opts: Dict = None,
    ) -> models.DisableEventPersistenceResponse:
        """
        关闭事件持久化功能
        """
        
        kwargs = {}
        kwargs["action"] = "DisableEventPersistence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableEventPersistenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableVpcCniNetworkType(
            self,
            request: models.DisableVpcCniNetworkTypeRequest,
            opts: Dict = None,
    ) -> models.DisableVpcCniNetworkTypeResponse:
        """
        提供给附加了VPC-CNI能力的Global-Route集群关闭VPC-CNI
        """
        
        kwargs = {}
        kwargs["action"] = "DisableVpcCniNetworkType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableVpcCniNetworkTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DrainClusterVirtualNode(
            self,
            request: models.DrainClusterVirtualNodeRequest,
            opts: Dict = None,
    ) -> models.DrainClusterVirtualNodeResponse:
        """
        驱逐超级节点
        """
        
        kwargs = {}
        kwargs["action"] = "DrainClusterVirtualNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DrainClusterVirtualNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableClusterAudit(
            self,
            request: models.EnableClusterAuditRequest,
            opts: Dict = None,
    ) -> models.EnableClusterAuditResponse:
        """
        开启集群审计
        """
        
        kwargs = {}
        kwargs["action"] = "EnableClusterAudit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableClusterAuditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableClusterDeletionProtection(
            self,
            request: models.EnableClusterDeletionProtectionRequest,
            opts: Dict = None,
    ) -> models.EnableClusterDeletionProtectionResponse:
        """
        启用集群删除保护
        """
        
        kwargs = {}
        kwargs["action"] = "EnableClusterDeletionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableClusterDeletionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableControlPlaneLogs(
            self,
            request: models.EnableControlPlaneLogsRequest,
            opts: Dict = None,
    ) -> models.EnableControlPlaneLogsResponse:
        """
        创建插件日志采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "EnableControlPlaneLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableControlPlaneLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableEncryptionProtection(
            self,
            request: models.EnableEncryptionProtectionRequest,
            opts: Dict = None,
    ) -> models.EnableEncryptionProtectionResponse:
        """
        开启加密数据保护，需要先开启KMS能力，完成KMS授权
        """
        
        kwargs = {}
        kwargs["action"] = "EnableEncryptionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableEncryptionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableEventPersistence(
            self,
            request: models.EnableEventPersistenceRequest,
            opts: Dict = None,
    ) -> models.EnableEventPersistenceResponse:
        """
        开启事件持久化功能
        """
        
        kwargs = {}
        kwargs["action"] = "EnableEventPersistence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableEventPersistenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableVpcCniNetworkType(
            self,
            request: models.EnableVpcCniNetworkTypeRequest,
            opts: Dict = None,
    ) -> models.EnableVpcCniNetworkTypeResponse:
        """
        GR集群可以通过本接口附加vpc-cni容器网络插件，开启vpc-cni容器网络能力
        """
        
        kwargs = {}
        kwargs["action"] = "EnableVpcCniNetworkType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableVpcCniNetworkTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForwardTKEEdgeApplicationRequestV3(
            self,
            request: models.ForwardTKEEdgeApplicationRequestV3Request,
            opts: Dict = None,
    ) -> models.ForwardTKEEdgeApplicationRequestV3Response:
        """
        操作TKEEdge集群的addon
        """
        
        kwargs = {}
        kwargs["action"] = "ForwardTKEEdgeApplicationRequestV3"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForwardTKEEdgeApplicationRequestV3Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetClusterLevelPrice(
            self,
            request: models.GetClusterLevelPriceRequest,
            opts: Dict = None,
    ) -> models.GetClusterLevelPriceResponse:
        """
        获取集群规模价格
        """
        
        kwargs = {}
        kwargs["action"] = "GetClusterLevelPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetClusterLevelPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMostSuitableImageCache(
            self,
            request: models.GetMostSuitableImageCacheRequest,
            opts: Dict = None,
    ) -> models.GetMostSuitableImageCacheResponse:
        """
        根据镜像列表，查询匹配的镜像缓存
        """
        
        kwargs = {}
        kwargs["action"] = "GetMostSuitableImageCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMostSuitableImageCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTkeAppChartList(
            self,
            request: models.GetTkeAppChartListRequest,
            opts: Dict = None,
    ) -> models.GetTkeAppChartListResponse:
        """
        获取TKE支持的App列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetTkeAppChartList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTkeAppChartListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUpgradeInstanceProgress(
            self,
            request: models.GetUpgradeInstanceProgressRequest,
            opts: Dict = None,
    ) -> models.GetUpgradeInstanceProgressResponse:
        """
        获得节点升级当前的进度，若集群未处于节点升级状态，则接口会报错：任务未找到。
        """
        
        kwargs = {}
        kwargs["action"] = "GetUpgradeInstanceProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUpgradeInstanceProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallAddon(
            self,
            request: models.InstallAddonRequest,
            opts: Dict = None,
    ) -> models.InstallAddonResponse:
        """
        为目标集群安装一个addon
        """
        
        kwargs = {}
        kwargs["action"] = "InstallAddon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallAddonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallEdgeLogAgent(
            self,
            request: models.InstallEdgeLogAgentRequest,
            opts: Dict = None,
    ) -> models.InstallEdgeLogAgentResponse:
        """
        在tke@edge集群的边缘节点上安装日志采集组件
        """
        
        kwargs = {}
        kwargs["action"] = "InstallEdgeLogAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallEdgeLogAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallLogAgent(
            self,
            request: models.InstallLogAgentRequest,
            opts: Dict = None,
    ) -> models.InstallLogAgentResponse:
        """
        在TKE集群中安装CLS日志采集组件
        """
        
        kwargs = {}
        kwargs["action"] = "InstallLogAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallLogAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListClusterInspectionResults(
            self,
            request: models.ListClusterInspectionResultsRequest,
            opts: Dict = None,
    ) -> models.ListClusterInspectionResultsResponse:
        """
        查询指定集群的巡检结果信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListClusterInspectionResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListClusterInspectionResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListClusterInspectionResultsItems(
            self,
            request: models.ListClusterInspectionResultsItemsRequest,
            opts: Dict = None,
    ) -> models.ListClusterInspectionResultsItemsResponse:
        """
        查询集群巡检结果历史列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListClusterInspectionResultsItems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListClusterInspectionResultsItemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterAsGroupAttribute(
            self,
            request: models.ModifyClusterAsGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterAsGroupAttributeResponse:
        """
        修改集群伸缩组属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterAsGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterAsGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterAsGroupOptionAttribute(
            self,
            request: models.ModifyClusterAsGroupOptionAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterAsGroupOptionAttributeResponse:
        """
        修改集群弹性伸缩属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterAsGroupOptionAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterAsGroupOptionAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterAttribute(
            self,
            request: models.ModifyClusterAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterAttributeResponse:
        """
        修改集群属性，至少选择一个参数更新
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterAuthenticationOptions(
            self,
            request: models.ModifyClusterAuthenticationOptionsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterAuthenticationOptionsResponse:
        """
        修改集群认证配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterAuthenticationOptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterAuthenticationOptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterEndpointSP(
            self,
            request: models.ModifyClusterEndpointSPRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterEndpointSPResponse:
        """
        修改托管集群外网端口的安全策略（老的方式，仅支持托管集群外网端口）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterEndpointSP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterEndpointSPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterExtraArgs(
            self,
            request: models.ModifyClusterExtraArgsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterExtraArgsResponse:
        """
        更新集群自定义参数，只支持托管集群
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterExtraArgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterExtraArgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterExtraArgsTaskState(
            self,
            request: models.ModifyClusterExtraArgsTaskStateRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterExtraArgsTaskStateResponse:
        """
        暂停或者取消集群更新参数任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterExtraArgsTaskState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterExtraArgsTaskStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterImage(
            self,
            request: models.ModifyClusterImageRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterImageResponse:
        """
        修改集群镜像
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterMaintenanceWindowAndExclusions(
            self,
            request: models.ModifyClusterMaintenanceWindowAndExclusionsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterMaintenanceWindowAndExclusionsResponse:
        """
        更新集群维护时间窗口和排除项
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterMaintenanceWindowAndExclusions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterMaintenanceWindowAndExclusionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterNodePool(
            self,
            request: models.ModifyClusterNodePoolRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterNodePoolResponse:
        """
        编辑节点池
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterRollOutSequenceTags(
            self,
            request: models.ModifyClusterRollOutSequenceTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterRollOutSequenceTagsResponse:
        """
        更新集群发布序列标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterRollOutSequenceTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterRollOutSequenceTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterRuntimeConfig(
            self,
            request: models.ModifyClusterRuntimeConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterRuntimeConfigResponse:
        """
        修改集群及节点池维度运行时配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterRuntimeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterRuntimeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterTags(
            self,
            request: models.ModifyClusterTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterTagsResponse:
        """
        修改集群标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterVirtualNodePool(
            self,
            request: models.ModifyClusterVirtualNodePoolRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterVirtualNodePoolResponse:
        """
        修改超级节点池
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterVirtualNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterVirtualNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalMaintenanceWindowAndExclusions(
            self,
            request: models.ModifyGlobalMaintenanceWindowAndExclusionsRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalMaintenanceWindowAndExclusionsResponse:
        """
        更新全局维护时间窗口和排除项
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalMaintenanceWindowAndExclusions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalMaintenanceWindowAndExclusionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMasterComponent(
            self,
            request: models.ModifyMasterComponentRequest,
            opts: Dict = None,
    ) -> models.ModifyMasterComponentResponse:
        """
        修改master组件，支持kube-apiserver、kube-scheduler、kube-controller-manager副本数调整为0和恢复
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMasterComponent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMasterComponentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNodePoolDesiredCapacityAboutAsg(
            self,
            request: models.ModifyNodePoolDesiredCapacityAboutAsgRequest,
            opts: Dict = None,
    ) -> models.ModifyNodePoolDesiredCapacityAboutAsgResponse:
        """
        修改节点池关联伸缩组的期望实例数
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNodePoolDesiredCapacityAboutAsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNodePoolDesiredCapacityAboutAsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNodePoolInstanceTypes(
            self,
            request: models.ModifyNodePoolInstanceTypesRequest,
            opts: Dict = None,
    ) -> models.ModifyNodePoolInstanceTypesResponse:
        """
        修改节点池的机型配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNodePoolInstanceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNodePoolInstanceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOpenPolicyList(
            self,
            request: models.ModifyOpenPolicyListRequest,
            opts: Dict = None,
    ) -> models.ModifyOpenPolicyListResponse:
        """
        批量修改opa策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOpenPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOpenPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusAgentExternalLabels(
            self,
            request: models.ModifyPrometheusAgentExternalLabelsRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusAgentExternalLabelsResponse:
        """
        修改被关联集群的external labels
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusAgentExternalLabels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusAgentExternalLabelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusAlertPolicy(
            self,
            request: models.ModifyPrometheusAlertPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusAlertPolicyResponse:
        """
        修改2.0实例告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusAlertPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusAlertPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusAlertRule(
            self,
            request: models.ModifyPrometheusAlertRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusAlertRuleResponse:
        """
        修改告警规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusConfig(
            self,
            request: models.ModifyPrometheusConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusConfigResponse:
        """
        修改集群采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusGlobalNotification(
            self,
            request: models.ModifyPrometheusGlobalNotificationRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusGlobalNotificationResponse:
        """
        修改全局告警通知渠道
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusGlobalNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusGlobalNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusRecordRuleYaml(
            self,
            request: models.ModifyPrometheusRecordRuleYamlRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusRecordRuleYamlResponse:
        """
        修改聚合规则yaml方式
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusRecordRuleYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusRecordRuleYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusTemp(
            self,
            request: models.ModifyPrometheusTempRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusTempResponse:
        """
        修改模板内容
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusTemp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusTempResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusTemplate(
            self,
            request: models.ModifyPrometheusTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusTemplateResponse:
        """
        修改模板内容
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReservedInstanceScope(
            self,
            request: models.ModifyReservedInstanceScopeRequest,
            opts: Dict = None,
    ) -> models.ModifyReservedInstanceScopeResponse:
        """
        修改预留券的抵扣范围，抵扣范围取值：Region、Zone 和 Node。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReservedInstanceScope"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReservedInstanceScopeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRollOutSequence(
            self,
            request: models.ModifyRollOutSequenceRequest,
            opts: Dict = None,
    ) -> models.ModifyRollOutSequenceResponse:
        """
        更新集群发布序列
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRollOutSequence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRollOutSequenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveNodeFromNodePool(
            self,
            request: models.RemoveNodeFromNodePoolRequest,
            opts: Dict = None,
    ) -> models.RemoveNodeFromNodePoolResponse:
        """
        移出节点池节点，但保留在集群内
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveNodeFromNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveNodeFromNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewReservedInstances(
            self,
            request: models.RenewReservedInstancesRequest,
            opts: Dict = None,
    ) -> models.RenewReservedInstancesResponse:
        """
        续费时请确保账户余额充足。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewReservedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewReservedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartEKSContainerInstances(
            self,
            request: models.RestartEKSContainerInstancesRequest,
            opts: Dict = None,
    ) -> models.RestartEKSContainerInstancesResponse:
        """
        重启弹性容器实例，支持批量操作
        """
        
        kwargs = {}
        kwargs["action"] = "RestartEKSContainerInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartEKSContainerInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackClusterRelease(
            self,
            request: models.RollbackClusterReleaseRequest,
            opts: Dict = None,
    ) -> models.RollbackClusterReleaseResponse:
        """
        在应用市场中集群回滚应用至某个历史版本
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackClusterRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackClusterReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunPrometheusInstance(
            self,
            request: models.RunPrometheusInstanceRequest,
            opts: Dict = None,
    ) -> models.RunPrometheusInstanceResponse:
        """
        初始化TMP实例，开启集成中心时调用
        """
        
        kwargs = {}
        kwargs["action"] = "RunPrometheusInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunPrometheusInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleInClusterMaster(
            self,
            request: models.ScaleInClusterMasterRequest,
            opts: Dict = None,
    ) -> models.ScaleInClusterMasterResponse:
        """
        缩容独立集群master节点，本功能为内测能力，使用之前请先提单联系我们。
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleInClusterMaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleInClusterMasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutClusterMaster(
            self,
            request: models.ScaleOutClusterMasterRequest,
            opts: Dict = None,
    ) -> models.ScaleOutClusterMasterResponse:
        """
        扩容独立集群master节点
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutClusterMaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutClusterMasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetNodePoolNodeProtection(
            self,
            request: models.SetNodePoolNodeProtectionRequest,
            opts: Dict = None,
    ) -> models.SetNodePoolNodeProtectionResponse:
        """
        仅能设置节点池中处于伸缩组的节点
        """
        
        kwargs = {}
        kwargs["action"] = "SetNodePoolNodeProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetNodePoolNodeProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchClusterEndpoint(
            self,
            request: models.SwitchClusterEndpointRequest,
            opts: Dict = None,
    ) -> models.SwitchClusterEndpointResponse:
        """
        切换集群网络访问链路为直连
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchClusterEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchClusterEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncPrometheusTemp(
            self,
            request: models.SyncPrometheusTempRequest,
            opts: Dict = None,
    ) -> models.SyncPrometheusTempResponse:
        """
        同步模板到实例或者集群，针对V2版本实例
        """
        
        kwargs = {}
        kwargs["action"] = "SyncPrometheusTemp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncPrometheusTempResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncPrometheusTemplate(
            self,
            request: models.SyncPrometheusTemplateRequest,
            opts: Dict = None,
    ) -> models.SyncPrometheusTemplateResponse:
        """
        同步模板到实例或者集群
        """
        
        kwargs = {}
        kwargs["action"] = "SyncPrometheusTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncPrometheusTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallClusterRelease(
            self,
            request: models.UninstallClusterReleaseRequest,
            opts: Dict = None,
    ) -> models.UninstallClusterReleaseResponse:
        """
        在应用市场中集群删除某个应用
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallClusterRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallClusterReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallEdgeLogAgent(
            self,
            request: models.UninstallEdgeLogAgentRequest,
            opts: Dict = None,
    ) -> models.UninstallEdgeLogAgentResponse:
        """
        从tke@edge集群边缘节点上卸载日志采集组件
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallEdgeLogAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallEdgeLogAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallLogAgent(
            self,
            request: models.UninstallLogAgentRequest,
            opts: Dict = None,
    ) -> models.UninstallLogAgentResponse:
        """
        从TKE集群中卸载CLS日志采集组件
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallLogAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallLogAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAddon(
            self,
            request: models.UpdateAddonRequest,
            opts: Dict = None,
    ) -> models.UpdateAddonResponse:
        """
        更新一个addon的参数和版本
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAddon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAddonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateClusterKubeconfig(
            self,
            request: models.UpdateClusterKubeconfigRequest,
            opts: Dict = None,
    ) -> models.UpdateClusterKubeconfigResponse:
        """
        对集群的Kubeconfig信息进行更新
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateClusterKubeconfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateClusterKubeconfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateClusterVersion(
            self,
            request: models.UpdateClusterVersionRequest,
            opts: Dict = None,
    ) -> models.UpdateClusterVersionResponse:
        """
        升级集群 Master 组件到指定版本
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateClusterVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateClusterVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEKSCluster(
            self,
            request: models.UpdateEKSClusterRequest,
            opts: Dict = None,
    ) -> models.UpdateEKSClusterResponse:
        """
        修改弹性集群名称等属性
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEKSCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEKSClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEKSContainerInstance(
            self,
            request: models.UpdateEKSContainerInstanceRequest,
            opts: Dict = None,
    ) -> models.UpdateEKSContainerInstanceResponse:
        """
        更新容器实例
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEKSContainerInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEKSContainerInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEdgeClusterVersion(
            self,
            request: models.UpdateEdgeClusterVersionRequest,
            opts: Dict = None,
    ) -> models.UpdateEdgeClusterVersionResponse:
        """
        升级边缘集群组件到指定版本，此版本为TKEEdge专用版本。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEdgeClusterVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEdgeClusterVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateImageCache(
            self,
            request: models.UpdateImageCacheRequest,
            opts: Dict = None,
    ) -> models.UpdateImageCacheResponse:
        """
        更新镜像缓存接口
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateImageCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateImageCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTKEEdgeCluster(
            self,
            request: models.UpdateTKEEdgeClusterRequest,
            opts: Dict = None,
    ) -> models.UpdateTKEEdgeClusterResponse:
        """
        修改边缘计算集群名称等属性
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTKEEdgeCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTKEEdgeClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeClusterInstances(
            self,
            request: models.UpgradeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.UpgradeClusterInstancesResponse:
        """
        给集群的一批work节点进行升级
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeClusterRelease(
            self,
            request: models.UpgradeClusterReleaseRequest,
            opts: Dict = None,
    ) -> models.UpgradeClusterReleaseResponse:
        """
        升级集群中已安装的应用
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeClusterRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeClusterReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)