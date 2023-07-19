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
from tencentcloud.vm.v20200709 import models


class VmClient(AbstractClient):
    _apiVersion = '2020-07-09'
    _endpoint = 'vm.tencentcloudapi.com'
    _service = 'vm'


    def CancelTask(self, request):
        """取消任务

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.vm.v20200709.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.vm.v20200709.models.CancelTaskResponse`

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


    def CreateBizConfig(self, request):
        """创建业务配置，1个账号最多可以创建20个配置，可定义音频审核的场景，如色情、谩骂等，

        在创建业务配置之前，你需要以下步骤：
        1. 开通COS存储捅功能，新建存储桶，例如 cms_segments，用来存储 视频转换过程中生成对音频和图片。
        2. 然后在COS控制台，授权天御内容安全主账号 对 cms_segments 存储桶对读写权限。具体授权操作，参考https://cloud.tencent.com/document/product/436/38648

        :param request: Request instance for CreateBizConfig.
        :type request: :class:`tencentcloud.vm.v20200709.models.CreateBizConfigRequest`
        :rtype: :class:`tencentcloud.vm.v20200709.models.CreateBizConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBizConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBizConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoModerationTask(self, request):
        """通过URL或存储桶创建审核任务

        :param request: Request instance for CreateVideoModerationTask.
        :type request: :class:`tencentcloud.vm.v20200709.models.CreateVideoModerationTaskRequest`
        :rtype: :class:`tencentcloud.vm.v20200709.models.CreateVideoModerationTaskResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskDetail(self, request):
        """查看任务详情DescribeTaskDetail

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.vm.v20200709.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.vm.v20200709.models.DescribeTaskDetailResponse`

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


    def DescribeVideoStat(self, request):
        """控制台识别统计

        :param request: Request instance for DescribeVideoStat.
        :type request: :class:`tencentcloud.vm.v20200709.models.DescribeVideoStatRequest`
        :rtype: :class:`tencentcloud.vm.v20200709.models.DescribeVideoStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))