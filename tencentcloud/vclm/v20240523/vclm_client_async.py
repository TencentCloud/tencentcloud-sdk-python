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
from tencentcloud.vclm.v20240523 import models
from typing import Dict


class VclmClient(AbstractClient):
    _apiVersion = '2024-05-23'
    _endpoint = 'vclm.tencentcloudapi.com'
    _service = 'vclm'

    async def CreateAigcElement(
            self,
            request: models.CreateAigcElementRequest,
            opts: Dict = None,
    ) -> models.CreateAigcElementResponse:
        """
        提交视频特效任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcElement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcElementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAigcElement(
            self,
            request: models.DeleteAigcElementRequest,
            opts: Dict = None,
    ) -> models.DeleteAigcElementResponse:
        """
        删除主体库
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAigcElement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAigcElementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAigcElement(
            self,
            request: models.DescribeAigcElementRequest,
            opts: Dict = None,
    ) -> models.DescribeAigcElementResponse:
        """
        提交视频特效任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAigcElement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAigcElementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHumanActorJob(
            self,
            request: models.DescribeHumanActorJobRequest,
            opts: Dict = None,
    ) -> models.DescribeHumanActorJobResponse:
        """
        通过JobId提交请求，获取人像驱动任务的结果信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHumanActorJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHumanActorJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHunyuanToVideoJob(
            self,
            request: models.DescribeHunyuanToVideoJobRequest,
            opts: Dict = None,
    ) -> models.DescribeHunyuanToVideoJobResponse:
        """
        查询混元生视频任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHunyuanToVideoJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHunyuanToVideoJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageToVideoGeneralJob(
            self,
            request: models.DescribeImageToVideoGeneralJobRequest,
            opts: Dict = None,
    ) -> models.DescribeImageToVideoGeneralJobResponse:
        """
        查询图生视频通用能力任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageToVideoGeneralJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageToVideoGeneralJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageToVideoJob(
            self,
            request: models.DescribeImageToVideoJobRequest,
            opts: Dict = None,
    ) -> models.DescribeImageToVideoJobResponse:
        """
        用于查询视频特效任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageToVideoJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageToVideoJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageToVideoViduJob(
            self,
            request: models.DescribeImageToVideoViduJobRequest,
            opts: Dict = None,
    ) -> models.DescribeImageToVideoViduJobResponse:
        """
        查询Vidu图生视频任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageToVideoViduJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageToVideoViduJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMotionControlKlingJob(
            self,
            request: models.DescribeMotionControlKlingJobRequest,
            opts: Dict = None,
    ) -> models.DescribeMotionControlKlingJobResponse:
        """
        查询Kling动作控制任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMotionControlKlingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMotionControlKlingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePortraitSingJob(
            self,
            request: models.DescribePortraitSingJobRequest,
            opts: Dict = None,
    ) -> models.DescribePortraitSingJobResponse:
        """
        用于查询图片唱演任务。
        支持提交音频和图片生成唱演视频，满足社交娱乐、互动营销等场景的需求。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePortraitSingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePortraitSingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReferenceToVideoViduJob(
            self,
            request: models.DescribeReferenceToVideoViduJobRequest,
            opts: Dict = None,
    ) -> models.DescribeReferenceToVideoViduJobResponse:
        """
        查询Vidu参考生视频任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReferenceToVideoViduJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReferenceToVideoViduJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplateToVideoJob(
            self,
            request: models.DescribeTemplateToVideoJobRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateToVideoJobResponse:
        """
        用于查询视频特效任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplateToVideoJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateToVideoJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTextToVideoJob(
            self,
            request: models.DescribeTextToVideoJobRequest,
            opts: Dict = None,
    ) -> models.DescribeTextToVideoJobResponse:
        """
        用于查询文生视频任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTextToVideoJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTextToVideoJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTextToVideoViduJob(
            self,
            request: models.DescribeTextToVideoViduJobRequest,
            opts: Dict = None,
    ) -> models.DescribeTextToVideoViduJobResponse:
        """
        查询Vidu文生视频任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTextToVideoViduJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTextToVideoViduJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoEditKlingJob(
            self,
            request: models.DescribeVideoEditKlingJobRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoEditKlingJobResponse:
        """
        查询Kling多模态编辑任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoEditKlingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoEditKlingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoExtendKlingJob(
            self,
            request: models.DescribeVideoExtendKlingJobRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoExtendKlingJobResponse:
        """
        查询视频延长任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoExtendKlingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoExtendKlingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoFaceFusionJob(
            self,
            request: models.DescribeVideoFaceFusionJobRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoFaceFusionJobResponse:
        """
        查询视频人脸融合任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoFaceFusionJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoFaceFusionJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitHumanActorJob(
            self,
            request: models.SubmitHumanActorJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHumanActorJobResponse:
        """
        用于提交人像驱动任务
        支持提交音频和图文来生成对应视频，满足动态交互、内容生产等场景需求。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHumanActorJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHumanActorJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitHunyuanToVideoJob(
            self,
            request: models.SubmitHunyuanToVideoJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHunyuanToVideoJobResponse:
        """
        ●混元生视频接口，基于混元大模型，根据输入的文本或图片智能生成视频。

        ●默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHunyuanToVideoJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHunyuanToVideoJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitImageToVideoGeneralJob(
            self,
            request: models.SubmitImageToVideoGeneralJobRequest,
            opts: Dict = None,
    ) -> models.SubmitImageToVideoGeneralJobResponse:
        """
        图生视频通用能力接口
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitImageToVideoGeneralJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitImageToVideoGeneralJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitImageToVideoJob(
            self,
            request: models.SubmitImageToVideoJobRequest,
            opts: Dict = None,
    ) -> models.SubmitImageToVideoJobResponse:
        """
        提交视频特效任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitImageToVideoJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitImageToVideoJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitImageToVideoViduJob(
            self,
            request: models.SubmitImageToVideoViduJobRequest,
            opts: Dict = None,
    ) -> models.SubmitImageToVideoViduJobResponse:
        """
        提交Vidu图生视频任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitImageToVideoViduJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitImageToVideoViduJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitMotionControlKlingJob(
            self,
            request: models.SubmitMotionControlKlingJobRequest,
            opts: Dict = None,
    ) -> models.SubmitMotionControlKlingJobResponse:
        """
        提交动作控制(Kling)任务并发
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitMotionControlKlingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitMotionControlKlingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitPortraitSingJob(
            self,
            request: models.SubmitPortraitSingJobRequest,
            opts: Dict = None,
    ) -> models.SubmitPortraitSingJobResponse:
        """
        用于提交图片唱演任务。
        支持提交音频和图片生成唱演视频，满足社交娱乐、互动营销等场景的需求。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitPortraitSingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitPortraitSingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitReferenceToVideoViduJob(
            self,
            request: models.SubmitReferenceToVideoViduJobRequest,
            opts: Dict = None,
    ) -> models.SubmitReferenceToVideoViduJobResponse:
        """
        提交Vidu参考生视频任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitReferenceToVideoViduJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitReferenceToVideoViduJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTemplateToVideoJob(
            self,
            request: models.SubmitTemplateToVideoJobRequest,
            opts: Dict = None,
    ) -> models.SubmitTemplateToVideoJobResponse:
        """
        提交视频特效任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTemplateToVideoJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTemplateToVideoJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTextToVideoJob(
            self,
            request: models.SubmitTextToVideoJobRequest,
            opts: Dict = None,
    ) -> models.SubmitTextToVideoJobResponse:
        """
        通过提交对视频内容的描述文本生成一个短视频。文生视频为异步处理任务，成功提交任务后返回任务的JobId。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTextToVideoJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTextToVideoJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTextToVideoViduJob(
            self,
            request: models.SubmitTextToVideoViduJobRequest,
            opts: Dict = None,
    ) -> models.SubmitTextToVideoViduJobResponse:
        """
        提交Vidu文生视频任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTextToVideoViduJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTextToVideoViduJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitVideoEditKlingJob(
            self,
            request: models.SubmitVideoEditKlingJobRequest,
            opts: Dict = None,
    ) -> models.SubmitVideoEditKlingJobResponse:
        """
        提交Kling多模态编辑任务
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitVideoEditKlingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitVideoEditKlingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitVideoExtendKlingJob(
            self,
            request: models.SubmitVideoExtendKlingJobRequest,
            opts: Dict = None,
    ) -> models.SubmitVideoExtendKlingJobResponse:
        """
        用于提交视频延长任务接口。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitVideoExtendKlingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitVideoExtendKlingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitVideoFaceFusionJob(
            self,
            request: models.SubmitVideoFaceFusionJobRequest,
            opts: Dict = None,
    ) -> models.SubmitVideoFaceFusionJobResponse:
        """
        提交视频人脸融合任务
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitVideoFaceFusionJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitVideoFaceFusionJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)