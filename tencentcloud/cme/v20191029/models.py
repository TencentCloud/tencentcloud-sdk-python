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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AccountInfo(AbstractModel):
    """制作云用户账号信息。

    """

    def __init__(self):
        """
        :param UserId: 用户 Id。
        :type UserId: str
        :param Phone: 用户手机号码。
        :type Phone: str
        :param Nick: 用户昵称。
        :type Nick: str
        :param Status: 账号状态，取值：
<li>Normal：有效；</li>
<li>Stopped：无效。</li>
        :type Status: str
        """
        self.UserId = None
        self.Phone = None
        self.Nick = None
        self.Status = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Phone = params.get("Phone")
        self.Nick = params.get("Nick")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddMemberInfo(AbstractModel):
    """添加的团队成员信息

    """

    def __init__(self):
        """
        :param MemberId: 团队成员 ID。
        :type MemberId: str
        :param Remark: 团队成员备注。
        :type Remark: str
        :param Role: 团队成员角色，不填则默认添加普通成员。可选值：
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AudioTrackItem(AbstractModel):
    """音频轨道上的音频片段信息。

    """

    def __init__(self):
        """
        :param SourceType: 音频媒体来源类型，取值有：
<ul>
<li>VOD ：素材来源于云点播文件 ；</li>
<li>CME ：视频来源于制作云媒体文件 ；</li>
<li>EXTERNAL ：视频来源于媒资绑定。</li>
</ul>
        :type SourceType: str
        :param SourceMedia: 音频片段的媒体来源，可以是：
<ul>
<li>当 SourceType 为 VOD 时，为云点播的媒体文件 FileId ，会默认将该 FileId 导入到项目中 ；</li>
<li>当 SourceType 为 CME 时，为制作云的媒体 ID，项目归属者必须对该云媒资有访问权限；</li>
<li>当 SourceType 为 EXTERNAL 时，为媒资绑定的 Definition 与 MediaKey 中间用冒号分隔合并后的字符串，格式为 Definition:MediaKey 。</li>
</ul>
        :type SourceMedia: str
        :param SourceMediaStartTime: 音频片段取自媒体文件的起始时间，单位为秒。0 表示从媒体开始位置截取。默认为0。
        :type SourceMediaStartTime: float
        :param Duration: 音频片段的时长，单位为秒。默认和媒体本身长度一致，表示截取全部媒体。
        :type Duration: float
        """
        self.SourceType = None
        self.SourceMedia = None
        self.SourceMediaStartTime = None
        self.Duration = None


    def _deserialize(self, params):
        self.SourceType = params.get("SourceType")
        self.SourceMedia = params.get("SourceMedia")
        self.SourceMediaStartTime = params.get("SourceMediaStartTime")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CMEExportInfo(AbstractModel):
    """云剪导出信息。

    """

    def __init__(self):
        """
        :param Owner: 导出媒体归属，个人或团队。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Name: 导出的媒体名称，不得超过30个字符。
        :type Name: str
        :param Description: 导出的媒体信息，不得超过50个字符。
        :type Description: str
        :param ClassPath: 导出的媒体分类路径，长度不能超过15字符。
        :type ClassPath: str
        :param TagSet: 导出的媒体标签，单个标签不得超过10个字符。
        :type TagSet: list of str
        :param ThirdPartyPublishInfos: 第三方平台发布信息列表。暂未正式对外，请勿使用。
        :type ThirdPartyPublishInfos: list of ThirdPartyPublishInfo
        """
        self.Owner = None
        self.Name = None
        self.Description = None
        self.ClassPath = None
        self.TagSet = None
        self.ThirdPartyPublishInfos = None


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ClassPath = params.get("ClassPath")
        self.TagSet = params.get("TagSet")
        if params.get("ThirdPartyPublishInfos") is not None:
            self.ThirdPartyPublishInfos = []
            for item in params.get("ThirdPartyPublishInfos"):
                obj = ThirdPartyPublishInfo()
                obj._deserialize(item)
                self.ThirdPartyPublishInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验分类创建权限。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLinkRequest(AbstractModel):
    """CreateLink请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Type: 链接类型，取值有:
<li>CLASS: 分类链接；</li>
<li> MATERIAL：媒体文件链接。</li>
        :type Type: str
        :param Name: 链接名称，不能超过30个字符。
        :type Name: str
        :param Owner: 链接归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param DestinationId: 目标资源Id。取值：
