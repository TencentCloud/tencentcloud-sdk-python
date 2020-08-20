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

from tencentcloud.common.abstract_model import AbstractModel


class AddMemberInfo(AbstractModel):
    """添加的团队成员信息

    """

    def __init__(self):
        """
        :param MemberId: 团队成员 ID。
        :type MemberId: str
        :param Remark: 团队成员备注。
        :type Remark: str
        """
        self.MemberId = None
        self.Remark = None


    def _deserialize(self, params):
        self.MemberId = params.get("MemberId")
        self.Remark = params.get("Remark")


class AddTeamMemberRequest(AbstractModel):
    """AddTeamMember请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TeamId: 团队 ID。
        :type TeamId: str
        :param TeamMembers: 要添加的成员列表，一次最多添加30个成员。
        :type TeamMembers: list of AddMemberInfo
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.TeamMembers = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        if params.get("TeamMembers") is not None:
            self.TeamMembers = []
            for item in params.get("TeamMembers"):
                obj = AddMemberInfo()
                obj._deserialize(item)
                self.TeamMembers.append(obj)
        self.Operator = params.get("Operator")


class AddTeamMemberResponse(AbstractModel):
    """AddTeamMember返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AudioMaterial(AbstractModel):
    """音频素材信息

    """

    def __init__(self):
        """
        :param MetaData: 素材元信息。
        :type MetaData: :class:`tencentcloud.cme.v20191029.models.MediaMetaData`
        :param MaterialUrl: 素材媒体文件的播放 URL 地址。
        :type MaterialUrl: str
        :param CoverUrl: 素材媒体文件的封面图片地址。
        :type CoverUrl: str
        :param MaterialStatus: 素材状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialStatus: :class:`tencentcloud.cme.v20191029.models.MaterialStatus`
        :param OriginalUrl: 素材媒体文件的原始 URL 地址。
        :type OriginalUrl: str
        :param VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        """
        self.MetaData = None
        self.MaterialUrl = None
        self.CoverUrl = None
        self.MaterialStatus = None
        self.OriginalUrl = None
        self.VodFileId = None


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.MaterialUrl = params.get("MaterialUrl")
        self.CoverUrl = params.get("CoverUrl")
        if params.get("MaterialStatus") is not None:
            self.MaterialStatus = MaterialStatus()
            self.MaterialStatus._deserialize(params.get("MaterialStatus"))
        self.OriginalUrl = params.get("OriginalUrl")
        self.VodFileId = params.get("VodFileId")


class AudioStreamInfo(AbstractModel):
    """音频流信息。

    """

    def __init__(self):
        """
        :param Bitrate: 码率，单位：bps。
        :type Bitrate: int
        :param SamplingRate: 采样率，单位：hz。
        :type SamplingRate: int
        :param Codec: 编码格式。
        :type Codec: str
        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")


class AuthorizationInfo(AbstractModel):
    """资源权限信息

    """

    def __init__(self):
        """
        :param Authorizee: 被授权者实体。
        :type Authorizee: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param PermissionSet: 详细授权值。 取值有：
<li>R：可读，可以浏览素材，但不能使用该素材（将其添加到 Project），或复制到自己的媒资库中</li>
<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>
<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>
<li>W：可修改、删除媒资。</li>
        :type PermissionSet: list of str
        """
        self.Authorizee = None
        self.PermissionSet = None


    def _deserialize(self, params):
        if params.get("Authorizee") is not None:
            self.Authorizee = Entity()
            self.Authorizee._deserialize(params.get("Authorizee"))
        self.PermissionSet = params.get("PermissionSet")


class Authorizer(AbstractModel):
    """授权者

    """

    def __init__(self):
        """
        :param Type: 授权者类型，取值有：
<li>PERSON：个人。</li>
<li>TEAM：团队。</li>
        :type Type: str
        :param Id: Id，当 Type=PERSON，取值为用户 Id。当Type=TEAM，取值为团队 ID。
        :type Id: str
        """
        self.Type = None
        self.Id = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")


class CMEExportInfo(AbstractModel):
    """云剪导出信息。

    """

    def __init__(self):
        """
        :param Owner: 导出的归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Name: 导出的素材名称，不得超过30个字符。
        :type Name: str
        :param Description: 导出的素材信息，不得超过50个字符。
        :type Description: str
        :param ClassPath: 导出的素材分类路径，长度不能超过15字符。
        :type ClassPath: str
        :param TagSet: 导出的素材标签，单个标签不得超过10个字符。
        :type TagSet: list of str
        """
        self.Owner = None
        self.Name = None
        self.Description = None
        self.ClassPath = None
        self.TagSet = None


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ClassPath = params.get("ClassPath")
        self.TagSet = params.get("TagSet")


class ClassInfo(AbstractModel):
    """分类信息

    """

    def __init__(self):
        """
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param ClassPath: 分类路径。
        :type ClassPath: str
        """
        self.Owner = None
        self.ClassPath = None


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.ClassPath = params.get("ClassPath")


class CreateClassRequest(AbstractModel):
    """CreateClass请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param ClassPath: 分类路径。
        :type ClassPath: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.ClassPath = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.ClassPath = params.get("ClassPath")
        self.Operator = params.get("Operator")


class CreateClassResponse(AbstractModel):
    """CreateClass返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLinkRequest(AbstractModel):
    """CreateLink请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Type: 链接类型，取值有:
<li>CLASS: 分类链接；</li>
<li> MATERIAL：素材链接。</li>
        :type Type: str
        :param Name: 链接名称，不能超过30个字符。
        :type Name: str
        :param Owner: 链接归属实体。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param DestinationId: 目标资源Id。取值：
<li>当 Type 为 MATERIAL 时填素材 ID；</li>
<li>当 Type 为 CLASS 时填写分类路径。</li>
        :type DestinationId: str
        :param DestinationOwner: 目标资源归属者。
        :type DestinationOwner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param ClassPath: 链接的分类路径，如填"/a/b"则代表链接属于该分类路径，不填则默认为根路径。
        :type ClassPath: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Type = None
        self.Name = None
        self.Owner = None
        self.DestinationId = None
        self.DestinationOwner = None
        self.ClassPath = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.DestinationId = params.get("DestinationId")
        if params.get("DestinationOwner") is not None:
            self.DestinationOwner = Entity()
            self.DestinationOwner._deserialize(params.get("DestinationOwner"))
        self.ClassPath = params.get("ClassPath")
        self.Operator = params.get("Operator")


