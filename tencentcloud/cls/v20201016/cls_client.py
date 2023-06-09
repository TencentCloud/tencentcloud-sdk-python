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
from tencentcloud.cls.v20201016 import models


class ClsClient(AbstractClient):
    _apiVersion = '2020-10-16'
    _endpoint = 'cls.tencentcloudapi.com'
    _service = 'cls'


    def AddMachineGroupInfo(self, request):
        """用于添加机器组信息

        :param request: Request instance for AddMachineGroupInfo.
        :type request: :class:`tencentcloud.cls.v20201016.models.AddMachineGroupInfoRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.AddMachineGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddMachineGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.AddMachineGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyConfigToMachineGroup(self, request):
        """应用采集配置到指定机器组

        :param request: Request instance for ApplyConfigToMachineGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.ApplyConfigToMachineGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ApplyConfigToMachineGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyConfigToMachineGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyConfigToMachineGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseKafkaConsumer(self, request):
        """关闭Kafka协议消费

        :param request: Request instance for CloseKafkaConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.CloseKafkaConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CloseKafkaConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseKafkaConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.CloseKafkaConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAlarm(self, request):
        """本接口用于创建告警策略。

        :param request: Request instance for CreateAlarm.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateAlarmRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAlarmNotice(self, request):
        """该接口用于创建通知渠道组。

        :param request: Request instance for CreateAlarmNotice.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateAlarmNoticeResponse`

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


    def CreateConfig(self, request):
        """创建采集规则配置

        :param request: Request instance for CreateConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateConfigExtra(self, request):
        """本接口用于创建特殊采集配置任务，特殊采集配置应用于自建K8S环境的采集Agent

        :param request: Request instance for CreateConfigExtra.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateConfigExtraRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateConfigExtraResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigExtra", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigExtraResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateConsumer(self, request):
        """本接口用于创建投递任务

        :param request: Request instance for CreateConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCosRecharge(self, request):
        """本接口用于创建cos导入任务

        :param request: Request instance for CreateCosRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateCosRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateCosRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCosRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateExport(self, request):
        """本接口仅创建下载任务，任务返回的下载地址，请用户调用DescribeExports查看任务列表。其中有下载地址CosPath参数。参考文档https://cloud.tencent.com/document/product/614/56449

        :param request: Request instance for CreateExport.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateExportRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateIndex(self, request):
        """本接口用于创建索引

        :param request: Request instance for CreateIndex.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateIndexRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIndex", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLogset(self, request):
        """本接口用于创建日志集，返回新创建的日志集的 ID。

        :param request: Request instance for CreateLogset.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateLogsetRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateLogsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogset", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLogsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMachineGroup(self, request):
        """创建机器组

        :param request: Request instance for CreateMachineGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateMachineGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateMachineGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMachineGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMachineGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateShipper(self, request):
        """新建投递到COS的任务，【！！！注意】使用此接口，需要检查是否配置了投递COS的角色和权限。如果没有配置，请参考文档投递权限查看和配置https://cloud.tencent.com/document/product/614/71623。

        :param request: Request instance for CreateShipper.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateShipperRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateShipperResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateShipper", params, headers=headers)
            response = json.loads(body)
            model = models.CreateShipperResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTopic(self, request):
        """本接口用于创建日志主题。

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAlarm(self, request):
        """本接口用于删除告警策略。

        :param request: Request instance for DeleteAlarm.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAlarmNotice(self, request):
        """该接口用于删除通知渠道组

        :param request: Request instance for DeleteAlarmNotice.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarmNotice", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlarmNoticeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteConfig(self, request):
        """删除采集规则配置

        :param request: Request instance for DeleteConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteConfigExtra(self, request):
        """本接口用于删除特殊采集规则配置，特殊采集配置应用于自建K8S环境的采集Agent

        :param request: Request instance for DeleteConfigExtra.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteConfigExtraRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteConfigExtraResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfigExtra", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigExtraResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteConfigFromMachineGroup(self, request):
        """删除应用到机器组的采集配置

        :param request: Request instance for DeleteConfigFromMachineGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteConfigFromMachineGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteConfigFromMachineGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfigFromMachineGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigFromMachineGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteConsumer(self, request):
        """本接口用于删除投递配置

        :param request: Request instance for DeleteConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteExport(self, request):
        """本接口用于删除日志下载任务

        :param request: Request instance for DeleteExport.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteExportRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExport", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteIndex(self, request):
        """本接口用于删除日志主题的索引配置，删除索引配置后将无法检索和查询采集到的日志。

        :param request: Request instance for DeleteIndex.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteIndexRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLogset(self, request):
        """本接口用于删除日志集。

        :param request: Request instance for DeleteLogset.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteLogsetRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteLogsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogset", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMachineGroup(self, request):
        """删除机器组

        :param request: Request instance for DeleteMachineGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteMachineGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteMachineGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMachineGroupInfo(self, request):
        """用于删除机器组信息

        :param request: Request instance for DeleteMachineGroupInfo.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteMachineGroupInfoRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteMachineGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteShipper(self, request):
        """删除投递规则

        :param request: Request instance for DeleteShipper.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteShipperRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteShipperResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShipper", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShipperResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTopic(self, request):
        """本接口用于删除日志主题。

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmNotices(self, request):
        """该接口用于获取通知渠道组列表

        :param request: Request instance for DescribeAlarmNotices.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmNoticesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmNoticesResponse`

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


    def DescribeAlarms(self, request):
        """本接口用于获取告警策略列表。

        :param request: Request instance for DescribeAlarms.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarms", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlertRecordHistory(self, request):
        """获取告警历史，例如今天未恢复的告警

        :param request: Request instance for DescribeAlertRecordHistory.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeAlertRecordHistoryRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeAlertRecordHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlertRecordHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlertRecordHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConfigExtras(self, request):
        """本接口用于获取特殊采集配置，特殊采集配置应用于自建K8S环境的采集Agent

        :param request: Request instance for DescribeConfigExtras.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConfigExtrasRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConfigExtrasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigExtras", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigExtrasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConfigMachineGroups(self, request):
        """获取采集规则配置所绑定的机器组

        :param request: Request instance for DescribeConfigMachineGroups.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConfigMachineGroupsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConfigMachineGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigMachineGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigMachineGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConfigs(self, request):
        """获取采集规则配置

        :param request: Request instance for DescribeConfigs.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConfigsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConsumer(self, request):
        """本接口用于获取投递配置

        :param request: Request instance for DescribeConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCosRecharges(self, request):
        """本接口用于获取cos导入配置

        :param request: Request instance for DescribeCosRecharges.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeCosRechargesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeCosRechargesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosRecharges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosRechargesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExports(self, request):
        """本接口用于获取日志下载任务列表

        :param request: Request instance for DescribeExports.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeExportsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeExportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIndex(self, request):
        """本接口用于获取索引配置信息

        :param request: Request instance for DescribeIndex.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeIndexRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogContext(self, request):
        """本接口用于搜索日志上下文附近的内容

        :param request: Request instance for DescribeLogContext.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeLogContextRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeLogContextResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogContext", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogContextResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogHistogram(self, request):
        """本接口用于构建日志数量直方图

        :param request: Request instance for DescribeLogHistogram.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeLogHistogramRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeLogHistogramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogHistogram", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogHistogramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogsets(self, request):
        """本接口用于获取日志集信息列表。

        :param request: Request instance for DescribeLogsets.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeLogsetsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeLogsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogsets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMachineGroupConfigs(self, request):
        """获取机器组绑定的采集规则配置

        :param request: Request instance for DescribeMachineGroupConfigs.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeMachineGroupConfigsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeMachineGroupConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineGroupConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineGroupConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMachineGroups(self, request):
        """获取机器组信息列表

        :param request: Request instance for DescribeMachineGroups.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeMachineGroupsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeMachineGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMachines(self, request):
        """获取制定机器组下的机器状态

        :param request: Request instance for DescribeMachines.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeMachinesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePartitions(self, request):
        """本接口用于获取主题分区列表。

        :param request: Request instance for DescribePartitions.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribePartitionsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribePartitionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePartitions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePartitionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeShipperTasks(self, request):
        """获取投递任务列表

        :param request: Request instance for DescribeShipperTasks.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeShipperTasksRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeShipperTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShipperTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShipperTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeShippers(self, request):
        """获取投递到COS的任务配置信息

        :param request: Request instance for DescribeShippers.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeShippersRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeShippersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShippers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShippersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTopics(self, request):
        """本接口用于获取日志主题列表，支持分页

        :param request: Request instance for DescribeTopics.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeTopicsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetAlarmLog(self, request):
        """本接口用于获取告警任务历史

        :param request: Request instance for GetAlarmLog.
        :type request: :class:`tencentcloud.cls.v20201016.models.GetAlarmLogRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.GetAlarmLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAlarmLog", params, headers=headers)
            response = json.loads(body)
            model = models.GetAlarmLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MergePartition(self, request):
        """本接口用于合并一个读写态的主题分区，合并时指定一个主题分区 ID，日志服务会自动合并范围右相邻的分区。

        :param request: Request instance for MergePartition.
        :type request: :class:`tencentcloud.cls.v20201016.models.MergePartitionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.MergePartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MergePartition", params, headers=headers)
            response = json.loads(body)
            model = models.MergePartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarm(self, request):
        """本接口用于修改告警策略。需要至少修改一项有效内容。

        :param request: Request instance for ModifyAlarm.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmNotice(self, request):
        """该接口用于修改通知渠道组

        :param request: Request instance for ModifyAlarmNotice.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmNoticeResponse`

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


    def ModifyConfig(self, request):
        """修改采集规则配置

        :param request: Request instance for ModifyConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyConfigExtra(self, request):
        """本接口用于修改特殊采集配置任务，特殊采集配置应用于自建K8S环境的采集Agent

        :param request: Request instance for ModifyConfigExtra.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyConfigExtraRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyConfigExtraResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConfigExtra", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConfigExtraResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyConsumer(self, request):
        """本接口用于修改投递任务

        :param request: Request instance for ModifyConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCosRecharge(self, request):
        """本接口用于修改cos导入任务

        :param request: Request instance for ModifyCosRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyCosRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyCosRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCosRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCosRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIndex(self, request):
        """本接口用于修改索引配置，该接口除受默认接口请求频率限制外，针对单个日志主题，并发数不能超过1，即同一时间同一个日志主题只能有一个正在执行的索引配置修改操作。

        :param request: Request instance for ModifyIndex.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyIndexRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIndex", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLogset(self, request):
        """本接口用于修改日志集信息

        :param request: Request instance for ModifyLogset.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyLogsetRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyLogsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogset", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMachineGroup(self, request):
        """修改机器组

        :param request: Request instance for ModifyMachineGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyMachineGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyMachineGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMachineGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMachineGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyShipper(self, request):
        """修改现有的投递规则，客户如果使用此接口，需要自行处理CLS对指定bucket的写权限。

        :param request: Request instance for ModifyShipper.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyShipperRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyShipperResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyShipper", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyShipperResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTopic(self, request):
        """本接口用于修改日志主题。

        :param request: Request instance for ModifyTopic.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyTopicRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OpenKafkaConsumer(self, request):
        """打开Kafka协议消费功能

        :param request: Request instance for OpenKafkaConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.OpenKafkaConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.OpenKafkaConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenKafkaConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.OpenKafkaConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RetryShipperTask(self, request):
        """重试失败的投递任务

        :param request: Request instance for RetryShipperTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.RetryShipperTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.RetryShipperTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryShipperTask", params, headers=headers)
            response = json.loads(body)
            model = models.RetryShipperTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchLog(self, request):
        """本接口用于检索分析日志, 该接口除受默认接口请求频率限制外，针对单个日志主题，查询并发数不能超过15。

        :param request: Request instance for SearchLog.
        :type request: :class:`tencentcloud.cls.v20201016.models.SearchLogRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.SearchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SplitPartition(self, request):
        """本接口用于分裂主题分区

        :param request: Request instance for SplitPartition.
        :type request: :class:`tencentcloud.cls.v20201016.models.SplitPartitionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.SplitPartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SplitPartition", params, headers=headers)
            response = json.loads(body)
            model = models.SplitPartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadLog(self, request, body):
        """## 提示
        为了保障您日志数据的可靠性以及更高效地使用日志服务，建议您使用CLS优化后的接口[上传结构化日志](https://cloud.tencent.com/document/product/614/16873)。

        同时我们给此接口专门优化定制了多个语言版本的SDK供您选择，SDK提供统一的异步发送、资源控制、自动重试、优雅关闭、感知上报等功能，使上报日志功能更完善，详情请参考[SDK采集](https://cloud.tencent.com/document/product/614/67157)。

        同时云API上传日志接口也支持同步上传日志数据，如果您选择继续使用此接口请参考下文。

        ## 功能描述

        本接口用于将日志写入到指定的日志主题。

        日志服务提供以下两种模式：

        #### 负载均衡模式

        系统根据当前日志主题下所有可读写的分区，遵循负载均衡原则自动分配写入的目标分区。该模式适合消费不保序的场景。

        #### 哈希路由模式

        系统根据携带的哈希值（X-CLS-HashKey）将数据写入到符合范围要求的目标分区。例如，可以将某个日志源端通过 hashkey 与某个主题分区强绑定，这样可以保证数据在该分区上写入和消费是严格保序的。



        #### 输入参数(pb二进制流，位于body中)

        | 字段名       | 类型    | 位置 | 必须 | 含义                                                         |
        | ------------ | ------- | ---- | ---- | ------------------------------------------------------------ |
        | logGroupList | message | pb   | 是   | logGroup 列表，封装好的日志组列表内容，建议 logGroup 数量不要超过5个 |

        LogGroup 说明：

        | 字段名      | 是否必选 | 含义                                                         |
        | ----------- | -------- | ------------------------------------------------------------ |
        | logs        | 是       | 日志数组，表示有多个 Log 组成的集合，一个 Log 表示一条日志，一个 LogGroup 中 Log 个数不能超过10000 |
        | contextFlow | 否       | LogGroup 的唯一ID，需要使用上下文功能时传入。格式："{上下文ID}-{LogGroupID}"。<br>上下文ID：唯一标识一个上下文（连续滚动的一系列日志文件，或者是需要保序的一系列日志），16进制64位整型字符串。<br>LogGroupID：连续递增的一串整型，16进制64位整型字符串。样例："102700A66102516A-59F59"。                        |
        | filename    | 否       | 日志文件名                                                   |
        | source      | 否       | 日志来源，一般使用机器 IP 作为标识                           |
        | logTags     | 否       | 日志的标签列表                                               |

        Log 说明：

        | 字段名   | 是否必选 | 含义                                                         |
        | -------- | -------- | ------------------------------------------------------------ |
        | time     | 是       | 日志时间（Unix 格式时间戳），支持秒、毫秒，建议采用毫秒      |
        | contents | 否       | key-value 格式的日志内容，表示一条日志里的多个 key-value 组合 |

        Content 说明：

        | 字段名 | 是否必选 | 含义                                                         |
        | ------ | -------- | ------------------------------------------------------------ |
        | key    | 是       | 单条日志里某个字段组的 key 值，不能以`_`开头                 |
        | value  | 是       | 单条日志某个字段组的 value 值，单条日志 value 不能超过1MB，LogGroup 中所有 value 总和不能超过5MB |

        LogTag 说明：

        | 字段名 | 是否必选 | 含义                             |
        | ------ | -------- | -------------------------------- |
        | key    | 是       | 自定义的标签 key                 |
        | value  | 是       | 自定义的标签 key 对应的 value 值 |

        ## PB 编译示例

        本示例将说明如何使用官方 protoc 编译工具将 PB 描述文件 编译生成为 C++ 语言可调用的上传日志接口。

        > ?目前 protoc 官方支持 Java、C++、Python 等语言的编译，详情请参见 [protoc](https://github.com/protocolbuffers/protobuf)。

        #### 1. 安装 Protocol Buffer

        下载 [Protocol Buffer](https://main.qcloudimg.com/raw/d7810aaf8b3073fbbc9d4049c21532aa/protobuf-2.6.1.tar.gz) ，解压并安装。示例版本为 protobuf 2.6.1，环境为 Centos 7.3 系统。 解压`protobuf-2.6.1.tar.gz`压缩包至`/usr/local`目录并进入该目录，执行命令如下：

        ```
        tar -zxvf protobuf-2.6.1.tar.gz -C /usr/local/ && cd /usr/local/protobuf-2.6.1
        ```

        开始编译和安装，配置环境变量，执行命令如下：

        ```
        [root@VM_0_8_centos protobuf-2.6.1]# ./configure
        [root@VM_0_8_centos protobuf-2.6.1]# make && make install
        [root@VM_0_8_centos protobuf-2.6.1]# export PATH=$PATH:/usr/local/protobuf-2.6.1/bin
        ```

        编译成功后，您可以使用以下命令查看版本：

        ```
        [root@VM_0_8_centos protobuf-2.6.1]# protoc --version
        liprotoc 2.6.1
        ```

        #### 2. 创建 PB 描述文件

        PB 描述文件是通信双方约定的数据交换格式，上传日志时须将规定的协议格式编译成对应语言版本的调用接口，然后添加到工程代码里，详情请参见 [protoc](https://github.com/protocolbuffers/protobuf) 。

        以日志服务所规定的 PB 数据格式内容为准， 在本地创建 PB 消息描述文件 cls.proto。

        > !PB 描述文件内容不可更改，且文件名须以`.proto`结尾。

        cls.proto 内容（PB 描述文件）如下：

        ```
        package cls;

        message Log
        {
            message Content
            {
                required string key   = 1; // 每组字段的 key
                required string value = 2; // 每组字段的 value
            }
            required int64   time     = 1; // 时间戳，UNIX时间格式
            repeated Content contents = 2; // 一条日志里的多个kv组合
        }

        message LogTag
        {
            required string key       = 1;
            required string value     = 2;
        }

        message LogGroup
        {
            repeated Log    logs        = 1; // 多条日志合成的日志数组
            optional string contextFlow = 2; // 目前暂无效用
            optional string filename    = 3; // 日志文件名
            optional string source      = 4; // 日志来源，一般使用机器IP
            repeated LogTag logTags     = 5;
        }

        message LogGroupList
        {
            repeated LogGroup logGroupList = 1; // 日志组列表
        }
        ```

        #### 3. 编译生成

        此例中，使用 proto 编译器生成 C++ 语言的文件，在 cls.proto 文件的同一目录下，执行如下编译命令：

        ```
        protoc --cpp_out=./ ./cls.proto
        ```

        > ?`--cpp_out=./`表示编译成 cpp 格式并输出当前目录下，`./cls.proto`表示位于当前目录下的 cls.proto 描述文件。

        编译成功后，会输出对应语言的代码文件。此例会生成 cls.pb.h 头文件和 [cls.pb.cc](http://cls.pb.cc) 代码实现文件，如下所示：

        ```
        [root@VM_0_8_centos protobuf-2.6.1]# protoc --cpp_out=./ ./cls.proto
        [root@VM_0_8_centos protobuf-2.6.1]# ls
        cls.pb.cc cls.pb.h cls.proto
        ```

        #### 4. 调用

        将生成的 cls.pb.h 头文件引入代码中，调用接口进行数据格式封装。

        :param request: Request instance for UploadLog.
        :type request: :class:`tencentcloud.cls.v20201016.models.UploadLogRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.UploadLogResponse`

        """
        try:
            params = request._serialize()
            params = {"X-CLS-"+key: value for key, value in params.items()}
            response = self.call_octet_stream("UploadLog", params, body)
            model = models.UploadLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)