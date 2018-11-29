# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def AddDelayLiveStream(self, request):
        """对流设置延播

        :param request: 调用AddDelayLiveStream所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.AddDelayLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddDelayLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddDelayLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddLiveWatermark(self, request):
        """添加水印

        :param request: 调用AddLiveWatermark所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.AddLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.AddLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveRecord(self, request):
        """- 使用前提
          1. 录制文件存放于点播平台，所以用户如需使用录制功能，需首先自行开通点播服务。
          2. 录制文件存放后相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，具体请参考 [对应文档](https://cloud.tencent.com/document/product/266/2838)。

        - 模式说明
          该接口支持两种录制模式：
          1. 定时录制模式。
            需要传入开始时间与结束时间，录制任务根据时间自动开始与结束。
          2. 实时视频录制模式。
            忽略传入的开始时间，在录制任务创建后立即开始录制，录制时长支持最大为30分钟，如果传入的结束时间与当前时间差大于30分钟，则按30分钟计算，实时视频录制主要用于录制精彩视频场景，时长建议控制在5分钟以内。

        - 注意事项
          1. 调用接口超时设置应大于3秒，小于3秒重试以及频繁调用都有可能产生重复录制任务。

        :param request: 调用CreateLiveRecord所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreateLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePullStreamConfig(self, request):
        """添加拉流配置，目前限制添加10条任务。

        :param request: 调用CreatePullStreamConfig所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.CreatePullStreamConfigRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.CreatePullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePullStreamConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePullStreamConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveRecord(self, request):
        """用于删除录制任务

        :param request: 调用DeleteLiveRecord所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveWatermark(self, request):
        """删除水印

        :param request: 调用DeleteLiveWatermark所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DeleteLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLivePlayAuthKey(self, request):
        """查询播放鉴权key

        :param request: 调用DescribeLivePlayAuthKey所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePlayAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLivePlayAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLivePlayAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLivePushAuthKey(self, request):
        """查询直播推流鉴权key

        :param request: 调用DescribeLivePushAuthKey所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLivePushAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLivePushAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLivePushAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamOnlineInfo(self, request):
        """查询在线推流信息列表

        :param request: 调用DescribeLiveStreamOnlineInfo所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineInfoRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamOnlineInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamOnlineInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamOnlineList(self, request):
        """返回正在直播中的流列表

        :param request: 调用DescribeLiveStreamOnlineList所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamOnlineListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamOnlineList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamOnlineListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamPublishedList(self, request):
        """返回已经推过流的流列表

        :param request: 调用DescribeLiveStreamPublishedList所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPublishedListRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamPublishedListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamPublishedList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamPublishedListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStreamState(self, request):
        """返回直播中、无推流或者禁播等状态

        :param request: 调用DescribeLiveStreamState所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamStateRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveStreamStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveWatermarks(self, request):
        """查询水印列表

        :param request: 调用DescribeLiveWatermarks所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarksRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribeLiveWatermarksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveWatermarks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveWatermarksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePullStreamConfigs(self, request):
        """查询拉流配置

        :param request: 调用DescribePullStreamConfigs所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DescribePullStreamConfigsRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DescribePullStreamConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePullStreamConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePullStreamConfigsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DropLiveStream(self, request):
        """断开推流连接，但可以重新推流

        :param request: 调用DropLiveStream所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.DropLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.DropLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DropLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DropLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ForbidLiveStream(self, request):
        """禁止某条流的推送，可以预设某个时刻将流恢复。

        :param request: 调用ForbidLiveStream所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ForbidLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ForbidLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ForbidLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForbidLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLivePlayAuthKey(self, request):
        """修改播放鉴权key

        :param request: 调用ModifyLivePlayAuthKey所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLivePlayAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLivePlayAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLivePushAuthKey(self, request):
        """修改直播推流鉴权key

        :param request: 调用ModifyLivePushAuthKey所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyLivePushAuthKeyRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLivePushAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLivePushAuthKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPullStreamConfig(self, request):
        """更新拉流配置

        :param request: 调用ModifyPullStreamConfig所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamConfigRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPullStreamConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPullStreamConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPullStreamStatus(self, request):
        """修改直播拉流配置状态

        :param request: 调用ModifyPullStreamStatus所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamStatusRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ModifyPullStreamStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPullStreamStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPullStreamStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeDelayLiveStream(self, request):
        """恢复延迟播放设置

        :param request: 调用ResumeDelayLiveStream所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ResumeDelayLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ResumeDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResumeDelayLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeDelayLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeLiveStream(self, request):
        """恢复某条流的推送。

        :param request: 调用ResumeLiveStream所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.ResumeLiveStreamRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.ResumeLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResumeLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetLiveWatermarkStatus(self, request):
        """设置水印是否启用

        :param request: 调用SetLiveWatermarkStatus所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.SetLiveWatermarkStatusRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.SetLiveWatermarkStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetLiveWatermarkStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetLiveWatermarkStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopLiveRecord(self, request):
        """说明：录制后的文件存放于点播平台。用户如需使用录制功能，需首先自行开通点播账号并确保账号可用。录制文件存放后，相关费用（含存储以及下行播放流量）按照点播平台计费方式收取，请参考对应文档。

        :param request: 调用StopLiveRecord所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.StopLiveRecordRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.StopLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopLiveRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateLiveWatermark(self, request):
        """更新水印

        :param request: 调用UpdateLiveWatermark所需参数的结构体。
        :type request: :class:`tencentcloud.live.v20180801.models.UpdateLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.live.v20180801.models.UpdateLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateLiveWatermarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)