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
from tencentcloud.privatedns.v20201028 import models
from typing import Dict


class PrivatednsClient(AbstractClient):
    _apiVersion = '2020-10-28'
    _endpoint = 'privatedns.tencentcloudapi.com'
    _service = 'privatedns'

    async def AddSpecifyPrivateZoneVpc(
            self,
            request: models.AddSpecifyPrivateZoneVpcRequest,
            opts: Dict = None,
    ) -> models.AddSpecifyPrivateZoneVpcResponse:
        """
        追加与私有域关联的VPC
        """
        
        kwargs = {}
        kwargs["action"] = "AddSpecifyPrivateZoneVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddSpecifyPrivateZoneVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExtendEndpoint(
            self,
            request: models.CreateExtendEndpointRequest,
            opts: Dict = None,
    ) -> models.CreateExtendEndpointResponse:
        """
        创建终端节点
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExtendEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExtendEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateForwardRule(
            self,
            request: models.CreateForwardRuleRequest,
            opts: Dict = None,
    ) -> models.CreateForwardRuleResponse:
        """
        创建自定义转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateForwardRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInboundEndpoint(
            self,
            request: models.CreateInboundEndpointRequest,
            opts: Dict = None,
    ) -> models.CreateInboundEndpointResponse:
        """
        删除入站终端节点
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInboundEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInboundEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateDNSAccount(
            self,
            request: models.CreatePrivateDNSAccountRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateDNSAccountResponse:
        """
        跨账号关联VPC时，可通过该API接口添加关联账号
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateDNSAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateDNSAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateZone(
            self,
            request: models.CreatePrivateZoneRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateZoneResponse:
        """
        创建私有域
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateZoneList(
            self,
            request: models.CreatePrivateZoneListRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateZoneListResponse:
        """
        批量创建私有域
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateZoneList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateZoneListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateZoneRecord(
            self,
            request: models.CreatePrivateZoneRecordRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateZoneRecordResponse:
        """
        添加私有域解析记录
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateZoneRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateZoneRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateZoneRecordList(
            self,
            request: models.CreatePrivateZoneRecordListRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateZoneRecordListResponse:
        """
        批量添加私有域解析记录
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateZoneRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateZoneRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEndPoint(
            self,
            request: models.DeleteEndPointRequest,
            opts: Dict = None,
    ) -> models.DeleteEndPointResponse:
        """
        删除终端节点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteForwardRule(
            self,
            request: models.DeleteForwardRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteForwardRuleResponse:
        """
        删除转发规则并停止转发
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteForwardRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInboundEndpoint(
            self,
            request: models.DeleteInboundEndpointRequest,
            opts: Dict = None,
    ) -> models.DeleteInboundEndpointResponse:
        """
        删除入站终端节点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInboundEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInboundEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateDNSAccount(
            self,
            request: models.DeletePrivateDNSAccountRequest,
            opts: Dict = None,
    ) -> models.DeletePrivateDNSAccountResponse:
        """
        适用于跨账号绑定VPC时需要移除关联账号的场景，解除账号关联后，将无法获取对应账号下的 VPC资源。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateDNSAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateDNSAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateZone(
            self,
            request: models.DeletePrivateZoneRequest,
            opts: Dict = None,
    ) -> models.DeletePrivateZoneResponse:
        """
        删除私有域并停止解析
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateZoneRecord(
            self,
            request: models.DeletePrivateZoneRecordRequest,
            opts: Dict = None,
    ) -> models.DeletePrivateZoneRecordResponse:
        """
        删除私有域解析记录
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateZoneRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateZoneRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSpecifyPrivateZoneVpc(
            self,
            request: models.DeleteSpecifyPrivateZoneVpcRequest,
            opts: Dict = None,
    ) -> models.DeleteSpecifyPrivateZoneVpcResponse:
        """
        删除与私有域关联的VPC
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSpecifyPrivateZoneVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSpecifyPrivateZoneVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountVpcList(
            self,
            request: models.DescribeAccountVpcListRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountVpcListResponse:
        """
        获取关联账号的VPC列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountVpcList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountVpcListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditLog(
            self,
            request: models.DescribeAuditLogRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditLogResponse:
        """
        获取操作日志列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCreateRecordListResult(
            self,
            request: models.DescribeCreateRecordListResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCreateRecordListResultResponse:
        """
        查询批量添加私有域解析记录结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCreateRecordListResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCreateRecordListResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCreateZoneListResult(
            self,
            request: models.DescribeCreateZoneListResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCreateZoneListResultResponse:
        """
        查询批量添加私有域结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCreateZoneListResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCreateZoneListResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDashboard(
            self,
            request: models.DescribeDashboardRequest,
            opts: Dict = None,
    ) -> models.DescribeDashboardResponse:
        """
        获取私有域解析概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExtendEndpointList(
            self,
            request: models.DescribeExtendEndpointListRequest,
            opts: Dict = None,
    ) -> models.DescribeExtendEndpointListResponse:
        """
        获取终端节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExtendEndpointList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExtendEndpointListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeForwardRuleList(
            self,
            request: models.DescribeForwardRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeForwardRuleListResponse:
        """
        查询转发规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeForwardRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeForwardRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInboundEndpointList(
            self,
            request: models.DescribeInboundEndpointListRequest,
            opts: Dict = None,
    ) -> models.DescribeInboundEndpointListResponse:
        """
        获取入站终端节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInboundEndpointList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInboundEndpointListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateDNSAccountList(
            self,
            request: models.DescribePrivateDNSAccountListRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateDNSAccountListResponse:
        """
        在跨账号绑定VPC的场景下，可通过该API接口获取所有已关联账号的列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateDNSAccountList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateDNSAccountListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateZone(
            self,
            request: models.DescribePrivateZoneRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateZoneResponse:
        """
        获取私有域信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateZoneList(
            self,
            request: models.DescribePrivateZoneListRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateZoneListResponse:
        """
        获取私有域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateZoneList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateZoneListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateZoneRecordList(
            self,
            request: models.DescribePrivateZoneRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateZoneRecordListResponse:
        """
        获取私有域记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateZoneRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateZoneRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateZoneService(
            self,
            request: models.DescribePrivateZoneServiceRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateZoneServiceResponse:
        """
        查询私有域解析开通状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateZoneService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateZoneServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuotaUsage(
            self,
            request: models.DescribeQuotaUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeQuotaUsageResponse:
        """
        查询额度使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuotaUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuotaUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecord(
            self,
            request: models.DescribeRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordResponse:
        """
        获取私有域记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRequestData(
            self,
            request: models.DescribeRequestDataRequest,
            opts: Dict = None,
    ) -> models.DescribeRequestDataResponse:
        """
        获取私有域解析请求量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRequestData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRequestDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyForwardRule(
            self,
            request: models.ModifyForwardRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyForwardRuleResponse:
        """
        修改转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyForwardRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInboundEndpoint(
            self,
            request: models.ModifyInboundEndpointRequest,
            opts: Dict = None,
    ) -> models.ModifyInboundEndpointResponse:
        """
        删除入站终端节点
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInboundEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInboundEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateZone(
            self,
            request: models.ModifyPrivateZoneRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateZoneResponse:
        """
        修改私有域信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateZoneRecord(
            self,
            request: models.ModifyPrivateZoneRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateZoneRecordResponse:
        """
        修改私有域解析记录
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateZoneRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateZoneRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateZoneVpc(
            self,
            request: models.ModifyPrivateZoneVpcRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateZoneVpcResponse:
        """
        修改私有域关联的VPC
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateZoneVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateZoneVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordsStatus(
            self,
            request: models.ModifyRecordsStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordsStatusResponse:
        """
        修改解析记录状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAsyncBindVpcStatus(
            self,
            request: models.QueryAsyncBindVpcStatusRequest,
            opts: Dict = None,
    ) -> models.QueryAsyncBindVpcStatusResponse:
        """
        查询异步绑定vpc操作状态
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAsyncBindVpcStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAsyncBindVpcStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubscribePrivateZoneService(
            self,
            request: models.SubscribePrivateZoneServiceRequest,
            opts: Dict = None,
    ) -> models.SubscribePrivateZoneServiceResponse:
        """
        开通私有域解析
        """
        
        kwargs = {}
        kwargs["action"] = "SubscribePrivateZoneService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubscribePrivateZoneServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)