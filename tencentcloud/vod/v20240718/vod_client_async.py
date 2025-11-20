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
from tencentcloud.vod.v20240718 import models
from typing import Dict


class VodClient(AbstractClient):
    _apiVersion = '2024-07-18'
    _endpoint = 'vod.tencentcloudapi.com'
    _service = 'vod'

    async def CreateIncrementalMigrationStrategy(
            self,
            request: models.CreateIncrementalMigrationStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateIncrementalMigrationStrategyResponse:
        """
        创建增量迁移策略。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIncrementalMigrationStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIncrementalMigrationStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStorage(
            self,
            request: models.CreateStorageRequest,
            opts: Dict = None,
    ) -> models.CreateStorageResponse:
        """
        该接口用于为专业版应用创建存储桶。

        注：
        - 本接口仅用于专业版应用；
        - 客户创建点播专业版应用时，系统默认为客户开通了部分地域的存储，用户如果需要开通其它地域的存储，可以通过该接口进行开通；
        - 通过 [DescribeStorageRegions](https://cloud.tencent.com/document/product/266/72480) 接口可以查询到所有存储地域及已经开通存储桶的地域。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStorageCredentials(
            self,
            request: models.CreateStorageCredentialsRequest,
            opts: Dict = None,
    ) -> models.CreateStorageCredentialsResponse:
        """
        用于按指定策略，生成专业版应用的临时访问凭证，比如生成用于客户端上传的临时凭证。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStorageCredentials"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStorageCredentialsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIncrementalMigrationStrategy(
            self,
            request: models.DeleteIncrementalMigrationStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteIncrementalMigrationStrategyResponse:
        """
        删除增量迁移策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIncrementalMigrationStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIncrementalMigrationStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIncrementalMigrationStrategyInfos(
            self,
            request: models.DescribeIncrementalMigrationStrategyInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeIncrementalMigrationStrategyInfosResponse:
        """
        查询增量迁移策略信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIncrementalMigrationStrategyInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIncrementalMigrationStrategyInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStorage(
            self,
            request: models.DescribeStorageRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageResponse:
        """
        该接口用于查询专业版应用中的存储桶信息，同时支持分页查询。

        注：
        - 本接口仅用于专业版应用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIncrementalMigrationStrategy(
            self,
            request: models.ModifyIncrementalMigrationStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyIncrementalMigrationStrategyResponse:
        """
        创建增量迁移策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIncrementalMigrationStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIncrementalMigrationStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)