# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.cme.v20191029 import models


class CmeClient(AbstractClient):
    _apiVersion = '2019-10-29'
    _endpoint = 'cme.tencentcloudapi.com'


    def AddTeamMember(self, request):
        """向一个团队中团队成员，并且指定成员的角色。

        :param request: Request instance for AddTeamMember.
        :type request: :class:`tencentcloud.cme.v20191029.models.AddTeamMemberRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.AddTeamMemberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddTeamMember", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddTeamMemberResponse()
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


    def CreateClass(self, request):
        """新增分类，用于管理素材。
        <li>分类层数不能超过10；</li>
        <li>子分类数不能超过10。</li>

        :param request: Request instance for CreateClass.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateClassRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClassResponse()
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


    def CreateLink(self, request):
        """创建素材链接或分类路径链接，将源资源信息链接到目标。

        :param request: Request instance for CreateLink.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateLinkRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateLinkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLink", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLinkResponse()
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


    def CreateProject(self, request):
        """创建云剪的编辑项目，支持创建视频剪辑、直播剪辑及导播台项目。

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProjectResponse()
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


    def CreateTeam(self, request):
        """创建一个团队。

        :param request: Request instance for CreateTeam.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateTeamRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateTeamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTeam", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTeamResponse()
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


    def DeleteClass(self, request):
        """删除分类信息，删除时检验下述限制：
        <li>分类路径必须存在；</li>
        <li>分类下没有绑定素材。</li>

        :param request: Request instance for DeleteClass.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteClassRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClassResponse()
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


    def DeleteLoginStatus(self, request):
        """删除用户登录态，使用户登出云剪平台。

        :param request: Request instance for DeleteLoginStatus.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteLoginStatusRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteLoginStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoginStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoginStatusResponse()
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


    def DeleteMaterial(self, request):
        """根据素材 Id 删除素材。

        :param request: Request instance for DeleteMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMaterialResponse()
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


    def DeleteProject(self, request):
        """删除云剪编辑项目。

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProjectResponse()
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


    def DeleteTeam(self, request):
        """删除一个团队。
        <li>要删除的团队必须没有归属的素材；</li>
        <li>要删除的团队必须没有归属的分类。</li>

        :param request: Request instance for DeleteTeam.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteTeamRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteTeamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTeam", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTeamResponse()
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


    def DeleteTeamMembers(self, request):
        """将团队成员从团队中删除，默认只有 Owner 及管理员才有此权限。

        :param request: Request instance for DeleteTeamMembers.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteTeamMembersRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteTeamMembersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTeamMembers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTeamMembersResponse()
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


    def DescribeClass(self, request):
        """获取指定归属者下所有的分类信息。

        :param request: Request instance for DescribeClass.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeClassRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassResponse()
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


    def DescribeJoinTeams(self, request):
        """获取指定的团队成员所加入的团队列表。

        :param request: Request instance for DescribeJoinTeams.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeJoinTeamsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeJoinTeamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJoinTeams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJoinTeamsResponse()
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


    def DescribeLoginStatus(self, request):
        """查询指定用户的登录态。

        :param request: Request instance for DescribeLoginStatus.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeLoginStatusRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeLoginStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoginStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoginStatusResponse()
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


    def DescribeMaterials(self, request):
        """根据素材 Id 批量获取素材详情。

        :param request: Request instance for DescribeMaterials.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeMaterialsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeMaterialsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMaterials", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMaterialsResponse()
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


    def DescribeProjects(self, request):
        """支持根据多种条件过滤出项目列表。

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectsResponse()
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


    def DescribeResourceAuthorization(self, request):
        """查询指定资源的授权列表。

        :param request: Request instance for DescribeResourceAuthorization.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeResourceAuthorizationRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeResourceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceAuthorization", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceAuthorizationResponse()
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


    def DescribeSharedSpace(self, request):
        """获取共享空间。当实体A对实体B授权某资源以后，实体B的共享空间就会增加实体A。

        :param request: Request instance for DescribeSharedSpace.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeSharedSpaceRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeSharedSpaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSharedSpace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSharedSpaceResponse()
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


    def DescribeTaskDetail(self, request):
        """获取任务详情信息，包含下面几个部分：
        <li>任务基础信息：包括任务状态、错误信息、创建时间等；</li>
        <li>导出项目输出信息：包括输出的素材 Id 等。</li>

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
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


    def DescribeTasks(self, request):
        """获取任务列表，支持条件筛选，返回对应的任务基础信息列表。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
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


    def DescribeTeamMembers(self, request):
        """获取指定成员 ID 的信息，同时支持拉取所有团队成员信息。

        :param request: Request instance for DescribeTeamMembers.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTeamMembersRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTeamMembersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTeamMembers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTeamMembersResponse()
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


    def DescribeTeams(self, request):
        """获取指定团队的信息。

        :param request: Request instance for DescribeTeams.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTeamsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTeamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTeams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTeamsResponse()
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


    def ExportVideoByEditorTrackData(self, request):
        """使用在线编辑轨道数据直接导出视频。

        :param request: Request instance for ExportVideoByEditorTrackData.
        :type request: :class:`tencentcloud.cme.v20191029.models.ExportVideoByEditorTrackDataRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExportVideoByEditorTrackDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportVideoByEditorTrackData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportVideoByEditorTrackDataResponse()
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


    def ExportVideoEditProject(self, request):
        """导出视频编辑项目，支持指定输出的模板。

        :param request: Request instance for ExportVideoEditProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ExportVideoEditProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExportVideoEditProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportVideoEditProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportVideoEditProjectResponse()
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


    def FlattenListMedia(self, request):
        """平铺分类路径下及其子分类下的所有素材。

        :param request: Request instance for FlattenListMedia.
        :type request: :class:`tencentcloud.cme.v20191029.models.FlattenListMediaRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.FlattenListMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FlattenListMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FlattenListMediaResponse()
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


    def GrantResourceAuthorization(self, request):
        """资源所属实体对目标实体授予目标资源的相应权限。

        :param request: Request instance for GrantResourceAuthorization.
        :type request: :class:`tencentcloud.cme.v20191029.models.GrantResourceAuthorizationRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.GrantResourceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GrantResourceAuthorization", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GrantResourceAuthorizationResponse()
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


    def ImportMaterial(self, request):
        """将云点播媒资文件导入到云剪素材库。

        :param request: Request instance for ImportMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.ImportMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ImportMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportMaterialResponse()
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


    def ImportMediaToProject(self, request):
        """将云点播中的媒资添加到素材库中，供后续视频编辑使用。

        :param request: Request instance for ImportMediaToProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ImportMediaToProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ImportMediaToProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportMediaToProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportMediaToProjectResponse()
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


    def ListMedia(self, request):
        """浏览当前分类路径下的资源，包括素材和子分类。

        :param request: Request instance for ListMedia.
        :type request: :class:`tencentcloud.cme.v20191029.models.ListMediaRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ListMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListMediaResponse()
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


    def ModifyMaterial(self, request):
        """修改素材信息，支持修改素材名称、分类路径、标签等信息。

        :param request: Request instance for ModifyMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMaterialResponse()
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


    def ModifyProject(self, request):
        """修改云剪编辑项目的信息。

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProjectResponse()
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


    def ModifyTeam(self, request):
        """修改团队信息，目前支持修改的操作有：
        <li>修改团队名称。</li>

        :param request: Request instance for ModifyTeam.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyTeamRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyTeamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTeam", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTeamResponse()
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


    def ModifyTeamMember(self, request):
        """修改团队成员信息，包括成员备注、角色等。

        :param request: Request instance for ModifyTeamMember.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyTeamMemberRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyTeamMemberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTeamMember", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTeamMemberResponse()
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


    def MoveClass(self, request):
        """移动某一个分类到另外一个分类下，也可用于分类重命名。
        <li>如果 SourceClassPath = /素材/视频/NBA，DestinationClassPath = /素材/视频/篮球，当 DestinationClassPath 不存在时候，操作结果为重命名 ClassPath，如果 DestinationClassPath 存在时候，操作结果为产生新目录 /素材/视频/篮球/NBA。</li>

        :param request: Request instance for MoveClass.
        :type request: :class:`tencentcloud.cme.v20191029.models.MoveClassRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.MoveClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MoveClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MoveClassResponse()
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


    def RevokeResourceAuthorization(self, request):
        """资源所属实体对目标实体回收目标资源的相应权限，若原本没有相应权限则不产生变更。

        :param request: Request instance for RevokeResourceAuthorization.
        :type request: :class:`tencentcloud.cme.v20191029.models.RevokeResourceAuthorizationRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.RevokeResourceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevokeResourceAuthorization", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevokeResourceAuthorizationResponse()
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


    def SearchMaterial(self, request):
        """根据检索条件搜索素材，返回素材的基本信息。

        :param request: Request instance for SearchMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.SearchMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.SearchMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchMaterialResponse()
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