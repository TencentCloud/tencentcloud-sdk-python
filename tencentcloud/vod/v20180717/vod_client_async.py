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
from tencentcloud.vod.v20180717 import models
from typing import Dict


class VodClient(AbstractClient):
    _apiVersion = '2018-07-17'
    _endpoint = 'vod.tencentcloudapi.com'
    _service = 'vod'

    async def ApplyUpload(
            self,
            request: models.ApplyUploadRequest,
            opts: Dict = None,
    ) -> models.ApplyUploadResponse:
        """
        * 我们强烈建议您使用云点播提供的 [服务端上传 SDK](/document/product/266/9759#1.-.E5.8F.91.E8.B5.B7.E4.B8.8A.E4.BC.A0) 来上传文件。直接调用 API 进行上传的难度和工作量都显著大于使用 SDK。
        * 该接口用于申请媒体文件（和封面文件）的上传，获取文件上传到云点播的元信息（包括上传路径、上传签名等），用于后续上传接口。
        * 上传流程请参考 [服务端上传综述](/document/product/266/9759)。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachMediaSubtitles(
            self,
            request: models.AttachMediaSubtitlesRequest,
            opts: Dict = None,
    ) -> models.AttachMediaSubtitlesResponse:
        """
        关联媒资字幕，将指定的字幕关联到转自适应码流模板号对应的媒体输出文件中（或解除关联）。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachMediaSubtitles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachMediaSubtitlesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitUpload(
            self,
            request: models.CommitUploadRequest,
            opts: Dict = None,
    ) -> models.CommitUploadResponse:
        """
        该接口用于确认媒体文件（和封面文件）上传到腾讯云点播的结果，并存储媒体信息，返回文件的播放地址和文件 ID。
        """
        
        kwargs = {}
        kwargs["action"] = "CommitUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommitUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ComposeMedia(
            self,
            request: models.ComposeMediaRequest,
            opts: Dict = None,
    ) -> models.ComposeMediaResponse:
        """
        该接口用于合成媒体文件，可以达到以下效果：

        1. **画面旋转**：对视频、图片的画面旋转一定角度，或按照某个方向翻转。
        2. **声音控制**：升高降低视频、音频中声音的音量，或者对视频静音。
        3. **画面叠加**：将视频、图片中的画面依序叠加在一起，如实现“画中画”的效果。
        4. **声音混合**：将视频、音频中的声音混合在一起（混音）。
        5. **声音提取**：将视频中的音频提取出来（不保留画面）。
        6. **裁剪**：对视频、音频裁剪出指定时间段。
        7. **拼接**：对视频、音频、图片按时间顺序前后拼接。
        8. **转场**：将多段视频或图片拼接时，可以在段落之间添加转场效果。

        合成后的媒体封装格式可以是 MP4（视频）或 MP3（音频）。如使用事件通知，事件通知的类型为 [视频合成完成](https://cloud.tencent.com/document/product/266/43000)。
        """
        
        kwargs = {}
        kwargs["action"] = "ComposeMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ComposeMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfirmEvents(
            self,
            request: models.ConfirmEventsRequest,
            opts: Dict = None,
    ) -> models.ConfirmEventsResponse:
        """
        * 开发者调用拉取事件通知，获取到事件后，必须调用该接口来确认消息已经收到；
        * 开发者获取到事件句柄后，等待确认的有效时间为 30 秒，超出 30 秒会报参数错误（4000）；
        * 更多参考事件通知的[可靠回调](https://cloud.tencent.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83)。
        """
        
        kwargs = {}
        kwargs["action"] = "ConfirmEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfirmEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIAnalysisTemplate(
            self,
            request: models.CreateAIAnalysisTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAIAnalysisTemplateResponse:
        """
        创建用户自定义音视频内容分析模板，数量上限：50。暂时不支持 HLS 格式。
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
        创建用户自定义音视频内容识别模板，数量上限：50。
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
        
    async def CreateAigcImageTask(
            self,
            request: models.CreateAigcImageTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAigcImageTaskResponse:
        """
        该接口用于[生成 AIGC 图片](https://cloud.tencent.com/document/product/266/124473)。<b>接口处于内测阶段，如需使用请[联系我们](https://cloud.tencent.com/online-service?from=sales_sales&source=PRESALE)，接口调用会产生实际费用，</b>请参考点播 [AIGC 生图片计费文档](https://cloud.tencent.com/document/product/266/95125#9c4dc6ff-4b3f-4b25-bf2d-393889dfb9ac)。该功能结算模式为[后付费](https://cloud.tencent.com/document/product/266/2838)，日结客户当天使用将在第二天出账，月结客户将在次月1日统一出上月使用费用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcImageTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcImageTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAigcVideoTask(
            self,
            request: models.CreateAigcVideoTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAigcVideoTaskResponse:
        """
        该接口用于[生成 AIGC 视频](https://cloud.tencent.com/document/product/266/124474)。<b>接口处于内测阶段，如需使用请[联系我们](https://cloud.tencent.com/online-service?from=sales_sales&source=PRESALE)，接口调用会产生实际费用</b>，请参考点播 [AIGC 生视频计费文档](https://cloud.tencent.com/document/product/266/95125#96b3b59a-f9e1-49e9-966a-bedb70a4bf12)。该功能结算模式为[后付费](https://cloud.tencent.com/document/product/266/2838)，日结客户当天使用将在第二天出账，月结客户将在次月1日统一出上月使用费用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAigcVideoTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAigcVideoTaskResponse
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
        
    async def CreateCLSLogset(
            self,
            request: models.CreateCLSLogsetRequest,
            opts: Dict = None,
    ) -> models.CreateCLSLogsetResponse:
        """
        由 VOD 创建新的日志集。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCLSLogset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCLSLogsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCLSTopic(
            self,
            request: models.CreateCLSTopicRequest,
            opts: Dict = None,
    ) -> models.CreateCLSTopicResponse:
        """
        创建 VOD 下新的 CLS 日志主题
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCLSTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCLSTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClass(
            self,
            request: models.CreateClassRequest,
            opts: Dict = None,
    ) -> models.CreateClassResponse:
        """
        * 用于对媒体进行分类管理；
        * 该接口不影响既有媒体的分类，如需修改媒体分类，请调用[修改媒体文件属性](/document/product/266/31762)接口。
        * 分类层次不可超过 4 层。
        * 每个分类的子类数量不可超过 500 个。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateComplexAdaptiveDynamicStreamingTask(
            self,
            request: models.CreateComplexAdaptiveDynamicStreamingTaskRequest,
            opts: Dict = None,
    ) -> models.CreateComplexAdaptiveDynamicStreamingTaskResponse:
        """
        发起复杂自适应码流处理任务，功能包括：
        1. 按指定的自适应码流模板输出 HLS、DASH 自适应码流；
        2. 自适应码流的内容保护方案可选择无加密、Widevine 或 FairPlay；
        3. 支持添加片头片尾；
        4. 输出的自适应码流可包含多语言音频流，每种语言分别来自不同的媒体文件；
        5. 输出的自适应码流可包含多语言字幕流。

        注意事项：
        1. 当使用片头时，片头媒体中的视频流需要和音频流对齐，否则将导致输出的内容音画不同步；
        2. 如果输出的自适应码流需要包含主媒体的音频，那么需要在 AudioSet 参数中指定主媒体的 FileId；
        3. 使用字幕时，需要先将字幕添加到主媒体，可通过 ModifyMediaInfo 接口或控制台的音视频详情页进行添加；
        4. 暂不支持极速高清、水印。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateComplexAdaptiveDynamicStreamingTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateComplexAdaptiveDynamicStreamingTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateContentReviewTemplate(
            self,
            request: models.CreateContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateContentReviewTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版审核模板支持音视频审核和图片审核，详细请参考 [创建审核模板](https://cloud.tencent.com/document/api/266/84391)。
        创建用户自定义音视频内容审核模板，数量上限：50。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateContentReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainVerifyRecord(
            self,
            request: models.CreateDomainVerifyRecordRequest,
            opts: Dict = None,
    ) -> models.CreateDomainVerifyRecordResponse:
        """
        该接口用于生成一条子域名解析，提示客户添加到域名解析上，用于泛域名及域名取回校验归属权。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainVerifyRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainVerifyRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnhanceMediaTemplate(
            self,
            request: models.CreateEnhanceMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateEnhanceMediaTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        创建音画质重生模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnhanceMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnhanceMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHeadTailTemplate(
            self,
            request: models.CreateHeadTailTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateHeadTailTemplateResponse:
        """
        创建片头片尾模板。
        - 最大支持模板数量为 100 个。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHeadTailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHeadTailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageProcessingTemplate(
            self,
            request: models.CreateImageProcessingTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateImageProcessingTemplateResponse:
        """
        创建一个用户自定义的图片处理模板，数量上限：16。最多支持十次操作，例如：裁剪-缩略-裁剪-模糊-缩略-裁剪-缩略-裁剪-模糊-缩略。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageProcessingTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageProcessingTemplateResponse
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
        
    async def CreateJustInTimeTranscodeTemplate(
            self,
            request: models.CreateJustInTimeTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateJustInTimeTranscodeTemplateResponse:
        """
        创建即时转码模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMPSTemplate(
            self,
            request: models.CreateMPSTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateMPSTemplateResponse:
        """
        该接口用于创建自定义模板，模板用于 ProcessMediaByMPS 接口的部分功能。
        创建模板时，需要将 MPS 相关参数以 JSON 格式填入 MPSCreateTemplateParams 参数中。关于具体的任务参数配置方法，请参考 MPS 任务模板相关文档说明。
        当前支持创建自定义模板的 MPS 功能：
        1. [音视频增强](https://cloud.tencent.com/document/product/862/118703)。

        > 以该种方式创建的任务模板：
        > 1. 模板的管理仍在点播平台中完成。
        > 2. 该功能目前仍在内测中，如需测试体验，您可以联系我们获得支持。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMPSTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMPSTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePersonSample(
            self,
            request: models.CreatePersonSampleRequest,
            opts: Dict = None,
    ) -> models.CreatePersonSampleResponse:
        """
        该接口用于创建素材样本，用于通过五官定位等技术，进行内容识别、不适宜视频识别等视频处理。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProcedureTemplate(
            self,
            request: models.CreateProcedureTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateProcedureTemplateResponse:
        """
        创建用户自定义的任务流模板，模板上限：50。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProcedureTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProcedureTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateQualityInspectTemplate(
            self,
            request: models.CreateQualityInspectTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateQualityInspectTemplateResponse:
        """
        创建音画质检测模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateQualityInspectTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateQualityInspectTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRebuildMediaTemplate(
            self,
            request: models.CreateRebuildMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateRebuildMediaTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        创建视频重生模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRebuildMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRebuildMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReviewTemplate(
            self,
            request: models.CreateReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateReviewTemplateResponse:
        """
        创建用户自定义审核模板，数量上限：50。
        >模板仅适用于 [音视频审核(ReviewAudioVideo)](https://cloud.tencent.com/document/api/266/80283) 和 [图片审核(ReviewImage)](https://cloud.tencent.com/document/api/266/73217) 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoundPlay(
            self,
            request: models.CreateRoundPlayRequest,
            opts: Dict = None,
    ) -> models.CreateRoundPlayResponse:
        """
        该接口用于创建轮播播单，数量上限：100。
        轮播播单的每个文件可以指定源文件，也可以指定某个转码文件。
        指定的文件必须是hls格式，所有的播单文件最好保持相同的码率和分辨率。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoundPlay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoundPlayResponse
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
        
    async def CreateStorageRegion(
            self,
            request: models.CreateStorageRegionRequest,
            opts: Dict = None,
    ) -> models.CreateStorageRegionResponse:
        """
        该接口用于开通某地域的存储。
          1. 用户开通点播业务时，系统默认为用户开通了部分地域的存储，用户如果需要开通其它地域的存储，可以通过该接口进行开通。
          2. 通过 DescribeStorageRegions 接口可以查询到所有存储地域及已经开通的地域。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStorageRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStorageRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubAppId(
            self,
            request: models.CreateSubAppIdRequest,
            opts: Dict = None,
    ) -> models.CreateSubAppIdResponse:
        """
        该接口用于创建点播应用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubAppId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubAppIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSuperPlayerConfig(
            self,
            request: models.CreateSuperPlayerConfigRequest,
            opts: Dict = None,
    ) -> models.CreateSuperPlayerConfigResponse:
        """
        该 API 已经<font color='red'>不再维护</font>，新版播放器签名不再使用播放器配置模板，详细请参考 [播放器签名](https://cloud.tencent.com/document/product/266/45554)。
        创建播放器配置，数量上限：100。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSuperPlayerConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSuperPlayerConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTranscodeTemplate(
            self,
            request: models.CreateTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateTranscodeTemplateResponse:
        """
        创建用户自定义转码模板，数量上限：100。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVodDomain(
            self,
            request: models.CreateVodDomainRequest,
            opts: Dict = None,
    ) -> models.CreateVodDomainResponse:
        """
        该接口用于将加速域名添加到点播，一个用户最多添加20个加速域名。
        1.域名添加成功后点播会进行域名的部署，域名由部署状态变为在线状态大概需要2分钟的时间。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVodDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVodDomainResponse
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
        
    async def DeleteAIAnalysisTemplate(
            self,
            request: models.DeleteAIAnalysisTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAIAnalysisTemplateResponse:
        """
        删除用户自定义音视频内容分析模板。

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
        删除用户自定义音视频内容识别模板。
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
        
    async def DeleteCLSTopic(
            self,
            request: models.DeleteCLSTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteCLSTopicResponse:
        """
        删除点播开通的日志主题。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCLSTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCLSTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClass(
            self,
            request: models.DeleteClassRequest,
            opts: Dict = None,
    ) -> models.DeleteClassResponse:
        """
        * 仅当待删分类无子分类且无媒体关联情况下，可删除分类；
        * 否则，请先执行[删除媒体](/document/product/266/31764)及子分类，再删除该分类；
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteContentReviewTemplate(
            self,
            request: models.DeleteContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteContentReviewTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版审核模板支持音视频审核和图片审核，详细请参考 [删除审核模板](https://cloud.tencent.com/document/api/266/84390)。
        删除用户自定义音视频内容审核模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteContentReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnhanceMediaTemplate(
            self,
            request: models.DeleteEnhanceMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteEnhanceMediaTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        删除音画质重生模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnhanceMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnhanceMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHeadTailTemplate(
            self,
            request: models.DeleteHeadTailTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteHeadTailTemplateResponse:
        """
        删除片头片尾模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHeadTailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHeadTailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageProcessingTemplate(
            self,
            request: models.DeleteImageProcessingTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteImageProcessingTemplateResponse:
        """
        删除用户自定义图片处理模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageProcessingTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageProcessingTemplateResponse
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
        
    async def DeleteJustInTimeTranscodeTemplate(
            self,
            request: models.DeleteJustInTimeTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteJustInTimeTranscodeTemplateResponse:
        """
        删除即时转码模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMPSTemplate(
            self,
            request: models.DeleteMPSTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteMPSTemplateResponse:
        """
        删除用户自定义 MPS 任务模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMPSTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMPSTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMedia(
            self,
            request: models.DeleteMediaRequest,
            opts: Dict = None,
    ) -> models.DeleteMediaResponse:
        """
        * 删除媒体及其对应的视频处理文件（原始文件、如转码视频、雪碧图、截图、微信发布视频等）；
        * 可单独删除指定 ID 的视频文件下的原文件、转码视频、微信发布视频等；
        * 注意：原文件删除后，无法发起转码、微信发布等任何视频处理操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePersonSample(
            self,
            request: models.DeletePersonSampleRequest,
            opts: Dict = None,
    ) -> models.DeletePersonSampleResponse:
        """
        该接口用于根据人物 ID，删除素材样本。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePersonSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePersonSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProcedureTemplate(
            self,
            request: models.DeleteProcedureTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteProcedureTemplateResponse:
        """
        删除用户自定义的任务流模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProcedureTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProcedureTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteQualityInspectTemplate(
            self,
            request: models.DeleteQualityInspectTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteQualityInspectTemplateResponse:
        """
        删除音画质检测模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteQualityInspectTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteQualityInspectTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRebuildMediaTemplate(
            self,
            request: models.DeleteRebuildMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteRebuildMediaTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        删除视频重生模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRebuildMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRebuildMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReviewTemplate(
            self,
            request: models.DeleteReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteReviewTemplateResponse:
        """
        删除用户自定义审核模板。
        >模板仅适用于 [音视频审核(ReviewAudioVideo)](https://cloud.tencent.com/document/api/266/80283) 和 [图片审核(ReviewImage)](https://cloud.tencent.com/document/api/266/73217) 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoundPlay(
            self,
            request: models.DeleteRoundPlayRequest,
            opts: Dict = None,
    ) -> models.DeleteRoundPlayResponse:
        """
        该接口用于删除轮播播单。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoundPlay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoundPlayResponse
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
        
    async def DeleteSuperPlayerConfig(
            self,
            request: models.DeleteSuperPlayerConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteSuperPlayerConfigResponse:
        """
        该 API 已经<font color='red'>不再维护</font>，新版播放器签名不再使用播放器配置模板，详细请参考 [播放器签名](https://cloud.tencent.com/document/product/266/45554)。
        删除播放器配置。
        *注：系统预置播放器配置不允许删除。*
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSuperPlayerConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSuperPlayerConfigResponse
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
        
    async def DeleteVodDomain(
            self,
            request: models.DeleteVodDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteVodDomainResponse:
        """
        该接口用于删除点播加速域名。
        1、域名删除前需要先关闭所有区域的加速。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVodDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVodDomainResponse
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
        
    async def DescribeAIAnalysisTemplates(
            self,
            request: models.DescribeAIAnalysisTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisTemplatesResponse:
        """
        根据音视频内容分析模板唯一标识，获取音视频内容分析模板详情列表。返回结果包含符合条件的所有用户自定义音视频内容分析模板及[系统预置音视频内容分析模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.88.86.E6.9E.90.E6.A8.A1.E6.9D.BF)。
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
        根据音视频内容识别模板唯一标识，获取音视频内容识别模板详情列表。返回结果包含符合条件的所有用户自定义音视频内容识别模板及[系统预置音视频内容识别模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E8.AF.86.E5.88.AB.E6.A8.A1.E6.9D.BF)。
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
        
    async def DescribeAigcUsageData(
            self,
            request: models.DescribeAigcUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeAigcUsageDataResponse:
        """
        该接口返回查询时间范围内AIGC的统计信息。
           1. 可以查询最近365天内的AIGC统计数据。
           2. 查询时间跨度不超过90天。
           3. 查询时间跨度超过1天的，返回以天为粒度的数据，否则，返回以5分钟为粒度的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAigcUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAigcUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllClass(
            self,
            request: models.DescribeAllClassRequest,
            opts: Dict = None,
    ) -> models.DescribeAllClassResponse:
        """
        * 获得用户的所有分类信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllClassResponse
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
        
    async def DescribeCDNStatDetails(
            self,
            request: models.DescribeCDNStatDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeCDNStatDetailsResponse:
        """
        该接口用于查询点播域名的 CDN 带宽、流量等统计数据。
        * 查询的起始时间和结束时间跨度不超过90天。
        * 可以查询不同服务区域的数据。
        * 中国境内的数据支持查询指定地区、运营商的统计数据。
        * 播放统计仅针对 VOD 域名（即 EdgeOne 域名的分发不计入播放统计）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCDNStatDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCDNStatDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCDNUsageData(
            self,
            request: models.DescribeCDNUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCDNUsageDataResponse:
        """
        该接口用于查询点播 CDN 的流量、带宽等统计数据。
           1. CDN 用量数据系统侧保留 13 个月，您通过接口仅可查询最近 365 天内的用量数据。如需调取超出 365 天的历史用量数据，请联系我们。
           2. 查询时间跨度不超过90天。
           3. 可以指定用量数据的时间粒度，支持5分钟、1小时、1天的时间粒度。
           4. 流量为查询时间粒度内的总流量，带宽为查询时间粒度内的峰值带宽。
           5. 播放统计仅针对 VOD 域名（即 EdgeOne 域名的分发不计入播放统计）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCDNUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCDNUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCLSLogsets(
            self,
            request: models.DescribeCLSLogsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeCLSLogsetsResponse:
        """
        查询 VOD 创建的 CLS 日志集。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSLogsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSLogsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCLSPushTargets(
            self,
            request: models.DescribeCLSPushTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeCLSPushTargetsResponse:
        """
        查询点播域名下日志投递的目标主题。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSPushTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSPushTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCLSTopics(
            self,
            request: models.DescribeCLSTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeCLSTopicsResponse:
        """
        查询 VOD 创建的 CLS 日志主题列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnLogs(
            self,
            request: models.DescribeCdnLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnLogsResponse:
        """
        查询点播域名的 CDN （不含 EdgeOne 回源到 VOD 域名）访问日志的下载链接。
            1. 可以查询最近30天内的 CDN 日志下载链接。
            2. 默认情况下 CDN 每小时生成一个日志文件，如果某一个小时没有 CDN 访问，不会生成日志文件。
            3. CDN 日志下载链接的有效期为24小时。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdnLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdnLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientUploadAccelerationUsageData(
            self,
            request: models.DescribeClientUploadAccelerationUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeClientUploadAccelerationUsageDataResponse:
        """
        该接口返回查询时间范围内客户端上传加速统计信息。
           1. 可以查询最近365天内的客户端上传加速统计数据。
           2. 查询时间跨度不超过90天。
           3. 查询时间跨度超过1天的，返回以天为粒度的数据，否则，返回以5分钟为粒度的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientUploadAccelerationUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientUploadAccelerationUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContentReviewTemplates(
            self,
            request: models.DescribeContentReviewTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeContentReviewTemplatesResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版审核模板支持音视频审核和图片审核，详细请参考 [获取审核模板列表](https://cloud.tencent.com/document/api/266/84389)。
        根据音视频内容审核模板唯一标识，获取音视频内容审核模板详情列表。返回结果包含符合条件的所有用户自定义模板及[系统预置内容审核模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.AE.A1.E6.A0.B8.E6.A8.A1.E6.9D.BF)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContentReviewTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContentReviewTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCurrentPlaylist(
            self,
            request: models.DescribeCurrentPlaylistRequest,
            opts: Dict = None,
    ) -> models.DescribeCurrentPlaylistResponse:
        """
        查询轮播当前播放列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCurrentPlaylist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCurrentPlaylistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDailyMediaPlayStat(
            self,
            request: models.DescribeDailyMediaPlayStatRequest,
            opts: Dict = None,
    ) -> models.DescribeDailyMediaPlayStatResponse:
        """
        该接口用于查询指定日期范围内每天的播放统计数据。
        * 可以查询最近一年的播放统计数据。
        * 结束日期和起始日期的时间跨度最大为90天。
        * 播放统计仅针对 VOD 域名（即 EdgeOne 域名的分发不计入播放统计）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDailyMediaPlayStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDailyMediaPlayStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDailyMostPlayedStat(
            self,
            request: models.DescribeDailyMostPlayedStatRequest,
            opts: Dict = None,
    ) -> models.DescribeDailyMostPlayedStatResponse:
        """
        该接口用于查询每日播放Top100 的媒体文件的播放统计数据。
        * 可以查询最近一年的播放统计数据。
        * 可以按播放次数或者播放流量查询。
        * 播放次数统计说明：
            1. HLS 文件：访问 M3U8 文件时统计播放次数；访问 TS 文件不统计播放次数。
            2. 其它文件（如 MP4 文件）：播放请求带有 range 参数且 range 的 start 参数不等于0时不统计播放次数，其它情况统计播放次数。
        * 播放统计仅针对 VOD 域名（即 EdgeOne 域名的分发不计入播放统计）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDailyMostPlayedStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDailyMostPlayedStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDailyPlayStatFileList(
            self,
            request: models.DescribeDailyPlayStatFileListRequest,
            opts: Dict = None,
    ) -> models.DescribeDailyPlayStatFileListResponse:
        """
        该接口用于查询播放统计文件的下载地址。
        * 可以查询最近一年的播放统计文件下载地址，查询的起始日期和结束日期的时间跨度不超过90天。
        * 云点播每天对前一天的 CDN 请求日志进行分析处理，生成播放统计文件。
        * 播放统计文件内容包含媒体文件的播放次数、播放流量等统计信息。
        * 播放次数统计说明：
            1. HLS 文件：访问M3U8 文件时统计播放次数；访问TS 文件不统计播放次数。
            2. 其它文件（如 MP4 文件）：播放请求带有 range 参数且 range 的 start 参数不等于0时不统计播放次数，其它情况统计播放次数。
        * 播放设备的统计：播放请求带了 UserAgent 参数，并且 UserAgent 包含 Android 或者 iPhone 等标识，会统计为移动端播放次数，否则统计为 PC 端播放次数。
        * 播放统计仅针对 VOD 域名（即 EdgeOne 域名的分发不计入播放统计）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDailyPlayStatFileList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDailyPlayStatFileListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultDistributionConfig(
            self,
            request: models.DescribeDefaultDistributionConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultDistributionConfigResponse:
        """
        该接口用于查询默认分发配置。
        * 分发域名和分发协议，即媒体文件分发 URL 中的域名和协议。媒体文件按默认分发配置进行分发。
        * 播放密钥，用于计算播放器签名。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultDistributionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultDistributionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDrmDataKey(
            self,
            request: models.DescribeDrmDataKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeDrmDataKeyResponse:
        """
        本 API 是 [旧版本加密](https://cloud.tencent.com/document/product/266/9638) 中 [DescribeDrmDataKey 的 API 2017 接口](https://cloud.tencent.com/document/product/266/9643) 的升级版本。

        如果您是新接入点播加密的用户，不要使用该 API，请参考 [视频加密综述](https://cloud.tencent.com/document/product/266/45552) 使用推荐的加密方式。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDrmDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDrmDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDrmKeyProviderInfo(
            self,
            request: models.DescribeDrmKeyProviderInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDrmKeyProviderInfoResponse:
        """
        查询 DRM 密钥提供商信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDrmKeyProviderInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDrmKeyProviderInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnhanceMediaTemplates(
            self,
            request: models.DescribeEnhanceMediaTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeEnhanceMediaTemplatesResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        获取音画质重生模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnhanceMediaTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnhanceMediaTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventConfig(
            self,
            request: models.DescribeEventConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeEventConfigResponse:
        """
        腾讯云点播为客户提供了媒体上传、媒体管理、媒体处理等等服务，在这些服务执行过程或执行结束时，腾讯云点播也提供各种对应的事件通知，方便开发者感知服务处理状态，并做下一步的业务操作。

        开发者可以通过本接口来查询当前配置事件通知的接收方式、接收地址以及哪些事件开启了接收回调通知。

        默认接口请求频率限制：100次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventsState(
            self,
            request: models.DescribeEventsStateRequest,
            opts: Dict = None,
    ) -> models.DescribeEventsStateResponse:
        """
        * 该接口用于业务服务器获取 [可靠回调](https://cloud.tencent.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83) 事件通知的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventsState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventsStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileAttributes(
            self,
            request: models.DescribeFileAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeFileAttributesResponse:
        """
        用于异步获取文件属性。
        - 当前仅支持获取源文件的 Md5、Sha1。
        - 对输入文件为 HLS 或 DASH 的情况，仅获取索引文件的属性。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHeadTailTemplates(
            self,
            request: models.DescribeHeadTailTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeHeadTailTemplatesResponse:
        """
        获取片头片尾模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHeadTailTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHeadTailTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageProcessingTemplates(
            self,
            request: models.DescribeImageProcessingTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeImageProcessingTemplatesResponse:
        """
        获取图片处理模板列表，支持根据条件，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageProcessingTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageProcessingTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageReviewUsageData(
            self,
            request: models.DescribeImageReviewUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeImageReviewUsageDataResponse:
        """
        该接口返回查询时间范围内每天使用的图片审核用量信息。
           1. 可以查询最近365天内的图片审核统计数据。
           2. 查询时间跨度不超过90天。
           3. 查询时间跨度超过1天的，返回以天为粒度的数据，否则，返回以5分钟为粒度的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageReviewUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageReviewUsageDataResponse
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
        
    async def DescribeJustInTimeTranscodeTemplates(
            self,
            request: models.DescribeJustInTimeTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeJustInTimeTranscodeTemplatesResponse:
        """
        获取即时转码模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJustInTimeTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJustInTimeTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseUsageData(
            self,
            request: models.DescribeLicenseUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseUsageDataResponse:
        """
        该接口返回查询时间范围内每天 License 请求次数信息。
           1. 可以查询最近365天内的 License 请求次数统计数据。
           2. 查询时间跨度不超过90天。
           3. 查询时间跨度超过1天的，返回以天为粒度的数据，否则，返回以5分钟为粒度的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseUsageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMPSTemplates(
            self,
            request: models.DescribeMPSTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeMPSTemplatesResponse:
        """
        获取用户自定义媒体处理服务（MPS）任务模板。
        查询模板列表时，需要将 MPS 相关参数以 JSON 格式填入 MPSDescribeTemplateParams 参数中。关于具体的任务参数配置方法，请参考 MPS 任务模板相关文档说明。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMPSTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMPSTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMediaInfos(
            self,
            request: models.DescribeMediaInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeMediaInfosResponse:
        """
        1. 该接口可以获取多个媒体文件的多种信息，包括：
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
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMediaInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMediaInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMediaPlayStatDetails(
            self,
            request: models.DescribeMediaPlayStatDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeMediaPlayStatDetailsResponse:
        """
        该接口用于查询媒体文件按指定时间粒度统计的播放数据
        * 可以查询最近一年的播放统计数据。
        * 时间粒度为小时，结束时间和起始时间的跨度最大为7天。
        * 时间粒度为天，结束时间和起始时间的跨度最大为90天。
        * 播放统计仅针对 VOD 域名（即 EdgeOne 域名的分发不计入播放统计）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMediaPlayStatDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMediaPlayStatDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMediaProcessUsageData(
            self,
            request: models.DescribeMediaProcessUsageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeMediaProcessUsageDataResponse:
        """
        该接口返回查询时间范围内每天使用的视频处理用量信息。
           1. 视频处理用量数据系统侧保留 13 个月，您通过接口仅可查询最近 365 天内的用量数据。如需调取超出 365 天的历史用量数据，请联系我们。
           2. 查询时间跨度不超过90天。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMediaProcessUsageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMediaProcessUsageDataResponse
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
        
    async def DescribePrepaidProducts(
            self,
            request: models.DescribePrepaidProductsRequest,
            opts: Dict = None,
    ) -> models.DescribePrepaidProductsResponse:
        """
        该接口可以查询用户已经购买的预付费商品的信息，包括：
            1. 商品的类型、生效和失效日期。
            2. 商品中每种资源的额度和剩余额度。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrepaidProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrepaidProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcedureTemplates(
            self,
            request: models.DescribeProcedureTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeProcedureTemplatesResponse:
        """
        根据任务流模板名字，获取任务流模板详情列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcedureTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcedureTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityInspectTemplates(
            self,
            request: models.DescribeQualityInspectTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityInspectTemplatesResponse:
        """
        获取音画质检测模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityInspectTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityInspectTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRebuildMediaTemplates(
            self,
            request: models.DescribeRebuildMediaTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeRebuildMediaTemplatesResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        获取视频重生模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRebuildMediaTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRebuildMediaTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReviewDetails(
            self,
            request: models.DescribeReviewDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeReviewDetailsResponse:
        """
        <b>本接口已不推荐使用，用 [DescribeMediaProcessUsageData](/document/product/266/41464) 替代</b>

        该接口返回查询时间范围内每天使用的视频内容智能识别时长数据，单位： 秒。

        1. 可以查询最近365天内的视频内容智能识别时长统计数据。
        2. 查询时间跨度不超过90天。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReviewDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReviewDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReviewTemplates(
            self,
            request: models.DescribeReviewTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeReviewTemplatesResponse:
        """
        获取审核模板列表。
        >模板仅适用于 [音视频审核(ReviewAudioVideo)](https://cloud.tencent.com/document/api/266/80283) 和 [图片审核(ReviewImage)](https://cloud.tencent.com/document/api/266/73217) 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReviewTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReviewTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoundPlays(
            self,
            request: models.DescribeRoundPlaysRequest,
            opts: Dict = None,
    ) -> models.DescribeRoundPlaysResponse:
        """
        该接口用于获取轮播播单列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoundPlays"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoundPlaysResponse
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
        
    async def DescribeStorageData(
            self,
            request: models.DescribeStorageDataRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageDataResponse:
        """
        查询存储空间使用情况和文件数量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorageData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStorageDetails(
            self,
            request: models.DescribeStorageDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageDetailsResponse:
        """
        该接口返回查询时间范围内使用的点播存储空间，单位：字节。
            1. 存储用量数据系统侧保留 13 个月，您通过接口仅可查询最近 365 天内的用量数据。如需调取超出 365 天的历史用量数据，请联系我们；
            2. 查询时间跨度不超过90天；
            3. 分钟粒度查询跨度不超过7天；
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorageDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStorageRegions(
            self,
            request: models.DescribeStorageRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageRegionsResponse:
        """
        该接口用于：
          1. 查询点播可开通的所有存储园区列表。
          2. 查询已经开通的园区列表。
          3. 查询默认使用的存储园区。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorageRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubAppIds(
            self,
            request: models.DescribeSubAppIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubAppIdsResponse:
        """
        该接口用于获取当前账号的应用列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubAppIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubAppIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSuperPlayerConfigs(
            self,
            request: models.DescribeSuperPlayerConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeSuperPlayerConfigsResponse:
        """
        该 API 已经<font color='red'>不再维护</font>，新版播放器签名不再使用播放器配置模板，详细请参考 [播放器签名](https://cloud.tencent.com/document/product/266/45554)。
        查询播放器配置，支持根据条件，分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSuperPlayerConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSuperPlayerConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskDetail(
            self,
            request: models.DescribeTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskDetailResponse:
        """
        通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询3天之内提交的任务）。
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
        * 只能查询到最近三天（72 小时）内的任务。
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
        
    async def DescribeVodDomains(
            self,
            request: models.DescribeVodDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeVodDomainsResponse:
        """
        该接口用于查询点播域名信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVodDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVodDomainsResponse
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
        
    async def EditMedia(
            self,
            request: models.EditMediaRequest,
            opts: Dict = None,
    ) -> models.EditMediaResponse:
        """
        对视频进行编辑（剪辑、拼接等），生成一个新的点播视频。编辑的功能包括：

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
        """
        
        kwargs = {}
        kwargs["action"] = "EditMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnhanceMediaByTemplate(
            self,
            request: models.EnhanceMediaByTemplateRequest,
            opts: Dict = None,
    ) -> models.EnhanceMediaByTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，请使用新版接口 [音画质重生](https://cloud.tencent.com/document/api/266/102571)。
        使用模板发起音画质重生。
        """
        
        kwargs = {}
        kwargs["action"] = "EnhanceMediaByTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnhanceMediaByTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnhanceMediaQuality(
            self,
            request: models.EnhanceMediaQualityRequest,
            opts: Dict = None,
    ) -> models.EnhanceMediaQualityResponse:
        """
        对点播中的音视频媒体发起音画质重生任务。
        """
        
        kwargs = {}
        kwargs["action"] = "EnhanceMediaQuality"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnhanceMediaQualityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteFunction(
            self,
            request: models.ExecuteFunctionRequest,
            opts: Dict = None,
    ) -> models.ExecuteFunctionResponse:
        """
        本接口仅用于定制开发的特殊场景，除非云点播客服人员主动告知您需要使用本接口，其它情况请勿调用。
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractCopyRightWatermark(
            self,
            request: models.ExtractCopyRightWatermarkRequest,
            opts: Dict = None,
    ) -> models.ExtractCopyRightWatermarkResponse:
        """
        如果有盗录溯源需求，请参考 [幽灵水印](https://cloud.tencent.com/document/product/266/94228)。
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractCopyRightWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractCopyRightWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractTraceWatermark(
            self,
            request: models.ExtractTraceWatermarkRequest,
            opts: Dict = None,
    ) -> models.ExtractTraceWatermarkResponse:
        """
        如果有盗录溯源需求，推荐使用 [幽灵水印](https://cloud.tencent.com/document/product/266/94228)。
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractTraceWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractTraceWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FastEditMedia(
            self,
            request: models.FastEditMediaRequest,
            opts: Dict = None,
    ) -> models.FastEditMediaResponse:
        """
        对云点播的 HLS 视频实现快速拼接和快速剪辑，生成新的 HLS 格式的媒体。

        快速拼接或剪辑生成的视频，将产生新的 FileId 并进行固化，固化成功后新视频的文件独立于原始输入视频存在，不受原始视频删除等影响。

        <font color='red'>注意：</font>通过 ModifyEventConfig 接口启用接收剪辑固化事件通知，固化成功后将会收到一个 PersistenceComplete 类型的事件通知。在收到这个事件通知之前，不应该对原始输入的视频进行删除、降冷等操作，否则拼接剪辑生成的视频播放可能出现异常。
        """
        
        kwargs = {}
        kwargs["action"] = "FastEditMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FastEditMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForbidMediaDistribution(
            self,
            request: models.ForbidMediaDistributionRequest,
            opts: Dict = None,
    ) -> models.ForbidMediaDistributionResponse:
        """
        * 对媒体禁播后，除了点播控制台预览，其他场景访问视频各种资源的 URL（原始文件、转码输出文件、截图等）均会返回 403。
          禁播/解禁操作全网生效时间约 5~10 分钟。
        * 注意：禁播媒体仅能操作标准存储和低频存储的媒体。低频存储媒体，必须存储至少 30 天，提前删除或变更存储类型，仍旧按照 30 天计费；如果禁播低频存储媒体，该媒体低频存储的时长不足 30 天，会产生提前删除计费；同时，禁播后该媒体的低频存储时长会从当前时间重新开始计算，如果不满 30 天继续对该媒体进行删除或变更存储类型，也将产生提前删除计费。例：媒体 001 已经低频存储了 10 天，此时对 001 进行禁播，低频存储的计费仍旧按 30 天计算（提前删除计费时长为 30 - 10 = 20 天）；禁播后 001 的低频存储时长重新开始计算，如果禁播后第 5 天删除了 001，低频存储计费也会按 30 天计算（提前删除计费时长为 30 - 5 = 25 天）；001 实际的低频存储时长为 10 + 5 = 15 天，低频存储计费时长为 10 + 20(提前删除计费)+ 5 + 25(提前删除计费) = 60 天。
        """
        
        kwargs = {}
        kwargs["action"] = "ForbidMediaDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForbidMediaDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HandleCurrentPlaylist(
            self,
            request: models.HandleCurrentPlaylistRequest,
            opts: Dict = None,
    ) -> models.HandleCurrentPlaylistResponse:
        """
        操作轮播当前播放列表。支持的操作有：<li> Insert：向当前播列表插入播放节目。</li><li> Delete：删除播列表中的播放节目。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "HandleCurrentPlaylist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HandleCurrentPlaylistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportMediaKnowledge(
            self,
            request: models.ImportMediaKnowledgeRequest,
            opts: Dict = None,
    ) -> models.ImportMediaKnowledgeResponse:
        """
        用于将智能分析的结果导入到知识库中。
        """
        
        kwargs = {}
        kwargs["action"] = "ImportMediaKnowledge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportMediaKnowledgeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InspectMediaQuality(
            self,
            request: models.InspectMediaQualityRequest,
            opts: Dict = None,
    ) -> models.InspectMediaQualityResponse:
        """
        对点播中的音视频媒体发起音画质检测任务。
        """
        
        kwargs = {}
        kwargs["action"] = "InspectMediaQuality"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InspectMediaQualityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LiveRealTimeClip(
            self,
            request: models.LiveRealTimeClipRequest,
            opts: Dict = None,
    ) -> models.LiveRealTimeClipResponse:
        """
        直播即时剪辑，是指在直播过程中（即直播尚未结束时），客户可以在过往直播内容中选择一段，实时生成一个新的视频（HLS 格式），开发者可以将其立即分享出去，或者长久保存起来。

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

        <font color='red'>注意：</font>如果剪辑时指定进行固化，通过 ModifyEventConfig 接口启用接收剪辑固化事件通知，固化成功后将会收到一个 PersistenceComplete 类型的事件通知。在收到这个事件通知之前，不应该对直播录制视频进行删除、降冷等操作，否则剪辑生成的视频播放可能出现异常。

        ### 剪辑不固化
        所谓剪辑不固化，是指剪辑所得到的结果（m3u8 文件）与直播录制视频共享相同的 ts 分片，新生成的视频不是一个独立完整的视频（没有独立 FileId，只有播放 URL），其有效期与直播录制的完整视频有效期是一致的。一旦直播录制出来的视频被删除，也会导致该片段无法播放。

        剪辑不固化，由于其剪辑结果不是一个独立的视频，因而也不会纳入点播媒资视频管理（例如控制台的视频总数不会统计这一片段）中，也无法单独针对这个片段做转码、微信发布等任何视频处理操作。

        剪辑不固化的优势在于其剪辑操作十分“轻量化”，不会产生额外的存储开销。但其不足之处在于生命周期与原始录制视频相同，且无法进一步进行转码等视频处理。
        """
        
        kwargs = {}
        kwargs["action"] = "LiveRealTimeClip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LiveRealTimeClipResponse
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
        修改用户自定义音视频内容分析模板。

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
        修改用户自定义音视频内容识别模板。
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
        
    async def ModifyClass(
            self,
            request: models.ModifyClassRequest,
            opts: Dict = None,
    ) -> models.ModifyClassResponse:
        """
        修改媒体分类属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyContentReviewTemplate(
            self,
            request: models.ModifyContentReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyContentReviewTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版审核模板支持音视频审核和图片审核，详细请参考 [修改审核模板](https://cloud.tencent.com/document/api/266/84388)。
        修改用户自定义音视频内容审核模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContentReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContentReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDefaultDistributionConfig(
            self,
            request: models.ModifyDefaultDistributionConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDefaultDistributionConfigResponse:
        """
        该接口用于修改默认分发配置。
        * 分发域名和分发协议，即媒体文件分发 URL 中的域名和协议。媒体文件按默认分发配置进行分发。
        * 播放密钥，用于计算播放器签名。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDefaultDistributionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDefaultDistributionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDefaultStorageRegion(
            self,
            request: models.ModifyDefaultStorageRegionRequest,
            opts: Dict = None,
    ) -> models.ModifyDefaultStorageRegionResponse:
        """
        该接口用于设置默认的存储地域。上传文件时如果没有指定地域，将上传到默认地域。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDefaultStorageRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDefaultStorageRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnhanceMediaTemplate(
            self,
            request: models.ModifyEnhanceMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyEnhanceMediaTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        修改音画质重生模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnhanceMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnhanceMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEventConfig(
            self,
            request: models.ModifyEventConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyEventConfigResponse:
        """
        腾讯云点播为客户提供了媒体上传、媒体管理、媒体处理等等服务，在这些服务执行过程或执行结束时，腾讯云点播也提供各种对应的事件通知，方便开发者感知服务处理状态，并做下一步的业务操作。

        开发者可以通过调用本接口来实现：
        - 设置接收回调通知的类型，目前有[ HTTP 回调通知](https://cloud.tencent.com/document/product/266/33779) 和 [基于消息队列的可靠通知](https://cloud.tencent.com/document/product/266/33779) 两种类型。
        - 对于[ HTTP 回调通知](https://cloud.tencent.com/document/product/266/33779)，可设置 3.0 格式回调的地址。3.0 格式回调的说明参见 [历史格式回调](https://cloud.tencent.com/document/product/266/33796)。
        - 对具体事件服务的通知事件选择设置接收或者忽略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEventConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEventConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHeadTailTemplate(
            self,
            request: models.ModifyHeadTailTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyHeadTailTemplateResponse:
        """
        修改片头片尾模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHeadTailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHeadTailTemplateResponse
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
        
    async def ModifyJustInTimeTranscodeTemplate(
            self,
            request: models.ModifyJustInTimeTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyJustInTimeTranscodeTemplateResponse:
        """
        修改即时转码模板。
        - 注意：即时转码模板创建后，不推荐修改，如需修改参数，推荐使用新增模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMPSTemplate(
            self,
            request: models.ModifyMPSTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyMPSTemplateResponse:
        """
        修改用户自定义 MPS 任务模板。
        修改模板时，需要将 MPS 相关参数以 JSON 格式填入 MPSModifyTemplateParams 参数中。关于具体的任务参数配置方法，请参考 MPS 任务模板相关文档说明。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMPSTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMPSTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMediaInfo(
            self,
            request: models.ModifyMediaInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyMediaInfoResponse:
        """
        修改媒体文件的属性，包括分类、名称、描述、标签、过期时间、打点信息、视频封面、字幕信息等。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMediaInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMediaInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMediaStorageClass(
            self,
            request: models.ModifyMediaStorageClassRequest,
            opts: Dict = None,
    ) -> models.ModifyMediaStorageClassResponse:
        """
        修改媒体文件的存储类型。
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
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMediaStorageClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMediaStorageClassResponse
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
        
    async def ModifyQualityInspectTemplate(
            self,
            request: models.ModifyQualityInspectTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyQualityInspectTemplateResponse:
        """
        修改音画质检测模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyQualityInspectTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyQualityInspectTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRebuildMediaTemplate(
            self,
            request: models.ModifyRebuildMediaTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyRebuildMediaTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，新版 [音画质重生](https://cloud.tencent.com/document/product/266/102571) 接口使用预置模板，详情请参见 [音画质重生模板](https://cloud.tencent.com/document/product/266/102586#50604b3f-0286-4a10-a3f7-18218116aff7)。
        修改视频重生模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRebuildMediaTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRebuildMediaTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReviewTemplate(
            self,
            request: models.ModifyReviewTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyReviewTemplateResponse:
        """
        修改用户自定义审核模板。
        >模板仅适用于 [音视频审核(ReviewAudioVideo)](https://cloud.tencent.com/document/api/266/80283) 和 [图片审核(ReviewImage)](https://cloud.tencent.com/document/api/266/73217) 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReviewTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReviewTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoundPlay(
            self,
            request: models.ModifyRoundPlayRequest,
            opts: Dict = None,
    ) -> models.ModifyRoundPlayResponse:
        """
        该接口用于修改轮播播单。
        修改后只有新的播放请求会生效，已经在播放中的用户在七天之内还可以播放修改前的播单。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoundPlay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoundPlayResponse
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
        
    async def ModifySubAppIdInfo(
            self,
            request: models.ModifySubAppIdInfoRequest,
            opts: Dict = None,
    ) -> models.ModifySubAppIdInfoResponse:
        """
        该接口用于修改应用信息，但不允许修改默认应用信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubAppIdInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubAppIdInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubAppIdStatus(
            self,
            request: models.ModifySubAppIdStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySubAppIdStatusResponse:
        """
        该接口用于启用、停用应用。被停用的应用将封停对应域名，并限制控制台访问。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubAppIdStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubAppIdStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySuperPlayerConfig(
            self,
            request: models.ModifySuperPlayerConfigRequest,
            opts: Dict = None,
    ) -> models.ModifySuperPlayerConfigResponse:
        """
        该 API 已经<font color='red'>不再维护</font>，新版播放器签名不再使用播放器配置模板，详细请参考 [播放器签名](https://cloud.tencent.com/document/product/266/45554)。
        修改播放器配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySuperPlayerConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySuperPlayerConfigResponse
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
        
    async def ModifyVodDomainAccelerateConfig(
            self,
            request: models.ModifyVodDomainAccelerateConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyVodDomainAccelerateConfigResponse:
        """
        该接口用于修改点播域名的加速区域。
        1、域名部署状态为 Online 状态时才允许修改加速区域。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVodDomainAccelerateConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVodDomainAccelerateConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVodDomainConfig(
            self,
            request: models.ModifyVodDomainConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyVodDomainConfigResponse:
        """
        该接口用于修改域名配置，可以修改域名的防盗链配置。
        1、域名部署状态为 Online 状态时才允许修改域名的配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVodDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVodDomainConfigResponse
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
        
    async def ParseStreamingManifest(
            self,
            request: models.ParseStreamingManifestRequest,
            opts: Dict = None,
    ) -> models.ParseStreamingManifestResponse:
        """
        上传 HLS 视频时，解析索引文件内容，返回待上传的分片文件列表。分片文件路径必须是当前目录或子目录的相对路径，不能是 URL，不能是绝对路径。
        """
        
        kwargs = {}
        kwargs["action"] = "ParseStreamingManifest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseStreamingManifestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessImage(
            self,
            request: models.ProcessImageRequest,
            opts: Dict = None,
    ) -> models.ProcessImageResponse:
        """
        该 API 已经<font color='red'>不再维护</font>，智能识别任务请使用图片智能识别 [ReviewImage](https://cloud.tencent.com/document/api/266/73217) 接口。

        对点播中的图片文件发起处理任务，功能包括：

        1. 智能识别（令人反感的信息、不安全的信息、不适宜的信息）;

        ><li>图片文件大小支持：文件 < 5M；</li>
        ><li>图片文件分辨率支持：建议分辨率大于256x256，否则可能会影响识别效果；</li>
        ><li>图片文件支持格式：PNG、JPG、JPEG、BMP、GIF、WEBP格式。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMedia(
            self,
            request: models.ProcessMediaRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaResponse:
        """
        对点播中的音视频媒体发起处理任务，功能包括：
        1. 视频转码（带水印）；
        2. 视频转动图；
        3. 对视频按指定时间点截图；
        4. 对视频采样截图；
        5. 对视频截取雪碧图；
        6. 对视频截取一张图做封面；
        7. 对视频转自适应码流（并加密）；
        8. 内容审核（令人反感的信息、不安全的信息、不适宜的信息），<font color=red>不建议</font> 使用该接口发起，推荐使用 [音视频审核(ReviewAudioVideo)](https://cloud.tencent.com/document/api/266/80283) 或 [图片审核(ReviewImage)](https://cloud.tencent.com/document/api/266/73217)；
        9. 内容分析（标签、分类、封面、按帧标签），暂时不支持 HLS 格式；
        10. 内容识别（视频片头片尾、人脸、文本全文、文本关键词、语音全文、语音关键词、物体）。

        如使用事件通知，事件通知的类型为 [任务流状态变更](https://cloud.tencent.com/document/product/266/9636)。
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMediaByMPS(
            self,
            request: models.ProcessMediaByMPSRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaByMPSResponse:
        """
        使用媒体处理服务（MPS）的媒体处理能力，对点播中的视频发起媒体处理，任务发起时需将 MPS 相关参数以 JSON 格式填入 MPSProcessMediaParams 参数中。具体任务参数配置请参考[媒体处理 ProcessMedia 接口](https://cloud.tencent.com/document/api/862/37578)。
        当前支持的 MPS 功能：
        1. [智能擦除](https://cloud.tencent.com/document/product/862/101530)：能够对视频画面中的 Logo、字幕、人脸和车牌等元素进行模糊、马赛克或无痕化处理，从而便于内容的传播和分享。该任务产生的新视频将生成新的 FileId 存储在点播平台的子应用中。
        2. [音视频增强](https://cloud.tencent.com/document/product/862/118703)：该功能支持分布式实时画质增强，包含视频去毛刺、降噪、色彩增强、细节增强、人脸增强、SDR2HDR、大模型增强等功能，可大幅提升音视频质量，广泛应用于 OTT、电商、赛事等场景，有效实现 QoE 与 QoS 双维度提升，创造显著业务价值。

        > 以该种方式发起的视频处理任务：
        > 1. 任务状态及结果的查询仍在点播平台中完成，使用 [DescribeTaskDetail](https://cloud.tencent.com/document/product/266/33431) 或 [DescribeTasks](https://cloud.tencent.com/document/product/266/33430) 查询任务。
        > 2. 相关功能的用量及账单将在 MPS 平台给出，因此在使用该功能前，首先需要开通 MPS 服务。
        > 3. 该功能目前仍在内测中，如需测试体验，您可以联系我们获得支持。
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMediaByMPS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMediaByMPSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMediaByProcedure(
            self,
            request: models.ProcessMediaByProcedureRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaByProcedureResponse:
        """
        使用任务流模板，对点播中的视频发起处理任务。
        有两种方式创建任务流模板：
        1. 在控制台上创建和修改任务流模板；
        2. 通过任务流模板接口创建任务流模板。

        如使用事件通知，除音视频审核任务外的事件通知的类型为 [任务流状态变更](https://cloud.tencent.com/document/product/266/9636)；音视频审核任务事件通知的类型为 [音视频审核完成](https://cloud.tencent.com/document/product/266/81258)。
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMediaByProcedure"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMediaByProcedureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ProcessMediaByUrl(
            self,
            request: models.ProcessMediaByUrlRequest,
            opts: Dict = None,
    ) -> models.ProcessMediaByUrlResponse:
        """
        该 API 已经<font color='red'>不再维护</font>，请使用 MPS 产品的 [ProcessMedia](https://cloud.tencent.com/document/product/862/37578) 接口，在入参 InputInfo.UrlInputInfo.Url 中指定视频 URL。
        """
        
        kwargs = {}
        kwargs["action"] = "ProcessMediaByUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ProcessMediaByUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullEvents(
            self,
            request: models.PullEventsRequest,
            opts: Dict = None,
    ) -> models.PullEventsResponse:
        """
        * 该接口用于业务服务器以 [可靠回调](https://cloud.tencent.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83) 的方式获取事件通知；
        * 接口为长轮询模式，即：如果服务端存在未消费事件，则立即返回给请求方；如果服务端没有未消费事件，则后台会将请求挂起，直到有新的事件产生为止；
        * 请求最多挂起5秒，建议请求方将超时时间设置为10秒；
        * 未被拉取的事件通知最多保留4天，超过该时限的事件通知可能会被清除；
        * 若该接口有事件返回，调用方必须在<font color="red">30秒</font>内调用 [确认事件通知](https://cloud.tencent.com/document/product/266/33434) 接口，确认事件通知已经处理，否则该事件通知在<font color="red">30秒</font>后会再次被拉取到。
        * 当前，API 每次最多可以获取16个事件通知。
        """
        
        kwargs = {}
        kwargs["action"] = "PullEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullUpload(
            self,
            request: models.PullUploadRequest,
            opts: Dict = None,
    ) -> models.PullUploadResponse:
        """
        该接口用于将一个网络上的视频拉取到云点播平台。
        """
        
        kwargs = {}
        kwargs["action"] = "PullUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PushUrlCache(
            self,
            request: models.PushUrlCacheRequest,
            opts: Dict = None,
    ) -> models.PushUrlCacheResponse:
        """
        1. 预热指定的 URL 列表。
        2. URL 的域名必须已在云点播中注册。
        3. 单次请求最多指定20个 URL。
        4. 默认预热配额为每天10000个 URL。
        """
        
        kwargs = {}
        kwargs["action"] = "PushUrlCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PushUrlCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebuildMedia(
            self,
            request: models.RebuildMediaRequest,
            opts: Dict = None,
    ) -> models.RebuildMediaResponse:
        """
        该 API 已经<font color=red>不再维护</font>，请使用新版接口 [音画质重生](https://cloud.tencent.com/document/api/266/102571)。
        发起音画质重生
        """
        
        kwargs = {}
        kwargs["action"] = "RebuildMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebuildMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebuildMediaByTemplate(
            self,
            request: models.RebuildMediaByTemplateRequest,
            opts: Dict = None,
    ) -> models.RebuildMediaByTemplateResponse:
        """
        该 API 已经<font color=red>不再维护</font>，请使用新版接口 [音画质重生](https://cloud.tencent.com/document/api/266/102571)。
        使用模板发起视频重生。
        """
        
        kwargs = {}
        kwargs["action"] = "RebuildMediaByTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebuildMediaByTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshUrlCache(
            self,
            request: models.RefreshUrlCacheRequest,
            opts: Dict = None,
    ) -> models.RefreshUrlCacheResponse:
        """
        1. 刷新指定的 URL 列表。
        2. URL 的域名必须已在云点播中注册。
        3. 单次请求最多指定20个 URL。
        4. 默认刷新配额为每天100000个 URL。
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshUrlCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshUrlCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveWatermark(
            self,
            request: models.RemoveWatermarkRequest,
            opts: Dict = None,
    ) -> models.RemoveWatermarkResponse:
        """
        智能去除水印
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetProcedureTemplate(
            self,
            request: models.ResetProcedureTemplateRequest,
            opts: Dict = None,
    ) -> models.ResetProcedureTemplateResponse:
        """
        重新设置用户自定义任务流模板的内容。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetProcedureTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetProcedureTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreMedia(
            self,
            request: models.RestoreMediaRequest,
            opts: Dict = None,
    ) -> models.RestoreMediaResponse:
        """
        当媒体文件的存储类型是归档存储或深度归档存储时，是不可访问的。如需访问，则需要调用本接口进行解冻，解冻后可访问的媒体文件是临时的，在有效期过后，则不可访问。
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReviewAudioVideo(
            self,
            request: models.ReviewAudioVideoRequest,
            opts: Dict = None,
    ) -> models.ReviewAudioVideoResponse:
        """
        对点播中的音视频媒体发起审核任务，智能检测视频画面、画面中的文字、语音中的文字、声音出现的违规内容。

        如使用事件通知，事件通知的类型为 [音视频审核完成](https://cloud.tencent.com/document/product/266/81258)。
        """
        
        kwargs = {}
        kwargs["action"] = "ReviewAudioVideo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReviewAudioVideoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReviewImage(
            self,
            request: models.ReviewImageRequest,
            opts: Dict = None,
    ) -> models.ReviewImageResponse:
        """
        对点播中的图片文件发起审核（令人反感的信息、不安全的信息、不适宜的信息）任务。

        ><li>图片文件大小支持：文件 < 5M；</li>
        ><li>图片文件分辨率支持：建议分辨率大于256x256，否则可能会影响审核效果；</li>
        ><li>图片文件支持格式：PNG、JPG、JPEG、BMP、GIF、WEBP格式。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "ReviewImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReviewImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchMedia(
            self,
            request: models.SearchMediaRequest,
            opts: Dict = None,
    ) -> models.SearchMediaResponse:
        """
        搜索媒体信息，支持多种条件筛选，以及支持对返回结果排序、过滤等功能，具体包括：
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
        """
        
        kwargs = {}
        kwargs["action"] = "SearchMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchMediaBySemantics(
            self,
            request: models.SearchMediaBySemanticsRequest,
            opts: Dict = None,
    ) -> models.SearchMediaBySemanticsResponse:
        """
        使用自然语言对媒体进行语义搜索。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchMediaBySemantics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchMediaBySemanticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetCLSPushTarget(
            self,
            request: models.SetCLSPushTargetRequest,
            opts: Dict = None,
    ) -> models.SetCLSPushTargetResponse:
        """
        为点播域名设置投递 CLS 的目标。
        """
        
        kwargs = {}
        kwargs["action"] = "SetCLSPushTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetCLSPushTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetDrmKeyProviderInfo(
            self,
            request: models.SetDrmKeyProviderInfoRequest,
            opts: Dict = None,
    ) -> models.SetDrmKeyProviderInfoResponse:
        """
        设置 DRM 密钥提供商信息。
        """
        
        kwargs = {}
        kwargs["action"] = "SetDrmKeyProviderInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetDrmKeyProviderInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetVodDomainCertificate(
            self,
            request: models.SetVodDomainCertificateRequest,
            opts: Dict = None,
    ) -> models.SetVodDomainCertificateResponse:
        """
        设置点播域名 HTTPS 证书。
        """
        
        kwargs = {}
        kwargs["action"] = "SetVodDomainCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetVodDomainCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SimpleHlsClip(
            self,
            request: models.SimpleHlsClipRequest,
            opts: Dict = None,
    ) -> models.SimpleHlsClipResponse:
        """
        对 HLS 视频进行按时间段裁剪，实时生成一个新的视频（HLS 格式），开发者可以将其立即分享出去，或者长久保存起来。

        腾讯云点播支持两种剪辑模式：
        - 剪辑固化：将剪辑出来的视频保存成独立的视频，拥有独立 FileId；适用于将精彩片段长久保存的场景；
        - 剪辑不固化：剪辑得到的视频附属于输入文件，没有独立 FileId；适用于将精彩片段临时分享的场景。

        该接口基于输入 m3u8 文件进行裁剪，其最小剪辑精度为一个 ts 切片，无法实现秒级或者更为精确的剪辑精度。

        ### 剪辑固化
        所谓剪辑固化，是指将剪辑出来的视频保存成一个独立的视频（拥有独立的 FileId）。其生命周期不受原始输入视频影响（即使原始输入视频被删除，剪辑结果也不会受到任何影响）；也可以对其进行转码、微信发布等二次处理。

        举例如下：一场完整的足球比赛，原始视频可能长达 2 个小时，客户出于节省成本的目的可以对这个视频存储 2 个月，但对于剪辑的「精彩时刻」视频却可以指定存储更长时间，同时可以单独对「精彩时刻」视频进行转码、微信发布等额外的点播操作，这时候可以选择剪辑并且固化的方案。

        剪辑固化的优势在于其生命周期与原始输入视频相互独立，可以独立管理、长久保存。

        <font color='red'>注意：</font>如果剪辑时指定进行固化，通过 ModifyEventConfig 接口启用接收剪辑固化事件通知，固化成功后将会收到一个 PersistenceComplete 类型的事件通知。在收到这个事件通知之前，不应该对原始输入的视频进行删除、降冷等操作，否则剪辑生成的视频播放可能出现异常。

        ### 剪辑不固化
        所谓剪辑不固化，是指剪辑所得到的结果（m3u8 文件）与原始输入视频共享相同的 ts 分片，新生成的视频不是一个独立完整的视频（没有独立 FileId，只有播放 URL），其有效期与原始输入的完整视频有效期是一致的。一旦原始输入的视频被删除，也会导致该片段无法播放。

        剪辑不固化，由于其剪辑结果不是一个独立的视频，因而也不会纳入点播媒资视频管理（例如控制台的视频总数不会统计这一片段）中，也无法单独针对这个片段做转码、微信发布等任何视频处理操作。

        剪辑不固化的优势在于其剪辑操作十分“轻量化”，不会产生额外的存储开销。但其不足之处在于生命周期与原始录制视频相同，且无法进一步进行转码等视频处理。
        """
        
        kwargs = {}
        kwargs["action"] = "SimpleHlsClip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SimpleHlsClipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SplitMedia(
            self,
            request: models.SplitMediaRequest,
            opts: Dict = None,
    ) -> models.SplitMediaResponse:
        """
        对点播视频进行拆条，生成多个新的点播视频。
        """
        
        kwargs = {}
        kwargs["action"] = "SplitMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SplitMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyDomainRecord(
            self,
            request: models.VerifyDomainRecordRequest,
            opts: Dict = None,
    ) -> models.VerifyDomainRecordResponse:
        """
        该接口用于验证域名解析值。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyDomainRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyDomainRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def WeChatMiniProgramPublish(
            self,
            request: models.WeChatMiniProgramPublishRequest,
            opts: Dict = None,
    ) -> models.WeChatMiniProgramPublishResponse:
        """
        将点播视频发布到微信小程序，供微信小程序播放器播放。
        本接口支持发布原始视频和转码后视频，暂不支持发布自适应码流。
        """
        
        kwargs = {}
        kwargs["action"] = "WeChatMiniProgramPublish"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.WeChatMiniProgramPublishResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)