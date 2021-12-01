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
from tencentcloud.ivld.v20210903 import models


class IvldClient(AbstractClient):
    _apiVersion = '2021-09-03'
    _endpoint = 'ivld.tencentcloudapi.com'
    _service = 'ivld'


    def CreateTask(self, request):
        """创建智能标签任务。

        请注意，本接口为异步接口，**返回TaskId只代表任务创建成功，不代表任务执行成功**。

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskResponse()
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


    def DeleteMedia(self, request):
        """将MediaId对应的媒资文件从系统中删除。

        **请注意，本接口仅删除媒资文件，媒资文件对应的视频分析结果不会被删除**。如您需要删除结构化分析结果，请调用DeleteTask接口。

        :param request: Request instance for DeleteMedia.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DeleteMediaRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DeleteMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMediaResponse()
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


    def DescribeMedia(self, request):
        """描述媒资文件信息，包括媒资状态，分辨率，帧率等。

        如果媒资文件未完成导入，本接口将仅输出媒资文件的状态信息；导入完成后，本接口还将输出媒资文件的其他元信息。

        :param request: Request instance for DescribeMedia.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeMediaRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaResponse()
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


    def DescribeMedias(self, request):
        """依照输入条件，描述命中的媒资文件信息，包括媒资状态，分辨率，帧率等。

        请注意，本接口最多支持同时描述**50**个媒资文件

        如果媒资文件未完成导入，本接口将仅输出媒资文件的状态信息；导入完成后，本接口还将输出媒资文件的其他元信息。

        :param request: Request instance for DescribeMedias.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeMediasRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeMediasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMedias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediasResponse()
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


    def DescribeTask(self, request):
        """描述智能标签任务进度。

        请注意，**此接口仅返回任务执行状态信息，不返回任务执行结果**


        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResponse()
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
        """描述任务信息，如果任务成功完成，还将返回任务结果

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskDetailResponse`

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
        """依照输入条件，描述命中的任务信息，包括任务创建时间，处理时间信息等。

        请注意，本接口最多支持同时描述**50**个任务信息

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeTasksResponse`

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


    def ImportMedia(self, request):
        """将URL指向的媒资视频文件导入系统之中。

        **请注意，本接口为异步接口**。接口返回MediaId仅代表导入视频任务发起，不代表任务完成，您可调用读接口(DescribeMedia/DescribeMedias)接口查询MediaId对应的媒资文件的状态。

        当前URL只支持COS地址，其形式为`https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${ObjectKey}`，其中`${Bucket}`为您的COS桶名称，Region为COS桶所在[可用区](https://cloud.tencent.com/document/product/213/6091)，`${ObjectKey}`为指向存储在COS桶内的待分析的视频的[ObjectKey](https://cloud.tencent.com/document/product/436/13324)

        分析完成后，本产品将在您的`${Bucket}`桶内创建名为`${ObjectKey}-${task-start-time}`的目录(`task-start-time`形式为1970-01-01T08:08:08)并将分析结果将回传回该目录，也即，结构化分析结果(包括图片，JSON等数据)将会写回`https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${ObjectKey}-${task-start-time}`目录

        :param request: Request instance for ImportMedia.
        :type request: :class:`tencentcloud.ivld.v20210903.models.ImportMediaRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.ImportMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportMediaResponse()
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