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
from tencentcloud.cls.v20201016 import models
from typing import Dict


class ClsClient(AbstractClient):
    _apiVersion = '2020-10-16'
    _endpoint = 'cls.tencentcloudapi.com'
    _service = 'cls'

    async def AddMachineGroupInfo(
            self,
            request: models.AddMachineGroupInfoRequest,
            opts: Dict = None,
    ) -> models.AddMachineGroupInfoResponse:
        """
        用于添加机器组信息
        """
        
        kwargs = {}
        kwargs["action"] = "AddMachineGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddMachineGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyConfigToMachineGroup(
            self,
            request: models.ApplyConfigToMachineGroupRequest,
            opts: Dict = None,
    ) -> models.ApplyConfigToMachineGroupResponse:
        """
        应用采集配置到指定机器组
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyConfigToMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyConfigToMachineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckFunction(
            self,
            request: models.CheckFunctionRequest,
            opts: Dict = None,
    ) -> models.CheckFunctionResponse:
        """
        本接口用于数据加工DSL函数的语法校验。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckRechargeKafkaServer(
            self,
            request: models.CheckRechargeKafkaServerRequest,
            opts: Dict = None,
    ) -> models.CheckRechargeKafkaServerResponse:
        """
        本接口用于校验Kafka服务集群是否可以正常访问
        """
        
        kwargs = {}
        kwargs["action"] = "CheckRechargeKafkaServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckRechargeKafkaServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseKafkaConsumer(
            self,
            request: models.CloseKafkaConsumerRequest,
            opts: Dict = None,
    ) -> models.CloseKafkaConsumerResponse:
        """
        关闭Kafka协议消费
        """
        
        kwargs = {}
        kwargs["action"] = "CloseKafkaConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseKafkaConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitConsumerOffsets(
            self,
            request: models.CommitConsumerOffsetsRequest,
            opts: Dict = None,
    ) -> models.CommitConsumerOffsetsResponse:
        """
        提交消费点位
        """
        
        kwargs = {}
        kwargs["action"] = "CommitConsumerOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommitConsumerOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarm(
            self,
            request: models.CreateAlarmRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmResponse:
        """
        本接口用于创建告警策略。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarmNotice(
            self,
            request: models.CreateAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmNoticeResponse:
        """
        该接口用于创建通知渠道组，提供两种配置模式，二选一：
        1，简易模式，提供最基本的通知渠道功能。需填写如下参数：
        - Type
        - NoticeReceivers
        - WebCallbacks

        2，高级模式，在简易模式基础上，支持设定规则，为不同类型的告警分别设定通知渠道，并支持告警升级功能。需填写如下参数：
        - NoticeRules
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarmShield(
            self,
            request: models.CreateAlarmShieldRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmShieldResponse:
        """
        该接口用于创建告警屏蔽规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarmShield"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmShieldResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudProductLogCollection(
            self,
            request: models.CreateCloudProductLogCollectionRequest,
            opts: Dict = None,
    ) -> models.CreateCloudProductLogCollectionResponse:
        """
        内部云产品接入使用相关接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudProductLogCollection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudProductLogCollectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfig(
            self,
            request: models.CreateConfigRequest,
            opts: Dict = None,
    ) -> models.CreateConfigResponse:
        """
        创建采集规则配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfigExtra(
            self,
            request: models.CreateConfigExtraRequest,
            opts: Dict = None,
    ) -> models.CreateConfigExtraResponse:
        """
        本接口用于创建特殊采集配置任务，特殊采集配置应用于自建K8S环境的采集Agent
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfigExtra"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigExtraResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsoleSharing(
            self,
            request: models.CreateConsoleSharingRequest,
            opts: Dict = None,
    ) -> models.CreateConsoleSharingResponse:
        """
        创建控制台分享
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsoleSharing"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsoleSharingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsumer(
            self,
            request: models.CreateConsumerRequest,
            opts: Dict = None,
    ) -> models.CreateConsumerResponse:
        """
        本接口用于创建投递CKafka任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsumerGroup(
            self,
            request: models.CreateConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.CreateConsumerGroupResponse:
        """
        消费组心跳
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosRecharge(
            self,
            request: models.CreateCosRechargeRequest,
            opts: Dict = None,
    ) -> models.CreateCosRechargeResponse:
        """
        本接口用于创建cos导入任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDashboardSubscribe(
            self,
            request: models.CreateDashboardSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreateDashboardSubscribeResponse:
        """
        此接口用于创建仪表盘订阅
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDashboardSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDashboardSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataTransform(
            self,
            request: models.CreateDataTransformRequest,
            opts: Dict = None,
    ) -> models.CreateDataTransformResponse:
        """
        本接口用于创建数据加工任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataTransform"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataTransformResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeliverCloudFunction(
            self,
            request: models.CreateDeliverCloudFunctionRequest,
            opts: Dict = None,
    ) -> models.CreateDeliverCloudFunctionResponse:
        """
        本接口用于创建投递SCF任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeliverCloudFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeliverCloudFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDlcDeliver(
            self,
            request: models.CreateDlcDeliverRequest,
            opts: Dict = None,
    ) -> models.CreateDlcDeliverResponse:
        """
        创建DLC投递任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDlcDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDlcDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEsRecharge(
            self,
            request: models.CreateEsRechargeRequest,
            opts: Dict = None,
    ) -> models.CreateEsRechargeResponse:
        """
        创建es导入配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEsRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEsRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExport(
            self,
            request: models.CreateExportRequest,
            opts: Dict = None,
    ) -> models.CreateExportResponse:
        """
        本接口仅创建下载任务。任务返回的下载地址，请用户调用[DescribeExports](https://cloud.tencent.com/document/product/614/56449)查看任务列表，其中有下载地址CosPath参数。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHostMetricConfig(
            self,
            request: models.CreateHostMetricConfigRequest,
            opts: Dict = None,
    ) -> models.CreateHostMetricConfigResponse:
        """
        创建主机指标采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHostMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIndex(
            self,
            request: models.CreateIndexRequest,
            opts: Dict = None,
    ) -> models.CreateIndexResponse:
        """
        本接口用于创建索引
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKafkaRecharge(
            self,
            request: models.CreateKafkaRechargeRequest,
            opts: Dict = None,
    ) -> models.CreateKafkaRechargeResponse:
        """
        本接口用于创建Kafka数据订阅任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKafkaRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKafkaRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLogset(
            self,
            request: models.CreateLogsetRequest,
            opts: Dict = None,
    ) -> models.CreateLogsetResponse:
        """
        本接口用于创建日志集，返回新创建的日志集的 ID。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMachineGroup(
            self,
            request: models.CreateMachineGroupRequest,
            opts: Dict = None,
    ) -> models.CreateMachineGroupResponse:
        """
        创建机器组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMachineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMetricConfig(
            self,
            request: models.CreateMetricConfigRequest,
            opts: Dict = None,
    ) -> models.CreateMetricConfigResponse:
        """
        创建指标采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMetricSubscribe(
            self,
            request: models.CreateMetricSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreateMetricSubscribeResponse:
        """
        创建指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMetricSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMetricSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNoticeContent(
            self,
            request: models.CreateNoticeContentRequest,
            opts: Dict = None,
    ) -> models.CreateNoticeContentResponse:
        """
        该接口用于创建通知内容。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNoticeContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNoticeContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScheduledSql(
            self,
            request: models.CreateScheduledSqlRequest,
            opts: Dict = None,
    ) -> models.CreateScheduledSqlResponse:
        """
        本接口用于创建定时SQL分析任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScheduledSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScheduledSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateShipper(
            self,
            request: models.CreateShipperRequest,
            opts: Dict = None,
    ) -> models.CreateShipperResponse:
        """
        新建投递到COS的任务，【！！！注意】使用此接口，需要检查是否配置了投递COS的角色和权限。如果没有配置，请参考文档投递权限查看和配置https://cloud.tencent.com/document/product/614/71623。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateShipper"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateShipperResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSplunkDeliver(
            self,
            request: models.CreateSplunkDeliverRequest,
            opts: Dict = None,
    ) -> models.CreateSplunkDeliverResponse:
        """
        创建Splunk投递任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSplunkDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSplunkDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopic(
            self,
            request: models.CreateTopicRequest,
            opts: Dict = None,
    ) -> models.CreateTopicResponse:
        """
        本接口用于创建日志或指标主题。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWebCallback(
            self,
            request: models.CreateWebCallbackRequest,
            opts: Dict = None,
    ) -> models.CreateWebCallbackResponse:
        """
        该接口用于创建告警渠道回调配置。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWebCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWebCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarm(
            self,
            request: models.DeleteAlarmRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmResponse:
        """
        本接口用于删除告警策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarmNotice(
            self,
            request: models.DeleteAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmNoticeResponse:
        """
        该接口用于删除通知渠道组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarmShield(
            self,
            request: models.DeleteAlarmShieldRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmShieldResponse:
        """
        该接口用于删除告警屏蔽规则。当告警屏蔽规则在生效中或者是在失效中，无法被删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmShield"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmShieldResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudProductLogCollection(
            self,
            request: models.DeleteCloudProductLogCollectionRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudProductLogCollectionResponse:
        """
        内部云产品接入使用相关接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudProductLogCollection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudProductLogCollectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfig(
            self,
            request: models.DeleteConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigResponse:
        """
        删除采集规则配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfigExtra(
            self,
            request: models.DeleteConfigExtraRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigExtraResponse:
        """
        本接口用于删除特殊采集规则配置，特殊采集配置应用于自建K8S环境的采集Agent
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfigExtra"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigExtraResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfigFromMachineGroup(
            self,
            request: models.DeleteConfigFromMachineGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigFromMachineGroupResponse:
        """
        删除应用到机器组的采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfigFromMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigFromMachineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsoleSharing(
            self,
            request: models.DeleteConsoleSharingRequest,
            opts: Dict = None,
    ) -> models.DeleteConsoleSharingResponse:
        """
        删除控制台分享
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsoleSharing"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsoleSharingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsumer(
            self,
            request: models.DeleteConsumerRequest,
            opts: Dict = None,
    ) -> models.DeleteConsumerResponse:
        """
        删除投递Ckafka任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsumerGroup(
            self,
            request: models.DeleteConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteConsumerGroupResponse:
        """
        删除消费组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCosRecharge(
            self,
            request: models.DeleteCosRechargeRequest,
            opts: Dict = None,
    ) -> models.DeleteCosRechargeResponse:
        """
        本接口用于删除cos导入任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCosRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCosRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDashboardSubscribe(
            self,
            request: models.DeleteDashboardSubscribeRequest,
            opts: Dict = None,
    ) -> models.DeleteDashboardSubscribeResponse:
        """
        此接口用于删除仪表盘订阅
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDashboardSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDashboardSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataTransform(
            self,
            request: models.DeleteDataTransformRequest,
            opts: Dict = None,
    ) -> models.DeleteDataTransformResponse:
        """
        本接口用于删除数据加工任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataTransform"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataTransformResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDlcDeliver(
            self,
            request: models.DeleteDlcDeliverRequest,
            opts: Dict = None,
    ) -> models.DeleteDlcDeliverResponse:
        """
        删除DLC投递任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDlcDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDlcDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEsRecharge(
            self,
            request: models.DeleteEsRechargeRequest,
            opts: Dict = None,
    ) -> models.DeleteEsRechargeResponse:
        """
        删除es导入配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEsRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEsRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteExport(
            self,
            request: models.DeleteExportRequest,
            opts: Dict = None,
    ) -> models.DeleteExportResponse:
        """
        本接口用于删除日志下载任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHostMetricConfig(
            self,
            request: models.DeleteHostMetricConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteHostMetricConfigResponse:
        """
        删除主机指标采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHostMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHostMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIndex(
            self,
            request: models.DeleteIndexRequest,
            opts: Dict = None,
    ) -> models.DeleteIndexResponse:
        """
        本接口用于删除日志主题的索引配置，删除索引配置后将无法检索和查询采集到的日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteKafkaRecharge(
            self,
            request: models.DeleteKafkaRechargeRequest,
            opts: Dict = None,
    ) -> models.DeleteKafkaRechargeResponse:
        """
        本接口用于删除Kafka数据订阅任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteKafkaRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteKafkaRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogset(
            self,
            request: models.DeleteLogsetRequest,
            opts: Dict = None,
    ) -> models.DeleteLogsetResponse:
        """
        本接口用于删除日志集。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineGroup(
            self,
            request: models.DeleteMachineGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineGroupResponse:
        """
        删除机器组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineGroupInfo(
            self,
            request: models.DeleteMachineGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineGroupInfoResponse:
        """
        用于删除机器组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMetricConfig(
            self,
            request: models.DeleteMetricConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteMetricConfigResponse:
        """
        删除指标采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMetricSubscribe(
            self,
            request: models.DeleteMetricSubscribeRequest,
            opts: Dict = None,
    ) -> models.DeleteMetricSubscribeResponse:
        """
        删除指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMetricSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMetricSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNoticeContent(
            self,
            request: models.DeleteNoticeContentRequest,
            opts: Dict = None,
    ) -> models.DeleteNoticeContentResponse:
        """
        该接口用于删除通知内容配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNoticeContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNoticeContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScheduledSql(
            self,
            request: models.DeleteScheduledSqlRequest,
            opts: Dict = None,
    ) -> models.DeleteScheduledSqlResponse:
        """
        本接口用于删除定时SQL分析任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScheduledSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScheduledSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShipper(
            self,
            request: models.DeleteShipperRequest,
            opts: Dict = None,
    ) -> models.DeleteShipperResponse:
        """
        删除投递COS任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShipper"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShipperResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSplunkDeliver(
            self,
            request: models.DeleteSplunkDeliverRequest,
            opts: Dict = None,
    ) -> models.DeleteSplunkDeliverResponse:
        """
        删除Splunk投递任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSplunkDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSplunkDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopic(
            self,
            request: models.DeleteTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicResponse:
        """
        本接口用于删除日志或指标主题。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebCallback(
            self,
            request: models.DeleteWebCallbackRequest,
            opts: Dict = None,
    ) -> models.DeleteWebCallbackResponse:
        """
        该接口用于删除告警渠道回调配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNotices(
            self,
            request: models.DescribeAlarmNoticesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNoticesResponse:
        """
        该接口用于获取通知渠道组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNotices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNoticesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmShields(
            self,
            request: models.DescribeAlarmShieldsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmShieldsResponse:
        """
        获取告警屏蔽配置规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmShields"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmShieldsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarms(
            self,
            request: models.DescribeAlarmsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmsResponse:
        """
        本接口用于获取告警策略列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlertRecordHistory(
            self,
            request: models.DescribeAlertRecordHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeAlertRecordHistoryResponse:
        """
        获取告警历史，例如今天未恢复的告警
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlertRecordHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlertRecordHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudProductLogTasks(
            self,
            request: models.DescribeCloudProductLogTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudProductLogTasksResponse:
        """
        云产品接入使用相关接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudProductLogTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudProductLogTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterBaseMetricConfigs(
            self,
            request: models.DescribeClusterBaseMetricConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterBaseMetricConfigsResponse:
        """
        获取指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterBaseMetricConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterBaseMetricConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterMetricConfigs(
            self,
            request: models.DescribeClusterMetricConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterMetricConfigsResponse:
        """
        获取指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterMetricConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterMetricConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigExtras(
            self,
            request: models.DescribeConfigExtrasRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigExtrasResponse:
        """
        本接口用于获取特殊采集配置，特殊采集配置应用于自建K8S环境的采集Agent
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigExtras"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigExtrasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigMachineGroups(
            self,
            request: models.DescribeConfigMachineGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigMachineGroupsResponse:
        """
        获取采集规则配置所绑定的机器组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigMachineGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigMachineGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigs(
            self,
            request: models.DescribeConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigsResponse:
        """
        获取采集规则配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsoleSharingList(
            self,
            request: models.DescribeConsoleSharingListRequest,
            opts: Dict = None,
    ) -> models.DescribeConsoleSharingListResponse:
        """
        批量查询控制台分享列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsoleSharingList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsoleSharingListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumer(
            self,
            request: models.DescribeConsumerRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerResponse:
        """
        本接口用于获取投递配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerGroups(
            self,
            request: models.DescribeConsumerGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerGroupsResponse:
        """
        获取消费组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerOffsets(
            self,
            request: models.DescribeConsumerOffsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerOffsetsResponse:
        """
        获取消费组点位信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerPreview(
            self,
            request: models.DescribeConsumerPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerPreviewResponse:
        """
        本接口用于kafka投递数据预览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumers(
            self,
            request: models.DescribeConsumersRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumersResponse:
        """
        获取投递规则信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosRecharges(
            self,
            request: models.DescribeCosRechargesRequest,
            opts: Dict = None,
    ) -> models.DescribeCosRechargesResponse:
        """
        本接口用于获取cos导入配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosRecharges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosRechargesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDashboardSubscribes(
            self,
            request: models.DescribeDashboardSubscribesRequest,
            opts: Dict = None,
    ) -> models.DescribeDashboardSubscribesResponse:
        """
        本接口用于获取仪表盘订阅列表，支持分页
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDashboardSubscribes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDashboardSubscribesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDashboards(
            self,
            request: models.DescribeDashboardsRequest,
            opts: Dict = None,
    ) -> models.DescribeDashboardsResponse:
        """
        本接口用于获取仪表盘
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDashboards"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDashboardsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataTransformInfo(
            self,
            request: models.DescribeDataTransformInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataTransformInfoResponse:
        """
        本接口用于获取数据加工任务列表基本信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataTransformInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataTransformInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDlcDelivers(
            self,
            request: models.DescribeDlcDeliversRequest,
            opts: Dict = None,
    ) -> models.DescribeDlcDeliversResponse:
        """
        获取告警渠道回调配置列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDlcDelivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDlcDeliversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEsRechargePreview(
            self,
            request: models.DescribeEsRechargePreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeEsRechargePreviewResponse:
        """
        es导入预览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEsRechargePreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEsRechargePreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEsRecharges(
            self,
            request: models.DescribeEsRechargesRequest,
            opts: Dict = None,
    ) -> models.DescribeEsRechargesResponse:
        """
        获取es导入配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEsRecharges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEsRechargesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExports(
            self,
            request: models.DescribeExportsRequest,
            opts: Dict = None,
    ) -> models.DescribeExportsResponse:
        """
        本接口用于获取日志下载任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostMetricConfigs(
            self,
            request: models.DescribeHostMetricConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeHostMetricConfigsResponse:
        """
        获取指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostMetricConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostMetricConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndex(
            self,
            request: models.DescribeIndexRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexResponse:
        """
        本接口用于获取索引配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaConsumer(
            self,
            request: models.DescribeKafkaConsumerRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaConsumerResponse:
        """
        获取Kafka协议消费信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaConsumerGroupDetail(
            self,
            request: models.DescribeKafkaConsumerGroupDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaConsumerGroupDetailResponse:
        """
        获取Kafka协议消费组详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaConsumerGroupDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaConsumerGroupDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaConsumerGroupList(
            self,
            request: models.DescribeKafkaConsumerGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaConsumerGroupListResponse:
        """
        获取Kafka协议消费组信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaConsumerGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaConsumerGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaConsumerPreview(
            self,
            request: models.DescribeKafkaConsumerPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaConsumerPreviewResponse:
        """
        kafka协议消费预览接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaConsumerPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaConsumerPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaConsumerTopics(
            self,
            request: models.DescribeKafkaConsumerTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaConsumerTopicsResponse:
        """
        本接口用于获取kafka协议消费主题信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaConsumerTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaConsumerTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaRecharges(
            self,
            request: models.DescribeKafkaRechargesRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaRechargesResponse:
        """
        本接口用于获取Kafka数据订阅任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaRecharges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaRechargesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogContext(
            self,
            request: models.DescribeLogContextRequest,
            opts: Dict = None,
    ) -> models.DescribeLogContextResponse:
        """
        本接口用于搜索日志上下文附近的内容，详情参考[上下文检索](https://cloud.tencent.com/document/product/614/53248)。
        API返回数据包最大49MB，建议启用 gzip 压缩（HTTP Request Header Accept-Encoding:gzip）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogContext"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogContextResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogHistogram(
            self,
            request: models.DescribeLogHistogramRequest,
            opts: Dict = None,
    ) -> models.DescribeLogHistogramResponse:
        """
        本接口用于构建日志数量直方图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogHistogram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogHistogramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogsets(
            self,
            request: models.DescribeLogsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogsetsResponse:
        """
        本接口用于获取日志集信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineGroupConfigs(
            self,
            request: models.DescribeMachineGroupConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineGroupConfigsResponse:
        """
        获取机器组绑定的采集规则配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineGroupConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineGroupConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineGroups(
            self,
            request: models.DescribeMachineGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineGroupsResponse:
        """
        获取机器组信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachines(
            self,
            request: models.DescribeMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeMachinesResponse:
        """
        获取指定机器组下的机器状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricCorrectDimension(
            self,
            request: models.DescribeMetricCorrectDimensionRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricCorrectDimensionResponse:
        """
        获取指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricCorrectDimension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricCorrectDimensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricSubscribePreview(
            self,
            request: models.DescribeMetricSubscribePreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricSubscribePreviewResponse:
        """
        创建指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricSubscribePreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricSubscribePreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricSubscribes(
            self,
            request: models.DescribeMetricSubscribesRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricSubscribesResponse:
        """
        获取指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricSubscribes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricSubscribesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNoticeContents(
            self,
            request: models.DescribeNoticeContentsRequest,
            opts: Dict = None,
    ) -> models.DescribeNoticeContentsResponse:
        """
        获取通知内容列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNoticeContents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNoticeContentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePartitions(
            self,
            request: models.DescribePartitionsRequest,
            opts: Dict = None,
    ) -> models.DescribePartitionsResponse:
        """
        该接口已废弃，如需获取分区数量，请使用DescribeTopics接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePartitions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePartitionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScheduledSqlInfo(
            self,
            request: models.DescribeScheduledSqlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeScheduledSqlInfoResponse:
        """
        本接口用于获取定时SQL分析任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScheduledSqlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScheduledSqlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShipperTasks(
            self,
            request: models.DescribeShipperTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeShipperTasksResponse:
        """
        获取投递任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShipperTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShipperTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShippers(
            self,
            request: models.DescribeShippersRequest,
            opts: Dict = None,
    ) -> models.DescribeShippersResponse:
        """
        获取投递到COS的任务配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShippers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShippersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSplunkDelivers(
            self,
            request: models.DescribeSplunkDeliversRequest,
            opts: Dict = None,
    ) -> models.DescribeSplunkDeliversResponse:
        """
        获取Splunk投递任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSplunkDelivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSplunkDeliversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSplunkPreview(
            self,
            request: models.DescribeSplunkPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeSplunkPreviewResponse:
        """
        splunk投递任务预览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSplunkPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSplunkPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicBaseMetricConfigs(
            self,
            request: models.DescribeTopicBaseMetricConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicBaseMetricConfigsResponse:
        """
        获取指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicBaseMetricConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicBaseMetricConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicMetricConfigs(
            self,
            request: models.DescribeTopicMetricConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicMetricConfigsResponse:
        """
        获取指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicMetricConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicMetricConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopics(
            self,
            request: models.DescribeTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicsResponse:
        """
        本接口用于获取日志或指标主题列表，支持分页
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebCallbacks(
            self,
            request: models.DescribeWebCallbacksRequest,
            opts: Dict = None,
    ) -> models.DescribeWebCallbacksResponse:
        """
        获取告警渠道回调配置列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebCallbacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebCallbacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAlarmLog(
            self,
            request: models.GetAlarmLogRequest,
            opts: Dict = None,
    ) -> models.GetAlarmLogResponse:
        """
        本接口用于获取告警策略执行详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetAlarmLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAlarmLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMetricLabelValues(
            self,
            request: models.GetMetricLabelValuesRequest,
            opts: Dict = None,
    ) -> models.GetMetricLabelValuesResponse:
        """
        获取时序label values列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetMetricLabelValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMetricLabelValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MergePartition(
            self,
            request: models.MergePartitionRequest,
            opts: Dict = None,
    ) -> models.MergePartitionResponse:
        """
        该接口已废弃，如需修改分区数量，请使用ModifyTopic接口。
        """
        
        kwargs = {}
        kwargs["action"] = "MergePartition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MergePartitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarm(
            self,
            request: models.ModifyAlarmRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmResponse:
        """
        本接口用于修改告警策略。需要至少修改一项有效内容。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmNotice(
            self,
            request: models.ModifyAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmNoticeResponse:
        """
        该接口用于修改通知渠道组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmShield(
            self,
            request: models.ModifyAlarmShieldRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmShieldResponse:
        """
        该接口用于修改告警屏蔽规则。当告警屏蔽规则为失效中时，无法对其进行修改
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmShield"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmShieldResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudProductLogCollection(
            self,
            request: models.ModifyCloudProductLogCollectionRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudProductLogCollectionResponse:
        """
        内部云产品接入使用相关接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudProductLogCollection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudProductLogCollectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConfig(
            self,
            request: models.ModifyConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyConfigResponse:
        """
        修改采集规则配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConfigExtra(
            self,
            request: models.ModifyConfigExtraRequest,
            opts: Dict = None,
    ) -> models.ModifyConfigExtraResponse:
        """
        本接口用于修改特殊采集配置任务，特殊采集配置应用于自建K8S环境的采集Agent
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConfigExtra"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConfigExtraResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsoleSharing(
            self,
            request: models.ModifyConsoleSharingRequest,
            opts: Dict = None,
    ) -> models.ModifyConsoleSharingResponse:
        """
        修改控制台分享，目前仅允许修改有效期
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsoleSharing"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsoleSharingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsumer(
            self,
            request: models.ModifyConsumerRequest,
            opts: Dict = None,
    ) -> models.ModifyConsumerResponse:
        """
        本接口用于修改投递Ckafka任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsumerGroup(
            self,
            request: models.ModifyConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyConsumerGroupResponse:
        """
        更新消费组信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCosRecharge(
            self,
            request: models.ModifyCosRechargeRequest,
            opts: Dict = None,
    ) -> models.ModifyCosRechargeResponse:
        """
        本接口用于修改cos导入任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCosRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCosRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDashboardSubscribe(
            self,
            request: models.ModifyDashboardSubscribeRequest,
            opts: Dict = None,
    ) -> models.ModifyDashboardSubscribeResponse:
        """
        此接口用于修改仪表盘订阅
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDashboardSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDashboardSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDataTransform(
            self,
            request: models.ModifyDataTransformRequest,
            opts: Dict = None,
    ) -> models.ModifyDataTransformResponse:
        """
        本接口用于修改数据加工任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDataTransform"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDataTransformResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDlcDeliver(
            self,
            request: models.ModifyDlcDeliverRequest,
            opts: Dict = None,
    ) -> models.ModifyDlcDeliverResponse:
        """
        修改DLC投递任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDlcDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDlcDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEsRecharge(
            self,
            request: models.ModifyEsRechargeRequest,
            opts: Dict = None,
    ) -> models.ModifyEsRechargeResponse:
        """
        修改es导入配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEsRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEsRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostMetricConfig(
            self,
            request: models.ModifyHostMetricConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyHostMetricConfigResponse:
        """
        修改主机指标采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIndex(
            self,
            request: models.ModifyIndexRequest,
            opts: Dict = None,
    ) -> models.ModifyIndexResponse:
        """
        本接口用于修改索引配置，该接口除受默认接口请求频率限制外，针对单个日志主题，并发数不能超过1，即同一时间同一个日志主题只能有一个正在执行的索引配置修改操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyKafkaConsumer(
            self,
            request: models.ModifyKafkaConsumerRequest,
            opts: Dict = None,
    ) -> models.ModifyKafkaConsumerResponse:
        """
        修改Kafka协议消费信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyKafkaConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyKafkaConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyKafkaConsumerGroupOffset(
            self,
            request: models.ModifyKafkaConsumerGroupOffsetRequest,
            opts: Dict = None,
    ) -> models.ModifyKafkaConsumerGroupOffsetResponse:
        """
        修改Kafka协议消费组点位
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyKafkaConsumerGroupOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyKafkaConsumerGroupOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyKafkaRecharge(
            self,
            request: models.ModifyKafkaRechargeRequest,
            opts: Dict = None,
    ) -> models.ModifyKafkaRechargeResponse:
        """
        本接口用于修改Kafka数据订阅任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyKafkaRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyKafkaRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogset(
            self,
            request: models.ModifyLogsetRequest,
            opts: Dict = None,
    ) -> models.ModifyLogsetResponse:
        """
        本接口用于修改日志集信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMachineGroup(
            self,
            request: models.ModifyMachineGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyMachineGroupResponse:
        """
        修改机器组。
        注意：修改接口直接覆盖历史数据，改为本次合法入参数据，请谨慎调用此接口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMetricConfig(
            self,
            request: models.ModifyMetricConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyMetricConfigResponse:
        """
        创建指标采集配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMetricSubscribe(
            self,
            request: models.ModifyMetricSubscribeRequest,
            opts: Dict = None,
    ) -> models.ModifyMetricSubscribeResponse:
        """
        修改指标订阅配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMetricSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMetricSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNoticeContent(
            self,
            request: models.ModifyNoticeContentRequest,
            opts: Dict = None,
    ) -> models.ModifyNoticeContentResponse:
        """
        该接口用于修改通知内容配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNoticeContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNoticeContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyScheduledSql(
            self,
            request: models.ModifyScheduledSqlRequest,
            opts: Dict = None,
    ) -> models.ModifyScheduledSqlResponse:
        """
        本接口用于修改定时SQL分析任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyScheduledSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyScheduledSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyShipper(
            self,
            request: models.ModifyShipperRequest,
            opts: Dict = None,
    ) -> models.ModifyShipperResponse:
        """
        修改现有的投递规则，客户如果使用此接口，需要自行处理CLS对指定bucket的写权限。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyShipper"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyShipperResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySplunkDeliver(
            self,
            request: models.ModifySplunkDeliverRequest,
            opts: Dict = None,
    ) -> models.ModifySplunkDeliverResponse:
        """
        修改splunk投递任务相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySplunkDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySplunkDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTopic(
            self,
            request: models.ModifyTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyTopicResponse:
        """
        本接口用于修改日志或指标主题。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebCallback(
            self,
            request: models.ModifyWebCallbackRequest,
            opts: Dict = None,
    ) -> models.ModifyWebCallbackResponse:
        """
        该接口用于修改告警渠道回调配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenKafkaConsumer(
            self,
            request: models.OpenKafkaConsumerRequest,
            opts: Dict = None,
    ) -> models.OpenKafkaConsumerResponse:
        """
        打开Kafka协议消费功能
        """
        
        kwargs = {}
        kwargs["action"] = "OpenKafkaConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenKafkaConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PreviewKafkaRecharge(
            self,
            request: models.PreviewKafkaRechargeRequest,
            opts: Dict = None,
    ) -> models.PreviewKafkaRechargeResponse:
        """
        本接口用于预览Kafka数据订阅任务客户日志信息
        """
        
        kwargs = {}
        kwargs["action"] = "PreviewKafkaRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PreviewKafkaRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMetric(
            self,
            request: models.QueryMetricRequest,
            opts: Dict = None,
    ) -> models.QueryMetricResponse:
        """
        查询指定时刻指标的最新值。
        如果该时刻向前推5分钟内均无指标数据，则无相应的查询结果。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMetric"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMetricResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryRangeMetric(
            self,
            request: models.QueryRangeMetricRequest,
            opts: Dict = None,
    ) -> models.QueryRangeMetricResponse:
        """
        查询指定时间范围内指标的变化趋势
        """
        
        kwargs = {}
        kwargs["action"] = "QueryRangeMetric"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryRangeMetricResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryShipperTask(
            self,
            request: models.RetryShipperTaskRequest,
            opts: Dict = None,
    ) -> models.RetryShipperTaskResponse:
        """
        重试失败的投递任务
        """
        
        kwargs = {}
        kwargs["action"] = "RetryShipperTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryShipperTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchCosRechargeInfo(
            self,
            request: models.SearchCosRechargeInfoRequest,
            opts: Dict = None,
    ) -> models.SearchCosRechargeInfoResponse:
        """
        本接口用于预览cos导入信息
        """
        
        kwargs = {}
        kwargs["action"] = "SearchCosRechargeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchCosRechargeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchDashboardSubscribe(
            self,
            request: models.SearchDashboardSubscribeRequest,
            opts: Dict = None,
    ) -> models.SearchDashboardSubscribeResponse:
        """
        此接口用于预览仪表盘订阅
        """
        
        kwargs = {}
        kwargs["action"] = "SearchDashboardSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchDashboardSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchLog(
            self,
            request: models.SearchLogRequest,
            opts: Dict = None,
    ) -> models.SearchLogResponse:
        """
        本接口用于检索分析日志，使用该接口时请注意如下事项：
        1. 该接口除受默认接口请求频率限制外，针对单个日志主题，查询并发数不能超过15。
        2. 检索语法建议使用日志服务专用检索语法CQL，请使用SyntaxRule参数，将值设置为1，控制台默认也使用该语法规则。
        3. API返回数据包最大49MB，建议启用 gzip 压缩（HTTP Request Header Accept-Encoding:gzip）。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendConsumerHeartbeat(
            self,
            request: models.SendConsumerHeartbeatRequest,
            opts: Dict = None,
    ) -> models.SendConsumerHeartbeatResponse:
        """
        消费组心跳
        """
        
        kwargs = {}
        kwargs["action"] = "SendConsumerHeartbeat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendConsumerHeartbeatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SplitPartition(
            self,
            request: models.SplitPartitionRequest,
            opts: Dict = None,
    ) -> models.SplitPartitionResponse:
        """
        该接口已废弃，如需修改分区数量，请使用ModifyTopic接口。
        """
        
        kwargs = {}
        kwargs["action"] = "SplitPartition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SplitPartitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadLog(
            self,
            request: models.UploadLogRequest,
            body: bytes,
            opts: Dict = None,
    ) -> models.UploadLogResponse:
        """
        ## 提示
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
        """
        
        kwargs = {}
        kwargs["action"] = "UploadLog"
        kwargs["params"] = body
        kwargs["resp_cls"] = models.UploadLogResponse
        kwargs["headers"] = request.headers or {}
        kwargs["headers"].update({"X-CLS-" + k : v for k, v in request._serialize().items()})
        kwargs["opts"] = opts or {}
        kwargs["opts"]["IsOctetStream"] = True
        
        return await self.call_and_deserialize(**kwargs)