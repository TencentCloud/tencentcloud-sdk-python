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
from tencentcloud.chdfs.v20190718 import models
from typing import Dict


class ChdfsClient(AbstractClient):
    _apiVersion = '2019-07-18'
    _endpoint = 'chdfs.tencentcloudapi.com'
    _service = 'chdfs'

    async def CreateAccessGroup(
            self,
            request: models.CreateAccessGroupRequest,
            opts: Dict = None,
    ) -> models.CreateAccessGroupResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        创建权限组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessRules(
            self,
            request: models.CreateAccessRulesRequest,
            opts: Dict = None,
    ) -> models.CreateAccessRulesResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量创建权限规则，权限规则ID和创建时间无需填写。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileSystem(
            self,
            request: models.CreateFileSystemRequest,
            opts: Dict = None,
    ) -> models.CreateFileSystemResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        创建文件系统（异步）。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLifeCycleRules(
            self,
            request: models.CreateLifeCycleRulesRequest,
            opts: Dict = None,
    ) -> models.CreateLifeCycleRulesResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量创建生命周期规则，生命周期规则ID和创建时间无需填写。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLifeCycleRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLifeCycleRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMountPoint(
            self,
            request: models.CreateMountPointRequest,
            opts: Dict = None,
    ) -> models.CreateMountPointResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        创建文件系统挂载点，仅限于创建成功的文件系统。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMountPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMountPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRestoreTasks(
            self,
            request: models.CreateRestoreTasksRequest,
            opts: Dict = None,
    ) -> models.CreateRestoreTasksResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量创建回热任务，回热任务ID、状态和创建时间无需填写。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRestoreTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRestoreTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccessGroup(
            self,
            request: models.DeleteAccessGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteAccessGroupResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        删除权限组。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccessGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccessGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccessRules(
            self,
            request: models.DeleteAccessRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteAccessRulesResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量删除权限规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFileSystem(
            self,
            request: models.DeleteFileSystemRequest,
            opts: Dict = None,
    ) -> models.DeleteFileSystemResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        删除文件系统，不允许删除非空文件系统。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLifeCycleRules(
            self,
            request: models.DeleteLifeCycleRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteLifeCycleRulesResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量删除生命周期规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLifeCycleRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLifeCycleRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMountPoint(
            self,
            request: models.DeleteMountPointRequest,
            opts: Dict = None,
    ) -> models.DeleteMountPointResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        删除挂载点。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMountPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMountPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessGroups(
            self,
            request: models.DescribeAccessGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessGroupsResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        查看权限组列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessRules(
            self,
            request: models.DescribeAccessRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessRulesResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        通过权限组ID查看权限规则列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileSystem(
            self,
            request: models.DescribeFileSystemRequest,
            opts: Dict = None,
    ) -> models.DescribeFileSystemResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        查看文件系统详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileSystems(
            self,
            request: models.DescribeFileSystemsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileSystemsResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        查看文件系统列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileSystems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileSystemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLifeCycleRules(
            self,
            request: models.DescribeLifeCycleRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLifeCycleRulesResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        通过文件系统ID查看生命周期规则列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLifeCycleRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLifeCycleRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMountPoint(
            self,
            request: models.DescribeMountPointRequest,
            opts: Dict = None,
    ) -> models.DescribeMountPointResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        查看挂载点详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMountPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMountPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMountPoints(
            self,
            request: models.DescribeMountPointsRequest,
            opts: Dict = None,
    ) -> models.DescribeMountPointsResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        通过文件系统ID或者权限组ID查看挂载点列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMountPoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMountPointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTags(
            self,
            request: models.DescribeResourceTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTagsResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        通过文件系统ID查看资源标签列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRestoreTasks(
            self,
            request: models.DescribeRestoreTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeRestoreTasksResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        通过文件系统ID查看回热任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRestoreTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRestoreTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessGroup(
            self,
            request: models.ModifyAccessGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessGroupResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        修改权限组属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessRules(
            self,
            request: models.ModifyAccessRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessRulesResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量修改权限规则属性，需要指定权限规则ID，支持修改权限规则地址、访问模式和优先级。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileSystem(
            self,
            request: models.ModifyFileSystemRequest,
            opts: Dict = None,
    ) -> models.ModifyFileSystemResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        修改文件系统属性，仅限于创建成功的文件系统。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLifeCycleRules(
            self,
            request: models.ModifyLifeCycleRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyLifeCycleRulesResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量修改生命周期规则属性，需要指定生命周期规则ID，支持修改生命周期规则名称、路径、转换列表和状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLifeCycleRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLifeCycleRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMountPoint(
            self,
            request: models.ModifyMountPointRequest,
            opts: Dict = None,
    ) -> models.ModifyMountPointResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        修改挂载点属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMountPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMountPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceTags(
            self,
            request: models.ModifyResourceTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceTagsResponse:
        """
        云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        修改资源标签列表，全量覆盖。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)