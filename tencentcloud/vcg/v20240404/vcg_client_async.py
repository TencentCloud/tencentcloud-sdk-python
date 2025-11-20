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
from tencentcloud.vcg.v20240404 import models
from typing import Dict


class VcgClient(AbstractClient):
    _apiVersion = '2024-04-04'
    _endpoint = 'vcg.tencentcloudapi.com'
    _service = 'vcg'

    async def DescribeVideoStylizationJob(
            self,
            request: models.DescribeVideoStylizationJobRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoStylizationJobResponse:
        """
        用于查询视频风格化任务。视频风格化支持将输入视频生成特定风格的视频。生成后的视频画面风格多样、流畅自然，能够满足社交娱乐、互动营销、视频素材制作等场景的需求。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoStylizationJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoStylizationJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitVideoStylizationJob(
            self,
            request: models.SubmitVideoStylizationJobRequest,
            opts: Dict = None,
    ) -> models.SubmitVideoStylizationJobResponse:
        """
        用于提交视频风格化任务。支持将输入视频生成特定风格的视频。生成后的视频画面风格多样、流畅自然，能够满足社交娱乐、互动营销、视频素材制作等场景的需求。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitVideoStylizationJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitVideoStylizationJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)