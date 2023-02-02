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
from tencentcloud.vm.v20210922 import models


class VmClient(AbstractClient):
    _apiVersion = '2021-09-22'
    _endpoint = 'vm.tencentcloudapi.com'
    _service = 'vm'


    def CancelTask(self, request):
        """取消任务

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.vm.v20210922.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.vm.v20210922.models.CancelTaskResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVideoModerationTask(self, request):
        """通过URL或存储桶创建审核任务。

        ### 直播断流处理说明：
        - 请确认已对接[取消任务](https://cloud.tencent.com/document/product/1265/80018)。
        - 如果直播任务取消/结束，则终止直播拉流并退出审核。
        - 如果直播任务没有取消/结束，直播视频推流因故中断，产品将在将在10分钟内持续拉流重试。如果10分钟检测到图片截帧/音频切片数据，则恢复正常审核，反之，则终止拉流并退出审核。在拉流终止后，用户如有审核需求，需重新送审。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for CreateVideoModerationTask.
        :type request: :class:`tencentcloud.vm.v20210922.models.CreateVideoModerationTaskRequest`
        :rtype: :class:`tencentcloud.vm.v20210922.models.CreateVideoModerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoModerationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoModerationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskDetail(self, request):
        """查看任务详情DescribeTaskDetail

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.vm.v20210922.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.vm.v20210922.models.DescribeTaskDetailResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasks(self, request):
        """通过查看审核任务列表接口，可查询任务队列；您可根据多种业务信息（业务类型、审核结果、任务状态等）筛选审核任务列表。<br>

        默认接口请求频率限制：**20次/秒**。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.vm.v20210922.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.vm.v20210922.models.DescribeTasksResponse`

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
                raise TencentCloudSDKException(e.message, e.message)