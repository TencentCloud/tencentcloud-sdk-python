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
from tencentcloud.ams.v20201229 import models


class AmsClient(AbstractClient):
    _apiVersion = '2020-12-29'
    _endpoint = 'ams.tencentcloudapi.com'
    _service = 'ams'


    def CancelTask(self, request):
        """取消任务

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.ams.v20201229.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAudioModerationSyncTask(self, request):
        """本接口（CreateAudioModerationSyncTask） 用于提交短音频内容进行智能审核任务，使用前请您登陆控制台开通音频内容安全服务。

        功能使用说明：
        前往“内容安全控制台-音频内容安全”开启使用音频内容安全服务，首次开通可获得10小时免费调用时长；

        接口限制：
        - 音频文件大小支持：文件 < 5M;
        - 音频文件时长小于60s，超过60s音频调用则报错；
        - 音频码率类型支持：8Kbps - 16Kbps；
        - 音频文件支持格式：wav、mp3；
        - 接口仅限音频文件传入，视频文件传入请调用长音频异步接口；
        - 接口默认QPS为10，默认接口请求频率限制20次/秒，如需要更高的并发或请求频率，请工单咨询；
        - 接口超时为5s，每一次请求超过该时长会报错；

        :param request: Request instance for CreateAudioModerationSyncTask.
        :type request: :class:`tencentcloud.ams.v20201229.models.CreateAudioModerationSyncTaskRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.CreateAudioModerationSyncTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAudioModerationSyncTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAudioModerationSyncTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAudioModerationTask(self, request):
        """本接口（Audio Moderation）用于提交音频内容（包括音频文件或流地址）进行智能审核任务，使用前请您登陆控制台开通音频内容安全服务。

        ### 功能使用说明：
        - 前往“内容安全控制台-音频内容安全”开启使用音频内容安全服务，首次开通可获得20小时免费调用时长

        ### 接口功能说明：
        - 支持对音频流或音频文件进行检测，判断其中是否包含违规内容；
        - 支持设置回调地址 Callback 获取检测结果，或通过接口(查询音频检测结果)主动轮询获取检测结果；
        - 支持识别违规内容，包括：低俗、谩骂、色情、涉政、广告等场景；
        - 支持批量提交检测任务。检测任务列表最多支持10个；

        ### 音频文件调用说明：
        - 音频文件大小支持：文件 < 500M；
        - 音频文件时长支持：< 1小时；
        - 音频码率类型支持：128 Kbps - 256 Kbps ；
        - 音频文件支持格式：wav、mp3、aac、flac、amr、3gp、 m4a、wma、ogg、ape；
        - 支持音视频文件分离并对音频文件进行独立识别；

        ### 音频流调用说明：
        - 音频流时长支持：< 3小时；
        - 音频码率类型支持：128 Kbps - 256 Kbps ；
        - 音频流支持的传输协议：RTMP、HTTP、HTTPS；
        - 音频流格式支持的类型：rtp、srtp、rtmp、rtmps、mmsh、 mmst、hls、http、tcp、https、m3u8；
        - 支持音视频流分离并对音频流进行独立识别；

        :param request: Request instance for CreateAudioModerationTask.
        :type request: :class:`tencentcloud.ams.v20201229.models.CreateAudioModerationTaskRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.CreateAudioModerationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAudioModerationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAudioModerationTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskDetail(self, request):
        """查看任务详情

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.ams.v20201229.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasks(self, request):
        """查看审核任务列表

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.ams.v20201229.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)