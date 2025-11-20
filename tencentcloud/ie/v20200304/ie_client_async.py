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
from tencentcloud.ie.v20200304 import models
from typing import Dict


class IeClient(AbstractClient):
    _apiVersion = '2020-03-04'
    _endpoint = 'ie.tencentcloudapi.com'
    _service = 'ie'

    async def CreateEditingTask(
            self,
            request: models.CreateEditingTaskRequest,
            opts: Dict = None,
    ) -> models.CreateEditingTaskResponse:
        """
        创建编辑理解任务，可以同时选择视频标签识别、分类识别、智能拆条、智能集锦、智能封面和片头片尾识别中的一项或者多项能力。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEditingTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEditingTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMediaProcessTask(
            self,
            request: models.CreateMediaProcessTaskRequest,
            opts: Dict = None,
    ) -> models.CreateMediaProcessTaskResponse:
        """
        用于创建编辑处理任务，如媒体截取、媒体编辑、媒体拼接、媒体字幕。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMediaProcessTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMediaProcessTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMediaQualityRestorationTask(
            self,
            request: models.CreateMediaQualityRestorationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateMediaQualityRestorationTaskResponse:
        """
        创建画质重生任务，对视频进行转码、去噪、去划痕、去毛刺、超分、细节增强和色彩增强。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMediaQualityRestorationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMediaQualityRestorationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateQualityControlTask(
            self,
            request: models.CreateQualityControlTaskRequest,
            opts: Dict = None,
    ) -> models.CreateQualityControlTaskResponse:
        """
        通过接口可以智能检测视频画面中抖动重影、模糊、低光照、过曝光、黑边、白边、黑屏、白屏、花屏、噪点、马赛克、二维码等在内的多个场景，还可以自动检测视频无音频异常、无声音片段。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateQualityControlTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateQualityControlTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEditingTaskResult(
            self,
            request: models.DescribeEditingTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeEditingTaskResultResponse:
        """
        获取编辑理解任务结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEditingTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEditingTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMediaProcessTaskResult(
            self,
            request: models.DescribeMediaProcessTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeMediaProcessTaskResultResponse:
        """
        用于获取编辑处理任务的结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMediaProcessTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMediaProcessTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMediaQualityRestorationTaskRusult(
            self,
            request: models.DescribeMediaQualityRestorationTaskRusultRequest,
            opts: Dict = None,
    ) -> models.DescribeMediaQualityRestorationTaskRusultResponse:
        """
        获取画质重生任务结果，查看结束后的文件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMediaQualityRestorationTaskRusult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMediaQualityRestorationTaskRusultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityControlTaskResult(
            self,
            request: models.DescribeQualityControlTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityControlTaskResultResponse:
        """
        获取媒体质检任务结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityControlTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityControlTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopMediaProcessTask(
            self,
            request: models.StopMediaProcessTaskRequest,
            opts: Dict = None,
    ) -> models.StopMediaProcessTaskResponse:
        """
        用于停止正在进行中的编辑处理任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StopMediaProcessTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopMediaProcessTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopMediaQualityRestorationTask(
            self,
            request: models.StopMediaQualityRestorationTaskRequest,
            opts: Dict = None,
    ) -> models.StopMediaQualityRestorationTaskResponse:
        """
        删除正在进行的画质重生任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopMediaQualityRestorationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopMediaQualityRestorationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)