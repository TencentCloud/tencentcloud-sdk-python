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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckFunction(self, request):
        """本接口用于数据加工DSL函数的语法校验。

        :param request: Request instance for CheckFunction.
        :type request: :class:`tencentcloud.cls.v20201016.models.CheckFunctionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CheckFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckRechargeKafkaServer(self, request):
        """本接口用于校验Kafka服务集群是否可以正常访问

        :param request: Request instance for CheckRechargeKafkaServer.
        :type request: :class:`tencentcloud.cls.v20201016.models.CheckRechargeKafkaServerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CheckRechargeKafkaServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckRechargeKafkaServer", params, headers=headers)
            response = json.loads(body)
            model = models.CheckRechargeKafkaServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlarmNotice(self, request):
        """该接口用于创建通知渠道组，提供两种配置模式，二选一：
        1，简易模式，提供最基本的通知渠道功能。需填写如下参数：
        - Type
        - NoticeReceivers
        - WebCallbacks

        2，高级模式，在简易模式基础上，支持设定规则，为不同类型的告警分别设定通知渠道，并支持告警升级功能。需填写如下参数：
        - NoticeRules

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlarmShield(self, request):
        """该接口用于创建告警屏蔽规则。

        :param request: Request instance for CreateAlarmShield.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateAlarmShieldRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateAlarmShieldResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlarmShield", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlarmShieldResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudProductLogCollection(self, request):
        """内部云产品接入使用相关接口

        :param request: Request instance for CreateCloudProductLogCollection.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateCloudProductLogCollectionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateCloudProductLogCollectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudProductLogCollection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudProductLogCollectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsoleSharing(self, request):
        """创建控制台分享

        :param request: Request instance for CreateConsoleSharing.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateConsoleSharingRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateConsoleSharingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsoleSharing", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsoleSharingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsumer(self, request):
        """本接口用于创建投递CKafka任务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDashboardSubscribe(self, request):
        """此接口用于创建仪表盘订阅

        :param request: Request instance for CreateDashboardSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateDashboardSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateDashboardSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDashboardSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDashboardSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataTransform(self, request):
        """本接口用于创建数据加工任务。

        :param request: Request instance for CreateDataTransform.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateDataTransformRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateDataTransformResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataTransform", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataTransformResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeliverCloudFunction(self, request):
        """本接口用于创建投递SCF任务

        :param request: Request instance for CreateDeliverCloudFunction.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateDeliverCloudFunctionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateDeliverCloudFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeliverCloudFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeliverCloudFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKafkaRecharge(self, request):
        """本接口用于创建Kafka数据订阅任务

        :param request: Request instance for CreateKafkaRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateKafkaRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateKafkaRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKafkaRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKafkaRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNoticeContent(self, request):
        """该接口用于创建通知内容。

        :param request: Request instance for CreateNoticeContent.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateNoticeContentRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateNoticeContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNoticeContent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNoticeContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScheduledSql(self, request):
        """本接口用于创建定时SQL分析任务

        :param request: Request instance for CreateScheduledSql.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateScheduledSqlRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateScheduledSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScheduledSql", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScheduledSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWebCallback(self, request):
        """该接口用于创建告警渠道回调配置。

        :param request: Request instance for CreateWebCallback.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateWebCallbackRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateWebCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebCallback", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWebCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAlarmShield(self, request):
        """该接口用于删除告警屏蔽规则。

        :param request: Request instance for DeleteAlarmShield.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmShieldRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmShieldResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarmShield", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlarmShieldResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudProductLogCollection(self, request):
        """内部云产品接入使用相关接口

        :param request: Request instance for DeleteCloudProductLogCollection.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteCloudProductLogCollectionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteCloudProductLogCollectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudProductLogCollection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudProductLogCollectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConsoleSharing(self, request):
        """删除控制台分享

        :param request: Request instance for DeleteConsoleSharing.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteConsoleSharingRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteConsoleSharingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConsoleSharing", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConsoleSharingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDashboardSubscribe(self, request):
        """此接口用于删除仪表盘订阅

        :param request: Request instance for DeleteDashboardSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteDashboardSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteDashboardSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDashboardSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDashboardSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataTransform(self, request):
        """本接口用于删除数据加工任务

        :param request: Request instance for DeleteDataTransform.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteDataTransformRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteDataTransformResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataTransform", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataTransformResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteKafkaRecharge(self, request):
        """本接口用于删除Kafka数据订阅任务

        :param request: Request instance for DeleteKafkaRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteKafkaRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteKafkaRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteKafkaRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteKafkaRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNoticeContent(self, request):
        """该接口用于删除通知内容配置

        :param request: Request instance for DeleteNoticeContent.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteNoticeContentRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteNoticeContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNoticeContent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNoticeContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScheduledSql(self, request):
        """本接口用于删除定时SQL分析任务

        :param request: Request instance for DeleteScheduledSql.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteScheduledSqlRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteScheduledSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScheduledSql", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScheduledSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShipper(self, request):
        """删除投递COS任务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebCallback(self, request):
        """该接口用于删除告警渠道回调配置。

        :param request: Request instance for DeleteWebCallback.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteWebCallbackRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteWebCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmShields(self, request):
        """获取告警屏蔽配置规则

        :param request: Request instance for DescribeAlarmShields.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmShieldsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmShieldsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmShields", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmShieldsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudProductLogTasks(self, request):
        """云产品接入使用相关接口

        :param request: Request instance for DescribeCloudProductLogTasks.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeCloudProductLogTasksRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeCloudProductLogTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudProductLogTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudProductLogTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsoleSharingList(self, request):
        """批量查询控制台分享列表

        :param request: Request instance for DescribeConsoleSharingList.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConsoleSharingListRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConsoleSharingListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsoleSharingList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsoleSharingListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDashboardSubscribes(self, request):
        """本接口用于获取仪表盘订阅列表，支持分页

        :param request: Request instance for DescribeDashboardSubscribes.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeDashboardSubscribesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeDashboardSubscribesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDashboardSubscribes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDashboardSubscribesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDashboards(self, request):
        """本接口用于获取仪表盘

        :param request: Request instance for DescribeDashboards.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeDashboardsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeDashboardsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDashboards", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDashboardsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataTransformInfo(self, request):
        """本接口用于获取数据加工任务列表基本信息

        :param request: Request instance for DescribeDataTransformInfo.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeDataTransformInfoRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeDataTransformInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataTransformInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataTransformInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKafkaConsumer(self, request):
        """获取Kafka协议消费信息

        :param request: Request instance for DescribeKafkaConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKafkaConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKafkaConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKafkaRecharges(self, request):
        """本接口用于获取Kafka数据订阅任务

        :param request: Request instance for DescribeKafkaRecharges.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaRechargesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaRechargesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKafkaRecharges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKafkaRechargesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogContext(self, request):
        """本接口用于搜索日志上下文附近的内容，详情参考[上下文检索](https://cloud.tencent.com/document/product/614/53248)。
        API返回数据包最大49MB，建议启用 gzip 压缩（HTTP Request Header Accept-Encoding:gzip）。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachines(self, request):
        """获取指定机器组下的机器状态

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNoticeContents(self, request):
        """获取通知内容列表

        :param request: Request instance for DescribeNoticeContents.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeNoticeContentsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeNoticeContentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNoticeContents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNoticeContentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePartitions(self, request):
        """该接口已废弃，如需获取分区数量，请使用DescribeTopics接口。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScheduledSqlInfo(self, request):
        """本接口用于获取定时SQL分析任务列表

        :param request: Request instance for DescribeScheduledSqlInfo.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeScheduledSqlInfoRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeScheduledSqlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScheduledSqlInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScheduledSqlInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebCallbacks(self, request):
        """获取告警渠道回调配置列表。

        :param request: Request instance for DescribeWebCallbacks.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeWebCallbacksRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeWebCallbacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebCallbacks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebCallbacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAlarmLog(self, request):
        """本接口用于获取告警策略执行详情

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MergePartition(self, request):
        """该接口已废弃，如需修改分区数量，请使用ModifyTopic接口。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAlarmShield(self, request):
        """该接口用于修改告警屏蔽规则。

        :param request: Request instance for ModifyAlarmShield.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmShieldRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmShieldResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmShield", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmShieldResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudProductLogCollection(self, request):
        """内部云产品接入使用相关接口

        :param request: Request instance for ModifyCloudProductLogCollection.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyCloudProductLogCollectionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyCloudProductLogCollectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudProductLogCollection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudProductLogCollectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsoleSharing(self, request):
        """修改控制台分享，目前仅允许修改有效期

        :param request: Request instance for ModifyConsoleSharing.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyConsoleSharingRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyConsoleSharingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsoleSharing", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsoleSharingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsumer(self, request):
        """本接口用于修改投递Ckafka任务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDashboardSubscribe(self, request):
        """此接口用于修改仪表盘订阅

        :param request: Request instance for ModifyDashboardSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyDashboardSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyDashboardSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDashboardSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDashboardSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataTransform(self, request):
        """本接口用于修改数据加工任务

        :param request: Request instance for ModifyDataTransform.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyDataTransformRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyDataTransformResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataTransform", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataTransformResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyKafkaConsumer(self, request):
        """修改Kafka协议消费信息

        :param request: Request instance for ModifyKafkaConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyKafkaConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyKafkaConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyKafkaConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyKafkaConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyKafkaRecharge(self, request):
        """本接口用于修改Kafka数据订阅任务

        :param request: Request instance for ModifyKafkaRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyKafkaRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyKafkaRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyKafkaRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyKafkaRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNoticeContent(self, request):
        """该接口用于修改通知内容配置

        :param request: Request instance for ModifyNoticeContent.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyNoticeContentRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyNoticeContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNoticeContent", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNoticeContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyScheduledSql(self, request):
        """本接口用于修改定时SQL分析任务

        :param request: Request instance for ModifyScheduledSql.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyScheduledSqlRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyScheduledSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyScheduledSql", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyScheduledSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebCallback(self, request):
        """该接口用于修改告警渠道回调配置。

        :param request: Request instance for ModifyWebCallback.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyWebCallbackRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyWebCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebCallback", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PreviewKafkaRecharge(self, request):
        """本接口用于预览Kafka数据订阅任务客户日志信息

        :param request: Request instance for PreviewKafkaRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.PreviewKafkaRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.PreviewKafkaRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PreviewKafkaRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.PreviewKafkaRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryMetric(self, request):
        """查询指定时刻指标的最新值。
        如果该时刻向前推5分钟内均无指标数据，则无相应的查询结果。

        :param request: Request instance for QueryMetric.
        :type request: :class:`tencentcloud.cls.v20201016.models.QueryMetricRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.QueryMetricResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMetric", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMetricResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryRangeMetric(self, request):
        """查询指定时间范围内指标的变化趋势

        :param request: Request instance for QueryRangeMetric.
        :type request: :class:`tencentcloud.cls.v20201016.models.QueryRangeMetricRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.QueryRangeMetricResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryRangeMetric", params, headers=headers)
            response = json.loads(body)
            model = models.QueryRangeMetricResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchCosRechargeInfo(self, request):
        """本接口用于预览cos导入信息

        :param request: Request instance for SearchCosRechargeInfo.
        :type request: :class:`tencentcloud.cls.v20201016.models.SearchCosRechargeInfoRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.SearchCosRechargeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchCosRechargeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.SearchCosRechargeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchDashboardSubscribe(self, request):
        """此接口用于预览仪表盘订阅

        :param request: Request instance for SearchDashboardSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.SearchDashboardSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.SearchDashboardSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchDashboardSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.SearchDashboardSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchLog(self, request):
        """本接口用于检索分析日志，使用该接口时请注意如下事项：
        1. 该接口除受默认接口请求频率限制外，针对单个日志主题，查询并发数不能超过15。
        2. 检索语法建议使用日志服务专用检索语法CQL，请使用SyntaxRule参数，将值设置为1，控制台默认也使用该语法规则。
        3. API返回数据包最大49MB，建议启用 gzip 压缩（HTTP Request Header Accept-Encoding:gzip）。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SplitPartition(self, request):
        """该接口已废弃，如需修改分区数量，请使用ModifyTopic接口。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadLog(self, request, body):
        """## 提示
        为了保障您日志数据的可靠性以及更高效地使用日志服务，建议您使用CLS优化后的接口[上传结构化日志](https://cloud.tencent.com/document/product/614/16873)。

        同时我们给此接口专门优化定制了多个语言版本的SDK供您选择，SDK提供统一的异步发送、资源控制、自动重试、优雅关闭、感知上报等功能，使上报日志功能更完善，详情请参考[SDK采集](https://cloud.tencent.com/document/product/614/67157)。

        同时云API上传日志接口也支持同步上传日志数据，如果您选择继续使用此接口请参考下文。

        ## 功能描述

        本接口用于将日志写入到指定的日志主题。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))