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
from tencentcloud.ms.v20180408 import models
from typing import Dict


class MsClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'ms.tencentcloudapi.com'
    _service = 'ms'

    async def CancelEncryptTask(
            self,
            request: models.CancelEncryptTaskRequest,
            opts: Dict = None,
    ) -> models.CancelEncryptTaskResponse:
        """
        该接口供渠道合作应用加固使用，接口调用有白名单用户限制，取消渠道合作加固中的任务
        """
        
        kwargs = {}
        kwargs["action"] = "CancelEncryptTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelEncryptTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBindInstance(
            self,
            request: models.CreateBindInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateBindInstanceResponse:
        """
        将应用和资源进行绑定。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBindInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBindInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosSecKeyInstance(
            self,
            request: models.CreateCosSecKeyInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateCosSecKeyInstanceResponse:
        """
        获取云COS文件存储临时密钥，密钥仅限于临时上传文件，有访问限制和时效性，请保管好临时密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosSecKeyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosSecKeyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEncryptInstance(
            self,
            request: models.CreateEncryptInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateEncryptInstanceResponse:
        """
        该接口供渠道合作应用加固使用，接口调用有白名单用户限制，用于创建加固任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEncryptInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEncryptInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrderInstance(
            self,
            request: models.CreateOrderInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateOrderInstanceResponse:
        """
        该接口供渠道合作应用加固使用，接口调用有白名单用户限制。
        订单类型有：免费试用、按年收费、按次收费。
        应用加固支持的平台类型有：android加固 、ios源码混淆 、sdk加固、applet小程序加固
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrderInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrderInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResourceInstances(
            self,
            request: models.CreateResourceInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateResourceInstancesResponse:
        """
        不再使用

        用户可以使用该接口自建资源，只支持白名单用户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResourceInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateShieldInstance(
            self,
            request: models.CreateShieldInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateShieldInstanceResponse:
        """
        用户通过该接口提交应用进行应用加固，加固后需通过DescribeShieldResult接口查询加固结果。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateShieldInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateShieldInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateShieldPlanInstance(
            self,
            request: models.CreateShieldPlanInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateShieldPlanInstanceResponse:
        """
        对资源进行策略新增。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateShieldPlanInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateShieldPlanInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShieldInstances(
            self,
            request: models.DeleteShieldInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteShieldInstancesResponse:
        """
        删除一个或者多个app加固信息。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShieldInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShieldInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApkDetectionResult(
            self,
            request: models.DescribeApkDetectionResultRequest,
            opts: Dict = None,
    ) -> models.DescribeApkDetectionResultResponse:
        """
        该接口采用同步模式请求腾讯APK云检测服务，即时返回检测数据，需要用户用轮询的方式调用本接口来进行样本送检并获取检测结果(每隔60s发送一次请求，传相同的参数，重试30次)，一般情况下0.5h内会出检测结果，最长时间是3h。当Result为ok并且ResultList数组非空有值时，代表检测完毕，若长时间获取不到检测结果，请联系客服。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApkDetectionResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApkDetectionResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEncryptInstances(
            self,
            request: models.DescribeEncryptInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeEncryptInstancesResponse:
        """
        该接口供渠道合作应用加固使用，接口调用有白名单用户限制，用于查询加固任务，入参中的条件过滤字段均为精准匹配。支持功能点: 1. 多任务分页查询  2.根据任务Id唯一值查询单记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEncryptInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEncryptInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEncryptPlan(
            self,
            request: models.DescribeEncryptPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeEncryptPlanResponse:
        """
        该接口供渠道合作应用加固使用，接口调用有白名单用户限制。入参中的条件过滤字段均为精准匹配。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEncryptPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEncryptPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrderInstances(
            self,
            request: models.DescribeOrderInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeOrderInstancesResponse:
        """
        该接口供渠道合作应用加固使用，接口调用有白名单用户限制。 接口返回的结果为：创建订单后，订单审批状态信息，以及与订单关联的资源状态等信息，入参中的条件过滤字段均为精准匹配.
        接口功能点：
        1.支持多订单分页查询；
        2.支持唯一订单号精准匹配查询；
        3.支持唯一资源号精准匹配查询；
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrderInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrderInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceInstances(
            self,
            request: models.DescribeResourceInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceInstancesResponse:
        """
        获取某个用户的所有资源信息。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShieldInstances(
            self,
            request: models.DescribeShieldInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeShieldInstancesResponse:
        """
        本接口用于查看app列表。
        可以通过指定任务唯一标识ItemId来查询指定app的详细信息，或通过设定过滤器来查询满足过滤条件的app的详细信息。 指定偏移(Offset)和限制(Limit)来选择结果中的一部分，默认返回满足条件的前20个app信息。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShieldInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShieldInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShieldPlanInstance(
            self,
            request: models.DescribeShieldPlanInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeShieldPlanInstanceResponse:
        """
        查询加固策略。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShieldPlanInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShieldPlanInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShieldResult(
            self,
            request: models.DescribeShieldResultRequest,
            opts: Dict = None,
    ) -> models.DescribeShieldResultResponse:
        """
        通过唯一标识获取加固的结果。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShieldResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShieldResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUrlDetectionResult(
            self,
            request: models.DescribeUrlDetectionResultRequest,
            opts: Dict = None,
    ) -> models.DescribeUrlDetectionResultResponse:
        """
        移动安全-网址检测服务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUrlDetectionResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUrlDetectionResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserBaseInfoInstance(
            self,
            request: models.DescribeUserBaseInfoInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeUserBaseInfoInstanceResponse:
        """
        获取用户基础信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserBaseInfoInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserBaseInfoInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyResourceInstances(
            self,
            request: models.DestroyResourceInstancesRequest,
            opts: Dict = None,
    ) -> models.DestroyResourceInstancesResponse:
        """
        渠道合作资源销毁
        安卓应用加固-按年收费资源销毁，其他类型暂不支持
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyResourceInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyResourceInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RequestLocalTask(
            self,
            request: models.RequestLocalTaskRequest,
            opts: Dict = None,
    ) -> models.RequestLocalTaskResponse:
        """
        client任务请求
        """
        
        kwargs = {}
        kwargs["action"] = "RequestLocalTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RequestLocalTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateClientState(
            self,
            request: models.UpdateClientStateRequest,
            opts: Dict = None,
    ) -> models.UpdateClientStateResponse:
        """
        更新client状态，需要白名单
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateClientState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateClientStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateLocalTaskResult(
            self,
            request: models.UpdateLocalTaskResultRequest,
            opts: Dict = None,
    ) -> models.UpdateLocalTaskResultResponse:
        """
        更新本地任务执行结果
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateLocalTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateLocalTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)