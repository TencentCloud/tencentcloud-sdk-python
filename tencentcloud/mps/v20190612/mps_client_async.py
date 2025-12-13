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
from tencentcloud.mps.v20190612 import models
from typing import Dict


class MpsClient(AbstractClient):
    _apiVersion = '2019-06-12'
    _endpoint = 'mps.tencentcloudapi.com'
    _service = 'mps'

    async def BatchDeleteStreamLinkFlow(
            self,
            request: models.BatchDeleteStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteStreamLinkFlowResponse:
        """
        批量删除媒体传输流。
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchProcessMedia(
            self,
            request: models.BatchProcessMediaRequest,
            opts: Dict = None,
    ) -> models.BatchProcessMediaResponse:
        """
        对 URL视频链接批量发起处理任务，功能包括：
        智能字幕（语音全文、语音热词、语音翻译）
        """
        
        kwargs = {}
        kwargs["action"] = "BatchProcessMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchProcessMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchStartStreamLinkFlow(
            self,
            request: models.BatchStartStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.BatchStartStreamLinkFlowResponse:
        """
        批量启动媒体传输流。
        """
        
        kwargs = {}
        kwargs["action"] = "BatchStartStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchStartStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchStopStreamLinkFlow(
            self,
            request: models.BatchStopStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.BatchStopStreamLinkFlowResponse:
        """
        批量停止媒体传输流。
        """
        
        kwargs = {}
        kwargs["action"] = "BatchStopStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchStopStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIAnalysisTemplate(
            self,
            request: models.CreateAIAnalysisTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAIAnalysisTemplateResponse:
        """
        创建用户自定义内容分析模板，数量上限：50。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIAnalysisTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIAnalysisTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIRecognitionTemplate(
            self,
            request: models.CreateAIRecognitionTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAIRecognitionTemplateResponse:
        """
        创建用户自定义内容识别模板，数量上限：50。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIRecognitionTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIRecognitionTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAdaptiveDynamicStreamingTemplate(
            self,
            request: models.CreateAdaptiveDynamicStreamingTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAdaptiveDynamicStreamingTemplateResponse:
        """
        创建转自适应码流模板，数量上限：100。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAdaptiveDynamicStreamingTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAdaptiveDynamicStreamingTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAnimatedGraphicsTemplate(
            self,
            request: models.CreateAnimatedGraphicsTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAnimatedGraphicsTemplateResponse:
        """
        创建用户自定义转动图模板，数量上限：16。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAnimatedGraphicsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAnimatedGraphicsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAsrHotwords(
            self,
            request: models.CreateAsrHotwordsRequest,
            opts: Dict = None,
    ) -> models.CreateAsrHotwordsResponse:
        """
        智能字幕新建热词库接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAsrHotwords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAsrHotwordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBlindWatermarkTemplate(
            self,
            request: models.CreateBlindWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateBlindWatermarkTemplateResponse:
        """
        创建用户自定义数字水印模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBlindWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBlindWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateContentReviewTemplate(
            self,
            request: models.CreateContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateContentReviewTemplateResponse:
        """
        创建用户自定义内容审核模板，数量上限：50。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateContentReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageSpriteTemplate(
            self,
            request: models.CreateImageSpriteTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateImageSpriteTemplateResponse:
        """
        创建用户自定义雪碧图模板，数量上限：16。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageSpriteTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageSpriteTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveRecordTemplate(
            self,
            request: models.CreateLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveRecordTemplateResponse:
        """
        创建直播录制模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMediaEvaluation(
            self,
            request: models.CreateMediaEvaluationRequest,
            opts: Dict = None,
    ) -> models.CreateMediaEvaluationResponse:
        """
        发起视频评测任务，功能包括：

        1. 对一个原视频和多个转码后的视频进行评分。
        2. 计算不同转码方式的 BD-Rate。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMediaEvaluation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMediaEvaluationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePersonSample(
            self,
            request: models.CreatePersonSampleRequest,
            opts: Dict = None,
    ) -> models.CreatePersonSampleResponse:
        """
        该接口用于创建素材样本，用于通过五官定位等技术，进行内容识别、内容不适宜等视频处理。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProcessImageTemplate(
            self,
            request: models.CreateProcessImageTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateProcessImageTemplateResponse:
        """
        创建图片处理模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProcessImageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProcessImageTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateQualityControlTemplate(
            self,
            request: models.CreateQualityControlTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateQualityControlTemplateResponse:
        """
        创建媒体质检模板，数量上限：50。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateQualityControlTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateQualityControlTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSampleSnapshotTemplate(
            self,
            request: models.CreateSampleSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSampleSnapshotTemplateResponse:
        """
        创建用户自定义采样截图模板，数量上限：16。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSampleSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSampleSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSchedule(
            self,
            request: models.CreateScheduleRequest,
            opts: Dict = None,
    ) -> models.CreateScheduleResponse:
        """
        对 COS 中指定 Bucket 的目录下上传的媒体文件，设置处理规则，包括：
        1. 视频转码（带水印）；
        2. 视频转动图；
        3. 对视频按指定时间点截图；
        4. 对视频采样截图；
        5. 对视频截图雪碧图；
        6. 对视频转自适应码流；
        7. 智能内容审核（鉴黄、敏感信息检测）；
        8. 智能内容分析（标签、分类、封面、按帧标签）；
        9. 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词）。
        10. 媒体质检（直播流格式诊断、音画内容检测（抖动、模糊、低光照、过曝光、黑边、白边、黑屏、白屏、花屏、噪点、马赛克、二维码等）、无参考打分）
        11. 智能字幕（语音全文、语音热词、语音翻译）
        12. 智能擦除（去水印、去字幕、隐私保护）；

        注意：创建编排成功后是禁用状态，需要手动启用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSmartEraseTemplate(
            self,
            request: models.CreateSmartEraseTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSmartEraseTemplateResponse:
        """
        创建自定义智能擦除模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSmartEraseTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSmartEraseTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSmartSubtitleTemplate(
            self,
            request: models.CreateSmartSubtitleTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSmartSubtitleTemplateResponse:
        """
        创建自定义智能字幕模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSmartSubtitleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSmartSubtitleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshotByTimeOffsetTemplate(
            self,
            request: models.CreateSnapshotByTimeOffsetTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotByTimeOffsetTemplateResponse:
        """
        创建用户自定义指定时间点截图模板，数量上限：16。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshotByTimeOffsetTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotByTimeOffsetTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLinkEvent(
            self,
            request: models.CreateStreamLinkEventRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLinkEventResponse:
        """
        创建媒体传输的事件Event。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLinkEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLinkEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLinkFlow(
            self,
            request: models.CreateStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLinkFlowResponse:
        """
        创建媒体传输的传输流配置。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLinkInput(
            self,
            request: models.CreateStreamLinkInputRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLinkInputResponse:
        """
        创建媒体传输的输入配置。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLinkInput"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLinkInputResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLinkOutputInfo(
            self,
            request: models.CreateStreamLinkOutputInfoRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLinkOutputInfoResponse:
        """
        创建媒体传输流的输出信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLinkOutputInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLinkOutputInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLinkSecurityGroup(
            self,
            request: models.CreateStreamLinkSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLinkSecurityGroupResponse:
        """
        创建安全组，数量限制5个。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLinkSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLinkSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTranscodeTemplate(
            self,
            request: models.CreateTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateTranscodeTemplateResponse:
        """
        创建用户自定义转码模板，数量上限：1000
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoDatabaseEntryTask(
            self,
            request: models.CreateVideoDatabaseEntryTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVideoDatabaseEntryTaskResponse:
        """
        对URL链接或COS中的视频发起入库任务。
        可选在任务完成后向回调方发送任务完成状态信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoDatabaseEntryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoDatabaseEntryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoSearchTask(
            self,
            request: models.CreateVideoSearchTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVideoSearchTaskResponse:
        """
        使用检索值检索库中最接近检索值的若干视频。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoSearchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoSearchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWatermarkTemplate(
            self,
            request: models.CreateWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateWatermarkTemplateResponse:
        """
        创建用户自定义水印模板，数量上限：1000。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWordSamples(
            self,
            request: models.CreateWordSamplesRequest,
            opts: Dict = None,
    ) -> models.CreateWordSamplesResponse:
        """
        该接口用于批量创建关键词样本，样本用于通过OCR、ASR技术，进行不适宜内容识别、内容识别等视频处理。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWordSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWordSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflow(
            self,
            request: models.CreateWorkflowRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowResponse:
        """
        对 COS 中指定 Bucket 的目录下上传的媒体文件，设置处理规则，包括：
        1. 视频转码（带水印）；
        2. 视频转动图；
        3. 对视频按指定时间点截图；
        4. 对视频采样截图；
        5. 对视频截图雪碧图；
        6. 对视频转自适应码流；
        7. 智能内容审核（鉴黄、敏感信息检测）；
        8. 智能内容分析（标签、分类、封面、按帧标签）；
        9. 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词）。

        注意：创建工作流成功后是禁用状态，需要手动启用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIAnalysisTemplate(
            self,
            request: models.DeleteAIAnalysisTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAIAnalysisTemplateResponse:
        """
        删除用户自定义内容分析模板。

        注意：模板 ID 为 10000 以下的为系统预置模板，不允许删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIAnalysisTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIAnalysisTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIRecognitionTemplate(
            self,
            request: models.DeleteAIRecognitionTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAIRecognitionTemplateResponse:
        """
        删除用户自定义内容识别模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIRecognitionTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIRecognitionTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAdaptiveDynamicStreamingTemplate(
            self,
            request: models.DeleteAdaptiveDynamicStreamingTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAdaptiveDynamicStreamingTemplateResponse:
        """
        删除转自适应码流模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAdaptiveDynamicStreamingTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAdaptiveDynamicStreamingTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAnimatedGraphicsTemplate(
            self,
            request: models.DeleteAnimatedGraphicsTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAnimatedGraphicsTemplateResponse:
        """
        删除用户自定义转动图模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAnimatedGraphicsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAnimatedGraphicsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAsrHotwords(
            self,
            request: models.DeleteAsrHotwordsRequest,
            opts: Dict = None,
    ) -> models.DeleteAsrHotwordsResponse:
        """
        删除智能字幕热词库
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAsrHotwords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAsrHotwordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBlindWatermarkTemplate(
            self,
            request: models.DeleteBlindWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteBlindWatermarkTemplateResponse:
        """
        删除用户自定义数字水印模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBlindWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBlindWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteContentReviewTemplate(
            self,
            request: models.DeleteContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteContentReviewTemplateResponse:
        """
        删除用户自定义内容审核模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteContentReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageSpriteTemplate(
            self,
            request: models.DeleteImageSpriteTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteImageSpriteTemplateResponse:
        """
        删除雪碧图模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageSpriteTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageSpriteTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveRecordTemplate(
            self,
            request: models.DeleteLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveRecordTemplateResponse:
        """
        删除直播录制模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePersonSample(
            self,
            request: models.DeletePersonSampleRequest,
            opts: Dict = None,
    ) -> models.DeletePersonSampleResponse:
        """
        该接口用于根据素材 ID，删除素材样本。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProcessImageTemplate(
            self,
            request: models.DeleteProcessImageTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteProcessImageTemplateResponse:
        """
        删除图片处理模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProcessImageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProcessImageTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteQualityControlTemplate(
            self,
            request: models.DeleteQualityControlTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteQualityControlTemplateResponse:
        """
        删除媒体质检模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteQualityControlTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteQualityControlTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSampleSnapshotTemplate(
            self,
            request: models.DeleteSampleSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSampleSnapshotTemplateResponse:
        """
        删除用户自定义采样截图模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSampleSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSampleSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSchedule(
            self,
            request: models.DeleteScheduleRequest,
            opts: Dict = None,
    ) -> models.DeleteScheduleResponse:
        """
        删除编排
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSmartEraseTemplate(
            self,
            request: models.DeleteSmartEraseTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSmartEraseTemplateResponse:
        """
        删除用户自定义智能擦除模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmartEraseTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmartEraseTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSmartSubtitleTemplate(
            self,
            request: models.DeleteSmartSubtitleTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSmartSubtitleTemplateResponse:
        """
        删除用户自定义智能字幕模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmartSubtitleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmartSubtitleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshotByTimeOffsetTemplate(
            self,
            request: models.DeleteSnapshotByTimeOffsetTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotByTimeOffsetTemplateResponse:
        """
        删除用户自定义指定时间点截图模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshotByTimeOffsetTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotByTimeOffsetTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLinkEvent(
            self,
            request: models.DeleteStreamLinkEventRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLinkEventResponse:
        """
        删除媒体传输的事件配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLinkEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLinkEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLinkFlow(
            self,
            request: models.DeleteStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLinkFlowResponse:
        """
        删除媒体传输的传输流配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLinkOutput(
            self,
            request: models.DeleteStreamLinkOutputRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLinkOutputResponse:
        """
        删除媒体传输流的输出配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLinkOutput"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLinkOutputResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLinkSecurityGroup(
            self,
            request: models.DeleteStreamLinkSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLinkSecurityGroupResponse:
        """
        删除安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLinkSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLinkSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTranscodeTemplate(
            self,
            request: models.DeleteTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteTranscodeTemplateResponse:
        """
        删除用户自定义转码模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWatermarkTemplate(
            self,
            request: models.DeleteWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteWatermarkTemplateResponse:
        """
        删除用户自定义水印模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWordSamples(
            self,
            request: models.DeleteWordSamplesRequest,
            opts: Dict = None,
    ) -> models.DeleteWordSamplesResponse:
        """
        该接口用于批量删除关键词样本。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWordSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWordSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkflow(
            self,
            request: models.DeleteWorkflowRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowResponse:
        """
        删除工作流。对于已启用的工作流，需要禁用后才能删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisTemplates(
            self,
            request: models.DescribeAIAnalysisTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisTemplatesResponse:
        """
        根据内容分析模板唯一标识，获取内容分析模板详情列表。返回结果包含符合条件的所有用户自定义内容分析模板及系统预置视频内容分析模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIRecognitionTemplates(
            self,
            request: models.DescribeAIRecognitionTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAIRecognitionTemplatesResponse:
        """
        根据内容识别模板唯一标识，获取内容识别模板详情列表。返回结果包含符合条件的所有用户自定义内容识别模板及系统预置视频内容识别模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIRecognitionTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIRecognitionTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAdaptiveDynamicStreamingTemplates(
            self,
            request: models.DescribeAdaptiveDynamicStreamingTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAdaptiveDynamicStreamingTemplatesResponse:
        """
        查询转自适应码流模板，支持根据条件，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAdaptiveDynamicStreamingTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAdaptiveDynamicStreamingTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAnimatedGraphicsTemplates(
            self,
            request: models.DescribeAnimatedGraphicsTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAnimatedGraphicsTemplatesResponse:
        """
        查询转动图模板列表，支持根据条件，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAnimatedGraphicsTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAnimatedGraphicsTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsrHotwords(
            self,
            request: models.DescribeAsrHotwordsRequest,
            opts: Dict = None,
    ) -> models.DescribeAsrHotwordsResponse:
        """
        查询智能字幕热词库
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsrHotwords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsrHotwordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsrHotwordsList(
            self,
            request: models.DescribeAsrHotwordsListRequest,
            opts: Dict = None,
    ) -> models.DescribeAsrHotwordsListResponse:
        """
        获取热词库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsrHotwordsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsrHotwordsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchTaskDetail(
            self,
            request: models.DescribeBatchTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchTaskDetailResponse:
        """
        通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询7天之内提交的任务）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlindWatermarkTemplates(
            self,
            request: models.DescribeBlindWatermarkTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeBlindWatermarkTemplatesResponse:
        """
        查询用户自定义数字水印模板，支持根据条件，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlindWatermarkTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlindWatermarkTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContentReviewTemplates(
            self,
            request: models.DescribeContentReviewTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeContentReviewTemplatesResponse:
        """
        根据智能审核模板唯一标识，获取智能审核模板详情列表。返回结果包含符合条件的所有用户自定义模板及系统预置智能审核模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContentReviewTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContentReviewTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupAttachFlowsById(
            self,
            request: models.DescribeGroupAttachFlowsByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupAttachFlowsByIdResponse:
        """
        根据安全组反差关联的Flow信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupAttachFlowsById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupAttachFlowsByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageSpriteTemplates(
            self,
            request: models.DescribeImageSpriteTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeImageSpriteTemplatesResponse:
        """
        查询雪碧图模板，支持根据条件，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageSpriteTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageSpriteTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageTaskDetail(
            self,
            request: models.DescribeImageTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeImageTaskDetailResponse:
        """
        通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询7天之内提交的任务）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveRecordTemplates(
            self,
            request: models.DescribeLiveRecordTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveRecordTemplatesResponse:
        """
        获取直播录制模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveRecordTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveRecordTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMediaMetaData(
            self,
            request: models.DescribeMediaMetaDataRequest,
            opts: Dict = None,
    ) -> models.DescribeMediaMetaDataResponse:
        """
        获取媒体的元信息，包括视频画面宽、高、编码格式、时长、帧率等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMediaMetaData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMediaMetaDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePersonSamples(
            self,
            request: models.DescribePersonSamplesRequest,
            opts: Dict = None,
    ) -> models.DescribePersonSamplesResponse:
        """
        该接口用于查询素材样本信息，支持根据素材 ID、名称、标签，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePersonSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePersonSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessImageTemplates(
            self,
            request: models.DescribeProcessImageTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessImageTemplatesResponse:
        """
        查询图片处理模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessImageTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessImageTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityControlTemplates(
            self,
            request: models.DescribeQualityControlTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityControlTemplatesResponse:
        """
        查询用户自定义媒体质检模板，支持根据条件，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityControlTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityControlTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleSnapshotTemplates(
            self,
            request: models.DescribeSampleSnapshotTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleSnapshotTemplatesResponse:
        """
        查询采样截图模板，支持根据条件，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleSnapshotTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleSnapshotTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedules(
            self,
            request: models.DescribeSchedulesRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulesResponse:
        """
        查询编排。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmartEraseTemplates(
            self,
            request: models.DescribeSmartEraseTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSmartEraseTemplatesResponse:
        """
        根据智能擦除模板唯一标识，获取智能擦除模板详情列表。返回结果包含符合条件的所有用户自定义智能擦除模板及系统预置智能擦除模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmartEraseTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmartEraseTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmartSubtitleTemplates(
            self,
            request: models.DescribeSmartSubtitleTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSmartSubtitleTemplatesResponse:
        """
        根据智能字幕 模板唯一标识，获取智能字幕模板详情列表。返回结果包含符合条件的所有用户自定义智能字幕模板及系统预置智能字幕模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmartSubtitleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmartSubtitleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotByTimeOffsetTemplates(
            self,
            request: models.DescribeSnapshotByTimeOffsetTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotByTimeOffsetTemplatesResponse:
        """
        查询指定时间点截图模板，支持根据条件，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotByTimeOffsetTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotByTimeOffsetTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkActivateState(
            self,
            request: models.DescribeStreamLinkActivateStateRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkActivateStateResponse:
        """
        查询媒体传输开通状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkActivateState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkActivateStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkEvent(
            self,
            request: models.DescribeStreamLinkEventRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkEventResponse:
        """
        查询媒体传输事件的配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkEventAttachedFlows(
            self,
            request: models.DescribeStreamLinkEventAttachedFlowsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkEventAttachedFlowsResponse:
        """
        查询媒体传输事件关联的所有媒体输入流的配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkEventAttachedFlows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkEventAttachedFlowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkEvents(
            self,
            request: models.DescribeStreamLinkEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkEventsResponse:
        """
        批量查询媒体传输事件的配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlow(
            self,
            request: models.DescribeStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowResponse:
        """
        查询媒体输入流的配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlowLogs(
            self,
            request: models.DescribeStreamLinkFlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowLogsResponse:
        """
        查询媒体传输流的日志信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlowMediaStatistics(
            self,
            request: models.DescribeStreamLinkFlowMediaStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowMediaStatisticsResponse:
        """
        查询媒体传输流的媒体质量数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlowMediaStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowMediaStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlowRealtimeStatus(
            self,
            request: models.DescribeStreamLinkFlowRealtimeStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowRealtimeStatusResponse:
        """
        实时查询流的当前状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlowRealtimeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowRealtimeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlowSRTStatistics(
            self,
            request: models.DescribeStreamLinkFlowSRTStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowSRTStatisticsResponse:
        """
        查询媒体传输流的SRT质量数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlowSRTStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowSRTStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlowStatistics(
            self,
            request: models.DescribeStreamLinkFlowStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowStatisticsResponse:
        """
        查询媒体传输流的媒体质量数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlowStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlows(
            self,
            request: models.DescribeStreamLinkFlowsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowsResponse:
        """
        批量查询媒体输入流的配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkRegions(
            self,
            request: models.DescribeStreamLinkRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkRegionsResponse:
        """
        查询媒体传输所有地区。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkSecurityGroups(
            self,
            request: models.DescribeStreamLinkSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkSecurityGroupsResponse:
        """
        批量查询安全组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskDetail(
            self,
            request: models.DescribeTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskDetailResponse:
        """
        通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询7天之内提交的任务）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        * 该接口用于查询任务列表；
        * 当列表数据比较多时，单次接口调用无法拉取整个列表，可通过 ScrollToken 参数，分批拉取；
        * 只能查询到最近七天（168小时）内的任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTranscodeTemplates(
            self,
            request: models.DescribeTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeTranscodeTemplatesResponse:
        """
        根据转码模板唯一标识，获取转码模板详情列表。返回结果包含符合条件的所有用户自定义模板及[系统预置转码模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsageData(
            self,
            request: models.DescribeUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeUsageDataResponse:
        """
        该接口返回查询时间范围内每天使用的媒体处理用量信息。
           1. 可以查询最近365天内的媒体处理统计数据。
           2. 查询时间跨度不超过90天。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoDatabaseEntryTaskDetail(
            self,
            request: models.DescribeVideoDatabaseEntryTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoDatabaseEntryTaskDetailResponse:
        """
        根据任务ID查询视频入库任务的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoDatabaseEntryTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoDatabaseEntryTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoSearchTaskDetail(
            self,
            request: models.DescribeVideoSearchTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoSearchTaskDetailResponse:
        """
        根据任务ID查询视频检索任务的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoSearchTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoSearchTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWatermarkTemplates(
            self,
            request: models.DescribeWatermarkTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeWatermarkTemplatesResponse:
        """
        查询用户自定义水印模板，支持根据条件，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWatermarkTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWatermarkTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWordSamples(
            self,
            request: models.DescribeWordSamplesRequest,
            opts: Dict = None,
    ) -> models.DescribeWordSamplesResponse:
        """
        该接口用于根据应用场景、关键词、标签，分页查询关键词样本信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWordSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWordSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflows(
            self,
            request: models.DescribeWorkflowsRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowsResponse:
        """
        根据工作流 ID，获取工作流详情列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableSchedule(
            self,
            request: models.DisableScheduleRequest,
            opts: Dict = None,
    ) -> models.DisableScheduleResponse:
        """
        禁用自动化触发编排任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableWorkflow(
            self,
            request: models.DisableWorkflowRequest,
            opts: Dict = None,
    ) -> models.DisableWorkflowResponse:
        """
        禁用工作流。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroup(
            self,
            request: models.DisassociateSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupResponse:
        """
        批量解绑安全组下面关联的输入输出。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditMedia(
            self,
            request: models.EditMediaRequest,
            opts: Dict = None,
    ) -> models.EditMediaResponse:
        """
        对视频进行编辑，生成一个新的视频。编辑的功能包括：


        一、**剪辑任务**：简单的视频剪辑，如剪辑、拼接等
        1. 对一个文件进行剪辑，生成一个新的视频；
        2. 对多个文件进行拼接，生成一个新的视频；
        3. 对多个文件进行剪辑，然后再拼接，生成一个新的视频。

        二、**合成任务**：通过接口描述信息，合成一个新的视频。
        1. 多轨道（视频、音频、字幕）、多类型元素（视频、图片、音频、文字、空）
        2. 图像级别：贴图、缩放、任意角度旋转、镜像等
        3. 音频级别：音量控制、淡入淡出、混音等
        4. 视频级别：转场、倍数播放、拼接、剪切、字幕、画中画、音画分离、出入场动效等
        """
        
        kwargs = {}
        kwargs["action"] = "EditMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableSchedule(
            self,
            request: models.EnableScheduleRequest,
            opts: Dict = None,
    ) -> models.EnableScheduleResponse:
        """
        启用自动化触发编排任务。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableWorkflow(
            self,
            request: models.EnableWorkflowRequest,
            opts: Dict = None,
    ) -> models.EnableWorkflowResponse:
        """
        启用工作流。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteFunction(
            self,
            request: models.ExecuteFunctionRequest,
            opts: Dict = None,
    ) -> models.ExecuteFunctionResponse:
        """
        本接口仅用于定制开发的特殊场景，除非云媒体处理客服人员主动告知您需要使用本接口，其它情况请勿调用。
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractBlindWatermark(
            self,
            request: models.ExtractBlindWatermarkRequest,
            opts: Dict = None,
    ) -> models.ExtractBlindWatermarkResponse:
        """
        用于发起提取视频数字水印任务，提取结果可以通过DescribeTaskDetail查询。
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractBlindWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractBlindWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageTask(
            self,
            request: models.ManageTaskRequest,
            opts: Dict = None,
    ) -> models.ManageTaskResponse:
        """
        对已发起的任务进行管理。
        """
        
        kwargs = {}
        kwargs["action"] = "ManageTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAIAnalysisTemplate(
            self,
            request: models.ModifyAIAnalysisTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyAIAnalysisTemplateResponse:
        """
        修改用户自定义内容分析模板。

        注意：模板 ID 10000 以下的为系统预置模板，不允许修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAIAnalysisTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAIAnalysisTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAIRecognitionTemplate(
            self,
            request: models.ModifyAIRecognitionTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyAIRecognitionTemplateResponse:
        """
        修改用户自定义内容识别模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAIRecognitionTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAIRecognitionTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAdaptiveDynamicStreamingTemplate(
            self,
            request: models.ModifyAdaptiveDynamicStreamingTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyAdaptiveDynamicStreamingTemplateResponse:
        """
        修改转自适应码流模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAdaptiveDynamicStreamingTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAdaptiveDynamicStreamingTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAnimatedGraphicsTemplate(
            self,
            request: models.ModifyAnimatedGraphicsTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyAnimatedGraphicsTemplateResponse:
        """
        修改用户自定义转动图模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAnimatedGraphicsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAnimatedGraphicsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAsrHotwords(
            self,
            request: models.ModifyAsrHotwordsRequest,
            opts: Dict = None,
    ) -> models.ModifyAsrHotwordsResponse:
        """
        智能字幕更新热词库接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAsrHotwords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAsrHotwordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBlindWatermarkTemplate(
            self,
            request: models.ModifyBlindWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyBlindWatermarkTemplateResponse:
        """
        修改用户自定义数字水印模板，数字水印类型不允许修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBlindWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBlindWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyContentReviewTemplate(
            self,
            request: models.ModifyContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyContentReviewTemplateResponse:
        """
        修改用户自定义内容审核模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContentReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageSpriteTemplate(
            self,
            request: models.ModifyImageSpriteTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyImageSpriteTemplateResponse:
        """
        修改用户自定义雪碧图模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageSpriteTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageSpriteTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveRecordTemplate(
            self,
            request: models.ModifyLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveRecordTemplateResponse:
        """
        修改直播录制模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPersonSample(
            self,
            request: models.ModifyPersonSampleRequest,
            opts: Dict = None,
    ) -> models.ModifyPersonSampleResponse:
        """
        该接口用于根据素材 ID，修改素材样本信息，包括名称、描述的修改，以及五官、标签的添加、删除、重置操作。五官删除操作需保证至少剩余 1 张图片，否则，请使用重置操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProcessImageTemplate(
            self,
            request: models.ModifyProcessImageTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyProcessImageTemplateResponse:
        """
        修改图片处理模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProcessImageTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProcessImageTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyQualityControlTemplate(
            self,
            request: models.ModifyQualityControlTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyQualityControlTemplateResponse:
        """
        修改媒体质检模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyQualityControlTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyQualityControlTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySampleSnapshotTemplate(
            self,
            request: models.ModifySampleSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifySampleSnapshotTemplateResponse:
        """
        修改用户自定义采样截图模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySampleSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySampleSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySchedule(
            self,
            request: models.ModifyScheduleRequest,
            opts: Dict = None,
    ) -> models.ModifyScheduleResponse:
        """
        修改编排
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySmartEraseTemplate(
            self,
            request: models.ModifySmartEraseTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifySmartEraseTemplateResponse:
        """
        修改用户自定义智能擦除模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySmartEraseTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySmartEraseTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySmartSubtitleTemplate(
            self,
            request: models.ModifySmartSubtitleTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifySmartSubtitleTemplateResponse:
        """
        修改用户自定义智能字幕模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySmartSubtitleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySmartSubtitleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshotByTimeOffsetTemplate(
            self,
            request: models.ModifySnapshotByTimeOffsetTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotByTimeOffsetTemplateResponse:
        """
        修改用户自定义指定时间点截图模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshotByTimeOffsetTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotByTimeOffsetTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLinkEvent(
            self,
            request: models.ModifyStreamLinkEventRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLinkEventResponse:
        """
        修改媒体传输的事件配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLinkEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLinkEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLinkFlow(
            self,
            request: models.ModifyStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLinkFlowResponse:
        """
        修改媒体传输的传输流配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLinkInput(
            self,
            request: models.ModifyStreamLinkInputRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLinkInputResponse:
        """
        修改媒体传输流的输入信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLinkInput"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLinkInputResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLinkOutputInfo(
            self,
            request: models.ModifyStreamLinkOutputInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLinkOutputInfoResponse:
        """
        修改媒体传输流的输出配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLinkOutputInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLinkOutputInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLinkSecurityGroup(
            self,
            request: models.ModifyStreamLinkSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLinkSecurityGroupResponse:
        """
        更新安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLinkSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLinkSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTranscodeTemplate(
            self,
            request: models.ModifyTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyTranscodeTemplateResponse:
        """
        修改用户自定义转码模板信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWatermarkTemplate(
            self,
            request: models.ModifyWatermarkTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyWatermarkTemplateResponse:
        """
        修改用户自定义水印模板，水印类型不允许修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWatermarkTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWatermarkTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWordSample(
            self,
            request: models.ModifyWordSampleRequest,
            opts: Dict = None,
    ) -> models.ModifyWordSampleResponse:
        """
        该接口用于修改关键词的应用场景、标签，关键词本身不可修改，如需修改，可删除重建。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWordSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWordSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseLiveStreamProcessNotification(
            self,
            request: models.ParseLiveStreamProcessNotificationRequest,
            opts: Dict = None,
    ) -> models.ParseLiveStreamProcessNotificationResponse:
        """
        从 CMQ 获取到消息后，从消息的 msgBody 字段中解析出 MPS 直播流处理事件通知的内容。
        该接口不用于发起网络调用，而是用来帮助生成各个语言平台的 SDK，您可以参考 SDK 中的解析实现事件通知的解析。
        """
        
        kwargs = {}
        kwargs["action"] = "ParseLiveStreamProcessNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseLiveStreamProcessNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseNotification(
            self,
            request: models.ParseNotificationRequest,
            opts: Dict = None,
    ) -> models.ParseNotificationResponse:
        """
        从 CMQ 获取到消息后，从消息的 msgBody 字段中解析出 MPS 事件通知的内容。
        该接口不用于发起网络调用，而是用来帮助生成各个语言平台的 SDK，您可以参考 SDK 中的解析函数，实现事件通知的解析。
        """
        
        kwargs = {}
        kwargs["action"] = "ParseNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessImage(
            self,
            request: models.ProcessImageRequest,
            opts: Dict = None,
    ) -> models.ProcessImageResponse:
        """
        发起图片处理，功能包括：
        1. 格式转换；
        2. 图像增强；
        3. 图像擦除;
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessLiveStream(
            self,
            request: models.ProcessLiveStreamRequest,
            opts: Dict = None,
    ) -> models.ProcessLiveStreamResponse:
        """
        对直播流媒体发起处理任务，功能包括：

        * 智能内容审核（画面鉴黄、敏感信息检测、声音鉴黄）；
        * 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词、语音实时翻译、物体识别、游戏打点）。
        * 智能内容分析（新闻实时拆条）。
        * 质检（直播流格式诊断、音画内容检测（抖动、模糊、低光照、过曝光、黑边、白边、黑屏、白屏、花屏、噪点、马赛克、二维码等）、无参考打分）。
        * 录制

        直播流处理事件通知支持HTTP回调，也支持实时写入用户指定的消息队列 CMQ 中，用户从消息队列 CMQ 中获取事件通知结果，同时处理过程中存在输出文件的，会写入用户指定的输出文件的目标存储中。
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMedia(
            self,
            request: models.ProcessMediaRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaResponse:
        """
        对 URL视频链接 或 COS 中的媒体文件发起处理任务，功能包括：
        - 音视频转码（例如普通转码、极速高清转码、音视频增强、添加明水印、添加数字水印）；
        - 音视频转自适应码流；
        - 视频转动图；
        - 对视频按指定时间点截图；
        - 对视频采样截图；
        - 对视频截图雪碧图；
        - 媒体质检（例如媒体格式诊断、音画内容检测、无参考打分，其中音画内容检测主要针对抖动、模糊、低光照、过曝光、花屏、噪点、马赛克、二维码等问题）;
        - 智能字幕（例如生成字幕并翻译）；
        - 智能擦除（例如去水印、去字幕、隐私保护）；
        - 智能内容审核（例如鉴黄、敏感信息检测）；
        - 智能内容分析（例如标签、分类、封面、按帧标签、拆条、集锦、片头片尾、游戏打点）；
        - 智能内容识别（例如人脸、文本全文、文本关键词、语音全文、语音关键词、语音翻译、物体识别）；
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeMediaForZhiXue(
            self,
            request: models.RecognizeMediaForZhiXueRequest,
            opts: Dict = None,
    ) -> models.RecognizeMediaForZhiXueResponse:
        """
        智能媒体识别，包含表情和动作识别。仅用于智学，其他调用无效。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeMediaForZhiXue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeMediaForZhiXueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetWorkflow(
            self,
            request: models.ResetWorkflowRequest,
            opts: Dict = None,
    ) -> models.ResetWorkflowResponse:
        """
        重新设置一个已经存在且处于禁用状态的工作流。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartStreamLinkFlow(
            self,
            request: models.StartStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.StartStreamLinkFlowResponse:
        """
        启动媒体传输流。
        """
        
        kwargs = {}
        kwargs["action"] = "StartStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopStreamLinkFlow(
            self,
            request: models.StopStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.StopStreamLinkFlowResponse:
        """
        停止媒体传输流。
        """
        
        kwargs = {}
        kwargs["action"] = "StopStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextTranslation(
            self,
            request: models.TextTranslationRequest,
            opts: Dict = None,
    ) -> models.TextTranslationResponse:
        """
        文本翻译
        """
        
        kwargs = {}
        kwargs["action"] = "TextTranslation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextTranslationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def WithdrawsWatermark(
            self,
            request: models.WithdrawsWatermarkRequest,
            opts: Dict = None,
    ) -> models.WithdrawsWatermarkResponse:
        """
        提取视频中的盲水印。
        """
        
        kwargs = {}
        kwargs["action"] = "WithdrawsWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.WithdrawsWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)