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
from tencentcloud.bi.v20220105 import models


class BiClient(AbstractClient):
    _apiVersion = '2022-01-05'
    _endpoint = 'bi.tencentcloudapi.com'
    _service = 'bi'


    def ApplyEmbedInterval(self, request):
        r"""申请延长Token可用时间接口-强鉴权

        :param request: Request instance for ApplyEmbedInterval.
        :type request: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedIntervalRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedIntervalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyEmbedInterval", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyEmbedIntervalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearEmbedToken(self, request):
        r"""强鉴权token 清理，只有企业管理员才能调用该接口

        :param request: Request instance for ClearEmbedToken.
        :type request: :class:`tencentcloud.bi.v20220105.models.ClearEmbedTokenRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ClearEmbedTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearEmbedToken", params, headers=headers)
            response = json.loads(body)
            model = models.ClearEmbedTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuthApiKey(self, request):
        r"""创建ApiKey

        :param request: Request instance for CreateAuthApiKey.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateAuthApiKeyRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateAuthApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuthApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuthApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCorpTag(self, request):
        r"""创建企业标签

        :param request: Request instance for CreateCorpTag.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateCorpTagRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateCorpTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCorpTag", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCorpTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataTable(self, request):
        r"""添加数据表

        :param request: Request instance for CreateDataTable.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateDataTableRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateDataTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatasource(self, request):
        r"""创建数据源

        :param request: Request instance for CreateDatasource.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateDatasourceRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatasourceCloud(self, request):
        r"""创建云数据库

        :param request: Request instance for CreateDatasourceCloud.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateDatasourceCloudRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateDatasourceCloudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatasourceCloud", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatasourceCloudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmbedToken(self, request):
        r"""创建嵌出报表-强鉴权

        :param request: Request instance for CreateEmbedToken.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateEmbedTokenRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateEmbedTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmbedToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmbedTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePermissionRanks(self, request):
        r"""创建行列权限

        :param request: Request instance for CreatePermissionRanks.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreatePermissionRanksRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreatePermissionRanksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePermissionRanks", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePermissionRanksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProject(self, request):
        r"""创建项目

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTagTable(self, request):
        r"""创建标签表

        :param request: Request instance for CreateTagTable.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateTagTableRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateTagTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTagTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTagTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserGroup(self, request):
        r"""CreateUserGroup

        :param request: Request instance for CreateUserGroup.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateUserGroupRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserGroupMember(self, request):
        r"""CreateUserGroupMember

        :param request: Request instance for CreateUserGroupMember.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateUserGroupMemberRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateUserGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserRole(self, request):
        r"""创建用户角色

        :param request: Request instance for CreateUserRole.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateUserRoleRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateUserRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserRoleProject(self, request):
        r"""项目内-创建用户角色

        :param request: Request instance for CreateUserRoleProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateUserRoleProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateUserRoleProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserRoleProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserRoleProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuthApiKey(self, request):
        r"""删除ApiKey

        :param request: Request instance for DeleteAuthApiKey.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteAuthApiKeyRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteAuthApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuthApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuthApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDatasource(self, request):
        r"""删除数据源

        :param request: Request instance for DeleteDatasource.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteDatasourceRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        r"""删除项目

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserGroup(self, request):
        r"""DeleteUserGroup

        :param request: Request instance for DeleteUserGroup.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteUserGroupRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserGroupMember(self, request):
        r"""DeleteUserGroupMember

        :param request: Request instance for DeleteUserGroupMember.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteUserGroupMemberRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteUserGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserRole(self, request):
        r"""删除用户角色，会删除用户

        :param request: Request instance for DeleteUserRole.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteUserRoleRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteUserRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserRole", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserRoleProject(self, request):
        r"""项目内-删除用户角色

        :param request: Request instance for DeleteUserRoleProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.DeleteUserRoleProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DeleteUserRoleProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserRoleProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserRoleProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuthApiKeyInfo(self, request):
        r"""ApiKey信息

        :param request: Request instance for DescribeAuthApiKeyInfo.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeAuthApiKeyInfoRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeAuthApiKeyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuthApiKeyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuthApiKeyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuthApiKeyList(self, request):
        r"""ApiKey列表

        :param request: Request instance for DescribeAuthApiKeyList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeAuthApiKeyListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeAuthApiKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuthApiKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuthApiKeyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatasourceList(self, request):
        r"""查询数据源列表

        :param request: Request instance for DescribeDatasourceList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeDatasourceListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeDatasourceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatasourceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatasourceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePageWidgetList(self, request):
        r"""查询页面组件信息

        :param request: Request instance for DescribePageWidgetList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribePageWidgetListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribePageWidgetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePageWidgetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePageWidgetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePermissionRanksInfo(self, request):
        r"""根据角色或标签查询行列权限配置

        :param request: Request instance for DescribePermissionRanksInfo.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribePermissionRanksInfoRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribePermissionRanksInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePermissionRanksInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePermissionRanksInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePermissionRoleInfo(self, request):
        r"""行列权限项目内角色列表接口1

        :param request: Request instance for DescribePermissionRoleInfo.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribePermissionRoleInfoRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribePermissionRoleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePermissionRoleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePermissionRoleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePermissionStatusInfo(self, request):
        r"""查询行列权限初始状态1

        :param request: Request instance for DescribePermissionStatusInfo.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribePermissionStatusInfoRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribePermissionStatusInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePermissionStatusInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePermissionStatusInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectInfo(self, request):
        r"""项目详情接口

        :param request: Request instance for DescribeProjectInfo.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeProjectInfoRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeProjectInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectList(self, request):
        r"""项目信息

        :param request: Request instance for DescribeProjectList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeProjectListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeProjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceUserGroupPageList(self, request):
        r"""用户组资源权限查询接口

        :param request: Request instance for DescribeResourceUserGroupPageList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeResourceUserGroupPageListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeResourceUserGroupPageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceUserGroupPageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceUserGroupPageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSourceFieldList(self, request):
        r"""原始数据表字段接口信息

        :param request: Request instance for DescribeSourceFieldList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeSourceFieldListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeSourceFieldListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSourceFieldList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSourceFieldListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserGroupInfo(self, request):
        r"""DescribeUserGroupInfo

        :param request: Request instance for DescribeUserGroupInfo.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeUserGroupInfoRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeUserGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserGroupMemberList(self, request):
        r"""DescribeUserGroupMemberList

        :param request: Request instance for DescribeUserGroupMemberList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeUserGroupMemberListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeUserGroupMemberListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserGroupMemberList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserGroupMemberListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserGroupTreeList(self, request):
        r"""用户组数查询接口

        :param request: Request instance for DescribeUserGroupTreeList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeUserGroupTreeListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeUserGroupTreeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserGroupTreeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserGroupTreeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserProjectList(self, request):
        r"""项目内-用户接口

        :param request: Request instance for DescribeUserProjectList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeUserProjectListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeUserProjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserProjectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserProjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserRoleList(self, request):
        r"""用户角色列表

        :param request: Request instance for DescribeUserRoleList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeUserRoleListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeUserRoleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserRoleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserRoleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserRoleProjectList(self, request):
        r"""项目内-用户角色列表

        :param request: Request instance for DescribeUserRoleProjectList.
        :type request: :class:`tencentcloud.bi.v20220105.models.DescribeUserRoleProjectListRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.DescribeUserRoleProjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserRoleProjectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserRoleProjectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditCorpTag(self, request):
        r"""编辑企业标签(异步)

        :param request: Request instance for EditCorpTag.
        :type request: :class:`tencentcloud.bi.v20220105.models.EditCorpTagRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.EditCorpTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditCorpTag", params, headers=headers)
            response = json.loads(body)
            model = models.EditCorpTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportScreenPage(self, request):
        r"""页面截图导出

        :param request: Request instance for ExportScreenPage.
        :type request: :class:`tencentcloud.bi.v20220105.models.ExportScreenPageRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ExportScreenPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportScreenPage", params, headers=headers)
            response = json.loads(body)
            model = models.ExportScreenPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuthApiKey(self, request):
        r"""更新ApiKey

        :param request: Request instance for ModifyAuthApiKey.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyAuthApiKeyRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyAuthApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuthApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuthApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatasource(self, request):
        r"""更新数据源

        :param request: Request instance for ModifyDatasource.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyDatasourceRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatasourceCloud(self, request):
        r"""更新云数据库

        :param request: Request instance for ModifyDatasourceCloud.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyDatasourceCloudRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyDatasourceCloudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatasourceCloud", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatasourceCloudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        r"""修改项目信息

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceUser(self, request):
        r"""按用户资源修改

        :param request: Request instance for ModifyResourceUser.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyResourceUserRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyResourceUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceUserGroup(self, request):
        r"""更新用户组权限

        :param request: Request instance for ModifyResourceUserGroup.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyResourceUserGroupRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyResourceUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceUserGroupResource(self, request):
        r"""按资源 - 更新用户组权限

        :param request: Request instance for ModifyResourceUserGroupResource.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyResourceUserGroupResourceRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyResourceUserGroupResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceUserGroupResource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceUserGroupResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTagTable(self, request):
        r"""编辑标签表

        :param request: Request instance for ModifyTagTable.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyTagTableRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyTagTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTagTable", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTagTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserDetailInfo(self, request):
        r"""修改用户角色信息

        :param request: Request instance for ModifyUserDetailInfo.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyUserDetailInfoRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyUserDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserDetailInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserDetailInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserGroup(self, request):
        r"""ModifyUserGroup

        :param request: Request instance for ModifyUserGroup.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyUserGroupRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyUserGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserRole(self, request):
        r"""修改用户角色信息

        :param request: Request instance for ModifyUserRole.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyUserRoleRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyUserRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserRole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserRoleProject(self, request):
        r"""项目-修改用户角色信息

        :param request: Request instance for ModifyUserRoleProject.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyUserRoleProjectRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyUserRoleProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserRoleProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserRoleProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserTag(self, request):
        r"""修改用户标签值

        :param request: Request instance for ModifyUserTag.
        :type request: :class:`tencentcloud.bi.v20220105.models.ModifyUserTagRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ModifyUserTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserTag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryUserGroupMember(self, request):
        r"""QueryUserGroupMember

        :param request: Request instance for QueryUserGroupMember.
        :type request: :class:`tencentcloud.bi.v20220105.models.QueryUserGroupMemberRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.QueryUserGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryUserGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.QueryUserGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))