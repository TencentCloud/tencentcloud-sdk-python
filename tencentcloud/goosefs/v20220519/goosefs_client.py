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
from tencentcloud.goosefs.v20220519 import models


class GoosefsClient(AbstractClient):
    _apiVersion = '2022-05-19'
    _endpoint = 'goosefs.tencentcloudapi.com'
    _service = 'goosefs'


    def AddCrossVpcSubnetSupportForClientNode(self, request):
        """为客户端节点添加跨vpc或子网访问能力

        :param request: Request instance for AddCrossVpcSubnetSupportForClientNode.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.AddCrossVpcSubnetSupportForClientNodeRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.AddCrossVpcSubnetSupportForClientNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCrossVpcSubnetSupportForClientNode", params, headers=headers)
            response = json.loads(body)
            model = models.AddCrossVpcSubnetSupportForClientNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachFileSystemBucket(self, request):
        """为文件系统关联Bucket

        :param request: Request instance for AttachFileSystemBucket.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.AttachFileSystemBucketRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.AttachFileSystemBucketResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachFileSystemBucket", params, headers=headers)
            response = json.loads(body)
            model = models.AttachFileSystemBucketResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchAddClientNodes(self, request):
        """批量添加客户端节点

        :param request: Request instance for BatchAddClientNodes.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.BatchAddClientNodesRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.BatchAddClientNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchAddClientNodes", params, headers=headers)
            response = json.loads(body)
            model = models.BatchAddClientNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteClientNodes(self, request):
        """批量删除客户端节点

        :param request: Request instance for BatchDeleteClientNodes.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.BatchDeleteClientNodesRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.BatchDeleteClientNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteClientNodes", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteClientNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataRepositoryTask(self, request):
        """创建数据流通任务,包括从将文件系统的数据上传到存储桶下, 以及从存储桶下载到文件系统里。

        :param request: Request instance for CreateDataRepositoryTask.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.CreateDataRepositoryTaskRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.CreateDataRepositoryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataRepositoryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataRepositoryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFileSystem(self, request):
        """创建文件系统

        :param request: Request instance for CreateFileSystem.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.CreateFileSystemRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.CreateFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCrossVpcSubnetSupportForClientNode(self, request):
        """为客户端节点删除跨vpc子网访问能力

        :param request: Request instance for DeleteCrossVpcSubnetSupportForClientNode.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DeleteCrossVpcSubnetSupportForClientNodeRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DeleteCrossVpcSubnetSupportForClientNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCrossVpcSubnetSupportForClientNode", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCrossVpcSubnetSupportForClientNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFileSystem(self, request):
        """删除文件系统

        :param request: Request instance for DeleteFileSystem.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DeleteFileSystemRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DeleteFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientNodes(self, request):
        """列出集群中所有的客户端节点

        :param request: Request instance for DescribeClientNodes.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeClientNodesRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeClientNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterClientToken(self, request):
        """查询GooseFS集群客户端凭证

        :param request: Request instance for DescribeClusterClientToken.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterClientTokenRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterClientTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterClientToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterClientTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterRoleToken(self, request):
        """查询GooseFS集群角色凭证

        :param request: Request instance for DescribeClusterRoleToken.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterRoleTokenRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterRoleTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterRoleToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterRoleTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterRoles(self, request):
        """查询GooseFS集群角色

        :param request: Request instance for DescribeClusterRoles.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterRolesRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeClusterRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataRepositoryTaskStatus(self, request):
        """获取数据流通任务实时状态，用作客户端控制

        :param request: Request instance for DescribeDataRepositoryTaskStatus.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeDataRepositoryTaskStatusRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeDataRepositoryTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataRepositoryTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataRepositoryTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileSystemBuckets(self, request):
        """罗列文件系统关联的Bucket映射

        :param request: Request instance for DescribeFileSystemBuckets.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeFileSystemBucketsRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeFileSystemBucketsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileSystemBuckets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileSystemBucketsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileSystems(self, request):
        """列出所有的文件系统

        :param request: Request instance for DescribeFileSystems.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeFileSystemsRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeFileSystemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileSystems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileSystemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachFileSystemBucket(self, request):
        """解绑文件系统与Bucket的映射

        :param request: Request instance for DetachFileSystemBucket.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DetachFileSystemBucketRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DetachFileSystemBucketResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachFileSystemBucket", params, headers=headers)
            response = json.loads(body)
            model = models.DetachFileSystemBucketResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExpandCapacity(self, request):
        """扩展文件系统容量

        :param request: Request instance for ExpandCapacity.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.ExpandCapacityRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.ExpandCapacityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExpandCapacity", params, headers=headers)
            response = json.loads(body)
            model = models.ExpandCapacityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataRepositoryBandwidth(self, request):
        """修改数据流动带宽

        :param request: Request instance for ModifyDataRepositoryBandwidth.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.ModifyDataRepositoryBandwidthRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.ModifyDataRepositoryBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataRepositoryBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataRepositoryBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCrossVpcSubnetSupportForClientNode(self, request):
        """查询客户端节点跨vpc子网访问能力

        :param request: Request instance for QueryCrossVpcSubnetSupportForClientNode.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.QueryCrossVpcSubnetSupportForClientNodeRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.QueryCrossVpcSubnetSupportForClientNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCrossVpcSubnetSupportForClientNode", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCrossVpcSubnetSupportForClientNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryDataRepositoryBandwidth(self, request):
        """查询数据流动带宽

        :param request: Request instance for QueryDataRepositoryBandwidth.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.QueryDataRepositoryBandwidthRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.QueryDataRepositoryBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDataRepositoryBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.QueryDataRepositoryBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))