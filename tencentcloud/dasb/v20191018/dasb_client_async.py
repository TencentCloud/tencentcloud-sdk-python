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
from tencentcloud.dasb.v20191018 import models
from typing import Dict


class DasbClient(AbstractClient):
    _apiVersion = '2019-10-18'
    _endpoint = 'dasb.tencentcloudapi.com'
    _service = 'dasb'

    async def AddDeviceGroupMembers(
            self,
            request: models.AddDeviceGroupMembersRequest,
            opts: Dict = None,
    ) -> models.AddDeviceGroupMembersResponse:
        """
        添加资产组成员
        """
        
        kwargs = {}
        kwargs["action"] = "AddDeviceGroupMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDeviceGroupMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUserGroupMembers(
            self,
            request: models.AddUserGroupMembersRequest,
            opts: Dict = None,
    ) -> models.AddUserGroupMembersResponse:
        """
        添加用户组成员
        """
        
        kwargs = {}
        kwargs["action"] = "AddUserGroupMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUserGroupMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindDeviceAccountPassword(
            self,
            request: models.BindDeviceAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.BindDeviceAccountPasswordResponse:
        """
        绑定主机账号密码
        """
        
        kwargs = {}
        kwargs["action"] = "BindDeviceAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindDeviceAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindDeviceAccountPrivateKey(
            self,
            request: models.BindDeviceAccountPrivateKeyRequest,
            opts: Dict = None,
    ) -> models.BindDeviceAccountPrivateKeyResponse:
        """
        绑定主机账号私钥
        """
        
        kwargs = {}
        kwargs["action"] = "BindDeviceAccountPrivateKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindDeviceAccountPrivateKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindDeviceResource(
            self,
            request: models.BindDeviceResourceRequest,
            opts: Dict = None,
    ) -> models.BindDeviceResourceResponse:
        """
        修改资产绑定的堡垒机服务
        """
        
        kwargs = {}
        kwargs["action"] = "BindDeviceResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindDeviceResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAcl(
            self,
            request: models.CreateAclRequest,
            opts: Dict = None,
    ) -> models.CreateAclResponse:
        """
        新建访问权限
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetSyncJob(
            self,
            request: models.CreateAssetSyncJobRequest,
            opts: Dict = None,
    ) -> models.CreateAssetSyncJobResponse:
        """
        创建手工资产同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateChangePwdTask(
            self,
            request: models.CreateChangePwdTaskRequest,
            opts: Dict = None,
    ) -> models.CreateChangePwdTaskResponse:
        """
        创建修改密码任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateChangePwdTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateChangePwdTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCmdTemplate(
            self,
            request: models.CreateCmdTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateCmdTemplateResponse:
        """
        新建高危命令模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCmdTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCmdTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeviceAccount(
            self,
            request: models.CreateDeviceAccountRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceAccountResponse:
        """
        新建主机账号
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeviceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeviceGroup(
            self,
            request: models.CreateDeviceGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceGroupResponse:
        """
        新建资产组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeviceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResource(
            self,
            request: models.CreateResourceRequest,
            opts: Dict = None,
    ) -> models.CreateResourceResponse:
        """
        创建堡垒机实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        新建用户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserGroup(
            self,
            request: models.CreateUserGroupRequest,
            opts: Dict = None,
    ) -> models.CreateUserGroupResponse:
        """
        新建用户组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAcls(
            self,
            request: models.DeleteAclsRequest,
            opts: Dict = None,
    ) -> models.DeleteAclsResponse:
        """
        删除访问权限
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAcls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAclsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteChangePwdTask(
            self,
            request: models.DeleteChangePwdTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteChangePwdTaskResponse:
        """
        删除改密任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteChangePwdTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteChangePwdTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCmdTemplates(
            self,
            request: models.DeleteCmdTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteCmdTemplatesResponse:
        """
        删除高危命令模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCmdTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCmdTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeviceAccounts(
            self,
            request: models.DeleteDeviceAccountsRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceAccountsResponse:
        """
        删除主机账号
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeviceAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeviceGroupMembers(
            self,
            request: models.DeleteDeviceGroupMembersRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceGroupMembersResponse:
        """
        删除资产组成员
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeviceGroupMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceGroupMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeviceGroups(
            self,
            request: models.DeleteDeviceGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceGroupsResponse:
        """
        删除资产组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeviceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDevices(
            self,
            request: models.DeleteDevicesRequest,
            opts: Dict = None,
    ) -> models.DeleteDevicesResponse:
        """
        删除主机
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserGroupMembers(
            self,
            request: models.DeleteUserGroupMembersRequest,
            opts: Dict = None,
    ) -> models.DeleteUserGroupMembersResponse:
        """
        删除用户组成员
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserGroupMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserGroupMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserGroups(
            self,
            request: models.DeleteUserGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteUserGroupsResponse:
        """
        删除用户组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsers(
            self,
            request: models.DeleteUsersRequest,
            opts: Dict = None,
    ) -> models.DeleteUsersResponse:
        """
        删除用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployResource(
            self,
            request: models.DeployResourceRequest,
            opts: Dict = None,
    ) -> models.DeployResourceResponse:
        """
        开通服务，初始化资源，只针对新购资源
        """
        
        kwargs = {}
        kwargs["action"] = "DeployResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAcls(
            self,
            request: models.DescribeAclsRequest,
            opts: Dict = None,
    ) -> models.DescribeAclsResponse:
        """
        查询访问权限列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAcls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAclsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSyncStatus(
            self,
            request: models.DescribeAssetSyncStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSyncStatusResponse:
        """
        查询资产同步状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSyncStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSyncStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChangePwdTask(
            self,
            request: models.DescribeChangePwdTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeChangePwdTaskResponse:
        """
        查询改密任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChangePwdTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChangePwdTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChangePwdTaskDetail(
            self,
            request: models.DescribeChangePwdTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeChangePwdTaskDetailResponse:
        """
        查询改密任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChangePwdTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChangePwdTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmdTemplates(
            self,
            request: models.DescribeCmdTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeCmdTemplatesResponse:
        """
        查询命令模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmdTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmdTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDasbImageIds(
            self,
            request: models.DescribeDasbImageIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeDasbImageIdsResponse:
        """
        获取镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDasbImageIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDasbImageIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceAccounts(
            self,
            request: models.DescribeDeviceAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceAccountsResponse:
        """
        查询主机账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceGroupMembers(
            self,
            request: models.DescribeDeviceGroupMembersRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceGroupMembersResponse:
        """
        查询资产组成员列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceGroupMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceGroupMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceGroups(
            self,
            request: models.DescribeDeviceGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceGroupsResponse:
        """
        查询资产组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevices(
            self,
            request: models.DescribeDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicesResponse:
        """
        查询资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomains(
            self,
            request: models.DescribeDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainsResponse:
        """
        查询网络域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginEvent(
            self,
            request: models.DescribeLoginEventRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginEventResponse:
        """
        查询登录日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOperationEvent(
            self,
            request: models.DescribeOperationEventRequest,
            opts: Dict = None,
    ) -> models.DescribeOperationEventResponse:
        """
        查询操作日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOperationEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOperationEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResources(
            self,
            request: models.DescribeResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesResponse:
        """
        查询用户购买的堡垒机服务信息，包括资源ID、授权点数、VPC、过期时间等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserGroupMembers(
            self,
            request: models.DescribeUserGroupMembersRequest,
            opts: Dict = None,
    ) -> models.DescribeUserGroupMembersResponse:
        """
        查询用户组成员列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserGroupMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserGroupMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserGroups(
            self,
            request: models.DescribeUserGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeUserGroupsResponse:
        """
        查询用户组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsers(
            self,
            request: models.DescribeUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersResponse:
        """
        查询用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportExternalDevice(
            self,
            request: models.ImportExternalDeviceRequest,
            opts: Dict = None,
    ) -> models.ImportExternalDeviceResponse:
        """
        导入外部资产信息
        """
        
        kwargs = {}
        kwargs["action"] = "ImportExternalDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportExternalDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAcl(
            self,
            request: models.ModifyAclRequest,
            opts: Dict = None,
    ) -> models.ModifyAclResponse:
        """
        修改访问权限
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyChangePwdTask(
            self,
            request: models.ModifyChangePwdTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyChangePwdTaskResponse:
        """
        更新修改密码任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyChangePwdTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyChangePwdTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCmdTemplate(
            self,
            request: models.ModifyCmdTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyCmdTemplateResponse:
        """
        修改高危命令模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCmdTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCmdTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDevice(
            self,
            request: models.ModifyDeviceRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceResponse:
        """
        修改资产信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceGroup(
            self,
            request: models.ModifyDeviceGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceGroupResponse:
        """
        修改资产组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOAuthSetting(
            self,
            request: models.ModifyOAuthSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyOAuthSettingResponse:
        """
        设置OAuth认证参数
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOAuthSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOAuthSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResource(
            self,
            request: models.ModifyResourceRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceResponse:
        """
        资源变配
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUser(
            self,
            request: models.ModifyUserRequest,
            opts: Dict = None,
    ) -> models.ModifyUserResponse:
        """
        修改用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserGroup(
            self,
            request: models.ModifyUserGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyUserGroupResponse:
        """
        修改用户组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetDeviceAccountPassword(
            self,
            request: models.ResetDeviceAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetDeviceAccountPasswordResponse:
        """
        清除设备账号绑定密码
        """
        
        kwargs = {}
        kwargs["action"] = "ResetDeviceAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetDeviceAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetDeviceAccountPrivateKey(
            self,
            request: models.ResetDeviceAccountPrivateKeyRequest,
            opts: Dict = None,
    ) -> models.ResetDeviceAccountPrivateKeyResponse:
        """
        清除设备账号绑定的密钥
        """
        
        kwargs = {}
        kwargs["action"] = "ResetDeviceAccountPrivateKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetDeviceAccountPrivateKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetUser(
            self,
            request: models.ResetUserRequest,
            opts: Dict = None,
    ) -> models.ResetUserResponse:
        """
        重置用户
        """
        
        kwargs = {}
        kwargs["action"] = "ResetUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunChangePwdTask(
            self,
            request: models.RunChangePwdTaskRequest,
            opts: Dict = None,
    ) -> models.RunChangePwdTaskResponse:
        """
        执行改密任务
        """
        
        kwargs = {}
        kwargs["action"] = "RunChangePwdTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunChangePwdTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchAuditLog(
            self,
            request: models.SearchAuditLogRequest,
            opts: Dict = None,
    ) -> models.SearchAuditLogResponse:
        """
        搜索审计日志
        """
        
        kwargs = {}
        kwargs["action"] = "SearchAuditLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchAuditLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchCommand(
            self,
            request: models.SearchCommandRequest,
            opts: Dict = None,
    ) -> models.SearchCommandResponse:
        """
        命令执行检索
        """
        
        kwargs = {}
        kwargs["action"] = "SearchCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchCommandBySid(
            self,
            request: models.SearchCommandBySidRequest,
            opts: Dict = None,
    ) -> models.SearchCommandBySidResponse:
        """
        根据会话Id搜索Command
        """
        
        kwargs = {}
        kwargs["action"] = "SearchCommandBySid"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchCommandBySidResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchFile(
            self,
            request: models.SearchFileRequest,
            opts: Dict = None,
    ) -> models.SearchFileResponse:
        """
        文件传输检索
        """
        
        kwargs = {}
        kwargs["action"] = "SearchFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchFileBySid(
            self,
            request: models.SearchFileBySidRequest,
            opts: Dict = None,
    ) -> models.SearchFileBySidResponse:
        """
        搜索文件传输会话下文件操作列表
        """
        
        kwargs = {}
        kwargs["action"] = "SearchFileBySid"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchFileBySidResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchSession(
            self,
            request: models.SearchSessionRequest,
            opts: Dict = None,
    ) -> models.SearchSessionResponse:
        """
        搜索会话
        """
        
        kwargs = {}
        kwargs["action"] = "SearchSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchSessionCommand(
            self,
            request: models.SearchSessionCommandRequest,
            opts: Dict = None,
    ) -> models.SearchSessionCommandResponse:
        """
        命令检索
        """
        
        kwargs = {}
        kwargs["action"] = "SearchSessionCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchSessionCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)