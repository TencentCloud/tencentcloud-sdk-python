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
from tencentcloud.fwm.v20250611 import models
from typing import Dict


class FwmClient(AbstractClient):
    _apiVersion = '2025-06-11'
    _endpoint = 'fwm.tencentcloudapi.com'
    _service = 'fwm'

    async def CancelIgnorePolicyRisk(
            self,
            request: models.CancelIgnorePolicyRiskRequest,
            opts: Dict = None,
    ) -> models.CancelIgnorePolicyRiskResponse:
        """
        取消忽略策略风险
        """
        
        kwargs = {}
        kwargs["action"] = "CancelIgnorePolicyRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelIgnorePolicyRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAnalyzePolicyTask(
            self,
            request: models.CreateAnalyzePolicyTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAnalyzePolicyTaskResponse:
        """
        创建策略风险分析任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAnalyzePolicyTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAnalyzePolicyTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdgeAclRule(
            self,
            request: models.CreateEdgeAclRuleRequest,
            opts: Dict = None,
    ) -> models.CreateEdgeAclRuleResponse:
        """
        向已有的互联网边界ACL规则组中添加规则。需要先创建规则组，然后通过此接口添加规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdgeAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdgeAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdgeAclRuleGroup(
            self,
            request: models.CreateEdgeAclRuleGroupRequest,
            opts: Dict = None,
    ) -> models.CreateEdgeAclRuleGroupResponse:
        """
        创建互联网边界ACL规则组，支持同时创建多条规则。Product 必须为 cfw_edge_acl。规则支持 IP、域名、参数模板、实例、标签等多种源/目标类型。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdgeAclRuleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdgeAclRuleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatAclRule(
            self,
            request: models.CreateNatAclRuleRequest,
            opts: Dict = None,
    ) -> models.CreateNatAclRuleResponse:
        """
        在已有规则组中添加NAT ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatAclRuleGroup(
            self,
            request: models.CreateNatAclRuleGroupRequest,
            opts: Dict = None,
    ) -> models.CreateNatAclRuleGroupResponse:
        """
        创建NAT ACL规则组（NAT边界防火墙规则组管理）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatAclRuleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatAclRuleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroupRule(
            self,
            request: models.CreateSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupRuleResponse:
        """
        规则组编辑时添加规则（规则组管理）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroupRuleGroup(
            self,
            request: models.CreateSecurityGroupRuleGroupRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupRuleGroupResponse:
        """
        创建规则组（规则组管理）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupRuleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupRuleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStrategy(
            self,
            request: models.CreateStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateStrategyResponse:
        """
        创建策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcAclRule(
            self,
            request: models.CreateVpcAclRuleRequest,
            opts: Dict = None,
    ) -> models.CreateVpcAclRuleResponse:
        """
        在已有规则组中添加VPC ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcAclRuleGroup(
            self,
            request: models.CreateVpcAclRuleGroupRequest,
            opts: Dict = None,
    ) -> models.CreateVpcAclRuleGroupResponse:
        """
        创建VPC ACL规则组（VPC间防火墙规则组管理）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcAclRuleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcAclRuleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEdgeAclRule(
            self,
            request: models.DeleteEdgeAclRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteEdgeAclRuleResponse:
        """
        批量删除互联网边界ACL规则。支持一次删除多条规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEdgeAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEdgeAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNatAclRule(
            self,
            request: models.DeleteNatAclRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteNatAclRuleResponse:
        """
        删除NAT ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNatAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNatAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRuleGroup(
            self,
            request: models.DeleteRuleGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleGroupResponse:
        """
        删除规则组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRuleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityGroupRule(
            self,
            request: models.DeleteSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityGroupRuleResponse:
        """
        删除规则（规则组管理）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStrategy(
            self,
            request: models.DeleteStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteStrategyResponse:
        """
        删除策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcAclRule(
            self,
            request: models.DeleteVpcAclRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcAclRuleResponse:
        """
        删除VPC ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeAclRules(
            self,
            request: models.DescribeEdgeAclRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeAclRulesResponse:
        """
        查询指定规则组下的互联网边界ACL规则列表。支持分页和多种过滤条件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeAclRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeAclRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatAclRules(
            self,
            request: models.DescribeNatAclRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeNatAclRulesResponse:
        """
        查询NAT ACL规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatAclRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatAclRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganMembers(
            self,
            request: models.DescribeOrganMembersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganMembersResponse:
        """
        查询集团下所有纳管成员账号列表，支持分页、排序和多条件筛选，仅管理员可调用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganSummary(
            self,
            request: models.DescribeOrganSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganSummaryResponse:
        """
        获取集团概览信息，包括集团名称、管理员信息、成员数量等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyRiskAccountProductStats(
            self,
            request: models.DescribePolicyRiskAccountProductStatsRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyRiskAccountProductStatsResponse:
        """
        查询账号+产品维度风险统计，按账号分组返回各产品的体检策略数、待整改风险数、整改率、最近体检时间等信息，支持按账号名称/ID搜索以及仅看待整改、仅超时未体检筛选
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyRiskAccountProductStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyRiskAccountProductStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskAnalysisDetails(
            self,
            request: models.DescribeRiskAnalysisDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskAnalysisDetailsResponse:
        """
        获取实时分析风险详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskAnalysisDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskAnalysisDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCategoryStats(
            self,
            request: models.DescribeRiskCategoryStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCategoryStatsResponse:
        """
        查询策略体检风险分类统计数据,包含各类风险的规则数量、处置状态、整改率等信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCategoryStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCategoryStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskList(
            self,
            request: models.DescribeRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskListResponse:
        """
        查询用户所有规则的策略问题
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupRule(
            self,
            request: models.DescribeSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupRuleResponse:
        """
        查询规则详情（规则组管理）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupRules(
            self,
            request: models.DescribeSecurityGroupRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupRulesResponse:
        """
        查询规则组中规则列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStrategies(
            self,
            request: models.DescribeStrategiesRequest,
            opts: Dict = None,
    ) -> models.DescribeStrategiesResponse:
        """
        查询策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStrategies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStrategiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStrategy(
            self,
            request: models.DescribeStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeStrategyResponse:
        """
        查询策略详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStrategyAccounts(
            self,
            request: models.DescribeStrategyAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeStrategyAccountsResponse:
        """
        查看防火墙管理规则下发账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStrategyAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStrategyAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStrategyDispatchStatus(
            self,
            request: models.DescribeStrategyDispatchStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeStrategyDispatchStatusResponse:
        """
        查询策略下发状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStrategyDispatchStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStrategyDispatchStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcAclRules(
            self,
            request: models.DescribeVpcAclRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcAclRulesResponse:
        """
        查询VPC ACL规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcAclRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcAclRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DispatchStrategy(
            self,
            request: models.DispatchStrategyRequest,
            opts: Dict = None,
    ) -> models.DispatchStrategyResponse:
        """
        下发策略
        """
        
        kwargs = {}
        kwargs["action"] = "DispatchStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DispatchStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IgnorePolicyRisk(
            self,
            request: models.IgnorePolicyRiskRequest,
            opts: Dict = None,
    ) -> models.IgnorePolicyRiskResponse:
        """
        忽略策略问题
        """
        
        kwargs = {}
        kwargs["action"] = "IgnorePolicyRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IgnorePolicyRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdgeAclRule(
            self,
            request: models.ModifyEdgeAclRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyEdgeAclRuleResponse:
        """
        修改互联网边界ACL规则。Rule 参数中必须包含 RuleId 用于指定要修改的规则。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdgeAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdgeAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdgeAclRuleSequence(
            self,
            request: models.ModifyEdgeAclRuleSequenceRequest,
            opts: Dict = None,
    ) -> models.ModifyEdgeAclRuleSequenceResponse:
        """
        批量调整互联网边界ACL规则的执行顺序。Sequences 参数必须包含所有受影响的规则序号映射关系。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdgeAclRuleSequence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdgeAclRuleSequenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatAclRule(
            self,
            request: models.ModifyNatAclRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyNatAclRuleResponse:
        """
        修改NAT ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatAclRuleSequence(
            self,
            request: models.ModifyNatAclRuleSequenceRequest,
            opts: Dict = None,
    ) -> models.ModifyNatAclRuleSequenceResponse:
        """
        调整NAT ACL规则优先级顺序
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatAclRuleSequence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatAclRuleSequenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRuleGroup(
            self,
            request: models.ModifyRuleGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleGroupResponse:
        """
        修改规则组信息（规则组管理）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRuleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupRule(
            self,
            request: models.ModifySecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupRuleResponse:
        """
        修改规则（规则组管理）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStrategy(
            self,
            request: models.ModifyStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyStrategyResponse:
        """
        修改策略信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStrategySequence(
            self,
            request: models.ModifyStrategySequenceRequest,
            opts: Dict = None,
    ) -> models.ModifyStrategySequenceResponse:
        """
        快速排序修改策略优先级
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStrategySequence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStrategySequenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcAclRule(
            self,
            request: models.ModifyVpcAclRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcAclRuleResponse:
        """
        修改VPC ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcAclRuleSequence(
            self,
            request: models.ModifyVpcAclRuleSequenceRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcAclRuleSequenceResponse:
        """
        调整VPC ACL规则优先级顺序
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcAclRuleSequence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcAclRuleSequenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)