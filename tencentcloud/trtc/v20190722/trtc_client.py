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


    def CreateCloudRecording(self, request):
        """接口说明：
        启动云端录制功能，完成房间内的音视频录制，并上传到指定的云存储。您可以通过此 API 接口把TRTC 房间中的每一路音视频流做单独的录制有或者多路视频画面混流一路。

        您可以通过此接口实现如下目标：
        * 指定订阅流参数（RecordParams）来指定需要录制的主播的黑名单或者白名单。
        * 指定第三方存储的参数（StorageParams）来指定上传到您希望的云存储，目前仅支持云点播存储（CloudVod）
        * 指定混流模式下的音视频转码详细参数（MixTranscodeParams），包括视频分辨率、视频码率、视频帧率、以及声音质量等
        * 指定混流模式各路画面的位置和布局或者也可以指定自动模板的方式来配置。

        关键名词：
        * 单流录制：分别录制房间的订阅UserId的音频和视频。录制服务会实时将录制文件上传至云点播存储。
        * 合流录制：将房间内订阅UserId的音视频混录成一个音视频文件，并将录制文件上传至云点播存储（录制结束后可前往云点播控制台查看录制文件：https://console.cloud.tencent.com/vod/media）。

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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCallDetailInfo(self, request):
        """查询指定时间内的用户列表及用户通话质量数据，可查询14天内数据。DataType 不为null，查询起止时间不超过1个小时，查询用户不超过6个，支持跨天查询。DataType为null时，查询起止时间不超过4个小时， 默认查询6个用户，同时支持每页查询100以内用户个数（PageSize不超过100）。接口用于查询质量问题，不推荐作为计费使用。（同老接口DescribeCallDetail）
        **注意**：
        1.该接口只用于历史数据统计或核对数据使用，实时类关键业务逻辑不能使用。
        2.该接口目前免费提供中，监控仪表盘商业化计费后该接口需要订阅付费版后方可调用，仪表盘商业化说明请见：https://cloud.tencent.com/document/product/647/77735

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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExternalTrtcMeasure(self, request):
        """接口内部调用计量接口，计量接口迁通用集群后不可用。目前已有新的对外接口可以供用户使用。

        获取Trtc的用量统计数据。走计费渠道二期 只允许查两天的数据。
        当前接口已不再更新维护，请使用新版音视频用量接口：DescribeTrtcUsage （https://cloud.tencent.com/document/product/647/81425）

        :param request: Request instance for DescribeExternalTrtcMeasure.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeExternalTrtcMeasureRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeExternalTrtcMeasureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExternalTrtcMeasure", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExternalTrtcMeasureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRoomInfo(self, request):
        """查询SdkAppId下的房间列表。默认返回10条通话，一次最多返回100条通话。可查询14天内的数据。（同老接口DescribeRoomInformation）
        **注意**：
        1.该接口只用于历史数据统计或核对数据使用，实时类关键业务逻辑不能使用。
        2.该接口目前免费提供中，监控仪表盘商业化计费后该接口需要订阅付费版后方可调用，仪表盘商业化说明请见：https://cloud.tencent.com/document/product/647/77735

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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTRTCRealTimeScaleMetricData(self, request):
        """查询TRTC监控仪表盘-实时监控规模指标（会返回下列指标）
        -userCount（在线用户数）
        -roomCount（在线房间数）
        注意：
        1.调用接口需开通监控仪表盘【基础版】和【进阶版】，监控仪表盘【免费版】不支持调用，监控仪表盘版本功能和计费说明：https://cloud.tencent.com/document/product/647/81331。
        2.查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时。

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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTrtcUsage(self, request):
        """获取TRTC音视频互动的用量明细。
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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserInfo(self, request):
        """查询指定时间内的用户列表，可查询14天内数据，查询起止时间不超过4小时。默认每页查询6个用户，支持每页最大查询100个用户PageSize不超过100）。（同老接口DescribeUserInformation）
        **注意**：
        1.该接口只用于历史数据统计或核对数据使用，实时类关键业务逻辑不能使用。
        2.该接口目前免费提供中，监控仪表盘商业化计费后该接口需要订阅付费版后方可调用，仪表盘商业化说明请见：https://cloud.tencent.com/document/product/647/77735

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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
        - 自定义模板：适用于在混流中指定用户的画面位置，或者预设视频画面位置的场景。当预设位置指定用户时，排版引擎会该用户预留位置；当预设位置未指定用户时，排版引擎会根据进房间顺序自动填充。预设位置填满时，不再混合其他用户的画面和声音。自定义模板启用占位图功能时（LayoutParams中的PlaceHolderMode设置成1），在预设位置的用户没有上行视频时可显示对应的占位图（PlaceImageId）。

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
                raise TencentCloudSDKException(e.message, e.message)


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
        - 自定义模板：适用于在混流中指定用户的画面位置，或者预设视频画面位置的场景。当预设位置指定用户时，排版引擎会该用户预留位置；当预设位置未指定用户时，排版引擎会根据进房间顺序自动填充。预设位置填满时，不再混合其他用户的画面和声音。自定义模板启用占位图功能时（LayoutParams中的PlaceHolderMode设置成1），在预设位置的用户没有上行视频时可显示对应的占位图（PlaceImageId）。

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
                raise TencentCloudSDKException(e.message, e.message)


    def StartPublishCdnStream(self, request):
        """接口说明：启动旁路以及混流转推任务。TRTC 的房间中可能会同时存在多路音视频流，您可以通过此API接口，实现以下几种效果：
        1、支持将单个主播的音视频流发布（也称作“转推”）到直播CDN上，请参考示例2（发起单流音视频旁路转推）和示例3（发起单流纯音频旁路转推）。
        2、支持将同个房间多个主播或者不同房间多个主播的音视频混合成1路后再发布到直播CDN上，您可以通过AudioParams.SubscribeAudioList和VideoParams.LayoutParams调整参与混音的用户列表以及指定各路混流画面的布局位置。请参考示例1（发起混流转推）。
        3、支持预先设置一个房间的混流模板，将该房间中的多个音视频混合成1路发布到直播CDN，腾讯云后台实时监控TRTC房间中的主播变化，自动按照混流模板调整布局。目前已经支持了如下几种混流预设模板：
             - 悬浮模板：第一个进入房间的用户的视频画面会铺满整个屏幕，其他用户的视频画面从左下角依次水平排列，显示为小画面，最多4行，每行4个，小画面悬浮于大画面之上。最多支持1个大画面和15个小画面。
             - 九宫格模板：所有用户的视频画面大小一致，平分整个屏幕，人数越多，每个画面的尺寸越小，最多支持16个画面。
             - 屏幕分享模板：适合视频会议和在线教育场景的布局，屏幕分享（或者主讲的摄像头）始终占据屏幕左侧的大画面位置，其他用户依次垂直排列于右侧，最多两列，每列最多8个小画面。最多支持1个大画面和15个小画面。若上行分辨率宽高比与画面输出宽高比不一致时，左侧大画面为了保持内容的完整性采用缩放方式处理，右侧小画面采用裁剪方式处理。
        4、支持同时将音视频流发布到最多10个直播CDN上。您可以通过PublishCdnParams.PublishCdnUrl指定转推CDN的url，如果您想转推到腾讯云CDN，PublishCdnParams.IsTencentCdn填为1。
        5、支持通过配置服务端回调，实时将转推状态以HTTP/HTTPS POST 请求发送给您的服务器，如果您需要接入转推事件回调，请联系腾讯云技术支持。
        6、云API调用支持广州、上海、北京、香港四个地域，如果您想转推海外，请选择香港地域。
        7、国内站默认只支持转推腾讯云CDN，如您有转推第三方CDN的需求，请联系腾讯云技术支持，由后台进行评估。
        注意：
        1、**混流转码为收费功能，调用接口将产生云端混流转码费用，详见[云端混流转推计费说明](https://cloud.tencent.com/document/product/647/49446)。**
        2、**转推非腾讯云CDN将产生云端转推费用，详见[云端混流转推计费说明](https://cloud.tencent.com/document/product/647/82155)。**

        其他使用说明如下：
        1、使用混流转推接口时，您需要先调用启动转推任务接口（StartPublishCdnStream），获取启动转推任务响应中的任务ID标识（TaskId）。后续传入任务ID标识（TaskId）来更新转推任务（UpdatePublishCdnStream）和停止转推任务（StopPublishCdnStream）。
        2、为了确保转推链接的稳定，同一个转推任务不支持纯音频、音视频、纯视频之间的切换。
        3、为了确保转推链接的稳定，更新转推任务接口（UpdatePublishCdnStream）不支持时更改视频参数（codec）和音频参数（codec、采样率、码率、声道数），其余参数建议全量带齐。
        4、发起单流旁路任务时，AudioParams和VideoParams都填写表示音视频旁路，如果仅填写AudioParams表示纯音频旁路，任务进行过程中不支持纯音频到音视频的切换。音视频旁路时，VideoParams中的Width、Height、Fps、BitRate、Gop需要按照真实上行参数填写。
        5、更新转推任务（UpdatePublishCdnStream）必须携带SequenceNumber参数，用于防止请求乱序。客户保证对同一个任务更新时的SequenceNumber参数递增：腾讯云返回InternalError错误码时，需重试请求（不换SequenceNumber）；腾讯云返回FailedOperation.OutdateRequest过期错误码时，无需处理即可。
        6、您可以在主播进房前，提前创建转推任务，结束转推任务时需要主动调用停止接口。如果您没有调用停止转推任务接口时，腾讯云后台会按照所有参与混流的用户没有任何数据上行的时间算起，直到超过启动转推任务时设置的超时时间（AgentParams.MaxIdleTime）为止，自动停止混流转推任务。

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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def StopPublishCdnStream(self, request):
        """停止转推任务。

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
                raise TencentCloudSDKException(e.message, e.message)


    def UpdatePublishCdnStream(self, request):
        """更新转推任务。
        注：请参见启动转推任务的接口说明和使用说明。

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
                raise TencentCloudSDKException(e.message, e.message)