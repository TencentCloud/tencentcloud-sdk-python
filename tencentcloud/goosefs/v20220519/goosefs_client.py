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
from tencentcloud.goosefs.v20220519 import models


class GoosefsClient(AbstractClient):
    _apiVersion = '2022-05-19'
    _endpoint = 'goosefs.tencentcloudapi.com'
    _service = 'goosefs'


    def AddCrossVpcSubnetSupportForClientNode(self, request):
        r"""为客户端节点添加跨vpc或子网访问能力

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
        r"""为文件系统关联Bucket

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
        r"""批量添加客户端节点

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
        r"""批量删除客户端节点

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


    def BuildClientNodeMountCommand(self, request):
        r"""生成客户端的挂载命令

        :param request: Request instance for BuildClientNodeMountCommand.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.BuildClientNodeMountCommandRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.BuildClientNodeMountCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BuildClientNodeMountCommand", params, headers=headers)
            response = json.loads(body)
            model = models.BuildClientNodeMountCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelLoadTask(self, request):
        r"""取消单个预热任务，仅任务在 waiting、running 状态时可以调用此接口。注意，该接口需要 GooseFS 集群版本 ≥ 1.5.1。

        :param request: Request instance for CancelLoadTask.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.CancelLoadTaskRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.CancelLoadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelLoadTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelLoadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataRepositoryTask(self, request):
        r"""创建数据流通任务,包括从将文件系统的数据上传到存储桶下, 以及从存储桶下载到文件系统里。

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
        r"""创建文件系统

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


    def CreateFileset(self, request):
        r"""创建Fileset

        :param request: Request instance for CreateFileset.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.CreateFilesetRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.CreateFilesetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileset", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFilesetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoadTask(self, request):
        r"""GooseFS 预热相关接口，用于下发，列出，查询，修改预热任务。用于元数据预热、数据预热场景。 注意，该接口需要 GooseFS 集群版本 ≥ 1.5.1。

        :param request: Request instance for CreateLoadTask.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.CreateLoadTaskRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.CreateLoadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCrossVpcSubnetSupportForClientNode(self, request):
        r"""为客户端节点删除跨vpc子网访问能力

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
        r"""删除文件系统

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


    def DeleteFileset(self, request):
        r"""删除Fileset

        :param request: Request instance for DeleteFileset.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DeleteFilesetRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DeleteFilesetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFileset", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFilesetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientNodes(self, request):
        r"""列出集群中所有的客户端节点

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
        r"""查询GooseFS集群客户端凭证

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
        r"""查询GooseFS集群角色凭证

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


    def DescribeDataRepositoryTaskStatus(self, request):
        r"""获取数据流通任务实时状态，用作客户端控制

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
        r"""罗列文件系统关联的Bucket映射

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
        r"""列出所有的文件系统

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


    def DescribeFilesetGeneralConfig(self, request):
        r"""查询Fileset通用配置

        :param request: Request instance for DescribeFilesetGeneralConfig.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeFilesetGeneralConfigRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeFilesetGeneralConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFilesetGeneralConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFilesetGeneralConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFilesets(self, request):
        r"""查询Fileset列表

        :param request: Request instance for DescribeFilesets.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeFilesetsRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeFilesetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFilesets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFilesetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadTask(self, request):
        r"""查询单个预热任务执行情况。注意，该接口需要 GooseFS 集群版本 ≥ 1.5.1。

        :param request: Request instance for DescribeLoadTask.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.DescribeLoadTaskRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.DescribeLoadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachFileSystemBucket(self, request):
        r"""解绑文件系统与Bucket的映射

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
        r"""扩展文件系统容量

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


    def ListLoadTasks(self, request):
        r"""列出该集群下所有预热任务。注意，该接口需要 GooseFS 集群版本 ≥ 1.5.1。

        :param request: Request instance for ListLoadTasks.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.ListLoadTasksRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.ListLoadTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLoadTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListLoadTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataRepositoryBandwidth(self, request):
        r"""修改数据流动带宽

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
        r"""查询客户端节点跨vpc子网访问能力

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
        r"""查询数据流动带宽

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


    def UpdateFileset(self, request):
        r"""修改FIleset

        :param request: Request instance for UpdateFileset.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.UpdateFilesetRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.UpdateFilesetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFileset", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFilesetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFilesetGeneralConfig(self, request):
        r"""修改Fileset通用配置

        :param request: Request instance for UpdateFilesetGeneralConfig.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.UpdateFilesetGeneralConfigRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.UpdateFilesetGeneralConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFilesetGeneralConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFilesetGeneralConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateLoadTaskPriority(self, request):
        r"""变更已有 GooseFS 预热任务配置，仅任务状态为 waiting 时可调用该接口。注意，该接口需要 GooseFS 集群版本 ≥ 1.5.1。

        :param request: Request instance for UpdateLoadTaskPriority.
        :type request: :class:`tencentcloud.goosefs.v20220519.models.UpdateLoadTaskPriorityRequest`
        :rtype: :class:`tencentcloud.goosefs.v20220519.models.UpdateLoadTaskPriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateLoadTaskPriority", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateLoadTaskPriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))