class CreateLinkResponse(AbstractModel):
    """CreateLink返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialId: 新建链接的素材 Id。
        :type MaterialId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaterialId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Category: 项目类别，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
        :type Category: str
        :param Name: 项目名称，不可超过30个字符。
        :type Name: str
        :param AspectRatio: 画布宽高比，取值有：
<li>16:9；</li>
<li>9:16。</li>
        :type AspectRatio: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        self.Platform = None
        self.Category = None
        self.Name = None
        self.AspectRatio = None
        self.Owner = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Category = params.get("Category")
        self.Name = params.get("Name")
        self.AspectRatio = params.get("AspectRatio")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RequestId = params.get("RequestId")


class CreateTeamRequest(AbstractModel):
    """CreateTeam请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Name: 团队名称，限30个字符。
        :type Name: str
        :param OwnerId: 团队所有者，指定用户 ID。
        :type OwnerId: str
        :param OwnerRemark: 团队所有者的备注，限30个字符。
        :type OwnerRemark: str
        :param TeamId: 自定义团队 ID。创建后不可修改，限20个英文字符及"-"。同时不能以 cmetid_开头。不填会生成默认团队 ID。
        :type TeamId: str
        """
        self.Platform = None
        self.Name = None
        self.OwnerId = None
        self.OwnerRemark = None
        self.TeamId = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Name = params.get("Name")
        self.OwnerId = params.get("OwnerId")
        self.OwnerRemark = params.get("OwnerRemark")
        self.TeamId = params.get("TeamId")


class CreateTeamResponse(AbstractModel):
    """CreateTeam返回参数结构体

    """

    def __init__(self):
        """
        :param TeamId: 创建的团队 ID。
        :type TeamId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TeamId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TeamId = params.get("TeamId")
        self.RequestId = params.get("RequestId")


class DeleteClassRequest(AbstractModel):
    """DeleteClass请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param ClassPath: 分类路径。
        :type ClassPath: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.ClassPath = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.ClassPath = params.get("ClassPath")
        self.Operator = params.get("Operator")


class DeleteClassResponse(AbstractModel):
    """DeleteClass返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoginStatusRequest(AbstractModel):
    """DeleteLoginStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param UserIds: 用户 Id 列表，N 从 0 开始取值，最大 19。
        :type UserIds: list of str
        """
        self.Platform = None
        self.UserIds = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.UserIds = params.get("UserIds")


class DeleteLoginStatusResponse(AbstractModel):
    """DeleteLoginStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMaterialRequest(AbstractModel):
    """DeleteMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.MaterialId = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.MaterialId = params.get("MaterialId")
        self.Operator = params.get("Operator")


