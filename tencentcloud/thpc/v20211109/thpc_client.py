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


    def BindAutoScalingGroup(self, request):
        """本接口(BindAutoScalingGroup)用于为集群队列绑定弹性伸缩组

        :param request: Request instance for BindAutoScalingGroup.
        :type request: :class:`tencentcloud.thpc.v20211109.models.BindAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.thpc.v20211109.models.BindAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindAutoScalingGroup", params, headers=headers)
            response = json.loads(body)
            model = models.BindAutoScalingGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        """本接口 (CreateCluster) 用于创建并启动集群。

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.thpc.v20211109.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.thpc.v20211109.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCluster(self, request):
        """本接口（DeleteCluster）用于删除一个指定的集群。

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.thpc.v20211109.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.thpc.v20211109.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusters(self, request):
        """本接口（DescribeClusters）用于查询集群列表。

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.thpc.v20211109.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.thpc.v20211109.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))