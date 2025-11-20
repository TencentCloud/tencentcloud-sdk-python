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
from tencentcloud.tms.v20200713 import models
from typing import Dict


class TmsClient(AbstractClient):
    _apiVersion = '2020-07-13'
    _endpoint = 'tms.tencentcloudapi.com'
    _service = 'tms'

    async def AccountTipoffAccess(
            self,
            request: models.AccountTipoffAccessRequest,
            opts: Dict = None,
    ) -> models.AccountTipoffAccessResponse:
        """
        举报恶意账号
        """
        
        kwargs = {}
        kwargs["action"] = "AccountTipoffAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AccountTipoffAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTextLib(
            self,
            request: models.DescribeTextLibRequest,
            opts: Dict = None,
    ) -> models.DescribeTextLibResponse:
        """
        控制台获取用户词库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTextLib"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTextLibResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTextStat(
            self,
            request: models.DescribeTextStatRequest,
            opts: Dict = None,
    ) -> models.DescribeTextStatResponse:
        """
        控制台识别统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTextStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTextStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextModeration(
            self,
            request: models.TextModerationRequest,
            opts: Dict = None,
    ) -> models.TextModerationResponse:
        """
        文本内容检测（Text Moderation）服务使用了深度学习技术，识别可能令人反感、不安全或不适宜的文本内容，同时支持用户配置词库黑白名单，打击自定义识别类型的图片。
        """
        
        kwargs = {}
        kwargs["action"] = "TextModeration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextModerationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)