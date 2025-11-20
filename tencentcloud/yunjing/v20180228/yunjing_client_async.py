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
from tencentcloud.yunjing.v20180228 import models
from typing import Dict


class YunjingClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'yunjing.tencentcloudapi.com'
    _service = 'yunjing'

    async def AddLoginWhiteList(
            self,
            request: models.AddLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.AddLoginWhiteListResponse:
        """
        本接口（AddLoginWhiteList）用于添加白名单规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddMachineTag(
            self,
            request: models.AddMachineTagRequest,
            opts: Dict = None,
    ) -> models.AddMachineTagResponse:
        """
        增加机器关联标签
        """
        
        kwargs = {}
        kwargs["action"] = "AddMachineTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddMachineTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseProVersion(
            self,
            request: models.CloseProVersionRequest,
            opts: Dict = None,
    ) -> models.CloseProVersionResponse:
        """
        本接口 (CloseProVersion) 用于关闭专业版。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseProVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseProVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaselineStrategy(
            self,
            request: models.CreateBaselineStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateBaselineStrategyResponse:
        """
        根据策略信息创建基线策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaselineStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaselineStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenPortTask(
            self,
            request: models.CreateOpenPortTaskRequest,
            opts: Dict = None,
    ) -> models.CreateOpenPortTaskResponse:
        """
        本接口 (CreateOpenPortTask) 用于创建实时获取端口任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenPortTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenPortTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProcessTask(
            self,
            request: models.CreateProcessTaskRequest,
            opts: Dict = None,
    ) -> models.CreateProcessTaskResponse:
        """
        本接口 (CreateProcessTask) 用于创建实时拉取进程任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProcessTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProcessTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUsualLoginPlaces(
            self,
            request: models.CreateUsualLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.CreateUsualLoginPlacesResponse:
        """
        此接口（CreateUsualLoginPlaces）用于添加常用登录地。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUsualLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUsualLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAttackLogs(
            self,
            request: models.DeleteAttackLogsRequest,
            opts: Dict = None,
    ) -> models.DeleteAttackLogsResponse:
        """
        删除网络攻击日志
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAttackLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAttackLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBashEvents(
            self,
            request: models.DeleteBashEventsRequest,
            opts: Dict = None,
    ) -> models.DeleteBashEventsResponse:
        """
        根据Ids删除高危命令事件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBashEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBashEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBashRules(
            self,
            request: models.DeleteBashRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteBashRulesResponse:
        """
        删除高危命令规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBruteAttacks(
            self,
            request: models.DeleteBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.DeleteBruteAttacksResponse:
        """
        本接口 (DeleteBruteAttacks) 用于删除暴力破解记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoginWhiteList(
            self,
            request: models.DeleteLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteLoginWhiteListResponse:
        """
        删除白名单规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachine(
            self,
            request: models.DeleteMachineRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineResponse:
        """
        本接口（DeleteMachine）用于卸载云镜客户端。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineTag(
            self,
            request: models.DeleteMachineTagRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineTagResponse:
        """
        删除服务器关联的标签
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMaliciousRequests(
            self,
            request: models.DeleteMaliciousRequestsRequest,
            opts: Dict = None,
    ) -> models.DeleteMaliciousRequestsResponse:
        """
        本接口 (DeleteMaliciousRequests) 用于删除恶意请求记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMaliciousRequests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMaliciousRequestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMalwares(
            self,
            request: models.DeleteMalwaresRequest,
            opts: Dict = None,
    ) -> models.DeleteMalwaresResponse:
        """
        本接口 (DeleteMalwares) 用于删除木马记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNonlocalLoginPlaces(
            self,
            request: models.DeleteNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DeleteNonlocalLoginPlacesResponse:
        """
        本接口 (DeleteNonlocalLoginPlaces) 用于删除异地登录记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivilegeEvents(
            self,
            request: models.DeletePrivilegeEventsRequest,
            opts: Dict = None,
    ) -> models.DeletePrivilegeEventsResponse:
        """
        根据Ids删除本地提权
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivilegeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivilegeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivilegeRules(
            self,
            request: models.DeletePrivilegeRulesRequest,
            opts: Dict = None,
    ) -> models.DeletePrivilegeRulesResponse:
        """
        删除本地提权规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivilegeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivilegeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReverseShellEvents(
            self,
            request: models.DeleteReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.DeleteReverseShellEventsResponse:
        """
        根据Ids删除反弹Shell事件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReverseShellRules(
            self,
            request: models.DeleteReverseShellRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteReverseShellRulesResponse:
        """
        删除反弹Shell规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReverseShellRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReverseShellRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTags(
            self,
            request: models.DeleteTagsRequest,
            opts: Dict = None,
    ) -> models.DeleteTagsResponse:
        """
        删除标签
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsualLoginPlaces(
            self,
            request: models.DeleteUsualLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DeleteUsualLoginPlacesResponse:
        """
        本接口（DeleteUsualLoginPlaces）用于删除常用登录地。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsualLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsualLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountStatistics(
            self,
            request: models.DescribeAccountStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountStatisticsResponse:
        """
        本接口 (DescribeAccountStatistics) 用于获取帐号统计列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        本接口 (DescribeAccounts) 用于获取帐号列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentVuls(
            self,
            request: models.DescribeAgentVulsRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentVulsResponse:
        """
        本接口 (DescribeAgentVuls) 用于获取单台主机的漏洞列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentVuls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentVulsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmAttribute(
            self,
            request: models.DescribeAlarmAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmAttributeResponse:
        """
        本接口 (DescribeAlarmAttribute) 用于获取告警设置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackLogInfo(
            self,
            request: models.DescribeAttackLogInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackLogInfoResponse:
        """
        网络攻击日志详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackLogInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackLogInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackLogs(
            self,
            request: models.DescribeAttackLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackLogsResponse:
        """
        按分页形式展示网络攻击日志列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashEvents(
            self,
            request: models.DescribeBashEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeBashEventsResponse:
        """
        获取高危命令列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashRules(
            self,
            request: models.DescribeBashRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBashRulesResponse:
        """
        获取高危命令规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBruteAttacks(
            self,
            request: models.DescribeBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.DescribeBruteAttacksResponse:
        """
        本接口{DescribeBruteAttacks}用于获取暴力破解事件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComponentInfo(
            self,
            request: models.DescribeComponentInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeComponentInfoResponse:
        """
        本接口 (DescribeComponentInfo) 用于获取组件信息数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComponentInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComponentInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComponentStatistics(
            self,
            request: models.DescribeComponentStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeComponentStatisticsResponse:
        """
        本接口 (DescribeComponentStatistics) 用于获取组件统计列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComponentStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComponentStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComponents(
            self,
            request: models.DescribeComponentsRequest,
            opts: Dict = None,
    ) -> models.DescribeComponentsResponse:
        """
        本接口 (DescribeComponents) 用于获取组件列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComponents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComponentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHistoryAccounts(
            self,
            request: models.DescribeHistoryAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeHistoryAccountsResponse:
        """
        本接口 (DescribeHistoryAccounts) 用于获取帐号变更历史列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHistoryAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHistoryAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImpactedHosts(
            self,
            request: models.DescribeImpactedHostsRequest,
            opts: Dict = None,
    ) -> models.DescribeImpactedHostsResponse:
        """
        本接口 (DescribeImpactedHosts) 用于获取漏洞受影响机器列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImpactedHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImpactedHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginWhiteList(
            self,
            request: models.DescribeLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginWhiteListResponse:
        """
        获取异地登录白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineInfo(
            self,
            request: models.DescribeMachineInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineInfoResponse:
        """
        本接口（DescribeMachineInfo）用于获取机器详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachines(
            self,
            request: models.DescribeMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeMachinesResponse:
        """
        本接口 (DescribeMachines) 用于获取区域主机列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaliciousRequests(
            self,
            request: models.DescribeMaliciousRequestsRequest,
            opts: Dict = None,
    ) -> models.DescribeMaliciousRequestsResponse:
        """
        本接口 (DescribeMaliciousRequests) 用于获取恶意请求数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaliciousRequests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaliciousRequestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwares(
            self,
            request: models.DescribeMalwaresRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwaresResponse:
        """
        本接口（DescribeMalwares）用于获取木马事件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNonlocalLoginPlaces(
            self,
            request: models.DescribeNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DescribeNonlocalLoginPlacesResponse:
        """
        本接口(DescribeNonlocalLoginPlaces)用于获取异地登录事件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpenPortStatistics(
            self,
            request: models.DescribeOpenPortStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeOpenPortStatisticsResponse:
        """
        本接口 (DescribeOpenPortStatistics) 用于获取端口统计列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpenPortStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpenPortStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpenPortTaskStatus(
            self,
            request: models.DescribeOpenPortTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeOpenPortTaskStatusResponse:
        """
        本接口 (DescribeOpenPortTaskStatus) 用于获取实时拉取端口任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpenPortTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpenPortTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpenPorts(
            self,
            request: models.DescribeOpenPortsRequest,
            opts: Dict = None,
    ) -> models.DescribeOpenPortsResponse:
        """
        本接口 (DescribeOpenPorts) 用于获取端口列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpenPorts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpenPortsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewStatistics(
            self,
            request: models.DescribeOverviewStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewStatisticsResponse:
        """
        本接口用于（DescribeOverviewStatistics）获取概览统计数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivilegeEvents(
            self,
            request: models.DescribePrivilegeEventsRequest,
            opts: Dict = None,
    ) -> models.DescribePrivilegeEventsResponse:
        """
        获取本地提权事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivilegeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivilegeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivilegeRules(
            self,
            request: models.DescribePrivilegeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribePrivilegeRulesResponse:
        """
        获取本地提权规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivilegeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivilegeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProVersionInfo(
            self,
            request: models.DescribeProVersionInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProVersionInfoResponse:
        """
        本接口 (DescribeProVersionInfo) 用于获取专业版信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProVersionInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProVersionInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessStatistics(
            self,
            request: models.DescribeProcessStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessStatisticsResponse:
        """
        本接口 (DescribeProcessStatistics) 用于获取进程统计列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessTaskStatus(
            self,
            request: models.DescribeProcessTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessTaskStatusResponse:
        """
        本接口 (DescribeProcessTaskStatus) 用于获取实时拉取进程任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcesses(
            self,
            request: models.DescribeProcessesRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessesResponse:
        """
        本接口 (DescribeProcesses) 用于获取进程列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcesses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellEvents(
            self,
            request: models.DescribeReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellEventsResponse:
        """
        获取反弹Shell列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellRules(
            self,
            request: models.DescribeReverseShellRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellRulesResponse:
        """
        获取反弹Shell规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityDynamics(
            self,
            request: models.DescribeSecurityDynamicsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityDynamicsResponse:
        """
        本接口 (DescribeSecurityDynamics) 用于获取安全事件消息数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityDynamics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityDynamicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityTrends(
            self,
            request: models.DescribeSecurityTrendsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityTrendsResponse:
        """
        本接口 (DescribeSecurityTrends) 用于获取安全事件统计数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityTrends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityTrendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagMachines(
            self,
            request: models.DescribeTagMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeTagMachinesResponse:
        """
        获取指定标签关联的服务器信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTags(
            self,
            request: models.DescribeTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsResponse:
        """
        获取所有主机标签
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsualLoginPlaces(
            self,
            request: models.DescribeUsualLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DescribeUsualLoginPlacesResponse:
        """
        此接口（DescribeUsualLoginPlaces）用于查询常用登录地。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsualLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsualLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulInfo(
            self,
            request: models.DescribeVulInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVulInfoResponse:
        """
        本接口 (DescribeVulInfo) 用于获取漏洞详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanResult(
            self,
            request: models.DescribeVulScanResultRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanResultResponse:
        """
        本接口 (DescribeVulScanResult) 用于获取漏洞检测结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVuls(
            self,
            request: models.DescribeVulsRequest,
            opts: Dict = None,
    ) -> models.DescribeVulsResponse:
        """
        本接口 (DescribeVuls) 用于获取漏洞列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVuls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReportBruteAttacks(
            self,
            request: models.DescribeWeeklyReportBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportBruteAttacksResponse:
        """
        本接口 (DescribeWeeklyReportBruteAttacks) 用于获取专业周报密码破解数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReportBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReportInfo(
            self,
            request: models.DescribeWeeklyReportInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportInfoResponse:
        """
        本接口 (DescribeWeeklyReportInfo) 用于获取专业周报详情数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReportInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReportMalwares(
            self,
            request: models.DescribeWeeklyReportMalwaresRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportMalwaresResponse:
        """
        本接口 (DescribeWeeklyReportMalwares) 用于获取专业周报木马数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReportMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReportNonlocalLoginPlaces(
            self,
            request: models.DescribeWeeklyReportNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportNonlocalLoginPlacesResponse:
        """
        本接口 (DescribeWeeklyReportNonlocalLoginPlaces) 用于获取专业周报异地登录数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReportNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReportVuls(
            self,
            request: models.DescribeWeeklyReportVulsRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportVulsResponse:
        """
        本接口 (DescribeWeeklyReportVuls) 用于专业版周报漏洞数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReportVuls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportVulsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReports(
            self,
            request: models.DescribeWeeklyReportsRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportsResponse:
        """
        本接口 (DescribeWeeklyReports) 用于获取周报列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditBashRule(
            self,
            request: models.EditBashRuleRequest,
            opts: Dict = None,
    ) -> models.EditBashRuleResponse:
        """
        新增或修改高危命令规则
        """
        
        kwargs = {}
        kwargs["action"] = "EditBashRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditBashRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditPrivilegeRule(
            self,
            request: models.EditPrivilegeRuleRequest,
            opts: Dict = None,
    ) -> models.EditPrivilegeRuleResponse:
        """
        新增或修改本地提权规则
        """
        
        kwargs = {}
        kwargs["action"] = "EditPrivilegeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditPrivilegeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditReverseShellRule(
            self,
            request: models.EditReverseShellRuleRequest,
            opts: Dict = None,
    ) -> models.EditReverseShellRuleResponse:
        """
        编辑反弹Shell规则
        """
        
        kwargs = {}
        kwargs["action"] = "EditReverseShellRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditReverseShellRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditTags(
            self,
            request: models.EditTagsRequest,
            opts: Dict = None,
    ) -> models.EditTagsResponse:
        """
        新增或编辑标签
        """
        
        kwargs = {}
        kwargs["action"] = "EditTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAttackLogs(
            self,
            request: models.ExportAttackLogsRequest,
            opts: Dict = None,
    ) -> models.ExportAttackLogsResponse:
        """
        导出网络攻击日志
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAttackLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAttackLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBashEvents(
            self,
            request: models.ExportBashEventsRequest,
            opts: Dict = None,
    ) -> models.ExportBashEventsResponse:
        """
        导出高危命令事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBashEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBashEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBruteAttacks(
            self,
            request: models.ExportBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.ExportBruteAttacksResponse:
        """
        本接口 (ExportBruteAttacks) 用于导出密码破解记录成CSV文件。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportMaliciousRequests(
            self,
            request: models.ExportMaliciousRequestsRequest,
            opts: Dict = None,
    ) -> models.ExportMaliciousRequestsResponse:
        """
        本接口 (ExportMaliciousRequests) 用于导出下载恶意请求文件。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportMaliciousRequests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportMaliciousRequestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportMalwares(
            self,
            request: models.ExportMalwaresRequest,
            opts: Dict = None,
    ) -> models.ExportMalwaresResponse:
        """
        本接口 (ExportMalwares) 用于导出木马记录CSV文件。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportNonlocalLoginPlaces(
            self,
            request: models.ExportNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.ExportNonlocalLoginPlacesResponse:
        """
        本接口 (ExportNonlocalLoginPlaces) 用于导出异地登录事件记录CSV文件。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportPrivilegeEvents(
            self,
            request: models.ExportPrivilegeEventsRequest,
            opts: Dict = None,
    ) -> models.ExportPrivilegeEventsResponse:
        """
        导出本地提权事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportPrivilegeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportPrivilegeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportReverseShellEvents(
            self,
            request: models.ExportReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.ExportReverseShellEventsResponse:
        """
        导出反弹Shell事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IgnoreImpactedHosts(
            self,
            request: models.IgnoreImpactedHostsRequest,
            opts: Dict = None,
    ) -> models.IgnoreImpactedHostsResponse:
        """
        本接口 (IgnoreImpactedHosts) 用于忽略漏洞。
        """
        
        kwargs = {}
        kwargs["action"] = "IgnoreImpactedHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IgnoreImpactedHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceOpenProVersionPrepaid(
            self,
            request: models.InquiryPriceOpenProVersionPrepaidRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceOpenProVersionPrepaidResponse:
        """
        本接口 (InquiryPriceOpenProVersionPrepaid) 用于开通专业版询价(预付费)。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceOpenProVersionPrepaid"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceOpenProVersionPrepaidResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MisAlarmNonlocalLoginPlaces(
            self,
            request: models.MisAlarmNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.MisAlarmNonlocalLoginPlacesResponse:
        """
        本接口{MisAlarmNonlocalLoginPlaces}将设置当前地点为常用登录地。
        """
        
        kwargs = {}
        kwargs["action"] = "MisAlarmNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MisAlarmNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmAttribute(
            self,
            request: models.ModifyAlarmAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmAttributeResponse:
        """
        本接口（ModifyAlarmAttribute）用于修改告警设置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoOpenProVersionConfig(
            self,
            request: models.ModifyAutoOpenProVersionConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoOpenProVersionConfigResponse:
        """
        本接口 (ModifyAutoOpenProVersionConfig) 用于设置新增主机自动开通专业版配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoOpenProVersionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoOpenProVersionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoginWhiteList(
            self,
            request: models.ModifyLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyLoginWhiteListResponse:
        """
        编辑白名单规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProVersionRenewFlag(
            self,
            request: models.ModifyProVersionRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyProVersionRenewFlagResponse:
        """
        本接口 (ModifyProVersionRenewFlag) 用于修改专业版包年包月续费标识。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProVersionRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProVersionRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenProVersion(
            self,
            request: models.OpenProVersionRequest,
            opts: Dict = None,
    ) -> models.OpenProVersionResponse:
        """
        本接口 (OpenProVersion) 用于开通专业版。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenProVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenProVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenProVersionPrepaid(
            self,
            request: models.OpenProVersionPrepaidRequest,
            opts: Dict = None,
    ) -> models.OpenProVersionPrepaidResponse:
        """
        本接口 (OpenProVersionPrepaid) 用于开通专业版(包年包月)。
        """
        
        kwargs = {}
        kwargs["action"] = "OpenProVersionPrepaid"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenProVersionPrepaidResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverMalwares(
            self,
            request: models.RecoverMalwaresRequest,
            opts: Dict = None,
    ) -> models.RecoverMalwaresResponse:
        """
        本接口（RecoverMalwares）用于批量恢复已经被隔离的木马文件。
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewProVersion(
            self,
            request: models.RenewProVersionRequest,
            opts: Dict = None,
    ) -> models.RenewProVersionResponse:
        """
        本接口 (RenewProVersion) 用于续费专业版(包年包月)。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewProVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewProVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RescanImpactedHost(
            self,
            request: models.RescanImpactedHostRequest,
            opts: Dict = None,
    ) -> models.RescanImpactedHostResponse:
        """
        本接口 (RescanImpactedHost) 用于漏洞重新检测。
        """
        
        kwargs = {}
        kwargs["action"] = "RescanImpactedHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RescanImpactedHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SeparateMalwares(
            self,
            request: models.SeparateMalwaresRequest,
            opts: Dict = None,
    ) -> models.SeparateMalwaresResponse:
        """
        本接口（SeparateMalwares）用于隔离木马。
        """
        
        kwargs = {}
        kwargs["action"] = "SeparateMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SeparateMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetBashEventsStatus(
            self,
            request: models.SetBashEventsStatusRequest,
            opts: Dict = None,
    ) -> models.SetBashEventsStatusResponse:
        """
        设置高危命令事件状态
        """
        
        kwargs = {}
        kwargs["action"] = "SetBashEventsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetBashEventsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchBashRules(
            self,
            request: models.SwitchBashRulesRequest,
            opts: Dict = None,
    ) -> models.SwitchBashRulesResponse:
        """
        切换高危命令规则状态
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TrustMaliciousRequest(
            self,
            request: models.TrustMaliciousRequestRequest,
            opts: Dict = None,
    ) -> models.TrustMaliciousRequestResponse:
        """
        本接口 (TrustMaliciousRequest) 用于恶意请求添加信任。
        """
        
        kwargs = {}
        kwargs["action"] = "TrustMaliciousRequest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TrustMaliciousRequestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TrustMalwares(
            self,
            request: models.TrustMalwaresRequest,
            opts: Dict = None,
    ) -> models.TrustMalwaresResponse:
        """
        本接口(TrustMalwares)将被识别木马文件设为信任。
        """
        
        kwargs = {}
        kwargs["action"] = "TrustMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TrustMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UntrustMaliciousRequest(
            self,
            request: models.UntrustMaliciousRequestRequest,
            opts: Dict = None,
    ) -> models.UntrustMaliciousRequestResponse:
        """
        本接口 (UntrustMaliciousRequest) 用于取消信任恶意请求。
        """
        
        kwargs = {}
        kwargs["action"] = "UntrustMaliciousRequest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UntrustMaliciousRequestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UntrustMalwares(
            self,
            request: models.UntrustMalwaresRequest,
            opts: Dict = None,
    ) -> models.UntrustMalwaresResponse:
        """
        本接口（UntrustMalwares）用于取消信任木马文件。
        """
        
        kwargs = {}
        kwargs["action"] = "UntrustMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UntrustMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)