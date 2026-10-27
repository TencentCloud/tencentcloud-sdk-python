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
from tencentcloud.cvd.v20201104 import models
from typing import Dict


class CvdClient(AbstractClient):
    _apiVersion = '2020-11-04'
    _endpoint = 'cvd.tencentcloudapi.com'
    _service = 'cvd'

    async def AssociateSecurityGroup(
            self,
            request: models.AssociateSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupResponse:
        """
        安全组批量关联云桌面
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindInstances(
            self,
            request: models.BindInstancesRequest,
            opts: Dict = None,
    ) -> models.BindInstancesResponse:
        """
        绑定桌面
        """
        
        kwargs = {}
        kwargs["action"] = "BindInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCommandTask(
            self,
            request: models.CreateCommandTaskRequest,
            opts: Dict = None,
    ) -> models.CreateCommandTaskResponse:
        """
        创建批量脚本任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCommandTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCommandTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataDisk(
            self,
            request: models.CreateDataDiskRequest,
            opts: Dict = None,
    ) -> models.CreateDataDiskResponse:
        """
        实例新增数据盘
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainControlPolicy(
            self,
            request: models.CreateDomainControlPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateDomainControlPolicyResponse:
        """
        新建域名访问控制策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainControlPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainControlPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImage(
            self,
            request: models.CreateImageRequest,
            opts: Dict = None,
    ) -> models.CreateImageResponse:
        """
        创建自定义镜像。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstances(
            self,
            request: models.CreateInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateInstancesResponse:
        """
        创建云桌面实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePolicy(
            self,
            request: models.CreatePolicyRequest,
            opts: Dict = None,
    ) -> models.CreatePolicyResponse:
        """
        创建策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCommandTasks(
            self,
            request: models.DeleteCommandTasksRequest,
            opts: Dict = None,
    ) -> models.DeleteCommandTasksResponse:
        """
        删除命令任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCommandTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCommandTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainControlPolicy(
            self,
            request: models.DeleteDomainControlPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainControlPolicyResponse:
        """
        删除域名访问控制策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainControlPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainControlPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImages(
            self,
            request: models.DeleteImagesRequest,
            opts: Dict = None,
    ) -> models.DeleteImagesResponse:
        """
        用于删除一个或多个自定义镜像。单次最大删除5个。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCommandTasks(
            self,
            request: models.DescribeCommandTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeCommandTasksResponse:
        """
        拉取命令任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCommandTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCommandTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImages(
            self,
            request: models.DescribeImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeImagesResponse:
        """
        获取云桌面镜像详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceFetchMsg(
            self,
            request: models.DescribeInstanceFetchMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceFetchMsgResponse:
        """
        获取指定实例的登录Fetch信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceFetchMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceFetchMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceGraphData(
            self,
            request: models.DescribeInstanceGraphDataRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceGraphDataResponse:
        """
        获取实例磁盘分区监控数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceGraphData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceGraphDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLoginMsg(
            self,
            request: models.DescribeInstanceLoginMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLoginMsgResponse:
        """
        获取指定实例的登录login信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLoginMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLoginMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorData(
            self,
            request: models.DescribeInstanceMonitorDataRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorDataResponse:
        """
        查询实例监控数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceRegionDistribution(
            self,
            request: models.DescribeInstanceRegionDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceRegionDistributionResponse:
        """
        获取用户在各个区域云桌面实例个数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceRegionDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceRegionDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        获取云桌面实例详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesBindStatus(
            self,
            request: models.DescribeInstancesBindStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesBindStatusResponse:
        """
        获取桌面实例绑定状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesBindStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesBindStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesStatus(
            self,
            request: models.DescribeInstancesStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesStatusResponse:
        """
        获取桌面实例状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvocationDetail(
            self,
            request: models.DescribeInvocationDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInvocationDetailResponse:
        """
        查询脚本任务执行的详细情况。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvocationDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvocationDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvocations(
            self,
            request: models.DescribeInvocationsRequest,
            opts: Dict = None,
    ) -> models.DescribeInvocationsResponse:
        """
        查询指定云桌面上的任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvocations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvocationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyDetail(
            self,
            request: models.DescribePolicyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyDetailResponse:
        """
        拉取租户策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroups(
            self,
            request: models.DescribeSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupsResponse:
        """
        拉取云桌面关联的安全组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshots(
            self,
            request: models.DescribeSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotsResponse:
        """
        拉取快照列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsage(
            self,
            request: models.DescribeUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeUsageResponse:
        """
        拉取实例使用时长详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsers(
            self,
            request: models.DescribeUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersResponse:
        """
        拉取用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroup(
            self,
            request: models.DisassociateSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupResponse:
        """
        安全组批量解关联云桌面
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDiskConfiguration(
            self,
            request: models.ModifyDiskConfigurationRequest,
            opts: Dict = None,
    ) -> models.ModifyDiskConfigurationResponse:
        """
        实例硬盘扩容
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDiskConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDiskConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageAttrs(
            self,
            request: models.ModifyImageAttrsRequest,
            opts: Dict = None,
    ) -> models.ModifyImageAttrsResponse:
        """
        修改镜像属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageAttrs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageAttrsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceBasicAttribute(
            self,
            request: models.ModifyInstanceBasicAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceBasicAttributeResponse:
        """
        修改桌面实例属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceBasicAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceBasicAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesType(
            self,
            request: models.ModifyInstancesTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesTypeResponse:
        """
        调整实例机型配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesVpc(
            self,
            request: models.ModifyInstancesVpcRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesVpcResponse:
        """
        调整实例私有网络
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebootInstances(
            self,
            request: models.RebootInstancesRequest,
            opts: Dict = None,
    ) -> models.RebootInstancesResponse:
        """
        重启实例
        """
        
        kwargs = {}
        kwargs["action"] = "RebootInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebootInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveDataDisks(
            self,
            request: models.RemoveDataDisksRequest,
            opts: Dict = None,
    ) -> models.RemoveDataDisksResponse:
        """
        卸载实例数据盘
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveDataDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveDataDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemovePolicy(
            self,
            request: models.RemovePolicyRequest,
            opts: Dict = None,
    ) -> models.RemovePolicyResponse:
        """
        删除策略
        """
        
        kwargs = {}
        kwargs["action"] = "RemovePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemovePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewInstances(
            self,
            request: models.RenewInstancesRequest,
            opts: Dict = None,
    ) -> models.RenewInstancesResponse:
        """
        实例续费
        """
        
        kwargs = {}
        kwargs["action"] = "RenewInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstances(
            self,
            request: models.ResetInstancesRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesResponse:
        """
        实例重置
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunCommand(
            self,
            request: models.RunCommandRequest,
            opts: Dict = None,
    ) -> models.RunCommandResponse:
        """
        在指定的云桌面实例上执行脚本任务。
        """
        
        kwargs = {}
        kwargs["action"] = "RunCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartInstances(
            self,
            request: models.StartInstancesRequest,
            opts: Dict = None,
    ) -> models.StartInstancesResponse:
        """
        开启实例
        """
        
        kwargs = {}
        kwargs["action"] = "StartInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCommandTasks(
            self,
            request: models.StopCommandTasksRequest,
            opts: Dict = None,
    ) -> models.StopCommandTasksResponse:
        """
        停止命令任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopCommandTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCommandTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstances(
            self,
            request: models.StopInstancesRequest,
            opts: Dict = None,
    ) -> models.StopInstancesResponse:
        """
        关闭实例
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInvocation(
            self,
            request: models.StopInvocationRequest,
            opts: Dict = None,
    ) -> models.StopInvocationResponse:
        """
        停止脚本任务的执行。
        """
        
        kwargs = {}
        kwargs["action"] = "StopInvocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInvocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopSession(
            self,
            request: models.StopSessionRequest,
            opts: Dict = None,
    ) -> models.StopSessionResponse:
        """
        注销或者断开机器当前会话
        """
        
        kwargs = {}
        kwargs["action"] = "StopSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateInstances(
            self,
            request: models.TerminateInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminateInstancesResponse:
        """
        主动退还、销毁退还实例。
        <li>包年包月实例首次调用本接口，且参数DestroyImmediately为false时，实例进入隔离期，再次调用本接口，实例将被销毁，且不可恢复。</li>
        <li>包年包月实例，如果参数DestroyImmediately为true来调用此接口，则实例将被直接销毁，且不可恢复。</li>
        <li>按量计费实例调用本接口将被直接销毁，且不可恢复。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindInstances(
            self,
            request: models.UnbindInstancesRequest,
            opts: Dict = None,
    ) -> models.UnbindInstancesResponse:
        """
        解除用户和机器绑定关系
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePolicy(
            self,
            request: models.UpdatePolicyRequest,
            opts: Dict = None,
    ) -> models.UpdatePolicyResponse:
        """
        更新策略
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)