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
from tencentcloud.partners.v20180321 import models
from typing import Dict


class PartnersClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'partners.tencentcloudapi.com'
    _service = 'partners'

    async def AgentPayDeals(
            self,
            request: models.AgentPayDealsRequest,
            opts: Dict = None,
    ) -> models.AgentPayDealsResponse:
        """
        代理商支付订单接口，支持自付/代付
        """
        
        kwargs = {}
        kwargs["action"] = "AgentPayDeals"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AgentPayDealsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AgentTransferMoney(
            self,
            request: models.AgentTransferMoneyRequest,
            opts: Dict = None,
    ) -> models.AgentTransferMoneyResponse:
        """
        为合作伙伴提供转账给客户能力。仅支持合作伙伴为自己名下客户转账。
        """
        
        kwargs = {}
        kwargs["action"] = "AgentTransferMoney"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AgentTransferMoneyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignClientsToSales(
            self,
            request: models.AssignClientsToSalesRequest,
            opts: Dict = None,
    ) -> models.AssignClientsToSalesResponse:
        """
        为代客or申请中代客分派跟进人（业务员），入参可从以下API获取
        - 代客列表获取API： [DescribeAgentAuditedClients](https://cloud.tencent.com/document/product/563/19184)
        - 申请中代客列表获取API：[DescribeAgentClients](https://cloud.tencent.com/document/product/563/16046)
        - 业务员列表获取API：[DescribeSalesmans](https://cloud.tencent.com/document/product/563/35196) <br><br>
        """
        
        kwargs = {}
        kwargs["action"] = "AssignClientsToSales"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignClientsToSalesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AuditApplyClient(
            self,
            request: models.AuditApplyClientRequest,
            opts: Dict = None,
    ) -> models.AuditApplyClientResponse:
        """
        代理商可以审核其名下申请中代客
        """
        
        kwargs = {}
        kwargs["action"] = "AuditApplyClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AuditApplyClientResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePayRelationForClient(
            self,
            request: models.CreatePayRelationForClientRequest,
            opts: Dict = None,
    ) -> models.CreatePayRelationForClientResponse:
        """
        合作伙伴为客户创建强代付关系
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePayRelationForClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePayRelationForClientResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentAuditedClients(
            self,
            request: models.DescribeAgentAuditedClientsRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentAuditedClientsResponse:
        """
        查询已审核客户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentAuditedClients"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentAuditedClientsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentBills(
            self,
            request: models.DescribeAgentBillsRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentBillsResponse:
        """
        代理商可查询自己及名下代客所有业务明细
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentBills"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentBillsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentClientGrade(
            self,
            request: models.DescribeAgentClientGradeRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentClientGradeResponse:
        """
        传入代客uin，查客户级别，客户审核状态，客户实名认证状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentClientGrade"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentClientGradeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentClients(
            self,
            request: models.DescribeAgentClientsRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentClientsResponse:
        """
        代理商可查询自己名下待审核客户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentClients"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentClientsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentDealsByCache(
            self,
            request: models.DescribeAgentDealsByCacheRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentDealsByCacheResponse:
        """
        供代理商拉取全量预付费普通客户订单
        （对应控制台：客户订单-预付费-普通订单）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentDealsByCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentDealsByCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentDealsPriceDetailByDealName(
            self,
            request: models.DescribeAgentDealsPriceDetailByDealNameRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentDealsPriceDetailByDealNameResponse:
        """
        供代理商使用名下有效普通代客的预付费子订单号查询订单费用详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentDealsPriceDetailByDealName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentDealsPriceDetailByDealNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentPayDealsV2(
            self,
            request: models.DescribeAgentPayDealsV2Request,
            opts: Dict = None,
    ) -> models.DescribeAgentPayDealsV2Response:
        """
        查询最近15天内的代理商代付订单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentPayDealsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentPayDealsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentRelateBigDealIds(
            self,
            request: models.DescribeAgentRelateBigDealIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentRelateBigDealIdsResponse:
        """
        根据大订单号查询关联申请合并支付的其他订单号
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentRelateBigDealIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentRelateBigDealIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentSelfPayDealsV2(
            self,
            request: models.DescribeAgentSelfPayDealsV2Request,
            opts: Dict = None,
    ) -> models.DescribeAgentSelfPayDealsV2Response:
        """
        查询代理商名下指定代客最近15天内的自付订单（预付费）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentSelfPayDealsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentSelfPayDealsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientBalanceNew(
            self,
            request: models.DescribeClientBalanceNewRequest,
            opts: Dict = None,
    ) -> models.DescribeClientBalanceNewResponse:
        """
        为合作伙伴提供查询客户余额能力。调用者必须是合作伙伴，只能查询自己名下客户余额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientBalanceNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientBalanceNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientJoinIncreaseList(
            self,
            request: models.DescribeClientJoinIncreaseListRequest,
            opts: Dict = None,
    ) -> models.DescribeClientJoinIncreaseListResponse:
        """
        查询合作伙伴名下客户的参与增量激励考核信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientJoinIncreaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientJoinIncreaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientSwitchTraTaskInfo(
            self,
            request: models.DescribeClientSwitchTraTaskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeClientSwitchTraTaskInfoResponse:
        """
        查询客户的交易类型切换任务的信息，查询成功则获取当前用户的切换链接，查询失败则返回失败的原因
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientSwitchTraTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientSwitchTraTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRebateInfos(
            self,
            request: models.DescribeRebateInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeRebateInfosResponse:
        """
        【该接口已下线，请切换使用升级版本DescribeRebateInfosNew】代理商可查询自己名下全部返佣信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRebateInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRebateInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRebateInfosNew(
            self,
            request: models.DescribeRebateInfosNewRequest,
            opts: Dict = None,
    ) -> models.DescribeRebateInfosNewResponse:
        """
        代理商可查询自己名下全部返佣信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRebateInfosNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRebateInfosNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSalesmans(
            self,
            request: models.DescribeSalesmansRequest,
            opts: Dict = None,
    ) -> models.DescribeSalesmansResponse:
        """
        代理商查询名下业务员列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSalesmans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSalesmansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnbindClientList(
            self,
            request: models.DescribeUnbindClientListRequest,
            opts: Dict = None,
    ) -> models.DescribeUnbindClientListResponse:
        """
        代理商名下客户解绑记录查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnbindClientList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnbindClientListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClientRemark(
            self,
            request: models.ModifyClientRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyClientRemarkResponse:
        """
        代理商可以对名下客户添加备注、修改备注
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClientRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClientRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemovePayRelationForClient(
            self,
            request: models.RemovePayRelationForClientRequest,
            opts: Dict = None,
    ) -> models.RemovePayRelationForClientResponse:
        """
        合作伙伴为客户消除强代付关系
        """
        
        kwargs = {}
        kwargs["action"] = "RemovePayRelationForClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemovePayRelationForClientResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)