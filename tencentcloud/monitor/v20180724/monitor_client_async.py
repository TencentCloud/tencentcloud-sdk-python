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
from tencentcloud.monitor.v20180724 import models
from typing import Dict


class MonitorClient(AbstractClient):
    _apiVersion = '2018-07-24'
    _endpoint = 'monitor.tencentcloudapi.com'
    _service = 'monitor'

    async def BindPrometheusManagedGrafana(
            self,
            request: models.BindPrometheusManagedGrafanaRequest,
            opts: Dict = None,
    ) -> models.BindPrometheusManagedGrafanaResponse:
        """
        绑定 Grafana 可视化服务实例
        """
        
        kwargs = {}
        kwargs["action"] = "BindPrometheusManagedGrafana"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindPrometheusManagedGrafanaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindingPolicyObject(
            self,
            request: models.BindingPolicyObjectRequest,
            opts: Dict = None,
    ) -> models.BindingPolicyObjectResponse:
        """
        将告警策略绑定到特定对象
        """
        
        kwargs = {}
        kwargs["action"] = "BindingPolicyObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindingPolicyObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindingPolicyTag(
            self,
            request: models.BindingPolicyTagRequest,
            opts: Dict = None,
    ) -> models.BindingPolicyTagResponse:
        """
        策略绑定标签
        """
        
        kwargs = {}
        kwargs["action"] = "BindingPolicyTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindingPolicyTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CleanGrafanaInstance(
            self,
            request: models.CleanGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.CleanGrafanaInstanceResponse:
        """
        强制销毁 Grafana 实例
        """
        
        kwargs = {}
        kwargs["action"] = "CleanGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CleanGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarmNotice(
            self,
            request: models.CreateAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmNoticeResponse:
        """
        创建通知模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarmPolicy(
            self,
            request: models.CreateAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmPolicyResponse:
        """
        创建告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarmShield(
            self,
            request: models.CreateAlarmShieldRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmShieldResponse:
        """
        创建告警屏蔽规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarmShield"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmShieldResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlertRule(
            self,
            request: models.CreateAlertRuleRequest,
            opts: Dict = None,
    ) -> models.CreateAlertRuleResponse:
        """
        创建 Prometheus 告警规则。

        请注意，**告警对象和告警消息是 Prometheus Rule Annotations 的特殊字段，需要通过 annotations 来传递，对应的 Key 分别为summary/description**，，请参考 [Prometheus Rule更多配置请参考](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConditionsTemplate(
            self,
            request: models.CreateConditionsTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateConditionsTemplateResponse:
        """
        创建告警条件模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConditionsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConditionsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExporterIntegration(
            self,
            request: models.CreateExporterIntegrationRequest,
            opts: Dict = None,
    ) -> models.CreateExporterIntegrationResponse:
        """
        创建集成中心 exporter 集成，因集成较多，建议控制台创建集成。(前提：已授权创建托管 EKS 集群，验证方式：1. 控制台界面确认，未提示授权则表示已授权创建；2. 通过 DescribePrometheusInstanceInitStatus 接口查询集群状态，如果托管集群不存在，可通过 RunPrometheusInstance 接口创建)
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExporterIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExporterIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExternalCluster(
            self,
            request: models.CreateExternalClusterRequest,
            opts: Dict = None,
    ) -> models.CreateExternalClusterResponse:
        """
        注册外部集群到云上 TMP 实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExternalCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExternalClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGrafanaInstance(
            self,
            request: models.CreateGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateGrafanaInstanceResponse:
        """
        本接口（CreateGrafanaInstance）用于创建 Grafana 包年包月实例，默认基础版、到期自动续费。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGrafanaIntegration(
            self,
            request: models.CreateGrafanaIntegrationRequest,
            opts: Dict = None,
    ) -> models.CreateGrafanaIntegrationResponse:
        """
        创建 Grafana 集成配置，其中 Prometheus 集成不通过该接口创建，可参考 BindPrometheusManagedGrafana 接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGrafanaIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGrafanaIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGrafanaNotificationChannel(
            self,
            request: models.CreateGrafanaNotificationChannelRequest,
            opts: Dict = None,
    ) -> models.CreateGrafanaNotificationChannelResponse:
        """
        创建 Grafana 告警通道
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGrafanaNotificationChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGrafanaNotificationChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePolicyGroup(
            self,
            request: models.CreatePolicyGroupRequest,
            opts: Dict = None,
    ) -> models.CreatePolicyGroupResponse:
        """
        增加策略组
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePolicyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePolicyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusAgent(
            self,
            request: models.CreatePrometheusAgentRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusAgentResponse:
        """
        创建 Prometheus CVM Agent
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusAlertGroup(
            self,
            request: models.CreatePrometheusAlertGroupRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusAlertGroupResponse:
        """
        创建Prometheus告警规则分组

        告警分组中可包含多条告警规则，分组内告警消息通过告警分组的通知模板发送。
        支持单个告警分组下分别创建启用/禁用的告警规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusAlertGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusAlertGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusAlertPolicy(
            self,
            request: models.CreatePrometheusAlertPolicyRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusAlertPolicyResponse:
        """
        创建 Prometheus 告警策略(将逐步废弃，建议使用 CreatePrometheusAlertGroup 创建告警策略)
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusAlertPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusAlertPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusClusterAgent(
            self,
            request: models.CreatePrometheusClusterAgentRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusClusterAgentResponse:
        """
        与腾讯云可观测融合的2.0实例关联集群
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
        创建prometheus配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusGlobalNotification(
            self,
            request: models.CreatePrometheusGlobalNotificationRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusGlobalNotificationResponse:
        """
        创建全局告警通知渠道。集群内创建的告警规则如果未配置告警通知渠道，默认走全局告警通知渠道（建议在控制台创建告警，集群内创建告警不易维护）
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusGlobalNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusGlobalNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusMultiTenantInstancePostPayMode(
            self,
            request: models.CreatePrometheusMultiTenantInstancePostPayModeRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusMultiTenantInstancePostPayModeResponse:
        """
        创建按量 Prometheus 实例，根据用量收费实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusMultiTenantInstancePostPayMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusMultiTenantInstancePostPayModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusRecordRuleYaml(
            self,
            request: models.CreatePrometheusRecordRuleYamlRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusRecordRuleYamlResponse:
        """
        以Yaml的方式创建聚合规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusRecordRuleYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusRecordRuleYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusScrapeJob(
            self,
            request: models.CreatePrometheusScrapeJobRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusScrapeJobResponse:
        """
        创建 Prometheus Agent 抓取任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusScrapeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusScrapeJobResponse
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
        
    async def CreateRecordingRule(
            self,
            request: models.CreateRecordingRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRecordingRuleResponse:
        """
        创建 Prometheus 的预聚合规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSSOAccount(
            self,
            request: models.CreateSSOAccountRequest,
            opts: Dict = None,
    ) -> models.CreateSSOAccountResponse:
        """
        Grafana实例授权其他腾讯云用户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSSOAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSSOAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceDiscovery(
            self,
            request: models.CreateServiceDiscoveryRequest,
            opts: Dict = None,
    ) -> models.CreateServiceDiscoveryResponse:
        """
        在腾讯云容器服务下创建 Prometheus 服务发现。
        <p>注意：前提条件，已经通过 Prometheus 控制台集成了对应的腾讯云容器服务，具体请参考
        <a href="https://cloud.tencent.com/document/product/248/48859" target="_blank">Agent 安装</a>。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceDiscovery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceDiscoveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarmNotices(
            self,
            request: models.DeleteAlarmNoticesRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmNoticesResponse:
        """
        删除告警通知模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmNotices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmNoticesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarmPolicy(
            self,
            request: models.DeleteAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmPolicyResponse:
        """
        删除告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarmShields(
            self,
            request: models.DeleteAlarmShieldsRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmShieldsResponse:
        """
        删除告警屏蔽规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmShields"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmShieldsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlertRules(
            self,
            request: models.DeleteAlertRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteAlertRulesResponse:
        """
        批量删除 Prometheus 报警规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlertRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlertRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteExporterIntegration(
            self,
            request: models.DeleteExporterIntegrationRequest,
            opts: Dict = None,
    ) -> models.DeleteExporterIntegrationResponse:
        """
        删除集成中心 exporter 集成
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteExporterIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteExporterIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGrafanaInstance(
            self,
            request: models.DeleteGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteGrafanaInstanceResponse:
        """
        本接口（DeleteGrafanaInstance）用于 Grafana 包年包月实例的退费，调用后实例处于停服状态，不可使用，7天后自动销毁。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGrafanaIntegration(
            self,
            request: models.DeleteGrafanaIntegrationRequest,
            opts: Dict = None,
    ) -> models.DeleteGrafanaIntegrationResponse:
        """
        删除 Grafana 集成配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGrafanaIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGrafanaIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGrafanaNotificationChannel(
            self,
            request: models.DeleteGrafanaNotificationChannelRequest,
            opts: Dict = None,
    ) -> models.DeleteGrafanaNotificationChannelResponse:
        """
        删除 Grafana 告警通道
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGrafanaNotificationChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGrafanaNotificationChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePolicyGroup(
            self,
            request: models.DeletePolicyGroupRequest,
            opts: Dict = None,
    ) -> models.DeletePolicyGroupResponse:
        """
        删除告警策略组
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePolicyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePolicyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusAlertGroups(
            self,
            request: models.DeletePrometheusAlertGroupsRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusAlertGroupsResponse:
        """
        删除Prometheus告警规则分组
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusAlertGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusAlertGroupsResponse
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
        删除Prometheus配置，如果目标不存在，将返回成功
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
        删除聚合实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusRecordRuleYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusRecordRuleYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusScrapeJobs(
            self,
            request: models.DeletePrometheusScrapeJobsRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusScrapeJobsResponse:
        """
        删除 Prometheus Agent 抓取任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusScrapeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusScrapeJobsResponse
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
        
    async def DeleteRecordingRules(
            self,
            request: models.DeleteRecordingRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordingRulesResponse:
        """
        批量删除 Prometheus 预聚合规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordingRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordingRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSSOAccount(
            self,
            request: models.DeleteSSOAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteSSOAccountResponse:
        """
        Grafana可视化服务 删除授权用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSSOAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSSOAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceDiscovery(
            self,
            request: models.DeleteServiceDiscoveryRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceDiscoveryResponse:
        """
        删除在腾讯云容器服务下创建的 Prometheus 服务发现。
        <p>注意：前提条件，已经通过 Prometheus 控制台集成了对应的腾讯云容器服务，具体请参考
        <a href="https://cloud.tencent.com/document/product/248/48859" target="_blank">Agent 安装</a>。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceDiscovery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceDiscoveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccidentEventList(
            self,
            request: models.DescribeAccidentEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeAccidentEventListResponse:
        """
        获取平台事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccidentEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccidentEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmEvents(
            self,
            request: models.DescribeAlarmEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmEventsResponse:
        """
        查询告警事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmHistories(
            self,
            request: models.DescribeAlarmHistoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmHistoriesResponse:
        """
        查询告警历史

        请注意，**如果使用子用户进行告警历史的查询，只能查询到被授权项目下的告警历史**，或不区分项目的产品的告警历史。如何对子账户授予项目的权限，请参考 [访问管理-项目与标签](https://cloud.tencent.com/document/product/598/32738)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmHistories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmHistoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmMetrics(
            self,
            request: models.DescribeAlarmMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmMetricsResponse:
        """
        查询告警指标列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNotice(
            self,
            request: models.DescribeAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNoticeResponse:
        """
        查询单个通知模板的详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNoticeCallbacks(
            self,
            request: models.DescribeAlarmNoticeCallbacksRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNoticeCallbacksResponse:
        """
        获取告警通知模板所有回调URL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNoticeCallbacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNoticeCallbacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNotices(
            self,
            request: models.DescribeAlarmNoticesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNoticesResponse:
        """
        查询通知模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNotices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNoticesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmPolicies(
            self,
            request: models.DescribeAlarmPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmPoliciesResponse:
        """
        查询告警策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmPolicy(
            self,
            request: models.DescribeAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmPolicyResponse:
        """
        获取单个告警策略详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmSmsQuota(
            self,
            request: models.DescribeAlarmSmsQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmSmsQuotaResponse:
        """
        获取告警短信配额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmSmsQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmSmsQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlertRules(
            self,
            request: models.DescribeAlertRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlertRulesResponse:
        """
        Prometheus 报警规则查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlertRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlertRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllNamespaces(
            self,
            request: models.DescribeAllNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeAllNamespacesResponse:
        """
        查询所有名字空间
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaseMetrics(
            self,
            request: models.DescribeBaseMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeBaseMetricsResponse:
        """
        获取基础指标属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaseMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaseMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBasicAlarmList(
            self,
            request: models.DescribeBasicAlarmListRequest,
            opts: Dict = None,
    ) -> models.DescribeBasicAlarmListResponse:
        """
        获取基础告警列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBasicAlarmList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBasicAlarmListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindingPolicyObjectList(
            self,
            request: models.DescribeBindingPolicyObjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeBindingPolicyObjectListResponse:
        """
        获取已绑定对象列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindingPolicyObjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindingPolicyObjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAgentCreatingProgress(
            self,
            request: models.DescribeClusterAgentCreatingProgressRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAgentCreatingProgressResponse:
        """
        获取prom实例中集群详细的关联状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAgentCreatingProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAgentCreatingProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConditionsTemplateList(
            self,
            request: models.DescribeConditionsTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeConditionsTemplateListResponse:
        """
        获取条件模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConditionsTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConditionsTemplateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDNSConfig(
            self,
            request: models.DescribeDNSConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDNSConfigResponse:
        """
        列出 Grafana DNS 配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDNSConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDNSConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExporterIntegrations(
            self,
            request: models.DescribeExporterIntegrationsRequest,
            opts: Dict = None,
    ) -> models.DescribeExporterIntegrationsResponse:
        """
        查询集成中心 exporter 集成列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExporterIntegrations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExporterIntegrationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExternalClusterRegisterCommand(
            self,
            request: models.DescribeExternalClusterRegisterCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeExternalClusterRegisterCommandResponse:
        """
        查看外部集群注册命令
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExternalClusterRegisterCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExternalClusterRegisterCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExternalClusterUninstallCommand(
            self,
            request: models.DescribeExternalClusterUninstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeExternalClusterUninstallCommandResponse:
        """
        查看外部集群 Agent 卸载命令
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExternalClusterUninstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExternalClusterUninstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaChannels(
            self,
            request: models.DescribeGrafanaChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaChannelsResponse:
        """
        列出 Grafana 所有告警通道
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaConfig(
            self,
            request: models.DescribeGrafanaConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaConfigResponse:
        """
        列出 Grafana 的设置，即 grafana.ini 文件内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaEnvironments(
            self,
            request: models.DescribeGrafanaEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaEnvironmentsResponse:
        """
        列出 Grafana 环境变量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaInstances(
            self,
            request: models.DescribeGrafanaInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaInstancesResponse:
        """
        列出用户所有的 Grafana 服务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaIntegrations(
            self,
            request: models.DescribeGrafanaIntegrationsRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaIntegrationsResponse:
        """
        列出 Grafana 已安装的集成
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaIntegrations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaIntegrationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaNotificationChannels(
            self,
            request: models.DescribeGrafanaNotificationChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaNotificationChannelsResponse:
        """
        列出 Grafana 告警通道
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaNotificationChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaNotificationChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaWhiteList(
            self,
            request: models.DescribeGrafanaWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaWhiteListResponse:
        """
        列出 Grafana 白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstalledPlugins(
            self,
            request: models.DescribeInstalledPluginsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstalledPluginsResponse:
        """
        列出实例已安装的插件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstalledPlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstalledPluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonitorResourceInfo(
            self,
            request: models.DescribeMonitorResourceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeMonitorResourceInfoResponse:
        """
        获取资源消耗页概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonitorResourceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonitorResourceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonitorTypes(
            self,
            request: models.DescribeMonitorTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeMonitorTypesResponse:
        """
        腾讯云可观测平台支持多种类型的监控，此接口列出支持的所有类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonitorTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonitorTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePhoneAlarmFlowTotalCount(
            self,
            request: models.DescribePhoneAlarmFlowTotalCountRequest,
            opts: Dict = None,
    ) -> models.DescribePhoneAlarmFlowTotalCountResponse:
        """
        查询周期内电话流水总数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePhoneAlarmFlowTotalCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePhoneAlarmFlowTotalCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePluginOverviews(
            self,
            request: models.DescribePluginOverviewsRequest,
            opts: Dict = None,
    ) -> models.DescribePluginOverviewsResponse:
        """
        列出可安装的所有 Grafana 插件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePluginOverviews"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginOverviewsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyConditionList(
            self,
            request: models.DescribePolicyConditionListRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyConditionListResponse:
        """
        获取基础告警策略条件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyConditionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyConditionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyGroupInfo(
            self,
            request: models.DescribePolicyGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyGroupInfoResponse:
        """
        获取基础策略组详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyGroupList(
            self,
            request: models.DescribePolicyGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyGroupListResponse:
        """
        获取基础策略告警组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyObjectCount(
            self,
            request: models.DescribePolicyObjectCountRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyObjectCountResponse:
        """
        查询策略组在每个地域下面绑定的对象数统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyObjectCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyObjectCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductEventList(
            self,
            request: models.DescribeProductEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeProductEventListResponse:
        """
        分页获取产品事件的列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductList(
            self,
            request: models.DescribeProductListRequest,
            opts: Dict = None,
    ) -> models.DescribeProductListResponse:
        """
        查询腾讯云可观测平台云产品列表，支持云服务器CVM、云数据库、云消息队列、负载均衡、容器服务、专线等云产品。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductListResponse
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
        列出 Prometheus CVM Agent
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAgents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAgentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusAlertGroups(
            self,
            request: models.DescribePrometheusAlertGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusAlertGroupsResponse:
        """
        查询给定prometheus下的告警分组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAlertGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAlertGroupsResponse
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
        拉取Prometheus配置
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
        
    async def DescribePrometheusInstanceDetail(
            self,
            request: models.DescribePrometheusInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstanceDetailResponse:
        """
        获取TMP实例详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstanceDetailResponse
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
        
    async def DescribePrometheusInstanceUsage(
            self,
            request: models.DescribePrometheusInstanceUsageRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstanceUsageResponse:
        """
        查询Prometheus按量实例用量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstanceUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstanceUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstances(
            self,
            request: models.DescribePrometheusInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstancesResponse:
        """
        本接口 (DescribePrometheusInstances) 用于查询一个或多个实例的详细信息。
        <ul>
        <li>可以根据实例ID、实例名称或者实例状态等信息来查询实例的详细信息</li>
        <li>如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的实例。</li>
        </ul>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstancesOverview(
            self,
            request: models.DescribePrometheusInstancesOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstancesOverviewResponse:
        """
        获取与 Prometheus 监控融合实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstancesOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstancesOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusIntegrationMetrics(
            self,
            request: models.DescribePrometheusIntegrationMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusIntegrationMetricsResponse:
        """
        获取prometheus集成指标
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusIntegrationMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusIntegrationMetricsResponse
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
        
    async def DescribePrometheusRegions(
            self,
            request: models.DescribePrometheusRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusRegionsResponse:
        """
        列出 Prometheus 服务所有可用的地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusScrapeJobs(
            self,
            request: models.DescribePrometheusScrapeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusScrapeJobsResponse:
        """
        列出 Prometheus 抓取任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusScrapeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusScrapeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusScrapeStatistics(
            self,
            request: models.DescribePrometheusScrapeStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusScrapeStatisticsResponse:
        """
        获取实例采集速率信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusScrapeStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusScrapeStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusTargetsTMP(
            self,
            request: models.DescribePrometheusTargetsTMPRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusTargetsTMPResponse:
        """
        获取targets信息，在过滤条件中指定job名称时返回targets详情，否则仅返回数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusTargetsTMP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusTargetsTMPResponse
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
        
    async def DescribePrometheusZones(
            self,
            request: models.DescribePrometheusZonesRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusZonesResponse:
        """
        列出 Prometheus 服务可用区。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordingRules(
            self,
            request: models.DescribeRecordingRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordingRulesResponse:
        """
        根据条件查询 Prometheus 预聚合规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordingRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordingRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRemoteURLs(
            self,
            request: models.DescribeRemoteURLsRequest,
            opts: Dict = None,
    ) -> models.DescribeRemoteURLsResponse:
        """
        获取多写配置详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRemoteURLs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRemoteURLsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRemoteWrites(
            self,
            request: models.DescribeRemoteWritesRequest,
            opts: Dict = None,
    ) -> models.DescribeRemoteWritesResponse:
        """
        查询安装的 Agent 列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRemoteWrites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRemoteWritesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSSOAccount(
            self,
            request: models.DescribeSSOAccountRequest,
            opts: Dict = None,
    ) -> models.DescribeSSOAccountResponse:
        """
        列出当前grafana实例的所有授权账号
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSSOAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSSOAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceDiscovery(
            self,
            request: models.DescribeServiceDiscoveryRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceDiscoveryResponse:
        """
        列出在腾讯云容器服务下创建的 Prometheus 服务发现。
        <p>注意：前提条件，已经通过 Prometheus 控制台集成了对应的腾讯云容器服务，具体请参考
        <a href="https://cloud.tencent.com/document/product/248/48859" target="_blank">Agent 安装</a>。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceDiscovery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceDiscoveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStatisticData(
            self,
            request: models.DescribeStatisticDataRequest,
            opts: Dict = None,
    ) -> models.DescribeStatisticDataResponse:
        """
        根据维度条件查询监控数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStatisticData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStatisticDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPrometheusInstance(
            self,
            request: models.DestroyPrometheusInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyPrometheusInstanceResponse:
        """
        彻底删除 Prometheus 实例相关数据，给定的实例必须先被 Terminate(该接口是异步接口，实例是否释放需要通过 DescribePrometheusInstances 接口返回的状态来判断)。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPrometheusInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPrometheusInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableGrafanaInternet(
            self,
            request: models.EnableGrafanaInternetRequest,
            opts: Dict = None,
    ) -> models.EnableGrafanaInternetResponse:
        """
        设置 Grafana 公网访问
        """
        
        kwargs = {}
        kwargs["action"] = "EnableGrafanaInternet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableGrafanaInternetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableGrafanaSSO(
            self,
            request: models.EnableGrafanaSSORequest,
            opts: Dict = None,
    ) -> models.EnableGrafanaSSOResponse:
        """
        设置 Grafana 单点登录，使用腾讯云账号
        """
        
        kwargs = {}
        kwargs["action"] = "EnableGrafanaSSO"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableGrafanaSSOResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableSSOCamCheck(
            self,
            request: models.EnableSSOCamCheckRequest,
            opts: Dict = None,
    ) -> models.EnableSSOCamCheckResponse:
        """
        SSO单点登录时，设置是否cam鉴权
        """
        
        kwargs = {}
        kwargs["action"] = "EnableSSOCamCheck"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableSSOCamCheckResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportPrometheusReadOnlyDynamicAPI(
            self,
            request: models.ExportPrometheusReadOnlyDynamicAPIRequest,
            opts: Dict = None,
    ) -> models.ExportPrometheusReadOnlyDynamicAPIResponse:
        """
        Prometheus 内部动态 api 代理，仅内部使用
        """
        
        kwargs = {}
        kwargs["action"] = "ExportPrometheusReadOnlyDynamicAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportPrometheusReadOnlyDynamicAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMonitorData(
            self,
            request: models.GetMonitorDataRequest,
            opts: Dict = None,
    ) -> models.GetMonitorDataResponse:
        """
        获取云产品的监控数据。此接口不适用于拉取容器服务监控数据，如需拉取容器服务监控数据，请使用[根据维度条件查询监控数据](https://cloud.tencent.com/document/product/248/51845)接口。
        传入产品的命名空间、对象维度描述和监控指标即可获得相应的监控数据。
        接口调用限制：单请求最多可支持批量拉取10个实例的监控数据，单请求的数据点数限制为1440个。
        若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。
        拉取数据的粒度和统计方式的对应关系尽量在接入平台进行配置，如果没有配置对应统计方式，请提工单反馈。

        >?
        >- 2022年9月1日起，腾讯云可观测平台开始对GetMonitorData接口计费。每个主账号每月可获得100万次免费请求额度，超过免费额度后如需继续调用接口需要开通 [API请求按量付费](https://buy.cloud.tencent.com/APIRequestBuy)。计费规则可查看[API计费文档](https://cloud.tencent.com/document/product/248/77914)。
        """
        
        kwargs = {}
        kwargs["action"] = "GetMonitorData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMonitorDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPrometheusAgentManagementCommand(
            self,
            request: models.GetPrometheusAgentManagementCommandRequest,
            opts: Dict = None,
    ) -> models.GetPrometheusAgentManagementCommandResponse:
        """
        获取 Prometheus Agent 管理相关的命令行
        """
        
        kwargs = {}
        kwargs["action"] = "GetPrometheusAgentManagementCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPrometheusAgentManagementCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTopNMonitorData(
            self,
            request: models.GetTopNMonitorDataRequest,
            opts: Dict = None,
    ) -> models.GetTopNMonitorDataResponse:
        """
        支持TopN查询，对于给定的监控指标和时间区间，按照指标大小按序返回不同维度组合及数据。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTopNMonitorData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTopNMonitorDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallPlugins(
            self,
            request: models.InstallPluginsRequest,
            opts: Dict = None,
    ) -> models.InstallPluginsResponse:
        """
        安装 Grafana Plugin
        """
        
        kwargs = {}
        kwargs["action"] = "InstallPlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallPluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmNotice(
            self,
            request: models.ModifyAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmNoticeResponse:
        """
        编辑告警通知模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicyCondition(
            self,
            request: models.ModifyAlarmPolicyConditionRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyConditionResponse:
        """
        修改告警策略触发条件
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicyCondition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyConditionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicyInfo(
            self,
            request: models.ModifyAlarmPolicyInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyInfoResponse:
        """
        告警2.0编辑告警策略基本信息，包括策略名、备注
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicyNotice(
            self,
            request: models.ModifyAlarmPolicyNoticeRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyNoticeResponse:
        """
        修改告警策略绑定的告警通知模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicyNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicyStatus(
            self,
            request: models.ModifyAlarmPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyStatusResponse:
        """
        启停告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicyTasks(
            self,
            request: models.ModifyAlarmPolicyTasksRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyTasksResponse:
        """
        修改告警策略的触发任务，TriggerTasks字段放触发任务列表，TriggerTasks传空数组时，代表解绑该策略的所有触发任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicyTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmReceivers(
            self,
            request: models.ModifyAlarmReceiversRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmReceiversResponse:
        """
        修改告警接收人
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmReceivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmReceiversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGrafanaInstance(
            self,
            request: models.ModifyGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyGrafanaInstanceResponse:
        """
        修改 Grafana 实例属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPolicyGroup(
            self,
            request: models.ModifyPolicyGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyPolicyGroupResponse:
        """
        更新策略组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPolicyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPolicyGroupResponse
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
        
    async def ModifyPrometheusConfig(
            self,
            request: models.ModifyPrometheusConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusConfigResponse:
        """
        修改prometheus采集配置
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
        
    async def ModifyPrometheusInstanceAttributes(
            self,
            request: models.ModifyPrometheusInstanceAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusInstanceAttributesResponse:
        """
        修改 Prometheus 实例相关属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusInstanceAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusInstanceAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusRecordRuleYaml(
            self,
            request: models.ModifyPrometheusRecordRuleYamlRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusRecordRuleYamlResponse:
        """
        通过yaml的方式修改Prometheus预聚合规则
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
        
    async def ModifyRemoteURLs(
            self,
            request: models.ModifyRemoteURLsRequest,
            opts: Dict = None,
    ) -> models.ModifyRemoteURLsResponse:
        """
        修改多写配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRemoteURLs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRemoteURLsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeGrafanaInstance(
            self,
            request: models.ResumeGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.ResumeGrafanaInstanceResponse:
        """
        本接口（ResumeGrafanaInstance）用于 Grafana 包年包月实例的停服续费，调用后按原版本续费一个月。仍在运行中的实例无法使用该接口进行续费。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeGrafanaInstanceResponse
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
        
    async def SetDefaultAlarmPolicy(
            self,
            request: models.SetDefaultAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.SetDefaultAlarmPolicyResponse:
        """
        设置一个策略为该告警策略类型、该项目的默认告警策略。
        同一项目下相同的告警策略类型，就会被设置为非默认。
        """
        
        kwargs = {}
        kwargs["action"] = "SetDefaultAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetDefaultAlarmPolicyResponse
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
        
    async def TerminatePrometheusInstances(
            self,
            request: models.TerminatePrometheusInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminatePrometheusInstancesResponse:
        """
        销毁按量 Prometheus 实例
        """
        
        kwargs = {}
        kwargs["action"] = "TerminatePrometheusInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminatePrometheusInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindingAllPolicyObject(
            self,
            request: models.UnBindingAllPolicyObjectRequest,
            opts: Dict = None,
    ) -> models.UnBindingAllPolicyObjectResponse:
        """
        删除全部的关联对象
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindingAllPolicyObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindingAllPolicyObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindingPolicyObject(
            self,
            request: models.UnBindingPolicyObjectRequest,
            opts: Dict = None,
    ) -> models.UnBindingPolicyObjectResponse:
        """
        删除策略的关联对象
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindingPolicyObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindingPolicyObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindPrometheusManagedGrafana(
            self,
            request: models.UnbindPrometheusManagedGrafanaRequest,
            opts: Dict = None,
    ) -> models.UnbindPrometheusManagedGrafanaResponse:
        """
        解除实例绑定的 Grafana 可视化实例
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindPrometheusManagedGrafana"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindPrometheusManagedGrafanaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallGrafanaDashboard(
            self,
            request: models.UninstallGrafanaDashboardRequest,
            opts: Dict = None,
    ) -> models.UninstallGrafanaDashboardResponse:
        """
        删除 Grafana Dashboard
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallGrafanaDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallGrafanaDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallGrafanaPlugins(
            self,
            request: models.UninstallGrafanaPluginsRequest,
            opts: Dict = None,
    ) -> models.UninstallGrafanaPluginsResponse:
        """
        删除已安装的插件
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallGrafanaPlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallGrafanaPluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlertRule(
            self,
            request: models.UpdateAlertRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateAlertRuleResponse:
        """
        更新 Prometheus 的告警规则。

        请注意，**告警对象和告警消息是 Prometheus Rule Annotations 的特殊字段，需要通过 annotations 来传递，对应的 Key 分别为summary/description**，请参考 [Prometheus Rule更多配置请参考](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlertRuleState(
            self,
            request: models.UpdateAlertRuleStateRequest,
            opts: Dict = None,
    ) -> models.UpdateAlertRuleStateResponse:
        """
        更新 Prometheus 报警策略状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlertRuleState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAlertRuleStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDNSConfig(
            self,
            request: models.UpdateDNSConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateDNSConfigResponse:
        """
        更新 Grafana 的 DNS 配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDNSConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDNSConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateExporterIntegration(
            self,
            request: models.UpdateExporterIntegrationRequest,
            opts: Dict = None,
    ) -> models.UpdateExporterIntegrationResponse:
        """
        更新 exporter 集成配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateExporterIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateExporterIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGrafanaConfig(
            self,
            request: models.UpdateGrafanaConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateGrafanaConfigResponse:
        """
        更新 Grafana 配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGrafanaConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGrafanaConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGrafanaEnvironments(
            self,
            request: models.UpdateGrafanaEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.UpdateGrafanaEnvironmentsResponse:
        """
        更新 Grafana 环境变量
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGrafanaEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGrafanaEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGrafanaIntegration(
            self,
            request: models.UpdateGrafanaIntegrationRequest,
            opts: Dict = None,
    ) -> models.UpdateGrafanaIntegrationResponse:
        """
        更新 Grafana 集成配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGrafanaIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGrafanaIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGrafanaNotificationChannel(
            self,
            request: models.UpdateGrafanaNotificationChannelRequest,
            opts: Dict = None,
    ) -> models.UpdateGrafanaNotificationChannelResponse:
        """
        更新 Grafana 告警通道
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGrafanaNotificationChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGrafanaNotificationChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGrafanaWhiteList(
            self,
            request: models.UpdateGrafanaWhiteListRequest,
            opts: Dict = None,
    ) -> models.UpdateGrafanaWhiteListResponse:
        """
        更新 Grafana 白名单
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGrafanaWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGrafanaWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePrometheusAgentStatus(
            self,
            request: models.UpdatePrometheusAgentStatusRequest,
            opts: Dict = None,
    ) -> models.UpdatePrometheusAgentStatusResponse:
        """
        更新 Prometheus CVM Agent 状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePrometheusAgentStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePrometheusAgentStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePrometheusAlertGroup(
            self,
            request: models.UpdatePrometheusAlertGroupRequest,
            opts: Dict = None,
    ) -> models.UpdatePrometheusAlertGroupResponse:
        """
        更新Prometheus告警规则分组
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePrometheusAlertGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePrometheusAlertGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePrometheusAlertGroupState(
            self,
            request: models.UpdatePrometheusAlertGroupStateRequest,
            opts: Dict = None,
    ) -> models.UpdatePrometheusAlertGroupStateResponse:
        """
        批量更新告警分组状态，将分组中全部告警规则更新为目标状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePrometheusAlertGroupState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePrometheusAlertGroupStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePrometheusScrapeJob(
            self,
            request: models.UpdatePrometheusScrapeJobRequest,
            opts: Dict = None,
    ) -> models.UpdatePrometheusScrapeJobResponse:
        """
        更新 Prometheus Agent 抓取任务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePrometheusScrapeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePrometheusScrapeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordingRule(
            self,
            request: models.UpdateRecordingRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordingRuleResponse:
        """
        更新 Prometheus 的预聚合规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSSOAccount(
            self,
            request: models.UpdateSSOAccountRequest,
            opts: Dict = None,
    ) -> models.UpdateSSOAccountResponse:
        """
        更新已授权账号的备注、权限信息，会直接覆盖原有的信息，不传则不会更新。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSSOAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSSOAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateServiceDiscovery(
            self,
            request: models.UpdateServiceDiscoveryRequest,
            opts: Dict = None,
    ) -> models.UpdateServiceDiscoveryResponse:
        """
        在腾讯云容器服务下更新 Prometheus 服务发现。
        <p>注意：前提条件，已经通过 Prometheus 控制台集成了对应的腾讯云容器服务，具体请参考
        <a href="https://cloud.tencent.com/document/product/248/48859" target="_blank">Agent 安装</a>。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateServiceDiscovery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateServiceDiscoveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeGrafanaDashboard(
            self,
            request: models.UpgradeGrafanaDashboardRequest,
            opts: Dict = None,
    ) -> models.UpgradeGrafanaDashboardResponse:
        """
        升级 Grafana Dashboard
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeGrafanaDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeGrafanaDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeGrafanaInstance(
            self,
            request: models.UpgradeGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeGrafanaInstanceResponse:
        """
        升级 Grafana 实例
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)