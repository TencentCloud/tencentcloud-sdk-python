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
from tencentcloud.cme.v20191029 import models
from typing import Dict


class CmeClient(AbstractClient):
    _apiVersion = '2019-10-29'
    _endpoint = 'cme.tencentcloudapi.com'
    _service = 'cme'

    async def AddTeamMember(
            self,
            request: models.AddTeamMemberRequest,
            opts: Dict = None,
    ) -> models.AddTeamMemberResponse:
        """
        向一个团队中添加团队成员，并且指定成员的角色。
        """
        
        kwargs = {}
        kwargs["action"] = "AddTeamMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddTeamMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyProject(
            self,
            request: models.CopyProjectRequest,
            opts: Dict = None,
    ) -> models.CopyProjectResponse:
        """
        复制一个项目，包括项目素材及轨道数据。目前仅普通剪辑及模板制作项目可复制，其它类型的项目不支持复制。
        """
        
        kwargs = {}
        kwargs["action"] = "CopyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClass(
            self,
            request: models.CreateClassRequest,
            opts: Dict = None,
    ) -> models.CreateClassResponse:
        """
        新增分类，用于管理素材。分类层数不能超过20。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLink(
            self,
            request: models.CreateLinkRequest,
            opts: Dict = None,
    ) -> models.CreateLinkResponse:
        """
        创建媒体链接或分类路径链接，将资源信息链接到目标。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLink"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLinkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        创建多媒体创作引擎项目，目前支持的项目类型有：
        <li>视频剪辑项目：用于普通视频剪辑；</li>
        <li>直播剪辑项目：用于直播流剪辑；</li>
        <li>导播台项目：用于云导播台；</li>
        <li>视频拆条：用于视频拆条；</li>
        <li>录制回放项目：用于直播录制回放；</li>
        <li>媒体转推项目：用于媒体文件转直播输出。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTeam(
            self,
            request: models.CreateTeamRequest,
            opts: Dict = None,
    ) -> models.CreateTeamResponse:
        """
        创建一个团队。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTeam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTeamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoEncodingPreset(
            self,
            request: models.CreateVideoEncodingPresetRequest,
            opts: Dict = None,
    ) -> models.CreateVideoEncodingPresetResponse:
        """
        指定导出的参数，创建一个视频编码配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoEncodingPreset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoEncodingPresetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClass(
            self,
            request: models.DeleteClassRequest,
            opts: Dict = None,
    ) -> models.DeleteClassResponse:
        """
        删除分类信息，删除时检验下述限制：
        <li>分类路径必须存在；</li>
        <li>分类下没有绑定素材。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoginStatus(
            self,
            request: models.DeleteLoginStatusRequest,
            opts: Dict = None,
    ) -> models.DeleteLoginStatusResponse:
        """
        删除用户登录态，使用户登出多媒体创作引擎平台。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoginStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoginStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMaterial(
            self,
            request: models.DeleteMaterialRequest,
            opts: Dict = None,
    ) -> models.DeleteMaterialResponse:
        """
        根据媒体 Id 删除媒体。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        删除项目。处于推流状态的云转推和点播转直播项目不允许删除，若强行调用删除项目接口会返回失败。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTeam(
            self,
            request: models.DeleteTeamRequest,
            opts: Dict = None,
    ) -> models.DeleteTeamResponse:
        """
        删除一个团队。要删除团队，必须满足以下条件：
        <li>要删除的团队必须没有归属的素材；</li>
        <li>要删除的团队必须没有归属的分类。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTeam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTeamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTeamMembers(
            self,
            request: models.DeleteTeamMembersRequest,
            opts: Dict = None,
    ) -> models.DeleteTeamMembersResponse:
        """
        将团队成员从团队中删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTeamMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTeamMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVideoEncodingPreset(
            self,
            request: models.DeleteVideoEncodingPresetRequest,
            opts: Dict = None,
    ) -> models.DeleteVideoEncodingPresetResponse:
        """
        删除指定 ID 的视频编码配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVideoEncodingPreset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVideoEncodingPresetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        获取平台中所有的已注册账号。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClass(
            self,
            request: models.DescribeClassRequest,
            opts: Dict = None,
    ) -> models.DescribeClassResponse:
        """
        获取指定归属者下所有的分类信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJoinTeams(
            self,
            request: models.DescribeJoinTeamsRequest,
            opts: Dict = None,
    ) -> models.DescribeJoinTeamsResponse:
        """
        获取用户所加入的团队列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJoinTeams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJoinTeamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginStatus(
            self,
            request: models.DescribeLoginStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginStatusResponse:
        """
        查询指定用户的登录态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaterials(
            self,
            request: models.DescribeMaterialsRequest,
            opts: Dict = None,
    ) -> models.DescribeMaterialsResponse:
        """
        根据媒体 Id 批量获取媒体详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaterials"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaterialsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlatforms(
            self,
            request: models.DescribePlatformsRequest,
            opts: Dict = None,
    ) -> models.DescribePlatformsResponse:
        """
        <li>支持获取所创建的所有平台列表信息；</li>
        <li>支持获取指定的平台列表信息。</li>

        关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlatforms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlatformsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        支持根据多种条件过滤出项目列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceAuthorization(
            self,
            request: models.DescribeResourceAuthorizationRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceAuthorizationResponse:
        """
        查询资源被授权的情况。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceAuthorization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceAuthorizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSharedSpace(
            self,
            request: models.DescribeSharedSpaceRequest,
            opts: Dict = None,
    ) -> models.DescribeSharedSpaceResponse:
        """
        获取共享空间。当个人或团队A对个人或团队B授权某资源以后，个人或团队B的共享空间就会增加个人或团队A。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSharedSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSharedSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskDetail(
            self,
            request: models.DescribeTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskDetailResponse:
        """
        获取任务详情信息，包含下面几个部分：
        <li>任务基础信息：包括任务状态、错误信息、创建时间等；</li>
        <li>导出项目输出信息：包括输出的素材 Id 等。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        获取任务列表，支持条件筛选，返回对应的任务基础信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTeamMembers(
            self,
            request: models.DescribeTeamMembersRequest,
            opts: Dict = None,
    ) -> models.DescribeTeamMembersResponse:
        """
        获取指定团队的成员信息。支持获取指定成员的信息，同时也支持分页拉取指定团队的所有成员信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTeamMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTeamMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTeams(
            self,
            request: models.DescribeTeamsRequest,
            opts: Dict = None,
    ) -> models.DescribeTeamsResponse:
        """
        获取指定团队的信息，拉取团队信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTeams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTeamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoEncodingPresets(
            self,
            request: models.DescribeVideoEncodingPresetsRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoEncodingPresetsResponse:
        """
        查询视频编码配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoEncodingPresets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoEncodingPresetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVideoByEditorTrackData(
            self,
            request: models.ExportVideoByEditorTrackDataRequest,
            opts: Dict = None,
    ) -> models.ExportVideoByEditorTrackDataResponse:
        """
        使用 [视频合成协议](https://cloud.tencent.com/document/product/1156/51225) 合成视频，支持导出视频到 CME 云媒资或者云点播媒资。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVideoByEditorTrackData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVideoByEditorTrackDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVideoByTemplate(
            self,
            request: models.ExportVideoByTemplateRequest,
            opts: Dict = None,
    ) -> models.ExportVideoByTemplateResponse:
        """
        使用视频剪辑模板直接导出视频。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVideoByTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVideoByTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVideoByVideoSegmentationData(
            self,
            request: models.ExportVideoByVideoSegmentationDataRequest,
            opts: Dict = None,
    ) -> models.ExportVideoByVideoSegmentationDataResponse:
        """
        使用视频智能拆条数据导出视频，将指定的视频拆条片段导出为一个视频(内测中，请勿使用)。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVideoByVideoSegmentationData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVideoByVideoSegmentationDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVideoEditProject(
            self,
            request: models.ExportVideoEditProjectRequest,
            opts: Dict = None,
    ) -> models.ExportVideoEditProjectResponse:
        """
        导出视频编辑项目，支持指定输出的模板。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVideoEditProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVideoEditProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FlattenListMedia(
            self,
            request: models.FlattenListMediaRequest,
            opts: Dict = None,
    ) -> models.FlattenListMediaResponse:
        """
        平铺分类路径下及其子分类下的所有媒体基础信息，返回当前分类及子分类中的所有媒体的基础信息。
        """
        
        kwargs = {}
        kwargs["action"] = "FlattenListMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FlattenListMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateVideoSegmentationSchemeByAi(
            self,
            request: models.GenerateVideoSegmentationSchemeByAiRequest,
            opts: Dict = None,
    ) -> models.GenerateVideoSegmentationSchemeByAiResponse:
        """
        <li>发起视频智能拆条任务，支持智能生成和平精英集锦、王者荣耀集锦、足球集锦、篮球集锦 、人物集锦、新闻拆条等任务。</li>
        <li>和平精英集锦和王者荣耀集锦根据击杀场景进行拆条，足球集锦和篮球集锦根据进球场景进行拆条，人物集锦根据人物人脸特征进行拆条，新闻拆条根据导播进行拆条。</li>
        <li>【本接口内测中，暂不建议使用】</li>
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateVideoSegmentationSchemeByAi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateVideoSegmentationSchemeByAiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GrantResourceAuthorization(
            self,
            request: models.GrantResourceAuthorizationRequest,
            opts: Dict = None,
    ) -> models.GrantResourceAuthorizationResponse:
        """
        资源归属者对个人或团队授予目标资源的相应权限。
        """
        
        kwargs = {}
        kwargs["action"] = "GrantResourceAuthorization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GrantResourceAuthorizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HandleMediaCastProject(
            self,
            request: models.HandleMediaCastProjectRequest,
            opts: Dict = None,
    ) -> models.HandleMediaCastProjectResponse:
        """
        对媒体转推项目进行操作。
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
        """
        
        kwargs = {}
        kwargs["action"] = "HandleMediaCastProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HandleMediaCastProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HandleStreamConnectProject(
            self,
            request: models.HandleStreamConnectProjectRequest,
            opts: Dict = None,
    ) -> models.HandleStreamConnectProjectResponse:
        """
        <font color=red>本接口废弃，可创建媒体转推项目替代，操作媒体转推项目可使用 <b>[HandleMediaCastProject 接口](/document/product/1156/87841) </b>实现。</font>

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
        """
        
        kwargs = {}
        kwargs["action"] = "HandleStreamConnectProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HandleStreamConnectProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportMaterial(
            self,
            request: models.ImportMaterialRequest,
            opts: Dict = None,
    ) -> models.ImportMaterialResponse:
        """
        将云点播媒资文件导入到多媒体创作引擎媒体资源库。支持导入媒体归属团队或者个人。
        """
        
        kwargs = {}
        kwargs["action"] = "ImportMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportMediaToProject(
            self,
            request: models.ImportMediaToProjectRequest,
            opts: Dict = None,
    ) -> models.ImportMediaToProjectResponse:
        """
        将云点播中的媒资或者用户自有媒资文件添加到项目中与项目关联，供后续视频编辑使用。目前仅视频编辑项目和智能视频拆条项目有效。
        """
        
        kwargs = {}
        kwargs["action"] = "ImportMediaToProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportMediaToProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListMedia(
            self,
            request: models.ListMediaRequest,
            opts: Dict = None,
    ) -> models.ListMediaResponse:
        """
        浏览当前分类路径下的资源，包括媒体文件和子分类，返回媒资基础信息和分类信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ListMedia"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListMediaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaterial(
            self,
            request: models.ModifyMaterialRequest,
            opts: Dict = None,
    ) -> models.ModifyMaterialResponse:
        """
        修改媒体信息，支持修改媒体名称、分类路径、标签等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        修改项目信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTeam(
            self,
            request: models.ModifyTeamRequest,
            opts: Dict = None,
    ) -> models.ModifyTeamResponse:
        """
        修改团队信息，目前支持修改的操作有：
        <li>修改团队名称。</li>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTeam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTeamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTeamMember(
            self,
            request: models.ModifyTeamMemberRequest,
            opts: Dict = None,
    ) -> models.ModifyTeamMemberResponse:
        """
        修改团队成员信息，包括成员备注、角色等。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTeamMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTeamMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVideoEncodingPreset(
            self,
            request: models.ModifyVideoEncodingPresetRequest,
            opts: Dict = None,
    ) -> models.ModifyVideoEncodingPresetResponse:
        """
        修改视频编码配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVideoEncodingPreset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVideoEncodingPresetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MoveClass(
            self,
            request: models.MoveClassRequest,
            opts: Dict = None,
    ) -> models.MoveClassResponse:
        """
        移动某一个分类到另外一个分类下，也可用于分类重命名。
        如果 SourceClassPath = /素材/视频/NBA，DestinationClassPath = /素材/视频/篮球
        <li>当 DestinationClassPath 不存在时候，操作结果为重命名 ClassPath；</li>
        <li>当 DestinationClassPath 存在时候，操作结果为产生新目录 /素材/视频/篮球/NBA</li>
        """
        
        kwargs = {}
        kwargs["action"] = "MoveClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MoveClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MoveResource(
            self,
            request: models.MoveResourceRequest,
            opts: Dict = None,
    ) -> models.MoveResourceResponse:
        """
        移动资源，支持跨个人或团队移动媒体以及分类。如果填写了Operator，则需要校验用户对媒体和分类资源的访问以及写权限。
        <li>当原始资源为媒体时，该接口效果为将该媒体移动到目标分类下面；</li>
        <li>当原始资源为分类时，该接口效果为将原始分类移动到目标分类或者是重命名。</li>
         如果 SourceResource.Resource.Id = /素材/视频/NBA，DestinationResource.Resource.Id= /素材/视频/篮球
        <li>当 DestinationResource.Resource.Id 不存在时候且原始资源与目标资源归属相同，操作结果为重命名原始分类；</li>
        <li>当 DestinationResource.Resource.Id 存在时候，操作结果为产生新目录 /素材/视频/篮球/NBA</li>
        """
        
        kwargs = {}
        kwargs["action"] = "MoveResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MoveResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseEvent(
            self,
            request: models.ParseEventRequest,
            opts: Dict = None,
    ) -> models.ParseEventResponse:
        """
        该接口接受多媒体创作引擎回调给业务的事件内容，将其转化为对应的 EventContent 结构。请不要实际调用该接口，只需要将接收到的事件内容直接使用 JSON 解析到 EventContent  结构即可使用。
        """
        
        kwargs = {}
        kwargs["action"] = "ParseEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokeResourceAuthorization(
            self,
            request: models.RevokeResourceAuthorizationRequest,
            opts: Dict = None,
    ) -> models.RevokeResourceAuthorizationResponse:
        """
        资源所属实体对目标实体撤销目标资源的相应权限，若原本没有相应权限则不产生变更。
        """
        
        kwargs = {}
        kwargs["action"] = "RevokeResourceAuthorization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokeResourceAuthorizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchMaterial(
            self,
            request: models.SearchMaterialRequest,
            opts: Dict = None,
    ) -> models.SearchMaterialResponse:
        """
        根据检索条件搜索媒体，返回媒体的基本信息。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)