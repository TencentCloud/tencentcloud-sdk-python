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
from tencentcloud.thpc.v20220401 import models


class ThpcClient(AbstractClient):
    _apiVersion = '2022-04-01'
    _endpoint = 'thpc.tencentcloudapi.com'
    _service = 'thpc'


    def AddNodes(self, request):
        """本接口(AddNodes)用于添加一个或者多个计算节点或者登录节点到指定集群。

        :param request: Request instance for AddNodes.
        :type request: :class:`tencentcloud.thpc.v20220401.models.AddNodesRequest`
        :rtype: :class:`tencentcloud.thpc.v20220401.models.AddNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNodes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddNodesResponse()
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


    def BindAutoScalingGroup(self, request):
        """本接口(BindAutoScalingGroup)用于为集群队列绑定弹性伸缩组

        :param request: Request instance for BindAutoScalingGroup.
        :type request: :class:`tencentcloud.thpc.v20220401.models.BindAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.thpc.v20220401.models.BindAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindAutoScalingGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindAutoScalingGroupResponse()
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


    def CreateCluster(self, request):
        """本接口 (CreateCluster) 用于创建并启动集群。

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.thpc.v20220401.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.thpc.v20220401.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
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
        :type request: :class:`tencentcloud.thpc.v20220401.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.thpc.v20220401.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCluster", params, headers=headers)
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


    def DeleteNodes(self, request):
        """本接口(DeleteNodes)用于删除指定集群中一个或者多个计算节点或者登录节点。

        :param request: Request instance for DeleteNodes.
        :type request: :class:`tencentcloud.thpc.v20220401.models.DeleteNodesRequest`
        :rtype: :class:`tencentcloud.thpc.v20220401.models.DeleteNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNodes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNodesResponse()
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


    def DescribeClusters(self, request):
        """本接口（DescribeClusters）用于查询集群列表。

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.thpc.v20220401.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.thpc.v20220401.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClustersResponse()
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