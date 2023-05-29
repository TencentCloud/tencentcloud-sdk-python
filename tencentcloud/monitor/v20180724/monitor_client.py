# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.monitor.v20180724 import models


class MonitorClient(AbstractClient):
    _apiVersion = '2018-07-24'
    _endpoint = 'monitor.tencentcloudapi.com'
    _service = 'monitor'


    def BindPrometheusManagedGrafana(self, request):
        """绑定 Grafana 可视化服务实例

        :param request: Request instance for BindPrometheusManagedGrafana.
        :type request: :class:`tencentcloud.monitor.v20180724.models.BindPrometheusManagedGrafanaRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.BindPrometheusManagedGrafanaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindPrometheusManagedGrafana", params, headers=headers)
            response = json.loads(body)
            model = models.BindPrometheusManagedGrafanaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindingPolicyObject(self, request):
        """将告警策略绑定到特定对象

        :param request: Request instance for BindingPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.BindingPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.BindingPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindingPolicyObject", params, headers=headers)
            response = json.loads(body)
            model = models.BindingPolicyObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindingPolicyTag(self, request):
        """策略绑定标签

        :param request: Request instance for BindingPolicyTag.
        :type request: :class:`tencentcloud.monitor.v20180724.models.BindingPolicyTagRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.BindingPolicyTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindingPolicyTag", params, headers=headers)
            response = json.loads(body)
            model = models.BindingPolicyTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckIsPrometheusNewUser(self, request):
        """判断用户是否为云原生监控新用户，即在任何地域下均未创建过监控实例的用户

        :param request: Request instance for CheckIsPrometheusNewUser.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CheckIsPrometheusNewUserRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CheckIsPrometheusNewUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIsPrometheusNewUser", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIsPrometheusNewUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CleanGrafanaInstance(self, request):
        """强制销毁 Grafana 实例

        :param request: Request instance for CleanGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CleanGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CleanGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CleanGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CleanGrafanaInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAlarmNotice(self, request):
        """创建通知模板

        :param request: Request instance for CreateAlarmNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlarmNotice", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlarmNoticeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAlarmPolicy(self, request):
        """创建告警策略

        :param request: Request instance for CreateAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlarmPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAlertRule(self, request):
        """创建 Prometheus 告警规则。

        请注意，**告警对象和告警消息是 Prometheus Rule Annotations 的特殊字段，需要通过 annotations 来传递，对应的 Key 分别为summary/description**，，请参考 [Prometheus Rule更多配置请参考](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)。

        :param request: Request instance for CreateAlertRule.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateAlertRuleRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlertRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlertRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateExporterIntegration(self, request):
        """创建 exporter 集成

        :param request: Request instance for CreateExporterIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateExporterIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateExporterIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExporterIntegration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExporterIntegrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateGrafanaInstance(self, request):
        """创建 Grafana 实例

        :param request: Request instance for CreateGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGrafanaInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateGrafanaIntegration(self, request):
        """创建 Grafana 集成配置

        :param request: Request instance for CreateGrafanaIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGrafanaIntegration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGrafanaIntegrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateGrafanaNotificationChannel(self, request):
        """创建 Grafana 告警通道

        :param request: Request instance for CreateGrafanaNotificationChannel.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaNotificationChannelRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaNotificationChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGrafanaNotificationChannel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGrafanaNotificationChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePolicyGroup(self, request):
        """增加策略组

        :param request: Request instance for CreatePolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePolicyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePolicyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePolicyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusAgent(self, request):
        """创建 Prometheus CVM Agent

        :param request: Request instance for CreatePrometheusAgent.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusAgent", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusAlertPolicy(self, request):
        """创建告警策略

        :param request: Request instance for CreatePrometheusAlertPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusAlertPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusAlertPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusAlertPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusAlertPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusClusterAgent(self, request):
        """与腾讯云可观测融合的2.0实例关联集群

        :param request: Request instance for CreatePrometheusClusterAgent.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusClusterAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusClusterAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusClusterAgent", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusClusterAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusConfig(self, request):
        """创建prometheus配置

        :param request: Request instance for CreatePrometheusConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusGlobalNotification(self, request):
        """创建全局告警通知渠道

        :param request: Request instance for CreatePrometheusGlobalNotification.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusGlobalNotificationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusGlobalNotificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusGlobalNotification", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusGlobalNotificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusMultiTenantInstancePostPayMode(self, request):
        """创建按量 Prometheus 实例，根据用量收费实例

        :param request: Request instance for CreatePrometheusMultiTenantInstancePostPayMode.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusMultiTenantInstancePostPayModeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusMultiTenantInstancePostPayModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusMultiTenantInstancePostPayMode", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusMultiTenantInstancePostPayModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusRecordRuleYaml(self, request):
        """以Yaml的方式创建聚合规则

        :param request: Request instance for CreatePrometheusRecordRuleYaml.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusRecordRuleYamlRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusRecordRuleYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusRecordRuleYaml", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusRecordRuleYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusScrapeJob(self, request):
        """创建 Prometheus 抓取任务

        :param request: Request instance for CreatePrometheusScrapeJob.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusScrapeJobRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusScrapeJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusScrapeJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusScrapeJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusTemp(self, request):
        """创建一个云原生Prometheus模板

        :param request: Request instance for CreatePrometheusTemp.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusTempRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusTempResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusTemp", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusTempResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRecordingRule(self, request):
        """创建 Prometheus 的预聚合规则

        :param request: Request instance for CreateRecordingRule.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateRecordingRuleRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateRecordingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordingRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordingRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSSOAccount(self, request):
        """Grafana实例授权其他腾讯云用户

        :param request: Request instance for CreateSSOAccount.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateSSOAccountRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateSSOAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSSOAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSSOAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateServiceDiscovery(self, request):
        """在腾讯云容器服务下创建 Prometheus 服务发现。
        <p>注意：前提条件，已经通过 Prometheus 控制台集成了对应的腾讯云容器服务，具体请参考
        <a href="https://cloud.tencent.com/document/product/248/48859" target="_blank">Agent 安装</a>。</p>

        :param request: Request instance for CreateServiceDiscovery.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateServiceDiscoveryRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateServiceDiscoveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceDiscovery", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceDiscoveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAlarmNotices(self, request):
        """删除告警通知模板

        :param request: Request instance for DeleteAlarmNotices.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmNoticesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmNoticesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarmNotices", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlarmNoticesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAlarmPolicy(self, request):
        """删除告警策略

        :param request: Request instance for DeleteAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlarmPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAlertRules(self, request):
        """批量删除 Prometheus 报警规则

        :param request: Request instance for DeleteAlertRules.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteAlertRulesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteAlertRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlertRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlertRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteExporterIntegration(self, request):
        """删除 exporter 集成

        :param request: Request instance for DeleteExporterIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteExporterIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteExporterIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExporterIntegration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteExporterIntegrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGrafanaInstance(self, request):
        """删除 Grafana 实例

        :param request: Request instance for DeleteGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGrafanaInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGrafanaIntegration(self, request):
        """删除 Grafana 集成配置

        :param request: Request instance for DeleteGrafanaIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGrafanaIntegration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGrafanaIntegrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGrafanaNotificationChannel(self, request):
        """删除 Grafana 告警通道

        :param request: Request instance for DeleteGrafanaNotificationChannel.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaNotificationChannelRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaNotificationChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGrafanaNotificationChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGrafanaNotificationChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePolicyGroup(self, request):
        """删除告警策略组

        :param request: Request instance for DeletePolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePolicyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePolicyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePolicyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePrometheusAlertPolicy(self, request):
        """删除2.0实例告警策略

        :param request: Request instance for DeletePrometheusAlertPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusAlertPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusAlertPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusAlertPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrometheusAlertPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePrometheusClusterAgent(self, request):
        """解除TMP实例的集群关联

        :param request: Request instance for DeletePrometheusClusterAgent.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusClusterAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusClusterAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusClusterAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrometheusClusterAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePrometheusConfig(self, request):
        """删除Prometheus配置，如果目标不存在，将返回成功

        :param request: Request instance for DeletePrometheusConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrometheusConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePrometheusRecordRuleYaml(self, request):
        """删除聚合实例

        :param request: Request instance for DeletePrometheusRecordRuleYaml.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusRecordRuleYamlRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusRecordRuleYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusRecordRuleYaml", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrometheusRecordRuleYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePrometheusScrapeJobs(self, request):
        """删除 Prometheus 抓取任务

        :param request: Request instance for DeletePrometheusScrapeJobs.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusScrapeJobsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusScrapeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusScrapeJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrometheusScrapeJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePrometheusTemp(self, request):
        """删除一个云原生Prometheus配置模板

        :param request: Request instance for DeletePrometheusTemp.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusTempRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusTempResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusTemp", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrometheusTempResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePrometheusTempSync(self, request):
        """解除模板同步，这将会删除目标中该模板所生产的配置，针对V2版本实例

        :param request: Request instance for DeletePrometheusTempSync.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusTempSyncRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusTempSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusTempSync", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrometheusTempSyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRecordingRules(self, request):
        """批量删除 Prometheus 预聚合规则

        :param request: Request instance for DeleteRecordingRules.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteRecordingRulesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteRecordingRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordingRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordingRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSSOAccount(self, request):
        """Grafana可视化服务 删除授权用户

        :param request: Request instance for DeleteSSOAccount.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteSSOAccountRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteSSOAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSSOAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSSOAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteServiceDiscovery(self, request):
        """删除在腾讯云容器服务下创建的 Prometheus 服务发现。
        <p>注意：前提条件，已经通过 Prometheus 控制台集成了对应的腾讯云容器服务，具体请参考
        <a href="https://cloud.tencent.com/document/product/248/48859" target="_blank">Agent 安装</a>。</p>

        :param request: Request instance for DeleteServiceDiscovery.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteServiceDiscoveryRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteServiceDiscoveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceDiscovery", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceDiscoveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccidentEventList(self, request):
        """获取平台事件列表

        :param request: Request instance for DescribeAccidentEventList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAccidentEventListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAccidentEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccidentEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccidentEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmEvents(self, request):
        """查询告警事件列表

        :param request: Request instance for DescribeAlarmEvents.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmEventsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmHistories(self, request):
        """查询告警历史

        请注意，**如果使用子用户进行告警历史的查询，只能查询到被授权项目下的告警历史**，或不区分项目的产品的告警历史。如何对子账户授予项目的权限，请参考 [访问管理-项目与标签](https://cloud.tencent.com/document/product/598/32738)。

        :param request: Request instance for DescribeAlarmHistories.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmHistoriesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmHistoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmHistories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmHistoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmMetrics(self, request):
        """查询告警指标列表

        :param request: Request instance for DescribeAlarmMetrics.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmMetricsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmNotice(self, request):
        """查询单个通知模板的详情

        :param request: Request instance for DescribeAlarmNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmNotice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmNoticeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmNoticeCallbacks(self, request):
        """获取告警通知模板所有回调URL

        :param request: Request instance for DescribeAlarmNoticeCallbacks.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeCallbacksRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeCallbacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmNoticeCallbacks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmNoticeCallbacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmNotices(self, request):
        """查询通知模板列表

        :param request: Request instance for DescribeAlarmNotices.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmNotices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmNoticesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmPolicies(self, request):
        """查询告警策略列表

        :param request: Request instance for DescribeAlarmPolicies.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPoliciesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmPolicy(self, request):
        """获取单个告警策略详情

        :param request: Request instance for DescribeAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlertRules(self, request):
        """Prometheus 报警规则查询接口

        :param request: Request instance for DescribeAlertRules.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlertRulesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlertRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlertRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlertRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAllNamespaces(self, request):
        """查询所有名字空间

        :param request: Request instance for DescribeAllNamespaces.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAllNamespacesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAllNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBaseMetrics(self, request):
        """获取基础指标属性

        :param request: Request instance for DescribeBaseMetrics.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBaseMetricsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBaseMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaseMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaseMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBasicAlarmList(self, request):
        """获取基础告警列表

        :param request: Request instance for DescribeBasicAlarmList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBasicAlarmListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBasicAlarmListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBasicAlarmList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBasicAlarmListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBindingPolicyObjectList(self, request):
        """获取已绑定对象列表

        :param request: Request instance for DescribeBindingPolicyObjectList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindingPolicyObjectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBindingPolicyObjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterAgentCreatingProgress(self, request):
        """获取prom实例中集群详细的关联状态

        :param request: Request instance for DescribeClusterAgentCreatingProgress.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeClusterAgentCreatingProgressRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeClusterAgentCreatingProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAgentCreatingProgress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterAgentCreatingProgressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConditionsTemplateList(self, request):
        """获取条件模板列表

        :param request: Request instance for DescribeConditionsTemplateList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeConditionsTemplateListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeConditionsTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConditionsTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConditionsTemplateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDNSConfig(self, request):
        """列出 Grafana DNS 配置

        :param request: Request instance for DescribeDNSConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeDNSConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeDNSConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDNSConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDNSConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExporterIntegrations(self, request):
        """查询 exporter 集成列表

        :param request: Request instance for DescribeExporterIntegrations.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeExporterIntegrationsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeExporterIntegrationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExporterIntegrations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExporterIntegrationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaChannels(self, request):
        """列出 Grafana 所有告警通道

        :param request: Request instance for DescribeGrafanaChannels.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaChannelsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaChannels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGrafanaChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaConfig(self, request):
        """列出 Grafana 的设置，即 grafana.ini 文件内容

        :param request: Request instance for DescribeGrafanaConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGrafanaConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaEnvironments(self, request):
        """列出 Grafana 环境变量

        :param request: Request instance for DescribeGrafanaEnvironments.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaEnvironmentsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGrafanaEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaInstances(self, request):
        """列出用户所有的 Grafana 服务

        :param request: Request instance for DescribeGrafanaInstances.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaInstancesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGrafanaInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaIntegrations(self, request):
        """列出 Grafana 已安装的集成

        :param request: Request instance for DescribeGrafanaIntegrations.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaIntegrationsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaIntegrationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaIntegrations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGrafanaIntegrationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaNotificationChannels(self, request):
        """列出 Grafana 告警通道

        :param request: Request instance for DescribeGrafanaNotificationChannels.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaNotificationChannelsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaNotificationChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaNotificationChannels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGrafanaNotificationChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaWhiteList(self, request):
        """列出 Grafana 白名单

        :param request: Request instance for DescribeGrafanaWhiteList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaWhiteListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGrafanaWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstalledPlugins(self, request):
        """列出实例已安装的插件

        :param request: Request instance for DescribeInstalledPlugins.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeInstalledPluginsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeInstalledPluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstalledPlugins", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstalledPluginsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMonitorTypes(self, request):
        """腾讯云可观测平台支持多种类型的监控，此接口列出支持的所有类型

        :param request: Request instance for DescribeMonitorTypes.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeMonitorTypesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeMonitorTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonitorTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonitorTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePluginOverviews(self, request):
        """列出可安装的所有 Grafana 插件

        :param request: Request instance for DescribePluginOverviews.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePluginOverviewsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePluginOverviewsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePluginOverviews", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginOverviewsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePolicyConditionList(self, request):
        """获取基础告警策略条件

        :param request: Request instance for DescribePolicyConditionList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyConditionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyConditionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePolicyGroupInfo(self, request):
        """获取基础策略组详情

        :param request: Request instance for DescribePolicyGroupInfo.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePolicyGroupList(self, request):
        """获取基础策略告警组列表

        :param request: Request instance for DescribePolicyGroupList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProductEventList(self, request):
        """分页获取产品事件的列表

        :param request: Request instance for DescribeProductEventList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProductList(self, request):
        """查询腾讯云可观测平台云产品列表，支持云服务器CVM、云数据库、云消息队列、负载均衡、容器服务、专线等云产品。

        :param request: Request instance for DescribeProductList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeProductListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeProductListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusAgentInstances(self, request):
        """获取关联目标集群的实例列表

        :param request: Request instance for DescribePrometheusAgentInstances.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusAgentInstancesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusAgentInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusAgentInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusAgentInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusAgents(self, request):
        """列出 Prometheus CVM Agent

        :param request: Request instance for DescribePrometheusAgents.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusAgentsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusAgentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusAgents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusAgentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusAlertPolicy(self, request):
        """获取2.0实例告警策略列表

        :param request: Request instance for DescribePrometheusAlertPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusAlertPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusAlertPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusAlertPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusAlertPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusClusterAgents(self, request):
        """获取TMP实例关联集群列表

        :param request: Request instance for DescribePrometheusClusterAgents.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusClusterAgentsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusClusterAgentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusClusterAgents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusClusterAgentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusConfig(self, request):
        """拉取Prometheus配置

        :param request: Request instance for DescribePrometheusConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusGlobalConfig(self, request):
        """获得实例级别抓取配置

        :param request: Request instance for DescribePrometheusGlobalConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusGlobalConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusGlobalConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusGlobalConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusGlobalConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusGlobalNotification(self, request):
        """查询全局告警通知渠道

        :param request: Request instance for DescribePrometheusGlobalNotification.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusGlobalNotificationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusGlobalNotificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusGlobalNotification", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusGlobalNotificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusInstanceDetail(self, request):
        """获取TMP实例详情

        :param request: Request instance for DescribePrometheusInstanceDetail.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstanceDetailRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusInstanceInitStatus(self, request):
        """获取2.0实例初始化任务状态

        :param request: Request instance for DescribePrometheusInstanceInitStatus.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstanceInitStatusRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstanceInitStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusInstanceInitStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusInstanceInitStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusInstanceUsage(self, request):
        """查询Prometheus按量实例用量

        :param request: Request instance for DescribePrometheusInstanceUsage.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstanceUsageRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstanceUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusInstanceUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusInstanceUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusInstances(self, request):
        """本接口 (DescribePrometheusInstances) 用于查询一个或多个实例的详细信息。
        <ul>
        <li>可以根据实例ID、实例名称或者实例状态等信息来查询实例的详细信息</li>
        <li>如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的实例。</li>
        </ul>

        :param request: Request instance for DescribePrometheusInstances.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstancesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusInstancesOverview(self, request):
        """获取与 Prometheus 监控融合实例列表

        :param request: Request instance for DescribePrometheusInstancesOverview.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstancesOverviewRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstancesOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusInstancesOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusInstancesOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusRecordRuleYaml(self, request):
        """拉取Prometheus聚合规则yaml列表

        :param request: Request instance for DescribePrometheusRecordRuleYaml.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusRecordRuleYamlRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusRecordRuleYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusRecordRuleYaml", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusRecordRuleYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusRecordRules(self, request):
        """获取聚合规则列表，包含关联集群内crd资源创建的record rule

        :param request: Request instance for DescribePrometheusRecordRules.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusRecordRulesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusRecordRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusRecordRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusRecordRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusScrapeJobs(self, request):
        """列出 Prometheus 抓取任务

        :param request: Request instance for DescribePrometheusScrapeJobs.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusScrapeJobsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusScrapeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusScrapeJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusScrapeJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusTargetsTMP(self, request):
        """获取targets信息

        :param request: Request instance for DescribePrometheusTargetsTMP.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusTargetsTMPRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusTargetsTMPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusTargetsTMP", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusTargetsTMPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusTemp(self, request):
        """拉取模板列表，默认模板将总是在最前面

        :param request: Request instance for DescribePrometheusTemp.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusTempRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusTempResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusTemp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusTempResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusTempSync(self, request):
        """获取模板关联实例信息，针对V2版本实例

        :param request: Request instance for DescribePrometheusTempSync.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusTempSyncRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusTempSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusTempSync", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusTempSyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusZones(self, request):
        """列出 Prometheus 服务可用区

        :param request: Request instance for DescribePrometheusZones.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusZonesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRecordingRules(self, request):
        """根据条件查询 Prometheus 预聚合规则

        :param request: Request instance for DescribeRecordingRules.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeRecordingRulesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeRecordingRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordingRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordingRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSSOAccount(self, request):
        """列出当前grafana实例的所有授权账号

        :param request: Request instance for DescribeSSOAccount.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeSSOAccountRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeSSOAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSSOAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSSOAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceDiscovery(self, request):
        """列出在腾讯云容器服务下创建的 Prometheus 服务发现。
        <p>注意：前提条件，已经通过 Prometheus 控制台集成了对应的腾讯云容器服务，具体请参考
        <a href="https://cloud.tencent.com/document/product/248/48859" target="_blank">Agent 安装</a>。</p>

        :param request: Request instance for DescribeServiceDiscovery.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeServiceDiscoveryRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeServiceDiscoveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceDiscovery", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceDiscoveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStatisticData(self, request):
        """根据维度条件查询监控数据

        :param request: Request instance for DescribeStatisticData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeStatisticDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeStatisticDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStatisticData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStatisticDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyPrometheusInstance(self, request):
        """彻底删除 Prometheus 实例相关数据，给定的实例必须先被 Terminate

        :param request: Request instance for DestroyPrometheusInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DestroyPrometheusInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DestroyPrometheusInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyPrometheusInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyPrometheusInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableGrafanaInternet(self, request):
        """设置 Grafana 公网访问

        :param request: Request instance for EnableGrafanaInternet.
        :type request: :class:`tencentcloud.monitor.v20180724.models.EnableGrafanaInternetRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.EnableGrafanaInternetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableGrafanaInternet", params, headers=headers)
            response = json.loads(body)
            model = models.EnableGrafanaInternetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableGrafanaSSO(self, request):
        """设置 Grafana 单点登录，使用腾讯云账号

        :param request: Request instance for EnableGrafanaSSO.
        :type request: :class:`tencentcloud.monitor.v20180724.models.EnableGrafanaSSORequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.EnableGrafanaSSOResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableGrafanaSSO", params, headers=headers)
            response = json.loads(body)
            model = models.EnableGrafanaSSOResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableSSOCamCheck(self, request):
        """SSO单点登录时，设置是否cam鉴权

        :param request: Request instance for EnableSSOCamCheck.
        :type request: :class:`tencentcloud.monitor.v20180724.models.EnableSSOCamCheckRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.EnableSSOCamCheckResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableSSOCamCheck", params, headers=headers)
            response = json.loads(body)
            model = models.EnableSSOCamCheckResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetMonitorData(self, request):
        """获取云产品的监控数据。此接口不适用于拉取容器服务监控数据，如需拉取容器服务监控数据，请使用[根据维度条件查询监控数据](https://cloud.tencent.com/document/product/248/51845)接口。
        传入产品的命名空间、对象维度描述和监控指标即可获得相应的监控数据。
        接口调用限制：单请求最多可支持批量拉取10个实例的监控数据，单请求的数据点数限制为1440个。
        若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。

        >?
        >- 2022年9月1日起，云监控开始对GetMonitorData接口计费。每个主账号每月可获得100万次免费请求额度，超过免费额度后如需继续调用接口需要开通 [API请求按量付费](https://buy.cloud.tencent.com/APIRequestBuy)。计费规则可查看[API计费文档](https://cloud.tencent.com/document/product/248/77914)。

        :param request: Request instance for GetMonitorData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.GetMonitorDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.GetMonitorDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMonitorData", params, headers=headers)
            response = json.loads(body)
            model = models.GetMonitorDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetPrometheusAgentManagementCommand(self, request):
        """获取 Prometheus Agent 管理相关的命令行

        :param request: Request instance for GetPrometheusAgentManagementCommand.
        :type request: :class:`tencentcloud.monitor.v20180724.models.GetPrometheusAgentManagementCommandRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.GetPrometheusAgentManagementCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPrometheusAgentManagementCommand", params, headers=headers)
            response = json.loads(body)
            model = models.GetPrometheusAgentManagementCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InstallPlugins(self, request):
        """安装 Grafana Plugin

        :param request: Request instance for InstallPlugins.
        :type request: :class:`tencentcloud.monitor.v20180724.models.InstallPluginsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.InstallPluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallPlugins", params, headers=headers)
            response = json.loads(body)
            model = models.InstallPluginsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmNotice(self, request):
        """编辑告警通知模板

        :param request: Request instance for ModifyAlarmNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmNotice", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmNoticeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmPolicyCondition(self, request):
        """修改告警策略触发条件

        :param request: Request instance for ModifyAlarmPolicyCondition.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyConditionRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyConditionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicyCondition", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmPolicyConditionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmPolicyInfo(self, request):
        """告警2.0编辑告警策略基本信息，包括策略名、备注

        :param request: Request instance for ModifyAlarmPolicyInfo.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyInfoRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmPolicyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmPolicyNotice(self, request):
        """修改告警策略绑定的告警通知模板

        :param request: Request instance for ModifyAlarmPolicyNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicyNotice", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmPolicyNoticeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmPolicyStatus(self, request):
        """启停告警策略

        :param request: Request instance for ModifyAlarmPolicyStatus.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyStatusRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmPolicyTasks(self, request):
        """修改告警策略的触发任务，TriggerTasks字段放触发任务列表，TriggerTasks传空数组时，代表解绑该策略的所有触发任务。

        :param request: Request instance for ModifyAlarmPolicyTasks.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyTasksRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicyTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmPolicyTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmReceivers(self, request):
        """修改告警接收人

        :param request: Request instance for ModifyAlarmReceivers.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmReceiversRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmReceiversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmReceivers", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmReceiversResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyGrafanaInstance(self, request):
        """修改 Grafana 实例属性

        :param request: Request instance for ModifyGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGrafanaInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPolicyGroup(self, request):
        """更新策略组

        :param request: Request instance for ModifyPolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPolicyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPolicyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPolicyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrometheusAgentExternalLabels(self, request):
        """修改被关联集群的external labels

        :param request: Request instance for ModifyPrometheusAgentExternalLabels.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusAgentExternalLabelsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusAgentExternalLabelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusAgentExternalLabels", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrometheusAgentExternalLabelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrometheusAlertPolicy(self, request):
        """修改2.0实例告警策略

        :param request: Request instance for ModifyPrometheusAlertPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusAlertPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusAlertPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusAlertPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrometheusAlertPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrometheusConfig(self, request):
        """修改prometheus配置，如果配置项不存在，则会新增

        :param request: Request instance for ModifyPrometheusConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrometheusConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrometheusGlobalNotification(self, request):
        """修改全局告警通知渠道

        :param request: Request instance for ModifyPrometheusGlobalNotification.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusGlobalNotificationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusGlobalNotificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusGlobalNotification", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrometheusGlobalNotificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrometheusInstanceAttributes(self, request):
        """修改 Prometheus 实例相关属性

        :param request: Request instance for ModifyPrometheusInstanceAttributes.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusInstanceAttributesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusInstanceAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusInstanceAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrometheusInstanceAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrometheusRecordRuleYaml(self, request):
        """通过yaml的方式修改Prometheus聚合实例

        :param request: Request instance for ModifyPrometheusRecordRuleYaml.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusRecordRuleYamlRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusRecordRuleYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusRecordRuleYaml", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrometheusRecordRuleYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrometheusTemp(self, request):
        """修改模板内容

        :param request: Request instance for ModifyPrometheusTemp.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusTempRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusTempResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusTemp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrometheusTempResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PutMonitorData(self, request):
        """对应的功能控制台及后端服务已于2年前下线，剩余该API接口未下线。

        默认接口请求频率限制：50次/秒。
        默认单租户指标上限：100个。
        单次上报最多 30 个指标/值对，请求返回错误时，请求中所有的指标/值均不会被保存。

        上报的时间戳为期望保存的时间戳，建议构造整数分钟时刻的时间戳。
        时间戳时间范围必须为当前时间到 300 秒前之间。
        同一 IP 指标对的数据需按分钟先后顺序上报。

        :param request: Request instance for PutMonitorData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.PutMonitorDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.PutMonitorDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutMonitorData", params, headers=headers)
            response = json.loads(body)
            model = models.PutMonitorDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeGrafanaInstance(self, request):
        """恢复 Grafana 实例

        :param request: Request instance for ResumeGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ResumeGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ResumeGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeGrafanaInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RunPrometheusInstance(self, request):
        """初始化TMP实例，开启集成中心时调用

        :param request: Request instance for RunPrometheusInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.RunPrometheusInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.RunPrometheusInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunPrometheusInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RunPrometheusInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendCustomAlarmMsg(self, request):
        """发送自定义消息告警

        :param request: Request instance for SendCustomAlarmMsg.
        :type request: :class:`tencentcloud.monitor.v20180724.models.SendCustomAlarmMsgRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.SendCustomAlarmMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendCustomAlarmMsg", params, headers=headers)
            response = json.loads(body)
            model = models.SendCustomAlarmMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetDefaultAlarmPolicy(self, request):
        """设置一个策略为该告警策略类型、该项目的默认告警策略。
        同一项目下相同的告警策略类型，就会被设置为非默认。

        :param request: Request instance for SetDefaultAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.SetDefaultAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.SetDefaultAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetDefaultAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.SetDefaultAlarmPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncPrometheusTemp(self, request):
        """同步模板到实例或者集群，针对V2版本实例

        :param request: Request instance for SyncPrometheusTemp.
        :type request: :class:`tencentcloud.monitor.v20180724.models.SyncPrometheusTempRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.SyncPrometheusTempResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncPrometheusTemp", params, headers=headers)
            response = json.loads(body)
            model = models.SyncPrometheusTempResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminatePrometheusInstances(self, request):
        """销毁按量 Prometheus 实例

        :param request: Request instance for TerminatePrometheusInstances.
        :type request: :class:`tencentcloud.monitor.v20180724.models.TerminatePrometheusInstancesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.TerminatePrometheusInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminatePrometheusInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminatePrometheusInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindingAllPolicyObject(self, request):
        """删除全部的关联对象

        :param request: Request instance for UnBindingAllPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UnBindingAllPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UnBindingAllPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindingAllPolicyObject", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindingAllPolicyObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindingPolicyObject(self, request):
        """删除策略的关联对象

        :param request: Request instance for UnBindingPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UnBindingPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UnBindingPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindingPolicyObject", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindingPolicyObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnbindPrometheusManagedGrafana(self, request):
        """解除实例绑定的 Grafana 可视化实例

        :param request: Request instance for UnbindPrometheusManagedGrafana.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UnbindPrometheusManagedGrafanaRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UnbindPrometheusManagedGrafanaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindPrometheusManagedGrafana", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindPrometheusManagedGrafanaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UninstallGrafanaDashboard(self, request):
        """删除 Grafana Dashboard

        :param request: Request instance for UninstallGrafanaDashboard.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UninstallGrafanaDashboardRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UninstallGrafanaDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallGrafanaDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.UninstallGrafanaDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UninstallGrafanaPlugins(self, request):
        """删除已安装的插件

        :param request: Request instance for UninstallGrafanaPlugins.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UninstallGrafanaPluginsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UninstallGrafanaPluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallGrafanaPlugins", params, headers=headers)
            response = json.loads(body)
            model = models.UninstallGrafanaPluginsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAlertRule(self, request):
        """更新 Prometheus 的报警规则。

        请注意，**告警对象和告警消息是 Prometheus Rule Annotations 的特殊字段，需要通过 annotations 来传递，对应的 Key 分别为summary/description**，，请参考 [Prometheus Rule更多配置请参考](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)。

        :param request: Request instance for UpdateAlertRule.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateAlertRuleRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlertRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAlertRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAlertRuleState(self, request):
        """更新 Prometheus 报警策略状态

        :param request: Request instance for UpdateAlertRuleState.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateAlertRuleStateRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateAlertRuleStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlertRuleState", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAlertRuleStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateDNSConfig(self, request):
        """更新 Grafana 的 DNS 配置

        :param request: Request instance for UpdateDNSConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateDNSConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateDNSConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDNSConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDNSConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateExporterIntegration(self, request):
        """更新 exporter 集成配置

        :param request: Request instance for UpdateExporterIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateExporterIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateExporterIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateExporterIntegration", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateExporterIntegrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGrafanaConfig(self, request):
        """更新 Grafana 配置

        :param request: Request instance for UpdateGrafanaConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGrafanaConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGrafanaConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGrafanaEnvironments(self, request):
        """更新 Grafana 环境变量

        :param request: Request instance for UpdateGrafanaEnvironments.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaEnvironmentsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGrafanaEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGrafanaEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGrafanaIntegration(self, request):
        """更新 Grafana 集成配置

        :param request: Request instance for UpdateGrafanaIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGrafanaIntegration", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGrafanaIntegrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGrafanaNotificationChannel(self, request):
        """更新 Grafana 告警通道

        :param request: Request instance for UpdateGrafanaNotificationChannel.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaNotificationChannelRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaNotificationChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGrafanaNotificationChannel", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGrafanaNotificationChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGrafanaWhiteList(self, request):
        """更新 Grafana 白名单

        :param request: Request instance for UpdateGrafanaWhiteList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaWhiteListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGrafanaWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGrafanaWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdatePrometheusAgentStatus(self, request):
        """更新 Prometheus CVM Agent 状态

        :param request: Request instance for UpdatePrometheusAgentStatus.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdatePrometheusAgentStatusRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdatePrometheusAgentStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePrometheusAgentStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePrometheusAgentStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdatePrometheusScrapeJob(self, request):
        """更新 Prometheus 抓取任务

        :param request: Request instance for UpdatePrometheusScrapeJob.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdatePrometheusScrapeJobRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdatePrometheusScrapeJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePrometheusScrapeJob", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePrometheusScrapeJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateRecordingRule(self, request):
        """更新 Prometheus 的预聚合规则

        :param request: Request instance for UpdateRecordingRule.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateRecordingRuleRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateRecordingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordingRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRecordingRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateSSOAccount(self, request):
        """更新已授权账号的备注、权限信息，会直接覆盖原有的信息，不传则不会更新。

        :param request: Request instance for UpdateSSOAccount.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateSSOAccountRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateSSOAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSSOAccount", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSSOAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateServiceDiscovery(self, request):
        """在腾讯云容器服务下更新 Prometheus 服务发现。
        <p>注意：前提条件，已经通过 Prometheus 控制台集成了对应的腾讯云容器服务，具体请参考
        <a href="https://cloud.tencent.com/document/product/248/48859" target="_blank">Agent 安装</a>。</p>

        :param request: Request instance for UpdateServiceDiscovery.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateServiceDiscoveryRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateServiceDiscoveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateServiceDiscovery", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateServiceDiscoveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeGrafanaDashboard(self, request):
        """升级 Grafana Dashboard

        :param request: Request instance for UpgradeGrafanaDashboard.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpgradeGrafanaDashboardRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpgradeGrafanaDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeGrafanaDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeGrafanaDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeGrafanaInstance(self, request):
        """升级 Grafana 实例

        :param request: Request instance for UpgradeGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpgradeGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpgradeGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeGrafanaInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)