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
from tencentcloud.vod.v20180717 import models


class VodClient(AbstractClient):
    _apiVersion = '2018-07-17'
    _endpoint = 'vod.tencentcloudapi.com'
    _service = 'vod'


    def ApplyUpload(self, request):
        """* 我们强烈建议您使用云点播提供的 [服务端上传 SDK](/document/product/266/9759#1.-.E5.8F.91.E8.B5.B7.E4.B8.8A.E4.BC.A0) 来上传文件。直接调用 API 进行上传的难度和工作量都显著大于使用 SDK。
        * 该接口用于申请媒体文件（和封面文件）的上传，获取文件上传到云点播的元信息（包括上传路径、上传签名等），用于后续上传接口。
        * 上传流程请参考 [服务端上传综述](/document/product/266/9759)。

        :param request: Request instance for ApplyUpload.
        :type request: :class:`tencentcloud.vod.v20180717.models.ApplyUploadRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ApplyUploadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyUpload", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyUploadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachMediaSubtitles(self, request):
        """关联媒资字幕，将指定的字幕关联到转自适应码流模板号对应的媒体输出文件中（或解除关联）。

        :param request: Request instance for AttachMediaSubtitles.
        :type request: :class:`tencentcloud.vod.v20180717.models.AttachMediaSubtitlesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.AttachMediaSubtitlesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachMediaSubtitles", params, headers=headers)
            response = json.loads(body)
            model = models.AttachMediaSubtitlesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitUpload(self, request):
        """该接口用于确认媒体文件（和封面文件）上传到腾讯云点播的结果，并存储媒体信息，返回文件的播放地址和文件 ID。

        :param request: Request instance for CommitUpload.
        :type request: :class:`tencentcloud.vod.v20180717.models.CommitUploadRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CommitUploadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitUpload", params, headers=headers)
            response = json.loads(body)
            model = models.CommitUploadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ComposeMedia(self, request):
        """该接口用于合成媒体文件，可以达到以下效果：

        1. **画面旋转**：对视频、图片的画面旋转一定角度，或按照某个方向翻转。
        2. **声音控制**：升高降低视频、音频中声音的音量，或者对视频静音。
        3. **画面叠加**：将视频、图片中的画面依序叠加在一起，如实现“画中画”的效果。
        4. **声音混合**：将视频、音频中的声音混合在一起（混音）。
        5. **声音提取**：将视频中的音频提取出来（不保留画面）。
        6. **裁剪**：对视频、音频裁剪出指定时间段。
        7. **拼接**：对视频、音频、图片按时间顺序前后拼接。
        8. **转场**：将多段视频或图片拼接时，可以在段落之间添加转场效果。

        合成后的媒体封装格式可以是 MP4（视频）或 MP3（音频）。如使用事件通知，事件通知的类型为 [视频合成完成](https://cloud.tencent.com/document/product/266/43000)。

        :param request: Request instance for ComposeMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.ComposeMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ComposeMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ComposeMedia", params, headers=headers)
            response = json.loads(body)
            model = models.ComposeMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfirmEvents(self, request):
        """* 开发者调用拉取事件通知，获取到事件后，必须调用该接口来确认消息已经收到；
        * 开发者获取到事件句柄后，等待确认的有效时间为 30 秒，超出 30 秒会报参数错误（4000）；
        * 更多参考事件通知的[可靠回调](https://cloud.tencent.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83)。

        :param request: Request instance for ConfirmEvents.
        :type request: :class:`tencentcloud.vod.v20180717.models.ConfirmEventsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ConfirmEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIAnalysisTemplate(self, request):
        """创建用户自定义音视频内容分析模板，数量上限：50。

        :param request: Request instance for CreateAIAnalysisTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAIAnalysisTemplateResponse`

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
        """创建用户自定义音视频内容识别模板，数量上限：50。

        :param request: Request instance for CreateAIRecognitionTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAIRecognitionTemplateResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAdaptiveDynamicStreamingTemplateResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateAnimatedGraphicsTemplateResponse`

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


    def CreateCLSLogset(self, request):
        """由 VOD 创建新的日志集。

        :param request: Request instance for CreateCLSLogset.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateCLSLogsetRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateCLSLogsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCLSLogset", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCLSLogsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCLSTopic(self, request):
        """创建 VOD 下新的 CLS 日志主题

        :param request: Request instance for CreateCLSTopic.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateCLSTopicRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateCLSTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCLSTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCLSTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClass(self, request):
        """* 用于对媒体进行分类管理；
        * 该接口不影响既有媒体的分类，如需修改媒体分类，请调用[修改媒体文件属性](/document/product/266/31762)接口。
        * 分类层次不可超过 4 层。
        * 每个分类的子类数量不可超过 500 个。

        :param request: Request instance for CreateClass.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateClassRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClass", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateContentReviewTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版审核模板支持音视频审核和图片审核，详细请参考 [创建审核模板](https://cloud.tencent.com/document/api/266/84391)。
        创建用户自定义音视频内容审核模板，数量上限：50。

        :param request: Request instance for CreateContentReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateContentReviewTemplateResponse`

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


    def CreateDomainVerifyRecord(self, request):
        """该接口用于生成一条子域名解析，提示客户添加到域名解析上，用于泛域名及域名取回校验归属权。

        :param request: Request instance for CreateDomainVerifyRecord.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateDomainVerifyRecordRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateDomainVerifyRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainVerifyRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainVerifyRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEnhanceMediaTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        创建音画质重生模板。

        :param request: Request instance for CreateEnhanceMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateEnhanceMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateEnhanceMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnhanceMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnhanceMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHeadTailTemplate(self, request):
        """创建片头片尾模板。
        - 最大支持模板数量为 100 个。

        :param request: Request instance for CreateHeadTailTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateHeadTailTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateHeadTailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHeadTailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHeadTailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageProcessingTemplate(self, request):
        """创建一个用户自定义的图片处理模板，数量上限：16。最多支持十次操作，例如：裁剪-缩略-裁剪-模糊-缩略-裁剪-缩略-裁剪-模糊-缩略。

        :param request: Request instance for CreateImageProcessingTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateImageProcessingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateImageProcessingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageProcessingTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageProcessingTemplateResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateImageSpriteTemplateResponse`

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


    def CreateJustInTimeTranscodeTemplate(self, request):
        """创建即时转码模板。

        :param request: Request instance for CreateJustInTimeTranscodeTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateJustInTimeTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateJustInTimeTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJustInTimeTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJustInTimeTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePersonSample(self, request):
        """该接口用于创建素材样本，用于通过五官定位等技术，进行内容识别、不适宜视频识别等视频处理。

        :param request: Request instance for CreatePersonSample.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreatePersonSampleRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreatePersonSampleResponse`

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


    def CreateProcedureTemplate(self, request):
        """创建用户自定义的任务流模板，模板上限：50。

        :param request: Request instance for CreateProcedureTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateProcedureTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProcedureTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProcedureTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQualityInspectTemplate(self, request):
        """创建音画质检测模板。

        :param request: Request instance for CreateQualityInspectTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateQualityInspectTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateQualityInspectTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQualityInspectTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQualityInspectTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRebuildMediaTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        创建视频重生模板。

        :param request: Request instance for CreateRebuildMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateRebuildMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateRebuildMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRebuildMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRebuildMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReviewTemplate(self, request):
        """创建用户自定义审核模板，数量上限：50。
        >模板仅适用于 [音视频审核(ReviewAudioVideo)](https://cloud.tencent.com/document/api/266/80283) 和 [图片审核(ReviewImage)](https://cloud.tencent.com/document/api/266/73217) 接口。

        :param request: Request instance for CreateReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoundPlay(self, request):
        """该接口用于创建轮播播单，数量上限：100。
        轮播播单的每个文件可以指定源文件，也可以指定某个转码文件。
        指定的文件必须是hls格式，所有的播单文件最好保持相同的码率和分辨率。

        :param request: Request instance for CreateRoundPlay.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateRoundPlayRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateRoundPlayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoundPlay", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoundPlayResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateSampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateSampleSnapshotTemplateResponse`

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


    def CreateSnapshotByTimeOffsetTemplate(self, request):
        """创建用户自定义指定时间点截图模板，数量上限：16。

        :param request: Request instance for CreateSnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateSnapshotByTimeOffsetTemplateResponse`

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


    def CreateStorageRegion(self, request):
        """该接口用于开通某地域的存储。
          1. 用户开通点播业务时，系统默认为用户开通了部分地域的存储，用户如果需要开通其它地域的存储，可以通过该接口进行开通。
          2. 通过 DescribeStorageRegions 接口可以查询到所有存储地域及已经开通的地域。

        :param request: Request instance for CreateStorageRegion.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateStorageRegionRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateStorageRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStorageRegion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStorageRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubAppId(self, request):
        """该接口用于创建点播应用。

        :param request: Request instance for CreateSubAppId.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateSubAppIdRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateSubAppIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubAppId", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubAppIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSuperPlayerConfig(self, request):
        """该 API 已经<font color='red'>不再维护</font>，新版播放器签名不再使用播放器配置模板，详细请参考 [播放器签名](https://cloud.tencent.com/document/product/266/45554)。
        创建播放器配置，数量上限：100。

        :param request: Request instance for CreateSuperPlayerConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateSuperPlayerConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateSuperPlayerConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSuperPlayerConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSuperPlayerConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTranscodeTemplate(self, request):
        """创建用户自定义转码模板，数量上限：100。

        :param request: Request instance for CreateTranscodeTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateTranscodeTemplateResponse`

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


    def CreateVodDomain(self, request):
        """该接口用于将加速域名添加到点播，一个用户最多添加20个加速域名。
        1.域名添加成功后点播会进行域名的部署，域名由部署状态变为在线状态大概需要2分钟的时间。

        :param request: Request instance for CreateVodDomain.
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateVodDomainRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateVodDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVodDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVodDomainResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateWatermarkTemplateResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.CreateWordSamplesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.CreateWordSamplesResponse`

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


    def DeleteAIAnalysisTemplate(self, request):
        """删除用户自定义音视频内容分析模板。

        注意：模板 ID 为 10000 以下的为系统预置模板，不允许删除。

        :param request: Request instance for DeleteAIAnalysisTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAIAnalysisTemplateResponse`

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
        """删除用户自定义音视频内容识别模板。

        :param request: Request instance for DeleteAIRecognitionTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAIRecognitionTemplateResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAdaptiveDynamicStreamingTemplateResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteAnimatedGraphicsTemplateResponse`

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


    def DeleteCLSTopic(self, request):
        """删除点播开通的日志主题。

        :param request: Request instance for DeleteCLSTopic.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteCLSTopicRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteCLSTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCLSTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCLSTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClass(self, request):
        """* 仅当待删分类无子分类且无媒体关联情况下，可删除分类；
        * 否则，请先执行[删除媒体](/document/product/266/31764)及子分类，再删除该分类；

        :param request: Request instance for DeleteClass.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteClassRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClass", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteContentReviewTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版审核模板支持音视频审核和图片审核，详细请参考 [删除审核模板](https://cloud.tencent.com/document/api/266/84390)。
        删除用户自定义音视频内容审核模板。

        :param request: Request instance for DeleteContentReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteContentReviewTemplateResponse`

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


    def DeleteEnhanceMediaTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        删除音画质重生模板。

        :param request: Request instance for DeleteEnhanceMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteEnhanceMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteEnhanceMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEnhanceMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEnhanceMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHeadTailTemplate(self, request):
        """删除片头片尾模板。

        :param request: Request instance for DeleteHeadTailTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteHeadTailTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteHeadTailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHeadTailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHeadTailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageProcessingTemplate(self, request):
        """删除用户自定义图片处理模板。

        :param request: Request instance for DeleteImageProcessingTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteImageProcessingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteImageProcessingTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageProcessingTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageProcessingTemplateResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteImageSpriteTemplateResponse`

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


    def DeleteJustInTimeTranscodeTemplate(self, request):
        """删除即时转码模板。

        :param request: Request instance for DeleteJustInTimeTranscodeTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteJustInTimeTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteJustInTimeTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteJustInTimeTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteJustInTimeTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMedia(self, request):
        """* 删除媒体及其对应的视频处理文件（原始文件、如转码视频、雪碧图、截图、微信发布视频等）；
        * 可单独删除指定 ID 的视频文件下的原文件、转码视频、微信发布视频等；
        * 注意：原文件删除后，无法发起转码、微信发布等任何视频处理操作。

        :param request: Request instance for DeleteMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMedia", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePersonSample(self, request):
        """该接口用于根据人物 ID，删除素材样本。

        :param request: Request instance for DeletePersonSample.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeletePersonSampleRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeletePersonSampleResponse`

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


    def DeleteProcedureTemplate(self, request):
        """删除用户自定义的任务流模板。

        :param request: Request instance for DeleteProcedureTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteProcedureTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProcedureTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProcedureTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQualityInspectTemplate(self, request):
        """删除音画质检测模板。

        :param request: Request instance for DeleteQualityInspectTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteQualityInspectTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteQualityInspectTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQualityInspectTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQualityInspectTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRebuildMediaTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        删除视频重生模板。

        :param request: Request instance for DeleteRebuildMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteRebuildMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteRebuildMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRebuildMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRebuildMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReviewTemplate(self, request):
        """删除用户自定义审核模板。
        >模板仅适用于 [音视频审核(ReviewAudioVideo)](https://cloud.tencent.com/document/api/266/80283) 和 [图片审核(ReviewImage)](https://cloud.tencent.com/document/api/266/73217) 接口。

        :param request: Request instance for DeleteReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoundPlay(self, request):
        """该接口用于删除轮播播单。

        :param request: Request instance for DeleteRoundPlay.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteRoundPlayRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteRoundPlayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoundPlay", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoundPlayResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteSampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteSampleSnapshotTemplateResponse`

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


    def DeleteSnapshotByTimeOffsetTemplate(self, request):
        """删除用户自定义指定时间点截图模板。

        :param request: Request instance for DeleteSnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteSnapshotByTimeOffsetTemplateResponse`

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


    def DeleteSuperPlayerConfig(self, request):
        """该 API 已经<font color='red'>不再维护</font>，新版播放器签名不再使用播放器配置模板，详细请参考 [播放器签名](https://cloud.tencent.com/document/product/266/45554)。
        删除播放器配置。
        *注：系统预置播放器配置不允许删除。*

        :param request: Request instance for DeleteSuperPlayerConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteSuperPlayerConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteSuperPlayerConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSuperPlayerConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSuperPlayerConfigResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteTranscodeTemplateResponse`

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


    def DeleteVodDomain(self, request):
        """该接口用于删除点播加速域名。
        1、域名删除前需要先关闭所有区域的加速。

        :param request: Request instance for DeleteVodDomain.
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteVodDomainRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteVodDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVodDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVodDomainResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteWatermarkTemplateResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.DeleteWordSamplesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteWordSamplesResponse`

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


    def DescribeAIAnalysisTemplates(self, request):
        """根据音视频内容分析模板唯一标识，获取音视频内容分析模板详情列表。返回结果包含符合条件的所有用户自定义音视频内容分析模板及[系统预置音视频内容分析模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.88.86.E6.9E.90.E6.A8.A1.E6.9D.BF)。

        :param request: Request instance for DescribeAIAnalysisTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAIAnalysisTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAIAnalysisTemplatesResponse`

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
        """根据音视频内容识别模板唯一标识，获取音视频内容识别模板详情列表。返回结果包含符合条件的所有用户自定义音视频内容识别模板及[系统预置音视频内容识别模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E8.AF.86.E5.88.AB.E6.A8.A1.E6.9D.BF)。

        :param request: Request instance for DescribeAIRecognitionTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAIRecognitionTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAIRecognitionTemplatesResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAdaptiveDynamicStreamingTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAdaptiveDynamicStreamingTemplatesResponse`

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


    def DescribeAllClass(self, request):
        """* 获得用户的所有分类信息。

        :param request: Request instance for DescribeAllClass.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAllClassRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAllClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllClass", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllClassResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeAnimatedGraphicsTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeAnimatedGraphicsTemplatesResponse`

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


    def DescribeCDNStatDetails(self, request):
        """该接口用于查询点播域名的 CDN 带宽、流量等统计数据。
        * 查询的起始时间和结束时间跨度不超过90天。
        * 可以查询不同服务区域的数据。
        * 中国境内的数据支持查询指定地区、运营商的统计数据。

        :param request: Request instance for DescribeCDNStatDetails.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCDNStatDetailsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCDNStatDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCDNStatDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCDNStatDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCDNUsageData(self, request):
        """该接口用于查询点播 CDN 的流量、带宽等统计数据。
           1. 可以查询最近365天内的 CDN 用量数据。
           2.  查询时间跨度不超过90天。
           3. 可以指定用量数据的时间粒度，支持5分钟、1小时、1天的时间粒度。
           4.  流量为查询时间粒度内的总流量，带宽为查询时间粒度内的峰值带宽。

        :param request: Request instance for DescribeCDNUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCDNUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCDNUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCDNUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCDNUsageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCLSLogsets(self, request):
        """查询 VOD 创建的 CLS 日志集。

        :param request: Request instance for DescribeCLSLogsets.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCLSLogsetsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCLSLogsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCLSLogsets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCLSLogsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCLSPushTargets(self, request):
        """查询点播域名下日志投递的目标主题。

        :param request: Request instance for DescribeCLSPushTargets.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCLSPushTargetsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCLSPushTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCLSPushTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCLSPushTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCLSTopics(self, request):
        """查询 VOD 创建的 CLS 日志主题列表。

        :param request: Request instance for DescribeCLSTopics.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCLSTopicsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCLSTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCLSTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCLSTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdnLogs(self, request):
        """查询点播域名的 CDN 访问日志的下载链接。
            1. 可以查询最近30天内的 CDN 日志下载链接。
            2. 默认情况下 CDN 每小时生成一个日志文件，如果某一个小时没有 CDN 访问，不会生成日志文件。
            3. CDN 日志下载链接的有效期为24小时。

        :param request: Request instance for DescribeCdnLogs.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCdnLogsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCdnLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdnLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdnLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientUploadAccelerationUsageData(self, request):
        """该接口返回查询时间范围内客户端上传加速统计信息。
           1. 可以查询最近365天内的客户端上传加速统计数据。
           2. 查询时间跨度不超过90天。
           3. 查询时间跨度超过1天的，返回以天为粒度的数据，否则，返回以5分钟为粒度的数据。

        :param request: Request instance for DescribeClientUploadAccelerationUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeClientUploadAccelerationUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeClientUploadAccelerationUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientUploadAccelerationUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientUploadAccelerationUsageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContentReviewTemplates(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版审核模板支持音视频审核和图片审核，详细请参考 [获取审核模板列表](https://cloud.tencent.com/document/api/266/84389)。
        根据音视频内容审核模板唯一标识，获取音视频内容审核模板详情列表。返回结果包含符合条件的所有用户自定义模板及[系统预置内容审核模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.AE.A1.E6.A0.B8.E6.A8.A1.E6.9D.BF)。

        :param request: Request instance for DescribeContentReviewTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeContentReviewTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeContentReviewTemplatesResponse`

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


    def DescribeCurrentPlaylist(self, request):
        """查询轮播当前播放列表。

        :param request: Request instance for DescribeCurrentPlaylist.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeCurrentPlaylistRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeCurrentPlaylistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCurrentPlaylist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCurrentPlaylistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDailyMediaPlayStat(self, request):
        """该接口用于查询指定日期范围内每天的播放统计数据。
        * 可以查询最近一年的播放统计数据。
        * 结束日期和起始日期的时间跨度最大为90天。

        :param request: Request instance for DescribeDailyMediaPlayStat.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDailyMediaPlayStatRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDailyMediaPlayStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDailyMediaPlayStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDailyMediaPlayStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDailyMostPlayedStat(self, request):
        """该接口用于查询每日播放Top100 的媒体文件的播放统计数据。
        * 可以查询最近一年的播放统计数据。
        * 可以按播放次数或者播放流量查询。
        * 播放次数统计说明：
            1. HLS 文件：访问 M3U8 文件时统计播放次数；访问 TS 文件不统计播放次数。
            2. 其它文件（如 MP4 文件）：播放请求带有 range 参数且 range 的 start 参数不等于0时不统计播放次数，其它情况统计播放次数。

        :param request: Request instance for DescribeDailyMostPlayedStat.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDailyMostPlayedStatRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDailyMostPlayedStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDailyMostPlayedStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDailyMostPlayedStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDailyPlayStatFileList(self, request):
        """该接口用于查询播放统计文件的下载地址。
        * 可以查询最近一年的播放统计文件下载地址，查询的起始日期和结束日期的时间跨度不超过90天。
        * 云点播每天对前一天的 CDN 请求日志进行分析处理，生成播放统计文件。
        * 播放统计文件内容包含媒体文件的播放次数、播放流量等统计信息。
        * 播放次数统计说明：
            1. HLS 文件：访问M3U8 文件时统计播放次数；访问TS 文件不统计播放次数。
            2. 其它文件（如 MP4 文件）：播放请求带有 range 参数且 range 的 start 参数不等于0时不统计播放次数，其它情况统计播放次数。
        * 播放设备的统计：播放请求带了 UserAgent 参数，并且 UserAgent 包含 Android 或者 iPhone 等标识，会统计为移动端播放次数，否则统计为 PC 端播放次数。

        :param request: Request instance for DescribeDailyPlayStatFileList.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDailyPlayStatFileListRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDailyPlayStatFileListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDailyPlayStatFileList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDailyPlayStatFileListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultDistributionConfig(self, request):
        """该接口用于查询默认分发配置。
        * 分发域名和分发协议，即媒体文件分发 URL 中的域名和协议。媒体文件按默认分发配置进行分发。
        * 播放密钥，用于计算播放器签名。

        :param request: Request instance for DescribeDefaultDistributionConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDefaultDistributionConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDefaultDistributionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultDistributionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultDistributionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDrmDataKey(self, request):
        """本 API 是 [旧版本加密](https://cloud.tencent.com/document/product/266/9638) 中 [DescribeDrmDataKey 的 API 2017 接口](https://cloud.tencent.com/document/product/266/9643) 的升级版本。

        如果您是新接入点播加密的用户，不要使用该 API，请参考 [视频加密综述](https://cloud.tencent.com/document/product/266/45552) 使用推荐的加密方式。

        :param request: Request instance for DescribeDrmDataKey.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDrmDataKeyRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDrmDataKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDrmDataKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDrmDataKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDrmKeyProviderInfo(self, request):
        """查询 DRM 密钥提供商信息。

        :param request: Request instance for DescribeDrmKeyProviderInfo.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeDrmKeyProviderInfoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeDrmKeyProviderInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDrmKeyProviderInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDrmKeyProviderInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnhanceMediaTemplates(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        获取音画质重生模板列表。

        :param request: Request instance for DescribeEnhanceMediaTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeEnhanceMediaTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeEnhanceMediaTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnhanceMediaTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnhanceMediaTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventConfig(self, request):
        """腾讯云点播为客户提供了媒体上传、媒体管理、媒体处理等等服务，在这些服务执行过程或执行结束时，腾讯云点播也提供各种对应的事件通知，方便开发者感知服务处理状态，并做下一步的业务操作。

        开发者可以通过本接口来查询当前配置事件通知的接收方式、接收地址以及哪些事件开启了接收回调通知。

        默认接口请求频率限制：100次/秒。

        :param request: Request instance for DescribeEventConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeEventConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeEventConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventsState(self, request):
        """* 该接口用于业务服务器获取 [可靠回调](https://cloud.tencent.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83) 事件通知的状态。

        :param request: Request instance for DescribeEventsState.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeEventsStateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeEventsStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventsState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventsStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileAttributes(self, request):
        """用于异步获取文件属性。
        - 当前仅支持获取源文件的 Md5、Sha1。
        - 对输入文件为 HLS 或 DASH 的情况，仅获取索引文件的属性。

        :param request: Request instance for DescribeFileAttributes.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeFileAttributesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeFileAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHeadTailTemplates(self, request):
        """获取片头片尾模板列表。

        :param request: Request instance for DescribeHeadTailTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeHeadTailTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeHeadTailTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHeadTailTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHeadTailTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageProcessingTemplates(self, request):
        """获取图片处理模板列表，支持根据条件，分页查询。

        :param request: Request instance for DescribeImageProcessingTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeImageProcessingTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeImageProcessingTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageProcessingTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageProcessingTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageReviewUsageData(self, request):
        """该接口返回查询时间范围内每天使用的图片审核用量信息。
           1. 可以查询最近365天内的图片审核统计数据。
           2. 查询时间跨度不超过90天。
           3. 查询时间跨度超过1天的，返回以天为粒度的数据，否则，返回以5分钟为粒度的数据。

        :param request: Request instance for DescribeImageReviewUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeImageReviewUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeImageReviewUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageReviewUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageReviewUsageDataResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeImageSpriteTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeImageSpriteTemplatesResponse`

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


    def DescribeJustInTimeTranscodeTemplates(self, request):
        """获取即时转码模板列表。

        :param request: Request instance for DescribeJustInTimeTranscodeTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeJustInTimeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeJustInTimeTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJustInTimeTranscodeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJustInTimeTranscodeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseUsageData(self, request):
        """该接口返回查询时间范围内每天 License 请求次数信息。
           1. 可以查询最近365天内的 License 请求次数统计数据。
           2. 查询时间跨度不超过90天。
           3. 查询时间跨度超过1天的，返回以天为粒度的数据，否则，返回以5分钟为粒度的数据。

        :param request: Request instance for DescribeLicenseUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeLicenseUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeLicenseUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseUsageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMediaInfos(self, request):
        """1. 该接口可以获取多个媒体文件的多种信息，包括：
            1. 基础信息（basicInfo）：包括媒体名称、分类、播放地址、封面图片等。
            2. 元信息（metaData）：包括大小、时长、视频流信息、音频流信息等。
            3. 转码结果信息（transcodeInfo）：包括该媒体转码生成的各种规格的媒体地址、视频流参数、音频流参数等。
            4. 转动图结果信息（animatedGraphicsInfo）：对视频转动图（如 gif）后的动图信息。
            5. 采样截图信息（sampleSnapshotInfo）：对视频采样截图后的截图信息。
            6. 雪碧图信息（imageSpriteInfo）：对视频截取雪碧图后的雪碧图信息。
            7. 指定时间点截图信息（snapshotByTimeOffsetInfo）：对视频依照指定时间点截图后，的截图信息。
            8. 视频打点信息（keyFrameDescInfo）：对视频设置的打点信息。
            9. 转自适应码流信息（adaptiveDynamicStreamingInfo）：包括规格、加密类型、打包格式等相关信息。
            10. 审核信息（reviewInfo）：包括媒体审核及媒体封面审核信息。
        2. 可以指定回包只返回部分信息。

        :param request: Request instance for DescribeMediaInfos.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeMediaInfosRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeMediaInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMediaInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMediaInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMediaPlayStatDetails(self, request):
        """该接口用于查询媒体文件按指定时间粒度统计的播放数据
        * 可以查询最近一年的播放统计数据。
        * 时间粒度为小时，结束时间和起始时间的跨度最大为7天。
        * 时间粒度为天，结束时间和起始时间的跨度最大为90天。

        :param request: Request instance for DescribeMediaPlayStatDetails.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeMediaPlayStatDetailsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeMediaPlayStatDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMediaPlayStatDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMediaPlayStatDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMediaProcessUsageData(self, request):
        """该接口返回查询时间范围内每天使用的视频处理用量信息。
           1. 可以查询最近365天内的视频处理统计数据。
           2. 查询时间跨度不超过90天。

        :param request: Request instance for DescribeMediaProcessUsageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeMediaProcessUsageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeMediaProcessUsageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMediaProcessUsageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMediaProcessUsageDataResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribePersonSamplesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribePersonSamplesResponse`

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


    def DescribePrepaidProducts(self, request):
        """该接口可以查询用户已经购买的预付费商品的信息，包括：
            1. 商品的类型、生效和失效日期。
            2. 商品中每种资源的额度和剩余额度。

        :param request: Request instance for DescribePrepaidProducts.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribePrepaidProductsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribePrepaidProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrepaidProducts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrepaidProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcedureTemplates(self, request):
        """根据任务流模板名字，获取任务流模板详情列表。

        :param request: Request instance for DescribeProcedureTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeProcedureTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeProcedureTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcedureTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcedureTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQualityInspectTemplates(self, request):
        """获取音画质检测模板列表。

        :param request: Request instance for DescribeQualityInspectTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeQualityInspectTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeQualityInspectTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityInspectTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityInspectTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRebuildMediaTemplates(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        获取视频重生模板列表。

        :param request: Request instance for DescribeRebuildMediaTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeRebuildMediaTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeRebuildMediaTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRebuildMediaTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRebuildMediaTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReviewDetails(self, request):
        """<b>本接口已不推荐使用，用 [DescribeMediaProcessUsageData](/document/product/266/41464) 替代</b>

        该接口返回查询时间范围内每天使用的视频内容智能识别时长数据，单位： 秒。

        1. 可以查询最近365天内的视频内容智能识别时长统计数据。
        2. 查询时间跨度不超过90天。

        :param request: Request instance for DescribeReviewDetails.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeReviewDetailsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeReviewDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReviewDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReviewDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReviewTemplates(self, request):
        """获取审核模板列表。
        >模板仅适用于 [音视频审核(ReviewAudioVideo)](https://cloud.tencent.com/document/api/266/80283) 和 [图片审核(ReviewImage)](https://cloud.tencent.com/document/api/266/73217) 接口。

        :param request: Request instance for DescribeReviewTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeReviewTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeReviewTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReviewTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReviewTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoundPlays(self, request):
        """该接口用于获取轮播播单列表。

        :param request: Request instance for DescribeRoundPlays.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeRoundPlaysRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeRoundPlaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoundPlays", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoundPlaysResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeSampleSnapshotTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeSampleSnapshotTemplatesResponse`

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


    def DescribeSnapshotByTimeOffsetTemplates(self, request):
        """查询指定时间点截图模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeSnapshotByTimeOffsetTemplates.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeSnapshotByTimeOffsetTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeSnapshotByTimeOffsetTemplatesResponse`

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


    def DescribeStorageData(self, request):
        """查询存储空间使用情况和文件数量。

        :param request: Request instance for DescribeStorageData.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeStorageDataRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeStorageDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorageData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStorageDetails(self, request):
        """该接口返回查询时间范围内使用的点播存储空间，单位：字节。
            1. 可以查询最近365天内的存储空间数据；
            2. 查询时间跨度不超过90天；
            3. 分钟粒度查询跨度不超过7天；

        :param request: Request instance for DescribeStorageDetails.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeStorageDetailsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeStorageDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorageDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStorageRegions(self, request):
        """该接口用于：
          1. 查询点播可开通的所有存储园区列表。
          2. 查询已经开通的园区列表。
          3. 查询默认使用的存储园区。

        :param request: Request instance for DescribeStorageRegions.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeStorageRegionsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeStorageRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorageRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubAppIds(self, request):
        """该接口用于获取当前账号的应用列表。

        :param request: Request instance for DescribeSubAppIds.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeSubAppIdsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeSubAppIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubAppIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubAppIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSuperPlayerConfigs(self, request):
        """该 API 已经<font color='red'>不再维护</font>，新版播放器签名不再使用播放器配置模板，详细请参考 [播放器签名](https://cloud.tencent.com/document/product/266/45554)。
        查询播放器配置，支持根据条件，分页查询。

        :param request: Request instance for DescribeSuperPlayerConfigs.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeSuperPlayerConfigsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeSuperPlayerConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSuperPlayerConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSuperPlayerConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskDetail(self, request):
        """通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询3天之内提交的任务）。

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeTaskDetailResponse`

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
        * 只能查询到最近三天（72 小时）内的任务。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeTasksResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeTranscodeTemplatesResponse`

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


    def DescribeVodDomains(self, request):
        """该接口用于查询点播域名信息列表。

        :param request: Request instance for DescribeVodDomains.
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeVodDomainsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeVodDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVodDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVodDomainsResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeWatermarkTemplatesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeWatermarkTemplatesResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.DescribeWordSamplesRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeWordSamplesResponse`

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


    def EditMedia(self, request):
        """对视频进行编辑（剪辑、拼接等），生成一个新的点播视频。编辑的功能包括：

        1. 对点播中的一个文件进行剪辑，生成一个新的视频；
        2. 对点播中的多个文件进行拼接，生成一个新的视频；
        3. 对点播中的多个文件进行剪辑，然后再拼接，生成一个新的视频；
        4. 对点播中的一个流，直接生成一个新的视频；
        5. 对点播中的一个流进行剪辑，生成一个新的视频；
        6. 对点播中的多个流进行拼接，生成一个新的视频；
        7. 对点播中的多个流进行剪辑，然后拼接，生成一个新的视频。

        对于生成的新视频，还可以指定生成后的视频是否要执行任务流。

        >当对直播流做剪辑、拼接等操作时，请确保流结束后再操作。否则生成的视频可能不完整。

        如使用事件通知，事件通知的类型为 [视频编辑完成](https://cloud.tencent.com/document/product/266/33794)。

        :param request: Request instance for EditMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.EditMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.EditMediaResponse`

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


    def EnhanceMediaByTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，请使用新版接口 [音画质重生](https://cloud.tencent.com/document/api/266/102571)。
        使用模板发起音画质重生。

        :param request: Request instance for EnhanceMediaByTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.EnhanceMediaByTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.EnhanceMediaByTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnhanceMediaByTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.EnhanceMediaByTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnhanceMediaQuality(self, request):
        """对点播中的音视频媒体发起音画质重生任务。

        :param request: Request instance for EnhanceMediaQuality.
        :type request: :class:`tencentcloud.vod.v20180717.models.EnhanceMediaQualityRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.EnhanceMediaQualityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnhanceMediaQuality", params, headers=headers)
            response = json.loads(body)
            model = models.EnhanceMediaQualityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteFunction(self, request):
        """本接口仅用于定制开发的特殊场景，除非云点播客服人员主动告知您需要使用本接口，其它情况请勿调用。

        :param request: Request instance for ExecuteFunction.
        :type request: :class:`tencentcloud.vod.v20180717.models.ExecuteFunctionRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ExecuteFunctionResponse`

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


    def ExtractCopyRightWatermark(self, request):
        """该 API 已经<font color='red'>不再维护</font>。如果有盗录溯源需求，请参考 [幽灵水印](https://cloud.tencent.com/document/product/266/94228)。

        :param request: Request instance for ExtractCopyRightWatermark.
        :type request: :class:`tencentcloud.vod.v20180717.models.ExtractCopyRightWatermarkRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ExtractCopyRightWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExtractCopyRightWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.ExtractCopyRightWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExtractTraceWatermark(self, request):
        """该 API 已经<font color='red'>不再维护</font>。如果有盗录溯源需求，请参考 [幽灵水印](https://cloud.tencent.com/document/product/266/94228)。

        :param request: Request instance for ExtractTraceWatermark.
        :type request: :class:`tencentcloud.vod.v20180717.models.ExtractTraceWatermarkRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ExtractTraceWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExtractTraceWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.ExtractTraceWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FastEditMedia(self, request):
        """对云点播的 HLS 视频实现快速拼接和快速剪辑，生成新的 HLS 格式的媒体。

        快速拼接或剪辑生成的视频，将产生新的 FileId 并进行固化，固化成功后新视频的文件独立于原始输入视频存在，不受原始视频删除等影响。

        <font color='red'>注意：</font>通过 ModifyEventConfig 接口启用接收剪辑固化事件通知，固化成功后将会收到一个 PersitenceComplete 类型的事件通知。在收到这个事件通知之前，不应该对原始输入的视频进行删除、降冷等操作，否则拼接剪辑生成的视频播放可能出现异常。

        :param request: Request instance for FastEditMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.FastEditMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.FastEditMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FastEditMedia", params, headers=headers)
            response = json.loads(body)
            model = models.FastEditMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForbidMediaDistribution(self, request):
        """* 对媒体禁播后，除了点播控制台预览，其他场景访问视频各种资源的 URL（原始文件、转码输出文件、截图等）均会返回 403。
          禁播/解禁操作全网生效时间约 5~10 分钟。
        * 注意：禁播媒体仅能操作标准存储和低频存储的媒体。低频存储媒体，必须存储至少 30 天，提前删除或变更存储类型，仍旧按照 30 天计费；如果禁播低频存储媒体，该媒体低频存储的时长不足 30 天，会产生提前删除计费；同时，禁播后该媒体的低频存储时长会从当前时间重新开始计算，如果不满 30 天继续对该媒体进行删除或变更存储类型，也将产生提前删除计费。例：媒体 001 已经低频存储了 10 天，此时对 001 进行禁播，低频存储的计费仍旧按 30 天计算（提前删除计费时长为 30 - 10 = 20 天）；禁播后 001 的低频存储时长重新开始计算，如果禁播后第 5 天删除了 001，低频存储计费也会按 30 天计算（提前删除计费时长为 30 - 5 = 25 天）；001 实际的低频存储时长为 10 + 5 = 15 天，低频存储计费时长为 10 + 20(提前删除计费)+ 5 + 25(提前删除计费) = 60 天。

        :param request: Request instance for ForbidMediaDistribution.
        :type request: :class:`tencentcloud.vod.v20180717.models.ForbidMediaDistributionRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ForbidMediaDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForbidMediaDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.ForbidMediaDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HandleCurrentPlaylist(self, request):
        """操作轮播当前播放列表。支持的操作有：<li> Insert：向当前播列表插入播放节目。</li><li> Delete：删除播列表中的播放节目。</li>

        :param request: Request instance for HandleCurrentPlaylist.
        :type request: :class:`tencentcloud.vod.v20180717.models.HandleCurrentPlaylistRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.HandleCurrentPlaylistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HandleCurrentPlaylist", params, headers=headers)
            response = json.loads(body)
            model = models.HandleCurrentPlaylistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InspectMediaQuality(self, request):
        """对点播中的音视频媒体发起音画质检测任务。

        :param request: Request instance for InspectMediaQuality.
        :type request: :class:`tencentcloud.vod.v20180717.models.InspectMediaQualityRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.InspectMediaQualityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InspectMediaQuality", params, headers=headers)
            response = json.loads(body)
            model = models.InspectMediaQualityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LiveRealTimeClip(self, request):
        """直播即时剪辑，是指在直播过程中（即直播尚未结束时），客户可以在过往直播内容中选择一段，实时生成一个新的视频（HLS 格式），开发者可以将其立即分享出去，或者长久保存起来。

        腾讯云点播支持两种即时剪辑模式：
        - 剪辑固化：将剪辑出来的视频保存成独立的视频，拥有独立 FileId；适用于将精彩片段**长久保存**的场景；
        - 剪辑不固化：剪辑得到的视频附属于直播录制文件，没有独立 FileId；适用于将精彩片段**临时分享**的场景。

        注意：
        - 使用直播即时剪辑功能的前提是：目标直播流开启了[时移回看](https://cloud.tencent.com/document/product/267/32742)功能。
        - 直播即时剪辑是基于直播录制生成的 m3u8 文件进行的，故而其最小剪辑精度为一个 ts 切片，无法实现秒级或者更为精确的剪辑精度。
        - 由于直播过程中可能存在断流的情况，所以有可能导致剪辑生成的实际视频时长与期望不一致。例如剪辑某个直播流的时间区间为 2018-09-20T10:30:00Z 到 2018-09-20T10:40:00Z ，如果在该时间区间中发生过断流，那么返回的媒资文件的时长将少于 10 分钟，在这种情况下，可以通过输出参数 <a href="#p_segmentset">SegmentSet</a> 感知到。

        ### 剪辑固化
        所谓剪辑固化，是指将剪辑出来的视频是保存成一个独立的视频（拥有独立的 FileId）。其生命周期不受原始直播录制视频影响（即使原始录制视频被删除，剪辑结果也不会受到任何影响）；也可以对其进行转码、微信发布等二次处理。

        举例如下：一场完整的足球比赛，直播录制出来的原始视频可能长达 2 个小时，客户出于节省成本的目的可以对这个视频存储 2 个月，但对于直播即时剪辑的「精彩时刻」视频却可以指定存储更长时间，同时可以单独对「精彩时刻」视频进行转码、微信发布等额外的点播操作，这时候可以选择直播即时剪辑并且固化的方案。

        剪辑固化的优势在于其生命周期与原始录制视频相互独立，可以独立管理、长久保存。

        <font color='red'>注意：</font>如果剪辑时指定进行固化，通过 ModifyEventConfig 接口启用接收剪辑固化事件通知，固化成功后将会收到一个 PersitenceComplete 类型的事件通知。在收到这个事件通知之前，不应该对直播录制视频进行删除、降冷等操作，否则剪辑生成的视频播放可能出现异常。

        ### 剪辑不固化
        所谓剪辑不固化，是指剪辑所得到的结果（m3u8 文件）与直播录制视频共享相同的 ts 分片，新生成的视频不是一个独立完整的视频（没有独立 FileId，只有播放 URL），其有效期与直播录制的完整视频有效期是一致的。一旦直播录制出来的视频被删除，也会导致该片段无法播放。

        剪辑不固化，由于其剪辑结果不是一个独立的视频，因而也不会纳入点播媒资视频管理（例如控制台的视频总数不会统计这一片段）中，也无法单独针对这个片段做转码、微信发布等任何视频处理操作。

        剪辑不固化的优势在于其剪辑操作十分“轻量化”，不会产生额外的存储开销。但其不足之处在于生命周期与原始录制视频相同，且无法进一步进行转码等视频处理。

        :param request: Request instance for LiveRealTimeClip.
        :type request: :class:`tencentcloud.vod.v20180717.models.LiveRealTimeClipRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.LiveRealTimeClipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LiveRealTimeClip", params, headers=headers)
            response = json.loads(body)
            model = models.LiveRealTimeClipResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.ManageTaskRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ManageTaskResponse`

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
        """修改用户自定义音视频内容分析模板。

        注意：模板 ID 10000 以下的为系统预置模板，不允许修改。

        :param request: Request instance for ModifyAIAnalysisTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyAIAnalysisTemplateResponse`

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
        """修改用户自定义音视频内容识别模板。

        :param request: Request instance for ModifyAIRecognitionTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyAIRecognitionTemplateResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyAdaptiveDynamicStreamingTemplateResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyAnimatedGraphicsTemplateResponse`

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


    def ModifyClass(self, request):
        """修改媒体分类属性。

        :param request: Request instance for ModifyClass.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyClassRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClass", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyContentReviewTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版审核模板支持音视频审核和图片审核，详细请参考 [修改审核模板](https://cloud.tencent.com/document/api/266/84388)。
        修改用户自定义音视频内容审核模板。

        :param request: Request instance for ModifyContentReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyContentReviewTemplateResponse`

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


    def ModifyDefaultDistributionConfig(self, request):
        """该接口用于修改默认分发配置。
        * 分发域名和分发协议，即媒体文件分发 URL 中的域名和协议。媒体文件按默认分发配置进行分发。
        * 播放密钥，用于计算播放器签名。

        :param request: Request instance for ModifyDefaultDistributionConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyDefaultDistributionConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyDefaultDistributionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDefaultDistributionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDefaultDistributionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDefaultStorageRegion(self, request):
        """该接口用于设置默认的存储地域。上传文件时如果没有指定地域，将上传到默认地域。

        :param request: Request instance for ModifyDefaultStorageRegion.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyDefaultStorageRegionRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyDefaultStorageRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDefaultStorageRegion", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDefaultStorageRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnhanceMediaTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        修改音画质重生模板。

        :param request: Request instance for ModifyEnhanceMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyEnhanceMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyEnhanceMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnhanceMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnhanceMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEventConfig(self, request):
        """腾讯云点播为客户提供了媒体上传、媒体管理、媒体处理等等服务，在这些服务执行过程或执行结束时，腾讯云点播也提供各种对应的事件通知，方便开发者感知服务处理状态，并做下一步的业务操作。

        开发者可以通过调用本接口来实现：
        - 设置接收回调通知的类型，目前有[ HTTP 回调通知](https://cloud.tencent.com/document/product/266/33779) 和 [基于消息队列的可靠通知](https://cloud.tencent.com/document/product/266/33779) 两种类型。
        - 对于[ HTTP 回调通知](https://cloud.tencent.com/document/product/266/33779)，可设置 3.0 格式回调的地址。3.0 格式回调的说明参见 [历史格式回调](https://cloud.tencent.com/document/product/266/33796)。
        - 对具体事件服务的通知事件选择设置接收或者忽略。

        :param request: Request instance for ModifyEventConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyEventConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyEventConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEventConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEventConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHeadTailTemplate(self, request):
        """修改片头片尾模板。

        :param request: Request instance for ModifyHeadTailTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyHeadTailTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyHeadTailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHeadTailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHeadTailTemplateResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyImageSpriteTemplateResponse`

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


    def ModifyJustInTimeTranscodeTemplate(self, request):
        """修改即时转码模板。
        - 注意：即时转码模板创建后，不推荐修改，如需修改参数，推荐使用新增模板。

        :param request: Request instance for ModifyJustInTimeTranscodeTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyJustInTimeTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyJustInTimeTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyJustInTimeTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyJustInTimeTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMediaInfo(self, request):
        """修改媒体文件的属性，包括分类、名称、描述、标签、过期时间、打点信息、视频封面、字幕信息等。

        :param request: Request instance for ModifyMediaInfo.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyMediaInfoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyMediaInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMediaInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMediaInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMediaStorageClass(self, request):
        """修改媒体文件的存储类型。
        当媒体文件的存储类型为标准存储时，可以修改为以下类型：
        <li>低频存储</li>
        <li>归档存储</li>
        <li>深度归档存储</li>
        当媒体文件的当前存储类型为低频存储时，可以修改为以下类型：
        <li>标准存储</li>
        <li>归档存储</li>
        <li>深度归档存储</li>
        当媒体文件的当前存储类型为归档存储时，可以修改为以下类型：
        <li>标准存储</li>
        当媒体文件的当前存储类型为深度归档存储时，可以修改为以下类型：
        <li>标准存储</li>

        :param request: Request instance for ModifyMediaStorageClass.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyMediaStorageClassRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyMediaStorageClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMediaStorageClass", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMediaStorageClassResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyPersonSampleRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyPersonSampleResponse`

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


    def ModifyQualityInspectTemplate(self, request):
        """修改音画质检测模板。

        :param request: Request instance for ModifyQualityInspectTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyQualityInspectTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyQualityInspectTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQualityInspectTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQualityInspectTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRebuildMediaTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        修改视频重生模板。

        :param request: Request instance for ModifyRebuildMediaTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyRebuildMediaTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyRebuildMediaTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRebuildMediaTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRebuildMediaTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReviewTemplate(self, request):
        """修改用户自定义审核模板。
        >模板仅适用于 [音视频审核(ReviewAudioVideo)](https://cloud.tencent.com/document/api/266/80283) 和 [图片审核(ReviewImage)](https://cloud.tencent.com/document/api/266/73217) 接口。

        :param request: Request instance for ModifyReviewTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyReviewTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReviewTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReviewTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRoundPlay(self, request):
        """该接口用于修改轮播播单。
        修改后只有新的播放请求会生效，已经在播放中的用户在七天之内还可以播放修改前的播单。

        :param request: Request instance for ModifyRoundPlay.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyRoundPlayRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyRoundPlayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoundPlay", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoundPlayResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifySampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifySampleSnapshotTemplateResponse`

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


    def ModifySnapshotByTimeOffsetTemplate(self, request):
        """修改用户自定义指定时间点截图模板。

        :param request: Request instance for ModifySnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifySnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifySnapshotByTimeOffsetTemplateResponse`

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


    def ModifySubAppIdInfo(self, request):
        """该接口用于修改应用信息，但不允许修改默认应用信息。

        :param request: Request instance for ModifySubAppIdInfo.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifySubAppIdInfoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifySubAppIdInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubAppIdInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubAppIdInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubAppIdStatus(self, request):
        """该接口用于启用、停用应用。被停用的应用将封停对应域名，并限制控制台访问。

        :param request: Request instance for ModifySubAppIdStatus.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifySubAppIdStatusRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifySubAppIdStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubAppIdStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubAppIdStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySuperPlayerConfig(self, request):
        """该 API 已经<font color='red'>不再维护</font>，新版播放器签名不再使用播放器配置模板，详细请参考 [播放器签名](https://cloud.tencent.com/document/product/266/45554)。
        修改播放器配置。

        :param request: Request instance for ModifySuperPlayerConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifySuperPlayerConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifySuperPlayerConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySuperPlayerConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySuperPlayerConfigResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyTranscodeTemplateResponse`

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


    def ModifyVodDomainAccelerateConfig(self, request):
        """该接口用于修改点播域名的加速区域。
        1、域名部署状态为 Online 状态时才允许修改加速区域。

        :param request: Request instance for ModifyVodDomainAccelerateConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyVodDomainAccelerateConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyVodDomainAccelerateConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVodDomainAccelerateConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVodDomainAccelerateConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVodDomainConfig(self, request):
        """该接口用于修改域名配置，可以修改域名的防盗链配置。
        1、域名部署状态为 Online 状态时才允许修改域名的配置。

        :param request: Request instance for ModifyVodDomainConfig.
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyVodDomainConfigRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyVodDomainConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVodDomainConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVodDomainConfigResponse()
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
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyWatermarkTemplateResponse`

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
        :type request: :class:`tencentcloud.vod.v20180717.models.ModifyWordSampleRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyWordSampleResponse`

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


    def ParseStreamingManifest(self, request):
        """上传 HLS 视频时，解析索引文件内容，返回待上传的分片文件列表。分片文件路径必须是当前目录或子目录的相对路径，不能是 URL，不能是绝对路径。

        :param request: Request instance for ParseStreamingManifest.
        :type request: :class:`tencentcloud.vod.v20180717.models.ParseStreamingManifestRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ParseStreamingManifestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ParseStreamingManifest", params, headers=headers)
            response = json.loads(body)
            model = models.ParseStreamingManifestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessImage(self, request):
        """该 API 已经<font color='red'>不再维护</font>，智能识别任务请使用图片智能识别 [ReviewImage](https://cloud.tencent.com/document/api/266/73217) 接口。

        对点播中的图片文件发起处理任务，功能包括：

        1. 智能识别（令人反感的信息、不安全的信息、不适宜的信息）;

        ><li>图片文件大小支持：文件 < 5M；</li>
        ><li>图片文件分辨率支持：建议分辨率大于256x256，否则可能会影响识别效果；</li>
        ><li>图片文件支持格式：PNG、JPG、JPEG、BMP、GIF、WEBP格式。</li>

        :param request: Request instance for ProcessImage.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessImageRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessImageResponse`

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


    def ProcessMedia(self, request):
        """对点播中的音视频媒体发起处理任务，功能包括：
        1. 视频转码（带水印）；
        2. 视频转动图；
        3. 对视频按指定时间点截图；
        4. 对视频采样截图；
        5. 对视频截取雪碧图；
        6. 对视频截取一张图做封面；
        7. 对视频转自适应码流（并加密）；
        8. 内容审核（令人反感的信息、不安全的信息、不适宜的信息），<font color=red>不建议</font> 使用该接口发起，推荐使用 [音视频审核(ReviewAudioVideo)](https://cloud.tencent.com/document/api/266/80283) 或 [图片审核(ReviewImage)](https://cloud.tencent.com/document/api/266/73217)；
        9. 内容分析（标签、分类、封面、按帧标签）；
        10. 内容识别（视频片头片尾、人脸、文本全文、文本关键词、语音全文、语音关键词、物体）。

        如使用事件通知，事件通知的类型为 [任务流状态变更](https://cloud.tencent.com/document/product/266/9636)。

        :param request: Request instance for ProcessMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessMediaResponse`

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


    def ProcessMediaByProcedure(self, request):
        """使用任务流模板，对点播中的视频发起处理任务。
        有两种方式创建任务流模板：
        1. 在控制台上创建和修改任务流模板；
        2. 通过任务流模板接口创建任务流模板。

        如使用事件通知，除音视频审核任务外的事件通知的类型为 [任务流状态变更](https://cloud.tencent.com/document/product/266/9636)；音视频审核任务事件通知的类型为 [音视频审核完成](https://cloud.tencent.com/document/product/266/81258)。

        :param request: Request instance for ProcessMediaByProcedure.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByProcedureRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByProcedureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMediaByProcedure", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessMediaByProcedureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ProcessMediaByUrl(self, request):
        """该 API 已经<font color='red'>不再维护</font>，请使用 MPS 产品的 [ProcessMedia](https://cloud.tencent.com/document/product/862/37578) 接口，在入参 InputInfo.UrlInputInfo.Url 中指定视频 URL。

        :param request: Request instance for ProcessMediaByUrl.
        :type request: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByUrlRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ProcessMediaByUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ProcessMediaByUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ProcessMediaByUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PullEvents(self, request):
        """* 该接口用于业务服务器以 [可靠回调](https://cloud.tencent.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83) 的方式获取事件通知；
        * 接口为长轮询模式，即：如果服务端存在未消费事件，则立即返回给请求方；如果服务端没有未消费事件，则后台会将请求挂起，直到有新的事件产生为止；
        * 请求最多挂起5秒，建议请求方将超时时间设置为10秒；
        * 未被拉取的事件通知最多保留4天，超过该时限的事件通知可能会被清除；
        * 若该接口有事件返回，调用方必须在<font color="red">30秒</font>内调用 [确认事件通知](https://cloud.tencent.com/document/product/266/33434) 接口，确认事件通知已经处理，否则该事件通知在<font color="red">30秒</font>后会再次被拉取到。
        * 当前，API 每次最多可以获取16个事件通知。

        :param request: Request instance for PullEvents.
        :type request: :class:`tencentcloud.vod.v20180717.models.PullEventsRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.PullEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullEvents", params, headers=headers)
            response = json.loads(body)
            model = models.PullEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PullUpload(self, request):
        """该接口用于将一个网络上的视频拉取到云点播平台。

        :param request: Request instance for PullUpload.
        :type request: :class:`tencentcloud.vod.v20180717.models.PullUploadRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.PullUploadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullUpload", params, headers=headers)
            response = json.loads(body)
            model = models.PullUploadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PushUrlCache(self, request):
        """1. 预热指定的 URL 列表。
        2. URL 的域名必须已在云点播中注册。
        3. 单次请求最多指定20个 URL。
        4. 默认预热配额为每天10000个 URL。

        :param request: Request instance for PushUrlCache.
        :type request: :class:`tencentcloud.vod.v20180717.models.PushUrlCacheRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.PushUrlCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PushUrlCache", params, headers=headers)
            response = json.loads(body)
            model = models.PushUrlCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebuildMedia(self, request):
        """该 API 已经<font color=red>不再维护</font>，请使用新版接口 [音画质重生](https://cloud.tencent.com/document/api/266/102571)。
        发起音画质重生

        :param request: Request instance for RebuildMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.RebuildMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.RebuildMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebuildMedia", params, headers=headers)
            response = json.loads(body)
            model = models.RebuildMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebuildMediaByTemplate(self, request):
        """该 API 已经<font color=red>不再维护</font>，请使用新版接口 [音画质重生](https://cloud.tencent.com/document/api/266/102571)。
        使用模板发起视频重生。

        :param request: Request instance for RebuildMediaByTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.RebuildMediaByTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.RebuildMediaByTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebuildMediaByTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.RebuildMediaByTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshUrlCache(self, request):
        """1. 刷新指定的 URL 列表。
        2. URL 的域名必须已在云点播中注册。
        3. 单次请求最多指定20个 URL。
        4. 默认刷新配额为每天100000个 URL。

        :param request: Request instance for RefreshUrlCache.
        :type request: :class:`tencentcloud.vod.v20180717.models.RefreshUrlCacheRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.RefreshUrlCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshUrlCache", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshUrlCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveWatermark(self, request):
        """智能去除水印

        :param request: Request instance for RemoveWatermark.
        :type request: :class:`tencentcloud.vod.v20180717.models.RemoveWatermarkRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.RemoveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetProcedureTemplate(self, request):
        """重新设置用户自定义任务流模板的内容。

        :param request: Request instance for ResetProcedureTemplate.
        :type request: :class:`tencentcloud.vod.v20180717.models.ResetProcedureTemplateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ResetProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetProcedureTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ResetProcedureTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestoreMedia(self, request):
        """当媒体文件的存储类型是归档存储或深度归档存储时，是不可访问的。如需访问，则需要调用本接口进行解冻，解冻后可访问的媒体文件是临时的，在有效期过后，则不可访问。

        :param request: Request instance for RestoreMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.RestoreMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.RestoreMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreMedia", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReviewAudioVideo(self, request):
        """对点播中的音视频媒体发起审核任务，智能检测视频画面、画面中的文字、语音中的文字、声音出现的违规内容。

        如使用事件通知，事件通知的类型为 [音视频审核完成](https://cloud.tencent.com/document/product/266/81258)。

        :param request: Request instance for ReviewAudioVideo.
        :type request: :class:`tencentcloud.vod.v20180717.models.ReviewAudioVideoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ReviewAudioVideoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReviewAudioVideo", params, headers=headers)
            response = json.loads(body)
            model = models.ReviewAudioVideoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReviewImage(self, request):
        """对点播中的图片文件发起审核（令人反感的信息、不安全的信息、不适宜的信息）任务。

        ><li>图片文件大小支持：文件 < 5M；</li>
        ><li>图片文件分辨率支持：建议分辨率大于256x256，否则可能会影响审核效果；</li>
        ><li>图片文件支持格式：PNG、JPG、JPEG、BMP、GIF、WEBP格式。</li>

        :param request: Request instance for ReviewImage.
        :type request: :class:`tencentcloud.vod.v20180717.models.ReviewImageRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.ReviewImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReviewImage", params, headers=headers)
            response = json.loads(body)
            model = models.ReviewImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchMedia(self, request):
        """搜索媒体信息，支持多种条件筛选，以及支持对返回结果排序、过滤等功能，具体包括：
        - 指定文件 ID 集合 FileIds ，返回匹配集合中任意 ID 的媒体。
        - 根据多个媒体文件名 Names 或描述信息 Descriptions 进行模糊搜索。
        - 根据多个文件名前缀 NamePrefixes 进行搜索。
        - 指定分类集合 ClassIds（见输入参数），返回满足集合中任意分类的媒体。例如：媒体分类有电影、电视剧、综艺等，其中电影分类下又有子分类历史片、动作片、言情片。如果 ClassIds 指定了电影、电视剧，那么电影和电视剧下的所有子分类都会返回；而如果 ClassIds 指定的是历史片、动作片，那么只有这2个子分类下的媒体才会返回。
        - 指定标签集合 Tags（见输入参数），返回满足集合中任意标签的媒体。例如：媒体标签有二次元、宫斗、鬼畜，如果 Tags 指定了二次元、鬼畜2个标签，那么只要符合这2个标签中任意一个的媒体都会被检索出来。
        - 指定文件类型集合 Categories（见输入参数），返回满足集合中任意类型的媒体。例如：文件类型有 Video（视频）、 Audio （音频）、 Image （图片）。如果Categories指定了 Video 和 Audio 2个文件类型，那么符合这些类型的媒体都会被检索出来。
        - 指定来源集合 SourceTypes（见输入参数），返回满足集合中任意来源的媒体。例如：媒体来源有 Record (直播录制)、Upload （上传）等。如果 SourceTypes 指定了 Record 和 Upload ，那么符合这些来源的媒体都会被检索出来。
        - 指定文件封装格式集合 MediaTypes（见输入参数），返回满足集合中任意封装格式的媒体。例如：封装格式有 MP4、AVI、MP3 等。如果 MediaTypes 指定了 MP4 和 MP3，那么符合这些封装格式的媒体都会被检索出来。
        - 指定文件状态集合 Status（见输入参数），返回满足集合中任意状态的媒体。例如：文件状态有 Normal（正常）、SystemForbidden（平台封禁）、Forbidden（主动封禁）。如果 Status 指定了 Normal 和 Forbidden 2种文件状态，那么符合这些状态的媒体都会被检索出来。
        - 指定文件审核结果集合 ReviewResults（见输入参数），返回满足集合中任意状态的媒体。例如：文件审核结果有 pass（通过）、block（违规）等。如果 ReviewResults 指定了 pass 和 block 2种审核结果，那么符合这些审核结果的媒体都会被检索出来。
        - 指定直播推流码集合 StreamIds（见输入参数）筛选直播录制的媒体。
        - 指定媒体的创建时间范围筛选媒体。
        - 指定 TRTC 应用 ID 集合筛选媒体。
        - 指定 TRTC 房间 ID 集合筛选媒体。

        - 以上参数之间可以任意组合进行检索。例如：筛选创建时间在2018年12月1日12:00:00到2018年12月8日12:00:00之间、分类为电影或电视剧、带有宫斗和悬疑标签的媒体。注意，任何支持数组输入的参数，其元素之间的搜索逻辑为‘或’。所有参数之间的逻辑关系为‘与’。

        - 允许通过 Filters 控制返回的媒体信息种类（默认返回所有信息）。可选输入包括：
            1. 基础信息（basicInfo）：包括媒体名称、分类、播放地址、封面图片等。
            2. 元信息（metaData）：包括大小、时长、视频流信息、音频流信息等。
            3. 转码结果信息（transcodeInfo）：包括该媒体转码生成的各种规格的媒体地址、视频流参数、音频流参数等。
            4. 转动图结果信息（animatedGraphicsInfo）：对视频转动图（如 gif）后的动图信息。
            5. 采样截图信息（sampleSnapshotInfo）：对视频采样截图后的截图信息。
            6. 雪碧图信息（imageSpriteInfo）：对视频截取雪碧图后的雪碧图信息。
            7. 指定时间点截图信息（snapshotByTimeOffsetInfo）：对视频依照指定时间点截图后，的截图信息。
            8. 视频打点信息（keyFrameDescInfo）：对视频设置的打点信息。
            9. 转自适应码流信息（adaptiveDynamicStreamingInfo）：包括规格、加密类型、打包格式等相关信息。

        - 允许对结果根据创建时间进行排序并分页返回，通过 Offset 和 Limit （见输入参数）来控制分页。

        <div id="maxResultsDesc">接口返回结果数限制：</div>
        - <b><a href="#p_offset">Offset</a> 和 <a href="#p_limit">Limit</a> 两个参数影响单次分页查询结果数。特别注意：当这2个值都缺省时，本接口最多只返回10条查询结果。</b>
        - <b>最大支持返回5000条搜索结果，超出部分不再支持查询。如果搜索结果量太大，建议使用更精细的筛选条件来减少搜索结果。</b>

        <br>不推荐使用的条件筛选：
        - （不推荐：应使用 Names、NamePrefixes 或 Descriptions 替代）指定单个文本 Text 对媒体文件名或描述信息进行模糊搜索。
        - （不推荐：应使用 SourceTypes 替代）指定单个媒体文件来源 SourceType 进行搜索。
        - （不推荐：应使用 StreamIds 替代）指定单个推流直播码 StreamId 进行搜索。
        - （不推荐：应使用 CreateTime 替代）指定单个起始创建时间 StartTime 进行搜索。
        - （不推荐：应使用 CreateTime 替代）指定单个结尾创建时间 EndTime 进行搜索。

        :param request: Request instance for SearchMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.SearchMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SearchMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchMedia", params, headers=headers)
            response = json.loads(body)
            model = models.SearchMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetCLSPushTarget(self, request):
        """为点播域名设置投递 CLS 的目标。

        :param request: Request instance for SetCLSPushTarget.
        :type request: :class:`tencentcloud.vod.v20180717.models.SetCLSPushTargetRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SetCLSPushTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetCLSPushTarget", params, headers=headers)
            response = json.loads(body)
            model = models.SetCLSPushTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetDrmKeyProviderInfo(self, request):
        """设置 DRM 密钥提供商信息。

        :param request: Request instance for SetDrmKeyProviderInfo.
        :type request: :class:`tencentcloud.vod.v20180717.models.SetDrmKeyProviderInfoRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SetDrmKeyProviderInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetDrmKeyProviderInfo", params, headers=headers)
            response = json.loads(body)
            model = models.SetDrmKeyProviderInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetVodDomainCertificate(self, request):
        """设置点播域名 HTTPS 证书。

        :param request: Request instance for SetVodDomainCertificate.
        :type request: :class:`tencentcloud.vod.v20180717.models.SetVodDomainCertificateRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SetVodDomainCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVodDomainCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.SetVodDomainCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SimpleHlsClip(self, request):
        """对 HLS 视频进行按时间段裁剪，实时生成一个新的视频（HLS 格式），开发者可以将其立即分享出去，或者长久保存起来。

        腾讯云点播支持两种剪辑模式：
        - 剪辑固化：将剪辑出来的视频保存成独立的视频，拥有独立 FileId；适用于将精彩片段长久保存的场景；
        - 剪辑不固化：剪辑得到的视频附属于输入文件，没有独立 FileId；适用于将精彩片段临时分享的场景。

        裁剪精度支持粗略裁剪和精确裁剪：
        - 粗略剪辑：基于输入 m3u8 文件进行裁剪，其最小剪辑精度为一个 ts 切片，无法实现秒级或者更为精确的剪辑精度。
        - 精确剪辑：按照 StartTimeOffset 和 EndTimeOffset 参数进行精确裁剪。使用精确裁剪需要开通[即时转码](/document/product/266/102174)的功能。

        ### 剪辑固化
        所谓剪辑固化，是指将剪辑出来的视频保存成一个独立的视频（拥有独立的 FileId）。其生命周期不受原始输入视频影响（即使原始输入视频被删除，剪辑结果也不会受到任何影响）；也可以对其进行转码、微信发布等二次处理。

        举例如下：一场完整的足球比赛，原始视频可能长达 2 个小时，客户出于节省成本的目的可以对这个视频存储 2 个月，但对于剪辑的「精彩时刻」视频却可以指定存储更长时间，同时可以单独对「精彩时刻」视频进行转码、微信发布等额外的点播操作，这时候可以选择剪辑并且固化的方案。

        剪辑固化的优势在于其生命周期与原始输入视频相互独立，可以独立管理、长久保存。

        <font color='red'>注意：</font>如果剪辑时指定进行固化，通过 ModifyEventConfig 接口启用接收剪辑固化事件通知，固化成功后将会收到一个 PersitenceComplete 类型的事件通知。在收到这个事件通知之前，不应该对原始输入的视频进行删除、降冷等操作，否则剪辑生成的视频播放可能出现异常。

        ### 剪辑不固化
        所谓剪辑不固化，是指剪辑所得到的结果（m3u8 文件）与原始输入视频共享相同的 ts 分片，新生成的视频不是一个独立完整的视频（没有独立 FileId，只有播放 URL），其有效期与原始输入的完整视频有效期是一致的。一旦原始输入的视频被删除，也会导致该片段无法播放。

        剪辑不固化，由于其剪辑结果不是一个独立的视频，因而也不会纳入点播媒资视频管理（例如控制台的视频总数不会统计这一片段）中，也无法单独针对这个片段做转码、微信发布等任何视频处理操作。

        剪辑不固化的优势在于其剪辑操作十分“轻量化”，不会产生额外的存储开销。但其不足之处在于生命周期与原始录制视频相同，且无法进一步进行转码等视频处理。

        :param request: Request instance for SimpleHlsClip.
        :type request: :class:`tencentcloud.vod.v20180717.models.SimpleHlsClipRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SimpleHlsClipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SimpleHlsClip", params, headers=headers)
            response = json.loads(body)
            model = models.SimpleHlsClipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SplitMedia(self, request):
        """对点播视频进行拆条，生成多个新的点播视频。

        :param request: Request instance for SplitMedia.
        :type request: :class:`tencentcloud.vod.v20180717.models.SplitMediaRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.SplitMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SplitMedia", params, headers=headers)
            response = json.loads(body)
            model = models.SplitMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyDomainRecord(self, request):
        """该接口用于验证域名解析值。

        :param request: Request instance for VerifyDomainRecord.
        :type request: :class:`tencentcloud.vod.v20180717.models.VerifyDomainRecordRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.VerifyDomainRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyDomainRecord", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyDomainRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def WeChatMiniProgramPublish(self, request):
        """将点播视频发布到微信小程序，供微信小程序播放器播放。
        本接口支持发布原始视频和转码后视频，暂不支持发布自适应码流。

        :param request: Request instance for WeChatMiniProgramPublish.
        :type request: :class:`tencentcloud.vod.v20180717.models.WeChatMiniProgramPublishRequest`
        :rtype: :class:`tencentcloud.vod.v20180717.models.WeChatMiniProgramPublishResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("WeChatMiniProgramPublish", params, headers=headers)
            response = json.loads(body)
            model = models.WeChatMiniProgramPublishResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))