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
from tencentcloud.live.v20180801 import models
from typing import Dict


class LiveClient(AbstractClient):
    _apiVersion = '2018-08-01'
    _endpoint = 'live.tencentcloudapi.com'
    _service = 'live'

    async def AddCasterInputInfo(
            self,
            request: models.AddCasterInputInfoRequest,
            opts: Dict = None,
    ) -> models.AddCasterInputInfoResponse:
        """
        该接口用来向导播台中添加一个输入源，该输入源可以是拉流地址、或是一个文件链接
        """
        
        kwargs = {}
        kwargs["action"] = "AddCasterInputInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCasterInputInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCasterLayoutInfo(
            self,
            request: models.AddCasterLayoutInfoRequest,
            opts: Dict = None,
    ) -> models.AddCasterLayoutInfoResponse:
        """
        该接口用来增加导播台的布局参数。
        """
        
        kwargs = {}
        kwargs["action"] = "AddCasterLayoutInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCasterLayoutInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCasterMarkPicInfo(
            self,
            request: models.AddCasterMarkPicInfoRequest,
            opts: Dict = None,
    ) -> models.AddCasterMarkPicInfoResponse:
        """
        该接口用来新增图片水印。
        """
        
        kwargs = {}
        kwargs["action"] = "AddCasterMarkPicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCasterMarkPicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCasterMarkWordInfo(
            self,
            request: models.AddCasterMarkWordInfoRequest,
            opts: Dict = None,
    ) -> models.AddCasterMarkWordInfoResponse:
        """
        为导播台添加文本配置。
        """
        
        kwargs = {}
        kwargs["action"] = "AddCasterMarkWordInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCasterMarkWordInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCasterOutputInfo(
            self,
            request: models.AddCasterOutputInfoRequest,
            opts: Dict = None,
    ) -> models.AddCasterOutputInfoResponse:
        """
        该接口用来新增导播台推流信息。导播台主监启动后，将会将主监画面推向该接口设置的地址。
        """
        
        kwargs = {}
        kwargs["action"] = "AddCasterOutputInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCasterOutputInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddDelayLiveStream(
            self,
            request: models.AddDelayLiveStreamRequest,
            opts: Dict = None,
    ) -> models.AddDelayLiveStreamResponse:
        """
        针对大型活动直播，通过对直播流设置延时来控制现场与观众播放画面的时间间隔，避免突发状况造成影响。

        注意：如果在推流前设置延播，需要提前5分钟设置，目前该接口只支持流粒度。
        """
        
        kwargs = {}
        kwargs["action"] = "AddDelayLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDelayLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddLiveDomain(
            self,
            request: models.AddLiveDomainRequest,
            opts: Dict = None,
    ) -> models.AddLiveDomainResponse:
        """
        添加域名，一次只能提交一个域名。域名必须已备案。
        """
        
        kwargs = {}
        kwargs["action"] = "AddLiveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddLiveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddLiveWatermark(
            self,
            request: models.AddLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.AddLiveWatermarkResponse:
        """
        添加水印，成功返回水印 ID 后，需要调用[CreateLiveWatermarkRule](/document/product/267/32629)接口将水印 ID 绑定到流使用。 水印数量上限 100，超过后需要先删除，再添加。
        """
        
        kwargs = {}
        kwargs["action"] = "AddLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AuthenticateDomainOwner(
            self,
            request: models.AuthenticateDomainOwnerRequest,
            opts: Dict = None,
    ) -> models.AuthenticateDomainOwnerResponse:
        """
        验证用户是否拥有特定直播域名。
        """
        
        kwargs = {}
        kwargs["action"] = "AuthenticateDomainOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AuthenticateDomainOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelCommonMixStream(
            self,
            request: models.CancelCommonMixStreamRequest,
            opts: Dict = None,
    ) -> models.CancelCommonMixStreamResponse:
        """
        该接口用来取消混流。用法与 mix_streamv2.cancel_mix_stream 基本一致。
        """
        
        kwargs = {}
        kwargs["action"] = "CancelCommonMixStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelCommonMixStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyCaster(
            self,
            request: models.CopyCasterRequest,
            opts: Dict = None,
    ) -> models.CopyCasterResponse:
        """
        该接口用来复制导播台配置
        """
        
        kwargs = {}
        kwargs["action"] = "CopyCaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyCasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditKeywords(
            self,
            request: models.CreateAuditKeywordsRequest,
            opts: Dict = None,
    ) -> models.CreateAuditKeywordsResponse:
        """
        创建关键词，并关联到关键词库。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditKeywords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditKeywordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCaster(
            self,
            request: models.CreateCasterRequest,
            opts: Dict = None,
    ) -> models.CreateCasterResponse:
        """
        该接口用来创建新的导播台
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCasterInputPushUrl(
            self,
            request: models.CreateCasterInputPushUrlRequest,
            opts: Dict = None,
    ) -> models.CreateCasterInputPushUrlResponse:
        """
        该接口用来生成导播台推流地址
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCasterInputPushUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCasterInputPushUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCasterPgm(
            self,
            request: models.CreateCasterPgmRequest,
            opts: Dict = None,
    ) -> models.CreateCasterPgmResponse:
        """
        该接口用来启动主监任务，并将获取主监画面的播放地址。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCasterPgm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCasterPgmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCasterPgmFromPvw(
            self,
            request: models.CreateCasterPgmFromPvwRequest,
            opts: Dict = None,
    ) -> models.CreateCasterPgmFromPvwResponse:
        """
        该接口用来将预监画面的布局、水印、字幕等配置，复制到主监画面中。
        该接口使用时，预监任务需处于运行状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCasterPgmFromPvw"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCasterPgmFromPvwResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCasterPvw(
            self,
            request: models.CreateCasterPvwRequest,
            opts: Dict = None,
    ) -> models.CreateCasterPvwResponse:
        """
        该接口用来启动预监任务，并将获取预监画面的播放地址。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCasterPvw"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCasterPvwResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCommonMixStream(
            self,
            request: models.CreateCommonMixStreamRequest,
            opts: Dict = None,
    ) -> models.CreateCommonMixStreamResponse:
        """
        该接口用来创建通用混流。用法与旧接口 mix_streamv2.start_mix_stream_advanced 基本一致。
        注意：当前最多支持16路混流。
        最佳实践：https://cloud.tencent.com/document/product/267/45566
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCommonMixStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCommonMixStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveCallbackRule(
            self,
            request: models.CreateLiveCallbackRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveCallbackRuleResponse:
        """
        创建回调规则，需要先调用[CreateLiveCallbackTemplate](/document/product/267/32637)接口创建回调模板，将返回的模板id绑定到域名/路径进行使用。
        <br>回调协议相关文档：[事件消息通知](/document/product/267/32744)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveCallbackRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveCallbackRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveCallbackTemplate(
            self,
            request: models.CreateLiveCallbackTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveCallbackTemplateResponse:
        """
        创建回调模板，数量上限：50，成功返回模板id后，需要调用[CreateLiveCallbackRule](/document/product/267/32638)接口将模板 ID 绑定到域名/路径使用。
        <br>回调协议相关文档：[事件消息通知](/document/product/267/32744)。
        注意：至少填写一个回调 URL。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveCallbackTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveCallbackTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLivePadRule(
            self,
            request: models.CreateLivePadRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLivePadRuleResponse:
        """
        创建直播垫片规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLivePadRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLivePadRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLivePadTemplate(
            self,
            request: models.CreateLivePadTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLivePadTemplateResponse:
        """
        创建直播垫片模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLivePadTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLivePadTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLivePullStreamTask(
            self,
            request: models.CreateLivePullStreamTaskRequest,
            opts: Dict = None,
    ) -> models.CreateLivePullStreamTaskResponse:
        """
        创建直播拉流任务。支持将外部已有的点播文件，或者直播源拉取过来转推到指定的目标地址。
        注意：
        1. 默认支持任务数上限200个，如有特殊需求，可通过提单到售后进行评估增加上限。
        2. 源流视频编码目前只支持: H264, H265。其他编码格式建议先进行转码处理。
        3. 源流音频编码目前只支持: AAC。其他编码格式建议先进行转码处理。
        4. 可在控制台开启过期自动清理，避免过期任务占用任务数额度。
        5. 拉流转推功能为计费增值服务，计费规则详情可参见[计费文档](https://cloud.tencent.com/document/product/267/53308)。
        6. 拉流转推功能仅提供内容拉取与推送服务，请确保内容已获得授权并符合内容传播相关的法律法规。若内容有侵权或违规相关问题，云直播会停止相关的功能服务并保留追究法律责任的权利。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLivePullStreamTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLivePullStreamTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveRecord(
            self,
            request: models.CreateLiveRecordRequest,
            opts: Dict = None,
    ) -> models.CreateLiveRecordResponse:
        """
        - 使用前提
          1. 录制文件存放于点播平台，所以用户如需使用录制功能，需首先自行开通点播服务。
          2. 录制文件存放后相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，具体请参考 [对应文档](https://cloud.tencent.com/document/product/266/2838)。

        - 模式说明
          该接口支持两种录制模式：
          1. 定时录制模式【默认模式】。
            需要传入开始时间与结束时间，录制任务根据起止时间自动开始与结束。在所设置结束时间过期之前（且未调用StopLiveRecord提前终止任务），录制任务都是有效的，期间多次断流然后重推都会启动录制任务。
          2. 实时视频录制模式。
            忽略传入的开始时间，在录制任务创建后立即开始录制，录制时长支持最大为30分钟，如果传入的结束时间与当前时间差大于30分钟，则按30分钟计算，实时视频录制主要用于录制精彩视频场景，时长建议控制在5分钟以内。

        - 注意事项
          1. 调用接口超时设置应大于3秒，小于3秒重试以及按不同起止时间调用都有可能产生重复录制任务，进而导致额外录制费用。
          2. 受限于音视频文件格式（FLV/MP4/HLS）对编码类型的支持，视频编码类型支持 H.264，音频编码类型支持 AAC。
          3. 为避免恶意或非主观的频繁 API 请求，对定时录制模式最大创建任务数做了限制：其中，当天可以创建的最大任务数不超过4000（不含已删除的任务）；当前时刻并发运行的任务数不超过400。有超出此限制的需要提工单申请。
          4. 此调用方式暂时不支持海外推流录制。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveRecordRule(
            self,
            request: models.CreateLiveRecordRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveRecordRuleResponse:
        """
        创建录制规则，需要先调用[CreateLiveRecordTemplate](/document/product/267/32614)接口创建录制模板，将返回的模板id绑定到流使用。
        <br>录制相关文档：[直播录制](/document/product/267/32739)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveRecordRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveRecordRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveRecordTemplate(
            self,
            request: models.CreateLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveRecordTemplateResponse:
        """
        创建录制模板，数量上限：50，成功返回模板id后，需要调用[CreateLiveRecordRule](/document/product/267/32615)接口，将模板id绑定到流进行使用。
        <br>录制相关文档：[直播录制](/document/product/267/32739)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveSnapshotRule(
            self,
            request: models.CreateLiveSnapshotRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveSnapshotRuleResponse:
        """
        创建截图规则，需要先调用[CreateLiveSnapshotTemplate](/document/product/267/32624)接口创建截图模板，然后将返回的模板 ID 绑定到流进行使用。
        <br>截图相关文档：[直播截图](/document/product/267/32737)。
        注意：单个域名仅支持关联一个截图模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveSnapshotRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveSnapshotRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveSnapshotTemplate(
            self,
            request: models.CreateLiveSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveSnapshotTemplateResponse:
        """
        创建截图模板，数量上限：50，成功返回模板id后，需要调用[CreateLiveSnapshotRule](/document/product/267/32625)接口，将模板id绑定到流使用。
        <br>截图相关文档：[直播截图](/document/product/267/32737)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveStreamMonitor(
            self,
            request: models.CreateLiveStreamMonitorRequest,
            opts: Dict = None,
    ) -> models.CreateLiveStreamMonitorResponse:
        """
        该接口用来创建直播流监播任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveStreamMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveStreamMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveTimeShiftRule(
            self,
            request: models.CreateLiveTimeShiftRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveTimeShiftRuleResponse:
        """
        创建直播时移规则，需要先调用[CreateLiveTimeShiftTemplate](/document/product/267/86169)接口创建直播时移模板，将返回的模板id绑定到流使用。
        <br>直播时移相关文档：[直播时移](/document/product/267/86134)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveTimeShiftRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveTimeShiftRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveTimeShiftTemplate(
            self,
            request: models.CreateLiveTimeShiftTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveTimeShiftTemplateResponse:
        """
        创建直播时移模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveTimeShiftTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveTimeShiftTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveTranscodeRule(
            self,
            request: models.CreateLiveTranscodeRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveTranscodeRuleResponse:
        """
        创建转码规则，数量上限：50，需要先调用[CreateLiveTranscodeTemplate](/document/product/267/32646)接口创建转码模板，将返回的模板id绑定到流使用。
        <br>转码相关文档：[直播转封装及转码](/document/product/267/32736)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveTranscodeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveTranscodeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveTranscodeTemplate(
            self,
            request: models.CreateLiveTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLiveTranscodeTemplateResponse:
        """
        创建转码模板，数量上限：50，成功返回模板id后，需要调用[CreateLiveTranscodeRule](/document/product/267/32647)接口，将返回的模板id绑定到流使用。
        <br>转码相关文档：[直播转封装及转码](/document/product/267/32736)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveWatermarkRule(
            self,
            request: models.CreateLiveWatermarkRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLiveWatermarkRuleResponse:
        """
        创建水印规则，需要先调用[AddLiveWatermark](/document/product/267/30154)接口添加水印，将返回的水印id绑定到流使用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveWatermarkRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveWatermarkRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePullStreamConfig(
            self,
            request: models.CreatePullStreamConfigRequest,
            opts: Dict = None,
    ) -> models.CreatePullStreamConfigResponse:
        """
        创建临时拉流转推任务，目前限制添加10条任务。
        该接口已下线,请使用新接口 CreateLivePullStreamTask。

        注意：该接口用于创建临时拉流转推任务，
        拉流源地址即 FromUrl 可以是腾讯或非腾讯数据源，
        但转推目标地址即 ToUrl 目前限制为已注册的腾讯直播域名。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePullStreamConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePullStreamConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordTask(
            self,
            request: models.CreateRecordTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRecordTaskResponse:
        """
        创建一个在指定时间启动、结束的录制任务，并使用指定录制模板ID对应的配置进行录制。
        - 使用前提
        1. 录制文件存放于点播平台或对象存储内，所以用户如需使用录制功能，需首先自行开通点播服务或对象存储服务。
        2. 录制文件存放后相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，具体请参考[对应文档](https://cloud.tencent.com/document/product/266/2837)。
        - 注意事项
        1. 断流会结束当前录制并生成录制文件。在结束时间到达之前任务仍然有效，期间只要正常推流都会正常录制，与是否多次推、断流无关。
        2. 使用上避免创建时间段相互重叠的录制任务。若同一条流当前存在多个时段重叠的任务，为避免重复录制系统将启动最多3个录制任务。
        3. 创建的录制任务记录在平台侧只保留3个月。
        4. 当前录制任务管理API（[CreateRecordTask](https://cloud.tencent.com/document/product/267/45983)/[StopRecordTask](https://cloud.tencent.com/document/product/267/45981)/[DeleteRecordTask](https://cloud.tencent.com/document/product/267/45982)）与旧API（CreateLiveRecord/StopLiveRecord/DeleteLiveRecord）不兼容，两套接口不能混用。
        5. 避免 创建录制任务 与 推流 操作同时进行，可能导致因录制任务未生效而引起任务延迟启动问题，两者操作间隔建议大于3秒。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScreenshotTask(
            self,
            request: models.CreateScreenshotTaskRequest,
            opts: Dict = None,
    ) -> models.CreateScreenshotTaskResponse:
        """
        创建一个在指定时间启动、结束的截图任务，并使用指定截图模板ID对应的配置进行截图。
        - 注意事项
        1. 断流会结束当前截图。在结束时间到达之前任务仍然有效，期间只要正常推流都会正常截图，与是否多次推、断流无关。
        2. 使用上避免创建时间段相互重叠的截图任务。若同一条流当前存在多个时段重叠的任务，为避免重复系统将启动最多3个截图任务。
        3. 创建的截图任务记录在平台侧只保留3个月。
        4. 当前截图任务管理API（CreateScreenshotTask/StopScreenshotTask/DeleteScreenshotTask）与旧API（CreateLiveInstantSnapshot/StopLiveInstantSnapshot）不兼容，两套接口不能混用。
        5. 避免 创建截图任务 与 推流 操作同时进行，可能导致因截图任务未生效而引起任务延迟启动问题，两者操作间隔建议大于3秒。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScreenshotTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScreenshotTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditKeywords(
            self,
            request: models.DeleteAuditKeywordsRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditKeywordsResponse:
        """
        删除关键词信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditKeywords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditKeywordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCaster(
            self,
            request: models.DeleteCasterRequest,
            opts: Dict = None,
    ) -> models.DeleteCasterResponse:
        """
        该接口用来删除一个导播台的所有信息。
        注意，调用该接口后，所有的导播台信息将被清除，包括正在直播的内容也将直接中断。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCasterInputInfo(
            self,
            request: models.DeleteCasterInputInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteCasterInputInfoResponse:
        """
        该接口用来删除导播台中的输入源信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCasterInputInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCasterInputInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCasterLayoutInfo(
            self,
            request: models.DeleteCasterLayoutInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteCasterLayoutInfoResponse:
        """
        该接口用来将布局信息从导播台中删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCasterLayoutInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCasterLayoutInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCasterMarkPicInfo(
            self,
            request: models.DeleteCasterMarkPicInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteCasterMarkPicInfoResponse:
        """
        该接口用来删除导播台某个Index对应的水印。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCasterMarkPicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCasterMarkPicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCasterMarkWordInfo(
            self,
            request: models.DeleteCasterMarkWordInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteCasterMarkWordInfoResponse:
        """
        该接口用来删除导播台的文本配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCasterMarkWordInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCasterMarkWordInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCasterOutputInfo(
            self,
            request: models.DeleteCasterOutputInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteCasterOutputInfoResponse:
        """
        该接口用来删除导播台的推流信息。
        注：若删除推流到腾讯云直播源站配置，即OutputIndex为0，OutputType为1的推流配置，在重新启动主监后，系统会自动重新生成一个推流到腾讯云直播源站配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCasterOutputInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCasterOutputInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveCallbackRule(
            self,
            request: models.DeleteLiveCallbackRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveCallbackRuleResponse:
        """
        删除回调规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveCallbackRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveCallbackRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveCallbackTemplate(
            self,
            request: models.DeleteLiveCallbackTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveCallbackTemplateResponse:
        """
        删除回调模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveCallbackTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveCallbackTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveDomain(
            self,
            request: models.DeleteLiveDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveDomainResponse:
        """
        删除已添加的直播域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLivePadRule(
            self,
            request: models.DeleteLivePadRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLivePadRuleResponse:
        """
        删除直播垫片规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLivePadRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLivePadRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLivePadTemplate(
            self,
            request: models.DeleteLivePadTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLivePadTemplateResponse:
        """
        删除直播垫片模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLivePadTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLivePadTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLivePullStreamTask(
            self,
            request: models.DeleteLivePullStreamTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteLivePullStreamTaskResponse:
        """
        删除接口 CreateLivePullStreamTask 创建的拉流任务。
        注意：
        1. 入参中的 TaskId 为 CreateLivePullStreamTask 接口创建时返回的TaskId。
        2. 也可通过 DescribeLivePullStreamTasks 进行查询创建的任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLivePullStreamTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLivePullStreamTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveRecord(
            self,
            request: models.DeleteLiveRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveRecordResponse:
        """
        注：DeleteLiveRecord 接口仅用于删除录制任务记录，不具备停止录制的功能，也不能删除正在进行中的录制。如果需要停止录制任务，请使用终止录制[StopLiveRecord](/document/product/267/30146) 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveRecordRule(
            self,
            request: models.DeleteLiveRecordRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveRecordRuleResponse:
        """
        删除录制规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveRecordRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveRecordRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveRecordTemplate(
            self,
            request: models.DeleteLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveRecordTemplateResponse:
        """
        删除录制模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveSnapshotRule(
            self,
            request: models.DeleteLiveSnapshotRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveSnapshotRuleResponse:
        """
        删除截图规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveSnapshotRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveSnapshotRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveSnapshotTemplate(
            self,
            request: models.DeleteLiveSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveSnapshotTemplateResponse:
        """
        删除截图模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveStreamMonitor(
            self,
            request: models.DeleteLiveStreamMonitorRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveStreamMonitorResponse:
        """
        该接口用来删除直播流监播任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveStreamMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveStreamMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveTimeShiftRule(
            self,
            request: models.DeleteLiveTimeShiftRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveTimeShiftRuleResponse:
        """
        删除直播时移规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveTimeShiftRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveTimeShiftRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveTimeShiftTemplate(
            self,
            request: models.DeleteLiveTimeShiftTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveTimeShiftTemplateResponse:
        """
        删除直播时移模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveTimeShiftTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveTimeShiftTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveTranscodeRule(
            self,
            request: models.DeleteLiveTranscodeRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveTranscodeRuleResponse:
        """
        删除转码规则。
        DomainName+AppName+StreamName+TemplateId唯一标识单个转码规则，如需删除需要强匹配。其中TemplateId必填，其余参数为空时也需要传空字符串进行强匹配。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveTranscodeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveTranscodeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveTranscodeTemplate(
            self,
            request: models.DeleteLiveTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveTranscodeTemplateResponse:
        """
        删除转码模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveWatermark(
            self,
            request: models.DeleteLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveWatermarkResponse:
        """
        删除水印。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveWatermarkRule(
            self,
            request: models.DeleteLiveWatermarkRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveWatermarkRuleResponse:
        """
        删除水印规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveWatermarkRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveWatermarkRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePullStreamConfig(
            self,
            request: models.DeletePullStreamConfigRequest,
            opts: Dict = None,
    ) -> models.DeletePullStreamConfigResponse:
        """
        删除直播拉流配置。该接口已下线,请使用新接口 DeleteLivePullStreamTask。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePullStreamConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePullStreamConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordTask(
            self,
            request: models.DeleteRecordTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordTaskResponse:
        """
        删除录制任务配置。删除操作不影响正在运行当中的任务，仅对删除之后新的推流有效。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScreenshotTask(
            self,
            request: models.DeleteScreenshotTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteScreenshotTaskResponse:
        """
        删除截图任务配置。删除操作不影响正在运行当中的任务，仅对删除之后新的推流有效。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScreenshotTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScreenshotTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllStreamPlayInfoList(
            self,
            request: models.DescribeAllStreamPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAllStreamPlayInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        输入某个时间点（1分钟维度），查询该时间点所有流的下行信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllStreamPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllStreamPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAreaBillBandwidthAndFluxList(
            self,
            request: models.DescribeAreaBillBandwidthAndFluxListRequest,
            opts: Dict = None,
    ) -> models.DescribeAreaBillBandwidthAndFluxListResponse:
        """
        海外分区直播播放带宽和流量数据查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAreaBillBandwidthAndFluxList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAreaBillBandwidthAndFluxListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditKeywords(
            self,
            request: models.DescribeAuditKeywordsRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditKeywordsResponse:
        """
        获取关键词信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditKeywords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditKeywordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupStreamList(
            self,
            request: models.DescribeBackupStreamListRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupStreamListResponse:
        """
        返回正在直播中的流列表。适用于推流成功后查询在线流信息。

        注意：
        1. 该接口仅提供辅助查询在线流列表功能，业务重要场景不可强依赖该接口。
        2. 该接口仅适用于流数少于2万路的情况，对于流数较大用户请联系售后。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupStreamList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupStreamListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillBandwidthAndFluxList(
            self,
            request: models.DescribeBillBandwidthAndFluxListRequest,
            opts: Dict = None,
    ) -> models.DescribeBillBandwidthAndFluxListResponse:
        """
        直播播放带宽和流量数据查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillBandwidthAndFluxList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillBandwidthAndFluxListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallbackRecordsList(
            self,
            request: models.DescribeCallbackRecordsListRequest,
            opts: Dict = None,
    ) -> models.DescribeCallbackRecordsListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        用于查询回调事件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallbackRecordsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallbackRecordsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaster(
            self,
            request: models.DescribeCasterRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterResponse:
        """
        查询导播台信息接口，用来查询导播台状态、描述、输出长、宽等信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCasterDisplayInfo(
            self,
            request: models.DescribeCasterDisplayInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterDisplayInfoResponse:
        """
        查询导播台PVW任务和PGM任务的展示信息，包括使用的布局、水印、字幕等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCasterDisplayInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterDisplayInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCasterInputInfos(
            self,
            request: models.DescribeCasterInputInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterInputInfosResponse:
        """
        该接口用来查询导播台的输入源信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCasterInputInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterInputInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCasterLayoutInfos(
            self,
            request: models.DescribeCasterLayoutInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterLayoutInfosResponse:
        """
        该接口用来查询某个导播台的布局列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCasterLayoutInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterLayoutInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCasterList(
            self,
            request: models.DescribeCasterListRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterListResponse:
        """
        该接口用来查询账号下所有的导播台列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCasterList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCasterMarkPicInfos(
            self,
            request: models.DescribeCasterMarkPicInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterMarkPicInfosResponse:
        """
        该接口用来查询某个导播台的水印列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCasterMarkPicInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterMarkPicInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCasterMarkWordInfos(
            self,
            request: models.DescribeCasterMarkWordInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterMarkWordInfosResponse:
        """
        该接口用来查询某个导播台的文本列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCasterMarkWordInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterMarkWordInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCasterOutputInfos(
            self,
            request: models.DescribeCasterOutputInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterOutputInfosResponse:
        """
        该接口用来查询某个导播台的推流信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCasterOutputInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterOutputInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCasterPlayUrl(
            self,
            request: models.DescribeCasterPlayUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterPlayUrlResponse:
        """
        该接口用来获取导播台视频流的播放url，用来在页面上拉流展示。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCasterPlayUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterPlayUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCasterTransitionTypes(
            self,
            request: models.DescribeCasterTransitionTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterTransitionTypesResponse:
        """
        该接口用来获取所有的转场名称及其对应的素材url。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCasterTransitionTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterTransitionTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCasterUserStatus(
            self,
            request: models.DescribeCasterUserStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeCasterUserStatusResponse:
        """
        本接口用来查询当前APPID导播台业务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCasterUserStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCasterUserStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConcurrentRecordStreamNum(
            self,
            request: models.DescribeConcurrentRecordStreamNumRequest,
            opts: Dict = None,
    ) -> models.DescribeConcurrentRecordStreamNumResponse:
        """
        查询并发录制路数，对慢直播和普通直播适用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConcurrentRecordStreamNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConcurrentRecordStreamNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeliverBandwidthList(
            self,
            request: models.DescribeDeliverBandwidthListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeliverBandwidthListResponse:
        """
        查询直播转推计费带宽，查询时间范围最大支持3个月内的数据，时间跨度最长31天。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeliverBandwidthList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeliverBandwidthListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeliverLogDownList(
            self,
            request: models.DescribeDeliverLogDownListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeliverLogDownListResponse:
        """
        批量获取转推日志的URL。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeliverLogDownList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeliverLogDownListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupProIspPlayInfoList(
            self,
            request: models.DescribeGroupProIspPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupProIspPlayInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询按省份和运营商分组的下行播放数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupProIspPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupProIspPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHttpStatusInfoList(
            self,
            request: models.DescribeHttpStatusInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeHttpStatusInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询某段时间内5分钟粒度的各播放http状态码的个数。
        备注：数据延迟1小时，如10:00-10:59点的数据12点才能查到。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHttpStatusInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHttpStatusInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCallbackRules(
            self,
            request: models.DescribeLiveCallbackRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCallbackRulesResponse:
        """
        获取回调规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCallbackRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCallbackRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCallbackTemplate(
            self,
            request: models.DescribeLiveCallbackTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCallbackTemplateResponse:
        """
        获取单个回调模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCallbackTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCallbackTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCallbackTemplates(
            self,
            request: models.DescribeLiveCallbackTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCallbackTemplatesResponse:
        """
        获取回调模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCallbackTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCallbackTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCert(
            self,
            request: models.DescribeLiveCertRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCertResponse:
        """
        获取证书信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCerts(
            self,
            request: models.DescribeLiveCertsRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCertsResponse:
        """
        获取证书信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCerts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCertsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveCloudEffectList(
            self,
            request: models.DescribeLiveCloudEffectListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveCloudEffectListResponse:
        """
        使用该接口查询云端特效列表，特效列表中包含一部分官方精品特效，同时包含用户自定义生成的特效。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveCloudEffectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveCloudEffectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDelayInfoList(
            self,
            request: models.DescribeLiveDelayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDelayInfoListResponse:
        """
        获取直播延播列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDelayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDelayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomain(
            self,
            request: models.DescribeLiveDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainResponse:
        """
        查询直播域名信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomainCert(
            self,
            request: models.DescribeLiveDomainCertRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainCertResponse:
        """
        获取域名证书信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomainCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomainCertBindings(
            self,
            request: models.DescribeLiveDomainCertBindingsRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainCertBindingsResponse:
        """
        查询绑定证书的域名列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomainCertBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainCertBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomainPlayInfoList(
            self,
            request: models.DescribeLiveDomainPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainPlayInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询实时的域名维度下行播放数据，由于数据处理有耗时，接口默认查询4分钟前的准实时数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomainPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomainReferer(
            self,
            request: models.DescribeLiveDomainRefererRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainRefererResponse:
        """
        查询直播域名 Referer 黑白名单配置。
        由于 Referer 信息包含在 http 协议中，在开启配置后，播放协议为 rtmp 或 WebRTC 不会校验 Referer 配置，仍可正常播放。如需配置 Referer 鉴权建议使用 http-flv 或 http-hls 协议播放。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomainReferer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainRefererResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveDomains(
            self,
            request: models.DescribeLiveDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveDomainsResponse:
        """
        根据域名状态、类型等信息查询用户的域名信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveEnhanceInfoList(
            self,
            request: models.DescribeLiveEnhanceInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveEnhanceInfoListResponse:
        """
        查询直播增强用量明细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveEnhanceInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveEnhanceInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePackageInfo(
            self,
            request: models.DescribeLivePackageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePackageInfoResponse:
        """
        查询用户套餐包总量、使用量、剩余量、包状态、购买时间和过期时间等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePackageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePackageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePadRules(
            self,
            request: models.DescribeLivePadRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePadRulesResponse:
        """
        获取直播垫片规则列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePadRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePadRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePadStreamList(
            self,
            request: models.DescribeLivePadStreamListRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePadStreamListResponse:
        """
        使用该接口查询垫片流列表。垫片流状态更新存在一定延迟，可间隔30秒以上查询，避免频繁查询该接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePadStreamList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePadStreamListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePadTemplate(
            self,
            request: models.DescribeLivePadTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePadTemplateResponse:
        """
        获取单个直播垫片模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePadTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePadTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePadTemplates(
            self,
            request: models.DescribeLivePadTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePadTemplatesResponse:
        """
        获取直播垫片模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePadTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePadTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePlayAuthKey(
            self,
            request: models.DescribeLivePlayAuthKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePlayAuthKeyResponse:
        """
        查询播放鉴权key。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePlayAuthKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePlayAuthKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePullStreamTaskStatus(
            self,
            request: models.DescribeLivePullStreamTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePullStreamTaskStatusResponse:
        """
        查询直播拉流任务状态信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePullStreamTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePullStreamTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePullStreamTasks(
            self,
            request: models.DescribeLivePullStreamTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePullStreamTasksResponse:
        """
        查询使用 CreateLivePullStreamTask 接口创建的直播拉流任务。
        排序方式：默认按更新时间 倒序排列。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePullStreamTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePullStreamTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLivePushAuthKey(
            self,
            request: models.DescribeLivePushAuthKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeLivePushAuthKeyResponse:
        """
        查询直播推流鉴权key
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLivePushAuthKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLivePushAuthKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveRecordRules(
            self,
            request: models.DescribeLiveRecordRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveRecordRulesResponse:
        """
        获取录制规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveRecordRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveRecordRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveRecordTemplate(
            self,
            request: models.DescribeLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveRecordTemplateResponse:
        """
        获取单个录制模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveRecordTemplates(
            self,
            request: models.DescribeLiveRecordTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveRecordTemplatesResponse:
        """
        获取录制模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveRecordTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveRecordTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveSnapshotRules(
            self,
            request: models.DescribeLiveSnapshotRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveSnapshotRulesResponse:
        """
        获取截图规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveSnapshotRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveSnapshotRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveSnapshotTemplate(
            self,
            request: models.DescribeLiveSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveSnapshotTemplateResponse:
        """
        获取单个截图模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveSnapshotTemplates(
            self,
            request: models.DescribeLiveSnapshotTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveSnapshotTemplatesResponse:
        """
        获取截图模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveSnapshotTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveSnapshotTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamEventList(
            self,
            request: models.DescribeLiveStreamEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamEventListResponse:
        """
        用于查询推断流事件。<br>

        注意：
        1. 该接口提供离线推断流记录查询功能，不可作为重要业务场景强依赖接口。
        2. 该接口可通过使用IsFilter进行过滤，返回推流历史记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamMonitor(
            self,
            request: models.DescribeLiveStreamMonitorRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamMonitorResponse:
        """
        该接口用来查询某个特定监播任务的配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamMonitorList(
            self,
            request: models.DescribeLiveStreamMonitorListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamMonitorListResponse:
        """
        该接口用来查询直播流监播任务配置的列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamMonitorList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamMonitorListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamOnlineList(
            self,
            request: models.DescribeLiveStreamOnlineListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamOnlineListResponse:
        """
        返回正在直播中的流列表。适用于推流成功后查询在线流信息。

        注意：
        1. 该接口仅提供辅助查询在线流列表功能，业务重要场景不可强依赖该接口。
        2. 该接口仅适用于流数少于2万路的情况，对于流数较大用户请联系售后。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamOnlineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamOnlineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamPublishedList(
            self,
            request: models.DescribeLiveStreamPublishedListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamPublishedListResponse:
        """
        返回已经推过流的流列表。<br>
        注意：分页最多支持查询1万条记录，可通过调整查询时间范围来获取更多数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamPublishedList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamPublishedListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamPushInfoList(
            self,
            request: models.DescribeLiveStreamPushInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamPushInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询所有实时流的推流信息，包括客户端IP，服务端IP，帧率，码率，域名，开始推流时间。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamPushInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamPushInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStreamState(
            self,
            request: models.DescribeLiveStreamStateRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamStateResponse:
        """
        返回直播中、无推流或者禁播等状态。

        使用建议：
        该接口提供实时流状态查询功能，鉴于网络抖动等一些不可抗因素，使用该接口作为判断主播是否开播等重要业务场景时，请参考以下使用建议。
        1. 优先使用业务自身的房间开关播逻辑，判断主播是否在线，譬如客户端开播信令和主播在线心跳等。
        2. 对于没有房间管理的直播场景，可以结合以下方案综合判断。
        2.1 根据[推断流事件通知](/document/product/267/20388) 判断主播在线状态。
        2.2 通过定时（间隔>1min）查询[直播中的流接口](/document/api/267/20472)，判断主播是否在线。
        2.3 通过 本接口 查询直播流状态，判断主播是否在线。
        2.4 以上任一方式判断为在线，都认为主播开播中，并且接口查询超时或解析异常时，也默认为在线，减少对业务的影响。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStreamState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTimeShiftBillInfoList(
            self,
            request: models.DescribeLiveTimeShiftBillInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTimeShiftBillInfoListResponse:
        """
        提供给客户对账，按天统计，维度：推流域名、时移文件时长（累加）、配置天数（不累加）、时移总时长（累加）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTimeShiftBillInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTimeShiftBillInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTimeShiftRules(
            self,
            request: models.DescribeLiveTimeShiftRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTimeShiftRulesResponse:
        """
        获取直播时移规则列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTimeShiftRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTimeShiftRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTimeShiftTemplates(
            self,
            request: models.DescribeLiveTimeShiftTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTimeShiftTemplatesResponse:
        """
        获取直播时移模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTimeShiftTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTimeShiftTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTimeShiftWriteSizeInfoList(
            self,
            request: models.DescribeLiveTimeShiftWriteSizeInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTimeShiftWriteSizeInfoListResponse:
        """
        支持直播时移写入量数据查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTimeShiftWriteSizeInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTimeShiftWriteSizeInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTranscodeDetailInfo(
            self,
            request: models.DescribeLiveTranscodeDetailInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTranscodeDetailInfoResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        支持查询某天或某段时间的转码详细信息。由于转码数据量较大，如果查询时间跨度太长可能会拉不到数据，可以尝试将查询时间范围缩小些再重试。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTranscodeDetailInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTranscodeDetailInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTranscodeRules(
            self,
            request: models.DescribeLiveTranscodeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTranscodeRulesResponse:
        """
        获取转码规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTranscodeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTranscodeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTranscodeTemplate(
            self,
            request: models.DescribeLiveTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTranscodeTemplateResponse:
        """
        获取单个转码模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTranscodeTemplates(
            self,
            request: models.DescribeLiveTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTranscodeTemplatesResponse:
        """
        获取转码模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveTranscodeTotalInfo(
            self,
            request: models.DescribeLiveTranscodeTotalInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveTranscodeTotalInfoResponse:
        """
        查询转码总量数据，可查询近三个月内的数据。
        注意：
        如果是查询某一天内，则返回5分钟粒度数据；
        如果是查询跨天或指定域名， 则返回1小时粒度数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveTranscodeTotalInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveTranscodeTotalInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveWatermark(
            self,
            request: models.DescribeLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveWatermarkResponse:
        """
        获取单个水印信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveWatermarkRules(
            self,
            request: models.DescribeLiveWatermarkRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveWatermarkRulesResponse:
        """
        获取水印规则列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveWatermarkRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveWatermarkRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveWatermarks(
            self,
            request: models.DescribeLiveWatermarksRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveWatermarksResponse:
        """
        查询水印列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveWatermarks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveWatermarksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveXP2PDetailInfoList(
            self,
            request: models.DescribeLiveXP2PDetailInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveXP2PDetailInfoListResponse:
        """
        P2P流数据查询接口，用来获取流量、卡播和起播信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveXP2PDetailInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveXP2PDetailInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogDownloadList(
            self,
            request: models.DescribeLogDownloadListRequest,
            opts: Dict = None,
    ) -> models.DescribeLogDownloadListResponse:
        """
        批量获取日志URL。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogDownloadList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogDownloadListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonitorReport(
            self,
            request: models.DescribeMonitorReportRequest,
            opts: Dict = None,
    ) -> models.DescribeMonitorReportResponse:
        """
        用来查询监播场次7天内的智能识别、断流、低帧率等信息的汇总报告。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonitorReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonitorReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlayErrorCodeDetailInfoList(
            self,
            request: models.DescribePlayErrorCodeDetailInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribePlayErrorCodeDetailInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询下行播放错误码信息，某段时间内1分钟粒度的各http错误码出现的次数，包括4xx，5xx。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlayErrorCodeDetailInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlayErrorCodeDetailInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlayErrorCodeSumInfoList(
            self,
            request: models.DescribePlayErrorCodeSumInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribePlayErrorCodeSumInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询下行播放错误码信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlayErrorCodeSumInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlayErrorCodeSumInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProIspPlaySumInfoList(
            self,
            request: models.DescribeProIspPlaySumInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeProIspPlaySumInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询某段时间内每个国家地区每个省份每个运营商的平均每秒流量，总流量，总请求数信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProIspPlaySumInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProIspPlaySumInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProvinceIspPlayInfoList(
            self,
            request: models.DescribeProvinceIspPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeProvinceIspPlayInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询某省份某运营商下行播放数据，包括带宽，流量，请求数，并发连接数信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProvinceIspPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProvinceIspPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePullStreamConfigs(
            self,
            request: models.DescribePullStreamConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribePullStreamConfigsResponse:
        """
        查询直播拉流配置。该接口已下线,请使用新接口 DescribeLivePullStreamTasks。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePullStreamConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePullStreamConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePullTransformPushInfo(
            self,
            request: models.DescribePullTransformPushInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePullTransformPushInfoResponse:
        """
        查询拉流转推任务的时长信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePullTransformPushInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePullTransformPushInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePullTransformPushInfoList(
            self,
            request: models.DescribePullTransformPushInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribePullTransformPushInfoListResponse:
        """
        查询拉流转推任务流数据统计信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePullTransformPushInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePullTransformPushInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePushBandwidthAndFluxList(
            self,
            request: models.DescribePushBandwidthAndFluxListRequest,
            opts: Dict = None,
    ) -> models.DescribePushBandwidthAndFluxListResponse:
        """
        直播推流带宽和流量数据查询。
        推流计费会先取全球推流用量和全球播放用量进行比较，满足计费条件后再按各地区用量出账。详情参见[计费文档](https://cloud.tencent.com/document/product/267/34175)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePushBandwidthAndFluxList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePushBandwidthAndFluxListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordTask(
            self,
            request: models.DescribeRecordTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordTaskResponse:
        """
        查询指定时间段范围内启动和结束的录制任务列表。
        - 使用前提
        1. 仅用于查询由 CreateRecordTask 接口创建的录制任务。
        2. 不能查询被 DeleteRecordTask 接口删除以及已过期（平台侧保留3个月）的录制任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenShotSheetNumList(
            self,
            request: models.DescribeScreenShotSheetNumListRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenShotSheetNumListResponse:
        """
        接口用来查询直播增值业务--截图的张数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenShotSheetNumList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenShotSheetNumListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenshotTask(
            self,
            request: models.DescribeScreenshotTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenshotTaskResponse:
        """
        查询指定时间段范围内启动和结束的截图任务列表。
        - 使用前提
        1. 仅用于查询由 CreateScreenshotTask接口创建的截图任务。
        2. 不能查询被 DeleteScreenshotTask接口删除以及已过期（平台侧保留3个月）的截图任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenshotTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenshotTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamDayPlayInfoList(
            self,
            request: models.DescribeStreamDayPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamDayPlayInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询天维度每条流的播放数据，包括总流量等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamDayPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamDayPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPlayInfoList(
            self,
            request: models.DescribeStreamPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPlayInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询播放数据，支持按流名称查询详细播放数据，也可按播放域名查询详细总数据，数据延迟4分钟左右。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPushInfoList(
            self,
            request: models.DescribeStreamPushInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPushInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询流id的上行推流质量数据，包括音视频的帧率，码率，流逝时间，编码格式等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPushInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPushInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimeShiftRecordDetail(
            self,
            request: models.DescribeTimeShiftRecordDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTimeShiftRecordDetailResponse:
        """
        前提调用 DescribeTimeShiftStreamList 获得请求必要参数。查询指定范围内的时移流录制详情，最大支持24小时范围查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimeShiftRecordDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimeShiftRecordDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimeShiftStreamList(
            self,
            request: models.DescribeTimeShiftStreamListRequest,
            opts: Dict = None,
    ) -> models.DescribeTimeShiftStreamListResponse:
        """
        查询某个时间范围内所有时移流列表。最大支持查询24小时内的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimeShiftStreamList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimeShiftStreamListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopClientIpSumInfoList(
            self,
            request: models.DescribeTopClientIpSumInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeTopClientIpSumInfoListResponse:
        """
        该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询某段时间top n客户端ip汇总信息（暂支持top 1000）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopClientIpSumInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopClientIpSumInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTranscodeTaskNum(
            self,
            request: models.DescribeTranscodeTaskNumRequest,
            opts: Dict = None,
    ) -> models.DescribeTranscodeTaskNumResponse:
        """
        查询转码任务数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTranscodeTaskNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTranscodeTaskNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUploadStreamNums(
            self,
            request: models.DescribeUploadStreamNumsRequest,
            opts: Dict = None,
    ) -> models.DescribeUploadStreamNumsResponse:
        """
        直播上行路数查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUploadStreamNums"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUploadStreamNumsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVisitTopSumInfoList(
            self,
            request: models.DescribeVisitTopSumInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeVisitTopSumInfoListResponse:
        """
        查询某时间段top n的域名或流id信息（暂支持top 1000）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVisitTopSumInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVisitTopSumInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DropLiveStream(
            self,
            request: models.DropLiveStreamRequest,
            opts: Dict = None,
    ) -> models.DropLiveStreamResponse:
        """
        断开推流连接，但可以重新推流。
        注：对已经不活跃的流，调用该断流接口时，接口返回成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DropLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DropLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableLiveDomain(
            self,
            request: models.EnableLiveDomainRequest,
            opts: Dict = None,
    ) -> models.EnableLiveDomainResponse:
        """
        启用状态为停用的直播域名。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableLiveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableLiveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableOptimalSwitching(
            self,
            request: models.EnableOptimalSwitchingRequest,
            opts: Dict = None,
    ) -> models.EnableOptimalSwitchingResponse:
        """
        启用择优调度。
        注意：流维度的择优调度，当主备流结束后自动失效。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableOptimalSwitching"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableOptimalSwitchingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForbidLiveDomain(
            self,
            request: models.ForbidLiveDomainRequest,
            opts: Dict = None,
    ) -> models.ForbidLiveDomainResponse:
        """
        停止使用某个直播域名。
        """
        
        kwargs = {}
        kwargs["action"] = "ForbidLiveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForbidLiveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForbidLiveStream(
            self,
            request: models.ForbidLiveStreamRequest,
            opts: Dict = None,
    ) -> models.ForbidLiveStreamResponse:
        """
        禁止某条流的推送，可以预设某个时刻将流恢复。
        注意：
        1. 默认只要流名称正确，禁推就会生效。
        2. 如需要推流域名+推流路径+流名称 强匹配生效禁推，需提单联系售后开启配置。
        3. 如果配置了域名分组，需填写准确推流域名，才可断掉当前推流。
        """
        
        kwargs = {}
        kwargs["action"] = "ForbidLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForbidLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCaster(
            self,
            request: models.ModifyCasterRequest,
            opts: Dict = None,
    ) -> models.ModifyCasterResponse:
        """
        该接口用来设置导播台的描述、名称、录制模板id等参数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCasterInputInfo(
            self,
            request: models.ModifyCasterInputInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyCasterInputInfoResponse:
        """
        该接口用来修改已经设置过的输入源信息，如源地址，源类型等。
        设置前，需保证待修改的输入源已经存在。若不存在，需使用AddCasterInputInfo接口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCasterInputInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCasterInputInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCasterLayoutInfo(
            self,
            request: models.ModifyCasterLayoutInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyCasterLayoutInfoResponse:
        """
        该接口用来修改布局参数
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCasterLayoutInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCasterLayoutInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCasterMarkPicInfo(
            self,
            request: models.ModifyCasterMarkPicInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyCasterMarkPicInfoResponse:
        """
        该接口用来修改导播台水印信息。
        注意，修改的Index对应的水印需已存在
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCasterMarkPicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCasterMarkPicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCasterMarkWordInfo(
            self,
            request: models.ModifyCasterMarkWordInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyCasterMarkWordInfoResponse:
        """
        该接口用来修改导播台文本配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCasterMarkWordInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCasterMarkWordInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCasterOutputInfo(
            self,
            request: models.ModifyCasterOutputInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyCasterOutputInfoResponse:
        """
        该接口用来修改导播台的推流信息。
        注：只有在主监启动前设置才生效，主监启动后设置，下次推流生效。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCasterOutputInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCasterOutputInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveCallbackTemplate(
            self,
            request: models.ModifyLiveCallbackTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveCallbackTemplateResponse:
        """
        修改回调模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveCallbackTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveCallbackTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveDomainCertBindings(
            self,
            request: models.ModifyLiveDomainCertBindingsRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveDomainCertBindingsResponse:
        """
        批量绑定证书对应的播放域名，并更新启用状态。
        新建自有证书将自动上传至腾讯云ssl。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveDomainCertBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveDomainCertBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveDomainReferer(
            self,
            request: models.ModifyLiveDomainRefererRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveDomainRefererResponse:
        """
        设置直播域名 Referer 黑白名单。
        由于 Referer 信息包含在 http 协议中，在开启配置后，播放协议为 rtmp 或 WebRTC 不会校验 Referer 配置，仍可正常播放。如需配置 Referer 鉴权建议使用 http-flv 或 http-hls 协议播放。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveDomainReferer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveDomainRefererResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLivePadTemplate(
            self,
            request: models.ModifyLivePadTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLivePadTemplateResponse:
        """
        修改直播垫片模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLivePadTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLivePadTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLivePlayAuthKey(
            self,
            request: models.ModifyLivePlayAuthKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyLivePlayAuthKeyResponse:
        """
        修改播放鉴权key
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLivePlayAuthKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLivePlayAuthKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLivePlayDomain(
            self,
            request: models.ModifyLivePlayDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyLivePlayDomainResponse:
        """
        修改播放域名信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLivePlayDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLivePlayDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLivePullStreamTask(
            self,
            request: models.ModifyLivePullStreamTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyLivePullStreamTaskResponse:
        """
        更新直播拉流任务。
        1. 不支持修改拉流源类型，如需更换，请创建新任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLivePullStreamTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLivePullStreamTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLivePushAuthKey(
            self,
            request: models.ModifyLivePushAuthKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyLivePushAuthKeyResponse:
        """
        修改直播推流鉴权key
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLivePushAuthKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLivePushAuthKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveRecordTemplate(
            self,
            request: models.ModifyLiveRecordTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveRecordTemplateResponse:
        """
        修改录制模板配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveRecordTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveRecordTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveSnapshotTemplate(
            self,
            request: models.ModifyLiveSnapshotTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveSnapshotTemplateResponse:
        """
        修改截图模板配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveSnapshotTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveSnapshotTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveStreamMonitor(
            self,
            request: models.ModifyLiveStreamMonitorRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveStreamMonitorResponse:
        """
        该接口用来修改直播流监播任务的配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveStreamMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveStreamMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveTimeShiftTemplate(
            self,
            request: models.ModifyLiveTimeShiftTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveTimeShiftTemplateResponse:
        """
        修改直播时移模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveTimeShiftTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveTimeShiftTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveTranscodeTemplate(
            self,
            request: models.ModifyLiveTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveTranscodeTemplateResponse:
        """
        修改转码模板配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPullStreamConfig(
            self,
            request: models.ModifyPullStreamConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyPullStreamConfigResponse:
        """
        更新拉流配置。该接口为已下线接口，请使用新接口 ModifyLivePullStreamTask。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPullStreamConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPullStreamConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPullStreamStatus(
            self,
            request: models.ModifyPullStreamStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyPullStreamStatusResponse:
        """
        修改直播拉流配置的状态。该接口已下线,请使用新接口 ModifyLivePullStreamTask。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPullStreamStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPullStreamStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseCaster(
            self,
            request: models.ReleaseCasterRequest,
            opts: Dict = None,
    ) -> models.ReleaseCasterResponse:
        """
        调用该接口，释放导播台实例，但保留所有的配置。
        执行该接口，预监与主监画面停止，第三方推流停止。
        点播文件与直播地址将停止展示，客户自行推到导播台的流需要手动停止。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseCaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseCasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartLivePullStreamTask(
            self,
            request: models.RestartLivePullStreamTaskRequest,
            opts: Dict = None,
    ) -> models.RestartLivePullStreamTaskResponse:
        """
        将正在运行的拉流转推任务进行重启。
        注意：
        1. 重启任务会造成推流中断。
        2. 点播源任务的重启，会根据VodRefreshType决定是续播还是从头开始播。
        """
        
        kwargs = {}
        kwargs["action"] = "RestartLivePullStreamTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartLivePullStreamTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeDelayLiveStream(
            self,
            request: models.ResumeDelayLiveStreamRequest,
            opts: Dict = None,
    ) -> models.ResumeDelayLiveStreamResponse:
        """
        取消直播流设置的延时配置，恢复实时直播画面。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeDelayLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeDelayLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeLiveStream(
            self,
            request: models.ResumeLiveStreamRequest,
            opts: Dict = None,
    ) -> models.ResumeLiveStreamResponse:
        """
        恢复某条流的推流。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendLiveCloudEffect(
            self,
            request: models.SendLiveCloudEffectRequest,
            opts: Dict = None,
    ) -> models.SendLiveCloudEffectResponse:
        """
        使用该接口发送云端特效到线上正活跃的直播流，观众可在播放端看到特效从直播流画面中展示。
        """
        
        kwargs = {}
        kwargs["action"] = "SendLiveCloudEffect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendLiveCloudEffectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartLivePadStream(
            self,
            request: models.StartLivePadStreamRequest,
            opts: Dict = None,
    ) -> models.StartLivePadStreamResponse:
        """
        使用该接口将直播流开始切入垫片。
        """
        
        kwargs = {}
        kwargs["action"] = "StartLivePadStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartLivePadStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartLiveStreamMonitor(
            self,
            request: models.StartLiveStreamMonitorRequest,
            opts: Dict = None,
    ) -> models.StartLiveStreamMonitorResponse:
        """
        该接口用来启动直播流监播任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StartLiveStreamMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartLiveStreamMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCasterPgm(
            self,
            request: models.StopCasterPgmRequest,
            opts: Dict = None,
    ) -> models.StopCasterPgmResponse:
        """
        该接口用来停止导播台的主监输出。
        停止主监后，对应的推流到腾讯云直播源站和推流到其他第三方平台均将会停止。
        """
        
        kwargs = {}
        kwargs["action"] = "StopCasterPgm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCasterPgmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCasterPvw(
            self,
            request: models.StopCasterPvwRequest,
            opts: Dict = None,
    ) -> models.StopCasterPvwResponse:
        """
        该接口用来停止导播台的预监任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StopCasterPvw"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCasterPvwResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopLivePadStream(
            self,
            request: models.StopLivePadStreamRequest,
            opts: Dict = None,
    ) -> models.StopLivePadStreamResponse:
        """
        使用该接口将直播流停止切入垫片。
        """
        
        kwargs = {}
        kwargs["action"] = "StopLivePadStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopLivePadStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopLiveRecord(
            self,
            request: models.StopLiveRecordRequest,
            opts: Dict = None,
    ) -> models.StopLiveRecordResponse:
        """
        说明：录制后的文件存放于点播平台。用户如需使用录制功能，需首先自行开通点播账号并确保账号可用。录制文件存放后，相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，请参考对应文档。
        """
        
        kwargs = {}
        kwargs["action"] = "StopLiveRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopLiveRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopLiveStreamMonitor(
            self,
            request: models.StopLiveStreamMonitorRequest,
            opts: Dict = None,
    ) -> models.StopLiveStreamMonitorResponse:
        """
        该接口用来停止直播流监播任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StopLiveStreamMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopLiveStreamMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopRecordTask(
            self,
            request: models.StopRecordTaskRequest,
            opts: Dict = None,
    ) -> models.StopRecordTaskResponse:
        """
        提前结束录制，中止运行中的录制任务并生成录制文件。任务被成功终止后，本次任务将不再启动。
        """
        
        kwargs = {}
        kwargs["action"] = "StopRecordTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRecordTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopScreenshotTask(
            self,
            request: models.StopScreenshotTaskRequest,
            opts: Dict = None,
    ) -> models.StopScreenshotTaskResponse:
        """
        提前结束截图，中止运行中的截图任务。任务被成功终止后，本次任务将不再启动。
        """
        
        kwargs = {}
        kwargs["action"] = "StopScreenshotTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopScreenshotTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchBackupStream(
            self,
            request: models.SwitchBackupStreamRequest,
            opts: Dict = None,
    ) -> models.SwitchBackupStreamResponse:
        """
        调用该接口实现切换当前播放所使用的主备流。
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchBackupStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchBackupStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindLiveDomainCert(
            self,
            request: models.UnBindLiveDomainCertRequest,
            opts: Dict = None,
    ) -> models.UnBindLiveDomainCertResponse:
        """
        解绑域名证书
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindLiveDomainCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindLiveDomainCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateLiveWatermark(
            self,
            request: models.UpdateLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.UpdateLiveWatermarkResponse:
        """
        更新水印。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)