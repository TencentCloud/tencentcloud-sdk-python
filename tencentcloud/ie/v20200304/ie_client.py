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
from tencentcloud.ie.v20200304 import models


class IeClient(AbstractClient):
    _apiVersion = '2020-03-04'
    _endpoint = 'ie.tencentcloudapi.com'


    def CreateEditingTask(self, request):
        """创建编辑理解任务，可以同时选择视频标签识别、分类识别、智能拆条、智能集锦、智能封面和片头片尾识别中的一项或者多项能力。

        :param request: Request instance for CreateEditingTask.
        :type request: :class:`tencentcloud.ie.v20200304.models.CreateEditingTaskRequest`
        :rtype: :class:`tencentcloud.ie.v20200304.models.CreateEditingTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEditingTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEditingTaskResponse()
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


    def CreateMediaQualityRestorationTask(self, request):
        """创建画质重生任务，对视频进行转码、去噪、去划痕、去毛刺、超分、细节增强和色彩增强。

        :param request: Request instance for CreateMediaQualityRestorationTask.
        :type request: :class:`tencentcloud.ie.v20200304.models.CreateMediaQualityRestorationTaskRequest`
        :rtype: :class:`tencentcloud.ie.v20200304.models.CreateMediaQualityRestorationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMediaQualityRestorationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMediaQualityRestorationTaskResponse()
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


    def CreateQualityControlTask(self, request):
        """通过接口可以智能检测视频画面中抖动重影、模糊、低光照、过曝光、黑边、白边、黑屏、白屏、花屏、噪点、马赛克、二维码等在内的多个场景，还可以自动检测视频无音频异常、无声音片段。

        :param request: Request instance for CreateQualityControlTask.
        :type request: :class:`tencentcloud.ie.v20200304.models.CreateQualityControlTaskRequest`
        :rtype: :class:`tencentcloud.ie.v20200304.models.CreateQualityControlTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateQualityControlTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateQualityControlTaskResponse()
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


    def DescribeEditingTaskResult(self, request):
        """获取编辑理解任务结果。

        :param request: Request instance for DescribeEditingTaskResult.
        :type request: :class:`tencentcloud.ie.v20200304.models.DescribeEditingTaskResultRequest`
        :rtype: :class:`tencentcloud.ie.v20200304.models.DescribeEditingTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEditingTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEditingTaskResultResponse()
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


    def DescribeMediaQualityRestorationTaskRusult(self, request):
        """获取画质重生任务结果，查看结束后的文件信息

        :param request: Request instance for DescribeMediaQualityRestorationTaskRusult.
        :type request: :class:`tencentcloud.ie.v20200304.models.DescribeMediaQualityRestorationTaskRusultRequest`
        :rtype: :class:`tencentcloud.ie.v20200304.models.DescribeMediaQualityRestorationTaskRusultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaQualityRestorationTaskRusult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaQualityRestorationTaskRusultResponse()
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


    def DescribeQualityControlTaskResult(self, request):
        """获取媒体质检任务结果

        :param request: Request instance for DescribeQualityControlTaskResult.
        :type request: :class:`tencentcloud.ie.v20200304.models.DescribeQualityControlTaskResultRequest`
        :rtype: :class:`tencentcloud.ie.v20200304.models.DescribeQualityControlTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeQualityControlTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeQualityControlTaskResultResponse()
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


    def StopMediaQualityRestorationTask(self, request):
        """删除正在进行的画质重生任务

        :param request: Request instance for StopMediaQualityRestorationTask.
        :type request: :class:`tencentcloud.ie.v20200304.models.StopMediaQualityRestorationTaskRequest`
        :rtype: :class:`tencentcloud.ie.v20200304.models.StopMediaQualityRestorationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopMediaQualityRestorationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopMediaQualityRestorationTaskResponse()
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