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
from tencentcloud.cdwpg.v20201230 import models
from typing import Dict


class CdwpgClient(AbstractClient):
    _apiVersion = '2020-12-30'
    _endpoint = 'cdwpg.tencentcloudapi.com'
    _service = 'cdwpg'

    async def CreateInstanceByApi(
            self,
            request: models.CreateInstanceByApiRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceByApiResponse:
        """
        创建集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceByApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceByApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        获取云原生实例对应的账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBConfigHistory(
            self,
            request: models.DescribeDBConfigHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDBConfigHistoryResponse:
        """
        DescribeDBConfigHistory1
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBConfigHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBConfigHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBParams(
            self,
            request: models.DescribeDBParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBParamsResponse:
        """
        配置描述
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeErrorLog(
            self,
            request: models.DescribeErrorLogRequest,
            opts: Dict = None,
    ) -> models.DescribeErrorLogResponse:
        """
        查询错误日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeErrorLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeErrorLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstance(
            self,
            request: models.DescribeInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceResponse:
        """
        根据实例ID查询某个实例的具体信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceInfo(
            self,
            request: models.DescribeInstanceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceInfoResponse:
        """
        获取集群信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodes(
            self,
            request: models.DescribeInstanceNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodesResponse:
        """
        节点list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceOperations(
            self,
            request: models.DescribeInstanceOperationsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceOperationsResponse:
        """
        在集群详情页面，拉取该集群的操作
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceOperations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceOperationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceState(
            self,
            request: models.DescribeInstanceStateRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceStateResponse:
        """
        集群详情页中显示集群状态、流程进度等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        获取云原生实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSimpleInstances(
            self,
            request: models.DescribeSimpleInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeSimpleInstancesResponse:
        """
        获取集群实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSimpleInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSimpleInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLog(
            self,
            request: models.DescribeSlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogResponse:
        """
        查询慢SQL日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpgradeList(
            self,
            request: models.DescribeUpgradeListRequest,
            opts: Dict = None,
    ) -> models.DescribeUpgradeListResponse:
        """
        升级记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpgradeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpgradeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserHbaConfig(
            self,
            request: models.DescribeUserHbaConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUserHbaConfigResponse:
        """
        user_hba
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserHbaConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserHbaConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyInstanceByApi(
            self,
            request: models.DestroyInstanceByApiRequest,
            opts: Dict = None,
    ) -> models.DestroyInstanceByApiResponse:
        """
        销毁集群
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyInstanceByApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyInstanceByApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBParameters(
            self,
            request: models.ModifyDBParametersRequest,
            opts: Dict = None,
    ) -> models.ModifyDBParametersResponse:
        """
        集群配置下发
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        修改实例信息，目前为实例名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserHba(
            self,
            request: models.ModifyUserHbaRequest,
            opts: Dict = None,
    ) -> models.ModifyUserHbaResponse:
        """
        修改用户Hba配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserHba"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserHbaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAccountPassword(
            self,
            request: models.ResetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAccountPasswordResponse:
        """
        修改账号密码
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartInstance(
            self,
            request: models.RestartInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartInstanceResponse:
        """
        用户在控制台主动发起重启实例
        """
        
        kwargs = {}
        kwargs["action"] = "RestartInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutInstance(
            self,
            request: models.ScaleOutInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleOutInstanceResponse:
        """
        水平扩容
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleUpInstance(
            self,
            request: models.ScaleUpInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleUpInstanceResponse:
        """
        控制台垂直变配集群
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleUpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleUpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        在线升级
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)