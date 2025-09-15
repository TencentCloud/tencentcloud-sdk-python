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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.ams.v20201229 import models


class AmsClient(AbstractClient):
    _apiVersion = '2020-12-29'
    _endpoint = 'ams.tencentcloudapi.com'
    _service = 'ams'


    def CancelTask(self, request):
        r"""可使用该接口取消审核任务。请求成功后，接口返回RequestId则说明取消成功。<br>默认接口请求频率限制：**20次/秒**。

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.ams.v20201229.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAudioModerationSyncTask(self, request):
        r"""本接口（CreateAudioModerationSyncTask） 用于提交短音频内容进行智能审核任务，使用前请您使用腾讯云主账号登录控制台 [开通音频内容安全服务](https://console.cloud.tencent.com/cms/audio/package) 并调整好对应的业务配置。

        ### 接口使用说明：
        - 前往“[内容安全控制台-图片内容安全](https://console.cloud.tencent.com/cms/audio/package)”开启使用音频内容安全服务，首次开通服务的用户可免费领用试用套餐包，包含**10小时**免费调用时长，有效期为1个月。
        - 该接口为收费接口，计费方式敬请参见 [腾讯云音频内容安全定价](https://cloud.tencent.com/product/ams/pricing)。

        ### 接口调用说明：
        - 音频文件大小支持：**文件 <= 4M**;
        - 音频文件**时长不超过60s**，超过60s音频调用则报错；
        - 音频文件支持格式：**wav (PCM编码)** 、**mp3**、**aac**、**m4a** (采样率：16kHz~48kHz，位深：16bit 小端，声道数：单声道/双声道，建议格式：**16kHz/16bit/单声道**)；
        - 接口仅限音频文件传入，视频文件传入请调用长音频异步接口；
        - 接口**默认QPS为20**，如需自定义配置并发或请求频率，请工单咨询；
        - 接口**默认超时为10s**，请求如超过该时长则接口会报错。

        :param request: Request instance for CreateAudioModerationSyncTask.
        :type request: :class:`tencentcloud.ams.v20201229.models.CreateAudioModerationSyncTaskRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.CreateAudioModerationSyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAudioModerationSyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAudioModerationSyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAudioModerationTask(self, request):
        r"""本接口（Audio Moderation）用于提交音频内容（包括音频文件或流地址）进行智能审核任务，使用前请您使用腾讯云主账号登录控制台[开通音频内容安全服务](https://console.cloud.tencent.com/cms)并调整好对应的业务配置。<br>

        ### 功能使用说明：
        - 前往“[内容安全控制台-音频内容安全](https://console.cloud.tencent.com/cms)”开启使用音频内容安全服务，首次开通可获得**10小时**免费调用时长，有效期为1个月。

        ### 审核并发限制说明:

        - **点播音频（异步审核）**
            - 默认并发路数：10
            - 队列处理机制：
                - 当并发任务达到上限时，新任务进入队列等待处理;
                -  新送审任务优先处理，旧任务往后排;
        - **直播音频（异步审核）**
            - 默认并发路数：100
            - 队列处理机制：
              - 运行中的审核任务达到上限时，新请求会提示超频错误：`RequestLimitExceeded`，错误详细为：`You have reached the concurrency limit`;
              - 不支持排队;

        ### 接口功能说明：
        - 支持对音频流或音频文件进行检测，判断其中是否包含违规内容；
        - 支持设置回调地址 Callback 获取检测结果（对于已在审核的任务，最长回调时间为用户配置的**切片时长 + 2s**），或通过接口(查询音频检测结果)主动轮询获取检测结果；
        - 支持识别违规内容，包括：低俗、谩骂、色情、广告等场景；
        - 支持批量提交检测任务，检测任务列表**最多支持10个**。

        ### 音频文件流调用说明：
        - 音频文件大小支持：**文件 < 500M**；
        - 音频文件时长支持：**< 1小时**；
        - 音频码率类型支持：128 Kbps - 256 Kbps ；
        - 音频文件支持格式：wav、mp3、aac、flac、amr、3gp、 m4a、wma、ogg、ape；
        - （**当输入为视频文件时**）支持分离视频文件音轨，并对音频内容进行独立审核。

        ### 直播音频流调用说明：
        - 音频流时长支持：**24小时以内**，超过需要重新推送审核任务；
        - 音频码率类型支持：128 Kbps - 256 Kbps ；
        - 音频流支持的传输协议：RTMP、HTTP、HTTPS；
        - 音频流格式支持的类型：rtp、srtp、rtmp、rtmps、mmsh、 mmst、hls、http、tcp、https、m3u8；
        - （**当输入为视频流时**）支持提取视频流音轨，并对音频内容进行独立审核。

        ### 直播断流处理说明：
        - 请确认已对接[取消任务](https://cloud.tencent.com/document/product/1219/53258)。
        - 如果直播任务取消/结束，则终止直播拉流并退出审核。
        - 在直播任务未取消或结束的情况下，若推流中断（例如 `Operation not permitted` 错误），审核服务将在 10分钟内持续尝试重新拉流。检测到有效的图片或音频数据，审核将自动恢复正常；否则，10分钟后终止拉流并退出审核。此时如有需要，请重新提交审核请求。对于因网络问题导致的拉流失败（如 `HTTP 404 Not Found` 错误），系统将进行最多 16次重试。若成功获取有效数据，审核流程即刻恢复；若所有重试均失败，则同样终止拉流并退出审核，需用户重新送审。

        :param request: Request instance for CreateAudioModerationTask.
        :type request: :class:`tencentcloud.ams.v20201229.models.CreateAudioModerationTaskRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.CreateAudioModerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAudioModerationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAudioModerationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskDetail(self, request):
        r"""通过该接口可查看音频审核任务的详情信息，包括任务状态、检测结果、音频文件识别出的对应文本内容、检测结果所对应的恶意标签及推荐的后续操作等，具体输出内容可查看输出参数示例。

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.ams.v20201229.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.DescribeTaskDetailResponse`

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
        r"""通过该接口可查看审核任务列表；您也可根据多种业务信息（业务类型、审核结果、任务状态等）筛选审核任务列表。任务列表输出内容包括当前查询的任务总量、任务名称、任务状态、音频审核类型、基于检测结果的恶意标签及其后续操作等，具体输出内容可查看输出参数示例。<br>默认接口请求频率限制：**20次/秒**。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.ams.v20201229.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.DescribeTasksResponse`

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