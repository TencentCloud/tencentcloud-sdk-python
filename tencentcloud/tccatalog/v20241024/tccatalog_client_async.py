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
from tencentcloud.tccatalog.v20241024 import models
from typing import Dict


class TccatalogClient(AbstractClient):
    _apiVersion = '2024-10-24'
    _endpoint = 'tccatalog.tencentcloudapi.com'
    _service = 'tccatalog'

    async def AcceptTccVpcEndPointConnect(
            self,
            request: models.AcceptTccVpcEndPointConnectRequest,
            opts: Dict = None,
    ) -> models.AcceptTccVpcEndPointConnectResponse:
        """
        接受终端节点连接
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptTccVpcEndPointConnect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptTccVpcEndPointConnectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindTccVpcEndPointServiceWhiteList(
            self,
            request: models.BindTccVpcEndPointServiceWhiteListRequest,
            opts: Dict = None,
    ) -> models.BindTccVpcEndPointServiceWhiteListResponse:
        """
        绑定终端节点服务白名单用户
        """
        
        kwargs = {}
        kwargs["action"] = "BindTccVpcEndPointServiceWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindTccVpcEndPointServiceWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTccCatalog(
            self,
            request: models.DescribeTccCatalogRequest,
            opts: Dict = None,
    ) -> models.DescribeTccCatalogResponse:
        """
        获取Tcc数据目录详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTccCatalog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTccCatalogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTccCatalogs(
            self,
            request: models.DescribeTccCatalogsRequest,
            opts: Dict = None,
    ) -> models.DescribeTccCatalogsResponse:
        """
        获取Tcc数据目录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTccCatalogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTccCatalogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)