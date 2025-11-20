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
from tencentcloud.vrs.v20200824 import models
from typing import Dict


class VrsClient(AbstractClient):
    _apiVersion = '2020-08-24'
    _endpoint = 'vrs.tencentcloudapi.com'
    _service = 'vrs'

    async def CancelVRSTask(
            self,
            request: models.CancelVRSTaskRequest,
            opts: Dict = None,
    ) -> models.CancelVRSTaskResponse:
        """
        声音复刻取消任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "CancelVRSTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelVRSTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVRSTask(
            self,
            request: models.CreateVRSTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVRSTaskResponse:
        """
        本接口服务对提交音频进行声音复刻任务创建接口，异步返回复刻结果。
        • 请求方法为 HTTP POST , Content-Type为"application/json; charset=utf-8"
        • 签名方法参考 公共参数 中签名方法v3。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVRSTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVRSTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVRSTaskStatus(
            self,
            request: models.DescribeVRSTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeVRSTaskStatusResponse:
        """
        在调用声音复刻创建任务请求接口后，有回调和轮询两种方式获取识别结果。（注意：回调方式暂不支持一句话版声音复刻）
        • 当采用回调方式时，识别完成后会将结果通过 POST 请求的形式通知到用户在请求时填写的回调 URL，具体请参见 [“声音复刻任务创建接口”](https://cloud.tencent.com/document/product/1283/90064) CallbackUrl参数说明 。
        • 当采用轮询方式时，需要主动提交任务ID来轮询识别结果，共有任务成功、等待、执行中和失败四种结果，具体信息请参见下文说明。
        • 请求方法为 HTTP POST , Content-Type为"application/json; charset=utf-8"
        • 签名方法参考 公共参数 中签名方法v3。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVRSTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVRSTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectEnvAndSoundQuality(
            self,
            request: models.DetectEnvAndSoundQualityRequest,
            opts: Dict = None,
    ) -> models.DetectEnvAndSoundQualityResponse:
        """
        本接口用于检测音频的环境和音频质量。
        对于一句话声音复刻，音频时长需大于5s，小于15s，文件大小不能超过2MB，音频需为单声道，位深为16bit。建议格式：wav、单声道、采样率48kHz或24kHz
        • 请求方法为 HTTP POST , Content-Type为"application/json; charset=utf-8"
        • 签名方法参考 公共参数 中签名方法v3。
        """
        
        kwargs = {}
        kwargs["action"] = "DetectEnvAndSoundQuality"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectEnvAndSoundQualityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadVRSModel(
            self,
            request: models.DownloadVRSModelRequest,
            opts: Dict = None,
    ) -> models.DownloadVRSModelResponse:
        """
        下载声音复刻离线模型
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadVRSModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadVRSModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTrainingText(
            self,
            request: models.GetTrainingTextRequest,
            opts: Dict = None,
    ) -> models.GetTrainingTextResponse:
        """
        本接口用于获取声音复刻训练文本信息。
         请求方法为 HTTP POST , Content-Type为"application/json; charset=utf-8"
        • 签名方法参考 公共参数 中签名方法v3。
        • 当复刻类型为一句话声音复刻时，生成的TextId有效期为7天，且在成功创建一次复刻任务后失效。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTrainingText"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTrainingTextResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetVRSVoiceTypeInfo(
            self,
            request: models.GetVRSVoiceTypeInfoRequest,
            opts: Dict = None,
    ) -> models.GetVRSVoiceTypeInfoResponse:
        """
        该接口用于查询复刻音色详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetVRSVoiceTypeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetVRSVoiceTypeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetVRSVoiceTypes(
            self,
            request: models.GetVRSVoiceTypesRequest,
            opts: Dict = None,
    ) -> models.GetVRSVoiceTypesResponse:
        """
        查询复刻音色
        """
        
        kwargs = {}
        kwargs["action"] = "GetVRSVoiceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetVRSVoiceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)