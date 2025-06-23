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
from tencentcloud.live.v20180801 import models


class LiveClient(AbstractClient):
    _apiVersion = '2018-08-01'
    _endpoint = 'live.tencentcloudapi.com'
    _service = 'live'


    def AddCasterInputInfo(self, request):
        """该接口用来向导播台中添加一个输入源，该输入源可以是拉流地址、或是一个文件链接

        :param request: Request instance for AddCasterInputInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.AddCasterInputInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddCasterInputInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCasterInputInfo", params, headers=headers)
            response = json.loads(body)
            model = models.AddCasterInputInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCasterLayoutInfo(self, request):
        """该接口用来增加导播台的布局参数。

        :param request: Request instance for AddCasterLayoutInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.AddCasterLayoutInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddCasterLayoutInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCasterLayoutInfo", params, headers=headers)
            response = json.loads(body)
            model = models.AddCasterLayoutInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCasterMarkPicInfo(self, request):
        """该接口用来新增图片水印。

        :param request: Request instance for AddCasterMarkPicInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.AddCasterMarkPicInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddCasterMarkPicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCasterMarkPicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.AddCasterMarkPicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCasterMarkWordInfo(self, request):
        """为导播台添加文本配置。

        :param request: Request instance for AddCasterMarkWordInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.AddCasterMarkWordInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddCasterMarkWordInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCasterMarkWordInfo", params, headers=headers)
            response = json.loads(body)
            model = models.AddCasterMarkWordInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCasterOutputInfo(self, request):
        """该接口用来新增导播台推流信息。导播台主监启动后，将会将主监画面推向该接口设置的地址。

        :param request: Request instance for AddCasterOutputInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.AddCasterOutputInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddCasterOutputInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCasterOutputInfo", params, headers=headers)
            response = json.loads(body)
            model = models.AddCasterOutputInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddDelayLiveStream(self, request):
        """针对大型活动直播，通过对直播流设置延时来控制现场与观众播放画面的时间间隔，避免突发状况造成影响。

        注意：如果在推流前设置延播，需要提前5分钟设置，目前该接口只支持流粒度。

        :param request: Request instance for AddDelayLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.AddDelayLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDelayLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.AddDelayLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddLiveDomain(self, request):
        """添加域名，一次只能提交一个域名。域名必须已备案。

        :param request: Request instance for AddLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.AddLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddLiveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLiveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.AddLiveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddLiveWatermark(self, request):
        """添加水印，成功返回水印 ID 后，需要调用[CreateLiveWatermarkRule](/document/product/267/32629)接口将水印 ID 绑定到流使用。 水印数量上限 100，超过后需要先删除，再添加。

        :param request: Request instance for AddLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.AddLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.AddLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AuthenticateDomainOwner(self, request):
        """验证用户是否拥有特定直播域名。

        :param request: Request instance for AuthenticateDomainOwner.
        :type request: :class:`tencentcloud.live.v20180801.models.AuthenticateDomainOwnerRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AuthenticateDomainOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuthenticateDomainOwner", params, headers=headers)
            response = json.loads(body)
            model = models.AuthenticateDomainOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelCommonMixStream(self, request):
        """该接口用来取消混流。用法与 mix_streamv2.cancel_mix_stream 基本一致。

        :param request: Request instance for CancelCommonMixStream.
        :type request: :class:`tencentcloud.live.v20180801.models.CancelCommonMixStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CancelCommonMixStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelCommonMixStream", params, headers=headers)
            response = json.loads(body)
            model = models.CancelCommonMixStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyCaster(self, request):
        """该接口用来复制导播台配置

        :param request: Request instance for CopyCaster.
        :type request: :class:`tencentcloud.live.v20180801.models.CopyCasterRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CopyCasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyCaster", params, headers=headers)
            response = json.loads(body)
            model = models.CopyCasterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCaster(self, request):
        """该接口用来创建新的导播台

        :param request: Request instance for CreateCaster.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateCasterRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateCasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCaster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCasterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCasterInputPushUrl(self, request):
        """该接口用来生成导播台推流地址

        :param request: Request instance for CreateCasterInputPushUrl.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateCasterInputPushUrlRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateCasterInputPushUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCasterInputPushUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCasterInputPushUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCasterPgm(self, request):
        """该接口用来启动主监任务，并将获取主监画面的播放地址。

        :param request: Request instance for CreateCasterPgm.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateCasterPgmRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateCasterPgmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCasterPgm", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCasterPgmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCasterPgmFromPvw(self, request):
        """该接口用来将预监画面的布局、水印、字幕等配置，复制到主监画面中。
        该接口使用时，预监任务需处于运行状态。

        :param request: Request instance for CreateCasterPgmFromPvw.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateCasterPgmFromPvwRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateCasterPgmFromPvwResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCasterPgmFromPvw", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCasterPgmFromPvwResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCasterPvw(self, request):
        """该接口用来启动预监任务，并将获取预监画面的播放地址。

        :param request: Request instance for CreateCasterPvw.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateCasterPvwRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateCasterPvwResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCasterPvw", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCasterPvwResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCommonMixStream(self, request):
        """该接口用来创建通用混流。用法与旧接口 mix_streamv2.start_mix_stream_advanced 基本一致。
        注意：当前最多支持16路混流。
        最佳实践：https://cloud.tencent.com/document/product/267/45566

        :param request: Request instance for CreateCommonMixStream.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateCommonMixStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateCommonMixStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCommonMixStream", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCommonMixStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveCallbackRule(self, request):
        """创建回调规则，需要先调用[CreateLiveCallbackTemplate](/document/product/267/32637)接口创建回调模板，将返回的模板id绑定到域名/路径进行使用。
        <br>回调协议相关文档：[事件消息通知](/document/product/267/32744)。

        :param request: Request instance for CreateLiveCallbackRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveCallbackRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveCallbackRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveCallbackTemplate(self, request):
        """创建回调模板，数量上限：50，成功返回模板id后，需要调用[CreateLiveCallbackRule](/document/product/267/32638)接口将模板 ID 绑定到域名/路径使用。
        <br>回调协议相关文档：[事件消息通知](/document/product/267/32744)。
        注意：至少填写一个回调 URL。

        :param request: Request instance for CreateLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveCallbackTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveCallbackTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLivePadRule(self, request):
        """创建直播垫片规则。

        :param request: Request instance for CreateLivePadRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLivePadRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLivePadRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLivePadRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLivePadRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLivePadTemplate(self, request):
        """创建直播垫片模板。

        :param request: Request instance for CreateLivePadTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLivePadTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLivePadTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLivePadTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLivePadTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLivePullStreamTask(self, request):
        """创建直播拉流任务。支持将外部已有的点播文件，或者直播源拉取过来转推到指定的目标地址。
        注意：
        1. 默认支持任务数上限200个，如有特殊需求，可通过提单到售后进行评估增加上限。
        2. 源流视频编码目前只支持: H264, H265。其他编码格式建议先进行转码处理。
        3. 源流音频编码目前只支持: AAC。其他编码格式建议先进行转码处理。
        4. 可在控制台开启过期自动清理，避免过期任务占用任务数额度。
        5. 拉流转推功能为计费增值服务，计费规则详情可参见[计费文档](https://cloud.tencent.com/document/product/267/53308)。
        6. 拉流转推功能仅提供内容拉取与推送服务，请确保内容已获得授权并符合内容传播相关的法律法规。若内容有侵权或违规相关问题，云直播会停止相关的功能服务并保留追究法律责任的权利。

        :param request: Request instance for CreateLivePullStreamTask.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLivePullStreamTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLivePullStreamTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLivePullStreamTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLivePullStreamTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveRecord(self, request):
        """- 使用前提
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

        :param request: Request instance for CreateLiveRecord.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveRecordRule(self, request):
        """创建录制规则，需要先调用[CreateLiveRecordTemplate](/document/product/267/32614)接口创建录制模板，将返回的模板id绑定到流使用。
        <br>录制相关文档：[直播录制](/document/product/267/32739)。

        :param request: Request instance for CreateLiveRecordRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveRecordRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveRecordRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveRecordTemplate(self, request):
        """创建录制模板，数量上限：50，成功返回模板id后，需要调用[CreateLiveRecordRule](/document/product/267/32615)接口，将模板id绑定到流进行使用。
        <br>录制相关文档：[直播录制](/document/product/267/32739)。

        :param request: Request instance for CreateLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordTemplateResponse`

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


    def CreateLiveSnapshotRule(self, request):
        """创建截图规则，需要先调用[CreateLiveSnapshotTemplate](/document/product/267/32624)接口创建截图模板，然后将返回的模板 ID 绑定到流进行使用。
        <br>截图相关文档：[直播截图](/document/product/267/32737)。
        注意：单个域名仅支持关联一个截图模板。

        :param request: Request instance for CreateLiveSnapshotRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveSnapshotRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveSnapshotRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveSnapshotTemplate(self, request):
        """创建截图模板，数量上限：50，成功返回模板id后，需要调用[CreateLiveSnapshotRule](/document/product/267/32625)接口，将模板id绑定到流使用。
        <br>截图相关文档：[直播截图](/document/product/267/32737)。

        :param request: Request instance for CreateLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveStreamMonitor(self, request):
        """该接口用来创建直播流监播任务。

        :param request: Request instance for CreateLiveStreamMonitor.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveStreamMonitorRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveStreamMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveStreamMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveStreamMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveTimeShiftRule(self, request):
        """创建直播时移规则，需要先调用[CreateLiveTimeShiftTemplate](/document/product/267/86169)接口创建直播时移模板，将返回的模板id绑定到流使用。
        <br>直播时移相关文档：[直播时移](/document/product/267/86134)。

        :param request: Request instance for CreateLiveTimeShiftRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTimeShiftRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTimeShiftRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveTimeShiftRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveTimeShiftRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveTimeShiftTemplate(self, request):
        """创建直播时移模板。

        :param request: Request instance for CreateLiveTimeShiftTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTimeShiftTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTimeShiftTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveTimeShiftTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveTimeShiftTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveTranscodeRule(self, request):
        """创建转码规则，数量上限：50，需要先调用[CreateLiveTranscodeTemplate](/document/product/267/32646)接口创建转码模板，将返回的模板id绑定到流使用。
        <br>转码相关文档：[直播转封装及转码](/document/product/267/32736)。

        :param request: Request instance for CreateLiveTranscodeRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveTranscodeRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveTranscodeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveTranscodeTemplate(self, request):
        """创建转码模板，数量上限：50，成功返回模板id后，需要调用[CreateLiveTranscodeRule](/document/product/267/32647)接口，将返回的模板id绑定到流使用。
        <br>转码相关文档：[直播转封装及转码](/document/product/267/32736)。

        :param request: Request instance for CreateLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLiveWatermarkRule(self, request):
        """创建水印规则，需要先调用[AddLiveWatermark](/document/product/267/30154)接口添加水印，将返回的水印id绑定到流使用。

        :param request: Request instance for CreateLiveWatermarkRule.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveWatermarkRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveWatermarkRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveWatermarkRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLiveWatermarkRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePullStreamConfig(self, request):
        """创建临时拉流转推任务，目前限制添加10条任务。
        该接口已下线,请使用新接口 CreateLivePullStreamTask。

        注意：该接口用于创建临时拉流转推任务，
        拉流源地址即 FromUrl 可以是腾讯或非腾讯数据源，
        但转推目标地址即 ToUrl 目前限制为已注册的腾讯直播域名。

        :param request: Request instance for CreatePullStreamConfig.
        :type request: :class:`tencentcloud.live.v20180801.models.CreatePullStreamConfigRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreatePullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePullStreamConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePullStreamConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecordTask(self, request):
        """创建一个在指定时间启动、结束的录制任务，并使用指定录制模板ID对应的配置进行录制。
        - 使用前提
        1. 录制文件存放于点播平台或对象存储内，所以用户如需使用录制功能，需首先自行开通点播服务或对象存储服务。
        2. 录制文件存放后相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，具体请参考[对应文档](https://cloud.tencent.com/document/product/266/2837)。
        - 注意事项
        1. 断流会结束当前录制并生成录制文件。在结束时间到达之前任务仍然有效，期间只要正常推流都会正常录制，与是否多次推、断流无关。
        2. 使用上避免创建时间段相互重叠的录制任务。若同一条流当前存在多个时段重叠的任务，为避免重复录制系统将启动最多3个录制任务。
        3. 创建的录制任务记录在平台侧只保留3个月。
        4. 当前录制任务管理API（[CreateRecordTask](https://cloud.tencent.com/document/product/267/45983)/[StopRecordTask](https://cloud.tencent.com/document/product/267/45981)/[DeleteRecordTask](https://cloud.tencent.com/document/product/267/45982)）与旧API（CreateLiveRecord/StopLiveRecord/DeleteLiveRecord）不兼容，两套接口不能混用。
        5. 避免 创建录制任务 与 推流 操作同时进行，可能导致因录制任务未生效而引起任务延迟启动问题，两者操作间隔建议大于3秒。

        :param request: Request instance for CreateRecordTask.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateRecordTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateRecordTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScreenshotTask(self, request):
        """创建一个在指定时间启动、结束的截图任务，并使用指定截图模板ID对应的配置进行截图。
        - 注意事项
        1. 断流会结束当前截图。在结束时间到达之前任务仍然有效，期间只要正常推流都会正常截图，与是否多次推、断流无关。
        2. 使用上避免创建时间段相互重叠的截图任务。若同一条流当前存在多个时段重叠的任务，为避免重复系统将启动最多3个截图任务。
        3. 创建的截图任务记录在平台侧只保留3个月。
        4. 当前截图任务管理API（CreateScreenshotTask/StopScreenshotTask/DeleteScreenshotTask）与旧API（CreateLiveInstantSnapshot/StopLiveInstantSnapshot）不兼容，两套接口不能混用。
        5. 避免 创建截图任务 与 推流 操作同时进行，可能导致因截图任务未生效而引起任务延迟启动问题，两者操作间隔建议大于3秒。

        :param request: Request instance for CreateScreenshotTask.
        :type request: :class:`tencentcloud.live.v20180801.models.CreateScreenshotTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateScreenshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScreenshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScreenshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCaster(self, request):
        """该接口用来删除一个导播台的所有信息。
        注意，调用该接口后，所有的导播台信息将被清除，包括正在直播的内容也将直接中断。

        :param request: Request instance for DeleteCaster.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteCasterRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteCasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCaster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCasterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCasterInputInfo(self, request):
        """该接口用来删除导播台中的输入源信息。

        :param request: Request instance for DeleteCasterInputInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteCasterInputInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteCasterInputInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCasterInputInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCasterInputInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCasterLayoutInfo(self, request):
        """该接口用来将布局信息从导播台中删除

        :param request: Request instance for DeleteCasterLayoutInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteCasterLayoutInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteCasterLayoutInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCasterLayoutInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCasterLayoutInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCasterMarkPicInfo(self, request):
        """该接口用来删除导播台某个Index对应的水印。

        :param request: Request instance for DeleteCasterMarkPicInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteCasterMarkPicInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteCasterMarkPicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCasterMarkPicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCasterMarkPicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCasterMarkWordInfo(self, request):
        """该接口用来删除导播台的文本配置。

        :param request: Request instance for DeleteCasterMarkWordInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteCasterMarkWordInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteCasterMarkWordInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCasterMarkWordInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCasterMarkWordInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCasterOutputInfo(self, request):
        """该接口用来删除导播台的推流信息。
        注：若删除推流到腾讯云直播源站配置，即OutputIndex为0，OutputType为1的推流配置，在重新启动主监后，系统会自动重新生成一个推流到腾讯云直播源站配置。

        :param request: Request instance for DeleteCasterOutputInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteCasterOutputInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteCasterOutputInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCasterOutputInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCasterOutputInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveCallbackRule(self, request):
        """删除回调规则。

        :param request: Request instance for DeleteLiveCallbackRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveCallbackRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveCallbackRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveCallbackTemplate(self, request):
        """删除回调模板。

        :param request: Request instance for DeleteLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveCallbackTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveCallbackTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveDomain(self, request):
        """删除已添加的直播域名

        :param request: Request instance for DeleteLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLivePadRule(self, request):
        """删除直播垫片规则。

        :param request: Request instance for DeleteLivePadRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLivePadRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLivePadRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLivePadRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLivePadRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLivePadTemplate(self, request):
        """删除直播垫片模板。

        :param request: Request instance for DeleteLivePadTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLivePadTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLivePadTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLivePadTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLivePadTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLivePullStreamTask(self, request):
        """删除接口 CreateLivePullStreamTask 创建的拉流任务。
        注意：
        1. 入参中的 TaskId 为 CreateLivePullStreamTask 接口创建时返回的TaskId。
        2. 也可通过 DescribeLivePullStreamTasks 进行查询创建的任务。

        :param request: Request instance for DeleteLivePullStreamTask.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLivePullStreamTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLivePullStreamTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLivePullStreamTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLivePullStreamTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveRecord(self, request):
        """注：DeleteLiveRecord 接口仅用于删除录制任务记录，不具备停止录制的功能，也不能删除正在进行中的录制。如果需要停止录制任务，请使用终止录制[StopLiveRecord](/document/product/267/30146) 接口。

        :param request: Request instance for DeleteLiveRecord.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveRecordRule(self, request):
        """删除录制规则。

        :param request: Request instance for DeleteLiveRecordRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveRecordRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveRecordRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveRecordTemplate(self, request):
        """删除录制模板。

        :param request: Request instance for DeleteLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordTemplateResponse`

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


    def DeleteLiveSnapshotRule(self, request):
        """删除截图规则。

        :param request: Request instance for DeleteLiveSnapshotRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveSnapshotRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveSnapshotRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveSnapshotTemplate(self, request):
        """删除截图模板

        :param request: Request instance for DeleteLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveStreamMonitor(self, request):
        """该接口用来删除直播流监播任务。

        :param request: Request instance for DeleteLiveStreamMonitor.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveStreamMonitorRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveStreamMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveStreamMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveStreamMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveTimeShiftRule(self, request):
        """删除直播时移规则。

        :param request: Request instance for DeleteLiveTimeShiftRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTimeShiftRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTimeShiftRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveTimeShiftRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveTimeShiftRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveTimeShiftTemplate(self, request):
        """删除直播时移模板。

        :param request: Request instance for DeleteLiveTimeShiftTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTimeShiftTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTimeShiftTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveTimeShiftTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveTimeShiftTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveTranscodeRule(self, request):
        """删除转码规则。
        DomainName+AppName+StreamName+TemplateId唯一标识单个转码规则，如需删除需要强匹配。其中TemplateId必填，其余参数为空时也需要传空字符串进行强匹配。

        :param request: Request instance for DeleteLiveTranscodeRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveTranscodeRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveTranscodeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveTranscodeTemplate(self, request):
        """删除转码模板。

        :param request: Request instance for DeleteLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveWatermark(self, request):
        """删除水印。

        :param request: Request instance for DeleteLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLiveWatermarkRule(self, request):
        """删除水印规则

        :param request: Request instance for DeleteLiveWatermarkRule.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRuleRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveWatermarkRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLiveWatermarkRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePullStreamConfig(self, request):
        """删除直播拉流配置。该接口已下线,请使用新接口 DeleteLivePullStreamTask。

        :param request: Request instance for DeletePullStreamConfig.
        :type request: :class:`tencentcloud.live.v20180801.models.DeletePullStreamConfigRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeletePullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePullStreamConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePullStreamConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordTask(self, request):
        """删除录制任务配置。删除操作不影响正在运行当中的任务，仅对删除之后新的推流有效。

        :param request: Request instance for DeleteRecordTask.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteRecordTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteRecordTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScreenshotTask(self, request):
        """删除截图任务配置。删除操作不影响正在运行当中的任务，仅对删除之后新的推流有效。

        :param request: Request instance for DeleteScreenshotTask.
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteScreenshotTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteScreenshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScreenshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScreenshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllStreamPlayInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        输入某个时间点（1分钟维度），查询该时间点所有流的下行信息。

        :param request: Request instance for DescribeAllStreamPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeAllStreamPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeAllStreamPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllStreamPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllStreamPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAreaBillBandwidthAndFluxList(self, request):
        """海外分区直播播放带宽和流量数据查询。

        :param request: Request instance for DescribeAreaBillBandwidthAndFluxList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeAreaBillBandwidthAndFluxListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeAreaBillBandwidthAndFluxListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAreaBillBandwidthAndFluxList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAreaBillBandwidthAndFluxListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupStreamList(self, request):
        """返回正在直播中的流列表。适用于推流成功后查询在线流信息。

        注意：
        1. 该接口仅提供辅助查询在线流列表功能，业务重要场景不可强依赖该接口。
        2. 该接口仅适用于流数少于2万路的情况，对于流数较大用户请联系售后。

        :param request: Request instance for DescribeBackupStreamList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeBackupStreamListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeBackupStreamListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupStreamList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupStreamListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillBandwidthAndFluxList(self, request):
        """直播播放带宽和流量数据查询。

        :param request: Request instance for DescribeBillBandwidthAndFluxList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeBillBandwidthAndFluxListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeBillBandwidthAndFluxListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillBandwidthAndFluxList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillBandwidthAndFluxListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCallbackRecordsList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        用于查询回调事件。

        :param request: Request instance for DescribeCallbackRecordsList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCallbackRecordsListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCallbackRecordsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCallbackRecordsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCallbackRecordsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaster(self, request):
        """查询导播台信息接口，用来查询导播台状态、描述、输出长、宽等信息

        :param request: Request instance for DescribeCaster.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaster", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCasterDisplayInfo(self, request):
        """查询导播台PVW任务和PGM任务的展示信息，包括使用的布局、水印、字幕等信息。

        :param request: Request instance for DescribeCasterDisplayInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterDisplayInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterDisplayInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCasterDisplayInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterDisplayInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCasterInputInfos(self, request):
        """该接口用来查询导播台的输入源信息列表。

        :param request: Request instance for DescribeCasterInputInfos.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterInputInfosRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterInputInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCasterInputInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterInputInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCasterLayoutInfos(self, request):
        """该接口用来查询某个导播台的布局列表

        :param request: Request instance for DescribeCasterLayoutInfos.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterLayoutInfosRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterLayoutInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCasterLayoutInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterLayoutInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCasterList(self, request):
        """该接口用来查询账号下所有的导播台列表

        :param request: Request instance for DescribeCasterList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCasterList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCasterMarkPicInfos(self, request):
        """该接口用来查询某个导播台的水印列表。

        :param request: Request instance for DescribeCasterMarkPicInfos.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterMarkPicInfosRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterMarkPicInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCasterMarkPicInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterMarkPicInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCasterMarkWordInfos(self, request):
        """该接口用来查询某个导播台的文本列表。

        :param request: Request instance for DescribeCasterMarkWordInfos.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterMarkWordInfosRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterMarkWordInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCasterMarkWordInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterMarkWordInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCasterOutputInfos(self, request):
        """该接口用来查询某个导播台的推流信息列表。

        :param request: Request instance for DescribeCasterOutputInfos.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterOutputInfosRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterOutputInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCasterOutputInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterOutputInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCasterPlayUrl(self, request):
        """该接口用来获取导播台视频流的播放url，用来在页面上拉流展示。

        :param request: Request instance for DescribeCasterPlayUrl.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterPlayUrlRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterPlayUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCasterPlayUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterPlayUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCasterTransitionTypes(self, request):
        """该接口用来获取所有的转场名称及其对应的素材url。

        :param request: Request instance for DescribeCasterTransitionTypes.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterTransitionTypesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterTransitionTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCasterTransitionTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterTransitionTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCasterUserStatus(self, request):
        """本接口用来查询当前APPID导播台业务状态

        :param request: Request instance for DescribeCasterUserStatus.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeCasterUserStatusRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeCasterUserStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCasterUserStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCasterUserStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConcurrentRecordStreamNum(self, request):
        """查询并发录制路数，对慢直播和普通直播适用。

        :param request: Request instance for DescribeConcurrentRecordStreamNum.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeConcurrentRecordStreamNumRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeConcurrentRecordStreamNumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConcurrentRecordStreamNum", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConcurrentRecordStreamNumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeliverBandwidthList(self, request):
        """查询直播转推计费带宽，查询时间范围最大支持3个月内的数据，时间跨度最长31天。

        :param request: Request instance for DescribeDeliverBandwidthList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeDeliverBandwidthListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeDeliverBandwidthListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeliverBandwidthList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeliverBandwidthListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeliverLogDownList(self, request):
        """批量获取转推日志的URL。

        :param request: Request instance for DescribeDeliverLogDownList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeDeliverLogDownListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeDeliverLogDownListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeliverLogDownList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeliverLogDownListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupProIspPlayInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询按省份和运营商分组的下行播放数据。

        :param request: Request instance for DescribeGroupProIspPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeGroupProIspPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeGroupProIspPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupProIspPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupProIspPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHttpStatusInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询某段时间内5分钟粒度的各播放http状态码的个数。
        备注：数据延迟1小时，如10:00-10:59点的数据12点才能查到。

        :param request: Request instance for DescribeHttpStatusInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeHttpStatusInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeHttpStatusInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHttpStatusInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHttpStatusInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCallbackRules(self, request):
        """获取回调规则列表

        :param request: Request instance for DescribeLiveCallbackRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCallbackRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCallbackRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCallbackTemplate(self, request):
        """获取单个回调模板。

        :param request: Request instance for DescribeLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCallbackTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCallbackTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCallbackTemplates(self, request):
        """获取回调模板列表

        :param request: Request instance for DescribeLiveCallbackTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCallbackTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCallbackTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCallbackTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCert(self, request):
        """获取证书信息

        :param request: Request instance for DescribeLiveCert.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCert", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCerts(self, request):
        """获取证书信息列表

        :param request: Request instance for DescribeLiveCerts.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCertsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCerts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCertsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveCloudEffectList(self, request):
        """使用该接口查询云端特效列表，特效列表中包含一部分官方精品特效，同时包含用户自定义生成的特效。

        :param request: Request instance for DescribeLiveCloudEffectList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveCloudEffectListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveCloudEffectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveCloudEffectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveCloudEffectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDelayInfoList(self, request):
        """获取直播延播列表。

        :param request: Request instance for DescribeLiveDelayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDelayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDelayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDelayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDelayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomain(self, request):
        """查询直播域名信息。

        :param request: Request instance for DescribeLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomainCert(self, request):
        """获取域名证书信息。

        :param request: Request instance for DescribeLiveDomainCert.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomainCert", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomainCertBindings(self, request):
        """查询绑定证书的域名列表。

        :param request: Request instance for DescribeLiveDomainCertBindings.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertBindingsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainCertBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomainCertBindings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainCertBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomainPlayInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询实时的域名维度下行播放数据，由于数据处理有耗时，接口默认查询4分钟前的准实时数据。

        :param request: Request instance for DescribeLiveDomainPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomainPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomainReferer(self, request):
        """查询直播域名 Referer 黑白名单配置。
        由于 Referer 信息包含在 http 协议中，在开启配置后，播放协议为 rtmp 或 WebRTC 不会校验 Referer 配置，仍可正常播放。如需配置 Referer 鉴权建议使用 http-flv 或 http-hls 协议播放。

        :param request: Request instance for DescribeLiveDomainReferer.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainRefererRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainRefererResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomainReferer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainRefererResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveDomains(self, request):
        """根据域名状态、类型等信息查询用户的域名信息。

        :param request: Request instance for DescribeLiveDomains.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveEnhanceInfoList(self, request):
        """查询直播增强用量明细信息。

        :param request: Request instance for DescribeLiveEnhanceInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveEnhanceInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveEnhanceInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveEnhanceInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveEnhanceInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveForbidStreamList(self, request):
        """获取禁推流列表。

        注意：该接口仅作为直播辅助查询接口，重要业务场景不可强依赖该接口。

        :param request: Request instance for DescribeLiveForbidStreamList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveForbidStreamListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveForbidStreamListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveForbidStreamList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveForbidStreamListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePackageInfo(self, request):
        """查询用户套餐包总量、使用量、剩余量、包状态、购买时间和过期时间等。

        :param request: Request instance for DescribeLivePackageInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePackageInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePackageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePackageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePackageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePadRules(self, request):
        """获取直播垫片规则列表。

        :param request: Request instance for DescribeLivePadRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePadRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePadRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePadRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePadRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePadStreamList(self, request):
        """使用该接口查询垫片流列表。垫片流状态更新存在一定延迟，可间隔30秒以上查询，避免频繁查询该接口。

        :param request: Request instance for DescribeLivePadStreamList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePadStreamListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePadStreamListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePadStreamList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePadStreamListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePadTemplate(self, request):
        """获取单个直播垫片模板

        :param request: Request instance for DescribeLivePadTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePadTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePadTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePadTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePadTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePadTemplates(self, request):
        """获取直播垫片模板。

        :param request: Request instance for DescribeLivePadTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePadTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePadTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePadTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePadTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePlayAuthKey(self, request):
        """查询播放鉴权key。

        :param request: Request instance for DescribeLivePlayAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePlayAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePlayAuthKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePlayAuthKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePullStreamTaskStatus(self, request):
        """查询直播拉流任务状态信息。

        :param request: Request instance for DescribeLivePullStreamTaskStatus.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePullStreamTaskStatusRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePullStreamTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePullStreamTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePullStreamTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePullStreamTasks(self, request):
        """查询使用 CreateLivePullStreamTask 接口创建的直播拉流任务。
        排序方式：默认按更新时间 倒序排列。

        :param request: Request instance for DescribeLivePullStreamTasks.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePullStreamTasksRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePullStreamTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePullStreamTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePullStreamTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLivePushAuthKey(self, request):
        """查询直播推流鉴权key

        :param request: Request instance for DescribeLivePushAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePushAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLivePushAuthKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLivePushAuthKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveRecordRules(self, request):
        """获取录制规则列表

        :param request: Request instance for DescribeLiveRecordRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveRecordRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveRecordRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveRecordTemplate(self, request):
        """获取单个录制模板。

        :param request: Request instance for DescribeLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveRecordTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveRecordTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveRecordTemplates(self, request):
        """获取录制模板列表。

        :param request: Request instance for DescribeLiveRecordTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveRecordTemplatesResponse`

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


    def DescribeLiveSnapshotRules(self, request):
        """获取截图规则列表

        :param request: Request instance for DescribeLiveSnapshotRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveSnapshotRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveSnapshotRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveSnapshotTemplate(self, request):
        """获取单个截图模板。

        :param request: Request instance for DescribeLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveSnapshotTemplates(self, request):
        """获取截图模板列表。

        :param request: Request instance for DescribeLiveSnapshotTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveSnapshotTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveSnapshotTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveSnapshotTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamEventList(self, request):
        """用于查询推断流事件。<br>

        注意：
        1. 该接口提供离线推断流记录查询功能，不可作为重要业务场景强依赖接口。
        2. 该接口可通过使用IsFilter进行过滤，返回推流历史记录。

        :param request: Request instance for DescribeLiveStreamEventList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamEventListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamMonitor(self, request):
        """该接口用来查询某个特定监播任务的配置。

        :param request: Request instance for DescribeLiveStreamMonitor.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamMonitorRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamMonitorList(self, request):
        """该接口用来查询直播流监播任务配置的列表信息。

        :param request: Request instance for DescribeLiveStreamMonitorList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamMonitorListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamMonitorListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamMonitorList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamMonitorListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamOnlineList(self, request):
        """返回正在直播中的流列表。适用于推流成功后查询在线流信息。

        注意：
        1. 该接口仅提供辅助查询在线流列表功能，业务重要场景不可强依赖该接口。
        2. 该接口仅适用于流数少于2万路的情况，对于流数较大用户请联系售后。

        :param request: Request instance for DescribeLiveStreamOnlineList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamOnlineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamOnlineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamPublishedList(self, request):
        """返回已经推过流的流列表。<br>
        注意：分页最多支持查询1万条记录，可通过调整查询时间范围来获取更多数据。

        :param request: Request instance for DescribeLiveStreamPublishedList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPublishedListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPublishedListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamPublishedList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamPublishedListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamPushInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询所有实时流的推流信息，包括客户端IP，服务端IP，帧率，码率，域名，开始推流时间。

        :param request: Request instance for DescribeLiveStreamPushInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPushInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPushInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamPushInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamPushInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveStreamState(self, request):
        """返回直播中、无推流或者禁播等状态。

        使用建议：
        该接口提供实时流状态查询功能，鉴于网络抖动等一些不可抗因素，使用该接口作为判断主播是否开播等重要业务场景时，请参考以下使用建议。
        1. 优先使用业务自身的房间开关播逻辑，判断主播是否在线，譬如客户端开播信令和主播在线心跳等。
        2. 对于没有房间管理的直播场景，可以结合以下方案综合判断。
        2.1 根据[推断流事件通知](/document/product/267/20388) 判断主播在线状态。
        2.2 通过定时（间隔>1min）查询[直播中的流接口](/document/api/267/20472)，判断主播是否在线。
        2.3 通过 本接口 查询直播流状态，判断主播是否在线。
        2.4 以上任一方式判断为在线，都认为主播开播中，并且接口查询超时或解析异常时，也默认为在线，减少对业务的影响。

        :param request: Request instance for DescribeLiveStreamState.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamStateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStreamState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveStreamStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTimeShiftBillInfoList(self, request):
        """提供给客户对账，按天统计，维度：推流域名、时移文件时长（累加）、配置天数（不累加）、时移总时长（累加）。

        :param request: Request instance for DescribeLiveTimeShiftBillInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftBillInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftBillInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTimeShiftBillInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTimeShiftBillInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTimeShiftRules(self, request):
        """获取直播时移规则列表。

        :param request: Request instance for DescribeLiveTimeShiftRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTimeShiftRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTimeShiftRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTimeShiftTemplates(self, request):
        """获取直播时移模板。

        :param request: Request instance for DescribeLiveTimeShiftTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTimeShiftTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTimeShiftTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTimeShiftWriteSizeInfoList(self, request):
        """支持直播时移写入量数据查询。

        :param request: Request instance for DescribeLiveTimeShiftWriteSizeInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftWriteSizeInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTimeShiftWriteSizeInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTimeShiftWriteSizeInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTimeShiftWriteSizeInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTranscodeDetailInfo(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        支持查询某天或某段时间的转码详细信息。由于转码数据量较大，如果查询时间跨度太长可能会拉不到数据，可以尝试将查询时间范围缩小些再重试。

        :param request: Request instance for DescribeLiveTranscodeDetailInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeDetailInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTranscodeDetailInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTranscodeDetailInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTranscodeRules(self, request):
        """获取转码规则列表

        :param request: Request instance for DescribeLiveTranscodeRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTranscodeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTranscodeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTranscodeTemplate(self, request):
        """获取单个转码模板。

        :param request: Request instance for DescribeLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTranscodeTemplates(self, request):
        """获取转码模板列表。

        :param request: Request instance for DescribeLiveTranscodeTemplates.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTranscodeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTranscodeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveTranscodeTotalInfo(self, request):
        """查询转码总量数据，可查询近三个月内的数据。
        注意：
        如果是查询某一天内，则返回5分钟粒度数据；
        如果是查询跨天或指定域名， 则返回1小时粒度数据。

        :param request: Request instance for DescribeLiveTranscodeTotalInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTotalInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveTranscodeTotalInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveTranscodeTotalInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveTranscodeTotalInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveWatermark(self, request):
        """获取单个水印信息。

        :param request: Request instance for DescribeLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveWatermarkRules(self, request):
        """获取水印规则列表。

        :param request: Request instance for DescribeLiveWatermarkRules.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRulesRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarkRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveWatermarkRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveWatermarkRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveWatermarks(self, request):
        """查询水印列表。

        :param request: Request instance for DescribeLiveWatermarks.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarksRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveWatermarks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveWatermarksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLiveXP2PDetailInfoList(self, request):
        """P2P流数据查询接口，用来获取流量、卡播和起播信息。

        :param request: Request instance for DescribeLiveXP2PDetailInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveXP2PDetailInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveXP2PDetailInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveXP2PDetailInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLiveXP2PDetailInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogDownloadList(self, request):
        """批量获取日志URL。

        :param request: Request instance for DescribeLogDownloadList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLogDownloadListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLogDownloadListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogDownloadList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogDownloadListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMonitorReport(self, request):
        """用来查询监播场次7天内的智能识别、断流、低帧率等信息的汇总报告。

        :param request: Request instance for DescribeMonitorReport.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeMonitorReportRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeMonitorReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonitorReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonitorReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlayErrorCodeDetailInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询下行播放错误码信息，某段时间内1分钟粒度的各http错误码出现的次数，包括4xx，5xx。

        :param request: Request instance for DescribePlayErrorCodeDetailInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribePlayErrorCodeDetailInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribePlayErrorCodeDetailInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlayErrorCodeDetailInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlayErrorCodeDetailInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlayErrorCodeSumInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询下行播放错误码信息。

        :param request: Request instance for DescribePlayErrorCodeSumInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribePlayErrorCodeSumInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribePlayErrorCodeSumInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlayErrorCodeSumInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlayErrorCodeSumInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProIspPlaySumInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询某段时间内每个国家地区每个省份每个运营商的平均每秒流量，总流量，总请求数信息。

        :param request: Request instance for DescribeProIspPlaySumInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeProIspPlaySumInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeProIspPlaySumInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProIspPlaySumInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProIspPlaySumInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProvinceIspPlayInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询某省份某运营商下行播放数据，包括带宽，流量，请求数，并发连接数信息。

        :param request: Request instance for DescribeProvinceIspPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeProvinceIspPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeProvinceIspPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProvinceIspPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProvinceIspPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePullStreamConfigs(self, request):
        """查询直播拉流配置。该接口已下线,请使用新接口 DescribeLivePullStreamTasks。

        :param request: Request instance for DescribePullStreamConfigs.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribePullStreamConfigsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribePullStreamConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePullStreamConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePullStreamConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePullTransformPushInfo(self, request):
        """查询拉流转推任务的时长信息。

        :param request: Request instance for DescribePullTransformPushInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribePullTransformPushInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribePullTransformPushInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePullTransformPushInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePullTransformPushInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePushBandwidthAndFluxList(self, request):
        """直播推流带宽和流量数据查询。
        推流计费会先取全球推流用量和全球播放用量进行比较，满足计费条件后再按各地区用量出账。详情参见[计费文档](https://cloud.tencent.com/document/product/267/34175)。

        :param request: Request instance for DescribePushBandwidthAndFluxList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribePushBandwidthAndFluxListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribePushBandwidthAndFluxListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePushBandwidthAndFluxList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePushBandwidthAndFluxListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordTask(self, request):
        """查询指定时间段范围内启动和结束的录制任务列表。
        - 使用前提
        1. 仅用于查询由 CreateRecordTask 接口创建的录制任务。
        2. 不能查询被 DeleteRecordTask 接口删除以及已过期（平台侧保留3个月）的录制任务。

        :param request: Request instance for DescribeRecordTask.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeRecordTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeRecordTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenShotSheetNumList(self, request):
        """接口用来查询直播增值业务--截图的张数

        :param request: Request instance for DescribeScreenShotSheetNumList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeScreenShotSheetNumListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeScreenShotSheetNumListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenShotSheetNumList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenShotSheetNumListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenshotTask(self, request):
        """查询指定时间段范围内启动和结束的截图任务列表。
        - 使用前提
        1. 仅用于查询由 CreateScreenshotTask接口创建的截图任务。
        2. 不能查询被 DeleteScreenshotTask接口删除以及已过期（平台侧保留3个月）的截图任务。

        :param request: Request instance for DescribeScreenshotTask.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeScreenshotTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeScreenshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamDayPlayInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询天维度每条流的播放数据，包括总流量等。

        :param request: Request instance for DescribeStreamDayPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeStreamDayPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeStreamDayPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamDayPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamDayPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPlayInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询播放数据，支持按流名称查询详细播放数据，也可按播放域名查询详细总数据，数据延迟4分钟左右。

        :param request: Request instance for DescribeStreamPlayInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeStreamPlayInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeStreamPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPlayInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPlayInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamPushInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询流id的上行推流质量数据，包括音视频的帧率，码率，流逝时间，编码格式等。

        :param request: Request instance for DescribeStreamPushInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeStreamPushInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeStreamPushInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamPushInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamPushInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimeShiftRecordDetail(self, request):
        """前提调用 DescribeTimeShiftStreamList 获得请求必要参数。查询指定范围内的时移流录制详情，最大支持24小时范围查询。

        :param request: Request instance for DescribeTimeShiftRecordDetail.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeTimeShiftRecordDetailRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeTimeShiftRecordDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimeShiftRecordDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimeShiftRecordDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimeShiftStreamList(self, request):
        """查询某个时间范围内所有时移流列表。最大支持查询24小时内的数据。

        :param request: Request instance for DescribeTimeShiftStreamList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeTimeShiftStreamListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeTimeShiftStreamListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimeShiftStreamList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimeShiftStreamListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopClientIpSumInfoList(self, request):
        """该接口为监控数据接口，数据采集及统计方式与计费数据不同，仅供运营分析使用，不能用于计费对账参考。
        查询某段时间top n客户端ip汇总信息（暂支持top 1000）

        :param request: Request instance for DescribeTopClientIpSumInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeTopClientIpSumInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeTopClientIpSumInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopClientIpSumInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopClientIpSumInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTranscodeTaskNum(self, request):
        """查询转码任务数。

        :param request: Request instance for DescribeTranscodeTaskNum.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeTranscodeTaskNumRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeTranscodeTaskNumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeTaskNum", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeTaskNumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUploadStreamNums(self, request):
        """直播上行路数查询。

        :param request: Request instance for DescribeUploadStreamNums.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeUploadStreamNumsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeUploadStreamNumsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUploadStreamNums", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUploadStreamNumsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVisitTopSumInfoList(self, request):
        """查询某时间段top n的域名或流id信息（暂支持top 1000）。

        :param request: Request instance for DescribeVisitTopSumInfoList.
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeVisitTopSumInfoListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeVisitTopSumInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVisitTopSumInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVisitTopSumInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DropLiveStream(self, request):
        """断开推流连接，但可以重新推流。
        注：对已经不活跃的流，调用该断流接口时，接口返回成功。

        :param request: Request instance for DropLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.DropLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DropLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DropLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.DropLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableLiveDomain(self, request):
        """启用状态为停用的直播域名。

        :param request: Request instance for EnableLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.EnableLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.EnableLiveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableLiveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.EnableLiveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableOptimalSwitching(self, request):
        """启用择优调度。
        注意：流维度的择优调度，当主备流结束后自动失效。

        :param request: Request instance for EnableOptimalSwitching.
        :type request: :class:`tencentcloud.live.v20180801.models.EnableOptimalSwitchingRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.EnableOptimalSwitchingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableOptimalSwitching", params, headers=headers)
            response = json.loads(body)
            model = models.EnableOptimalSwitchingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForbidLiveDomain(self, request):
        """停止使用某个直播域名。

        :param request: Request instance for ForbidLiveDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.ForbidLiveDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ForbidLiveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForbidLiveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ForbidLiveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForbidLiveStream(self, request):
        """禁止某条流的推送，可以预设某个时刻将流恢复。
        注意：
        1. 默认只要流名称正确，禁推就会生效。
        2. 如需要推流域名+推流路径+流名称 强匹配生效禁推，需提单联系售后开启配置。
        3. 如果配置了域名分组，需填写准确推流域名，才可断掉当前推流。

        :param request: Request instance for ForbidLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.ForbidLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ForbidLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForbidLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.ForbidLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCaster(self, request):
        """该接口用来设置导播台的描述、名称、录制模板id等参数。

        :param request: Request instance for ModifyCaster.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyCasterRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyCasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCaster", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCasterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCasterInputInfo(self, request):
        """该接口用来修改已经设置过的输入源信息，如源地址，源类型等。
        设置前，需保证待修改的输入源已经存在。若不存在，需使用AddCasterInputInfo接口。

        :param request: Request instance for ModifyCasterInputInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyCasterInputInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyCasterInputInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCasterInputInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCasterInputInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCasterLayoutInfo(self, request):
        """该接口用来修改布局参数

        :param request: Request instance for ModifyCasterLayoutInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyCasterLayoutInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyCasterLayoutInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCasterLayoutInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCasterLayoutInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCasterMarkPicInfo(self, request):
        """该接口用来修改导播台水印信息。
        注意，修改的Index对应的水印需已存在

        :param request: Request instance for ModifyCasterMarkPicInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyCasterMarkPicInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyCasterMarkPicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCasterMarkPicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCasterMarkPicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCasterMarkWordInfo(self, request):
        """该接口用来修改导播台文本配置。

        :param request: Request instance for ModifyCasterMarkWordInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyCasterMarkWordInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyCasterMarkWordInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCasterMarkWordInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCasterMarkWordInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCasterOutputInfo(self, request):
        """该接口用来修改导播台的推流信息。
        注：只有在主监启动前设置才生效，主监启动后设置，下次推流生效。

        :param request: Request instance for ModifyCasterOutputInfo.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyCasterOutputInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyCasterOutputInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCasterOutputInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCasterOutputInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveCallbackTemplate(self, request):
        """修改回调模板。

        :param request: Request instance for ModifyLiveCallbackTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveCallbackTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveCallbackTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveCallbackTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveDomainCertBindings(self, request):
        """批量绑定证书对应的播放域名，并更新启用状态。
        新建自有证书将自动上传至腾讯云ssl。

        :param request: Request instance for ModifyLiveDomainCertBindings.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainCertBindingsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainCertBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveDomainCertBindings", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveDomainCertBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveDomainReferer(self, request):
        """设置直播域名 Referer 黑白名单。
        由于 Referer 信息包含在 http 协议中，在开启配置后，播放协议为 rtmp 或 WebRTC 不会校验 Referer 配置，仍可正常播放。如需配置 Referer 鉴权建议使用 http-flv 或 http-hls 协议播放。

        :param request: Request instance for ModifyLiveDomainReferer.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainRefererRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveDomainRefererResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveDomainReferer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveDomainRefererResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLivePadTemplate(self, request):
        """修改直播垫片模板。

        :param request: Request instance for ModifyLivePadTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePadTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePadTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLivePadTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLivePadTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLivePlayAuthKey(self, request):
        """修改播放鉴权key

        :param request: Request instance for ModifyLivePlayAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLivePlayAuthKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLivePlayAuthKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLivePlayDomain(self, request):
        """修改播放域名信息。

        :param request: Request instance for ModifyLivePlayDomain.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayDomainRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLivePlayDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLivePlayDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLivePullStreamTask(self, request):
        """更新直播拉流任务。
        1. 不支持修改拉流源类型，如需更换，请创建新任务。

        :param request: Request instance for ModifyLivePullStreamTask.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePullStreamTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePullStreamTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLivePullStreamTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLivePullStreamTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLivePushAuthKey(self, request):
        """修改直播推流鉴权key

        :param request: Request instance for ModifyLivePushAuthKey.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePushAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLivePushAuthKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLivePushAuthKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveRecordTemplate(self, request):
        """修改录制模板配置。

        :param request: Request instance for ModifyLiveRecordTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveRecordTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveRecordTemplateResponse`

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


    def ModifyLiveSnapshotTemplate(self, request):
        """修改截图模板配置。

        :param request: Request instance for ModifyLiveSnapshotTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveSnapshotTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveSnapshotTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveStreamMonitor(self, request):
        """该接口用来修改直播流监播任务的配置。

        :param request: Request instance for ModifyLiveStreamMonitor.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveStreamMonitorRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveStreamMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveStreamMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveStreamMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveTimeShiftTemplate(self, request):
        """修改直播时移模板。

        :param request: Request instance for ModifyLiveTimeShiftTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveTimeShiftTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveTimeShiftTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveTimeShiftTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveTimeShiftTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLiveTranscodeTemplate(self, request):
        """修改转码模板配置。

        :param request: Request instance for ModifyLiveTranscodeTemplate.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLiveTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLiveTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPullStreamConfig(self, request):
        """更新拉流配置。该接口为已下线接口，请使用新接口 ModifyLivePullStreamTask。

        :param request: Request instance for ModifyPullStreamConfig.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamConfigRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPullStreamConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPullStreamConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPullStreamStatus(self, request):
        """修改直播拉流配置的状态。该接口已下线,请使用新接口 ModifyLivePullStreamTask。

        :param request: Request instance for ModifyPullStreamStatus.
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamStatusRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPullStreamStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPullStreamStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseCaster(self, request):
        """调用该接口，释放导播台实例，但保留所有的配置。
        执行该接口，预监与主监画面停止，第三方推流停止。
        点播文件与直播地址将停止展示，客户自行推到导播台的流需要手动停止。

        :param request: Request instance for ReleaseCaster.
        :type request: :class:`tencentcloud.live.v20180801.models.ReleaseCasterRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ReleaseCasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseCaster", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseCasterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartLivePullStreamTask(self, request):
        """将正在运行的拉流转推任务进行重启。
        注意：
        1. 重启任务会造成推流中断。
        2. 点播源任务的重启，会根据VodRefreshType决定是续播还是从头开始播。

        :param request: Request instance for RestartLivePullStreamTask.
        :type request: :class:`tencentcloud.live.v20180801.models.RestartLivePullStreamTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.RestartLivePullStreamTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartLivePullStreamTask", params, headers=headers)
            response = json.loads(body)
            model = models.RestartLivePullStreamTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeDelayLiveStream(self, request):
        """取消直播流设置的延时配置，恢复实时直播画面。

        :param request: Request instance for ResumeDelayLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.ResumeDelayLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ResumeDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeDelayLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeDelayLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeLiveStream(self, request):
        """恢复某条流的推流。

        :param request: Request instance for ResumeLiveStream.
        :type request: :class:`tencentcloud.live.v20180801.models.ResumeLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ResumeLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendLiveCloudEffect(self, request):
        """使用该接口发送云端特效到线上正活跃的直播流，观众可在播放端看到特效从直播流画面中展示。

        :param request: Request instance for SendLiveCloudEffect.
        :type request: :class:`tencentcloud.live.v20180801.models.SendLiveCloudEffectRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.SendLiveCloudEffectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendLiveCloudEffect", params, headers=headers)
            response = json.loads(body)
            model = models.SendLiveCloudEffectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartLivePadStream(self, request):
        """使用该接口将直播流开始切入垫片。

        :param request: Request instance for StartLivePadStream.
        :type request: :class:`tencentcloud.live.v20180801.models.StartLivePadStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StartLivePadStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartLivePadStream", params, headers=headers)
            response = json.loads(body)
            model = models.StartLivePadStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartLiveStreamMonitor(self, request):
        """该接口用来启动直播流监播任务。

        :param request: Request instance for StartLiveStreamMonitor.
        :type request: :class:`tencentcloud.live.v20180801.models.StartLiveStreamMonitorRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StartLiveStreamMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartLiveStreamMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.StartLiveStreamMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCasterPgm(self, request):
        """该接口用来停止导播台的主监输出。
        停止主监后，对应的推流到腾讯云直播源站和推流到其他第三方平台均将会停止。

        :param request: Request instance for StopCasterPgm.
        :type request: :class:`tencentcloud.live.v20180801.models.StopCasterPgmRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopCasterPgmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCasterPgm", params, headers=headers)
            response = json.loads(body)
            model = models.StopCasterPgmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCasterPvw(self, request):
        """该接口用来停止导播台的预监任务。

        :param request: Request instance for StopCasterPvw.
        :type request: :class:`tencentcloud.live.v20180801.models.StopCasterPvwRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopCasterPvwResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCasterPvw", params, headers=headers)
            response = json.loads(body)
            model = models.StopCasterPvwResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopLivePadStream(self, request):
        """使用该接口将直播流停止切入垫片。

        :param request: Request instance for StopLivePadStream.
        :type request: :class:`tencentcloud.live.v20180801.models.StopLivePadStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopLivePadStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopLivePadStream", params, headers=headers)
            response = json.loads(body)
            model = models.StopLivePadStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopLiveRecord(self, request):
        """说明：录制后的文件存放于点播平台。用户如需使用录制功能，需首先自行开通点播账号并确保账号可用。录制文件存放后，相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，请参考对应文档。

        :param request: Request instance for StopLiveRecord.
        :type request: :class:`tencentcloud.live.v20180801.models.StopLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopLiveRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopLiveRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StopLiveRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopLiveStreamMonitor(self, request):
        """该接口用来停止直播流监播任务。

        :param request: Request instance for StopLiveStreamMonitor.
        :type request: :class:`tencentcloud.live.v20180801.models.StopLiveStreamMonitorRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopLiveStreamMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopLiveStreamMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.StopLiveStreamMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopRecordTask(self, request):
        """提前结束录制，中止运行中的录制任务并生成录制文件。任务被成功终止后，本次任务将不再启动。

        :param request: Request instance for StopRecordTask.
        :type request: :class:`tencentcloud.live.v20180801.models.StopRecordTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopRecordTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopRecordTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopRecordTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopScreenshotTask(self, request):
        """提前结束截图，中止运行中的截图任务。任务被成功终止后，本次任务将不再启动。

        :param request: Request instance for StopScreenshotTask.
        :type request: :class:`tencentcloud.live.v20180801.models.StopScreenshotTaskRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopScreenshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopScreenshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopScreenshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchBackupStream(self, request):
        """调用该接口实现切换当前播放所使用的主备流。

        :param request: Request instance for SwitchBackupStream.
        :type request: :class:`tencentcloud.live.v20180801.models.SwitchBackupStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.SwitchBackupStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchBackupStream", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchBackupStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnBindLiveDomainCert(self, request):
        """解绑域名证书

        :param request: Request instance for UnBindLiveDomainCert.
        :type request: :class:`tencentcloud.live.v20180801.models.UnBindLiveDomainCertRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.UnBindLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindLiveDomainCert", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindLiveDomainCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateLiveWatermark(self, request):
        """更新水印。

        :param request: Request instance for UpdateLiveWatermark.
        :type request: :class:`tencentcloud.live.v20180801.models.UpdateLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.UpdateLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))