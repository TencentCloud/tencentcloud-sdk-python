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
from tencentcloud.cme.v20191029 import models


class CmeClient(AbstractClient):
    _apiVersion = '2019-10-29'
    _endpoint = 'cme.tencentcloudapi.com'
    _service = 'cme'


    def AddTeamMember(self, request):
        """向一个团队中添加团队成员，并且指定成员的角色。

        :param request: Request instance for AddTeamMember.
        :type request: :class:`tencentcloud.cme.v20191029.models.AddTeamMemberRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.AddTeamMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddTeamMember", params, headers=headers)
            response = json.loads(body)
            model = models.AddTeamMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyProject(self, request):
        """复制一个项目，包括项目素材及轨道数据。目前仅普通剪辑及模板制作项目可复制，其它类型的项目不支持复制。

        :param request: Request instance for CopyProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.CopyProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CopyProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyProject", params, headers=headers)
            response = json.loads(body)
            model = models.CopyProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClass(self, request):
        """新增分类，用于管理素材。分类层数不能超过20。

        :param request: Request instance for CreateClass.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateClassRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClass", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLink(self, request):
        """创建媒体链接或分类路径链接，将资源信息链接到目标。

        :param request: Request instance for CreateLink.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateLinkRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateLinkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLink", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLinkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProject(self, request):
        """创建多媒体创作引擎项目，目前支持的项目类型有：
        <li>视频剪辑项目：用于普通视频剪辑；</li>
        <li>直播剪辑项目：用于直播流剪辑；</li>
        <li>导播台项目：用于云导播台；</li>
        <li>视频拆条：用于视频拆条；</li>
        <li>录制回放项目：用于直播录制回放；</li>
        <li>媒体转推项目：用于媒体文件转直播输出。</li>

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateProjectResponse`

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


    def CreateTeam(self, request):
        """创建一个团队。

        :param request: Request instance for CreateTeam.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateTeamRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTeam", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoEncodingPreset(self, request):
        """指定导出的参数，创建一个视频编码配置

        :param request: Request instance for CreateVideoEncodingPreset.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateVideoEncodingPresetRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateVideoEncodingPresetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoEncodingPreset", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoEncodingPresetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("DeleteClass", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoginStatus(self, request):
        """删除用户登录态，使用户登出多媒体创作引擎平台。

        :param request: Request instance for DeleteLoginStatus.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteLoginStatusRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteLoginStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoginStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoginStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMaterial(self, request):
        """根据媒体 Id 删除媒体。

        :param request: Request instance for DeleteMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteMaterialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMaterial", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMaterialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        """删除项目。处于推流状态的云转推和点播转直播项目不允许删除，若强行调用删除项目接口会返回失败。

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteProjectResponse`

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


    def DeleteTeam(self, request):
        """删除一个团队。要删除团队，必须满足以下条件：
        <li>要删除的团队必须没有归属的素材；</li>
        <li>要删除的团队必须没有归属的分类。</li>

        :param request: Request instance for DeleteTeam.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteTeamRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTeam", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTeamMembers(self, request):
        """将团队成员从团队中删除。

        :param request: Request instance for DeleteTeamMembers.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteTeamMembersRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteTeamMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTeamMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTeamMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVideoEncodingPreset(self, request):
        """删除指定 ID 的视频编码配置

        :param request: Request instance for DeleteVideoEncodingPreset.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteVideoEncodingPresetRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteVideoEncodingPresetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVideoEncodingPreset", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVideoEncodingPresetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccounts(self, request):
        """获取平台中所有的已注册账号。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClass(self, request):
        """获取指定归属者下所有的分类信息。

        :param request: Request instance for DescribeClass.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeClassRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClass", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJoinTeams(self, request):
        """获取用户所加入的团队列表

        :param request: Request instance for DescribeJoinTeams.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeJoinTeamsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeJoinTeamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJoinTeams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJoinTeamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginStatus(self, request):
        """查询指定用户的登录态。

        :param request: Request instance for DescribeLoginStatus.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeLoginStatusRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeLoginStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMaterials(self, request):
        """根据媒体 Id 批量获取媒体详情。

        :param request: Request instance for DescribeMaterials.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeMaterialsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeMaterialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaterials", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaterialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlatforms(self, request):
        """<li>支持获取所创建的所有平台列表信息；</li>
        <li>支持获取指定的平台列表信息。</li>

        关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。

        :param request: Request instance for DescribePlatforms.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribePlatformsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribePlatformsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlatforms", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlatformsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjects(self, request):
        """支持根据多种条件过滤出项目列表。

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceAuthorization(self, request):
        """查询资源被授权的情况。

        :param request: Request instance for DescribeResourceAuthorization.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeResourceAuthorizationRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeResourceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceAuthorization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceAuthorizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSharedSpace(self, request):
        """获取共享空间。当个人或团队A对个人或团队B授权某资源以后，个人或团队B的共享空间就会增加个人或团队A。

        :param request: Request instance for DescribeSharedSpace.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeSharedSpaceRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeSharedSpaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSharedSpace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSharedSpaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        """获取任务列表，支持条件筛选，返回对应的任务基础信息列表。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTeamMembers(self, request):
        """获取指定团队的成员信息。支持获取指定成员的信息，同时也支持分页拉取指定团队的所有成员信息。

        :param request: Request instance for DescribeTeamMembers.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTeamMembersRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTeamMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTeamMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTeamMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTeams(self, request):
        """获取指定团队的信息，拉取团队信息列表。

        :param request: Request instance for DescribeTeams.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTeamsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTeamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTeams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTeamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoEncodingPresets(self, request):
        """查询视频编码配置信息。

        :param request: Request instance for DescribeVideoEncodingPresets.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeVideoEncodingPresetsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeVideoEncodingPresetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoEncodingPresets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoEncodingPresetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVideoByEditorTrackData(self, request):
        """使用 [视频合成协议](https://cloud.tencent.com/document/product/1156/51225) 合成视频，支持导出视频到 CME 云媒资或者云点播媒资。

        :param request: Request instance for ExportVideoByEditorTrackData.
        :type request: :class:`tencentcloud.cme.v20191029.models.ExportVideoByEditorTrackDataRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExportVideoByEditorTrackDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVideoByEditorTrackData", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVideoByEditorTrackDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVideoByTemplate(self, request):
        """使用视频剪辑模板直接导出视频。

        :param request: Request instance for ExportVideoByTemplate.
        :type request: :class:`tencentcloud.cme.v20191029.models.ExportVideoByTemplateRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExportVideoByTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVideoByTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVideoByTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVideoByVideoSegmentationData(self, request):
        """使用视频智能拆条数据导出视频，将指定的视频拆条片段导出为一个视频(内测中，请勿使用)。

        :param request: Request instance for ExportVideoByVideoSegmentationData.
        :type request: :class:`tencentcloud.cme.v20191029.models.ExportVideoByVideoSegmentationDataRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExportVideoByVideoSegmentationDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVideoByVideoSegmentationData", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVideoByVideoSegmentationDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVideoEditProject(self, request):
        """导出视频编辑项目，支持指定输出的模板。

        :param request: Request instance for ExportVideoEditProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ExportVideoEditProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExportVideoEditProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVideoEditProject", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVideoEditProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FlattenListMedia(self, request):
        """平铺分类路径下及其子分类下的所有媒体基础信息，返回当前分类及子分类中的所有媒体的基础信息。

        :param request: Request instance for FlattenListMedia.
        :type request: :class:`tencentcloud.cme.v20191029.models.FlattenListMediaRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.FlattenListMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FlattenListMedia", params, headers=headers)
            response = json.loads(body)
            model = models.FlattenListMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("GenerateVideoSegmentationSchemeByAi", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateVideoSegmentationSchemeByAiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GrantResourceAuthorization(self, request):
        """资源归属者对个人或团队授予目标资源的相应权限。

        :param request: Request instance for GrantResourceAuthorization.
        :type request: :class:`tencentcloud.cme.v20191029.models.GrantResourceAuthorizationRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.GrantResourceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GrantResourceAuthorization", params, headers=headers)
            response = json.loads(body)
            model = models.GrantResourceAuthorizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HandleMediaCastProject(self, request):
        """对媒体转推项目进行操作。
        ### 操作类型<a id="Operation"></a>
        - `AddSource`（添加输入源），项目状态为 Idle、Working 时均可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B6-.E6.B7.BB.E5.8A.A0.E8.BE.93.E5.85.A5.E6.BA.90)；
        - `DeleteSource`（删除输入源），项目状态为 Idle、Working 时均可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B3-.E5.88.A0.E9.99.A4.E8.BE.93.E5.85.A5.E6.BA.90)；
        - `SwitchSource`（切换当前播放的输入源），项目状态为 Working 时可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B13-.E5.88.87.E6.8D.A2.E5.BD.93.E5.89.8D.E6.92.AD.E6.94.BE.E7.9A.84.E8.BE.93.E5.85.A5.E6.BA.90)
        - `AddDestination`（ 添加输出源），项目状态为 Idle、Working 时均可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B7-.E6.B7.BB.E5.8A.A0.E8.BE.93.E5.87.BA.E6.BA.90)；
        - `DeleteDestination`（删除输出源），项目状态为 Idle、Working 时均可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B4-.E5.88.A0.E9.99.A4.E8.BE.93.E5.87.BA.E6.BA.90)；
        - `EnableDestination`（启动输出源），项目状态为 Working 时可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B5-.E5.90.AF.E5.8A.A8.E8.BE.93.E5.87.BA.E6.BA.90)；
        - `DisableDestination`（停止输出源），项目状态为 Working 时可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B2-.E5.81.9C.E6.AD.A2.E8.BE.93.E5.87.BA.E6.BA.90)；
        - `ModifyDestination`（修改输出源），项目状态为 Idle、Working 时均可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B1-.E4.BF.AE.E6.94.B9.E8.BE.93.E5.87.BA.E6.BA.90)；
        - `Start`（启动媒体转推），项目状态为 Idle 时可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B10-.E5.90.AF.E5.8A.A8.E5.AA.92.E4.BD.93.E8.BD.AC.E6.8E.A8)。发起 Start 请求成功后，媒体转推项目开始启动，30秒内还需要再进行一次 Confirm操作进行确认；
        - `Confirm`（确认媒体转推项目启动），项目状态为 Working 时可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B14-.E7.A1.AE.E8.AE.A4.E5.AA.92.E4.BD.93.E8.BD.AC.E6.8E.A8.E9.A1.B9.E7.9B.AE.E5.90.AF.E5.8A.A8)；
        - `Stop`（停止媒体转推），项目状态为 Working 时可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B9-.E5.81.9C.E6.AD.A2.E5.AA.92.E4.BD.93.E8.BD.AC.E6.8E.A8)；
        - `ModifyOutputMediaSetting`（修改媒体输出配置），项目状态为 Idle 时可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B12-.E4.BF.AE.E6.94.B9.E8.BE.93.E5.87.BA.E7.9A.84.E5.AA.92.E4.BD.93.E9.85.8D.E7.BD.AE)；
        - `ModifyPlaySetting`（修改播放结束时间），项目状态为 Idle、Working 时均可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B8-.E4.BF.AE.E6.94.B9.E7.BB.93.E6.9D.9F.E6.97.B6.E9.97.B4);
        - `DescribePlayInfo`（查询播放信息），项目状态为 Idle、Working 时均可以操作。参见 [示例](#.E7.A4.BA.E4.BE.8B15-.E6.9F.A5.E8.AF.A2.E5.AA.92.E4.BD.93.E8.BD.AC.E6.8E.A8.E9.A1.B9.E7.9B.AE.E7.9A.84.E6.92.AD.E6.94.BE.E4.BF.A1.E6.81.AF)。

        :param request: Request instance for HandleMediaCastProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.HandleMediaCastProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.HandleMediaCastProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HandleMediaCastProject", params, headers=headers)
            response = json.loads(body)
            model = models.HandleMediaCastProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HandleStreamConnectProject(self, request):
        """<font color=red>本接口废弃，可创建媒体转推项目替代，操作媒体转推项目可使用 <b>[HandleMediaCastProject 接口](/document/product/1156/87841) </b>实现。</font>

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
        - `ModifyCurrentStopTime`（修改当前计划结束时间），参见 [示例13](#.E7.A4.BA.E4.BE.8B13-.E4.BF.AE.E6.94.B9.E8.BD.AC.E6.8E.A8.E7.BB.93.E6.9D.9F.E6.97.B6.E9.97.B4);
        - `DescribeInputPlayInfo`（查询播放进度），参见 [示例14](#.E7.A4.BA.E4.BE.8B14-.E6.9F.A5.E8.AF.A2.E7.82.B9.E6.92.AD.E8.BE.93.E5.85.A5.E6.BA.90.E6.92.AD.E6.94.BE.E8.BF.9B.E5.BA.A6)。

        :param request: Request instance for HandleStreamConnectProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.HandleStreamConnectProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.HandleStreamConnectProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HandleStreamConnectProject", params, headers=headers)
            response = json.loads(body)
            model = models.HandleStreamConnectProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportMaterial(self, request):
        """将云点播媒资文件导入到多媒体创作引擎媒体资源库。支持导入媒体归属团队或者个人。

        :param request: Request instance for ImportMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.ImportMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ImportMaterialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportMaterial", params, headers=headers)
            response = json.loads(body)
            model = models.ImportMaterialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportMediaToProject(self, request):
        """将云点播中的媒资或者用户自有媒资文件添加到项目中与项目关联，供后续视频编辑使用。目前仅视频编辑项目和智能视频拆条项目有效。

        :param request: Request instance for ImportMediaToProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ImportMediaToProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ImportMediaToProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportMediaToProject", params, headers=headers)
            response = json.loads(body)
            model = models.ImportMediaToProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListMedia(self, request):
        """浏览当前分类路径下的资源，包括媒体文件和子分类，返回媒资基础信息和分类信息。

        :param request: Request instance for ListMedia.
        :type request: :class:`tencentcloud.cme.v20191029.models.ListMediaRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ListMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListMedia", params, headers=headers)
            response = json.loads(body)
            model = models.ListMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMaterial(self, request):
        """修改媒体信息，支持修改媒体名称、分类路径、标签等信息。

        :param request: Request instance for ModifyMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyMaterialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaterial", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMaterialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        """修改项目信息。

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyProjectResponse`

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


    def ModifyTeam(self, request):
        """修改团队信息，目前支持修改的操作有：
        <li>修改团队名称。</li>

        :param request: Request instance for ModifyTeam.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyTeamRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTeam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTeamMember(self, request):
        """修改团队成员信息，包括成员备注、角色等。

        :param request: Request instance for ModifyTeamMember.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyTeamMemberRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyTeamMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTeamMember", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTeamMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVideoEncodingPreset(self, request):
        """修改视频编码配置信息。

        :param request: Request instance for ModifyVideoEncodingPreset.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyVideoEncodingPresetRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyVideoEncodingPresetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVideoEncodingPreset", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVideoEncodingPresetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("MoveClass", params, headers=headers)
            response = json.loads(body)
            model = models.MoveClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("MoveResource", params, headers=headers)
            response = json.loads(body)
            model = models.MoveResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ParseEvent(self, request):
        """该接口接受多媒体创作引擎回调给业务的事件内容，将其转化为对应的 EventContent 结构。请不要实际调用该接口，只需要将接收到的事件内容直接使用 JSON 解析到 EventContent  结构即可使用。

        :param request: Request instance for ParseEvent.
        :type request: :class:`tencentcloud.cme.v20191029.models.ParseEventRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ParseEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ParseEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ParseEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevokeResourceAuthorization(self, request):
        """资源所属实体对目标实体撤销目标资源的相应权限，若原本没有相应权限则不产生变更。

        :param request: Request instance for RevokeResourceAuthorization.
        :type request: :class:`tencentcloud.cme.v20191029.models.RevokeResourceAuthorizationRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.RevokeResourceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokeResourceAuthorization", params, headers=headers)
            response = json.loads(body)
            model = models.RevokeResourceAuthorizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchMaterial(self, request):
        """根据检索条件搜索媒体，返回媒体的基本信息。

        :param request: Request instance for SearchMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.SearchMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.SearchMaterialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchMaterial", params, headers=headers)
            response = json.loads(body)
            model = models.SearchMaterialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))