class DeleteMaterialResponse(AbstractModel):
    """DeleteMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        """
        self.Platform = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTeamMembersRequest(AbstractModel):
    """DeleteTeamMembers请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TeamId: 团队 ID。
        :type TeamId: str
        :param MemberIds: 要删除的成员列表。
        :type MemberIds: list of str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.MemberIds = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        self.MemberIds = params.get("MemberIds")
        self.Operator = params.get("Operator")


class DeleteTeamMembersResponse(AbstractModel):
    """DeleteTeamMembers返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTeamRequest(AbstractModel):
    """DeleteTeam请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问平台。
        :type Platform: str
        :param TeamId: 要删除的团队  ID。
        :type TeamId: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        self.Operator = params.get("Operator")


class DeleteTeamResponse(AbstractModel):
    """DeleteTeam返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeClassRequest(AbstractModel):
    """DescribeClass请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Operator = params.get("Operator")


class DescribeClassResponse(AbstractModel):
    """DescribeClass返回参数结构体

    """

    def __init__(self):
        """
        :param ClassInfoSet: 分类信息列表。
        :type ClassInfoSet: list of ClassInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClassInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClassInfoSet") is not None:
            self.ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = ClassInfo()
                obj._deserialize(item)
                self.ClassInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeJoinTeamsRequest(AbstractModel):
    """DescribeJoinTeams请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param MemberId: 团队成员　ID。
        :type MemberId: str
        :param Offset: 分页偏移量，默认值：0
        :type Offset: int
        :param Limit: 返回记录条数，默认值：30，最大值：30。
        :type Limit: int
        """
        self.Platform = None
        self.MemberId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.MemberId = params.get("MemberId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeJoinTeamsResponse(AbstractModel):
    """DescribeJoinTeams返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param TeamSet: 团队列表
        :type TeamSet: list of JoinTeamInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TeamSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TeamSet") is not None:
            self.TeamSet = []
            for item in params.get("TeamSet"):
                obj = JoinTeamInfo()
                obj._deserialize(item)
                self.TeamSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoginStatusRequest(AbstractModel):
    """DescribeLoginStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param UserIds: 用户 Id 列表，N 从 0 开始取值，最大 19。
        :type UserIds: list of str
        """
        self.Platform = None
        self.UserIds = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.UserIds = params.get("UserIds")


class DescribeLoginStatusResponse(AbstractModel):
    """DescribeLoginStatus返回参数结构体

    """

    def __init__(self):
        """
        :param LoginStatusInfoSet: 用户登录状态列表。
        :type LoginStatusInfoSet: list of LoginStatusInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoginStatusInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginStatusInfoSet") is not None:
            self.LoginStatusInfoSet = []
            for item in params.get("LoginStatusInfoSet"):
                obj = LoginStatusInfo()
                obj._deserialize(item)
                self.LoginStatusInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMaterialsRequest(AbstractModel):
    """DescribeMaterials请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param MaterialIds: 素材 ID 列表，N 从 0 开始取值，最大 19。
        :type MaterialIds: list of str
        :param Sort: 列表排序，支持下列排序字段：
<li>CreateTime：创建时间；</li>
<li>UpdateTime：更新时间。</li>
        :type Sort: :class:`tencentcloud.cme.v20191029.models.SortBy`
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.MaterialIds = None
        self.Sort = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.MaterialIds = params.get("MaterialIds")
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        self.Operator = params.get("Operator")


class DescribeMaterialsResponse(AbstractModel):
    """DescribeMaterials返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialInfoSet: 素材列表信息。
        :type MaterialInfoSet: list of MaterialInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaterialInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MaterialInfoSet") is not None:
            self.MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self.MaterialInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectIds: 项目 Id 列表，N 从 0 开始取值，最大 19。
        :type ProjectIds: list of str
        :param AspectRatioSet: 画布宽高比集合。
        :type AspectRatioSet: list of str
        :param CategorySet: 项目类别集合。
        :type CategorySet: list of str
        :param Sort: 列表排序，支持下列排序字段：
<li>CreateTime：创建时间；</li>
<li>UpdateTime：更新时间。</li>
        :type Sort: :class:`tencentcloud.cme.v20191029.models.SortBy`
        :param Owner: 项目归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Offset: 分页返回的起始偏移量，默认值：0。
        :type Offset: int
        :param Limit: 分页返回的记录条数，默认值：10。
        :type Limit: int
        """
        self.Platform = None
        self.ProjectIds = None
        self.AspectRatioSet = None
        self.CategorySet = None
        self.Sort = None
        self.Owner = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectIds = params.get("ProjectIds")
        self.AspectRatioSet = params.get("AspectRatioSet")
        self.CategorySet = params.get("CategorySet")
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param ProjectInfoSet: 项目信息列表。
        :type ProjectInfoSet: list of ProjectInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProjectInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProjectInfoSet") is not None:
            self.ProjectInfoSet = []
            for item in params.get("ProjectInfoSet"):
                obj = ProjectInfo()
                obj._deserialize(item)
                self.ProjectInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceAuthorizationRequest(AbstractModel):
    """DescribeResourceAuthorization请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Resource: 资源。
        :type Resource: :class:`tencentcloud.cme.v20191029.models.Resource`
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.Resource = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        if params.get("Resource") is not None:
            self.Resource = Resource()
            self.Resource._deserialize(params.get("Resource"))
        self.Operator = params.get("Operator")


class DescribeResourceAuthorizationResponse(AbstractModel):
    """DescribeResourceAuthorization返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的资源授权记录总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param AuthorizationInfoSet: 授权信息列表。
        :type AuthorizationInfoSet: list of AuthorizationInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AuthorizationInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AuthorizationInfoSet") is not None:
            self.AuthorizationInfoSet = []
            for item in params.get("AuthorizationInfoSet"):
                obj = AuthorizationInfo()
                obj._deserialize(item)
                self.AuthorizationInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSharedSpaceRequest(AbstractModel):
    """DescribeSharedSpace请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Authorizee: 被授权目标实体。
        :type Authorizee: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Authorizee = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Authorizee") is not None:
            self.Authorizee = Entity()
            self.Authorizee._deserialize(params.get("Authorizee"))
        self.Operator = params.get("Operator")


class DescribeSharedSpaceResponse(AbstractModel):
    """DescribeSharedSpace返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 查询到的共享空间总数。
        :type TotalCount: int
        :param AuthorizerSet: 各个共享空间对应的授权者信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizerSet: list of Authorizer
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AuthorizerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AuthorizerSet") is not None:
            self.AuthorizerSet = []
            for item in params.get("AuthorizerSet"):
                obj = Authorizer()
                obj._deserialize(item)
                self.AuthorizerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TaskId: 任务 Id。
        :type TaskId: str
        """
        self.Platform = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TaskId = params.get("TaskId")


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态，取值有：
<li>PROCESSING：处理中：</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :type Status: str
        :param Progress: 任务进度，取值为：0~100。
        :type Progress: int
        :param ErrCode: 错误码。
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param ErrMsg: 错误信息。
        :type ErrMsg: str
        :param TaskType: 任务类型，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：视频编辑项目导出。</li>
        :type TaskType: str
        :param VideoEditProjectOutput: 导出项目输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoEditProjectOutput: :class:`tencentcloud.cme.v20191029.models.VideoEditProjectOutput`
        :param CreateTime: 创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Progress = None
        self.ErrCode = None
        self.ErrMsg = None
        self.TaskType = None
        self.VideoEditProjectOutput = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        self.TaskType = params.get("TaskType")
        if params.get("VideoEditProjectOutput") is not None:
            self.VideoEditProjectOutput = VideoEditProjectOutput()
            self.VideoEditProjectOutput._deserialize(params.get("VideoEditProjectOutput"))
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param TaskTypeSet: 任务类型集合，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：视频编辑项目导出。</li>
        :type TaskTypeSet: list of str
        :param StatusSet: 任务状态集合，取值有：
<li>PROCESSING：处理中；</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :type StatusSet: list of str
        :param Offset: 分页返回的起始偏移量，默认值：0。
        :type Offset: int
        :param Limit: 分页返回的记录条数，默认值：10。
        :type Limit: int
        """
        self.Platform = None
        self.ProjectId = None
        self.TaskTypeSet = None
        self.StatusSet = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.TaskTypeSet = params.get("TaskTypeSet")
        self.StatusSet = params.get("StatusSet")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合搜索条件的记录总数。
        :type TotalCount: int
        :param TaskBaseInfoSet: 任务基础信息列表。
        :type TaskBaseInfoSet: list of TaskBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskBaseInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskBaseInfoSet") is not None:
            self.TaskBaseInfoSet = []
            for item in params.get("TaskBaseInfoSet"):
                obj = TaskBaseInfo()
                obj._deserialize(item)
                self.TaskBaseInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTeamMembersRequest(AbstractModel):
    """DescribeTeamMembers请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TeamId: 团队 ID。
        :type TeamId: str
        :param MemberIds: 成员 ID 列表，限指定30个指定成员。
        :type MemberIds: list of str
        :param Offset: 分页偏移量，默认值：0
        :type Offset: int
        :param Limit: 返回记录条数，默认值：30，最大值：30。
        :type Limit: int
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.MemberIds = None
        self.Offset = None
        self.Limit = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        self.MemberIds = params.get("MemberIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operator = params.get("Operator")


class DescribeTeamMembersResponse(AbstractModel):
    """DescribeTeamMembers返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param MemberSet: 团队成员列表。
        :type MemberSet: list of TeamMemberInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MemberSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MemberSet") is not None:
            self.MemberSet = []
            for item in params.get("MemberSet"):
                obj = TeamMemberInfo()
                obj._deserialize(item)
                self.MemberSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTeamsRequest(AbstractModel):
    """DescribeTeams请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TeamIds: 团队 ID 列表，限30个。
        :type TeamIds: list of str
        """
        self.Platform = None
        self.TeamIds = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamIds = params.get("TeamIds")


class DescribeTeamsResponse(AbstractModel):
    """DescribeTeams返回参数结构体

    """

    def __init__(self):
        """
        :param TeamSet: 团队列表。
        :type TeamSet: list of TeamInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TeamSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TeamSet") is not None:
            self.TeamSet = []
            for item in params.get("TeamSet"):
                obj = TeamInfo()
                obj._deserialize(item)
                self.TeamSet.append(obj)
        self.RequestId = params.get("RequestId")


class Entity(AbstractModel):
    """用于描述资源的归属实体。

    """

    def __init__(self):
        """
        :param Type: 类型，取值有：
<li>PERSON：个人。</li>
<li>TEAM：团队。</li>
        :type Type: str
        :param Id: Id，当 Type=PERSON，取值为用户 Id，当 Type=TEAM，取值为团队 Id。
        :type Id: str
        """
        self.Type = None
        self.Id = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")


class ExportVideoByEditorTrackDataRequest(AbstractModel):
    """ExportVideoByEditorTrackData请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Definition: 导出模板 Id，目前不支持自定义创建，只支持下面的预置模板 Id。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :type Definition: int
        :param ExportDestination: 导出目标。
<li>CME：云剪，即导出为云剪素材；</li>
<li>VOD：云点播，即导出为云点播媒资。</li>
        :type ExportDestination: str
        :param TrackData: 在线编辑轨道数据。
        :type TrackData: str
        :param CMEExportInfo: 导出的云剪素材信息。指定 ExportDestination = CME 时有效。
        :type CMEExportInfo: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        :param VODExportInfo: 导出的云点播媒资信息。指定 ExportDestination = VOD 时有效。
        :type VODExportInfo: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Definition = None
        self.ExportDestination = None
        self.TrackData = None
        self.CMEExportInfo = None
        self.VODExportInfo = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Definition = params.get("Definition")
        self.ExportDestination = params.get("ExportDestination")
        self.TrackData = params.get("TrackData")
        if params.get("CMEExportInfo") is not None:
            self.CMEExportInfo = CMEExportInfo()
            self.CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self.VODExportInfo = VODExportInfo()
            self.VODExportInfo._deserialize(params.get("VODExportInfo"))
        self.Operator = params.get("Operator")


class ExportVideoByEditorTrackDataResponse(AbstractModel):
    """ExportVideoByEditorTrackData返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 Id。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportVideoEditProjectRequest(AbstractModel):
    """ExportVideoEditProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param Definition: 导出模板 Id，目前不支持自定义创建，只支持下面的预置模板 Id。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :type Definition: int
        :param ExportDestination: 导出目标。
<li>CME：云剪，即导出为云剪素材；</li>
<li>VOD：云点播，即导出为云点播媒资。</li>
        :type ExportDestination: str
        :param CMEExportInfo: 导出的云剪素材信息。指定 ExportDestination = CME 时有效。
        :type CMEExportInfo: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        :param VODExportInfo: 导出的云点播媒资信息。指定 ExportDestination = VOD 时有效。
        :type VODExportInfo: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        """
        self.Platform = None
        self.ProjectId = None
        self.Definition = None
        self.ExportDestination = None
        self.CMEExportInfo = None
        self.VODExportInfo = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Definition = params.get("Definition")
        self.ExportDestination = params.get("ExportDestination")
        if params.get("CMEExportInfo") is not None:
            self.CMEExportInfo = CMEExportInfo()
            self.CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self.VODExportInfo = VODExportInfo()
            self.VODExportInfo._deserialize(params.get("VODExportInfo"))


class ExportVideoEditProjectResponse(AbstractModel):
    """ExportVideoEditProject返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 Id。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class FlattenListMediaRequest(AbstractModel):
    """FlattenListMedia请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ClassPath: 素材分类路径，例如填写"/a/b"，则代表平铺该分类路径下及其子分类路径下的素材信息。
        :type ClassPath: str
        :param Owner: 素材路径的归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：50。
        :type Limit: int
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.ClassPath = None
        self.Owner = None
        self.Offset = None
        self.Limit = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ClassPath = params.get("ClassPath")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operator = params.get("Operator")


class FlattenListMediaResponse(AbstractModel):
    """FlattenListMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param MaterialInfoSet: 该分类路径下及其子分类下的所有素材。
        :type MaterialInfoSet: list of MaterialInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MaterialInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MaterialInfoSet") is not None:
            self.MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self.MaterialInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class GrantResourceAuthorizationRequest(AbstractModel):
    """GrantResourceAuthorization请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Owner: 资源所属实体。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Resources: 被授权资源。
        :type Resources: list of Resource
        :param Authorizees: 被授权目标实体。
        :type Authorizees: list of Entity
        :param Permissions: 详细授权值。 取值有：
<li>R：可读，可以浏览素材，但不能使用该素材（将其添加到 Project），或复制到自己的媒资库中</li>
<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>
<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>
<li>W：可修改、删除媒资。</li>
        :type Permissions: list of str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.Resources = None
        self.Authorizees = None
        self.Permissions = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        if params.get("Authorizees") is not None:
            self.Authorizees = []
            for item in params.get("Authorizees"):
                obj = Entity()
                obj._deserialize(item)
                self.Authorizees.append(obj)
        self.Permissions = params.get("Permissions")
        self.Operator = params.get("Operator")


class GrantResourceAuthorizationResponse(AbstractModel):
    """GrantResourceAuthorization返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImageMaterial(AbstractModel):
    """图片素材信息

    """

    def __init__(self):
        """
        :param Height: 图片高度，单位：px。
        :type Height: int
        :param Width: 图片宽度，单位：px。
        :type Width: int
        :param MaterialUrl: 素材媒体文件的展示 URL 地址。
        :type MaterialUrl: str
        :param Size: 图片大小，单位：字节。
        :type Size: int
        :param OriginalUrl: 素材媒体文件的原始 URL 地址。
        :type OriginalUrl: str
        :param VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        """
        self.Height = None
        self.Width = None
        self.MaterialUrl = None
        self.Size = None
        self.OriginalUrl = None
        self.VodFileId = None


    def _deserialize(self, params):
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.MaterialUrl = params.get("MaterialUrl")
        self.Size = params.get("Size")
        self.OriginalUrl = params.get("OriginalUrl")
        self.VodFileId = params.get("VodFileId")


class ImportMaterialRequest(AbstractModel):
    """ImportMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        :param Owner: 素材归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Name: 素材名称，不能超过30个字符。
        :type Name: str
        :param ClassPath: 素材分类路径，形如："/a/b"，层级数不能超过10，每个层级长度不能超过15字符。若不填则默认为根路径。
        :type ClassPath: str
        :param PreProcessDefinition: 素材预处理任务模板 ID。取值：
<li>10：进行编辑预处理。</li>
        :type PreProcessDefinition: int
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.VodFileId = None
        self.Owner = None
        self.Name = None
        self.ClassPath = None
        self.PreProcessDefinition = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.VodFileId = params.get("VodFileId")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.ClassPath = params.get("ClassPath")
        self.PreProcessDefinition = params.get("PreProcessDefinition")
        self.Operator = params.get("Operator")


class ImportMaterialResponse(AbstractModel):
    """ImportMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param PreProcessTaskId: 素材预处理任务 ID，如果未指定发起预处理任务则为空。
        :type PreProcessTaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaterialId = None
        self.PreProcessTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.PreProcessTaskId = params.get("PreProcessTaskId")
        self.RequestId = params.get("RequestId")


class ImportMediaToProjectRequest(AbstractModel):
    """ImportMediaToProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        :param Name: 素材名称，不能超过30个字符。
        :type Name: str
        :param PreProcessDefinition: 素材预处理任务模板 ID，取值：
<li>10：进行编辑预处理。</li>
注意：如果填0则不进行处理。
        :type PreProcessDefinition: int
        """
        self.Platform = None
        self.ProjectId = None
        self.VodFileId = None
        self.Name = None
        self.PreProcessDefinition = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.VodFileId = params.get("VodFileId")
        self.Name = params.get("Name")
        self.PreProcessDefinition = params.get("PreProcessDefinition")


class ImportMediaToProjectResponse(AbstractModel):
    """ImportMediaToProject返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param TaskId: 素材预处理任务 ID，如果未指定发起预处理任务则为空。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaterialId = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class IntegerRange(AbstractModel):
    """整型范围

    """

    def __init__(self):
        """
        :param LowerBound: 按整形代表值的下限检索。
        :type LowerBound: int
        :param UpperBound: 按整形代表值的上限检索。
        :type UpperBound: int
        """
        self.LowerBound = None
        self.UpperBound = None


    def _deserialize(self, params):
        self.LowerBound = params.get("LowerBound")
        self.UpperBound = params.get("UpperBound")


class JoinTeamInfo(AbstractModel):
    """加入的团队信息

    """

    def __init__(self):
        """
        :param TeamId: 团队 ID。
        :type TeamId: str
        :param Name: 团队名称。
        :type Name: str
        :param MemberCount: 团队成员个数
        :type MemberCount: int
        :param Role: 成员在团队中的角色，取值有：
<li>Owner：团队所有者，添加团队成员及修改团队成员解决时不能填此角色；</li>
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :type Role: str
        """
        self.TeamId = None
        self.Name = None
        self.MemberCount = None
        self.Role = None


    def _deserialize(self, params):
        self.TeamId = params.get("TeamId")
        self.Name = params.get("Name")
        self.MemberCount = params.get("MemberCount")
        self.Role = params.get("Role")


class LinkMaterial(AbstractModel):
    """链接类型的素材信息

    """

    def __init__(self):
        """
        :param LinkType: 链接类型取值:
<li>CLASS: 分类链接;</li>
<li> MATERIAL：素材链接。</li>
        :type LinkType: str
        :param LinkStatus: 链接状态取值：
<li> Normal：正常 ；</li>
<li>NotFound：链接目标不存在；</li> <li>Forbidden：无权限。</li>
        :type LinkStatus: str
        :param LinkMaterialInfo: 素材链接详细信息，当LinkType="MATERIAL"时有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkMaterialInfo: :class:`tencentcloud.cme.v20191029.models.LinkMaterialInfo`
        :param LinkClassInfo: 分类链接目标信息，当LinkType=“CLASS”时有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkClassInfo: :class:`tencentcloud.cme.v20191029.models.ClassInfo`
        """
        self.LinkType = None
        self.LinkStatus = None
        self.LinkMaterialInfo = None
        self.LinkClassInfo = None


    def _deserialize(self, params):
        self.LinkType = params.get("LinkType")
        self.LinkStatus = params.get("LinkStatus")
        if params.get("LinkMaterialInfo") is not None:
            self.LinkMaterialInfo = LinkMaterialInfo()
            self.LinkMaterialInfo._deserialize(params.get("LinkMaterialInfo"))
        if params.get("LinkClassInfo") is not None:
            self.LinkClassInfo = ClassInfo()
            self.LinkClassInfo._deserialize(params.get("LinkClassInfo"))


class LinkMaterialInfo(AbstractModel):
    """链接素材信息

    """

    def __init__(self):
        """
        :param BasicInfo: 素材基本信息。
        :type BasicInfo: :class:`tencentcloud.cme.v20191029.models.MaterialBasicInfo`
        :param VideoMaterial: 视频素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoMaterial: :class:`tencentcloud.cme.v20191029.models.VideoMaterial`
        :param AudioMaterial: 音频素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioMaterial: :class:`tencentcloud.cme.v20191029.models.AudioMaterial`
        :param ImageMaterial: 图片素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageMaterial: :class:`tencentcloud.cme.v20191029.models.ImageMaterial`
        """
        self.BasicInfo = None
        self.VideoMaterial = None
        self.AudioMaterial = None
        self.ImageMaterial = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = MaterialBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("VideoMaterial") is not None:
            self.VideoMaterial = VideoMaterial()
            self.VideoMaterial._deserialize(params.get("VideoMaterial"))
        if params.get("AudioMaterial") is not None:
            self.AudioMaterial = AudioMaterial()
            self.AudioMaterial._deserialize(params.get("AudioMaterial"))
        if params.get("ImageMaterial") is not None:
            self.ImageMaterial = ImageMaterial()
            self.ImageMaterial._deserialize(params.get("ImageMaterial"))


class ListMediaRequest(AbstractModel):
    """ListMedia请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ClassPath: 素材分类路径，例如填写"/a/b"，则代表浏览该分类路径下的素材和子分类信息。
        :type ClassPath: str
        :param Owner: 素材和分类的归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：50。
        :type Limit: int
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.ClassPath = None
        self.Owner = None
        self.Offset = None
        self.Limit = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ClassPath = params.get("ClassPath")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operator = params.get("Operator")


class ListMediaResponse(AbstractModel):
    """ListMedia返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialTotalCount: 符合条件的素材记录总数。
        :type MaterialTotalCount: int
        :param MaterialInfoSet: 浏览分类路径下的素材列表信息。
        :type MaterialInfoSet: list of MaterialInfo
        :param ClassInfoSet: 浏览分类路径下的一级子类。
        :type ClassInfoSet: list of ClassInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaterialTotalCount = None
        self.MaterialInfoSet = None
        self.ClassInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaterialTotalCount = params.get("MaterialTotalCount")
        if params.get("MaterialInfoSet") is not None:
            self.MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self.MaterialInfoSet.append(obj)
        if params.get("ClassInfoSet") is not None:
            self.ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = ClassInfo()
                obj._deserialize(item)
                self.ClassInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class LoginStatusInfo(AbstractModel):
    """登录态信息

    """

    def __init__(self):
        """
        :param UserId: 用户 Id。
        :type UserId: str
        :param Status: 用户登录状态。
<li>Online：在线；</li>
<li>Offline：离线。</li>
        :type Status: str
        """
        self.UserId = None
        self.Status = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Status = params.get("Status")


class MaterialBasicInfo(AbstractModel):
    """素材基本信息。

    """

    def __init__(self):
        """
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param MaterialType: 素材类型，取值为：音频（AUDIO）、视频（VIDEO）、图片（IMAGE）、链接（LINK）、字幕 （SUBTITLE）、转场（TRANSITION）、滤镜（FILTER）、文本文字（TEXT）、图文动效（TEXT_IMAGE）。
        :type MaterialType: str
        :param Owner: 素材归属实体。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Name: 素材名称。
        :type Name: str
        :param CreateTime: 素材文件的创建时间，使用 ISO 日期格式。
        :type CreateTime: str
        :param UpdateTime: 素材文件的最近更新时间（如修改视频属性、发起视频处理等会触发更新媒体文件信息的操作），使用 ISO 日期格式。
        :type UpdateTime: str
        :param ClassPath: 素材的分类目录路径。
        :type ClassPath: str
        :param TagInfoSet: 素材绑定的标签信息列表 。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInfoSet: list of MaterialTagInfo
        :param PreviewUrl: 素材媒体文件的预览图。
        :type PreviewUrl: str
        """
        self.MaterialId = None
        self.MaterialType = None
        self.Owner = None
        self.Name = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ClassPath = None
        self.TagInfoSet = None
        self.PreviewUrl = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.MaterialType = params.get("MaterialType")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ClassPath = params.get("ClassPath")
        if params.get("TagInfoSet") is not None:
            self.TagInfoSet = []
            for item in params.get("TagInfoSet"):
                obj = MaterialTagInfo()
                obj._deserialize(item)
                self.TagInfoSet.append(obj)
        self.PreviewUrl = params.get("PreviewUrl")


class MaterialInfo(AbstractModel):
    """素材详情信息

    """

    def __init__(self):
        """
        :param BasicInfo: 素材基本信息。
        :type BasicInfo: :class:`tencentcloud.cme.v20191029.models.MaterialBasicInfo`
        :param VideoMaterial: 视频素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoMaterial: :class:`tencentcloud.cme.v20191029.models.VideoMaterial`
        :param AudioMaterial: 音频素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioMaterial: :class:`tencentcloud.cme.v20191029.models.AudioMaterial`
        :param ImageMaterial: 图片素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageMaterial: :class:`tencentcloud.cme.v20191029.models.ImageMaterial`
        :param LinkMaterial: 链接素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkMaterial: :class:`tencentcloud.cme.v20191029.models.LinkMaterial`
        """
        self.BasicInfo = None
        self.VideoMaterial = None
        self.AudioMaterial = None
        self.ImageMaterial = None
        self.LinkMaterial = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = MaterialBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("VideoMaterial") is not None:
            self.VideoMaterial = VideoMaterial()
            self.VideoMaterial._deserialize(params.get("VideoMaterial"))
        if params.get("AudioMaterial") is not None:
            self.AudioMaterial = AudioMaterial()
            self.AudioMaterial._deserialize(params.get("AudioMaterial"))
        if params.get("ImageMaterial") is not None:
            self.ImageMaterial = ImageMaterial()
            self.ImageMaterial._deserialize(params.get("ImageMaterial"))
        if params.get("LinkMaterial") is not None:
            self.LinkMaterial = LinkMaterial()
            self.LinkMaterial._deserialize(params.get("LinkMaterial"))


class MaterialStatus(AbstractModel):
    """素材的状态，目前仅包含素材编辑可用状态。

    """

    def __init__(self):
        """
        :param EditorUsableStatus: 素材编辑可用状态，取值有：
<li>NORMAL：正常，可直接用于编辑；</li>
<li>ABNORMAL : 异常，不可用于编辑；</li>
<li>PROCESSING：处理中，暂不可用于编辑。</li>
        :type EditorUsableStatus: str
        """
        self.EditorUsableStatus = None


    def _deserialize(self, params):
        self.EditorUsableStatus = params.get("EditorUsableStatus")


class MaterialTagInfo(AbstractModel):
    """素材标签信息

    """

    def __init__(self):
        """
        :param Type: 标签类型，取值为：
<li>PRESET：预置标签；</li>
        :type Type: str
        :param Id: 标签 Id 。当标签类型为 PRESET 时，标签 Id 为预置标签 Id 。
        :type Id: str
        :param Name: 标签名称。
        :type Name: str
        """
        self.Type = None
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")
        self.Name = params.get("Name")


class MediaImageSpriteInfo(AbstractModel):
    """雪碧图

    """

    def __init__(self):
        """
        :param Height: 雪碧图小图的高度。
        :type Height: int
        :param Width: 雪碧图小图的宽度。
        :type Width: int
        :param TotalCount: 雪碧图小图的总数量。
        :type TotalCount: int
        :param ImageUrlSet: 截取雪碧图输出的地址。
        :type ImageUrlSet: list of str
        :param WebVttUrl: 雪碧图子图位置与时间关系的 WebVtt 文件地址。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在雪碧大图里的坐标位置，一般被播放器用于实现预览。
        :type WebVttUrl: str
        """
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImageUrlSet = None
        self.WebVttUrl = None


    def _deserialize(self, params):
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImageUrlSet = params.get("ImageUrlSet")
        self.WebVttUrl = params.get("WebVttUrl")


class MediaMetaData(AbstractModel):
    """文件元信息。

    """

    def __init__(self):
        """
        :param Size: 大小。
        :type Size: int
        :param Container: 容器类型。
        :type Container: str
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
        :type Width: int
        :param Duration: 时长，单位：秒。
        :type Duration: float
        :param Rotate: 视频拍摄时的选择角度，单位：度
        :type Rotate: int
        :param VideoStreamInfoSet: 视频流信息。
        :type VideoStreamInfoSet: list of VideoStreamInfo
        :param AudioStreamInfoSet: 音频流信息。
        :type AudioStreamInfoSet: list of AudioStreamInfo
        """
        self.Size = None
        self.Container = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.Rotate = None
        self.VideoStreamInfoSet = None
        self.AudioStreamInfoSet = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Container = params.get("Container")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        self.Rotate = params.get("Rotate")
        if params.get("VideoStreamInfoSet") is not None:
            self.VideoStreamInfoSet = []
            for item in params.get("VideoStreamInfoSet"):
                obj = VideoStreamInfo()
                obj._deserialize(item)
                self.VideoStreamInfoSet.append(obj)
        if params.get("AudioStreamInfoSet") is not None:
            self.AudioStreamInfoSet = []
            for item in params.get("AudioStreamInfoSet"):
                obj = AudioStreamInfo()
                obj._deserialize(item)
                self.AudioStreamInfoSet.append(obj)


class ModifyMaterialRequest(AbstractModel):
    """ModifyMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param Owner: 素材归属。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Name: 素材名称，不能超过30个字符。
        :type Name: str
        :param ClassPath: 素材分类路径，例如填写"/a/b"，则代表该素材存储的路径为"/a/b"。
        :type ClassPath: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.MaterialId = None
        self.Owner = None
        self.Name = None
        self.ClassPath = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.MaterialId = params.get("MaterialId")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.ClassPath = params.get("ClassPath")
        self.Operator = params.get("Operator")


class ModifyMaterialResponse(AbstractModel):
    """ModifyMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param Name: 项目名称，不可超过30个字符。
        :type Name: str
        :param AspectRatio: 画布宽高比，取值有：
<li>16:9；</li>
<li>9:16。</li>
        :type AspectRatio: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        self.Platform = None
        self.ProjectId = None
        self.Name = None
        self.AspectRatio = None
        self.Owner = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.AspectRatio = params.get("AspectRatio")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTeamMemberRequest(AbstractModel):
    """ModifyTeamMember请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TeamId: 团队 ID。
        :type TeamId: str
        :param MemberId: 团队成员 ID。
        :type MemberId: str
        :param Remark: 成员备注，允许设置备注为空，不为空时长度不能超过15个字符。
        :type Remark: str
        :param Role: 成员角色，取值：
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :type Role: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.MemberId = None
        self.Remark = None
        self.Role = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        self.MemberId = params.get("MemberId")
        self.Remark = params.get("Remark")
        self.Role = params.get("Role")
        self.Operator = params.get("Operator")


class ModifyTeamMemberResponse(AbstractModel):
    """ModifyTeamMember返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTeamRequest(AbstractModel):
    """ModifyTeam请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TeamId: 团队 ID。
        :type TeamId: str
        :param Name: 团队名称，不能超过 30 个字符。
        :type Name: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.Name = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        self.Name = params.get("Name")
        self.Operator = params.get("Operator")


class ModifyTeamResponse(AbstractModel):
    """ModifyTeam返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MoveClassRequest(AbstractModel):
    """MoveClass请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param SourceClassPath: 源分类路径。
        :type SourceClassPath: str
        :param DestinationClassPath: 目标分类路径。
        :type DestinationClassPath: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.SourceClassPath = None
        self.DestinationClassPath = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.SourceClassPath = params.get("SourceClassPath")
        self.DestinationClassPath = params.get("DestinationClassPath")
        self.Operator = params.get("Operator")


class MoveClassResponse(AbstractModel):
    """MoveClass返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProjectInfo(AbstractModel):
    """项目信息。

    """

    def __init__(self):
        """
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param Name: 项目名称。
        :type Name: str
        :param AspectRatio: 画布宽高比。
        :type AspectRatio: str
        :param Category: 项目类别。
        :type Category: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param CoverUrl: 项目封面图片地址。
        :type CoverUrl: str
        :param CreateTime: 项目创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        :param UpdateTime: 项目更新时间，格式按照 ISO 8601 标准表示。
        :type UpdateTime: str
        """
        self.ProjectId = None
        self.Name = None
        self.AspectRatio = None
        self.Category = None
        self.Owner = None
        self.CoverUrl = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.AspectRatio = params.get("AspectRatio")
        self.Category = params.get("Category")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.CoverUrl = params.get("CoverUrl")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class Resource(AbstractModel):
    """用于描述资源

    """

    def __init__(self):
        """
        :param Type: 类型，取值有：
<li>MATERIAL：素材。</li>
<li>CLASS：分类。</li>
        :type Type: str
        :param Id: 资源 Id，当 Type 为 MATERIAL 时，取值为素材 Id；当 Type 为 CLASS 时，取值为分类路径 ClassPath。
        :type Id: str
        """
        self.Type = None
        self.Id = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")


class RevokeResourceAuthorizationRequest(AbstractModel):
    """RevokeResourceAuthorization请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Owner: 资源所属实体。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Resources: 被授权资源。
        :type Resources: list of Resource
        :param Authorizees: 被授权目标实体。
        :type Authorizees: list of Entity
        :param Permissions: 详细授权值。 取值有：
<li>R：可读，可以浏览素材，但不能使用该素材（将其添加到 Project），或复制到自己的媒资库中</li>
<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>
<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>
<li>W：可修改、删除媒资。</li>
        :type Permissions: list of str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.Resources = None
        self.Authorizees = None
        self.Permissions = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        if params.get("Authorizees") is not None:
            self.Authorizees = []
            for item in params.get("Authorizees"):
                obj = Entity()
                obj._deserialize(item)
                self.Authorizees.append(obj)
        self.Permissions = params.get("Permissions")
        self.Operator = params.get("Operator")


class RevokeResourceAuthorizationResponse(AbstractModel):
    """RevokeResourceAuthorization返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchMaterialRequest(AbstractModel):
    """SearchMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param SearchScopes: 指定搜索空间，数组长度不得超过5。
        :type SearchScopes: list of SearchScope
        :param MaterialTypes: 素材类型，取值：
<li>AUDIO：音频；</li>
<li>VIDEO：视频 ；</li>
<li>IMAGE：图片。</li>
        :type MaterialTypes: list of str
        :param Text: 搜索文本，模糊匹配素材名称或描述信息，匹配项越多，匹配度越高，排序越优先。长度限制：15个字符。
        :type Text: str
        :param Resolution: 按画质检索，取值为：LD/SD/HD/FHD/2K/4K。
        :type Resolution: str
        :param DurationRange: 按素材时长检索，单位s。
        :type DurationRange: :class:`tencentcloud.cme.v20191029.models.IntegerRange`
        :param CreateTimeRange: 按照素材创建时间检索。
        :type CreateTimeRange: :class:`tencentcloud.cme.v20191029.models.TimeRange`
        :param Tags: 按标签检索，填入检索的标签名。
        :type Tags: list of str
        :param Sort: 排序方式。Sort.Field 可选值：CreateTime。指定 Text 搜索时，将根据匹配度排序，该字段无效。
        :type Sort: :class:`tencentcloud.cme.v20191029.models.SortBy`
        :param Offset: 偏移量。默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：50。
        :type Limit: int
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.SearchScopes = None
        self.MaterialTypes = None
        self.Text = None
        self.Resolution = None
        self.DurationRange = None
        self.CreateTimeRange = None
        self.Tags = None
        self.Sort = None
        self.Offset = None
        self.Limit = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("SearchScopes") is not None:
            self.SearchScopes = []
            for item in params.get("SearchScopes"):
                obj = SearchScope()
                obj._deserialize(item)
                self.SearchScopes.append(obj)
        self.MaterialTypes = params.get("MaterialTypes")
        self.Text = params.get("Text")
        self.Resolution = params.get("Resolution")
        if params.get("DurationRange") is not None:
            self.DurationRange = IntegerRange()
            self.DurationRange._deserialize(params.get("DurationRange"))
        if params.get("CreateTimeRange") is not None:
            self.CreateTimeRange = TimeRange()
            self.CreateTimeRange._deserialize(params.get("CreateTimeRange"))
        self.Tags = params.get("Tags")
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operator = params.get("Operator")


class SearchMaterialResponse(AbstractModel):
    """SearchMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合记录总条数。
        :type TotalCount: int
        :param MaterialInfoSet: 素材信息，仅返回基础信息。
        :type MaterialInfoSet: list of MaterialInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MaterialInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MaterialInfoSet") is not None:
            self.MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self.MaterialInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class SearchScope(AbstractModel):
    """搜索空间

    """

    def __init__(self):
        """
        :param Owner: 分类路径归属。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param ClassPath: 按分类路径检索。 不填则默认按根分类路径检索。
        :type ClassPath: str
        """
        self.Owner = None
        self.ClassPath = None


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.ClassPath = params.get("ClassPath")


class SortBy(AbstractModel):
    """排序

    """

    def __init__(self):
        """
        :param Field: 排序字段。
        :type Field: str
        :param Order: 排序方式，可选值：Asc（升序）、Desc（降序），默认降序。
        :type Order: str
        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")


class TaskBaseInfo(AbstractModel):
    """任务基础信息。

    """

    def __init__(self):
        """
        :param TaskId: 任务 Id。
        :type TaskId: str
        :param TaskType: 任务类型，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：项目导出。</li>
        :type TaskType: str
        :param Status: 任务状态，取值有：
<li>PROCESSING：处理中：</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :type Status: str
        :param Progress: 任务进度，取值为：0~100。
        :type Progress: int
        :param ErrCode: 错误码。
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param ErrMsg: 错误信息。
        :type ErrMsg: str
        :param CreateTime: 创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        """
        self.TaskId = None
        self.TaskType = None
        self.Status = None
        self.Progress = None
        self.ErrCode = None
        self.ErrMsg = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        self.CreateTime = params.get("CreateTime")


class TeamInfo(AbstractModel):
    """团队信息

    """

    def __init__(self):
        """
        :param TeamId: 团队 ID。
        :type TeamId: str
        :param Name: 团队名称。
        :type Name: str
        :param MemberCount: 团队成员个数
        :type MemberCount: int
        :param CreateTime: 团队创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        :param UpdateTime: 团队最后更新时间，格式按照 ISO 8601 标准表示。
        :type UpdateTime: str
        """
        self.TeamId = None
        self.Name = None
        self.MemberCount = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TeamId = params.get("TeamId")
        self.Name = params.get("Name")
        self.MemberCount = params.get("MemberCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class TeamMemberInfo(AbstractModel):
    """团队成员信息

    """

    def __init__(self):
        """
        :param MemberId: 团队成员 ID。
        :type MemberId: str
        :param Remark: 团队成员备注。
        :type Remark: str
        :param Role: 团队成员角色，取值：
<li>Owner：团队所有者，添加团队成员及修改团队成员解决时不能填此角色；</li>
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :type Role: str
        """
        self.MemberId = None
        self.Remark = None
        self.Role = None


    def _deserialize(self, params):
        self.MemberId = params.get("MemberId")
        self.Remark = params.get("Remark")
        self.Role = params.get("Role")


class TimeRange(AbstractModel):
    """时间范围

    """

    def __init__(self):
        """
        :param StartTime: 开始时间，使用 ISO 日期格式。
        :type StartTime: str
        :param EndTime: 结束时间，使用 ISO 日期格式。
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class VODExportInfo(AbstractModel):
    """云点播导出信息。

    """

    def __init__(self):
        """
        :param Name: 导出的媒资名称。
        :type Name: str
        :param ClassId: 导出的媒资分类 Id。
        :type ClassId: int
        """
        self.Name = None
        self.ClassId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ClassId = params.get("ClassId")


class VideoEditProjectOutput(AbstractModel):
    """项目导出信息。

    """

    def __init__(self):
        """
        :param MaterialId: 导出的云剪素材 MaterialId，仅当导出为云剪素材时有效。
        :type MaterialId: str
        :param VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        :param URL: 导出的媒资 URL。
        :type URL: str
        :param MetaData: 元信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.cme.v20191029.models.MediaMetaData`
        """
        self.MaterialId = None
        self.VodFileId = None
        self.URL = None
        self.MetaData = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.VodFileId = params.get("VodFileId")
        self.URL = params.get("URL")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))


