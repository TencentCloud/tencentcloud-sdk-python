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
from tencentcloud.hasim.v20210716 import models
from typing import Dict


class HasimClient(AbstractClient):
    _apiVersion = '2021-07-16'
    _endpoint = 'hasim.tencentcloudapi.com'
    _service = 'hasim'

    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        创建自动化规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTactic(
            self,
            request: models.CreateTacticRequest,
            opts: Dict = None,
    ) -> models.CreateTacticResponse:
        """
        创建云兔切换策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTactic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTacticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTag(
            self,
            request: models.CreateTagRequest,
            opts: Dict = None,
    ) -> models.CreateTagResponse:
        """
        创建标签
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRule(
            self,
            request: models.DeleteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleResponse:
        """
        删除自动化规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTactic(
            self,
            request: models.DeleteTacticRequest,
            opts: Dict = None,
    ) -> models.DeleteTacticResponse:
        """
        删除策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTactic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTacticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTag(
            self,
            request: models.DeleteTagRequest,
            opts: Dict = None,
    ) -> models.DeleteTagResponse:
        """
        删除标签
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLink(
            self,
            request: models.DescribeLinkRequest,
            opts: Dict = None,
    ) -> models.DescribeLinkResponse:
        """
        查询云兔连接详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLink"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLinkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLinks(
            self,
            request: models.DescribeLinksRequest,
            opts: Dict = None,
    ) -> models.DescribeLinksResponse:
        """
        查询云兔连接列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLinks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLinksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrders(
            self,
            request: models.DescribeOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeOrdersResponse:
        """
        查询订单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRule(
            self,
            request: models.DescribeRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleResponse:
        """
        查询自动化规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRules(
            self,
            request: models.DescribeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesResponse:
        """
        查询自动化规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTactic(
            self,
            request: models.DescribeTacticRequest,
            opts: Dict = None,
    ) -> models.DescribeTacticResponse:
        """
        查询云兔切换策略信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTactic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTacticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTactics(
            self,
            request: models.DescribeTacticsRequest,
            opts: Dict = None,
    ) -> models.DescribeTacticsResponse:
        """
        查询云兔切换策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTactics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTacticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTags(
            self,
            request: models.DescribeTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsResponse:
        """
        查询标签列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLinkAdvancedLog(
            self,
            request: models.ModifyLinkAdvancedLogRequest,
            opts: Dict = None,
    ) -> models.ModifyLinkAdvancedLogResponse:
        """
        编辑云兔高级日志状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLinkAdvancedLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLinkAdvancedLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLinkTactic(
            self,
            request: models.ModifyLinkTacticRequest,
            opts: Dict = None,
    ) -> models.ModifyLinkTacticResponse:
        """
        编辑云兔策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLinkTactic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLinkTacticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLinkTele(
            self,
            request: models.ModifyLinkTeleRequest,
            opts: Dict = None,
    ) -> models.ModifyLinkTeleResponse:
        """
        修改云兔运营商
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLinkTele"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLinkTeleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRule(
            self,
            request: models.ModifyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleResponse:
        """
        编辑自动化规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRuleStatus(
            self,
            request: models.ModifyRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleStatusResponse:
        """
        编辑自动化规则状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTactic(
            self,
            request: models.ModifyTacticRequest,
            opts: Dict = None,
    ) -> models.ModifyTacticResponse:
        """
        修改云兔切换策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTactic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTacticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTag(
            self,
            request: models.ModifyTagRequest,
            opts: Dict = None,
    ) -> models.ModifyTagResponse:
        """
        编辑标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewLinkInfo(
            self,
            request: models.RenewLinkInfoRequest,
            opts: Dict = None,
    ) -> models.RenewLinkInfoResponse:
        """
        刷新云兔连接信息同步
        """
        
        kwargs = {}
        kwargs["action"] = "RenewLinkInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewLinkInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)