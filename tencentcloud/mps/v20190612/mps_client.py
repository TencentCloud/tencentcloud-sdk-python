# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.mps.v20190612 import models


class MpsClient(AbstractClient):
    _apiVersion = '2019-06-12'
    _endpoint = 'mps.tencentcloudapi.com'
    _service = 'mps'


    def BatchDeleteStreamLinkFlow(self, request):
        """批量删除媒体传输流。

        :param request: Request instance for BatchDeleteStreamLinkFlow.
        :type request: :class:`tencentcloud.mps.v20190612.models.BatchDeleteStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.BatchDeleteStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchProcessMedia(self, request):
        """对 URL视频链接批量发起处理任务，功能包括：
        智能字幕（语音全文、语音热词、语音翻译）

        :param request: Request instance for BatchProcessMedia.
        :type request: :class:`tencentcloud.mps.v20190612.models.BatchProcessMediaRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.BatchProcessMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchProcessMedia", params, headers=headers)
            response = json.loads(body)
            model = models.BatchProcessMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStartStreamLinkFlow(self, request):
        """批量启动媒体传输流。

        :param request: Request instance for BatchStartStreamLinkFlow.
        :type request: :class:`tencentcloud.mps.v20190612.models.BatchStartStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.BatchStartStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStartStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStartStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStopStreamLinkFlow(self, request):
        """批量停止媒体传输流。

        :param request: Request instance for BatchStopStreamLinkFlow.
        :type request: :class:`tencentcloud.mps.v20190612.models.BatchStopStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.BatchStopStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStopStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIAnalysisTemplate(self, request):
        """创建用户自定义内容分析模板，数量上限：50。

        :param request: Request instance for CreateAIAnalysisTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIAnalysisTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIAnalysisTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIRecognitionTemplate(self, request):
        """创建用户自定义内容识别模板，数量上限：50。

        :param request: Request instance for CreateAIRecognitionTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIRecognitionTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIRecognitionTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAdaptiveDynamicStreamingTemplate(self, request):
        """创建转自适应码流模板，数量上限：100。

        :param request: Request instance for CreateAdaptiveDynamicStreamingTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAdaptiveDynamicStreamingTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAdaptiveDynamicStreamingTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAnimatedGraphicsTemplate(self, request):
        """创建用户自定义转动图模板，数量上限：16。

        :param request: Request instance for CreateAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAnimatedGraphicsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAnimatedGraphicsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAsrHotwords(self, request):
        """智能字幕新建热词库接口

        :param request: Request instance for CreateAsrHotwords.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAsrHotwordsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAsrHotwordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAsrHotwords", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAsrHotwordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateContentReviewTemplate(self, request):
        """创建用户自定义内容审核模板，数量上限：50。

        :param request: Request instance for CreateContentReviewTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateContentReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateContentReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageSpriteTemplate(self, request):
        """创建用户自定义雪碧图模板，数量上限：16。

        :param request: Request instance for CreateImageSpriteTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageSpriteTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageSpriteTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveRecordTemplate(self, request):
        """创建直播录制模板

        :param request: Request instance for CreateLiveRecordTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePersonSample(self, request):
        """该接口用于创建素材样本，用于通过五官定位等技术，进行内容识别、内容不适宜等视频处理。

        :param request: Request instance for CreatePersonSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreatePersonSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreatePersonSampleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePersonSample", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePersonSampleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQualityControlTemplate(self, request):
        """创建媒体质检模板，数量上限：50。

        :param request: Request instance for CreateQualityControlTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateQualityControlTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateQualityControlTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQualityControlTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQualityControlTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSampleSnapshotTemplate(self, request):
        """创建用户自定义采样截图模板，数量上限：16。

        :param request: Request instance for CreateSampleSnapshotTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateSampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateSampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSampleSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSampleSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSchedule(self, request):
        """对 COS 中指定 Bucket 的目录下上传的媒体文件，设置处理规则，包括：
        1. 视频转码（带水印）；
        2. 视频转动图；
        3. 对视频按指定时间点截图；
        4. 对视频采样截图；
        5. 对视频截图雪碧图；
        6. 对视频转自适应码流；
        7. 智能内容审核（鉴黄、敏感信息检测）；
        8. 智能内容分析（标签、分类、封面、按帧标签）；
        9. 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词）。

        注意：创建编排成功后是禁用状态，需要手动启用。

        :param request: Request instance for CreateSchedule.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateScheduleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSmartSubtitleTemplate(self, request):
        """创建自定义智能字幕模板

        :param request: Request instance for CreateSmartSubtitleTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateSmartSubtitleTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateSmartSubtitleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSmartSubtitleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSmartSubtitleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSnapshotByTimeOffsetTemplate(self, request):
        """创建用户自定义指定时间点截图模板，数量上限：16。

        :param request: Request instance for CreateSnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateSnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshotByTimeOffsetTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotByTimeOffsetTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamLinkEvent(self, request):
        """创建媒体传输的事件Event。

        :param request: Request instance for CreateStreamLinkEvent.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateStreamLinkEventRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateStreamLinkEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLinkEvent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLinkEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamLinkFlow(self, request):
        """创建媒体传输的传输流配置。

        :param request: Request instance for CreateStreamLinkFlow.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamLinkInput(self, request):
        """创建媒体传输的输入配置。

        :param request: Request instance for CreateStreamLinkInput.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateStreamLinkInputRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateStreamLinkInputResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLinkInput", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLinkInputResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamLinkOutputInfo(self, request):
        """创建媒体传输流的输出信息。

        :param request: Request instance for CreateStreamLinkOutputInfo.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateStreamLinkOutputInfoRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateStreamLinkOutputInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLinkOutputInfo", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLinkOutputInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamLinkSecurityGroup(self, request):
        """创建安全组，数量限制5个。

        :param request: Request instance for CreateStreamLinkSecurityGroup.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateStreamLinkSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateStreamLinkSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLinkSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLinkSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTranscodeTemplate(self, request):
        """创建用户自定义转码模板，数量上限：1000

        :param request: Request instance for CreateTranscodeTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoDatabaseEntryTask(self, request):
        """对URL链接或COS中的视频发起入库任务。
        可选在任务完成后向回调方发送任务完成状态信息。

        :param request: Request instance for CreateVideoDatabaseEntryTask.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateVideoDatabaseEntryTaskRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateVideoDatabaseEntryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoDatabaseEntryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoDatabaseEntryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoSearchTask(self, request):
        """使用检索值检索库中最接近检索值的若干视频。

        :param request: Request instance for CreateVideoSearchTask.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateVideoSearchTaskRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateVideoSearchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoSearchTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoSearchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWatermarkTemplate(self, request):
        """创建用户自定义水印模板，数量上限：1000。

        :param request: Request instance for CreateWatermarkTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWatermarkTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWatermarkTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWordSamples(self, request):
        """该接口用于批量创建关键词样本，样本用于通过OCR、ASR技术，进行不适宜内容识别、内容识别等视频处理。

        :param request: Request instance for CreateWordSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateWordSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateWordSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWordSamples", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWordSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkflow(self, request):
        """对 COS 中指定 Bucket 的目录下上传的媒体文件，设置处理规则，包括：
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

        :param request: Request instance for CreateWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAIAnalysisTemplate(self, request):
        """删除用户自定义内容分析模板。

        注意：模板 ID 为 10000 以下的为系统预置模板，不允许删除。

        :param request: Request instance for DeleteAIAnalysisTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIAnalysisTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIAnalysisTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAIRecognitionTemplate(self, request):
        """删除用户自定义内容识别模板。

        :param request: Request instance for DeleteAIRecognitionTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIRecognitionTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIRecognitionTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAdaptiveDynamicStreamingTemplate(self, request):
        """删除转自适应码流模板

        :param request: Request instance for DeleteAdaptiveDynamicStreamingTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAdaptiveDynamicStreamingTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAdaptiveDynamicStreamingTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAnimatedGraphicsTemplate(self, request):
        """删除用户自定义转动图模板。

        :param request: Request instance for DeleteAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAnimatedGraphicsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAnimatedGraphicsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAsrHotwords(self, request):
        """删除智能字幕热词库

        :param request: Request instance for DeleteAsrHotwords.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAsrHotwordsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAsrHotwordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAsrHotwords", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAsrHotwordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteContentReviewTemplate(self, request):
        """删除用户自定义内容审核模板。

        :param request: Request instance for DeleteContentReviewTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteContentReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteContentReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageSpriteTemplate(self, request):
        """删除雪碧图模板。

        :param request: Request instance for DeleteImageSpriteTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageSpriteTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageSpriteTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveRecordTemplate(self, request):
        """删除直播录制模板

        :param request: Request instance for DeleteLiveRecordTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePersonSample(self, request):
        """该接口用于根据素材 ID，删除素材样本。

        :param request: Request instance for DeletePersonSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeletePersonSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeletePersonSampleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePersonSample", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePersonSampleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQualityControlTemplate(self, request):
        """删除媒体质检模板

        :param request: Request instance for DeleteQualityControlTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteQualityControlTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteQualityControlTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQualityControlTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQualityControlTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSampleSnapshotTemplate(self, request):
        """删除用户自定义采样截图模板。

        :param request: Request instance for DeleteSampleSnapshotTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteSampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteSampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSampleSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSampleSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSchedule(self, request):
        """删除编排

        :param request: Request instance for DeleteSchedule.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteScheduleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSmartSubtitleTemplate(self, request):
        """删除用户自定义智能字幕模板。

        :param request: Request instance for DeleteSmartSubtitleTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteSmartSubtitleTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteSmartSubtitleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSmartSubtitleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSmartSubtitleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshotByTimeOffsetTemplate(self, request):
        """删除用户自定义指定时间点截图模板。

        :param request: Request instance for DeleteSnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteSnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshotByTimeOffsetTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotByTimeOffsetTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamLinkEvent(self, request):
        """删除媒体传输的事件配置。

        :param request: Request instance for DeleteStreamLinkEvent.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteStreamLinkEventRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteStreamLinkEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLinkEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLinkEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamLinkFlow(self, request):
        """删除媒体传输的传输流配置。

        :param request: Request instance for DeleteStreamLinkFlow.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamLinkOutput(self, request):
        """删除媒体传输流的输出配置。

        :param request: Request instance for DeleteStreamLinkOutput.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteStreamLinkOutputRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteStreamLinkOutputResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLinkOutput", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLinkOutputResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamLinkSecurityGroup(self, request):
        """删除安全组。

        :param request: Request instance for DeleteStreamLinkSecurityGroup.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteStreamLinkSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteStreamLinkSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLinkSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLinkSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTranscodeTemplate(self, request):
        """删除用户自定义转码模板。

        :param request: Request instance for DeleteTranscodeTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWatermarkTemplate(self, request):
        """删除用户自定义水印模板。

        :param request: Request instance for DeleteWatermarkTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWatermarkTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWatermarkTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWordSamples(self, request):
        """该接口用于批量删除关键词样本。

        :param request: Request instance for DeleteWordSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteWordSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteWordSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWordSamples", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWordSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkflow(self, request):
        """删除工作流。对于已启用的工作流，需要禁用后才能删除。

        :param request: Request instance for DeleteWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisTemplates(self, request):
        """根据内容分析模板唯一标识，获取内容分析模板详情列表。返回结果包含符合条件的所有用户自定义内容分析模板及系统预置视频内容分析模板

        :param request: Request instance for DescribeAIAnalysisTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAIAnalysisTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAIAnalysisTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIRecognitionTemplates(self, request):
        """根据内容识别模板唯一标识，获取内容识别模板详情列表。返回结果包含符合条件的所有用户自定义内容识别模板及系统预置视频内容识别模板

        :param request: Request instance for DescribeAIRecognitionTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAIRecognitionTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAIRecognitionTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIRecognitionTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIRecognitionTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAdaptiveDynamicStreamingTemplates(self, request):
        """查询转自适应码流模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeAdaptiveDynamicStreamingTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAdaptiveDynamicStreamingTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAdaptiveDynamicStreamingTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAdaptiveDynamicStreamingTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAdaptiveDynamicStreamingTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAnimatedGraphicsTemplates(self, request):
        """查询转动图模板列表，支持根据条件，分页查询。

        :param request: Request instance for DescribeAnimatedGraphicsTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAnimatedGraphicsTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAnimatedGraphicsTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAnimatedGraphicsTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAnimatedGraphicsTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAsrHotwords(self, request):
        """查询智能字幕热词库

        :param request: Request instance for DescribeAsrHotwords.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAsrHotwordsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAsrHotwordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsrHotwords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAsrHotwordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAsrHotwordsList(self, request):
        """获取热词库列表

        :param request: Request instance for DescribeAsrHotwordsList.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAsrHotwordsListRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAsrHotwordsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsrHotwordsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAsrHotwordsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchTaskDetail(self, request):
        """通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询7天之内提交的任务）。

        :param request: Request instance for DescribeBatchTaskDetail.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeBatchTaskDetailRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeBatchTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContentReviewTemplates(self, request):
        """根据智能审核模板唯一标识，获取智能审核模板详情列表。返回结果包含符合条件的所有用户自定义模板及系统预置智能审核模板。

        :param request: Request instance for DescribeContentReviewTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeContentReviewTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeContentReviewTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentReviewTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContentReviewTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupAttachFlowsById(self, request):
        """根据安全组反差关联的Flow信息。

        :param request: Request instance for DescribeGroupAttachFlowsById.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeGroupAttachFlowsByIdRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeGroupAttachFlowsByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupAttachFlowsById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupAttachFlowsByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageSpriteTemplates(self, request):
        """查询雪碧图模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeImageSpriteTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeImageSpriteTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeImageSpriteTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageSpriteTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageSpriteTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageTaskDetail(self, request):
        """通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询7天之内提交的任务）。

        :param request: Request instance for DescribeImageTaskDetail.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeImageTaskDetailRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeImageTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveRecordTemplates(self, request):
        """获取直播录制模板

        :param request: Request instance for DescribeLiveRecordTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeLiveRecordTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeLiveRecordTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveRecordTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveRecordTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMediaMetaData(self, request):
        """获取媒体的元信息，包括视频画面宽、高、编码格式、时长、帧率等。

        :param request: Request instance for DescribeMediaMetaData.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeMediaMetaDataRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeMediaMetaDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMediaMetaData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMediaMetaDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePersonSamples(self, request):
        """该接口用于查询素材样本信息，支持根据素材 ID、名称、标签，分页查询。

        :param request: Request instance for DescribePersonSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribePersonSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribePersonSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePersonSamples", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQualityControlTemplates(self, request):
        """查询用户自定义媒体质检模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeQualityControlTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeQualityControlTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeQualityControlTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityControlTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityControlTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSampleSnapshotTemplates(self, request):
        """查询采样截图模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeSampleSnapshotTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeSampleSnapshotTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeSampleSnapshotTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSampleSnapshotTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSampleSnapshotTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSchedules(self, request):
        """查询编排。

        :param request: Request instance for DescribeSchedules.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeSchedulesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeSchedulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSchedules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSchedulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSmartSubtitleTemplates(self, request):
        """根据智能字幕 模板唯一标识，获取智能字幕模板详情列表。返回结果包含符合条件的所有用户自定义智能字幕模板及系统预置智能字幕模板

        :param request: Request instance for DescribeSmartSubtitleTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeSmartSubtitleTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeSmartSubtitleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmartSubtitleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmartSubtitleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotByTimeOffsetTemplates(self, request):
        """查询指定时间点截图模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeSnapshotByTimeOffsetTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeSnapshotByTimeOffsetTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeSnapshotByTimeOffsetTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotByTimeOffsetTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotByTimeOffsetTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkActivateState(self, request):
        """查询媒体传输开通状态。

        :param request: Request instance for DescribeStreamLinkActivateState.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkActivateStateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkActivateStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkActivateState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkActivateStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkEvent(self, request):
        """查询媒体传输事件的配置信息。

        :param request: Request instance for DescribeStreamLinkEvent.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkEventRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkEventAttachedFlows(self, request):
        """查询媒体传输事件关联的所有媒体输入流的配置信息。

        :param request: Request instance for DescribeStreamLinkEventAttachedFlows.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkEventAttachedFlowsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkEventAttachedFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkEventAttachedFlows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkEventAttachedFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkEvents(self, request):
        """批量查询媒体传输事件的配置信息。

        :param request: Request instance for DescribeStreamLinkEvents.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkEventsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlow(self, request):
        """查询媒体输入流的配置信息。

        :param request: Request instance for DescribeStreamLinkFlow.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlowLogs(self, request):
        """查询媒体传输流的日志信息。

        :param request: Request instance for DescribeStreamLinkFlowLogs.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowLogsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlowMediaStatistics(self, request):
        """查询媒体传输流的媒体质量数据。

        :param request: Request instance for DescribeStreamLinkFlowMediaStatistics.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowMediaStatisticsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowMediaStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlowMediaStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowMediaStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlowRealtimeStatus(self, request):
        """实时查询流的当前状态

        :param request: Request instance for DescribeStreamLinkFlowRealtimeStatus.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowRealtimeStatusRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowRealtimeStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlowRealtimeStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowRealtimeStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlowSRTStatistics(self, request):
        """查询媒体传输流的SRT质量数据。

        :param request: Request instance for DescribeStreamLinkFlowSRTStatistics.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowSRTStatisticsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowSRTStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlowSRTStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowSRTStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlowStatistics(self, request):
        """查询媒体传输流的媒体质量数据。

        :param request: Request instance for DescribeStreamLinkFlowStatistics.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowStatisticsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlowStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlows(self, request):
        """批量查询媒体输入流的配置信息。

        :param request: Request instance for DescribeStreamLinkFlows.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkRegions(self, request):
        """查询媒体传输所有地区。

        :param request: Request instance for DescribeStreamLinkRegions.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkRegionsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkSecurityGroups(self, request):
        """批量查询安全组信息。

        :param request: Request instance for DescribeStreamLinkSecurityGroups.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeStreamLinkSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskDetail(self, request):
        """通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询7天之内提交的任务）。

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        """* 该接口用于查询任务列表；
        * 当列表数据比较多时，单次接口调用无法拉取整个列表，可通过 ScrollToken 参数，分批拉取；
        * 只能查询到最近七天（168小时）内的任务。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTranscodeTemplates(self, request):
        """根据转码模板唯一标识，获取转码模板详情列表。返回结果包含符合条件的所有用户自定义模板及[系统预置转码模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。

        :param request: Request instance for DescribeTranscodeTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoDatabaseEntryTaskDetail(self, request):
        """根据任务ID查询视频入库任务的状态。

        :param request: Request instance for DescribeVideoDatabaseEntryTaskDetail.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeVideoDatabaseEntryTaskDetailRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeVideoDatabaseEntryTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoDatabaseEntryTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoDatabaseEntryTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoSearchTaskDetail(self, request):
        """根据任务ID查询视频检索任务的状态。

        :param request: Request instance for DescribeVideoSearchTaskDetail.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeVideoSearchTaskDetailRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeVideoSearchTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoSearchTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoSearchTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWatermarkTemplates(self, request):
        """查询用户自定义水印模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeWatermarkTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeWatermarkTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeWatermarkTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWatermarkTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWatermarkTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWordSamples(self, request):
        """该接口用于根据应用场景、关键词、标签，分页查询关键词样本信息。

        :param request: Request instance for DescribeWordSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeWordSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeWordSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWordSamples", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWordSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflows(self, request):
        """根据工作流 ID，获取工作流详情列表。

        :param request: Request instance for DescribeWorkflows.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeWorkflowsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeWorkflowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableSchedule(self, request):
        """禁用自动化触发编排任务。

        :param request: Request instance for DisableSchedule.
        :type request: :class:`tencentcloud.mps.v20190612.models.DisableScheduleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DisableScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DisableScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableWorkflow(self, request):
        """禁用工作流。

        :param request: Request instance for DisableWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.DisableWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DisableWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.DisableWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroup(self, request):
        """批量解绑安全组下面关联的输入输出。

        :param request: Request instance for DisassociateSecurityGroup.
        :type request: :class:`tencentcloud.mps.v20190612.models.DisassociateSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DisassociateSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditMedia(self, request):
        """对视频进行编辑，生成一个新的视频。编辑的功能包括：


        一、**剪辑任务**：简单的视频剪辑，如剪辑、拼接等
        1. 对一个文件进行剪辑，生成一个新的视频；
        2. 对多个文件进行拼接，生成一个新的视频；
        3. 对多个文件进行剪辑，然后再拼接，生成一个新的视频。

        二、**合成任务**：通过接口描述信息，合成一个新的视频。
        1. 多轨道（视频、音频、字幕）、多类型元素（视频、图片、音频、文字、空）
        2. 图像级别：贴图、缩放、任意角度旋转、镜像等
        3. 音频级别：音量控制、淡入淡出、混音等
        4. 视频级别：转场、倍数播放、拼接、剪切、字幕、画中画、音画分离、出入场动效等

        :param request: Request instance for EditMedia.
        :type request: :class:`tencentcloud.mps.v20190612.models.EditMediaRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.EditMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditMedia", params, headers=headers)
            response = json.loads(body)
            model = models.EditMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableSchedule(self, request):
        """启用自动化触发编排任务。

        :param request: Request instance for EnableSchedule.
        :type request: :class:`tencentcloud.mps.v20190612.models.EnableScheduleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.EnableScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.EnableScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableWorkflow(self, request):
        """启用工作流。

        :param request: Request instance for EnableWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.EnableWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.EnableWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.EnableWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteFunction(self, request):
        """本接口仅用于定制开发的特殊场景，除非云媒体处理客服人员主动告知您需要使用本接口，其它情况请勿调用。

        :param request: Request instance for ExecuteFunction.
        :type request: :class:`tencentcloud.mps.v20190612.models.ExecuteFunctionRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ExecuteFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteFunction", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageTask(self, request):
        """对已发起的任务进行管理。

        :param request: Request instance for ManageTask.
        :type request: :class:`tencentcloud.mps.v20190612.models.ManageTaskRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ManageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageTask", params, headers=headers)
            response = json.loads(body)
            model = models.ManageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAIAnalysisTemplate(self, request):
        """修改用户自定义内容分析模板。

        注意：模板 ID 10000 以下的为系统预置模板，不允许修改。

        :param request: Request instance for ModifyAIAnalysisTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAIAnalysisTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAIAnalysisTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAIRecognitionTemplate(self, request):
        """修改用户自定义内容识别模板。

        :param request: Request instance for ModifyAIRecognitionTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAIRecognitionTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAIRecognitionTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAdaptiveDynamicStreamingTemplate(self, request):
        """修改转自适应码流模板

        :param request: Request instance for ModifyAdaptiveDynamicStreamingTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAdaptiveDynamicStreamingTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAdaptiveDynamicStreamingTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAnimatedGraphicsTemplate(self, request):
        """修改用户自定义转动图模板。

        :param request: Request instance for ModifyAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAnimatedGraphicsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAnimatedGraphicsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAsrHotwords(self, request):
        """智能字幕更新热词库接口

        :param request: Request instance for ModifyAsrHotwords.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAsrHotwordsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAsrHotwordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAsrHotwords", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAsrHotwordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyContentReviewTemplate(self, request):
        """修改用户自定义内容审核模板。

        :param request: Request instance for ModifyContentReviewTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyContentReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyContentReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageSpriteTemplate(self, request):
        """修改用户自定义雪碧图模板。

        :param request: Request instance for ModifyImageSpriteTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageSpriteTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageSpriteTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveRecordTemplate(self, request):
        """修改直播录制模板

        :param request: Request instance for ModifyLiveRecordTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPersonSample(self, request):
        """该接口用于根据素材 ID，修改素材样本信息，包括名称、描述的修改，以及五官、标签的添加、删除、重置操作。五官删除操作需保证至少剩余 1 张图片，否则，请使用重置操作。

        :param request: Request instance for ModifyPersonSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyPersonSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyPersonSampleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPersonSample", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPersonSampleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQualityControlTemplate(self, request):
        """修改媒体质检模板。

        :param request: Request instance for ModifyQualityControlTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyQualityControlTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyQualityControlTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQualityControlTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQualityControlTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySampleSnapshotTemplate(self, request):
        """修改用户自定义采样截图模板。

        :param request: Request instance for ModifySampleSnapshotTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifySampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifySampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySampleSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySampleSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySchedule(self, request):
        """修改编排

        :param request: Request instance for ModifySchedule.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyScheduleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySchedule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySmartSubtitleTemplate(self, request):
        """修改用户自定义智能字幕模板。

        :param request: Request instance for ModifySmartSubtitleTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifySmartSubtitleTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifySmartSubtitleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySmartSubtitleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySmartSubtitleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshotByTimeOffsetTemplate(self, request):
        """修改用户自定义指定时间点截图模板。

        :param request: Request instance for ModifySnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifySnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifySnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshotByTimeOffsetTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotByTimeOffsetTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamLinkEvent(self, request):
        """修改媒体传输的事件配置信息。

        :param request: Request instance for ModifyStreamLinkEvent.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyStreamLinkEventRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyStreamLinkEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLinkEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLinkEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamLinkFlow(self, request):
        """修改媒体传输的传输流配置信息。

        :param request: Request instance for ModifyStreamLinkFlow.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamLinkInput(self, request):
        """修改媒体传输流的输入信息。

        :param request: Request instance for ModifyStreamLinkInput.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyStreamLinkInputRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyStreamLinkInputResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLinkInput", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLinkInputResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamLinkOutputInfo(self, request):
        """修改媒体传输流的输出配置。

        :param request: Request instance for ModifyStreamLinkOutputInfo.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyStreamLinkOutputInfoRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyStreamLinkOutputInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLinkOutputInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLinkOutputInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamLinkSecurityGroup(self, request):
        """更新安全组。

        :param request: Request instance for ModifyStreamLinkSecurityGroup.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyStreamLinkSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyStreamLinkSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLinkSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLinkSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTranscodeTemplate(self, request):
        """修改用户自定义转码模板信息。

        :param request: Request instance for ModifyTranscodeTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWatermarkTemplate(self, request):
        """修改用户自定义水印模板，水印类型不允许修改。

        :param request: Request instance for ModifyWatermarkTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWatermarkTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWatermarkTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWordSample(self, request):
        """该接口用于修改关键词的应用场景、标签，关键词本身不可修改，如需修改，可删除重建。

        :param request: Request instance for ModifyWordSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyWordSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyWordSampleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWordSample", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWordSampleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ParseLiveStreamProcessNotification(self, request):
        """从 CMQ 获取到消息后，从消息的 msgBody 字段中解析出 MPS 直播流处理事件通知的内容。
        该接口不用于发起网络调用，而是用来帮助生成各个语言平台的 SDK，您可以参考 SDK 中的解析实现事件通知的解析。

        :param request: Request instance for ParseLiveStreamProcessNotification.
        :type request: :class:`tencentcloud.mps.v20190612.models.ParseLiveStreamProcessNotificationRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ParseLiveStreamProcessNotificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ParseLiveStreamProcessNotification", params, headers=headers)
            response = json.loads(body)
            model = models.ParseLiveStreamProcessNotificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ParseNotification(self, request):
        """从 CMQ 获取到消息后，从消息的 msgBody 字段中解析出 MPS 事件通知的内容。
        该接口不用于发起网络调用，而是用来帮助生成各个语言平台的 SDK，您可以参考 SDK 中的解析函数，实现事件通知的解析。

        :param request: Request instance for ParseNotification.
        :type request: :class:`tencentcloud.mps.v20190612.models.ParseNotificationRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ParseNotificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ParseNotification", params, headers=headers)
            response = json.loads(body)
            model = models.ParseNotificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessImage(self, request):
        """发起图片处理，功能包括：
        1. 格式转换；
        2. 图像增强；
        3. 图像擦除;

        :param request: Request instance for ProcessImage.
        :type request: :class:`tencentcloud.mps.v20190612.models.ProcessImageRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ProcessImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessImage", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessLiveStream(self, request):
        """对直播流媒体发起处理任务，功能包括：

        * 智能内容审核（画面鉴黄、敏感信息检测、声音鉴黄）；
        * 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词、语音实时翻译、物体识别、游戏打点）。
        * 智能内容分析（新闻实时拆条）。
        * 质检（直播流格式诊断、音画内容检测（抖动、模糊、低光照、过曝光、黑边、白边、黑屏、白屏、花屏、噪点、马赛克、二维码等）、无参考打分）。
        * 录制

        直播流处理事件通知支持HTTP回调，也支持实时写入用户指定的消息队列 CMQ 中，用户从消息队列 CMQ 中获取事件通知结果，同时处理过程中存在输出文件的，会写入用户指定的输出文件的目标存储中。

        :param request: Request instance for ProcessLiveStream.
        :type request: :class:`tencentcloud.mps.v20190612.models.ProcessLiveStreamRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ProcessLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessMedia(self, request):
        """对 URL视频链接 或 COS 中的媒体文件发起处理任务，功能包括：
        1. 视频转码（普通转码、极速高清转码、音视频增强）；
        2. 视频转动图；
        3. 对视频按指定时间点截图；
        4. 对视频采样截图；
        5. 对视频截图雪碧图；
        6. 对视频转自适应码流；
        7. 智能内容审核（鉴黄、敏感信息检测）；
        8. 智能内容分析（标签、分类、封面、按帧标签、拆条、集锦、片头片尾、游戏打点）；
        9. 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词、语音翻译、物体识别）。
        10. 媒体质检（直播流格式诊断、音画内容检测（抖动、模糊、低光照、过曝光、黑边、白边、黑屏、白屏、花屏、噪点、马赛克、二维码等）、无参考打分）
        11. 智能字幕（语音全文、语音热词、语音翻译）

        :param request: Request instance for ProcessMedia.
        :type request: :class:`tencentcloud.mps.v20190612.models.ProcessMediaRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ProcessMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMedia", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeMediaForZhiXue(self, request):
        """智能媒体识别，包含表情和动作识别。仅用于智学，其他调用无效。

        :param request: Request instance for RecognizeMediaForZhiXue.
        :type request: :class:`tencentcloud.mps.v20190612.models.RecognizeMediaForZhiXueRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.RecognizeMediaForZhiXueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeMediaForZhiXue", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeMediaForZhiXueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetWorkflow(self, request):
        """重新设置一个已经存在且处于禁用状态的工作流。

        :param request: Request instance for ResetWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.ResetWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ResetWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.ResetWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartStreamLinkFlow(self, request):
        """启动媒体传输流。

        :param request: Request instance for StartStreamLinkFlow.
        :type request: :class:`tencentcloud.mps.v20190612.models.StartStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.StartStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.StartStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopStreamLinkFlow(self, request):
        """停止媒体传输流。

        :param request: Request instance for StopStreamLinkFlow.
        :type request: :class:`tencentcloud.mps.v20190612.models.StopStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.StopStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.StopStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def WithdrawsWatermark(self, request):
        """提取视频中的盲水印。

        :param request: Request instance for WithdrawsWatermark.
        :type request: :class:`tencentcloud.mps.v20190612.models.WithdrawsWatermarkRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.WithdrawsWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("WithdrawsWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.WithdrawsWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))