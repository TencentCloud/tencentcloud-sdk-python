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
from tencentcloud.bda.v20200324 import models


class BdaClient(AbstractClient):
    _apiVersion = '2020-03-24'
    _endpoint = 'bda.tencentcloudapi.com'
    _service = 'bda'


    def CreateSegmentationTask(self, request):
        r"""本接口为人像分割在线处理接口组中的提交任务接口，可以对提交的资源进行处理视频流/图片流识别视频作品中的人像区域，进行一键抠像、背景替换、人像虚化等后期处理。

        :param request: Request instance for CreateSegmentationTask.
        :type request: :class:`tencentcloud.bda.v20200324.models.CreateSegmentationTaskRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.CreateSegmentationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSegmentationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSegmentationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSegmentationTask(self, request):
        r"""可以查看单条任务的处理情况，包括处理状态，处理结果。

        :param request: Request instance for DescribeSegmentationTask.
        :type request: :class:`tencentcloud.bda.v20200324.models.DescribeSegmentationTaskRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.DescribeSegmentationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSegmentationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSegmentationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SegmentCustomizedPortraitPic(self, request):
        r"""在前后景分割的基础上优化多分类分割，支持对头发、五官等的分割，既作为换发型、挂件等底层技术，也可用于抠人头、抠人脸等玩法

        :param request: Request instance for SegmentCustomizedPortraitPic.
        :type request: :class:`tencentcloud.bda.v20200324.models.SegmentCustomizedPortraitPicRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.SegmentCustomizedPortraitPicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SegmentCustomizedPortraitPic", params, headers=headers)
            response = json.loads(body)
            model = models.SegmentCustomizedPortraitPicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SegmentPortraitPic(self, request):
        r"""即二分类人像分割，识别传入图片中人体的完整轮廓，进行抠像。

        :param request: Request instance for SegmentPortraitPic.
        :type request: :class:`tencentcloud.bda.v20200324.models.SegmentPortraitPicRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.SegmentPortraitPicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SegmentPortraitPic", params, headers=headers)
            response = json.loads(body)
            model = models.SegmentPortraitPicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateSegmentationTask(self, request):
        r"""终止指定视频人像分割处理任务

        :param request: Request instance for TerminateSegmentationTask.
        :type request: :class:`tencentcloud.bda.v20200324.models.TerminateSegmentationTaskRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.TerminateSegmentationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateSegmentationTask", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateSegmentationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))