class VideoMaterial(AbstractModel):
    """视频素材信息

    """

    def __init__(self):
        """
        :param MetaData: 素材元信息。
        :type MetaData: :class:`tencentcloud.cme.v20191029.models.MediaMetaData`
        :param ImageSpriteInfo: 雪碧图信息。
        :type ImageSpriteInfo: :class:`tencentcloud.cme.v20191029.models.MediaImageSpriteInfo`
        :param MaterialUrl: 素材媒体文件的播放 URL 地址。
        :type MaterialUrl: str
        :param CoverUrl: 素材媒体文件的封面图片地址。
        :type CoverUrl: str
        :param Resolution: 媒体文件分辨率。取值为：LD/SD/HD/FHD/2K/4K。
        :type Resolution: str
        :param MaterialStatus: 素材状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialStatus: :class:`tencentcloud.cme.v20191029.models.MaterialStatus`
        :param OriginalUrl: 素材媒体文件的原始 URL 地址。
        :type OriginalUrl: str
        :param VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        """
        self.MetaData = None
        self.ImageSpriteInfo = None
        self.MaterialUrl = None
        self.CoverUrl = None
        self.Resolution = None
        self.MaterialStatus = None
        self.OriginalUrl = None
        self.VodFileId = None


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("ImageSpriteInfo") is not None:
            self.ImageSpriteInfo = MediaImageSpriteInfo()
            self.ImageSpriteInfo._deserialize(params.get("ImageSpriteInfo"))
        self.MaterialUrl = params.get("MaterialUrl")
        self.CoverUrl = params.get("CoverUrl")
        self.Resolution = params.get("Resolution")
        if params.get("MaterialStatus") is not None:
            self.MaterialStatus = MaterialStatus()
            self.MaterialStatus._deserialize(params.get("MaterialStatus"))
        self.OriginalUrl = params.get("OriginalUrl")
        self.VodFileId = params.get("VodFileId")


class VideoStreamInfo(AbstractModel):
    """视频流信息。

    """

    def __init__(self):
        """
        :param Bitrate: 码率，单位：bps。
        :type Bitrate: int
        :param Height: 高度，单位：px。
        :type Height: int
        :param Width: 宽度，单位：px。
        :type Width: int
        :param Codec: 编码格式。
        :type Codec: str
        :param Fps: 帧率，单位：hz。
        :type Fps: int
        """
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Codec = None
        self.Fps = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")