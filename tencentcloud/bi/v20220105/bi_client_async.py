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
from tencentcloud.bi.v20220105 import models
from typing import Dict


class BiClient(AbstractClient):
    _apiVersion = '2022-01-05'
    _endpoint = 'bi.tencentcloudapi.com'
    _service = 'bi'

    async def ApplyEmbedInterval(
            self,
            request: models.ApplyEmbedIntervalRequest,
            opts: Dict = None,
    ) -> models.ApplyEmbedIntervalResponse:
        """
        申请延长Token可用时间接口-强鉴权
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyEmbedInterval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyEmbedIntervalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearEmbedToken(
            self,
            request: models.ClearEmbedTokenRequest,
            opts: Dict = None,
    ) -> models.ClearEmbedTokenResponse:
        """
        强鉴权token 清理，只有企业管理员才能调用该接口
        """
        
        kwargs = {}
        kwargs["action"] = "ClearEmbedToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearEmbedTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuthApiKey(
            self,
            request: models.CreateAuthApiKeyRequest,
            opts: Dict = None,
    ) -> models.CreateAuthApiKeyResponse:
        """
        创建ApiKey
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuthApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuthApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatasource(
            self,
            request: models.CreateDatasourceRequest,
            opts: Dict = None,
    ) -> models.CreateDatasourceResponse:
        """
        创建数据源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatasource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatasourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatasourceCloud(
            self,
            request: models.CreateDatasourceCloudRequest,
            opts: Dict = None,
    ) -> models.CreateDatasourceCloudResponse:
        """
        创建云数据库
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatasourceCloud"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatasourceCloudResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmbedToken(
            self,
            request: models.CreateEmbedTokenRequest,
            opts: Dict = None,
    ) -> models.CreateEmbedTokenResponse:
        """
        创建嵌出报表-强鉴权
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmbedToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmbedTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePermissionRanks(
            self,
            request: models.CreatePermissionRanksRequest,
            opts: Dict = None,
    ) -> models.CreatePermissionRanksResponse:
        """
        创建行列权限
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePermissionRanks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePermissionRanksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        创建项目
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserGroup(
            self,
            request: models.CreateUserGroupRequest,
            opts: Dict = None,
    ) -> models.CreateUserGroupResponse:
        """
        CreateUserGroup
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserGroupMember(
            self,
            request: models.CreateUserGroupMemberRequest,
            opts: Dict = None,
    ) -> models.CreateUserGroupMemberResponse:
        """
        CreateUserGroupMember
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserRole(
            self,
            request: models.CreateUserRoleRequest,
            opts: Dict = None,
    ) -> models.CreateUserRoleResponse:
        """
        创建用户角色
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserRoleProject(
            self,
            request: models.CreateUserRoleProjectRequest,
            opts: Dict = None,
    ) -> models.CreateUserRoleProjectResponse:
        """
        项目内-创建用户角色
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserRoleProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserRoleProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuthApiKey(
            self,
            request: models.DeleteAuthApiKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteAuthApiKeyResponse:
        """
        删除ApiKey
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuthApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuthApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDatasource(
            self,
            request: models.DeleteDatasourceRequest,
            opts: Dict = None,
    ) -> models.DeleteDatasourceResponse:
        """
        删除数据源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDatasource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDatasourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        删除项目
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserGroup(
            self,
            request: models.DeleteUserGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteUserGroupResponse:
        """
        DeleteUserGroup
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserGroupMember(
            self,
            request: models.DeleteUserGroupMemberRequest,
            opts: Dict = None,
    ) -> models.DeleteUserGroupMemberResponse:
        """
        DeleteUserGroupMember
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserRole(
            self,
            request: models.DeleteUserRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteUserRoleResponse:
        """
        删除用户角色，会删除用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserRoleProject(
            self,
            request: models.DeleteUserRoleProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteUserRoleProjectResponse:
        """
        项目内-删除用户角色
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserRoleProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserRoleProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuthApiKeyInfo(
            self,
            request: models.DescribeAuthApiKeyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAuthApiKeyInfoResponse:
        """
        ApiKey信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuthApiKeyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuthApiKeyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuthApiKeyList(
            self,
            request: models.DescribeAuthApiKeyListRequest,
            opts: Dict = None,
    ) -> models.DescribeAuthApiKeyListResponse:
        """
        ApiKey列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuthApiKeyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuthApiKeyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatasourceList(
            self,
            request: models.DescribeDatasourceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDatasourceListResponse:
        """
        查询数据源列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatasourceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatasourceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePageWidgetList(
            self,
            request: models.DescribePageWidgetListRequest,
            opts: Dict = None,
    ) -> models.DescribePageWidgetListResponse:
        """
        查询页面组件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePageWidgetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePageWidgetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePermissionRanksInfo(
            self,
            request: models.DescribePermissionRanksInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePermissionRanksInfoResponse:
        """
        根据角色或标签查询行列权限配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePermissionRanksInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePermissionRanksInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePermissionRoleInfo(
            self,
            request: models.DescribePermissionRoleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePermissionRoleInfoResponse:
        """
        行列权限项目内角色列表接口1
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePermissionRoleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePermissionRoleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePermissionStatusInfo(
            self,
            request: models.DescribePermissionStatusInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePermissionStatusInfoResponse:
        """
        查询行列权限初始状态1
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePermissionStatusInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePermissionStatusInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectInfo(
            self,
            request: models.DescribeProjectInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectInfoResponse:
        """
        项目详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectList(
            self,
            request: models.DescribeProjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectListResponse:
        """
        项目信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceUserGroupPageList(
            self,
            request: models.DescribeResourceUserGroupPageListRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceUserGroupPageListResponse:
        """
        用户组资源权限查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceUserGroupPageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceUserGroupPageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserGroupInfo(
            self,
            request: models.DescribeUserGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserGroupInfoResponse:
        """
        DescribeUserGroupInfo
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserGroupMemberList(
            self,
            request: models.DescribeUserGroupMemberListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserGroupMemberListResponse:
        """
        DescribeUserGroupMemberList
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserGroupMemberList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserGroupMemberListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserGroupTreeList(
            self,
            request: models.DescribeUserGroupTreeListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserGroupTreeListResponse:
        """
        用户组数查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserGroupTreeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserGroupTreeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserProjectList(
            self,
            request: models.DescribeUserProjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserProjectListResponse:
        """
        项目内-用户接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserProjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserProjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserRoleList(
            self,
            request: models.DescribeUserRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserRoleListResponse:
        """
        用户角色列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserRoleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserRoleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserRoleProjectList(
            self,
            request: models.DescribeUserRoleProjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserRoleProjectListResponse:
        """
        项目内-用户角色列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserRoleProjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserRoleProjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportScreenPage(
            self,
            request: models.ExportScreenPageRequest,
            opts: Dict = None,
    ) -> models.ExportScreenPageResponse:
        """
        页面截图导出
        """
        
        kwargs = {}
        kwargs["action"] = "ExportScreenPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportScreenPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuthApiKey(
            self,
            request: models.ModifyAuthApiKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyAuthApiKeyResponse:
        """
        更新ApiKey
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuthApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuthApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatasource(
            self,
            request: models.ModifyDatasourceRequest,
            opts: Dict = None,
    ) -> models.ModifyDatasourceResponse:
        """
        更新数据源
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatasource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatasourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatasourceCloud(
            self,
            request: models.ModifyDatasourceCloudRequest,
            opts: Dict = None,
    ) -> models.ModifyDatasourceCloudResponse:
        """
        更新云数据库
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatasourceCloud"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatasourceCloudResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        修改项目信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceUserGroup(
            self,
            request: models.ModifyResourceUserGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceUserGroupResponse:
        """
        更新用户组权限
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceUserGroupResource(
            self,
            request: models.ModifyResourceUserGroupResourceRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceUserGroupResourceResponse:
        """
        按资源 - 更新用户组权限
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceUserGroupResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceUserGroupResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserDetailInfo(
            self,
            request: models.ModifyUserDetailInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyUserDetailInfoResponse:
        """
        修改用户角色信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserDetailInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserDetailInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserGroup(
            self,
            request: models.ModifyUserGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyUserGroupResponse:
        """
        ModifyUserGroup
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserRole(
            self,
            request: models.ModifyUserRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyUserRoleResponse:
        """
        修改用户角色信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserRoleProject(
            self,
            request: models.ModifyUserRoleProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyUserRoleProjectResponse:
        """
        项目-修改用户角色信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserRoleProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserRoleProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryUserGroupMember(
            self,
            request: models.QueryUserGroupMemberRequest,
            opts: Dict = None,
    ) -> models.QueryUserGroupMemberResponse:
        """
        QueryUserGroupMember
        """
        
        kwargs = {}
        kwargs["action"] = "QueryUserGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryUserGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)