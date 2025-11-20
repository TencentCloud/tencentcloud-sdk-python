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
from tencentcloud.cloudaudit.v20190319 import models
from typing import Dict


class CloudauditClient(AbstractClient):
    _apiVersion = '2019-03-19'
    _endpoint = 'cloudaudit.tencentcloudapi.com'
    _service = 'cloudaudit'

    async def CreateAuditTrack(
            self,
            request: models.CreateAuditTrackRequest,
            opts: Dict = None,
    ) -> models.CreateAuditTrackResponse:
        """
        创建操作审计跟踪集
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditTrack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditTrackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEventsAuditTrack(
            self,
            request: models.CreateEventsAuditTrackRequest,
            opts: Dict = None,
    ) -> models.CreateEventsAuditTrackResponse:
        """
        创建操作审计跟踪集
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEventsAuditTrack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEventsAuditTrackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditTrack(
            self,
            request: models.DeleteAuditTrackRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditTrackResponse:
        """
        删除操作审计跟踪集
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditTrack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditTrackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAudit(
            self,
            request: models.DescribeAuditRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditResponse:
        """
        查询跟踪集详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAudit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditTrack(
            self,
            request: models.DescribeAuditTrackRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditTrackResponse:
        """
        查询操作审计跟踪集详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditTrack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditTrackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditTracks(
            self,
            request: models.DescribeAuditTracksRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditTracksResponse:
        """
        查询操作审计跟踪集列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditTracks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditTracksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEvents(
            self,
            request: models.DescribeEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeEventsResponse:
        """
        查询操作审计日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAttributeKey(
            self,
            request: models.GetAttributeKeyRequest,
            opts: Dict = None,
    ) -> models.GetAttributeKeyResponse:
        """
        查询AttributeKey的有效取值范围
        """
        
        kwargs = {}
        kwargs["action"] = "GetAttributeKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAttributeKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquireAuditCredit(
            self,
            request: models.InquireAuditCreditRequest,
            opts: Dict = None,
    ) -> models.InquireAuditCreditResponse:
        """
        查询用户可创建跟踪集的数量
        """
        
        kwargs = {}
        kwargs["action"] = "InquireAuditCredit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquireAuditCreditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAudits(
            self,
            request: models.ListAuditsRequest,
            opts: Dict = None,
    ) -> models.ListAuditsResponse:
        """
        查询跟踪集概要
        """
        
        kwargs = {}
        kwargs["action"] = "ListAudits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAuditsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCmqEnableRegion(
            self,
            request: models.ListCmqEnableRegionRequest,
            opts: Dict = None,
    ) -> models.ListCmqEnableRegionResponse:
        """
        查询操作审计支持的cmq的可用区
        """
        
        kwargs = {}
        kwargs["action"] = "ListCmqEnableRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCmqEnableRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCosEnableRegion(
            self,
            request: models.ListCosEnableRegionRequest,
            opts: Dict = None,
    ) -> models.ListCosEnableRegionResponse:
        """
        查询操作审计支持的cos可用区
        """
        
        kwargs = {}
        kwargs["action"] = "ListCosEnableRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCosEnableRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListKeyAliasByRegion(
            self,
            request: models.ListKeyAliasByRegionRequest,
            opts: Dict = None,
    ) -> models.ListKeyAliasByRegionResponse:
        """
        根据地域获取KMS密钥别名
        """
        
        kwargs = {}
        kwargs["action"] = "ListKeyAliasByRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListKeyAliasByRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LookUpEvents(
            self,
            request: models.LookUpEventsRequest,
            opts: Dict = None,
    ) -> models.LookUpEventsResponse:
        """
        用于对操作日志进行检索，便于用户进行查询相关的操作信息。
        """
        
        kwargs = {}
        kwargs["action"] = "LookUpEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LookUpEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditTrack(
            self,
            request: models.ModifyAuditTrackRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditTrackResponse:
        """
        修改操作审计跟踪集
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditTrack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditTrackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEventsAuditTrack(
            self,
            request: models.ModifyEventsAuditTrackRequest,
            opts: Dict = None,
    ) -> models.ModifyEventsAuditTrackResponse:
        """
        修改操作审计跟踪集
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEventsAuditTrack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEventsAuditTrackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartLogging(
            self,
            request: models.StartLoggingRequest,
            opts: Dict = None,
    ) -> models.StartLoggingResponse:
        """
        开启跟踪集
        """
        
        kwargs = {}
        kwargs["action"] = "StartLogging"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartLoggingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopLogging(
            self,
            request: models.StopLoggingRequest,
            opts: Dict = None,
    ) -> models.StopLoggingResponse:
        """
        关闭跟踪集
        """
        
        kwargs = {}
        kwargs["action"] = "StopLogging"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopLoggingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAudit(
            self,
            request: models.UpdateAuditRequest,
            opts: Dict = None,
    ) -> models.UpdateAuditResponse:
        """
        参数要求：
        1、如果IsCreateNewBucket的值存在的话，cosRegion和cosBucketName都是必填参数。
        2、如果IsEnableCmqNotify的值是1的话，IsCreateNewQueue、CmqRegion和CmqQueueName都是必填参数。
        3、如果IsEnableCmqNotify的值是0的话，IsCreateNewQueue、CmqRegion和CmqQueueName都不能传。
        4、如果IsEnableKmsEncry的值是1的话，KmsRegion和KeyId属于必填项
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAudit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAuditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)