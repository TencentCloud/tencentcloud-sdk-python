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
from tencentcloud.tiw.v20190919 import models
from typing import Dict


class TiwClient(AbstractClient):
    _apiVersion = '2019-09-19'
    _endpoint = 'tiw.tencentcloudapi.com'
    _service = 'tiw'

    async def CreatePPTCheckTask(
            self,
            request: models.CreatePPTCheckTaskRequest,
            opts: Dict = None,
    ) -> models.CreatePPTCheckTaskResponse:
        """
        检测PPT文件，识别PPT中包含的动态转码任务（Transcode）不支持的元素
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePPTCheckTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePPTCheckTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshotTask(
            self,
            request: models.CreateSnapshotTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotTaskResponse:
        """
        创建白板板书生成任务, 在任务结束后，如果提供了回调地址，将通过回调地址通知板书生成结果
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshotTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTranscode(
            self,
            request: models.CreateTranscodeRequest,
            opts: Dict = None,
    ) -> models.CreateTranscodeResponse:
        """
        创建一个文档转码任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTranscode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTranscodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoGenerationTask(
            self,
            request: models.CreateVideoGenerationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVideoGenerationTaskResponse:
        """
        创建视频生成任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoGenerationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoGenerationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOnlineRecord(
            self,
            request: models.DescribeOnlineRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeOnlineRecordResponse:
        """
        查询录制任务状态与结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOnlineRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOnlineRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOnlineRecordCallback(
            self,
            request: models.DescribeOnlineRecordCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribeOnlineRecordCallbackResponse:
        """
        查询实时录制回调地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOnlineRecordCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOnlineRecordCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePPTCheck(
            self,
            request: models.DescribePPTCheckRequest,
            opts: Dict = None,
    ) -> models.DescribePPTCheckResponse:
        """
        查询PPT检测任务的执行进度或结果，支持查询最近半年内的任务结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePPTCheck"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePPTCheckResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePPTCheckCallback(
            self,
            request: models.DescribePPTCheckCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribePPTCheckCallbackResponse:
        """
        查询PPT检测任务回调地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePPTCheckCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePPTCheckCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRunningTasks(
            self,
            request: models.DescribeRunningTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeRunningTasksResponse:
        """
        根据指定的任务类型，获取当前正在执行中的任务列表。只能查询最近3天内创建的任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRunningTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRunningTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotTask(
            self,
            request: models.DescribeSnapshotTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotTaskResponse:
        """
        获取指定白板板书生成任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTranscode(
            self,
            request: models.DescribeTranscodeRequest,
            opts: Dict = None,
    ) -> models.DescribeTranscodeResponse:
        """
        查询文档转码任务的执行进度与转码结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTranscode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTranscodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTranscodeByUrl(
            self,
            request: models.DescribeTranscodeByUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeTranscodeByUrlResponse:
        """
        通过文档URL查询转码任务，返回最近一天内最新的转码任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTranscodeByUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTranscodeByUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTranscodeCallback(
            self,
            request: models.DescribeTranscodeCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribeTranscodeCallbackResponse:
        """
        查询文档转码回调地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTranscodeCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTranscodeCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoGenerationTask(
            self,
            request: models.DescribeVideoGenerationTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoGenerationTaskResponse:
        """
        查询录制视频生成任务状态与结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoGenerationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoGenerationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoGenerationTaskCallback(
            self,
            request: models.DescribeVideoGenerationTaskCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoGenerationTaskCallbackResponse:
        """
        查询录制视频生成回调地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoGenerationTaskCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoGenerationTaskCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWarningCallback(
            self,
            request: models.DescribeWarningCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribeWarningCallbackResponse:
        """
        查询告警回调地址。此功能需要申请白名单使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWarningCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWarningCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteboardPush(
            self,
            request: models.DescribeWhiteboardPushRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteboardPushResponse:
        """
        查询推流任务状态与结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteboardPush"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteboardPushResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteboardPushCallback(
            self,
            request: models.DescribeWhiteboardPushCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteboardPushCallbackResponse:
        """
        查询白板推流回调地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteboardPushCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteboardPushCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseOnlineRecord(
            self,
            request: models.PauseOnlineRecordRequest,
            opts: Dict = None,
    ) -> models.PauseOnlineRecordResponse:
        """
        暂停实时录制
        """
        
        kwargs = {}
        kwargs["action"] = "PauseOnlineRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseOnlineRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeOnlineRecord(
            self,
            request: models.ResumeOnlineRecordRequest,
            opts: Dict = None,
    ) -> models.ResumeOnlineRecordResponse:
        """
        恢复实时录制
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeOnlineRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeOnlineRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetOnlineRecordCallback(
            self,
            request: models.SetOnlineRecordCallbackRequest,
            opts: Dict = None,
    ) -> models.SetOnlineRecordCallbackResponse:
        """
        设置实时录制回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40258
        """
        
        kwargs = {}
        kwargs["action"] = "SetOnlineRecordCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetOnlineRecordCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetOnlineRecordCallbackKey(
            self,
            request: models.SetOnlineRecordCallbackKeyRequest,
            opts: Dict = None,
    ) -> models.SetOnlineRecordCallbackKeyResponse:
        """
        设置实时录制回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        """
        
        kwargs = {}
        kwargs["action"] = "SetOnlineRecordCallbackKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetOnlineRecordCallbackKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetPPTCheckCallback(
            self,
            request: models.SetPPTCheckCallbackRequest,
            opts: Dict = None,
    ) -> models.SetPPTCheckCallbackResponse:
        """
        设置PPT检测任务回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260#c9cbe05f-fe1a-4410-b4dc-40cc301c7b81
        """
        
        kwargs = {}
        kwargs["action"] = "SetPPTCheckCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetPPTCheckCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetPPTCheckCallbackKey(
            self,
            request: models.SetPPTCheckCallbackKeyRequest,
            opts: Dict = None,
    ) -> models.SetPPTCheckCallbackKeyResponse:
        """
        设置PPT检测任务回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        """
        
        kwargs = {}
        kwargs["action"] = "SetPPTCheckCallbackKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetPPTCheckCallbackKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTranscodeCallback(
            self,
            request: models.SetTranscodeCallbackRequest,
            opts: Dict = None,
    ) -> models.SetTranscodeCallbackResponse:
        """
        设置文档转码回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260
        """
        
        kwargs = {}
        kwargs["action"] = "SetTranscodeCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTranscodeCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTranscodeCallbackKey(
            self,
            request: models.SetTranscodeCallbackKeyRequest,
            opts: Dict = None,
    ) -> models.SetTranscodeCallbackKeyResponse:
        """
        设置文档转码回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        """
        
        kwargs = {}
        kwargs["action"] = "SetTranscodeCallbackKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTranscodeCallbackKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetVideoGenerationTaskCallback(
            self,
            request: models.SetVideoGenerationTaskCallbackRequest,
            opts: Dict = None,
    ) -> models.SetVideoGenerationTaskCallbackResponse:
        """
        设置录制视频生成回调地址
        """
        
        kwargs = {}
        kwargs["action"] = "SetVideoGenerationTaskCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetVideoGenerationTaskCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetVideoGenerationTaskCallbackKey(
            self,
            request: models.SetVideoGenerationTaskCallbackKeyRequest,
            opts: Dict = None,
    ) -> models.SetVideoGenerationTaskCallbackKeyResponse:
        """
        设置视频生成回调鉴权密钥
        """
        
        kwargs = {}
        kwargs["action"] = "SetVideoGenerationTaskCallbackKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetVideoGenerationTaskCallbackKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetWarningCallback(
            self,
            request: models.SetWarningCallbackRequest,
            opts: Dict = None,
    ) -> models.SetWarningCallbackResponse:
        """
        设置告警回调地址。此功能需要申请白名单使用。
        """
        
        kwargs = {}
        kwargs["action"] = "SetWarningCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetWarningCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetWhiteboardPushCallback(
            self,
            request: models.SetWhiteboardPushCallbackRequest,
            opts: Dict = None,
    ) -> models.SetWhiteboardPushCallbackResponse:
        """
        设置白板推流回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        """
        
        kwargs = {}
        kwargs["action"] = "SetWhiteboardPushCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetWhiteboardPushCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetWhiteboardPushCallbackKey(
            self,
            request: models.SetWhiteboardPushCallbackKeyRequest,
            opts: Dict = None,
    ) -> models.SetWhiteboardPushCallbackKeyResponse:
        """
        设置白板推流回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        """
        
        kwargs = {}
        kwargs["action"] = "SetWhiteboardPushCallbackKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetWhiteboardPushCallbackKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartOnlineRecord(
            self,
            request: models.StartOnlineRecordRequest,
            opts: Dict = None,
    ) -> models.StartOnlineRecordResponse:
        """
        发起一个实时录制任务
        """
        
        kwargs = {}
        kwargs["action"] = "StartOnlineRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartOnlineRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartWhiteboardPush(
            self,
            request: models.StartWhiteboardPushRequest,
            opts: Dict = None,
    ) -> models.StartWhiteboardPushResponse:
        """
        发起一个白板推流任务
        """
        
        kwargs = {}
        kwargs["action"] = "StartWhiteboardPush"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartWhiteboardPushResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopOnlineRecord(
            self,
            request: models.StopOnlineRecordRequest,
            opts: Dict = None,
    ) -> models.StopOnlineRecordResponse:
        """
        停止实时录制
        """
        
        kwargs = {}
        kwargs["action"] = "StopOnlineRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopOnlineRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopWhiteboardPush(
            self,
            request: models.StopWhiteboardPushRequest,
            opts: Dict = None,
    ) -> models.StopWhiteboardPushResponse:
        """
        停止白板推流任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopWhiteboardPush"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopWhiteboardPushResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)