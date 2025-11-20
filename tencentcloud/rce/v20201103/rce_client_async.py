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
from tencentcloud.rce.v20201103 import models
from typing import Dict


class RceClient(AbstractClient):
    _apiVersion = '2020-11-03'
    _endpoint = 'rce.tencentcloudapi.com'
    _service = 'rce'

    async def CreateNameList(
            self,
            request: models.CreateNameListRequest,
            opts: Dict = None,
    ) -> models.CreateNameListResponse:
        """
        创建黑白名单，黑白名单数量上限为100
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNameList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNameListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNameList(
            self,
            request: models.DeleteNameListRequest,
            opts: Dict = None,
    ) -> models.DeleteNameListResponse:
        """
        修改黑白名单状态 关闭 开启 删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNameList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNameListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNameListData(
            self,
            request: models.DeleteNameListDataRequest,
            opts: Dict = None,
    ) -> models.DeleteNameListDataResponse:
        """
        删除黑白名单数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNameListData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNameListDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNameList(
            self,
            request: models.DescribeNameListRequest,
            opts: Dict = None,
    ) -> models.DescribeNameListResponse:
        """
        列表展示黑白名单列表数据, 包含列表名称, 名单类型, 数据类型, 数据来源, 描述, 状态等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNameList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNameListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNameListDataList(
            self,
            request: models.DescribeNameListDataListRequest,
            opts: Dict = None,
    ) -> models.DescribeNameListDataListResponse:
        """
        黑白名单详情数据展示 名单id 客户appid uin 数据内容 开始时间和结束时间 状态 描述
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNameListDataList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNameListDataListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNameListDetail(
            self,
            request: models.DescribeNameListDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeNameListDetailResponse:
        """
        查询黑白名单列表详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNameListDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNameListDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserUsageCnt(
            self,
            request: models.DescribeUserUsageCntRequest,
            opts: Dict = None,
    ) -> models.DescribeUserUsageCntResponse:
        """
        RCE控制台预付费和后付费次数展示
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserUsageCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserUsageCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportNameListData(
            self,
            request: models.ImportNameListDataRequest,
            opts: Dict = None,
    ) -> models.ImportNameListDataResponse:
        """
        新增黑白名单数据，所有黑白名单数据总量上限为10000
        """
        
        kwargs = {}
        kwargs["action"] = "ImportNameListData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportNameListDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageMarketingRisk(
            self,
            request: models.ManageMarketingRiskRequest,
            opts: Dict = None,
    ) -> models.ManageMarketingRiskResponse:
        """
        通用业务欺诈保护是基于人工智能技术和腾讯20年风控实战沉淀，依托腾讯海量业务构建的风控引擎，以轻量级的 SaaS 服务方式接入，帮助您快速解决注册、登录、营销活动等关键场景遇到的欺诈问题，实时防御黑灰产作恶。
        """
        
        kwargs = {}
        kwargs["action"] = "ManageMarketingRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageMarketingRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNameList(
            self,
            request: models.ModifyNameListRequest,
            opts: Dict = None,
    ) -> models.ModifyNameListResponse:
        """
        修改列表数据 列表名称 列表类型 数据类型 状态 备注
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNameList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNameListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNameListData(
            self,
            request: models.ModifyNameListDataRequest,
            opts: Dict = None,
    ) -> models.ModifyNameListDataResponse:
        """
        修改黑白名单列表详情 详情内容 开始和结束时间 状态 备注等
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNameListData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNameListDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)