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
from tencentcloud.bda.v20200324 import models
from typing import Dict


class BdaClient(AbstractClient):
    _apiVersion = '2020-03-24'
    _endpoint = 'bda.tencentcloudapi.com'
    _service = 'bda'

    async def CreateSegmentationTask(
            self,
            request: models.CreateSegmentationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSegmentationTaskResponse:
        """
        本接口为人像分割在线处理接口组中的提交任务接口，可以对提交的资源进行处理视频流/图片流识别视频作品中的人像区域，进行一键抠像、背景替换、人像虚化等后期处理。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSegmentationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSegmentationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSegmentationTask(
            self,
            request: models.DescribeSegmentationTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeSegmentationTaskResponse:
        """
        可以查看单条任务的处理情况，包括处理状态，处理结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSegmentationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSegmentationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SegmentCustomizedPortraitPic(
            self,
            request: models.SegmentCustomizedPortraitPicRequest,
            opts: Dict = None,
    ) -> models.SegmentCustomizedPortraitPicResponse:
        """
        在前后景分割的基础上优化多分类分割，支持对头发、五官等的分割，既作为换发型、挂件等底层技术，也可用于抠人头、抠人脸等玩法
        """
        
        kwargs = {}
        kwargs["action"] = "SegmentCustomizedPortraitPic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SegmentCustomizedPortraitPicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SegmentPortraitPic(
            self,
            request: models.SegmentPortraitPicRequest,
            opts: Dict = None,
    ) -> models.SegmentPortraitPicResponse:
        """
        即二分类人像分割，识别传入图片中人体的完整轮廓，进行抠像。
        """
        
        kwargs = {}
        kwargs["action"] = "SegmentPortraitPic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SegmentPortraitPicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateSegmentationTask(
            self,
            request: models.TerminateSegmentationTaskRequest,
            opts: Dict = None,
    ) -> models.TerminateSegmentationTaskResponse:
        """
        终止指定视频人像分割处理任务
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateSegmentationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateSegmentationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)