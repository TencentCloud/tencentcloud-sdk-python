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
from tencentcloud.apm.v20210622 import models
from typing import Dict


class ApmClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'apm.tencentcloudapi.com'
    _service = 'apm'

    async def CreateApmInstance(
            self,
            request: models.CreateApmInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateApmInstanceResponse:
        """
        业务购买 APM 业务系统，调用该接口创建
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApmInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApmInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApmPrometheusRule(
            self,
            request: models.CreateApmPrometheusRuleRequest,
            opts: Dict = None,
    ) -> models.CreateApmPrometheusRuleResponse:
        """
        用于创建apm业务系统与Prometheus实例的指标匹配规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApmPrometheusRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApmPrometheusRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApmSampleConfig(
            self,
            request: models.CreateApmSampleConfigRequest,
            opts: Dict = None,
    ) -> models.CreateApmSampleConfigResponse:
        """
        创建采样配置接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApmSampleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApmSampleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProfileTask(
            self,
            request: models.CreateProfileTaskRequest,
            opts: Dict = None,
    ) -> models.CreateProfileTaskResponse:
        """
        创建事件任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProfileTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProfileTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApmSampleConfig(
            self,
            request: models.DeleteApmSampleConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteApmSampleConfigResponse:
        """
        删除采样配置接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApmSampleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApmSampleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmAgent(
            self,
            request: models.DescribeApmAgentRequest,
            opts: Dict = None,
    ) -> models.DescribeApmAgentResponse:
        """
        获取 APM 接入点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmApplicationConfig(
            self,
            request: models.DescribeApmApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeApmApplicationConfigResponse:
        """
        查询应用配置接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmAssociation(
            self,
            request: models.DescribeApmAssociationRequest,
            opts: Dict = None,
    ) -> models.DescribeApmAssociationResponse:
        """
        用于查询apm业务系统与其他产品的关联关系
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmAssociation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmAssociationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmInstances(
            self,
            request: models.DescribeApmInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeApmInstancesResponse:
        """
        获取 APM 业务系统列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmPrometheusRule(
            self,
            request: models.DescribeApmPrometheusRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeApmPrometheusRuleResponse:
        """
        用于查询apm业务系统与Prometheus实例的指标匹配规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmPrometheusRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmPrometheusRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmSampleConfig(
            self,
            request: models.DescribeApmSampleConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeApmSampleConfigResponse:
        """
        查询采样配置接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmSampleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmSampleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmServiceMetric(
            self,
            request: models.DescribeApmServiceMetricRequest,
            opts: Dict = None,
    ) -> models.DescribeApmServiceMetricResponse:
        """
        获取 APM 应用指标列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmServiceMetric"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmServiceMetricResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralApmApplicationConfig(
            self,
            request: models.DescribeGeneralApmApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralApmApplicationConfigResponse:
        """
        查询应用配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralApmApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralApmApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralMetricData(
            self,
            request: models.DescribeGeneralMetricDataRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralMetricDataResponse:
        """
        获取指标数据通用接口。用户根据需要上送请求参数，返回对应的指标数据。
        接口调用频率限制为：20次/秒，1200次/分钟。单请求的数据点数限制为1440个。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralMetricData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralMetricDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralOTSpanList(
            self,
            request: models.DescribeGeneralOTSpanListRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralOTSpanListResponse:
        """
        通用查询 OpenTelemetry 调用链列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralOTSpanList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralOTSpanListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralSpanList(
            self,
            request: models.DescribeGeneralSpanListRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralSpanListResponse:
        """
        通用查询调用链列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralSpanList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralSpanListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricRecords(
            self,
            request: models.DescribeMetricRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricRecordsResponse:
        """
        查询指标列表接口，查询指标更推荐使用DescribeGeneralMetricData接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceOverview(
            self,
            request: models.DescribeServiceOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceOverviewResponse:
        """
        应用概览数据拉取
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagValues(
            self,
            request: models.DescribeTagValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeTagValuesResponse:
        """
        根据维度名和过滤条件，查询维度数据.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopologyNew(
            self,
            request: models.DescribeTopologyNewRequest,
            opts: Dict = None,
    ) -> models.DescribeTopologyNewResponse:
        """
        根据应用名查询服务拓扑图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopologyNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopologyNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmApplicationConfig(
            self,
            request: models.ModifyApmApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyApmApplicationConfigResponse:
        """
        修改应用配置接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmAssociation(
            self,
            request: models.ModifyApmAssociationRequest,
            opts: Dict = None,
    ) -> models.ModifyApmAssociationResponse:
        """
        用于修改apm业务系统与其他产品的关联关系（包括创建和删除）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmAssociation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmAssociationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmInstance(
            self,
            request: models.ModifyApmInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyApmInstanceResponse:
        """
        修改APM业务系统接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmPrometheusRule(
            self,
            request: models.ModifyApmPrometheusRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyApmPrometheusRuleResponse:
        """
        用于修改apm业务系统与Prometheus实例的指标匹配规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmPrometheusRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmPrometheusRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmSampleConfig(
            self,
            request: models.ModifyApmSampleConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyApmSampleConfigResponse:
        """
        修改采样配置接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmSampleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmSampleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGeneralApmApplicationConfig(
            self,
            request: models.ModifyGeneralApmApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyGeneralApmApplicationConfigResponse:
        """
        对外开放的openApi，客户可以灵活的指定需要修改的字段，再加入需要修改的服务列表.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGeneralApmApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGeneralApmApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateApmInstance(
            self,
            request: models.TerminateApmInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateApmInstanceResponse:
        """
        销毁 APM 业务系统
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateApmInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateApmInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)