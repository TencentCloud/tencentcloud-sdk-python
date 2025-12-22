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

    async def CheckAnimateImageJob(
            self,
            request: models.CheckAnimateImageJobRequest,
            opts: Dict = None,
    ) -> models.CheckAnimateImageJobResponse:
        """
        检查图片跳舞输入图
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAnimateImageJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAnimateImageJobResponse
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
        
    async def DescribeImageAnimateJob(
            self,
            request: models.DescribeImageAnimateJobRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAnimateJobResponse:
        """
        用于查询图片跳舞任务。图片跳舞能力支持舞蹈动作结合图片生成跳舞视频，满足社交娱乐、互动营销等场景的需求。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAnimateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAnimateJobResponse
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
        
    async def DescribeVideoEditJob(
            self,
            request: models.DescribeVideoEditJobRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoEditJobResponse:
        """
        用于提交视频编辑任务，支持上传视频、文本及图片素材开展编辑操作，涵盖风格迁移、元素替换、内容增减等核心能力。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoEditJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoEditJobResponse
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
        
    async def DescribeVideoVoiceJob(
            self,
            request: models.DescribeVideoVoiceJobRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoVoiceJobResponse:
        """
        通过JobId提交请求，获取视频配音频任务的结果信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoVoiceJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoVoiceJobResponse
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
        
    async def SubmitImageAnimateJob(
            self,
            request: models.SubmitImageAnimateJobRequest,
            opts: Dict = None,
    ) -> models.SubmitImageAnimateJobResponse:
        """
        用于提交图片跳舞任务。图片跳舞能力支持舞蹈动作结合图片生成跳舞视频，满足社交娱乐、互动营销等场景的需求。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitImageAnimateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitImageAnimateJobResponse
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
        
    async def SubmitVideoEditJob(
            self,
            request: models.SubmitVideoEditJobRequest,
            opts: Dict = None,
    ) -> models.SubmitVideoEditJobResponse:
        """
        用于提交视频编辑任务，支持上传视频、文本及图片素材开展编辑操作，涵盖风格迁移、元素替换、内容增减等核心能力。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitVideoEditJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitVideoEditJobResponse
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
        
    async def SubmitVideoVoiceJob(
            self,
            request: models.SubmitVideoVoiceJobRequest,
            opts: Dict = None,
    ) -> models.SubmitVideoVoiceJobResponse:
        """
        提交视频配音效任务，输入视频后提交请求，会返回一个JobId，用于查询视频配音效的处理进度。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitVideoVoiceJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitVideoVoiceJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)