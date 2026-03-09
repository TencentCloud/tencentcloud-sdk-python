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
from tencentcloud.cetcd.v20220325 import models
from typing import Dict


class CetcdClient(AbstractClient):
    _apiVersion = '2022-03-25'
    _endpoint = 'cetcd.tencentcloudapi.com'
    _service = 'cetcd'

    async def CreateEtcdInstance(
            self,
            request: models.CreateEtcdInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateEtcdInstanceResponse:
        """
        创建etcd实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEtcdInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEtcdInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEtcdSnapshot(
            self,
            request: models.CreateEtcdSnapshotRequest,
            opts: Dict = None,
    ) -> models.CreateEtcdSnapshotResponse:
        """
        创建etcd快照
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEtcdSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEtcdSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEtcdSnapshotPolicy(
            self,
            request: models.CreateEtcdSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateEtcdSnapshotPolicyResponse:
        """
        创建etcd快照策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEtcdSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEtcdSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEtcdAvailableVersions(
            self,
            request: models.DescribeEtcdAvailableVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeEtcdAvailableVersionsResponse:
        """
        查看etcd可用版本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEtcdAvailableVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEtcdAvailableVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEtcdCreatingProgress(
            self,
            request: models.DescribeEtcdCreatingProgressRequest,
            opts: Dict = None,
    ) -> models.DescribeEtcdCreatingProgressResponse:
        """
        查看etcd集群创建进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEtcdCreatingProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEtcdCreatingProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEtcdCredentials(
            self,
            request: models.DescribeEtcdCredentialsRequest,
            opts: Dict = None,
    ) -> models.DescribeEtcdCredentialsResponse:
        """
        查询etcd访问凭证
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEtcdCredentials"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEtcdCredentialsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEtcdInstances(
            self,
            request: models.DescribeEtcdInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeEtcdInstancesResponse:
        """
        查询etcd实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEtcdInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEtcdInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEtcdQuota(
            self,
            request: models.DescribeEtcdQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeEtcdQuotaResponse:
        """
        查看etcd集群配额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEtcdQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEtcdQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEtcdRegions(
            self,
            request: models.DescribeEtcdRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeEtcdRegionsResponse:
        """
        查看etcd支持地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEtcdRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEtcdRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEtcdSnapshotPolicies(
            self,
            request: models.DescribeEtcdSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeEtcdSnapshotPoliciesResponse:
        """
        查看etcd快照策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEtcdSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEtcdSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEtcdSnapshots(
            self,
            request: models.DescribeEtcdSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeEtcdSnapshotsResponse:
        """
        查看etcd快照列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEtcdSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEtcdSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEtcdTasks(
            self,
            request: models.DescribeEtcdTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeEtcdTasksResponse:
        """
        查看etcd相关tasks
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEtcdTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEtcdTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRPCMethodList(
            self,
            request: models.DescribeRPCMethodListRequest,
            opts: Dict = None,
    ) -> models.DescribeRPCMethodListResponse:
        """
        获取etcd集群的gRPC方法列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRPCMethodList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRPCMethodListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableEtcdInstanceDeletionProtection(
            self,
            request: models.DisableEtcdInstanceDeletionProtectionRequest,
            opts: Dict = None,
    ) -> models.DisableEtcdInstanceDeletionProtectionResponse:
        """
        关闭etcd实例删除保护
        """
        
        kwargs = {}
        kwargs["action"] = "DisableEtcdInstanceDeletionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableEtcdInstanceDeletionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableEtcdInstanceDeletionProtection(
            self,
            request: models.EnableEtcdInstanceDeletionProtectionRequest,
            opts: Dict = None,
    ) -> models.EnableEtcdInstanceDeletionProtectionResponse:
        """
        启用etcd实例删除保护
        """
        
        kwargs = {}
        kwargs["action"] = "EnableEtcdInstanceDeletionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableEtcdInstanceDeletionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEtcdAttribute(
            self,
            request: models.ModifyEtcdAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyEtcdAttributeResponse:
        """
        修改etcd实例属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEtcdAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEtcdAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEtcdConfiguration(
            self,
            request: models.ModifyEtcdConfigurationRequest,
            opts: Dict = None,
    ) -> models.ModifyEtcdConfigurationResponse:
        """
        修改etcd实例配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEtcdConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEtcdConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEtcdSnapshotPolicy(
            self,
            request: models.ModifyEtcdSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyEtcdSnapshotPolicyResponse:
        """
        修改etcd快照策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEtcdSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEtcdSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeEtcdInstance(
            self,
            request: models.ResizeEtcdInstanceRequest,
            opts: Dict = None,
    ) -> models.ResizeEtcdInstanceResponse:
        """
        扩容etcd实例
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeEtcdInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeEtcdInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeEtcdInstance(
            self,
            request: models.UpgradeEtcdInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeEtcdInstanceResponse:
        """
        升级etcd实例
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeEtcdInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeEtcdInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)