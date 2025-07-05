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
from tencentcloud.tiw.v20190919 import models


class TiwClient(AbstractClient):
    _apiVersion = '2019-09-19'
    _endpoint = 'tiw.tencentcloudapi.com'
    _service = 'tiw'


    def CreatePPTCheckTask(self, request):
        """检测PPT文件，识别PPT中包含的动态转码任务（Transcode）不支持的元素

        :param request: Request instance for CreatePPTCheckTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreatePPTCheckTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreatePPTCheckTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePPTCheckTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePPTCheckTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSnapshotTask(self, request):
        """创建白板板书生成任务, 在任务结束后，如果提供了回调地址，将通过回调地址通知板书生成结果

        :param request: Request instance for CreateSnapshotTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateSnapshotTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateSnapshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTranscode(self, request):
        """创建一个文档转码任务

        :param request: Request instance for CreateTranscode.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateTranscodeRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateTranscodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTranscode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTranscodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoGenerationTask(self, request):
        """创建视频生成任务

        :param request: Request instance for CreateVideoGenerationTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateVideoGenerationTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateVideoGenerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoGenerationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoGenerationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOnlineRecord(self, request):
        """查询录制任务状态与结果

        :param request: Request instance for DescribeOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOnlineRecordCallback(self, request):
        """查询实时录制回调地址

        :param request: Request instance for DescribeOnlineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOnlineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOnlineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePPTCheck(self, request):
        """查询PPT检测任务的执行进度或结果，支持查询最近半年内的任务结果

        :param request: Request instance for DescribePPTCheck.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribePPTCheckRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribePPTCheckResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePPTCheck", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePPTCheckResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePPTCheckCallback(self, request):
        """查询PPT检测任务回调地址

        :param request: Request instance for DescribePPTCheckCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribePPTCheckCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribePPTCheckCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePPTCheckCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePPTCheckCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRunningTasks(self, request):
        """根据指定的任务类型，获取当前正在执行中的任务列表。只能查询最近3天内创建的任务。

        :param request: Request instance for DescribeRunningTasks.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeRunningTasksRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeRunningTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRunningTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRunningTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotTask(self, request):
        """获取指定白板板书生成任务信息

        :param request: Request instance for DescribeSnapshotTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeSnapshotTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeSnapshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTranscode(self, request):
        """查询文档转码任务的执行进度与转码结果

        :param request: Request instance for DescribeTranscode.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTranscodeByUrl(self, request):
        """通过文档URL查询转码任务，返回最近一天内最新的转码任务状态

        :param request: Request instance for DescribeTranscodeByUrl.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeByUrlRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeByUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeByUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeByUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTranscodeCallback(self, request):
        """查询文档转码回调地址

        :param request: Request instance for DescribeTranscodeCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoGenerationTask(self, request):
        """查询录制视频生成任务状态与结果

        :param request: Request instance for DescribeVideoGenerationTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoGenerationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoGenerationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoGenerationTaskCallback(self, request):
        """查询录制视频生成回调地址

        :param request: Request instance for DescribeVideoGenerationTaskCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoGenerationTaskCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoGenerationTaskCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWarningCallback(self, request):
        """查询告警回调地址。此功能需要申请白名单使用。

        :param request: Request instance for DescribeWarningCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWarningCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWarningCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarningCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWarningCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteboardPush(self, request):
        """查询推流任务状态与结果

        :param request: Request instance for DescribeWhiteboardPush.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardPush", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardPushResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteboardPushCallback(self, request):
        """查询白板推流回调地址

        :param request: Request instance for DescribeWhiteboardPushCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardPushCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardPushCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseOnlineRecord(self, request):
        """暂停实时录制

        :param request: Request instance for PauseOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.PauseOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.PauseOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.PauseOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeOnlineRecord(self, request):
        """恢复实时录制

        :param request: Request instance for ResumeOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ResumeOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ResumeOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetOnlineRecordCallback(self, request):
        """设置实时录制回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40258

        :param request: Request instance for SetOnlineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOnlineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetOnlineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetOnlineRecordCallbackKey(self, request):
        """设置实时录制回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257

        :param request: Request instance for SetOnlineRecordCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOnlineRecordCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetOnlineRecordCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetPPTCheckCallback(self, request):
        """设置PPT检测任务回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260#c9cbe05f-fe1a-4410-b4dc-40cc301c7b81

        :param request: Request instance for SetPPTCheckCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetPPTCheckCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetPPTCheckCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetPPTCheckCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetPPTCheckCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetPPTCheckCallbackKey(self, request):
        """设置PPT检测任务回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257

        :param request: Request instance for SetPPTCheckCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetPPTCheckCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetPPTCheckCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetPPTCheckCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetPPTCheckCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTranscodeCallback(self, request):
        """设置文档转码回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260

        :param request: Request instance for SetTranscodeCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTranscodeCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetTranscodeCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTranscodeCallbackKey(self, request):
        """设置文档转码回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257

        :param request: Request instance for SetTranscodeCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTranscodeCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetTranscodeCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetVideoGenerationTaskCallback(self, request):
        """设置录制视频生成回调地址

        :param request: Request instance for SetVideoGenerationTaskCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVideoGenerationTaskCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetVideoGenerationTaskCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetVideoGenerationTaskCallbackKey(self, request):
        """设置视频生成回调鉴权密钥

        :param request: Request instance for SetVideoGenerationTaskCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVideoGenerationTaskCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetVideoGenerationTaskCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetWarningCallback(self, request):
        """设置告警回调地址。此功能需要申请白名单使用。

        :param request: Request instance for SetWarningCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetWarningCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetWarningCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetWarningCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetWarningCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetWhiteboardPushCallback(self, request):
        """设置白板推流回调地址，回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40257

        :param request: Request instance for SetWhiteboardPushCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetWhiteboardPushCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetWhiteboardPushCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetWhiteboardPushCallbackKey(self, request):
        """设置白板推流回调鉴权密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257

        :param request: Request instance for SetWhiteboardPushCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetWhiteboardPushCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetWhiteboardPushCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartOnlineRecord(self, request):
        """发起一个实时录制任务

        :param request: Request instance for StartOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StartOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StartOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StartOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartWhiteboardPush(self, request):
        """发起一个白板推流任务

        :param request: Request instance for StartWhiteboardPush.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StartWhiteboardPushRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StartWhiteboardPushResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartWhiteboardPush", params, headers=headers)
            response = json.loads(body)
            model = models.StartWhiteboardPushResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopOnlineRecord(self, request):
        """停止实时录制

        :param request: Request instance for StopOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StopOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StopOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StopOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopWhiteboardPush(self, request):
        """停止白板推流任务

        :param request: Request instance for StopWhiteboardPush.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StopWhiteboardPushRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StopWhiteboardPushResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopWhiteboardPush", params, headers=headers)
            response = json.loads(body)
            model = models.StopWhiteboardPushResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))