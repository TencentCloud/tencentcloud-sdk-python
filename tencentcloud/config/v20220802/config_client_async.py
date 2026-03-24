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
from tencentcloud.config.v20220802 import models
from typing import Dict


class ConfigClient(AbstractClient):
    _apiVersion = '2022-08-02'
    _endpoint = 'config.tencentcloudapi.com'
    _service = 'config'

    async def AddAggregateCompliancePack(
            self,
            request: models.AddAggregateCompliancePackRequest,
            opts: Dict = None,
    ) -> models.AddAggregateCompliancePackResponse:
        """
        账号组新建合规包
        """
        
        kwargs = {}
        kwargs["action"] = "AddAggregateCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAggregateCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAggregateConfigRule(
            self,
            request: models.AddAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.AddAggregateConfigRuleResponse:
        """
        账号组新建规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCompliancePack(
            self,
            request: models.AddCompliancePackRequest,
            opts: Dict = None,
    ) -> models.AddCompliancePackResponse:
        """
        新建合规包
        """
        
        kwargs = {}
        kwargs["action"] = "AddCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddConfigRule(
            self,
            request: models.AddConfigRuleRequest,
            opts: Dict = None,
    ) -> models.AddConfigRuleResponse:
        """
        新建 规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseAggregateConfigRule(
            self,
            request: models.CloseAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.CloseAggregateConfigRuleResponse:
        """
        账号组关闭规则
        """
        
        kwargs = {}
        kwargs["action"] = "CloseAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseConfigRecorder(
            self,
            request: models.CloseConfigRecorderRequest,
            opts: Dict = None,
    ) -> models.CloseConfigRecorderResponse:
        """
        资源监控管理-关闭监控
        """
        
        kwargs = {}
        kwargs["action"] = "CloseConfigRecorder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseConfigRecorderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseConfigRule(
            self,
            request: models.CloseConfigRuleRequest,
            opts: Dict = None,
    ) -> models.CloseConfigRuleResponse:
        """
        关闭规则
        """
        
        kwargs = {}
        kwargs["action"] = "CloseConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAggregator(
            self,
            request: models.CreateAggregatorRequest,
            opts: Dict = None,
    ) -> models.CreateAggregatorResponse:
        """
        新建账号组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAggregator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAggregatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRemediation(
            self,
            request: models.CreateRemediationRequest,
            opts: Dict = None,
    ) -> models.CreateRemediationResponse:
        """
        新增规则修正设置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRemediation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRemediationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAggregateCompliancePack(
            self,
            request: models.DeleteAggregateCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DeleteAggregateCompliancePackResponse:
        """
        账号组删除合规包
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAggregateCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAggregateCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAggregateConfigRule(
            self,
            request: models.DeleteAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAggregateConfigRuleResponse:
        """
        账号组删除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCompliancePack(
            self,
            request: models.DeleteCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DeleteCompliancePackResponse:
        """
        删除合规包
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfigRule(
            self,
            request: models.DeleteConfigRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigRuleResponse:
        """
        删除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRemediations(
            self,
            request: models.DeleteRemediationsRequest,
            opts: Dict = None,
    ) -> models.DeleteRemediationsResponse:
        """
        删除规则修正设置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRemediations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRemediationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggregateCompliancePack(
            self,
            request: models.DescribeAggregateCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DescribeAggregateCompliancePackResponse:
        """
        账号组合规包详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggregateCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggregateCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggregateConfigDeliver(
            self,
            request: models.DescribeAggregateConfigDeliverRequest,
            opts: Dict = None,
    ) -> models.DescribeAggregateConfigDeliverResponse:
        """
        账号组获取投递设置详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggregateConfigDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggregateConfigDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggregateConfigRule(
            self,
            request: models.DescribeAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeAggregateConfigRuleResponse:
        """
        账号组获取规则详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggregateDiscoveredResource(
            self,
            request: models.DescribeAggregateDiscoveredResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeAggregateDiscoveredResourceResponse:
        """
        账号组资源详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggregateDiscoveredResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggregateDiscoveredResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggregator(
            self,
            request: models.DescribeAggregatorRequest,
            opts: Dict = None,
    ) -> models.DescribeAggregatorResponse:
        """
        账号组详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggregator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggregatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompliancePack(
            self,
            request: models.DescribeCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DescribeCompliancePackResponse:
        """
        合规包详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigDeliver(
            self,
            request: models.DescribeConfigDeliverRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigDeliverResponse:
        """
        获取投递设置详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigRecorder(
            self,
            request: models.DescribeConfigRecorderRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigRecorderResponse:
        """
        获取监控详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigRecorder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigRecorderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigRule(
            self,
            request: models.DescribeConfigRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigRuleResponse:
        """
        获取规则详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiscoveredResource(
            self,
            request: models.DescribeDiscoveredResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDiscoveredResourceResponse:
        """
        资源详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiscoveredResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiscoveredResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSystemCompliancePack(
            self,
            request: models.DescribeSystemCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DescribeSystemCompliancePackResponse:
        """
        获取系统合规包详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSystemCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSystemCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSystemRule(
            self,
            request: models.DescribeSystemRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeSystemRuleResponse:
        """
        预设规则详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSystemRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSystemRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachAggregateConfigRuleToCompliancePack(
            self,
            request: models.DetachAggregateConfigRuleToCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DetachAggregateConfigRuleToCompliancePackResponse:
        """
        账号组合规包移除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DetachAggregateConfigRuleToCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachAggregateConfigRuleToCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachConfigRuleToCompliancePack(
            self,
            request: models.DetachConfigRuleToCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DetachConfigRuleToCompliancePackResponse:
        """
        合规包移除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DetachConfigRuleToCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachConfigRuleToCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateCompliancePacks(
            self,
            request: models.ListAggregateCompliancePacksRequest,
            opts: Dict = None,
    ) -> models.ListAggregateCompliancePacksResponse:
        """
        账号组获取合规包列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateCompliancePacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateCompliancePacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateConfigRuleEvaluationResults(
            self,
            request: models.ListAggregateConfigRuleEvaluationResultsRequest,
            opts: Dict = None,
    ) -> models.ListAggregateConfigRuleEvaluationResultsResponse:
        """
        账号组获取评估结果--规则维度（某个规则下资源的评估结果列表）
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateConfigRuleEvaluationResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateConfigRuleEvaluationResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateConfigRules(
            self,
            request: models.ListAggregateConfigRulesRequest,
            opts: Dict = None,
    ) -> models.ListAggregateConfigRulesResponse:
        """
        账号组获取规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateConfigRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateConfigRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateDiscoveredResources(
            self,
            request: models.ListAggregateDiscoveredResourcesRequest,
            opts: Dict = None,
    ) -> models.ListAggregateDiscoveredResourcesResponse:
        """
        账号组获取资源列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateDiscoveredResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateDiscoveredResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregators(
            self,
            request: models.ListAggregatorsRequest,
            opts: Dict = None,
    ) -> models.ListAggregatorsResponse:
        """
        账号组列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregators"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregatorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCompliancePacks(
            self,
            request: models.ListCompliancePacksRequest,
            opts: Dict = None,
    ) -> models.ListCompliancePacksResponse:
        """
        获取合规包列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListCompliancePacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCompliancePacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConfigRuleEvaluationResults(
            self,
            request: models.ListConfigRuleEvaluationResultsRequest,
            opts: Dict = None,
    ) -> models.ListConfigRuleEvaluationResultsResponse:
        """
        获取评估结果--规则维度（某个规则下资源的评估结果列表）
        """
        
        kwargs = {}
        kwargs["action"] = "ListConfigRuleEvaluationResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConfigRuleEvaluationResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConfigRules(
            self,
            request: models.ListConfigRulesRequest,
            opts: Dict = None,
    ) -> models.ListConfigRulesResponse:
        """
        获取规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListConfigRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConfigRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDiscoveredResources(
            self,
            request: models.ListDiscoveredResourcesRequest,
            opts: Dict = None,
    ) -> models.ListDiscoveredResourcesResponse:
        """
        获取资源列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListDiscoveredResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDiscoveredResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRemediationExecutions(
            self,
            request: models.ListRemediationExecutionsRequest,
            opts: Dict = None,
    ) -> models.ListRemediationExecutionsResponse:
        """
        修正记录
        """
        
        kwargs = {}
        kwargs["action"] = "ListRemediationExecutions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRemediationExecutionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRemediations(
            self,
            request: models.ListRemediationsRequest,
            opts: Dict = None,
    ) -> models.ListRemediationsResponse:
        """
        修正设置列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRemediations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRemediationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListResourceTypes(
            self,
            request: models.ListResourceTypesRequest,
            opts: Dict = None,
    ) -> models.ListResourceTypesResponse:
        """
        获取资源类型列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListResourceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListResourceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSystemCompliancePacks(
            self,
            request: models.ListSystemCompliancePacksRequest,
            opts: Dict = None,
    ) -> models.ListSystemCompliancePacksResponse:
        """
        获取系统合规包列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListSystemCompliancePacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSystemCompliancePacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSystemRules(
            self,
            request: models.ListSystemRulesRequest,
            opts: Dict = None,
    ) -> models.ListSystemRulesResponse:
        """
        获取预设规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListSystemRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSystemRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenAggregateConfigRule(
            self,
            request: models.OpenAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.OpenAggregateConfigRuleResponse:
        """
        账号组开启规则
        """
        
        kwargs = {}
        kwargs["action"] = "OpenAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenConfigRecorder(
            self,
            request: models.OpenConfigRecorderRequest,
            opts: Dict = None,
    ) -> models.OpenConfigRecorderResponse:
        """
        资源监控管理-开启监控
        """
        
        kwargs = {}
        kwargs["action"] = "OpenConfigRecorder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenConfigRecorderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenConfigRule(
            self,
            request: models.OpenConfigRuleRequest,
            opts: Dict = None,
    ) -> models.OpenConfigRuleResponse:
        """
        开启规则
        """
        
        kwargs = {}
        kwargs["action"] = "OpenConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutEvaluations(
            self,
            request: models.PutEvaluationsRequest,
            opts: Dict = None,
    ) -> models.PutEvaluationsResponse:
        """
        上报自定义规则评估结果
        """
        
        kwargs = {}
        kwargs["action"] = "PutEvaluations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutEvaluationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAggregateConfigRuleEvaluation(
            self,
            request: models.StartAggregateConfigRuleEvaluationRequest,
            opts: Dict = None,
    ) -> models.StartAggregateConfigRuleEvaluationResponse:
        """
        账号组触发评估
        """
        
        kwargs = {}
        kwargs["action"] = "StartAggregateConfigRuleEvaluation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAggregateConfigRuleEvaluationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartConfigRuleEvaluation(
            self,
            request: models.StartConfigRuleEvaluationRequest,
            opts: Dict = None,
    ) -> models.StartConfigRuleEvaluationResponse:
        """
        触发评估
        """
        
        kwargs = {}
        kwargs["action"] = "StartConfigRuleEvaluation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartConfigRuleEvaluationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartRemediation(
            self,
            request: models.StartRemediationRequest,
            opts: Dict = None,
    ) -> models.StartRemediationResponse:
        """
        手动执行规则修复
        """
        
        kwargs = {}
        kwargs["action"] = "StartRemediation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartRemediationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAggregateCompliancePack(
            self,
            request: models.UpdateAggregateCompliancePackRequest,
            opts: Dict = None,
    ) -> models.UpdateAggregateCompliancePackResponse:
        """
        账号组编辑合规包
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAggregateCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAggregateCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAggregateCompliancePackStatus(
            self,
            request: models.UpdateAggregateCompliancePackStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateAggregateCompliancePackStatusResponse:
        """
        账号组开启、关闭合规包
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAggregateCompliancePackStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAggregateCompliancePackStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAggregateConfigDeliver(
            self,
            request: models.UpdateAggregateConfigDeliverRequest,
            opts: Dict = None,
    ) -> models.UpdateAggregateConfigDeliverResponse:
        """
        账号组编辑投递设置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAggregateConfigDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAggregateConfigDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAggregateConfigRule(
            self,
            request: models.UpdateAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateAggregateConfigRuleResponse:
        """
        账号组编辑规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCompliancePack(
            self,
            request: models.UpdateCompliancePackRequest,
            opts: Dict = None,
    ) -> models.UpdateCompliancePackResponse:
        """
        编辑合规包
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCompliancePackStatus(
            self,
            request: models.UpdateCompliancePackStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateCompliancePackStatusResponse:
        """
        开启、关闭合规包
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCompliancePackStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCompliancePackStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConfigDeliver(
            self,
            request: models.UpdateConfigDeliverRequest,
            opts: Dict = None,
    ) -> models.UpdateConfigDeliverResponse:
        """
        编辑投递设置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConfigDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConfigDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConfigRecorder(
            self,
            request: models.UpdateConfigRecorderRequest,
            opts: Dict = None,
    ) -> models.UpdateConfigRecorderResponse:
        """
        编辑监控范围
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConfigRecorder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConfigRecorderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConfigRule(
            self,
            request: models.UpdateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateConfigRuleResponse:
        """
        编辑规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRemediation(
            self,
            request: models.UpdateRemediationRequest,
            opts: Dict = None,
    ) -> models.UpdateRemediationResponse:
        """
        新增告警监控规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRemediation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRemediationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)