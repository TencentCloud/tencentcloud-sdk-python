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
from tencentcloud.antiddos.v20250903 import models
from typing import Dict


class AntiddosClient(AbstractClient):
    _apiVersion = '2025-09-03'
    _endpoint = 'antiddos.tencentcloudapi.com'
    _service = 'antiddos'

    async def CreateProtection(
            self,
            request: models.CreateProtectionRequest,
            opts: Dict = None,
    ) -> models.CreateProtectionResponse:
        """
        <p>创建 DDoS 高防服务防护实例。</p>
        <p>防护实例是高防服务下承载防护策略与防护资源的基本单元。创建后，您可以在实例中配置防护策略，并绑定需要防护的云资源。</p>
        <p><strong>前提条件：</strong>当前腾讯云主账号已订阅 DDoS 高防套餐，具体操作请参见 <a href="https://cloud.tencent.com/document/product/297/137989">购买指引</a>。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProtection(
            self,
            request: models.DeleteProtectionRequest,
            opts: Dict = None,
    ) -> models.DeleteProtectionResponse:
        """
        <p>删除防护实例。</p>
        <p>删除后，该实例及其绑定的防护策略将不再生效。请确保实例中没有正在使用的防护资源，或已提前将防护资源换绑至其他实例。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSBlockRecords(
            self,
            request: models.DescribeDDoSBlockRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSBlockRecordsResponse:
        """
        查询封堵解封记录和解封配额信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSBlockRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSBlockRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSProtectionPolicy(
            self,
            request: models.DescribeDDoSProtectionPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSProtectionPolicyResponse:
        """
        <p>按防护实例 ID 查询该实例下的 L3/4 DDoS 防护策略详情。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSProtectionPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSProtectionPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProtectionResources(
            self,
            request: models.DescribeProtectionResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeProtectionResourcesResponse:
        """
        <p>按防护实例 ID 查询该实例下绑定的防护资源，支持分页与按资源类型过滤。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProtectionResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProtectionResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProtections(
            self,
            request: models.DescribeProtectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeProtectionsResponse:
        """
        <p>按过滤条件查询当前账号下有权限访问的 DDoS 高防服务防护实例，支持分页返回。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProtections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProtectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceProtections(
            self,
            request: models.DescribeResourceProtectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceProtectionsResponse:
        """
        <p>按资源六段式查询云资源当前绑定的 DDoS 高防服务防护实例。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceProtections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceProtectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSProtectionPolicy(
            self,
            request: models.ModifyDDoSProtectionPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSProtectionPolicyResponse:
        """
        <p>按防护实例 ID 修改该实例下的 L3/4 DDoS 防护策略。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSProtectionPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSProtectionPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProtection(
            self,
            request: models.ModifyProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifyProtectionResponse:
        """
        修改防护实例。支持修改防护实例的名称。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProtectionResource(
            self,
            request: models.ModifyProtectionResourceRequest,
            opts: Dict = None,
    ) -> models.ModifyProtectionResourceResponse:
        """
        <p>修改防护实例的防护资源。</p>
        <p>向防护实例中添加、替换或移除防护对象（即绑定到该实例进行防护的云资源）。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProtectionResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProtectionResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnblockResources(
            self,
            request: models.UnblockResourcesRequest,
            opts: Dict = None,
    ) -> models.UnblockResourcesResponse:
        """
        申请解封资源，可通过 DescribeDDoSBlockRecords 接口获取资源的封堵解封状态。
        """
        
        kwargs = {}
        kwargs["action"] = "UnblockResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnblockResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)