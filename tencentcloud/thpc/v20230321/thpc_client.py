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
from tencentcloud.thpc.v20230321 import models


class ThpcClient(AbstractClient):
    _apiVersion = '2023-03-21'
    _endpoint = 'thpc.tencentcloudapi.com'
    _service = 'thpc'


    def AddClusterStorageOption(self, request):
        """本接口（AddClusterStorageOption）用于添加集群存储选项信息。

        :param request: Request instance for AddClusterStorageOption.
        :type request: :class:`tencentcloud.thpc.v20230321.models.AddClusterStorageOptionRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.AddClusterStorageOptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddClusterStorageOption", params, headers=headers)
            response = json.loads(body)
            model = models.AddClusterStorageOptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddNodes(self, request):
        """本接口(AddNodes)用于添加一个或者多个计算节点或者登录节点到指定集群。

        :param request: Request instance for AddNodes.
        :type request: :class:`tencentcloud.thpc.v20230321.models.AddNodesRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.AddNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNodes", params, headers=headers)
            response = json.loads(body)
            model = models.AddNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddQueue(self, request):
        """本接口(AddQueue)用于添加队列到指定集群。
        * 本接口为目前只支持SchedulerType为SLURM的集群。
        * 单个集群中队列数量上限为10个。

        :param request: Request instance for AddQueue.
        :type request: :class:`tencentcloud.thpc.v20230321.models.AddQueueRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.AddQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddQueue", params, headers=headers)
            response = json.loads(body)
            model = models.AddQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        """本接口 (CreateCluster) 用于创建并启动集群。

        * 本接口为异步接口， 当创建集群请求下发成功后会返回一个集群`ID`和一个`RequestId`，此时创建集群操作并未立即完成。在此期间集群的状态将会处于“PENDING”或者“INITING”，集群创建结果可以通过调用 [DescribeClusters](https://cloud.tencent.com/document/product/1527/72100)  接口查询，如果集群状态(ClusterStatus)变为“RUNNING(运行中)”，则代表集群创建成功，“ INIT_FAILED”代表集群创建失败。

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.thpc.v20230321.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.CreateClusterResponse`

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
        :type request: :class:`tencentcloud.thpc.v20230321.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DeleteClusterResponse`

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


    def DeleteClusterStorageOption(self, request):
        """本接口 (DeleteClusterStorageOption) 用于删除集群存储选项信息。

        :param request: Request instance for DeleteClusterStorageOption.
        :type request: :class:`tencentcloud.thpc.v20230321.models.DeleteClusterStorageOptionRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DeleteClusterStorageOptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterStorageOption", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterStorageOptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNodes(self, request):
        """本接口(DeleteNodes)用于删除指定集群中一个或者多个计算节点或者登录节点。

        :param request: Request instance for DeleteNodes.
        :type request: :class:`tencentcloud.thpc.v20230321.models.DeleteNodesRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DeleteNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQueue(self, request):
        """本接口(DeleteQueue)用于从指定集群删除队列。
        * 本接口为目前只支持SchedulerType为SLURM的集群。

        * 删除队列时，需要保证队列内不存在节点。

        :param request: Request instance for DeleteQueue.
        :type request: :class:`tencentcloud.thpc.v20230321.models.DeleteQueueRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DeleteQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQueue", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScalingConfiguration(self, request):
        """本接口(DescribeAutoScalingConfiguration)用于查询集群弹性伸缩配置信息。本接口仅适用于弹性伸缩类型为THPC_AS的集群。

        :param request: Request instance for DescribeAutoScalingConfiguration.
        :type request: :class:`tencentcloud.thpc.v20230321.models.DescribeAutoScalingConfigurationRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DescribeAutoScalingConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScalingConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScalingConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterActivities(self, request):
        """本接口（DescribeClusterActivities）用于查询集群活动历史记录列表。

        :param request: Request instance for DescribeClusterActivities.
        :type request: :class:`tencentcloud.thpc.v20230321.models.DescribeClusterActivitiesRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DescribeClusterActivitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterActivities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterActivitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterStorageOption(self, request):
        """本接口 (DescribeClusterStorageOption) 用于查询集群存储选项信息。

        :param request: Request instance for DescribeClusterStorageOption.
        :type request: :class:`tencentcloud.thpc.v20230321.models.DescribeClusterStorageOptionRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DescribeClusterStorageOptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterStorageOption", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterStorageOptionResponse()
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
        :type request: :class:`tencentcloud.thpc.v20230321.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DescribeClustersResponse`

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


    def DescribeInitNodeScripts(self, request):
        """本接口 (DescribeInitNodeScripts) 用于查询节点初始化脚本列表。

        :param request: Request instance for DescribeInitNodeScripts.
        :type request: :class:`tencentcloud.thpc.v20230321.models.DescribeInitNodeScriptsRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DescribeInitNodeScriptsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInitNodeScripts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInitNodeScriptsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodes(self, request):
        """本接口 (DescribeNodes) 用于查询指定集群节点概览信息列表。

        :param request: Request instance for DescribeNodes.
        :type request: :class:`tencentcloud.thpc.v20230321.models.DescribeNodesRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DescribeNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQueues(self, request):
        """本接口(DescribeQueues)用于查询指定集群队列概览信息列表。

        :param request: Request instance for DescribeQueues.
        :type request: :class:`tencentcloud.thpc.v20230321.models.DescribeQueuesRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.DescribeQueuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQueues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQueuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInitNodeScripts(self, request):
        """本接口 (ModifyInitNodeScripts) 用于修改节点初始化脚本。

        :param request: Request instance for ModifyInitNodeScripts.
        :type request: :class:`tencentcloud.thpc.v20230321.models.ModifyInitNodeScriptsRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.ModifyInitNodeScriptsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInitNodeScripts", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInitNodeScriptsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetAutoScalingConfiguration(self, request):
        """本接口(SetAutoScalingConfiguration)用于为集群设置集群弹性伸缩配置信息。

        :param request: Request instance for SetAutoScalingConfiguration.
        :type request: :class:`tencentcloud.thpc.v20230321.models.SetAutoScalingConfigurationRequest`
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SetAutoScalingConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAutoScalingConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.SetAutoScalingConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))