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
from tencentcloud.thpc.v20211109 import models


class ThpcClient(AbstractClient):
    _apiVersion = '2021-11-09'
    _endpoint = 'thpc.tencentcloudapi.com'
    _service = 'thpc'


    def CreateCluster(self, request):
        """本接口 (CreateCluster) 用于创建并启动集群。

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.thpc.v20211109.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.thpc.v20211109.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterResponse()
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


    def DeleteCluster(self, request):
        """本接口（DeleteCluster）用于删除一个指定的集群。

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.thpc.v20211109.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.thpc.v20211109.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterResponse()
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