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
from tencentcloud.irp.v20220324 import models
from typing import Dict


class IrpClient(AbstractClient):
    _apiVersion = '2022-03-24'
    _endpoint = 'irp.tencentcloudapi.com'
    _service = 'irp'

    async def RecommendContent(
            self,
            request: models.RecommendContentRequest,
            opts: Dict = None,
    ) -> models.RecommendContentResponse:
        """
        获取推荐结果
        """
        
        kwargs = {}
        kwargs["action"] = "RecommendContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecommendContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportAction(
            self,
            request: models.ReportActionRequest,
            opts: Dict = None,
    ) -> models.ReportActionResponse:
        """
        上报行为
        """
        
        kwargs = {}
        kwargs["action"] = "ReportAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportMaterial(
            self,
            request: models.ReportMaterialRequest,
            opts: Dict = None,
    ) -> models.ReportMaterialResponse:
        """
        上报物料
        """
        
        kwargs = {}
        kwargs["action"] = "ReportMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportPortrait(
            self,
            request: models.ReportPortraitRequest,
            opts: Dict = None,
    ) -> models.ReportPortraitResponse:
        """
        上报用户画像
        """
        
        kwargs = {}
        kwargs["action"] = "ReportPortrait"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportPortraitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)