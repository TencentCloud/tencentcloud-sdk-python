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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.goosefs.v20220519 import models
from typing import Dict


class GoosefsClient(AbstractClient):
    _apiVersion = '2022-05-19'
    _endpoint = 'goosefs.tencentcloudapi.com'
    _service = 'goosefs'

    async def AddCrossVpcSubnetSupportForClientNode(
            self,
            request: models.AddCrossVpcSubnetSupportForClientNodeRequest,
            opts: Dict = None,
    ) -> models.AddCrossVpcSubnetSupportForClientNodeResponse:
        """
        为客户端节点添加跨vpc或子网访问能力
        """
        
        kwargs = {}
        kwargs["action"] = "AddCrossVpcSubnetSupportForClientNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCrossVpcSubnetSupportForClientNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachFileSystemBucket(
            self,
            request: models.AttachFileSystemBucketRequest,
            opts: Dict = None,
    ) -> models.AttachFileSystemBucketResponse:
        """
        为文件系统关联Bucket
        """
        
        kwargs = {}
        kwargs["action"] = "AttachFileSystemBucket"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachFileSystemBucketResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchAddClientNodes(
            self,
            request: models.BatchAddClientNodesRequest,
            opts: Dict = None,
    ) -> models.BatchAddClientNodesResponse:
        """
        批量添加客户端节点
        """
        
        kwargs = {}
        kwargs["action"] = "BatchAddClientNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchAddClientNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteClientNodes(
            self,
            request: models.BatchDeleteClientNodesRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteClientNodesResponse:
        """
        批量删除客户端节点
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteClientNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteClientNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BuildClientNodeMountCommand(
            self,
            request: models.BuildClientNodeMountCommandRequest,
            opts: Dict = None,
    ) -> models.BuildClientNodeMountCommandResponse:
        """
        生成客户端的挂载命令
        """
        
        kwargs = {}
        kwargs["action"] = "BuildClientNodeMountCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BuildClientNodeMountCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataRepositoryTask(
            self,
            request: models.CreateDataRepositoryTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDataRepositoryTaskResponse:
        """
        创建数据流通任务,包括从将文件系统的数据上传到存储桶下, 以及从存储桶下载到文件系统里。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataRepositoryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataRepositoryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileSystem(
            self,
            request: models.CreateFileSystemRequest,
            opts: Dict = None,
    ) -> models.CreateFileSystemResponse:
        """
        创建文件系统
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileset(
            self,
            request: models.CreateFilesetRequest,
            opts: Dict = None,
    ) -> models.CreateFilesetResponse:
        """
        创建Fileset
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFilesetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCrossVpcSubnetSupportForClientNode(
            self,
            request: models.DeleteCrossVpcSubnetSupportForClientNodeRequest,
            opts: Dict = None,
    ) -> models.DeleteCrossVpcSubnetSupportForClientNodeResponse:
        """
        为客户端节点删除跨vpc子网访问能力
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCrossVpcSubnetSupportForClientNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCrossVpcSubnetSupportForClientNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFileSystem(
            self,
            request: models.DeleteFileSystemRequest,
            opts: Dict = None,
    ) -> models.DeleteFileSystemResponse:
        """
        删除文件系统
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFileset(
            self,
            request: models.DeleteFilesetRequest,
            opts: Dict = None,
    ) -> models.DeleteFilesetResponse:
        """
        删除Fileset
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFileset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFilesetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientNodes(
            self,
            request: models.DescribeClientNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeClientNodesResponse:
        """
        列出集群中所有的客户端节点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterClientToken(
            self,
            request: models.DescribeClusterClientTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterClientTokenResponse:
        """
        查询GooseFS集群客户端凭证
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterClientToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterClientTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterRoleToken(
            self,
            request: models.DescribeClusterRoleTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterRoleTokenResponse:
        """
        查询GooseFS集群角色凭证
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterRoleToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterRoleTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterRoles(
            self,
            request: models.DescribeClusterRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterRolesResponse:
        """
        接口废弃

        查询GooseFS集群角色
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataRepositoryTaskStatus(
            self,
            request: models.DescribeDataRepositoryTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDataRepositoryTaskStatusResponse:
        """
        获取数据流通任务实时状态，用作客户端控制
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataRepositoryTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataRepositoryTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileSystemBuckets(
            self,
            request: models.DescribeFileSystemBucketsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileSystemBucketsResponse:
        """
        罗列文件系统关联的Bucket映射
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileSystemBuckets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileSystemBucketsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileSystems(
            self,
            request: models.DescribeFileSystemsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileSystemsResponse:
        """
        列出所有的文件系统
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileSystems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileSystemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFilesetGeneralConfig(
            self,
            request: models.DescribeFilesetGeneralConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeFilesetGeneralConfigResponse:
        """
        查询Fileset通用配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFilesetGeneralConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFilesetGeneralConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFilesets(
            self,
            request: models.DescribeFilesetsRequest,
            opts: Dict = None,
    ) -> models.DescribeFilesetsResponse:
        """
        查询Fileset列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFilesets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFilesetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachFileSystemBucket(
            self,
            request: models.DetachFileSystemBucketRequest,
            opts: Dict = None,
    ) -> models.DetachFileSystemBucketResponse:
        """
        解绑文件系统与Bucket的映射
        """
        
        kwargs = {}
        kwargs["action"] = "DetachFileSystemBucket"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachFileSystemBucketResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExpandCapacity(
            self,
            request: models.ExpandCapacityRequest,
            opts: Dict = None,
    ) -> models.ExpandCapacityResponse:
        """
        扩展文件系统容量
        """
        
        kwargs = {}
        kwargs["action"] = "ExpandCapacity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExpandCapacityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDataRepositoryBandwidth(
            self,
            request: models.ModifyDataRepositoryBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyDataRepositoryBandwidthResponse:
        """
        修改数据流动带宽
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDataRepositoryBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDataRepositoryBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCrossVpcSubnetSupportForClientNode(
            self,
            request: models.QueryCrossVpcSubnetSupportForClientNodeRequest,
            opts: Dict = None,
    ) -> models.QueryCrossVpcSubnetSupportForClientNodeResponse:
        """
        查询客户端节点跨vpc子网访问能力
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCrossVpcSubnetSupportForClientNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCrossVpcSubnetSupportForClientNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryDataRepositoryBandwidth(
            self,
            request: models.QueryDataRepositoryBandwidthRequest,
            opts: Dict = None,
    ) -> models.QueryDataRepositoryBandwidthResponse:
        """
        查询数据流动带宽
        """
        
        kwargs = {}
        kwargs["action"] = "QueryDataRepositoryBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryDataRepositoryBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFileset(
            self,
            request: models.UpdateFilesetRequest,
            opts: Dict = None,
    ) -> models.UpdateFilesetResponse:
        """
        修改FIleset
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFileset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFilesetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFilesetGeneralConfig(
            self,
            request: models.UpdateFilesetGeneralConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateFilesetGeneralConfigResponse:
        """
        修改Fileset通用配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFilesetGeneralConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFilesetGeneralConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)