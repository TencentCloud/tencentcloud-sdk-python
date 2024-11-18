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
from tencentcloud.trtc.v20190722 import models


class TrtcClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'trtc.tencentcloudapi.com'
    _service = 'trtc'


    def ControlAIConversation(self, request):
        """提供服务端控制机器人的功能

        :param request: Request instance for ControlAIConversation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.ControlAIConversationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ControlAIConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlAIConversation", params, headers=headers)
            response = json.loads(body)
            model = models.ControlAIConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudRecording(self, request):
        """接口说明：
        启动云端录制功能，完成房间内的音视频录制，并上传到指定的云存储。您可以通过此 API 接口把TRTC 房间中的每一路音视频流做单独的录制又或者多路视频画面合流混成一路。

        您可以通过此接口实现如下目标：
        * 指定订阅流参数（RecordParams）来指定需要录制的主播的黑名单或者白名单。
        * 指定录制存储参数（StorageParams）来指定上传到您希望的云存储，目前支持腾讯云（云点播VOD、对象存储COS）和第三方AWS
        * 指定合流模式下的音视频转码详细参数（MixTranscodeParams），包括视频分辨率、视频码率、视频帧率、以及声音质量等
        * 指定合流模式各路画面的位置和布局或者也可以指定自动模板的方式来配置。

        关键名词：
        * 单流录制：分别录制房间的订阅UserId的音频和视频，录制服务会实时将录制文件上传至您指定的云存储。
        * 合流录制：将房间内订阅UserId的音视频混录成一个视频文件，并将录制文件上传至您指定的云存储。（录制结束后可前往云点播控制台https://console.cloud.tencent.com/vod/media 或 对象存储COS控制台https://console.cloud.tencent.com/cos/bucket查看文件）。

        :param request: Request instance for CreateCloudRecording.
        :type request: :class:`tencentcloud.trtc.v20190722.models.CreateCloudRecordingRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CreateCloudRecordingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudRecording", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudRecordingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePicture(self, request):
        """如果您需要在 [云端混流转码](https://cloud.tencent.com/document/product/647/16827) 时频繁新增自定义背景图或水印，可通过此接口上传新的图片素材。无需频繁新增图片的场景，建议直接在 [控制台 > 应用管理 > 素材管理](https://cloud.tencent.com/document/product/647/50769) 中操作。

        :param request: Request instance for CreatePicture.
        :type request: :class:`tencentcloud.trtc.v20190722.models.CreatePictureRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CreatePictureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePicture", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePictureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudRecording(self, request):
        """成功开启录制后，可以使用此接口来停止录制任务。停止录制成功后不代表文件全部传输完成，如果未完成后台将会继续上传文件，成功后通过事件回调通知客户文件全部传输完成状态。

        :param request: Request instance for DeleteCloudRecording.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DeleteCloudRecordingRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DeleteCloudRecordingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudRecording", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudRecordingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePicture(self, request):
        """如果您需要在 [云端混流转码](https://cloud.tencent.com/document/product/647/16827) 时频繁删除自定义背景图或水印，可通过此接口删除已上传的图片。无需频繁删除图片的场景，建议直接在 [控制台 > 应用管理 > 素材管理](https://cloud.tencent.com/document/product/647/50769) 中操作。

        :param request: Request instance for DeletePicture.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DeletePictureRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DeletePictureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePicture", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePictureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIConversation(self, request):
        """查询AI对话任务状态。

        :param request: Request instance for DescribeAIConversation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeAIConversationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeAIConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIConversation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAITranscription(self, request):
        """查询AI转录任务状态。

        :param request: Request instance for DescribeAITranscription.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeAITranscriptionRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeAITranscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAITranscription", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAITranscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCallDetailInfo(self, request):
        """查询指定时间内的用户列表及用户通话质量数据，最大可查询14天内数据。DataType 不为null，查询起止时间不超过1个小时，查询用户不超过6个，支持跨天查询。DataType为null时，查询起止时间不超过4个小时， 默认查询6个用户，同时支持每页查询100以内用户个数（PageSize不超过100）。接口用于查询质量问题，不推荐作为计费使用。（同老接口DescribeCallDetail）
        **注意**：
        1.该接口只用于历史数据统计或核对数据使用，实时类关键业务逻辑不能使用。
        2.该接口自2024年4月1日起正式商业化，需订阅套餐解锁调用能力，提供以下两种解锁方式，可任选其一解锁：
        方式一：通过订阅[包月套餐](https://cloud.tencent.com/document/product/647/85386)「尊享版」（可查近7天）和「旗舰版」（可查近14天），[前往订阅](https://buy.cloud.tencent.com/trtc?trtcversion=top)。
        方式二：通过订阅[监控仪表盘](https://cloud.tencent.com/document/product/647/81331)商业套餐包「基础版」（可查近7天）和「进阶版」（可查近14天），[前往订阅](https://buy.cloud.tencent.com/trtc_monitor)。

        :param request: Request instance for DescribeCallDetailInfo.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeCallDetailInfoRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeCallDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCallDetailInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCallDetailInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudRecording(self, request):
        """成功开启录制后，可以使用此接口来查询录制状态。仅在录制任务进行时有效，录制退出后查询将会返回错误。
        录制文件上传到云点播VOD时，StorageFileList中不会返回录制文件信息，请订阅相关录制文件回调事件，获取录制文件信息。

        :param request: Request instance for DescribeCloudRecording.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeCloudRecordingRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeCloudRecordingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRecording", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRecordingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMixTranscodingUsage(self, request):
        """获取TRTC混流转码的用量明细。
        - 查询时间小于等于1天时，返回每5分钟粒度的数据；查询时间大于1天时，返回按天汇总的数据。
        - 单次查询统计区间最多不能超过31天。
        - 若查询当天用量，由于统计延迟等原因，返回数据可能不够准确。
        - 该接口只用于历史用量数据统计或核对数据使用，关键业务逻辑不能使用。
        - 默认接口请求频率限制：5次/秒。

        :param request: Request instance for DescribeMixTranscodingUsage.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeMixTranscodingUsageRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeMixTranscodingUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMixTranscodingUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMixTranscodingUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePicture(self, request):
        """如果您需要在 [云端混流转码](https://cloud.tencent.com/document/product/647/16827) 时频繁查找自定义背景图或水印信息，可通过此接口查找已上传的图片信息。无需频繁查找图片信息的场景，建议直接在 [控制台 > 应用管理 > 素材管理](https://cloud.tencent.com/document/product/647/50769) 中查看。

        :param request: Request instance for DescribePicture.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribePictureRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribePictureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePicture", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePictureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordStatistic(self, request):
        """查询云端录制计费时长。

        - 查询时间小于等于1天时，返回每5分钟粒度的数据；查询时间大于1天时，返回按天汇总的数据。
        - 单次查询统计区间最多不能超过31天。
        - 若查询当天用量，由于统计延迟等原因，返回数据可能不够准确。
        - 日结后付费将于次日上午推送账单，建议次日上午9点以后再来查询前一天的用量。

        :param request: Request instance for DescribeRecordStatistic.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRecordStatisticRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRecordStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordingUsage(self, request):
        """获取TRTC录制的用量明细。
        - 查询时间小于等于1天时，返回每5分钟粒度的数据；查询时间大于1天时，返回按天汇总的数据。
        - 单次查询统计区间最多不能超过31天。
        - 若查询当天用量，由于统计延迟等原因，返回数据可能不够准确。
        - 该接口只用于历史用量数据统计或核对数据使用，关键业务逻辑不能使用。
        - 默认接口请求频率限制：5次/秒。

        :param request: Request instance for DescribeRecordingUsage.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRecordingUsageRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRecordingUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordingUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordingUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRelayUsage(self, request):
        """获取TRTC旁路转推的用量明细。
        - 查询时间小于等于1天时，返回每5分钟粒度的数据；查询时间大于1天时，返回按天汇总的数据。
        - 单次查询统计区间最多不能超过31天。
        - 若查询当天用量，由于统计延迟等原因，返回数据可能不够准确。
        - 该接口只用于历史用量数据统计或核对数据使用，关键业务逻辑不能使用。
        - 默认接口请求频率限制：5次/秒。

        :param request: Request instance for DescribeRelayUsage.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRelayUsageRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRelayUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelayUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRelayUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoomInfo(self, request):
        """查询SdkAppId下的房间列表。默认返回10条通话，一次最多返回100条通话。最大可查询14天内的数据。（同老接口DescribeRoomInformation）
        **注意**：
        1.该接口只用于历史数据统计或核对数据使用，实时类关键业务逻辑不能使用。
        2.该接口自2024年4月1日起正式商业化，需订阅套餐解锁调用能力，提供以下两种解锁方式，可任意其一解锁：
        方式一：通过订阅[包月套餐](https://cloud.tencent.com/document/product/647/85386)「尊享版」（可查近7天）和「旗舰版」（可查近14天），[前往订阅](https://buy.cloud.tencent.com/trtc?trtcversion=top)。
        方式二：通过订阅[监控仪表盘](https://cloud.tencent.com/document/product/647/81331)商业套餐包「基础版」（可查近7天）和「进阶版」（可查近14天），[前往订阅](https://buy.cloud.tencent.com/trtc_monitor)。

        :param request: Request instance for DescribeRoomInfo.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRoomInfoRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRoomInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoomInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoomInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScaleInfo(self, request):
        """可查询SdkAppId每天的房间数和用户数，按天统计，可查询最近14天的数据。当天未结束，数据未统计完成，无法查到当天的房间数与用户数。（同老接口DescribeHistoryScale）

        :param request: Request instance for DescribeScaleInfo.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeScaleInfoRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeScaleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScaleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScaleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamIngest(self, request):
        """您可以查询输入在线媒体流任务的状态。

        :param request: Request instance for DescribeStreamIngest.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeStreamIngestRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeStreamIngestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamIngest", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamIngestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCMarketQualityData(self, request):
        """查询TRTC监控仪表盘-数据大盘质量指标（包括下列指标）
        joinSuccessRate：加入频道成功率。
        joinSuccessIn5sRate：5s内加入频道成功率。
        audioFreezeRate：音频卡顿率。
        videoFreezeRate：视频卡顿率。
        networkDelay ：网络延迟率。
        注意：
        1.调用接口需开通监控仪表盘【基础版】和【进阶版】，监控仪表盘【免费版】不支持调用，监控仪表盘[版本功能和计费说明](https://cloud.tencent.com/document/product/647/81331)。
        2.查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天。

        :param request: Request instance for DescribeTRTCMarketQualityData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketQualityDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketQualityDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCMarketQualityData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCMarketQualityDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCMarketQualityMetricData(self, request):
        """查询TRTC监控仪表盘-数据大盘质量指标（包括下列指标）
        joinSuccessRate：加入频道成功率。
        joinSuccessIn5sRate：5s内加入频道成功率。
        audioFreezeRate：音频卡顿率。
        videoFreezeRate：视频卡顿率。
        networkDelay ：网络延迟率。
        注意：
        1.调用接口需开通监控仪表盘【基础版】和【进阶版】，监控仪表盘【免费版】不支持调用，监控仪表盘版本功能和计费说明：https://cloud.tencent.com/document/product/647/81331。
        2.查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天。

        :param request: Request instance for DescribeTRTCMarketQualityMetricData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketQualityMetricDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketQualityMetricDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCMarketQualityMetricData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCMarketQualityMetricDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCMarketScaleData(self, request):
        """查询TRTC监控仪表盘-数据大盘规模指标（会返回通话人数，通话房间数，峰值同时在线人数，峰值同时在线频道数）
        userCount：通话人数，
        roomCount：通话房间数，从有用户加入频道到所有用户离开频道计为一个通话频道。
        peakCurrentChannels：峰值同时在线频道数。
        peakCurrentUsers：峰值同时在线人数。
        注意：
        1.调用接口需开通监控仪表盘【基础版】和【进阶版】，监控仪表盘【免费版】不支持调用，监控仪表盘[版本功能和计费说明](https://cloud.tencent.com/document/product/647/81331)。
        2.查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天。

        :param request: Request instance for DescribeTRTCMarketScaleData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketScaleDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketScaleDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCMarketScaleData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCMarketScaleDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCMarketScaleMetricData(self, request):
        """查询TRTC监控仪表盘-数据大盘规模指标（会返回通话人数，通话房间数，峰值同时在线人数，峰值同时在线频道数）
        userCount：通话人数，
        roomCount：通话房间数，从有用户加入频道到所有用户离开频道计为一个通话频道。
        peakCurrentChannels：峰值同时在线频道数。
        peakCurrentUsers：峰值同时在线人数。
        注意：
        1.调用接口需开通监控仪表盘【基础版】和【进阶版】，监控仪表盘【免费版】不支持调用，监控仪表盘版本功能和计费说明：https://cloud.tencent.com/document/product/647/81331。
        2.查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天。

        :param request: Request instance for DescribeTRTCMarketScaleMetricData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketScaleMetricDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketScaleMetricDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCMarketScaleMetricData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCMarketScaleMetricDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCRealTimeQualityData(self, request):
        """查询TRTC监控仪表盘-实时监控质量指标（会返回下列指标）
        -视频卡顿率
        -音频卡顿率
        注意：
        1.调用接口需开通监控仪表盘【基础版】和【进阶版】，监控仪表盘【免费版】不支持调用，监控仪表盘[版本功能和计费说明]（https://cloud.tencent.com/document/product/647/81331）。
        2.查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时。

        :param request: Request instance for DescribeTRTCRealTimeQualityData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeQualityDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeQualityDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCRealTimeQualityData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCRealTimeQualityDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCRealTimeQualityMetricData(self, request):
        """查询TRTC监控仪表盘-实时监控质量指标（会返回下列指标）
        -视频卡顿率
        -音频卡顿率
        注意：
        1.调用接口需开通监控仪表盘【基础版】和【进阶版】，监控仪表盘【免费版】不支持调用，监控仪表盘版本功能和计费说明：https://cloud.tencent.com/document/product/647/81331。
        2.查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时。

        :param request: Request instance for DescribeTRTCRealTimeQualityMetricData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeQualityMetricDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeQualityMetricDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCRealTimeQualityMetricData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCRealTimeQualityMetricDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCRealTimeScaleData(self, request):
        """查询TRTC监控仪表盘-实时监控规模指标（会返回下列指标）
        -userCount（在线用户数）
        -roomCount（在线房间数）
        注意：
        1.调用接口需开通监控仪表盘【基础版】和【进阶版】，监控仪表盘【免费版】不支持调用，监控仪表盘[版本功能和计费说明](https://cloud.tencent.com/document/product/647/81331)。
        2.查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时。
        3.除此之外您也可以通过[订阅TRTC包月套餐](https://buy.cloud.tencent.com/trtc)尊享版或旗舰版解锁此接口的调用能力，请在开通包月套餐后，请[提交工单](https://console.cloud.tencent.com/workorder/category)联系售后解锁调用能力

        :param request: Request instance for DescribeTRTCRealTimeScaleData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeScaleDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeScaleDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCRealTimeScaleData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCRealTimeScaleDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCRealTimeScaleMetricData(self, request):
        """查询TRTC监控仪表盘-实时监控规模指标（会返回下列指标）
        -userCount（在线用户数）
        -roomCount（在线房间数）
        注意：
        1.调用接口需开通监控仪表盘【基础版】和【进阶版】，监控仪表盘【免费版】不支持调用，监控仪表盘版本功能和计费说明：https://cloud.tencent.com/document/product/647/81331。
        2.查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时。
        xa0
        3.除此之外您也可以通过订阅TRTC包月套餐(https://buy.cloud.tencent.com/trtc)尊享版或旗舰版解锁此接口（DescribeTRTCRealTimeScaleMetricData）的调用能力，请在开通包月套餐后，请提交工单联系售后解锁调用能力https://console.cloud.tencent.com/workorder/category

        :param request: Request instance for DescribeTRTCRealTimeScaleMetricData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeScaleMetricDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeScaleMetricDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCRealTimeScaleMetricData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCRealTimeScaleMetricDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrtcMcuTranscodeTime(self, request):
        """查询旁路转码计费时长。
        - 查询时间小于等于1天时，返回每5分钟粒度的数据；查询时间大于1天时，返回按天汇总的数据。
        - 单次查询统计区间最多不能超过31天。
        - 若查询当天用量，由于统计延迟等原因，返回数据可能不够准确。
        - 日结后付费将于次日上午推送账单，建议次日上午9点以后再来查询前一天的用量。

        :param request: Request instance for DescribeTrtcMcuTranscodeTime.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTrtcMcuTranscodeTimeRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTrtcMcuTranscodeTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrtcMcuTranscodeTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrtcMcuTranscodeTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrtcRoomUsage(self, request):
        """查询TRTC音视频房间维度用量。
        - 单次只能查询一天数据，返回查询时间段内的汇总数据；通过多次查询可以查不同天数据。若查询跨天用量，由于统计延迟等原因，返回数据可能不够准确。
        - 该接口只用于历史用量数据统计或核对数据使用，关键业务逻辑不能使用，不可用于账单核对，如需对账请使用账号/应用维度用量API：DescribeTrtcUsage。
        - 默认接口请求频率限制：1次/15秒。
        - 数据最早可查日期为2023年4月1日0点，最大可查范围近3个月。

        :param request: Request instance for DescribeTrtcRoomUsage.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTrtcRoomUsageRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTrtcRoomUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrtcRoomUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrtcRoomUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrtcUsage(self, request):
        """获取TRTC音视频互动的用量明细，单位:分钟。
        - 查询时间小于等于1天时，返回每5分钟粒度的数据；查询时间大于1天时，返回按天汇总的数据。
        - 单次查询统计区间最多不能超过31天。
        - 若查询当天用量，由于统计延迟等原因，返回数据可能不够准确。
        - 该接口只用于历史用量数据统计或核对数据使用，关键业务逻辑不能使用。
        - 默认接口请求频率限制：5次/秒。

        :param request: Request instance for DescribeTrtcUsage.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTrtcUsageRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTrtcUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrtcUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrtcUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnusualEvent(self, request):
        """查询SdkAppId下任意20条异常体验事件，返回异常体验ID与可能产生异常体验的原因。可查询14天内数据，查询起止时间不超过1个小时。支持跨天查询。（同老接口DescribeAbnormalEvent）
        异常体验ID映射见：https://cloud.tencent.com/document/product/647/44916

        :param request: Request instance for DescribeUnusualEvent.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeUnusualEventRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeUnusualEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnusualEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnusualEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserEvent(self, request):
        """查询用户某次通话内的进退房，视频开关等详细事件。可查询14天内数据。（同接口DescribeDetailEvent）

        :param request: Request instance for DescribeUserEvent.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeUserEventRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeUserEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserInfo(self, request):
        """查询指定时间内的用户列表，最大可查询14天内数据，查询起止时间不超过4小时。默认每页查询6个用户，支持每页最大查询100个用户PageSize不超过100）。（同老接口DescribeUserInformation）
        **注意**：
        1.该接口只用于历史数据统计或核对数据使用，实时类关键业务逻辑不能使用。
        2.该接口自2024年4月1日起正式商业化，需订阅套餐解锁调用能力，提供以下两种解锁方式，可任选其一解锁：
        方式一：通过订阅[包月套餐](https://cloud.tencent.com/document/product/647/85386)「尊享版」（可查近7天）和「旗舰版」（可查近14天），[前往订阅](https://buy.cloud.tencent.com/trtc?trtcversion=top)。
        方式二：通过订阅[监控仪表盘](https://cloud.tencent.com/document/product/647/81331)商业套餐包「基础版」（可查近7天）和「进阶版」（可查近14天），[前往订阅](https://buy.cloud.tencent.com/trtc_monitor)。

        :param request: Request instance for DescribeUserInfo.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeUserInfoRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebRecord(self, request):
        """查询页面录制任务

        :param request: Request instance for DescribeWebRecord.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeWebRecordRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeWebRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DismissRoom(self, request):
        """接口说明：把房间所有用户从房间移出，解散房间。支持所有平台，Android、iOS、Windows 和 macOS 需升级到 TRTC SDK 6.6及以上版本。

        :param request: Request instance for DismissRoom.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DismissRoomRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DismissRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DismissRoom", params, headers=headers)
            response = json.loads(body)
            model = models.DismissRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DismissRoomByStrRoomId(self, request):
        """接口说明：把房间所有用户从房间移出，解散房间。支持所有平台，Android、iOS、Windows 和 macOS 需升级到 TRTC SDK 6.6及以上版本。

        :param request: Request instance for DismissRoomByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DismissRoomByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DismissRoomByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DismissRoomByStrRoomId", params, headers=headers)
            response = json.loads(body)
            model = models.DismissRoomByStrRoomIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudRecording(self, request):
        """成功开启录制后，可以使用此接口来更新录制任务。仅在录制任务进行时有效，录制退出后更新将会返回错误。更新操作是全量覆盖，并不是增量更新的模式，也就是说每次更新都需要携带全量的信息。

        :param request: Request instance for ModifyCloudRecording.
        :type request: :class:`tencentcloud.trtc.v20190722.models.ModifyCloudRecordingRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ModifyCloudRecordingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudRecording", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudRecordingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPicture(self, request):
        """如果您需要在 [云端混流转码](https://cloud.tencent.com/document/product/647/16827) 时频繁修改自定义背景图或水印素材，可通过此接口修改已上传的图片。无需频繁修改图片素材的场景，建议直接在 [控制台 > 应用管理 > 素材管理](https://cloud.tencent.com/document/product/647/50769) 中操作。

        :param request: Request instance for ModifyPicture.
        :type request: :class:`tencentcloud.trtc.v20190722.models.ModifyPictureRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ModifyPictureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPicture", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPictureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveUser(self, request):
        """接口说明：将用户从房间移出，适用于主播/房主/管理员踢人等场景。支持所有平台，Android、iOS、Windows 和 macOS 需升级到 TRTC SDK 6.6及以上版本。

        :param request: Request instance for RemoveUser.
        :type request: :class:`tencentcloud.trtc.v20190722.models.RemoveUserRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RemoveUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveUser", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveUserByStrRoomId(self, request):
        """接口说明：将用户从房间移出，适用于主播/房主/管理员踢人等场景。支持所有平台，Android、iOS、Windows 和 macOS 需升级到 TRTC SDK 6.6及以上版本。

        :param request: Request instance for RemoveUserByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.RemoveUserByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RemoveUserByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveUserByStrRoomId", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveUserByStrRoomIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartAIConversation(self, request):
        """启动AI对话任务，AI通道机器人进入TRTC房间，与房间内指定的成员进行AI对话，适用于智能客服，AI口语教师等场景

        TRTC AI对话功能内置语音转文本能力，同时提供通道服务，即客户可灵活指定第三方AI模型（LLM）服务和文本转音频（TTS)服务，更多[功能说明](https://cloud.tencent.com/document/product/647/108901)。

        :param request: Request instance for StartAIConversation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartAIConversationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartAIConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartAIConversation", params, headers=headers)
            response = json.loads(body)
            model = models.StartAIConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartAITranscription(self, request):
        """启动转录机器人，后台会通过机器人拉流进行实时进行语音识别并下发字幕和转录消息。
        转录机器人支持两种拉流方式，通过TranscriptionMode字段控制：
        - 拉取全房间的流。
        - 拉取特定用户的流。

        服务端通过TRTC的自定义消息实时下发字幕以及转录消息，CmdId固定是1。客户端只需监听自定义消息的回调即可，比如[c++回调](https://cloud.tencent.com/document/product/647/79637#4cd82f4edb24992a15a25187089e1565)。其他客户端比如安卓、Web等同样可在该链接处找到。

        :param request: Request instance for StartAITranscription.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartAITranscriptionRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartAITranscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartAITranscription", params, headers=headers)
            response = json.loads(body)
            model = models.StartAITranscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartMCUMixTranscode(self, request):
        """接口说明：启动云端混流，并指定混流画面中各路画面的布局位置。

        TRTC 的一个房间中可能会同时存在多路音视频流，您可以通过此 API 接口，通知腾讯云服务端将多路视频画面合成一路，并指定每一路画面的位置，同时将多路声音进行混音，最终形成一路音视频流，以便用于录制和直播观看。房间销毁后混流自动结束。

        您可以通过此接口实现如下目标：
        - 设置最终直播流的画质和音质，包括视频分辨率、视频码率、视频帧率、以及声音质量等。
        - 设置各路画面的位置和布局，您只需要在启动时设置一次，排版引擎会自动完成后续的画面排布。
        - 设置录制文件名，用于二次回放。
        - 设置 CDN 直播流 ID，用于在 CDN 进行直播观看。

        目前已经支持了如下几种布局模板：
        - 悬浮模板：第一个进入房间的用户的视频画面会铺满整个屏幕，其他用户的视频画面从左下角依次水平排列，显示为小画面，最多4行，每行4个，小画面悬浮于大画面之上。最多支持1个大画面和15个小画面，如果用户只发送音频，仍然会占用画面位置。
        - 九宫格模板：所有用户的视频画面大小一致，平分整个屏幕，人数越多，每个画面的尺寸越小。最多支持16个画面，如果用户只发送音频，仍然会占用画面位置。
        - 屏幕分享模板：适合视频会议和在线教育场景的布局，屏幕分享（或者主讲的摄像头）始终占据屏幕左侧的大画面位置，其他用户依次垂直排列于右侧，最多两列，每列最多8个小画面。最多支持1个大画面和15个小画面。若上行分辨率宽高比与画面输出宽高比不一致时，左侧大画面为了保持内容的完整性采用缩放方式处理，右侧小画面采用裁剪方式处理。
        - 画中画模板：适用于混合大小两路视频画面和其他用户混音，或者混合一路大画面和其他用户混音的场景。小画面悬浮于大画面之上，可以指定大小画面的用户以及小画面的显示位置，最多支持2个画面。
        - 自定义模板：适用于在混流中指定用户的画面位置，或者预设视频画面位置的场景。当预设位置指定用户时，排版引擎会为该用户预留位置；当预设位置未指定用户时，排版引擎会根据进房间顺序自动填充。预设位置填满时，不再混合其他用户的画面和声音。自定义模板启用占位图功能时（LayoutParams中的PlaceHolderMode设置成1），在预设位置的用户没有上行视频时可显示对应的占位图（PlaceImageId）。

        注意：
        1、**混流转码为收费功能，调用接口将产生云端混流转码费用，详见[云端混流转码计费说明](https://cloud.tencent.com/document/product/647/49446)。**
        2、2020年1月9号及以后创建的应用才能直接调用此接口。2020年1月9日之前创建的应用默认使用云直播的云端混流，如需切换至MCU混流，请[提交工单](https://console.cloud.tencent.com/workorder/category)寻求帮助。
        3、客户端混流和服务端混流不能混用。

        :param request: Request instance for StartMCUMixTranscode.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartMCUMixTranscodeRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartMCUMixTranscodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartMCUMixTranscode", params, headers=headers)
            response = json.loads(body)
            model = models.StartMCUMixTranscodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartMCUMixTranscodeByStrRoomId(self, request):
        """接口说明：启动云端混流，并指定混流画面中各路画面的布局位置。

        TRTC 的一个房间中可能会同时存在多路音视频流，您可以通过此 API 接口，通知腾讯云服务端将多路视频画面合成一路，并指定每一路画面的位置，同时将多路声音进行混音，最终形成一路音视频流，以便用于录制和直播观看。

        您可以通过此接口实现如下目标：
        - 设置最终直播流的画质和音质，包括视频分辨率、视频码率、视频帧率、以及声音质量等。
        - 设置各路画面的位置和布局，您只需要在启动时设置一次，排版引擎会自动完成后续的画面排布。
        - 设置录制文件名，用于二次回放。
        - 设置 CDN 直播流 ID，用于在 CDN 进行直播观看。

        目前已经支持了如下几种布局模板：
        - 悬浮模板：第一个进入房间的用户的视频画面会铺满整个屏幕，其他用户的视频画面从左下角依次水平排列，显示为小画面，最多4行，每行4个，小画面悬浮于大画面之上。最多支持1个大画面和15个小画面，如果用户只发送音频，仍然会占用画面位置。
        - 九宫格模板：所有用户的视频画面大小一致，平分整个屏幕，人数越多，每个画面的尺寸越小。最多支持16个画面，如果用户只发送音频，仍然会占用画面位置。
        - 屏幕分享模板：适合视频会议和在线教育场景的布局，屏幕分享（或者主讲的摄像头）始终占据屏幕左侧的大画面位置，其他用户依次垂直排列于右侧，最多两列，每列最多8个小画面。最多支持1个大画面和15个小画面。若上行分辨率宽高比与画面输出宽高比不一致时，左侧大画面为了保持内容的完整性采用缩放方式处理，右侧小画面采用裁剪方式处理。
        - 画中画模板：适用于混合大小两路视频画面和其他用户混音，或者混合一路大画面和其他用户混音的场景。小画面悬浮于大画面之上，可以指定大小画面的用户以及小画面的显示位置。
        - 自定义模板：适用于在混流中指定用户的画面位置，或者预设视频画面位置的场景。当预设位置指定用户时，排版引擎会为该用户预留位置；当预设位置未指定用户时，排版引擎会根据进房间顺序自动填充。预设位置填满时，不再混合其他用户的画面和声音。自定义模板启用占位图功能时（LayoutParams中的PlaceHolderMode设置成1），在预设位置的用户没有上行视频时可显示对应的占位图（PlaceImageId）。

        注意：
        1、**混流转码为收费功能，调用接口将产生云端混流转码费用，详见[云端混流转码计费说明](https://cloud.tencent.com/document/product/647/49446)。**
        2、2020年1月9号及以后创建的应用才能直接调用此接口。2020年1月9日之前创建的应用默认使用云直播的云端混流，如需切换至MCU混流，请[提交工单](https://console.cloud.tencent.com/workorder/category)寻求帮助。
        3、客户端混流和服务端混流不能混用。

        :param request: Request instance for StartMCUMixTranscodeByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartMCUMixTranscodeByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartMCUMixTranscodeByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartMCUMixTranscodeByStrRoomId", params, headers=headers)
            response = json.loads(body)
            model = models.StartMCUMixTranscodeByStrRoomIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartPublishCdnStream(self, request):
        """接口说明：
        启动一个混流转推任务，将  TRTC 房间的多路音视频流混成一路音视频流，编码后推到直播 CDN 或者回推到 TRTC 房间。也支持不转码直接转推 TRTC 房间的单路流。启动成功后，会返回一个 SdkAppid 维度唯一的任务 Id（TaskId）。您需要保存该 TaskId，后续需要依赖此 TaskId 更新和结束任务。可以参考文档： [功能说明](https://cloud.tencent.com/document/product/647/84721#b9a855f4-e38c-4616-9b07-fc44e0e8282a) 和 [常见问题](https://cloud.tencent.com/document/product/647/62620)

        注意：
        您可以在控制台开通旁路转推回调功能，对转推 CDN 状态的事件进行监控，回调请参考文档：[旁路转推回调说明](https://cloud.tencent.com/document/product/647/88552)
        您发起混流转推任务时，可能会产生如下费用：
        MCU 混流转码费用，请参考文档：[云端混流转码计费说明](https://cloud.tencent.com/document/product/647/49446)
        转推非腾讯云 CDN 费用，请参考文档：[云端转推计费说明](https://cloud.tencent.com/document/product/647/82155)

        :param request: Request instance for StartPublishCdnStream.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartPublishCdnStreamRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartPublishCdnStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartPublishCdnStream", params, headers=headers)
            response = json.loads(body)
            model = models.StartPublishCdnStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartStreamIngest(self, request):
        """将一个在线媒体流推到TRTC房间，更多功能说明见[输入媒体流进房](https://cloud.tencent.com/document/product/647/102957#50940aad-d90f-4473-9f46-d5dd46917653)。
        使用输入在线媒体流功能需先订阅 [尊享版或旗舰版套餐包](https://cloud.tencent.com/document/product/647/85386) 解锁能力位。

        :param request: Request instance for StartStreamIngest.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartStreamIngestRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartStreamIngestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartStreamIngest", params, headers=headers)
            response = json.loads(body)
            model = models.StartStreamIngestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartWebRecord(self, request):
        """通过此接口可以发起 WEB 页面录制任务，在接口参数中指定录制 URL，录制分辨率，录制结果存储等参数。
        因为参数或API逻辑问题会立即返回结果。而因为页面问题，如页面无法访问，会在回调中返回结果，请关注。

        :param request: Request instance for StartWebRecord.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartWebRecordRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartWebRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartWebRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StartWebRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAIConversation(self, request):
        """停止AI对话任务

        :param request: Request instance for StopAIConversation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopAIConversationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopAIConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAIConversation", params, headers=headers)
            response = json.loads(body)
            model = models.StopAIConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAITranscription(self, request):
        """停止AI转录任务。

        :param request: Request instance for StopAITranscription.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopAITranscriptionRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopAITranscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAITranscription", params, headers=headers)
            response = json.loads(body)
            model = models.StopAITranscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopMCUMixTranscode(self, request):
        """接口说明：结束云端混流

        :param request: Request instance for StopMCUMixTranscode.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopMCUMixTranscodeRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopMCUMixTranscodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopMCUMixTranscode", params, headers=headers)
            response = json.loads(body)
            model = models.StopMCUMixTranscodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopMCUMixTranscodeByStrRoomId(self, request):
        """接口说明：结束云端混流

        :param request: Request instance for StopMCUMixTranscodeByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopMCUMixTranscodeByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopMCUMixTranscodeByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopMCUMixTranscodeByStrRoomId", params, headers=headers)
            response = json.loads(body)
            model = models.StopMCUMixTranscodeByStrRoomIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopPublishCdnStream(self, request):
        """接口说明：
        停止指定的混流转推任务。如果没有调用 Stop 接口停止任务，所有参与混流转推的主播离开 TRTC 房间超过 AgentParams.MaxIdleTime 设置的时间后，任务也会自动停止。

        :param request: Request instance for StopPublishCdnStream.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopPublishCdnStreamRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopPublishCdnStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopPublishCdnStream", params, headers=headers)
            response = json.loads(body)
            model = models.StopPublishCdnStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopStreamIngest(self, request):
        """停止一个输入在线媒体流任务。

        :param request: Request instance for StopStreamIngest.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopStreamIngestRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopStreamIngestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopStreamIngest", params, headers=headers)
            response = json.loads(body)
            model = models.StopStreamIngestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopWebRecord(self, request):
        """停止页面录制任务

        :param request: Request instance for StopWebRecord.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopWebRecordRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopWebRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopWebRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StopWebRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAIConversation(self, request):
        """更新AIConversation参数

        :param request: Request instance for UpdateAIConversation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.UpdateAIConversationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UpdateAIConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAIConversation", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAIConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdatePublishCdnStream(self, request):
        """接口说明：
        成功发起混流转推后，可以使用此接口来更新任务。仅在任务进行时有效，任务退出后更新将会返回错误。更新操作为增量更新模式。
        注意：为了保障推流的稳定性，更新不支持任务在纯音频、音视频、纯视频之间进行切换。

        :param request: Request instance for UpdatePublishCdnStream.
        :type request: :class:`tencentcloud.trtc.v20190722.models.UpdatePublishCdnStreamRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UpdatePublishCdnStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePublishCdnStream", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePublishCdnStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateStreamIngest(self, request):
        """更新输入在线媒体流任务的StreamUrl

        :param request: Request instance for UpdateStreamIngest.
        :type request: :class:`tencentcloud.trtc.v20190722.models.UpdateStreamIngestRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UpdateStreamIngestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateStreamIngest", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateStreamIngestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))