<li>当 Type 为 MATERIAL 时填媒体 ID；</li>
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLinkResponse(AbstractModel):
    """CreateLink返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialId: 新建链接的媒体 Id。
        :type MaterialId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaterialId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Name: 项目名称，不可超过30个字符。
        :type Name: str
        :param Owner: 项目归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Category: 项目类别，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
<li>SWITCHER：导播台。</li>
<li>VIDEO_SEGMENTATION：视频拆条。</li>
<li>STREAM_CONNECT：云转推。</li>
<li>RECORD_REPLAY：录制回放。</li>
        :type Category: str
        :param Mode: 项目模式，一个项目可以有多种模式并相互切换。
当 Category 为 VIDEO_EDIT 时，可选模式有：
<li>Default：默认模式。</li>
<li>VideoEditTemplate：视频编辑模板制作模式。</li>
        :type Mode: str
        :param AspectRatio: 画布宽高比。
该字段已经废弃，请使用具体项目输入中的 AspectRatio 字段。
        :type AspectRatio: str
        :param Description: 项目描述信息。
        :type Description: str
        :param SwitcherProjectInput: 导播台信息，仅当项目类型为 SWITCHER 时必填。
        :type SwitcherProjectInput: :class:`tencentcloud.cme.v20191029.models.SwitcherProjectInput`
        :param LiveStreamClipProjectInput: 直播剪辑信息，暂未开放，请勿使用。
        :type LiveStreamClipProjectInput: :class:`tencentcloud.cme.v20191029.models.LiveStreamClipProjectInput`
        :param VideoEditProjectInput: 视频编辑信息，仅当项目类型为 VIDEO_EDIT 时必填。
        :type VideoEditProjectInput: :class:`tencentcloud.cme.v20191029.models.VideoEditProjectInput`
        :param VideoSegmentationProjectInput: 视频拆条信息，仅当项目类型为 VIDEO_SEGMENTATION  时必填。
        :type VideoSegmentationProjectInput: :class:`tencentcloud.cme.v20191029.models.VideoSegmentationProjectInput`
        :param StreamConnectProjectInput: 云转推项目信息，仅当项目类型为 STREAM_CONNECT 时必填。
        :type StreamConnectProjectInput: :class:`tencentcloud.cme.v20191029.models.StreamConnectProjectInput`
        :param RecordReplayProjectInput: 录制回放项目信息，仅当项目类型为 RECORD_REPLAY 时必填。
        :type RecordReplayProjectInput: :class:`tencentcloud.cme.v20191029.models.RecordReplayProjectInput`
        """
        self.Platform = None
        self.Name = None
        self.Owner = None
        self.Category = None
        self.Mode = None
        self.AspectRatio = None
        self.Description = None
        self.SwitcherProjectInput = None
        self.LiveStreamClipProjectInput = None
        self.VideoEditProjectInput = None
        self.VideoSegmentationProjectInput = None
        self.StreamConnectProjectInput = None
        self.RecordReplayProjectInput = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Name = params.get("Name")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Category = params.get("Category")
        self.Mode = params.get("Mode")
        self.AspectRatio = params.get("AspectRatio")
        self.Description = params.get("Description")
        if params.get("SwitcherProjectInput") is not None:
            self.SwitcherProjectInput = SwitcherProjectInput()
            self.SwitcherProjectInput._deserialize(params.get("SwitcherProjectInput"))
        if params.get("LiveStreamClipProjectInput") is not None:
            self.LiveStreamClipProjectInput = LiveStreamClipProjectInput()
            self.LiveStreamClipProjectInput._deserialize(params.get("LiveStreamClipProjectInput"))
        if params.get("VideoEditProjectInput") is not None:
            self.VideoEditProjectInput = VideoEditProjectInput()
            self.VideoEditProjectInput._deserialize(params.get("VideoEditProjectInput"))
        if params.get("VideoSegmentationProjectInput") is not None:
            self.VideoSegmentationProjectInput = VideoSegmentationProjectInput()
            self.VideoSegmentationProjectInput._deserialize(params.get("VideoSegmentationProjectInput"))
        if params.get("StreamConnectProjectInput") is not None:
            self.StreamConnectProjectInput = StreamConnectProjectInput()
            self.StreamConnectProjectInput._deserialize(params.get("StreamConnectProjectInput"))
        if params.get("RecordReplayProjectInput") is not None:
            self.RecordReplayProjectInput = RecordReplayProjectInput()
            self.RecordReplayProjectInput._deserialize(params.get("RecordReplayProjectInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param RtmpPushInputInfoSet: 输入源推流信息。
 <li> 当 Catagory 为 STREAM_CONNECT 时，数组返回长度为 2 ，第 0 个代表主输入源，第 1 个代表备输入源。只有当各自输入源类型为推流时才有有效内容。</li>
        :type RtmpPushInputInfoSet: list of RtmpPushInputInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.RtmpPushInputInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        if params.get("RtmpPushInputInfoSet") is not None:
            self.RtmpPushInputInfoSet = []
            for item in params.get("RtmpPushInputInfoSet"):
                obj = RtmpPushInputInfo()
                obj._deserialize(item)
                self.RtmpPushInputInfoSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMaterialRequest(AbstractModel):
    """DeleteMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param MaterialId: 媒体 Id。
        :type MaterialId: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验媒体删除权限。
        :type Operator: str
        """
        self.Platform = None
        self.MaterialId = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.MaterialId = params.get("MaterialId")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验对项目删除操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.ProjectId = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台唯一标识。
        :type Platform: str
        :param Phone: 手机号码。
        :type Phone: str
        :param Offset: 分页返回的起始偏移量，默认值：0。
        :type Offset: int
        :param Limit: 分页返回的记录条数，默认值：10，最大值：20。
        :type Limit: int
        """
        self.Platform = None
        self.Phone = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Phone = params.get("Phone")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合搜索条件的记录总数。
        :type TotalCount: int
        :param AccountInfoSet: 账号信息列表。
        :type AccountInfoSet: list of AccountInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccountInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccountInfoSet") is not None:
            self.AccountInfoSet = []
            for item in params.get("AccountInfoSet"):
                obj = AccountInfo()
                obj._deserialize(item)
                self.AccountInfoSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMaterialsRequest(AbstractModel):
    """DescribeMaterials请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param MaterialIds: 媒体 ID 列表，N 从 0 开始取值，最大 19。
        :type MaterialIds: list of str
        :param Sort: 列表排序，支持下列排序字段：
<li>CreateTime：创建时间；</li>
<li>UpdateTime：更新时间。</li>
        :type Sort: :class:`tencentcloud.cme.v20191029.models.SortBy`
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验媒体的访问权限。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMaterialsResponse(AbstractModel):
    """DescribeMaterials返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialInfoSet: 媒体列表信息。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePlatformsRequest(AbstractModel):
    """DescribePlatforms请求参数结构体

    """

    def __init__(self):
        """
        :param Platforms: 平台集合。
        :type Platforms: list of str
        :param LicenseIds: 平台绑定的 license Id 集合。
        :type LicenseIds: list of str
        :param Offset: 分页返回的起始偏移量，默认值：0。
        :type Offset: int
        :param Limit: 分页返回的记录条数，默认值：10。
        :type Limit: int
        """
        self.Platforms = None
        self.LicenseIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platforms = params.get("Platforms")
        self.LicenseIds = params.get("LicenseIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePlatformsResponse(AbstractModel):
    """DescribePlatforms返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合搜索条件的记录总数。
        :type TotalCount: int
        :param PlatformInfoSet: 平台信息列表。
        :type PlatformInfoSet: list of PlatformInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PlatformInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PlatformInfoSet") is not None:
            self.PlatformInfoSet = []
            for item in params.get("PlatformInfoSet"):
                obj = PlatformInfo()
                obj._deserialize(item)
                self.PlatformInfoSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param CategorySet: 项目类别，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
<li>SWITCHER：导播台。</li>
<li>VIDEO_SEGMENTATION：视频拆条。</li>
<li>STREAM_CONNECT：云转推。</li>
<li>RECORD_REPLAY：录制回放。</li>
        :type CategorySet: list of str
        :param Modes: 项目模式，一个项目可以有多种模式并相互切换。
当 Category 为 VIDEO_EDIT 时，可选模式有：
<li>Default：默认模式。</li>
<li>VideoEditTemplate：视频编辑模板制作模式。</li>
        :type Modes: list of str
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
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验项目访问权限。
        :type Operator: str
        """
        self.Platform = None
        self.ProjectIds = None
        self.AspectRatioSet = None
        self.CategorySet = None
        self.Modes = None
        self.Sort = None
        self.Owner = None
        self.Offset = None
        self.Limit = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectIds = params.get("ProjectIds")
        self.AspectRatioSet = params.get("AspectRatioSet")
        self.CategorySet = params.get("CategorySet")
        self.Modes = params.get("Modes")
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSharedSpaceRequest(AbstractModel):
    """DescribeSharedSpace请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Authorizee: 被授权目标,，个人或团队。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TaskId: 任务 Id。
        :type TaskId: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验对任务的访问权限。
        :type Operator: str
        """
        self.Platform = None
        self.TaskId = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TaskId = params.get("TaskId")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验对任务的访问权限。
        :type Operator: str
        """
        self.Platform = None
        self.ProjectId = None
        self.TaskTypeSet = None
        self.StatusSet = None
        self.Offset = None
        self.Limit = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.TaskTypeSet = params.get("TaskTypeSet")
        self.StatusSet = params.get("StatusSet")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTeamMembersRequest(AbstractModel):
    """DescribeTeamMembers请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TeamId: 团队 ID。
        :type TeamId: str
        :param MemberIds: 成员 ID 列表，限指定30个指定成员。如不填，则返回指定团队下的所有成员。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTeamsRequest(AbstractModel):
    """DescribeTeams请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TeamIds: 团队 ID 列表，限30个。若不填，则默认获取平台下所有团队。
        :type TeamIds: list of str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：20，最大值：30。
        :type Limit: int
        """
        self.Platform = None
        self.TeamIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamIds = params.get("TeamIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTeamsResponse(AbstractModel):
    """DescribeTeams返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param TeamSet: 团队列表。
        :type TeamSet: list of TeamInfo
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
                obj = TeamInfo()
                obj._deserialize(item)
                self.TeamSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EmptyTrackItem(AbstractModel):
    """空的轨道片段，用来进行时间轴的占位。如需要两个音频片段之间有一段时间的静音，可以用 EmptyTrackItem 来进行占位。

    """

    def __init__(self):
        """
        :param Duration: 持续时间，单位为秒。
        :type Duration: float
        """
        self.Duration = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Entity(AbstractModel):
    """用于描述资源的归属，归属者为个人或者团队。

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param TrackData: 在线编辑轨道数据。轨道数据相关介绍，请查看 [视频合成协议](https://cloud.tencent.com/document/product/1156/51225)。
        :type TrackData: str
        :param CMEExportInfo: 导出的云剪素材信息。指定 ExportDestination = CME 时有效。
        :type CMEExportInfo: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        :param VODExportInfo: 导出的云点播媒资信息。指定 ExportDestination = VOD 时有效。
        :type VODExportInfo: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验导出操作权限。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExportVideoByTemplateRequest(AbstractModel):
    """ExportVideoByTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TemplateId: 视频编辑模板  Id。
        :type TemplateId: str
        :param Definition: 导出模板 Id，目前不支持自定义创建，只支持下面的预置模板 Id。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :type Definition: int
        :param ExportDestination: 导出目标，可取值为：
<li>CME：云剪，即导出为云剪媒体；</li>
<li>VOD：云点播，即导出为云点播媒资。</li>
        :type ExportDestination: str
        :param SlotReplacements: 需要替换的素材信息。
        :type SlotReplacements: list of SlotReplacementInfo
        :param CMEExportInfo: 导出的云剪媒体信息。指定 ExportDestination = CME 时有效。
        :type CMEExportInfo: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        :param VODExportInfo: 导出的云点播媒资信息。指定 ExportDestination = VOD 时有效。
        :type VODExportInfo: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验项目导出权限。
        :type Operator: str
        """
        self.Platform = None
        self.TemplateId = None
        self.Definition = None
        self.ExportDestination = None
        self.SlotReplacements = None
        self.CMEExportInfo = None
        self.VODExportInfo = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TemplateId = params.get("TemplateId")
        self.Definition = params.get("Definition")
        self.ExportDestination = params.get("ExportDestination")
        if params.get("SlotReplacements") is not None:
            self.SlotReplacements = []
            for item in params.get("SlotReplacements"):
                obj = SlotReplacementInfo()
                obj._deserialize(item)
                self.SlotReplacements.append(obj)
        if params.get("CMEExportInfo") is not None:
            self.CMEExportInfo = CMEExportInfo()
            self.CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self.VODExportInfo = VODExportInfo()
            self.VODExportInfo._deserialize(params.get("VODExportInfo"))
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExportVideoByTemplateResponse(AbstractModel):
    """ExportVideoByTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 导出任务 Id。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExportVideoByVideoSegmentationDataRequest(AbstractModel):
    """ExportVideoByVideoSegmentationData请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 视频拆条项目 Id 。
        :type ProjectId: str
        :param SegmentGroupId: 指定需要导出的智能拆条片段的组 Id 。
        :type SegmentGroupId: str
        :param SegmentIds: 指定需要导出的智能拆条片段 Id  集合。
        :type SegmentIds: list of str
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
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.ProjectId = None
        self.SegmentGroupId = None
        self.SegmentIds = None
        self.Definition = None
        self.ExportDestination = None
        self.CMEExportInfo = None
        self.VODExportInfo = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.SegmentGroupId = params.get("SegmentGroupId")
        self.SegmentIds = params.get("SegmentIds")
        self.Definition = params.get("Definition")
        self.ExportDestination = params.get("ExportDestination")
        if params.get("CMEExportInfo") is not None:
            self.CMEExportInfo = CMEExportInfo()
            self.CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self.VODExportInfo = VODExportInfo()
            self.VODExportInfo._deserialize(params.get("VODExportInfo"))
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExportVideoByVideoSegmentationDataResponse(AbstractModel):
    """ExportVideoByVideoSegmentationData返回参数结构体

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
<li>CME：云剪，即导出为云剪媒体；</li>
<li>VOD：云点播，即导出为云点播媒资。</li>
        :type ExportDestination: str
        :param CoverData: 视频封面图片文件（如 jpeg, png 等）进行 Base64 编码后的字符串，仅支持 gif、jpeg、png 三种图片格式，原图片文件不能超过2 M大 小。
        :type CoverData: str
        :param CMEExportInfo: 导出的云剪媒体信息。指定 ExportDestination = CME 时有效。
        :type CMEExportInfo: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        :param VODExportInfo: 导出的云点播媒资信息。指定 ExportDestination = VOD 时有效。
        :type VODExportInfo: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验项目导出权限。
        :type Operator: str
        """
        self.Platform = None
        self.ProjectId = None
        self.Definition = None
        self.ExportDestination = None
        self.CoverData = None
        self.CMEExportInfo = None
        self.VODExportInfo = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Definition = params.get("Definition")
        self.ExportDestination = params.get("ExportDestination")
        self.CoverData = params.get("CoverData")
        if params.get("CMEExportInfo") is not None:
            self.CMEExportInfo = CMEExportInfo()
            self.CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self.VODExportInfo = VODExportInfo()
            self.VODExportInfo._deserialize(params.get("VODExportInfo"))
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExternalMediaInfo(AbstractModel):
    """媒资绑定资源信息，包含媒资绑定模板 ID 和文件信息。

    """

    def __init__(self):
        """
        :param Definition: 媒资绑定模板 ID。
        :type Definition: int
        :param MediaKey: 媒资绑定媒体路径或文件 ID。
        :type MediaKey: str
        """
        self.Definition = None
        self.MediaKey = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.MediaKey = params.get("MediaKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FlattenListMediaRequest(AbstractModel):
    """FlattenListMedia请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ClassPath: 媒体分类路径，例如填写"/a/b"，则代表平铺该分类路径下及其子分类路径下的媒体信息。
        :type ClassPath: str
        :param Owner: 媒体分类的归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：50。
        :type Limit: int
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验媒体访问权限。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FlattenListMediaResponse(AbstractModel):
    """FlattenListMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param MaterialInfoSet: 该分类路径下及其子分类下的所有媒体基础信息列表。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GenerateVideoSegmentationSchemeByAiRequest(AbstractModel):
    """GenerateVideoSegmentationSchemeByAi请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 视频拆条项目 Id 。
        :type ProjectId: str
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.ProjectId = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GenerateVideoSegmentationSchemeByAiResponse(AbstractModel):
    """GenerateVideoSegmentationSchemeByAi返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 视频智能拆条任务 Id 。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GrantResourceAuthorizationRequest(AbstractModel):
    """GrantResourceAuthorization请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Owner: 资源归属者，个人或者团队。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Resources: 被授权资源。
        :type Resources: list of Resource
        :param Authorizees: 被授权目标，个人或者团队。
        :type Authorizees: list of Entity
        :param Permissions: 详细授权值。 取值有：
<li>R：可读，可以浏览媒体，但不能使用该媒体文件（将其添加到 Project），或复制到自己的媒资库中</li>
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HandleStreamConnectProjectRequest(AbstractModel):
    """HandleStreamConnectProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 云转推项目Id 。
        :type ProjectId: str
        :param Operation: 请参考 [操作类型](#Operation)
        :type Operation: str
        :param InputInfo: 转推输入源操作参数。具体操作方式详见 [操作类型](#Operation) 及下文示例。
        :type InputInfo: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        :param InputEndpoint: 主备输入源标识，取值有：
<li> Main ：主源；</li>
<li> Backup ：备源。</li>
        :type InputEndpoint: str
        :param OutputInfo: 转推输出源操作参数。具体操作方式详见 [操作类型](#Operation) 及下文示例。
        :type OutputInfo: :class:`tencentcloud.cme.v20191029.models.StreamConnectOutput`
        :param CurrentStopTime: 云转推当前预计结束时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。具体操作方式详见 [操作类型](#Operation) 及下文示例。
        :type CurrentStopTime: str
        """
        self.Platform = None
        self.ProjectId = None
        self.Operation = None
        self.InputInfo = None
        self.InputEndpoint = None
        self.OutputInfo = None
        self.CurrentStopTime = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Operation = params.get("Operation")
        if params.get("InputInfo") is not None:
            self.InputInfo = StreamInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        self.InputEndpoint = params.get("InputEndpoint")
        if params.get("OutputInfo") is not None:
            self.OutputInfo = StreamConnectOutput()
            self.OutputInfo._deserialize(params.get("OutputInfo"))
        self.CurrentStopTime = params.get("CurrentStopTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HandleStreamConnectProjectResponse(AbstractModel):
    """HandleStreamConnectProject返回参数结构体

    """

    def __init__(self):
        """
        :param StreamInputRtmpPushUrl: 输入源推流地址，当 Operation 取值 AddInput 且 InputType 为 RtmpPush 类型时有效。
        :type StreamInputRtmpPushUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StreamInputRtmpPushUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StreamInputRtmpPushUrl = params.get("StreamInputRtmpPushUrl")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImportMaterialRequest(AbstractModel):
    """ImportMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Owner: 媒体归属者，团队或个人。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Name: 媒体名称，不能超过30个字符。
        :type Name: str
        :param SourceType: 导入媒资类型，取值：
<li>VOD：云点播文件；</li>
<li>EXTERNAL：媒资绑定。</li>
注意：如果不填默认为云点播文件。
        :type SourceType: str
        :param VodFileId: 云点播媒资 FileId，仅当 SourceType 为 VOD 时有效。
        :type VodFileId: str
        :param ExternalMediaInfo: 原始媒资文件信息，当 SourceType 取值 EXTERNAL 的时候必填。
        :type ExternalMediaInfo: :class:`tencentcloud.cme.v20191029.models.ExternalMediaInfo`
        :param ClassPath: 媒体分类路径，形如："/a/b"，层级数不能超过10，每个层级长度不能超过15字符。若不填则默认为根路径。
        :type ClassPath: str
        :param PreProcessDefinition: 媒体预处理任务模板 ID。取值：
<li>10：进行编辑预处理。</li>
        :type PreProcessDefinition: int
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.Name = None
        self.SourceType = None
        self.VodFileId = None
        self.ExternalMediaInfo = None
        self.ClassPath = None
        self.PreProcessDefinition = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.SourceType = params.get("SourceType")
        self.VodFileId = params.get("VodFileId")
        if params.get("ExternalMediaInfo") is not None:
            self.ExternalMediaInfo = ExternalMediaInfo()
            self.ExternalMediaInfo._deserialize(params.get("ExternalMediaInfo"))
        self.ClassPath = params.get("ClassPath")
        self.PreProcessDefinition = params.get("PreProcessDefinition")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImportMaterialResponse(AbstractModel):
    """ImportMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialId: 媒体 Id。
        :type MaterialId: str
        :param PreProcessTaskId: 媒体文预处理任务 ID，如果未指定发起预处理任务则为空。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImportMediaToProjectRequest(AbstractModel):
    """ImportMediaToProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param SourceType: 导入媒资类型，取值：
<li>VOD：云点播文件；</li>
<li>EXTERNAL：媒资绑定。</li>
注意：如果不填默认为云点播文件。
        :type SourceType: str
        :param VodFileId: 云点播媒资文件 Id，当 SourceType 取值 VOD 或者缺省的时候必填。
        :type VodFileId: str
        :param ExternalMediaInfo: 原始媒资文件信息，当 SourceType 取值 EXTERNAL 的时候必填。
        :type ExternalMediaInfo: :class:`tencentcloud.cme.v20191029.models.ExternalMediaInfo`
        :param Name: 媒体名称，不能超过30个字符。
        :type Name: str
        :param PreProcessDefinition: 媒体预处理任务模板 ID，取值：
<li>10：进行编辑预处理。</li>
注意：如果填0则不进行处理。
        :type PreProcessDefinition: int
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验项目和媒体文件访问权限。
        :type Operator: str
        """
        self.Platform = None
        self.ProjectId = None
        self.SourceType = None
        self.VodFileId = None
        self.ExternalMediaInfo = None
        self.Name = None
        self.PreProcessDefinition = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.SourceType = params.get("SourceType")
        self.VodFileId = params.get("VodFileId")
        if params.get("ExternalMediaInfo") is not None:
            self.ExternalMediaInfo = ExternalMediaInfo()
            self.ExternalMediaInfo._deserialize(params.get("ExternalMediaInfo"))
        self.Name = params.get("Name")
        self.PreProcessDefinition = params.get("PreProcessDefinition")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImportMediaToProjectResponse(AbstractModel):
    """ImportMediaToProject返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialId: 媒体 Id。
        :type MaterialId: str
        :param TaskId: 媒体预处理任务 ID，如果未指定发起预处理任务则为空。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class KuaishouPublishInfo(AbstractModel):
    """快手视频发布信息。

    """

    def __init__(self):
        """
        :param Title: 视频发布标题，限30个字符。
        :type Title: str
        """
        self.Title = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListMediaRequest(AbstractModel):
    """ListMedia请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ClassPath: 媒体分类路径，例如填写"/a/b"，则代表浏览该分类路径下的媒体和子分类信息。
        :type ClassPath: str
        :param Owner: 媒体和分类的归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：50。
        :type Limit: int
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验对媒体的访问权限。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListMediaResponse(AbstractModel):
    """ListMedia返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialTotalCount: 符合条件的媒体记录总数。
        :type MaterialTotalCount: int
        :param MaterialInfoSet: 浏览分类路径下的媒体列表信息。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LivePullInputInfo(AbstractModel):
    """直播拉流信息

    """

    def __init__(self):
        """
        :param InputUrl: 直播拉流地址。
        :type InputUrl: str
        """
        self.InputUrl = None


    def _deserialize(self, params):
        self.InputUrl = params.get("InputUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LiveStreamClipProjectInput(AbstractModel):
    """直播剪辑项目输入参数。

    """

    def __init__(self):
        """
        :param Url: 直播流播放地址，目前仅支持 HLS 和 FLV 格式。
        :type Url: str
        :param StreamRecordDuration: 直播流录制时长，单位为秒，最大值为 7200。
        :type StreamRecordDuration: int
        """
        self.Url = None
        self.StreamRecordDuration = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StreamRecordDuration = params.get("StreamRecordDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MaterialBasicInfo(AbstractModel):
    """媒体基本信息。

    """

    def __init__(self):
        """
        :param MaterialId: 媒体 Id。
        :type MaterialId: str
        :param MaterialType: 媒体类型，取值为：
<li> AUDIO :音频;</li>
<li> VIDEO :视频;</li>
<li> IMAGE :图片;</li>
<li> LINK  :链接.</li>
<li> OTHER : 其他.</li>
        :type MaterialType: str
        :param Owner: 媒体归属实体。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Name: 媒体名称。
        :type Name: str
        :param CreateTime: 媒体文件的创建时间，使用 ISO 日期格式。
        :type CreateTime: str
        :param UpdateTime: 媒体文件的最近更新时间（如修改视频属性、发起视频处理等会触发更新媒体文件信息的操作），使用 ISO 日期格式。
        :type UpdateTime: str
        :param ClassPath: 媒体的分类路径。
        :type ClassPath: str
        :param PresetTagSet: 预置标签列表。
        :type PresetTagSet: list of PresetTagInfo
        :param TagSet: 人工标签列表。
        :type TagSet: list of str
        :param PreviewUrl: 媒体文件的预览图。
        :type PreviewUrl: str
        :param TagInfoSet: 媒体绑定的标签信息列表 。
该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInfoSet: list of MaterialTagInfo
        """
        self.MaterialId = None
        self.MaterialType = None
        self.Owner = None
        self.Name = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ClassPath = None
        self.PresetTagSet = None
        self.TagSet = None
        self.PreviewUrl = None
        self.TagInfoSet = None


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
        if params.get("PresetTagSet") is not None:
            self.PresetTagSet = []
            for item in params.get("PresetTagSet"):
                obj = PresetTagInfo()
                obj._deserialize(item)
                self.PresetTagSet.append(obj)
        self.TagSet = params.get("TagSet")
        self.PreviewUrl = params.get("PreviewUrl")
        if params.get("TagInfoSet") is not None:
            self.TagInfoSet = []
            for item in params.get("TagInfoSet"):
                obj = MaterialTagInfo()
                obj._deserialize(item)
                self.TagInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MaterialInfo(AbstractModel):
    """媒体详情信息

    """

    def __init__(self):
        """
        :param BasicInfo: 媒体基本信息。
        :type BasicInfo: :class:`tencentcloud.cme.v20191029.models.MaterialBasicInfo`
        :param VideoMaterial: 视频媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoMaterial: :class:`tencentcloud.cme.v20191029.models.VideoMaterial`
        :param AudioMaterial: 音频媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioMaterial: :class:`tencentcloud.cme.v20191029.models.AudioMaterial`
        :param ImageMaterial: 图片媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageMaterial: :class:`tencentcloud.cme.v20191029.models.ImageMaterial`
        :param LinkMaterial: 链接媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkMaterial: :class:`tencentcloud.cme.v20191029.models.LinkMaterial`
        :param VideoEditTemplateMaterial: 模板媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoEditTemplateMaterial: :class:`tencentcloud.cme.v20191029.models.VideoEditTemplateMaterial`
        :param OtherMaterial: 其他类型媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherMaterial: :class:`tencentcloud.cme.v20191029.models.OtherMaterial`
        """
        self.BasicInfo = None
        self.VideoMaterial = None
        self.AudioMaterial = None
        self.ImageMaterial = None
        self.LinkMaterial = None
        self.VideoEditTemplateMaterial = None
        self.OtherMaterial = None


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
        if params.get("VideoEditTemplateMaterial") is not None:
            self.VideoEditTemplateMaterial = VideoEditTemplateMaterial()
            self.VideoEditTemplateMaterial._deserialize(params.get("VideoEditTemplateMaterial"))
        if params.get("OtherMaterial") is not None:
            self.OtherMaterial = OtherMaterial()
            self.OtherMaterial._deserialize(params.get("OtherMaterial"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MediaReplacementInfo(AbstractModel):
    """媒体替换信息。

    """

    def __init__(self):
        """
        :param MaterialId: 素材 ID。
        :type MaterialId: str
        :param StartTimeOffset: 替换媒体选取的开始时间，单位为秒，默认为 0。
        :type StartTimeOffset: float
        """
        self.MaterialId = None
        self.StartTimeOffset = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.StartTimeOffset = params.get("StartTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MediaTrack(AbstractModel):
    """轨道信息

    """

    def __init__(self):
        """
        :param Type: 轨道类型，取值有：
<ul>
<li>Video ：视频轨道。视频轨道由以下 Item 组成：<ul><li>VideoTrackItem</li><li>EmptyTrackItem</li><li>MediaTransitionItem</li></ul> </li>
<li>Audio ：音频轨道。音频轨道由以下 Item 组成：<ul><li>AudioTrackItem</li><li>EmptyTrackItem</li></ul> </li>
</ul>
        :type Type: str
        :param TrackItems: 轨道上的媒体片段列表。
        :type TrackItems: list of MediaTrackItem
        """
        self.Type = None
        self.TrackItems = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TrackItems") is not None:
            self.TrackItems = []
            for item in params.get("TrackItems"):
                obj = MediaTrackItem()
                obj._deserialize(item)
                self.TrackItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MediaTrackItem(AbstractModel):
    """媒体轨道的片段信息

    """

    def __init__(self):
        """
        :param Type: 片段类型。取值有：
<li>Video：视频片段；</li>
<li>Audio：音频片段；</li>
<li>Empty：空白片段；</li>
<li>Transition：转场。</li>
        :type Type: str
        :param VideoItem: 视频片段，当 Type = Video 时有效。
        :type VideoItem: :class:`tencentcloud.cme.v20191029.models.VideoTrackItem`
        :param AudioItem: 音频片段，当 Type = Audio 时有效。
        :type AudioItem: :class:`tencentcloud.cme.v20191029.models.AudioTrackItem`
        :param EmptyItem: 空白片段，当 Type = Empty 时有效。空片段用于时间轴的占位。<li>如需要两个音频片段之间有一段时间的静音，可以用 EmptyTrackItem 来进行占位。</li>
<li>使用 EmptyTrackItem 进行占位，来定位某个Item。</li>
        :type EmptyItem: :class:`tencentcloud.cme.v20191029.models.EmptyTrackItem`
        :param TransitionItem: 转场，当 Type = Transition 时有效。
        :type TransitionItem: :class:`tencentcloud.cme.v20191029.models.MediaTransitionItem`
        """
        self.Type = None
        self.VideoItem = None
        self.AudioItem = None
        self.EmptyItem = None
        self.TransitionItem = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("VideoItem") is not None:
            self.VideoItem = VideoTrackItem()
            self.VideoItem._deserialize(params.get("VideoItem"))
        if params.get("AudioItem") is not None:
            self.AudioItem = AudioTrackItem()
            self.AudioItem._deserialize(params.get("AudioItem"))
        if params.get("EmptyItem") is not None:
            self.EmptyItem = EmptyTrackItem()
            self.EmptyItem._deserialize(params.get("EmptyItem"))
        if params.get("TransitionItem") is not None:
            self.TransitionItem = MediaTransitionItem()
            self.TransitionItem._deserialize(params.get("TransitionItem"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MediaTransitionItem(AbstractModel):
    """转场信息

    """

    def __init__(self):
        """
        :param TransitionId: 转场 Id 。暂只支持一个转场。
        :type TransitionId: str
        :param Duration: 转场持续时间，单位为秒，默认为2秒。进行转场处理的两个媒体片段，第二个片段在轨道上的起始时间会自动进行调整，设置为前面一个片段的结束时间减去转场的持续时间。
        :type Duration: float
        """
        self.TransitionId = None
        self.Duration = None


    def _deserialize(self, params):
        self.TransitionId = params.get("TransitionId")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMaterialRequest(AbstractModel):
    """ModifyMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param MaterialId: 媒体 Id。
        :type MaterialId: str
        :param Owner: 媒体或分类路径归属。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Name: 媒体名称，不能超过30个字符。
        :type Name: str
        :param ClassPath: 媒体分类路径，例如填写"/a/b"，则代表该媒体存储的路径为"/a/b"。若修改分类路径，则 Owner 字段必填。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param Owner: 项目归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Mode: 项目模式，一个项目可以有多种模式并相互切换。
当 Category 为 VIDEO_EDIT 时，可选模式有：
<li>Defualt：默认模式。</li>
<li>VideoEditTemplate：视频编辑模板制作模式。</li>
        :type Mode: str
        """
        self.Platform = None
        self.ProjectId = None
        self.Name = None
        self.AspectRatio = None
        self.Owner = None
        self.Mode = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.AspectRatio = params.get("AspectRatio")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MoveResourceRequest(AbstractModel):
    """MoveResource请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param SourceResource: 待移动的原始资源信息，包含原始媒体或分类资源，以及资源归属。
        :type SourceResource: :class:`tencentcloud.cme.v20191029.models.ResourceInfo`
        :param DestinationResource: 目标信息，包含分类及归属，仅支持移动资源到分类。
        :type DestinationResource: :class:`tencentcloud.cme.v20191029.models.ResourceInfo`
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验资源访问以及写权限。
        :type Operator: str
        """
        self.Platform = None
        self.SourceResource = None
        self.DestinationResource = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("SourceResource") is not None:
            self.SourceResource = ResourceInfo()
            self.SourceResource._deserialize(params.get("SourceResource"))
        if params.get("DestinationResource") is not None:
            self.DestinationResource = ResourceInfo()
            self.DestinationResource._deserialize(params.get("DestinationResource"))
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MoveResourceResponse(AbstractModel):
    """MoveResource返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OtherMaterial(AbstractModel):
    """其他类型素材

    """

    def __init__(self):
        """
        :param MaterialUrl: 素材媒体文件的播放 URL 地址。
        :type MaterialUrl: str
        :param VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        """
        self.MaterialUrl = None
        self.VodFileId = None


    def _deserialize(self, params):
        self.MaterialUrl = params.get("MaterialUrl")
        self.VodFileId = params.get("VodFileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PenguinMediaPlatformPublishInfo(AbstractModel):
    """企鹅号发布信息。

    """

    def __init__(self):
        """
        :param Title: 视频发布标题。
        :type Title: str
        :param Description: 视频发布描述信息。
        :type Description: str
        :param Tags: 视频标签。
        :type Tags: list of str
        :param Category: 视频分类，详见[企鹅号官网](https://open.om.qq.com/resources/resourcesCenter)视频分类。
        :type Category: int
        """
        self.Title = None
        self.Description = None
        self.Tags = None
        self.Category = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Description = params.get("Description")
        self.Tags = params.get("Tags")
        self.Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PlatformInfo(AbstractModel):
    """平台信息。

    """

    def __init__(self):
        """
        :param Platform: 平台名称。
        :type Platform: str
        :param Description: 平台描述。
        :type Description: str
        :param VodSubAppId: 云点播子应用 Id。
        :type VodSubAppId: int
        :param LicenseId: 平台绑定的 license Id。
        :type LicenseId: str
        :param CreateTime: 创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        :param UpdateTime: 更新时间，格式按照 ISO 8601 标准表示。
        :type UpdateTime: str
        """
        self.Platform = None
        self.Description = None
        self.VodSubAppId = None
        self.LicenseId = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Description = params.get("Description")
        self.VodSubAppId = params.get("VodSubAppId")
        self.LicenseId = params.get("LicenseId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PresetTagInfo(AbstractModel):
    """预置标签信息

    """

    def __init__(self):
        """
        :param Id: 标签 Id 。
        :type Id: str
        :param Name: 标签名称。
        :type Name: str
        :param ParentTagId: 父级预设 Id。
        :type ParentTagId: str
        """
        self.Id = None
        self.Name = None
        self.ParentTagId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.ParentTagId = params.get("ParentTagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param Category: 项目类别，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
<li>SWITCHER：导播台。</li>
<li>VIDEO_SEGMENTATION：视频拆条。</li>
<li>STREAM_CONNECT：云转推。</li>
<li>RECORD_REPLAY：录制回放。</li>
        :type Category: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param CoverUrl: 项目封面图片地址。
        :type CoverUrl: str
        :param StreamConnectProjectInfo: 云转推项目信息，仅当项目类别取值 STREAM_CONNECT 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamConnectProjectInfo: :class:`tencentcloud.cme.v20191029.models.StreamConnectProjectInfo`
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
        self.StreamConnectProjectInfo = None
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
        if params.get("StreamConnectProjectInfo") is not None:
            self.StreamConnectProjectInfo = StreamConnectProjectInfo()
            self.StreamConnectProjectInfo._deserialize(params.get("StreamConnectProjectInfo"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RecordReplayProjectInput(AbstractModel):
    """录制回放项目输入信息。

    """

    def __init__(self):
        """
        :param PullStreamUrl: 录制拉流地址。
        :type PullStreamUrl: str
        :param MaterialOwner: 录制文件归属者。
        :type MaterialOwner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param MaterialClassPath: 录制文件存储分类路径。
        :type MaterialClassPath: str
        :param PushStreamUrl: 回放推流地址。
        :type PushStreamUrl: str
        """
        self.PullStreamUrl = None
        self.MaterialOwner = None
        self.MaterialClassPath = None
        self.PushStreamUrl = None


    def _deserialize(self, params):
        self.PullStreamUrl = params.get("PullStreamUrl")
        if params.get("MaterialOwner") is not None:
            self.MaterialOwner = Entity()
            self.MaterialOwner._deserialize(params.get("MaterialOwner"))
        self.MaterialClassPath = params.get("MaterialClassPath")
        self.PushStreamUrl = params.get("PushStreamUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResourceInfo(AbstractModel):
    """资源信息，包含资源以及归属信息

    """

    def __init__(self):
        """
        :param Resource: 媒资和分类资源。
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.cme.v20191029.models.Resource`
        :param Owner: 资源归属，个人或团队。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        self.Resource = None
        self.Owner = None


    def _deserialize(self, params):
        if params.get("Resource") is not None:
            self.Resource = Resource()
            self.Resource._deserialize(params.get("Resource"))
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RtmpPushInputInfo(AbstractModel):
    """直播推流信息，包括推流地址有效时长，云剪后端生成直播推流地址。

    """

    def __init__(self):
        """
        :param ExpiredSecond: 直播推流地址有效期，单位：秒 。
        :type ExpiredSecond: int
        :param PushUrl: 直播推流地址，入参不填默认由云剪生成。
        :type PushUrl: str
        """
        self.ExpiredSecond = None
        self.PushUrl = None


    def _deserialize(self, params):
        self.ExpiredSecond = params.get("ExpiredSecond")
        self.PushUrl = params.get("PushUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SearchMaterialRequest(AbstractModel):
    """SearchMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param SearchScopes: 指定搜索空间，数组长度不得超过5。
        :type SearchScopes: list of SearchScope
        :param MaterialTypes: 媒体类型，取值：
<li>AUDIO：音频；</li>
<li>VIDEO：视频 ；</li>
<li>IMAGE：图片。</li>
        :type MaterialTypes: list of str
        :param Text: 搜索文本，模糊匹配媒体名称或描述信息，匹配项越多，匹配度越高，排序越优先。长度限制：15个字符。
        :type Text: str
        :param Resolution: 按画质检索，取值为：LD/SD/HD/FHD/2K/4K。
        :type Resolution: str
        :param DurationRange: 按媒体时长检索，单位s。
        :type DurationRange: :class:`tencentcloud.cme.v20191029.models.IntegerRange`
        :param CreateTimeRange: 按照媒体创建时间检索。
        :type CreateTimeRange: :class:`tencentcloud.cme.v20191029.models.TimeRange`
        :param Tags: 按标签检索，填入检索的标签名。
        :type Tags: list of str
        :param Sort: 排序方式。Sort.Field 可选值：CreateTime。指定 Text 搜索时，将根据匹配度排序，该字段无效。
        :type Sort: :class:`tencentcloud.cme.v20191029.models.SortBy`
        :param Offset: 偏移量。默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：50。
        :type Limit: int
        :param Operator: 操作者。填写用户的 Id，用于标识调用者及校验媒体访问权限。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SearchMaterialResponse(AbstractModel):
    """SearchMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合记录总条数。
        :type TotalCount: int
        :param MaterialInfoSet: 媒体信息，仅返回基础信息。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SlotInfo(AbstractModel):
    """卡槽信息。

    """

    def __init__(self):
        """
        :param Id: 卡槽 Id。
        :type Id: int
        :param Type: 素材类型，同素材素材，可取值有：
<li> AUDIO :音频;</li>
<li> VIDEO :视频;</li>
<li> IMAGE :图片。</li>
        :type Type: str
        :param DefaultMaterialId: 默认素材 Id。
        :type DefaultMaterialId: str
        :param Duration: 素材时长，单位秒。
        :type Duration: float
        """
        self.Id = None
        self.Type = None
        self.DefaultMaterialId = None
        self.Duration = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.DefaultMaterialId = params.get("DefaultMaterialId")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SlotReplacementInfo(AbstractModel):
    """卡槽替换信息。

    """

    def __init__(self):
        """
        :param Id: 卡槽 Id。
        :type Id: int
        :param ReplacementType: 替换类型，可取值有：
<li> AUDIO :音频;</li>
<li> VIDEO :视频;</li>
<li> IMAGE :图片。</li>
注意：这里必须保证替换的素材类型与模板轨道数据的素材类型一致。
        :type ReplacementType: str
        :param MediaReplacementInfo: 媒体替换信息，仅当要替换的媒体类型为音频、视频、图片时有效。
        :type MediaReplacementInfo: :class:`tencentcloud.cme.v20191029.models.MediaReplacementInfo`
        """
        self.Id = None
        self.ReplacementType = None
        self.MediaReplacementInfo = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ReplacementType = params.get("ReplacementType")
        if params.get("MediaReplacementInfo") is not None:
            self.MediaReplacementInfo = MediaReplacementInfo()
            self.MediaReplacementInfo._deserialize(params.get("MediaReplacementInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamConnectOutput(AbstractModel):
    """云转推输出源。

    """

    def __init__(self):
        """
        :param Id: 云转推输出源标识，转推项目级别唯一。若不填则由后端生成。
        :type Id: str
        :param Name: 云转推输出源名称。
        :type Name: str
        :param Type: 云转推输出源类型，取值：
<li>URL ：URL类型</li>
不填默认为URL类型。
        :type Type: str
        :param PushUrl: 云转推推流地址。
        :type PushUrl: str
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.PushUrl = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.PushUrl = params.get("PushUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamConnectOutputInfo(AbstractModel):
    """云转推输出源信息，包含输出源和输出源转推状态。

    """

    def __init__(self):
        """
        :param StreamConnectOutput: 输出源。
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamConnectOutput: :class:`tencentcloud.cme.v20191029.models.StreamConnectOutput`
        :param PushSwitch: 输出流状态：
<li>On ：开；</li>
<li>Off ：关 。</li>
        :type PushSwitch: str
        """
        self.StreamConnectOutput = None
        self.PushSwitch = None


    def _deserialize(self, params):
        if params.get("StreamConnectOutput") is not None:
            self.StreamConnectOutput = StreamConnectOutput()
            self.StreamConnectOutput._deserialize(params.get("StreamConnectOutput"))
        self.PushSwitch = params.get("PushSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamConnectProjectInfo(AbstractModel):
    """云转推项目信息，包含输入源、输出源、当前转推开始时间等信息。

    """

    def __init__(self):
        """
        :param Status: 转推项目状态，取值有：
<li>Working ：转推中；</li>
<li>Idle ：空闲中。</li>
        :type Status: str
        :param CurrentInputEndpoint: 当前转推输入源，取值有：
<li>Main ：主输入源；</li>
<li>Backup ：备输入源。</li>
        :type CurrentInputEndpoint: str
        :param CurrentStartTime: 当前转推开始时间， 采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。仅 Status 取值 Working 时有效。
        :type CurrentStartTime: str
        :param CurrentStopTime: 当前转推计划结束时间， 采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。仅 Status 取值 Working 时有效。
        :type CurrentStopTime: str
        :param LastStopTime: 上一次转推结束时间， 采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。仅 Status 取值 Idle 时有效。
        :type LastStopTime: str
        :param MainInput: 云转推主输入源。
注意：此字段可能返回 null，表示取不到有效值。
        :type MainInput: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        :param BackupInput: 云转推备输入源。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupInput: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        :param OutputSet: 云转推输出源。
        :type OutputSet: list of StreamConnectOutputInfo
        """
        self.Status = None
        self.CurrentInputEndpoint = None
        self.CurrentStartTime = None
        self.CurrentStopTime = None
        self.LastStopTime = None
        self.MainInput = None
        self.BackupInput = None
        self.OutputSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.CurrentInputEndpoint = params.get("CurrentInputEndpoint")
        self.CurrentStartTime = params.get("CurrentStartTime")
        self.CurrentStopTime = params.get("CurrentStopTime")
        self.LastStopTime = params.get("LastStopTime")
        if params.get("MainInput") is not None:
            self.MainInput = StreamInputInfo()
            self.MainInput._deserialize(params.get("MainInput"))
        if params.get("BackupInput") is not None:
            self.BackupInput = StreamInputInfo()
            self.BackupInput._deserialize(params.get("BackupInput"))
        if params.get("OutputSet") is not None:
            self.OutputSet = []
            for item in params.get("OutputSet"):
                obj = StreamConnectOutputInfo()
                obj._deserialize(item)
                self.OutputSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamConnectProjectInput(AbstractModel):
    """云转推项目输入信息。

    """

    def __init__(self):
        """
        :param MainInput: 云转推主输入源信息。
        :type MainInput: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        :param BackupInput: 云转推备输入源信息。
        :type BackupInput: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        :param Outputs: 云转推输出源信息。
        :type Outputs: list of StreamConnectOutput
        """
        self.MainInput = None
        self.BackupInput = None
        self.Outputs = None


    def _deserialize(self, params):
        if params.get("MainInput") is not None:
            self.MainInput = StreamInputInfo()
            self.MainInput._deserialize(params.get("MainInput"))
        if params.get("BackupInput") is not None:
            self.BackupInput = StreamInputInfo()
            self.BackupInput._deserialize(params.get("BackupInput"))
        if params.get("Outputs") is not None:
            self.Outputs = []
            for item in params.get("Outputs"):
                obj = StreamConnectOutput()
                obj._deserialize(item)
                self.Outputs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamInputInfo(AbstractModel):
    """输入流信息。

    """

    def __init__(self):
        """
        :param InputType: 流输入类型，取值：
<li>VodPull ： 点播拉流；</li>
<li>LivePull ：直播拉流；</li>
<li>RtmpPush ： 直播推流。</li>
        :type InputType: str
        :param VodPullInputInfo: 点播拉流信息，当 InputType = VodPull 时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type VodPullInputInfo: :class:`tencentcloud.cme.v20191029.models.VodPullInputInfo`
        :param LivePullInputInfo: 直播拉流信息，当 InputType = LivePull  时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type LivePullInputInfo: :class:`tencentcloud.cme.v20191029.models.LivePullInputInfo`
        :param RtmpPushInputInfo: 直播推流信息，当 InputType = RtmpPush 时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type RtmpPushInputInfo: :class:`tencentcloud.cme.v20191029.models.RtmpPushInputInfo`
        """
        self.InputType = None
        self.VodPullInputInfo = None
        self.LivePullInputInfo = None
        self.RtmpPushInputInfo = None


    def _deserialize(self, params):
        self.InputType = params.get("InputType")
        if params.get("VodPullInputInfo") is not None:
            self.VodPullInputInfo = VodPullInputInfo()
            self.VodPullInputInfo._deserialize(params.get("VodPullInputInfo"))
        if params.get("LivePullInputInfo") is not None:
            self.LivePullInputInfo = LivePullInputInfo()
            self.LivePullInputInfo._deserialize(params.get("LivePullInputInfo"))
        if params.get("RtmpPushInputInfo") is not None:
            self.RtmpPushInputInfo = RtmpPushInputInfo()
            self.RtmpPushInputInfo._deserialize(params.get("RtmpPushInputInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SwitcherPgmOutputConfig(AbstractModel):
    """导播台主监输出配置信息

    """

    def __init__(self):
        """
        :param TemplateId: 导播台输出模板 ID，可取值：
<li>10001：分辨率为1080 P；</li>
<li>10002：分辨率为720 P；</li>
<li>10003：分辨率为480 P。</li>
        :type TemplateId: int
        :param Width: 导播台输出宽，单位：像素。
        :type Width: int
        :param Height: 导播台输出高，单位：像素。
        :type Height: int
        :param Fps: 导播台输出帧率，单位：帧/秒
        :type Fps: int
        :param BitRate: 导播台输出码率， 单位：bit/s。
        :type BitRate: int
        """
        self.TemplateId = None
        self.Width = None
        self.Height = None
        self.Fps = None
        self.BitRate = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SwitcherProjectInput(AbstractModel):
    """导播台项目输入信息

    """

    def __init__(self):
        """
        :param StopTime: 导播台停止时间，格式按照 ISO 8601 标准表示。若不填，该值默认为当前时间加七天。
        :type StopTime: str
        :param PgmOutputConfig: 导播台主监输出配置信息。若不填，默认输出 720P。
        :type PgmOutputConfig: :class:`tencentcloud.cme.v20191029.models.SwitcherPgmOutputConfig`
        """
        self.StopTime = None
        self.PgmOutputConfig = None


    def _deserialize(self, params):
        self.StopTime = params.get("StopTime")
        if params.get("PgmOutputConfig") is not None:
            self.PgmOutputConfig = SwitcherPgmOutputConfig()
            self.PgmOutputConfig._deserialize(params.get("PgmOutputConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ThirdPartyPublishInfo(AbstractModel):
    """第三方平台视频发布信息。

    """

    def __init__(self):
        """
        :param ChannelMaterialId: 发布通道  ID。
        :type ChannelMaterialId: str
        :param PenguinMediaPlatformPublishInfo: 企鹅号发布信息，如果使用的发布通道为企鹅号时必填。
        :type PenguinMediaPlatformPublishInfo: :class:`tencentcloud.cme.v20191029.models.PenguinMediaPlatformPublishInfo`
        :param WeiboPublishInfo: 新浪微博发布信息，如果使用的发布通道为新浪微博时必填。
        :type WeiboPublishInfo: :class:`tencentcloud.cme.v20191029.models.WeiboPublishInfo`
        :param KuaishouPublishInfo: 快手发布信息，如果使用的发布通道为快手时必填。
        :type KuaishouPublishInfo: :class:`tencentcloud.cme.v20191029.models.KuaishouPublishInfo`
        """
        self.ChannelMaterialId = None
        self.PenguinMediaPlatformPublishInfo = None
        self.WeiboPublishInfo = None
        self.KuaishouPublishInfo = None


    def _deserialize(self, params):
        self.ChannelMaterialId = params.get("ChannelMaterialId")
        if params.get("PenguinMediaPlatformPublishInfo") is not None:
            self.PenguinMediaPlatformPublishInfo = PenguinMediaPlatformPublishInfo()
            self.PenguinMediaPlatformPublishInfo._deserialize(params.get("PenguinMediaPlatformPublishInfo"))
        if params.get("WeiboPublishInfo") is not None:
            self.WeiboPublishInfo = WeiboPublishInfo()
            self.WeiboPublishInfo._deserialize(params.get("WeiboPublishInfo"))
        if params.get("KuaishouPublishInfo") is not None:
            self.KuaishouPublishInfo = KuaishouPublishInfo()
            self.KuaishouPublishInfo._deserialize(params.get("KuaishouPublishInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VODExportInfo(AbstractModel):
    """云点播导出信息。

    """

    def __init__(self):
        """
        :param Name: 导出的媒资名称。
        :type Name: str
        :param ClassId: 导出的媒资分类 Id。
        :type ClassId: int
        :param ThirdPartyPublishInfos: 第三方平台发布信息列表。暂未正式对外，请勿使用。
        :type ThirdPartyPublishInfos: list of ThirdPartyPublishInfo
        """
        self.Name = None
        self.ClassId = None
        self.ThirdPartyPublishInfos = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ClassId = params.get("ClassId")
        if params.get("ThirdPartyPublishInfos") is not None:
            self.ThirdPartyPublishInfos = []
            for item in params.get("ThirdPartyPublishInfos"):
                obj = ThirdPartyPublishInfo()
                obj._deserialize(item)
                self.ThirdPartyPublishInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VideoEditProjectInput(AbstractModel):
    """视频编辑项目输入参数

    """

    def __init__(self):
        """
        :param AspectRatio: 画布宽高比，取值有：
<li>16:9；</li>
<li>9:16；</li>
<li>2:1。</li>
默认值 16:9 。
        :type AspectRatio: str
        :param VideoEditTemplateId: 视频编辑模板媒体 ID ，通过模板媒体导入项目轨道数据时填写。
        :type VideoEditTemplateId: str
        :param InitTracks: 输入的媒体轨道列表，包括视频、音频，等媒体组成的多个轨道信息。其中：<li>输入的多个轨道在时间轴上和输出媒体文件的时间轴对齐；</li><li>时间轴上相同时间点的各个轨道的素材进行重叠，视频或者图片按轨道顺序进行图像的叠加，轨道顺序高的素材叠加在上面，音频素材进行混音；</li><li>视频、音频，每一种类型的轨道最多支持10个。</li>
注：当从模板导入项目时（即 VideoEditTemplateId 不为空时），该参数无效。
        :type InitTracks: list of MediaTrack
        """
        self.AspectRatio = None
        self.VideoEditTemplateId = None
        self.InitTracks = None


    def _deserialize(self, params):
        self.AspectRatio = params.get("AspectRatio")
        self.VideoEditTemplateId = params.get("VideoEditTemplateId")
        if params.get("InitTracks") is not None:
            self.InitTracks = []
            for item in params.get("InitTracks"):
                obj = MediaTrack()
                obj._deserialize(item)
                self.InitTracks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VideoEditTemplateMaterial(AbstractModel):
    """视频编辑模板素材信息。

    """

    def __init__(self):
        """
        :param AspectRatio: 视频编辑模板宽高比。
        :type AspectRatio: str
        :param SlotSet: 卡槽信息。
        :type SlotSet: list of SlotInfo
        """
        self.AspectRatio = None
        self.SlotSet = None


    def _deserialize(self, params):
        self.AspectRatio = params.get("AspectRatio")
        if params.get("SlotSet") is not None:
            self.SlotSet = []
            for item in params.get("SlotSet"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VideoSegmentationProjectInput(AbstractModel):
    """视频拆条项目的输入信息。

    """

    def __init__(self):
        """
        :param AspectRatio: 画布宽高比，取值有：
<li>16:9；</li>
<li>9:16；</li>
<li>2:1。</li>
默认值 16:9 。
        :type AspectRatio: str
        :param ProcessModel: 视频拆条处理模型，不填则默认为手工分割视频。取值 ：
<li>AI.GameHighlights.PUBG：和平精英集锦 ;</li>
<li>AI.GameHighlights.Honor OfKings：王者荣耀集锦 ;</li>
<li>AI.SportHighlights.Football：足球集锦 </li>
<li>AI.SportHighlights.Basketball：篮球集锦 ；</li>
<li>AI.PersonSegmentation：人物集锦  ;</li>
<li>AI.NewsSegmentation：新闻拆条。</li>
        :type ProcessModel: str
        """
        self.AspectRatio = None
        self.ProcessModel = None


    def _deserialize(self, params):
        self.AspectRatio = params.get("AspectRatio")
        self.ProcessModel = params.get("ProcessModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VideoTrackItem(AbstractModel):
    """视频轨的视频片段信息。

    """

    def __init__(self):
        """
        :param SourceType: 视频媒体来源类型，取值有：
<ul>
<li>VOD ：媒体来源于云点播文件 。</li>
<li>CME ：视频来源制作云媒体文件。</li>
<li>EXTERNAL ：视频来源于媒资绑定。</li>
</ul>
        :type SourceType: str
        :param SourceMedia: 视频片段的媒体文件来源，取值为：
<ul>
<li>当 SourceType 为 VOD 时，为云点播的媒体文件 FileId ，会默认将该 FileId 导入到项目中；</li>
<li>当 SourceType 为 CME 时，为制作云的媒体 ID，项目归属者必须对该云媒资有访问权限；</li>
<li>当 SourceType 为 EXTERNAL 时，为媒资绑定的 Definition 与 MediaKey 中间用冒号分隔合并后的字符串，格式为 Definition:MediaKey 。</li>
</ul>
        :type SourceMedia: str
        :param SourceMediaStartTime: 视频片段取自媒体文件的起始时间，单位为秒。默认为0。
        :type SourceMediaStartTime: float
        :param Duration: 视频片段时长，单位为秒。默认取视频媒体文件本身长度，表示截取全部媒体文件。如果源文件是图片，Duration需要大于0。
        :type Duration: float
        :param XPos: 视频片段原点距离画布原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 XPos 为画布宽度指定百分比的位置，如 10% 表示 XPos 为画布口宽度的 10%。</li>
<li>当字符串以 px 结尾，表示视频片段 XPos 单位为像素，如 100px 表示 XPos 为100像素。</li>
默认值：0px。
        :type XPos: str
        :param YPos: 视频片段原点距离画布原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 YPos 为画布高度指定百分比的位置，如 10% 表示 YPos 为画布高度的 10%。</li>
<li>当字符串以 px 结尾，表示视频片段 YPos 单位为像素，如 100px 表示 YPos 为100像素。</li>
默认值：0px。
        :type YPos: str
        :param CoordinateOrigin: 视频原点位置，取值有：
<li>Center：坐标原点为中心位置，如画布中心。</li>
默认值 ：Center。
        :type CoordinateOrigin: str
        :param Height: 视频片段的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 Height 为画布高度的百分比大小，如 10% 表示 Height 为画布高度的 10%；</li>
<li>当字符串以 px 结尾，表示视频片段 Height 单位为像素，如 100px 表示 Height 为100像素；</li>
<li>当 Width、Height 均为空，则 Width 和 Height 取视频媒体文件本身的 Width、Height；</li>
<li>当 Width 为空，Height 非空，则 Width 按比例缩放；</li>
<li>当 Width 非空，Height 为空，则 Height 按比例缩放。</li>
        :type Height: str
        :param Width: 视频片段的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 Width 为画布宽度的百分比大小，如 10% 表示 Width 为画布宽度的 10%；</li>
<li>当字符串以 px 结尾，表示视频片段 Width 单位为像素，如 100px 表示 Width 为100像素；</li>
<li>当 Width、Height 均为空，则 Width 和 Height 取视频媒体文件本身的 Width、Height；</li>
<li>当 Width 为空，Height 非空，则 Width 按比例缩放；</li>
<li>当 Width 非空，Height 为空，则 Height 按比例缩放。</li>
        :type Width: str
        """
        self.SourceType = None
        self.SourceMedia = None
        self.SourceMediaStartTime = None
        self.Duration = None
        self.XPos = None
        self.YPos = None
        self.CoordinateOrigin = None
        self.Height = None
        self.Width = None


    def _deserialize(self, params):
        self.SourceType = params.get("SourceType")
        self.SourceMedia = params.get("SourceMedia")
        self.SourceMediaStartTime = params.get("SourceMediaStartTime")
        self.Duration = params.get("Duration")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VodPullInputInfo(AbstractModel):
    """点播拉流信息，包括输入拉流地址和播放次数。

    """

    def __init__(self):
        """
        :param InputUrls: 点播输入拉流 URL 。
        :type InputUrls: list of str
        :param LoopTimes: 播放次数，取值有：
<li>-1 : 循环播放，直到转推结束；</li>
<li>0 : 不循环；</li>
<li>大于0 : 具体循环次数，次数和时间以先结束的为准。</li>
默认不循环。
        :type LoopTimes: int
        """
        self.InputUrls = None
        self.LoopTimes = None


    def _deserialize(self, params):
        self.InputUrls = params.get("InputUrls")
        self.LoopTimes = params.get("LoopTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class WeiboPublishInfo(AbstractModel):
    """微博发布信息。

    """

    def __init__(self):
        """
        :param Title: 视频发布标题。
        :type Title: str
        :param Description: 视频发布描述信息。
        :type Description: str
        :param Visible: 微博可见性，可取值为：
<li>Public：公开，所有人可见；</li>
<li>Private：私有，仅自己可见。</li>

默认为 Public，所有人可见。
        :type Visible: str
        """
        self.Title = None
        self.Description = None
        self.Visible = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Description = params.get("Description")
        self.Visible = params.get("Visible")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        