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
from tencentcloud.wedata.v20210820 import models


class WedataClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'wedata.tencentcloudapi.com'
    _service = 'wedata'


    def DescribeProject(self, request):
        """获取项目信息

        :param request: Request instance for DescribeProject.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectResponse()
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


    def DescribeRelatedInstances(self, request):
        """查询任务实例的关联实例列表

        :param request: Request instance for DescribeRelatedInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRelatedInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRelatedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelatedInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRelatedInstancesResponse()
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


    def DescribeTaskInstances(self, request):
        """查询任务实例列表

        :param request: Request instance for DescribeTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskInstancesResponse()
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