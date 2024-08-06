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
from tencentcloud.vrs.v20200824 import models


class VrsClient(AbstractClient):
    _apiVersion = '2020-08-24'
    _endpoint = 'vrs.tencentcloudapi.com'
    _service = 'vrs'


    def CancelVRSTask(self, request):
        """声音复刻取消任务接口

        :param request: Request instance for CancelVRSTask.
        :type request: :class:`tencentcloud.vrs.v20200824.models.CancelVRSTaskRequest`
        :rtype: :class:`tencentcloud.vrs.v20200824.models.CancelVRSTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelVRSTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelVRSTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVRSTask(self, request):
        """本接口服务对提交音频进行声音复刻任务创建接口，异步返回复刻结果。
        • 请求方法为 HTTP POST , Content-Type为"application/json; charset=utf-8"
        • 签名方法参考 公共参数 中签名方法v3。

        :param request: Request instance for CreateVRSTask.
        :type request: :class:`tencentcloud.vrs.v20200824.models.CreateVRSTaskRequest`
        :rtype: :class:`tencentcloud.vrs.v20200824.models.CreateVRSTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVRSTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVRSTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVRSTaskStatus(self, request):
        """在调用声音复刻创建任务请求接口后，有回调和轮询两种方式获取识别结果。
        • 当采用回调方式时，识别完成后会将结果通过 POST 请求的形式通知到用户在请求时填写的回调 URL，具体请参见 声音复刻结果回调 。
        • 当采用轮询方式时，需要主动提交任务ID来轮询识别结果，共有任务成功、等待、执行中和失败四种结果，具体信息请参见下文说明。
        • 请求方法为 HTTP POST , Content-Type为"application/json; charset=utf-8"
        • 签名方法参考 公共参数 中签名方法v3。

        :param request: Request instance for DescribeVRSTaskStatus.
        :type request: :class:`tencentcloud.vrs.v20200824.models.DescribeVRSTaskStatusRequest`
        :rtype: :class:`tencentcloud.vrs.v20200824.models.DescribeVRSTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVRSTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVRSTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectEnvAndSoundQuality(self, request):
        """本接口用于检测音频的环境和音频质量。
        对于一句话声音复刻，音频时长需大于3s，小于15s，文件大小不能超过2MB，音频需为单声道，位深为16bit。建议格式：wav、单声道、采样率48kHz或24kHz
        • 请求方法为 HTTP POST , Content-Type为"application/json; charset=utf-8"
        • 签名方法参考 公共参数 中签名方法v3。

        :param request: Request instance for DetectEnvAndSoundQuality.
        :type request: :class:`tencentcloud.vrs.v20200824.models.DetectEnvAndSoundQualityRequest`
        :rtype: :class:`tencentcloud.vrs.v20200824.models.DetectEnvAndSoundQualityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectEnvAndSoundQuality", params, headers=headers)
            response = json.loads(body)
            model = models.DetectEnvAndSoundQualityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadVRSModel(self, request):
        """下载声音复刻离线模型

        :param request: Request instance for DownloadVRSModel.
        :type request: :class:`tencentcloud.vrs.v20200824.models.DownloadVRSModelRequest`
        :rtype: :class:`tencentcloud.vrs.v20200824.models.DownloadVRSModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadVRSModel", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadVRSModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTrainingText(self, request):
        """本接口用于获取声音复刻训练文本信息。
         请求方法为 HTTP POST , Content-Type为"application/json; charset=utf-8"
        • 签名方法参考 公共参数 中签名方法v3。

        :param request: Request instance for GetTrainingText.
        :type request: :class:`tencentcloud.vrs.v20200824.models.GetTrainingTextRequest`
        :rtype: :class:`tencentcloud.vrs.v20200824.models.GetTrainingTextResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTrainingText", params, headers=headers)
            response = json.loads(body)
            model = models.GetTrainingTextResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetVRSVoiceTypes(self, request):
        """查询复刻音色

        :param request: Request instance for GetVRSVoiceTypes.
        :type request: :class:`tencentcloud.vrs.v20200824.models.GetVRSVoiceTypesRequest`
        :rtype: :class:`tencentcloud.vrs.v20200824.models.GetVRSVoiceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetVRSVoiceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.GetVRSVoiceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))