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
from tencentcloud.tat.v20201028 import models
from typing import Dict


class TatClient(AbstractClient):
    _apiVersion = '2020-10-28'
    _endpoint = 'tat.tencentcloudapi.com'
    _service = 'tat'

    async def CancelInvocation(
            self,
            request: models.CancelInvocationRequest,
            opts: Dict = None,
    ) -> models.CancelInvocationResponse:
        """
        取消一台或多台实例执行的命令

        * 如果命令还未下发到agent，任务状态处于PENDING、DELIVERING、DELIVER_DELAYED，取消后任务状态是CANCELLED
        * 如果命令已下发到agent，任务状态处于RUNNING， 取消后任务状态是TERMINATED
        """
        
        kwargs = {}
        kwargs["action"] = "CancelInvocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelInvocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCommand(
            self,
            request: models.CreateCommandRequest,
            opts: Dict = None,
    ) -> models.CreateCommandResponse:
        """
        此接口用于创建命令。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInvoker(
            self,
            request: models.CreateInvokerRequest,
            opts: Dict = None,
    ) -> models.CreateInvokerResponse:
        """
        此接口用于创建执行器。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInvoker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInvokerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRegisterCode(
            self,
            request: models.CreateRegisterCodeRequest,
            opts: Dict = None,
    ) -> models.CreateRegisterCodeResponse:
        """
        接口用于创建注册码。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRegisterCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRegisterCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCommand(
            self,
            request: models.DeleteCommandRequest,
            opts: Dict = None,
    ) -> models.DeleteCommandResponse:
        """
        此接口用于删除命令。
        如果命令与执行器关联，则无法被删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCommands(
            self,
            request: models.DeleteCommandsRequest,
            opts: Dict = None,
    ) -> models.DeleteCommandsResponse:
        """
        批量删除命令接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCommands"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCommandsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInvoker(
            self,
            request: models.DeleteInvokerRequest,
            opts: Dict = None,
    ) -> models.DeleteInvokerResponse:
        """
        此接口用于删除执行器。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInvoker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInvokerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRegisterCodes(
            self,
            request: models.DeleteRegisterCodesRequest,
            opts: Dict = None,
    ) -> models.DeleteRegisterCodesResponse:
        """
        此接口用于批量删除注册码。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRegisterCodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRegisterCodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRegisterInstance(
            self,
            request: models.DeleteRegisterInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteRegisterInstanceResponse:
        """
        接口用于删除托管实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRegisterInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRegisterInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutomationAgentStatus(
            self,
            request: models.DescribeAutomationAgentStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeAutomationAgentStatusResponse:
        """
        此接口用于查询自动化助手客户端的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutomationAgentStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutomationAgentStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCommands(
            self,
            request: models.DescribeCommandsRequest,
            opts: Dict = None,
    ) -> models.DescribeCommandsResponse:
        """
        此接口用于查询命令详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCommands"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCommandsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvocationTasks(
            self,
            request: models.DescribeInvocationTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeInvocationTasksResponse:
        """
        此接口用于查询执行任务详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvocationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvocationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvocations(
            self,
            request: models.DescribeInvocationsRequest,
            opts: Dict = None,
    ) -> models.DescribeInvocationsResponse:
        """
        此接口用于查询执行活动详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvocations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvocationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvokerRecords(
            self,
            request: models.DescribeInvokerRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeInvokerRecordsResponse:
        """
        此接口用于查询执行器的执行记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvokerRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvokerRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvokers(
            self,
            request: models.DescribeInvokersRequest,
            opts: Dict = None,
    ) -> models.DescribeInvokersResponse:
        """
        此接口用于查询执行器信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvokers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvokersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuotas(
            self,
            request: models.DescribeQuotasRequest,
            opts: Dict = None,
    ) -> models.DescribeQuotasResponse:
        """
        此接口用于获取配额信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        此接口用于查询 TAT 产品后台地域列表。
        RegionState 为 AVAILABLE，代表该地域的 TAT 后台服务已经可用；未返回，代表该地域的 TAT 后台服务尚不可用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegisterCodes(
            self,
            request: models.DescribeRegisterCodesRequest,
            opts: Dict = None,
    ) -> models.DescribeRegisterCodesResponse:
        """
        接口用于查询注册码信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegisterCodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegisterCodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegisterInstances(
            self,
            request: models.DescribeRegisterInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeRegisterInstancesResponse:
        """
        接口用于查询被托管的实例信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegisterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegisterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScenes(
            self,
            request: models.DescribeScenesRequest,
            opts: Dict = None,
    ) -> models.DescribeScenesResponse:
        """
        此接口用于查询场景详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScenes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScenesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableInvoker(
            self,
            request: models.DisableInvokerRequest,
            opts: Dict = None,
    ) -> models.DisableInvokerResponse:
        """
        此接口用于停止执行器。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableInvoker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableInvokerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableRegisterCodes(
            self,
            request: models.DisableRegisterCodesRequest,
            opts: Dict = None,
    ) -> models.DisableRegisterCodesResponse:
        """
        此接口用于批量禁用注册码。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableRegisterCodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableRegisterCodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableInvoker(
            self,
            request: models.EnableInvokerRequest,
            opts: Dict = None,
    ) -> models.EnableInvokerResponse:
        """
        此接口用于启用执行器。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableInvoker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableInvokerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeCommand(
            self,
            request: models.InvokeCommandRequest,
            opts: Dict = None,
    ) -> models.InvokeCommandResponse:
        """
        在指定的实例上触发命令，调用成功返回执行活动ID（inv-xxxxxxxx），每个执行活动内部有一个或多个执行任务（invt-xxxxxxxx），每个执行任务代表命令在一台 CVM 或一台 Lighthouse 上的执行记录。

        * 如果指定实例未安装 agent，或 agent 不在线，返回失败
        * 如果命令类型与 agent 运行环境不符，返回失败
        * 指定的实例需要处于 VPC 网络
        * 指定的实例需要处于 RUNNING 状态
        * 不可同时指定 CVM 和 Lighthouse
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCommand(
            self,
            request: models.ModifyCommandRequest,
            opts: Dict = None,
    ) -> models.ModifyCommandResponse:
        """
        此接口用于修改命令。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInvoker(
            self,
            request: models.ModifyInvokerRequest,
            opts: Dict = None,
    ) -> models.ModifyInvokerResponse:
        """
        此接口用于修改执行器。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInvoker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInvokerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRegisterInstance(
            self,
            request: models.ModifyRegisterInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyRegisterInstanceResponse:
        """
        接口用于修改托管实例信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRegisterInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRegisterInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PreviewReplacedCommandContent(
            self,
            request: models.PreviewReplacedCommandContentRequest,
            opts: Dict = None,
    ) -> models.PreviewReplacedCommandContentResponse:
        """
        此接口用于预览自定义参数替换后的命令内容。不会触发真实执行。
        """
        
        kwargs = {}
        kwargs["action"] = "PreviewReplacedCommandContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PreviewReplacedCommandContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunCommand(
            self,
            request: models.RunCommandRequest,
            opts: Dict = None,
    ) -> models.RunCommandResponse:
        """
        执行命令，调用成功返回执行活动ID（inv-xxxxxxxx），每个执行活动内部有一个或多个执行任务（invt-xxxxxxxx），每个执行任务代表命令在一台 CVM 或一台 Lighthouse 上的执行记录。

        * 如果指定实例未安装 agent，或 agent 不在线，返回失败
        * 如果命令类型与 agent 运行环境不符，返回失败
        * 指定的实例需要处于 VPC 网络
        * 指定的实例需要处于 `RUNNING` 状态
        * 不可同时指定 CVM 和 Lighthouse
        """
        
        kwargs = {}
        kwargs["action"] = "RunCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)