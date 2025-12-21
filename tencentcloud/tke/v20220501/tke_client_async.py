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
from tencentcloud.tke.v20220501 import models
from typing import Dict


class TkeClient(AbstractClient):
    _apiVersion = '2022-05-01'
    _endpoint = 'tke.tencentcloudapi.com'
    _service = 'tke'

    async def CreateHealthCheckPolicy(
            self,
            request: models.CreateHealthCheckPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateHealthCheckPolicyResponse:
        """
        创建健康检测策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHealthCheckPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHealthCheckPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNodePool(
            self,
            request: models.CreateNodePoolRequest,
            opts: Dict = None,
    ) -> models.CreateNodePoolResponse:
        """
        创建 TKE 节点池
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterMachines(
            self,
            request: models.DeleteClusterMachinesRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterMachinesResponse:
        """
        删除原生节点池节点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHealthCheckPolicy(
            self,
            request: models.DeleteHealthCheckPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteHealthCheckPolicyResponse:
        """
        删除健康检测策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHealthCheckPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHealthCheckPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNodePool(
            self,
            request: models.DeleteNodePoolRequest,
            opts: Dict = None,
    ) -> models.DeleteNodePoolResponse:
        """
        删除 TKE 节点池
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNodePoolResponse
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
        
    async def DescribeClusterMachines(
            self,
            request: models.DescribeClusterMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterMachinesResponse:
        """
        查询托原生点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterMachinesResponse
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
        
    async def DescribeHealthCheckPolicies(
            self,
            request: models.DescribeHealthCheckPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthCheckPoliciesResponse:
        """
        查询健康检测策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthCheckPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthCheckPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHealthCheckPolicyBindings(
            self,
            request: models.DescribeHealthCheckPolicyBindingsRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthCheckPolicyBindingsResponse:
        """
        查询健康检测策略绑定关系
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthCheckPolicyBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthCheckPolicyBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHealthCheckTemplate(
            self,
            request: models.DescribeHealthCheckTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthCheckTemplateResponse:
        """
        查询健康检测策略模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthCheckTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthCheckTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodePools(
            self,
            request: models.DescribeNodePoolsRequest,
            opts: Dict = None,
    ) -> models.DescribeNodePoolsResponse:
        """
        查询 TKE 节点池列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodePools"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodePoolsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterMachine(
            self,
            request: models.ModifyClusterMachineRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterMachineResponse:
        """
        修改原生节点
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHealthCheckPolicy(
            self,
            request: models.ModifyHealthCheckPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyHealthCheckPolicyResponse:
        """
        修改健康检测策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHealthCheckPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHealthCheckPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNodePool(
            self,
            request: models.ModifyNodePoolRequest,
            opts: Dict = None,
    ) -> models.ModifyNodePoolResponse:
        """
        更新 TKE 节点池
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebootMachines(
            self,
            request: models.RebootMachinesRequest,
            opts: Dict = None,
    ) -> models.RebootMachinesResponse:
        """
        重启原生节点实例
        """
        
        kwargs = {}
        kwargs["action"] = "RebootMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebootMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetMachineLogin(
            self,
            request: models.SetMachineLoginRequest,
            opts: Dict = None,
    ) -> models.SetMachineLoginResponse:
        """
        设置是否开启节点登录
        """
        
        kwargs = {}
        kwargs["action"] = "SetMachineLogin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetMachineLoginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartMachines(
            self,
            request: models.StartMachinesRequest,
            opts: Dict = None,
    ) -> models.StartMachinesResponse:
        """
        本接口 (StartMachines) 用于启动一个或多个原生节点实例。

        只有状态为 Stopped 的实例才可以进行此操作。
        接口调用成功后，等待一分钟左右，实例会进入 Running 状态。
        支持批量操作。每次请求批量实例的上限为100。
        本接口为同步接口，启动实例请求发送成功后会返回一个RequestId，此时操作并未立即完成。实例操作结果可以通过调用 DescribeClusterInstances 接口查询，如果实例的状态为 Running，则代表启动实例操作成功。
        """
        
        kwargs = {}
        kwargs["action"] = "StartMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopMachines(
            self,
            request: models.StopMachinesRequest,
            opts: Dict = None,
    ) -> models.StopMachinesResponse:
        """
        本接口 (StopMachines) 用于关闭一个或多个原生节点实例。

        只有状态为 Running 的实例才可以进行此操作。
        接口调用成功时，实例会进入 Stopping 状态；关闭实例成功时，实例会进入 Stopped 状态。
        支持强制关闭。强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        支持批量操作。每次请求批量实例的上限为 100。
        本接口为同步接口，关闭实例请求发送成功后会返回一个RequestId，此时操作并未立即完成。实例操作结果可以通过调用 DescribeClusterInstances 接口查询，如果实例的状态为stopped_with_charging，则代表关闭实例操作成功。
        """
        
        kwargs = {}
        kwargs["action"] = "StopMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)