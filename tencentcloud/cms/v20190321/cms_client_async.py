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
from tencentcloud.cms.v20190321 import models
from typing import Dict


class CmsClient(AbstractClient):
    _apiVersion = '2019-03-21'
    _endpoint = 'cms.tencentcloudapi.com'
    _service = 'cms'

    async def CreateKeywordsSamples(
            self,
            request: models.CreateKeywordsSamplesRequest,
            opts: Dict = None,
    ) -> models.CreateKeywordsSamplesResponse:
        """
        创建关键词接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKeywordsSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKeywordsSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLibSamples(
            self,
            request: models.DeleteLibSamplesRequest,
            opts: Dict = None,
    ) -> models.DeleteLibSamplesResponse:
        """
        删除关键词接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLibSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLibSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKeywordsLibs(
            self,
            request: models.DescribeKeywordsLibsRequest,
            opts: Dict = None,
    ) -> models.DescribeKeywordsLibsResponse:
        """
        获取用户词库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKeywordsLibs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeywordsLibsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLibSamples(
            self,
            request: models.DescribeLibSamplesRequest,
            opts: Dict = None,
    ) -> models.DescribeLibSamplesResponse:
        """
        获取关键词接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLibSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLibSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageModeration(
            self,
            request: models.ImageModerationRequest,
            opts: Dict = None,
    ) -> models.ImageModerationResponse:
        """
        图片内容检测服务（Image Moderation, IM）能自动扫描图片，识别涉黄、涉恐、涉政、涉毒等有害内容，同时支持用户配置图片黑名单，打击自定义的违规图片。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageModeration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageModerationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextModeration(
            self,
            request: models.TextModerationRequest,
            opts: Dict = None,
    ) -> models.TextModerationResponse:
        """
        文本内容检测（Text Moderation）服务使用了深度学习技术，识别涉黄、涉政、涉恐等有害内容，同时支持用户配置词库，打击自定义的违规文本。
        """
        
        kwargs = {}
        kwargs["action"] = "TextModeration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextModerationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)