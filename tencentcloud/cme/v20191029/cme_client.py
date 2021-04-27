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
    _service = 'cme'


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
        """创建媒体链接或分类路径链接，将源资源信息链接到目标。

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
        """创建云剪的编辑项目，支持创建视频剪辑、直播剪辑、导播台、视频拆条、录制回放以及云转推项目。

        <b>若需使用云转推功能，请先咨询 [智能客服](https://cloud.tencent.com/act/event/smarty-service?from=doc_1138) 或 [提交工单](https://console.cloud.tencent.com/workorder/category) 。</b>

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
        """根据媒体 Id 删除媒体。

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


    def DescribeAccounts(self, request):
        """获取用户账号信息。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
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
        """根据媒体 Id 批量获取媒体详情。

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


    def DescribePlatforms(self, request):
        """<li>支持获取所创建的所有平台列表信息；</li>
        <li>支持获取指定的平台列表信息。</li>


        :param request: Request instance for DescribePlatforms.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribePlatformsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribePlatformsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePlatforms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePlatformsResponse()
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
        """获取共享空间。当个人或团队A对个人或团队B授权某资源以后，个人或团队B的共享空间就会增加个人或团队A。

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
        """获取指定团队的信息，拉取团队信息列表。

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
        """使用视频合成协议导出视频，支持导出到CME云媒资和VOD云媒资。

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


    def ExportVideoByTemplate(self, request):
        """使用视频编辑模板直接导出视频。

        :param request: Request instance for ExportVideoByTemplate.
        :type request: :class:`tencentcloud.cme.v20191029.models.ExportVideoByTemplateRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExportVideoByTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportVideoByTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportVideoByTemplateResponse()
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


    def ExportVideoByVideoSegmentationData(self, request):
        """使用视频智能拆条数据导出视频，将指定的视频拆条片段导出为一个视频。

        :param request: Request instance for ExportVideoByVideoSegmentationData.
        :type request: :class:`tencentcloud.cme.v20191029.models.ExportVideoByVideoSegmentationDataRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExportVideoByVideoSegmentationDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportVideoByVideoSegmentationData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportVideoByVideoSegmentationDataResponse()
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
        """平铺分类路径下及其子分类下的所有媒体基础信息。

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


    def GenerateVideoSegmentationSchemeByAi(self, request):
        """<li>发起视频智能拆条任务，支持智能生成和平精英集锦、王者荣耀集锦、足球集锦、篮球集锦 、人物集锦、新闻拆条等任务。</li>
        <li>和平精英集锦和王者荣耀集锦根据击杀场景进行拆条，足球集锦和篮球集锦根据进球场景进行拆条，人物集锦根据人物人脸特征进行拆条，新闻拆条根据导播进行拆条。</li>
        <li>【本接口内测中，暂不建议使用】</li>

        :param request: Request instance for GenerateVideoSegmentationSchemeByAi.
        :type request: :class:`tencentcloud.cme.v20191029.models.GenerateVideoSegmentationSchemeByAiRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.GenerateVideoSegmentationSchemeByAiResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GenerateVideoSegmentationSchemeByAi", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenerateVideoSegmentationSchemeByAiResponse()
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
        """资源归属者对目标个人或团队授予目标资源的相应权限。

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


    def HandleStreamConnectProject(self, request):
        """对云转推项目进行操作。
        ### 操作类型<a id="Operation"></a>
        - `AddInput`（添加输入源），包括：
        	- 添加直播拉流输入源，参见 [示例1](#.E7.A4.BA.E4.BE.8B1-.E6.B7.BB.E5.8A.A0.E7.9B.B4.E6.92.AD.E6.8B.89.E6.B5.81.E8.BE.93.E5.85.A5.E6.BA.90)；
        	- 添加直播推流输入源，参见 [示例2](#.E7.A4.BA.E4.BE.8B2-.E6.B7.BB.E5.8A.A0.E7.9B.B4.E6.92.AD.E6.8E.A8.E6.B5.81.E8.BE.93.E5.85.A5.E6.BA.90)；
        	- 添加点播拉流输入源，参见 [示例3](#.E7.A4.BA.E4.BE.8B3-.E6.B7.BB.E5.8A.A0.E7.82.B9.E6.92.AD.E6.8B.89.E6.B5.81.E8.BE.93.E5.85.A5.E6.BA.90.E4.B8.94.E5.BE.AA.E7.8E.AF.E6.92.AD.E6.94.BE)、[示例4](#.E7.A4.BA.E4.BE.8B4-.E6.B7.BB.E5.8A.A0.E7.82.B9.E6.92.AD.E6.8B.89.E6.B5.81.E8.BE.93.E5.85.A5.E6.BA.90.E4.B8.94.E5.8D.95.E6.AC.A1.E6.92.AD.E6.94.BE)；
        - `DeleteInput`（删除输入源），参见 [示例5](#.E7.A4.BA.E4.BE.8B5-.E5.88.A0.E9.99.A4.E8.BE.93.E5.85.A5.E6.BA.90)；
        - `ModifyInput`（修改输入源），参见 [示例6](#.E7.A4.BA.E4.BE.8B6-.E4.BF.AE.E6.94.B9.E8.BE.93.E5.85.A5.E6.BA.90)；
        - `AddOutput`（ 添加输出源），参见 [示例7](#.E7.A4.BA.E4.BE.8B7-.E6.B7.BB.E5.8A.A0.E8.BE.93.E5.87.BA.E6.BA.90)；
        - `DeleteOutput`（删除输出源），参见 [示例8](#.E7.A4.BA.E4.BE.8B8-.E5.88.A0.E9.99.A4.E8.BE.93.E5.87.BA.E6.BA.90)；
        - `ModifyOutput`（修改输出源），参见 [示例9](#.E7.A4.BA.E4.BE.8B9-.E4.BF.AE.E6.94.B9.E8.BE.93.E5.87.BA.E6.BA.90)；
        - `Start`（开启转推），参见 [示例10](#.E7.A4.BA.E4.BE.8B10-.E5.BC.80.E5.90.AF.E4.BA.91.E8.BD.AC.E6.8E.A8)；
        - `Stop`（停止转推），参见 [示例11](#.E7.A4.BA.E4.BE.8B11-.E5.81.9C.E6.AD.A2.E4.BA.91.E8.BD.AC.E6.8E.A8)；
        - `SwitchInput`（切换输入源），参见 [示例12](#.E7.A4.BA.E4.BE.8B12-.E5.88.87.E6.8D.A2.E8.BE.93.E5.85.A5.E6.BA.90)；
        - `ModifyCurrentStopTime`（修改当前计划结束时间），参见 [示例13](#.E7.A4.BA.E4.BE.8B13-.E4.BF.AE.E6.94.B9.E8.BD.AC.E6.8E.A8.E7.BB.93.E6.9D.9F.E6.97.B6.E9.97.B4)。

        :param request: Request instance for HandleStreamConnectProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.HandleStreamConnectProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.HandleStreamConnectProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("HandleStreamConnectProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.HandleStreamConnectProjectResponse()
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
        """将云点播媒资文件导入到云剪媒体资源库。

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
        """将云点播中的媒资或者用户自有媒资文件添加到媒体库中，跟项目关联，供后续视频编辑使用。目前仅普通编辑项目和智能视频拆条项目有效。

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
        """浏览当前分类路径下的资源，包括媒体文件和子分类，返回媒资基础信息和分类信息。

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
        """修改媒体信息，支持修改媒体名称、分类路径、标签等信息。

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
        如果 SourceClassPath = /素材/视频/NBA，DestinationClassPath = /素材/视频/篮球
        <li>当 DestinationClassPath 不存在时候，操作结果为重命名 ClassPath；</li>
        <li>当 DestinationClassPath 存在时候，操作结果为产生新目录 /素材/视频/篮球/NBA</li>

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


    def MoveResource(self, request):
        """移动资源，支持跨个人或团队移动媒体以及分类。如果填写了Operator，则需要校验用户对媒体和分类资源的访问以及写权限。
        <li>当原始资源为媒体时，该接口效果为将该媒体移动到目标分类下面；</li>
        <li>当原始资源为分类时，该接口效果为将原始分类移动到目标分类或者是重命名。</li>
         如果 SourceResource.Resource.Id = /素材/视频/NBA，DestinationResource.Resource.Id= /素材/视频/篮球
        <li>当 DestinationResource.Resource.Id 不存在时候且原始资源与目标资源归属相同，操作结果为重命名原始分类；</li>
        <li>当 DestinationResource.Resource.Id 存在时候，操作结果为产生新目录 /素材/视频/篮球/NBA</li>

        :param request: Request instance for MoveResource.
        :type request: :class:`tencentcloud.cme.v20191029.models.MoveResourceRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.MoveResourceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MoveResource", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MoveResourceResponse()
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
        """根据检索条件搜索媒体，返回媒体的基本信息。

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