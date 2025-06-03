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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AccountInfo(AbstractModel):
    """制作云用户账号信息。

    """

    def __init__(self):
        r"""
        :param _UserId: 用户 Id。
        :type UserId: str
        :param _Phone: 用户手机号码。
        :type Phone: str
        :param _Nick: 用户昵称。
        :type Nick: str
        :param _Status: 账号状态，取值：
<li>Normal：有效；</li>
<li>Stopped：无效。</li>
        :type Status: str
        """
        self._UserId = None
        self._Phone = None
        self._Nick = None
        self._Status = None

    @property
    def UserId(self):
        """用户 Id。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Phone(self):
        """用户手机号码。
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Nick(self):
        """用户昵称。
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Status(self):
        """账号状态，取值：
<li>Normal：有效；</li>
<li>Stopped：无效。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Phone = params.get("Phone")
        self._Nick = params.get("Nick")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddMemberInfo(AbstractModel):
    """添加的团队成员信息

    """

    def __init__(self):
        r"""
        :param _MemberId: 团队成员 ID。
        :type MemberId: str
        :param _Remark: 团队成员备注。
        :type Remark: str
        :param _Role: 团队成员角色，不填则默认添加普通成员。可选值：
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :type Role: str
        """
        self._MemberId = None
        self._Remark = None
        self._Role = None

    @property
    def MemberId(self):
        """团队成员 ID。
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Remark(self):
        """团队成员备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Role(self):
        """团队成员角色，不填则默认添加普通成员。可选值：
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._Remark = params.get("Remark")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTeamMemberRequest(AbstractModel):
    """AddTeamMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _TeamId: 团队 ID。
        :type TeamId: str
        :param _TeamMembers: 要添加的成员列表，一次最多添加30个成员。
        :type TeamMembers: list of AddMemberInfo
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以向任意团队中添加成员。如果指定操作者，则操作者必须为管理员或者团队所有者。
        :type Operator: str
        """
        self._Platform = None
        self._TeamId = None
        self._TeamMembers = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TeamId(self):
        """团队 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def TeamMembers(self):
        """要添加的成员列表，一次最多添加30个成员。
        :rtype: list of AddMemberInfo
        """
        return self._TeamMembers

    @TeamMembers.setter
    def TeamMembers(self, TeamMembers):
        self._TeamMembers = TeamMembers

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以向任意团队中添加成员。如果指定操作者，则操作者必须为管理员或者团队所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._TeamId = params.get("TeamId")
        if params.get("TeamMembers") is not None:
            self._TeamMembers = []
            for item in params.get("TeamMembers"):
                obj = AddMemberInfo()
                obj._deserialize(item)
                self._TeamMembers.append(obj)
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTeamMemberResponse(AbstractModel):
    """AddTeamMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AudioMaterial(AbstractModel):
    """音频素材信息

    """

    def __init__(self):
        r"""
        :param _MetaData: 素材元信息。
        :type MetaData: :class:`tencentcloud.cme.v20191029.models.MediaMetaData`
        :param _MaterialUrl: 素材媒体文件的播放 URL 地址。
        :type MaterialUrl: str
        :param _CoverUrl: 素材媒体文件的封面图片地址。
        :type CoverUrl: str
        :param _MaterialStatus: 素材状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialStatus: :class:`tencentcloud.cme.v20191029.models.MaterialStatus`
        :param _OriginalUrl: 素材媒体文件的原始 URL 地址。
        :type OriginalUrl: str
        :param _VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        """
        self._MetaData = None
        self._MaterialUrl = None
        self._CoverUrl = None
        self._MaterialStatus = None
        self._OriginalUrl = None
        self._VodFileId = None

    @property
    def MetaData(self):
        """素材元信息。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaMetaData`
        """
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData

    @property
    def MaterialUrl(self):
        """素材媒体文件的播放 URL 地址。
        :rtype: str
        """
        return self._MaterialUrl

    @MaterialUrl.setter
    def MaterialUrl(self, MaterialUrl):
        self._MaterialUrl = MaterialUrl

    @property
    def CoverUrl(self):
        """素材媒体文件的封面图片地址。
        :rtype: str
        """
        return self._CoverUrl

    @CoverUrl.setter
    def CoverUrl(self, CoverUrl):
        self._CoverUrl = CoverUrl

    @property
    def MaterialStatus(self):
        """素材状态。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MaterialStatus`
        """
        return self._MaterialStatus

    @MaterialStatus.setter
    def MaterialStatus(self, MaterialStatus):
        self._MaterialStatus = MaterialStatus

    @property
    def OriginalUrl(self):
        """素材媒体文件的原始 URL 地址。
        :rtype: str
        """
        return self._OriginalUrl

    @OriginalUrl.setter
    def OriginalUrl(self, OriginalUrl):
        self._OriginalUrl = OriginalUrl

    @property
    def VodFileId(self):
        """云点播媒资 FileId。
        :rtype: str
        """
        return self._VodFileId

    @VodFileId.setter
    def VodFileId(self, VodFileId):
        self._VodFileId = VodFileId


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self._MetaData = MediaMetaData()
            self._MetaData._deserialize(params.get("MetaData"))
        self._MaterialUrl = params.get("MaterialUrl")
        self._CoverUrl = params.get("CoverUrl")
        if params.get("MaterialStatus") is not None:
            self._MaterialStatus = MaterialStatus()
            self._MaterialStatus._deserialize(params.get("MaterialStatus"))
        self._OriginalUrl = params.get("OriginalUrl")
        self._VodFileId = params.get("VodFileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioStreamInfo(AbstractModel):
    """音频流信息。

    """

    def __init__(self):
        r"""
        :param _Bitrate: 码率，单位：bps。
        :type Bitrate: int
        :param _SamplingRate: 采样率，单位：hz。
        :type SamplingRate: int
        :param _Codec: 编码格式。
        :type Codec: str
        """
        self._Bitrate = None
        self._SamplingRate = None
        self._Codec = None

    @property
    def Bitrate(self):
        """码率，单位：bps。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def SamplingRate(self):
        """采样率，单位：hz。
        :rtype: int
        """
        return self._SamplingRate

    @SamplingRate.setter
    def SamplingRate(self, SamplingRate):
        self._SamplingRate = SamplingRate

    @property
    def Codec(self):
        """编码格式。
        :rtype: str
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec


    def _deserialize(self, params):
        self._Bitrate = params.get("Bitrate")
        self._SamplingRate = params.get("SamplingRate")
        self._Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTrackItem(AbstractModel):
    """音频轨道上的音频片段信息。

    """

    def __init__(self):
        r"""
        :param _SourceType: 音频媒体来源类型，取值有：
<ul>
<li>VOD ：素材来源于云点播文件 ；</li>
<li>CME ：视频来源于制作云媒体文件 ；</li>
<li>EXTERNAL ：视频来源于媒资绑定，如果媒体不是存储在腾讯云点播中或者云创中，都需要使用媒资绑定。</li>
</ul>
        :type SourceType: str
        :param _SourceMedia: 音频媒体，可取值为：
<ul>
<li>当 SourceType 为 VOD 时，参数填云点播 FileId ；</li>
<li>当 SourceType 为 CME 时，参数填多媒体创作引擎媒体 Id；</li>
<li>当 SourceType 为 EXTERNAL 时，目前仅支持外部媒体 URL(如`https://www.example.com/a.mp3`)，参数填写规则请参见注意事项。</li>
</ul>

注意：
<li>当 SourceType 为 EXTERNAL 并且媒体 URL Scheme 为 `https` 时(如：`https://www.example.com/a.mp3`)，参数为：`1000000:www.example.com/a.mp3`。</li>
<li>当 SourceType 为 EXTERNAL 并且媒体 URL Scheme 为 `http` 时(如：`http://www.example.com/b.mp3`)，参数为：`1000001:www.example.com/b.mp3`。</li>
        :type SourceMedia: str
        :param _SourceMediaStartTime: 音频片段取自媒体文件的起始时间，单位为秒。0 表示从媒体开始位置截取。默认为0。
        :type SourceMediaStartTime: float
        :param _Duration: 音频片段的时长，单位为秒。默认和媒体本身长度一致，表示截取全部媒体。
        :type Duration: float
        """
        self._SourceType = None
        self._SourceMedia = None
        self._SourceMediaStartTime = None
        self._Duration = None

    @property
    def SourceType(self):
        """音频媒体来源类型，取值有：
<ul>
<li>VOD ：素材来源于云点播文件 ；</li>
<li>CME ：视频来源于制作云媒体文件 ；</li>
<li>EXTERNAL ：视频来源于媒资绑定，如果媒体不是存储在腾讯云点播中或者云创中，都需要使用媒资绑定。</li>
</ul>
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceMedia(self):
        """音频媒体，可取值为：
<ul>
<li>当 SourceType 为 VOD 时，参数填云点播 FileId ；</li>
<li>当 SourceType 为 CME 时，参数填多媒体创作引擎媒体 Id；</li>
<li>当 SourceType 为 EXTERNAL 时，目前仅支持外部媒体 URL(如`https://www.example.com/a.mp3`)，参数填写规则请参见注意事项。</li>
</ul>

注意：
<li>当 SourceType 为 EXTERNAL 并且媒体 URL Scheme 为 `https` 时(如：`https://www.example.com/a.mp3`)，参数为：`1000000:www.example.com/a.mp3`。</li>
<li>当 SourceType 为 EXTERNAL 并且媒体 URL Scheme 为 `http` 时(如：`http://www.example.com/b.mp3`)，参数为：`1000001:www.example.com/b.mp3`。</li>
        :rtype: str
        """
        return self._SourceMedia

    @SourceMedia.setter
    def SourceMedia(self, SourceMedia):
        self._SourceMedia = SourceMedia

    @property
    def SourceMediaStartTime(self):
        """音频片段取自媒体文件的起始时间，单位为秒。0 表示从媒体开始位置截取。默认为0。
        :rtype: float
        """
        return self._SourceMediaStartTime

    @SourceMediaStartTime.setter
    def SourceMediaStartTime(self, SourceMediaStartTime):
        self._SourceMediaStartTime = SourceMediaStartTime

    @property
    def Duration(self):
        """音频片段的时长，单位为秒。默认和媒体本身长度一致，表示截取全部媒体。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._SourceType = params.get("SourceType")
        self._SourceMedia = params.get("SourceMedia")
        self._SourceMediaStartTime = params.get("SourceMediaStartTime")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationInfo(AbstractModel):
    """资源权限信息

    """

    def __init__(self):
        r"""
        :param _Authorizee: 被授权者实体。
        :type Authorizee: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _PermissionSet: 详细授权值。 取值有：
<li>R：可读，可以浏览素材，但不能使用该素材（将其添加到 Project），或复制到自己的媒资库中。</li>
<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>
<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>
<li>W：可修改、删除媒资。</li>
        :type PermissionSet: list of str
        """
        self._Authorizee = None
        self._PermissionSet = None

    @property
    def Authorizee(self):
        """被授权者实体。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Authorizee

    @Authorizee.setter
    def Authorizee(self, Authorizee):
        self._Authorizee = Authorizee

    @property
    def PermissionSet(self):
        """详细授权值。 取值有：
<li>R：可读，可以浏览素材，但不能使用该素材（将其添加到 Project），或复制到自己的媒资库中。</li>
<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>
<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>
<li>W：可修改、删除媒资。</li>
        :rtype: list of str
        """
        return self._PermissionSet

    @PermissionSet.setter
    def PermissionSet(self, PermissionSet):
        self._PermissionSet = PermissionSet


    def _deserialize(self, params):
        if params.get("Authorizee") is not None:
            self._Authorizee = Entity()
            self._Authorizee._deserialize(params.get("Authorizee"))
        self._PermissionSet = params.get("PermissionSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Authorizer(AbstractModel):
    """授权者

    """

    def __init__(self):
        r"""
        :param _Type: 授权者类型，取值有：
<li>PERSON：个人。</li>
<li>TEAM：团队。</li>
        :type Type: str
        :param _Id: Id，当 Type=PERSON，取值为用户 Id。当Type=TEAM，取值为团队 ID。
        :type Id: str
        """
        self._Type = None
        self._Id = None

    @property
    def Type(self):
        """授权者类型，取值有：
<li>PERSON：个人。</li>
<li>TEAM：团队。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Id(self):
        """Id，当 Type=PERSON，取值为用户 Id。当Type=TEAM，取值为团队 ID。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CMEExportInfo(AbstractModel):
    """多媒体创作引擎导出信息。

    """

    def __init__(self):
        r"""
        :param _Owner: 导出媒体归属，个人或团队。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Name: 导出的媒体名称，不得超过30个字符。
        :type Name: str
        :param _Description: 导出的媒体信息，不得超过50个字符。
        :type Description: str
        :param _ClassPath: 导出的媒体分类路径，长度不能超过15字符。不存在默认创建。
        :type ClassPath: str
        :param _TagSet: 导出的媒体标签，单个标签不得超过10个字符。
        :type TagSet: list of str
        :param _ThirdPartyPublishInfos: 第三方平台发布信息列表。暂未正式对外，请勿使用。
        :type ThirdPartyPublishInfos: list of ThirdPartyPublishInfo
        """
        self._Owner = None
        self._Name = None
        self._Description = None
        self._ClassPath = None
        self._TagSet = None
        self._ThirdPartyPublishInfos = None

    @property
    def Owner(self):
        """导出媒体归属，个人或团队。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Name(self):
        """导出的媒体名称，不得超过30个字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """导出的媒体信息，不得超过50个字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClassPath(self):
        """导出的媒体分类路径，长度不能超过15字符。不存在默认创建。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath

    @property
    def TagSet(self):
        """导出的媒体标签，单个标签不得超过10个字符。
        :rtype: list of str
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def ThirdPartyPublishInfos(self):
        """第三方平台发布信息列表。暂未正式对外，请勿使用。
        :rtype: list of ThirdPartyPublishInfo
        """
        return self._ThirdPartyPublishInfos

    @ThirdPartyPublishInfos.setter
    def ThirdPartyPublishInfos(self, ThirdPartyPublishInfos):
        self._ThirdPartyPublishInfos = ThirdPartyPublishInfos


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ClassPath = params.get("ClassPath")
        self._TagSet = params.get("TagSet")
        if params.get("ThirdPartyPublishInfos") is not None:
            self._ThirdPartyPublishInfos = []
            for item in params.get("ThirdPartyPublishInfos"):
                obj = ThirdPartyPublishInfo()
                obj._deserialize(item)
                self._ThirdPartyPublishInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassCreatedEvent(AbstractModel):
    """分类创建事件。

    """

    def __init__(self):
        r"""
        :param _Owner: 分类归属。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _ClassPath: 分类路径。
        :type ClassPath: str
        """
        self._Owner = None
        self._ClassPath = None

    @property
    def Owner(self):
        """分类归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def ClassPath(self):
        """分类路径。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._ClassPath = params.get("ClassPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassDeletedEvent(AbstractModel):
    """分类删除事件。

    """

    def __init__(self):
        r"""
        :param _Owner: 删除的分类归属。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _ClassPathSet: 删除的分类路径列表。
        :type ClassPathSet: list of str
        """
        self._Owner = None
        self._ClassPathSet = None

    @property
    def Owner(self):
        """删除的分类归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def ClassPathSet(self):
        """删除的分类路径列表。
        :rtype: list of str
        """
        return self._ClassPathSet

    @ClassPathSet.setter
    def ClassPathSet(self, ClassPathSet):
        self._ClassPathSet = ClassPathSet


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._ClassPathSet = params.get("ClassPathSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassInfo(AbstractModel):
    """分类信息

    """

    def __init__(self):
        r"""
        :param _Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _ClassPath: 分类路径。
        :type ClassPath: str
        """
        self._Owner = None
        self._ClassPath = None

    @property
    def Owner(self):
        """归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def ClassPath(self):
        """分类路径。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._ClassPath = params.get("ClassPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassMovedEvent(AbstractModel):
    """分类移动事件。

    """

    def __init__(self):
        r"""
        :param _SourceOwner: 源分类归属。
        :type SourceOwner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _SourceClassPathSet: 源分类路径列表。
        :type SourceClassPathSet: list of str
        :param _DestinationOwner: 目标分类归属。
        :type DestinationOwner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _DestinationClassPath: 目标分类归属。
        :type DestinationClassPath: str
        """
        self._SourceOwner = None
        self._SourceClassPathSet = None
        self._DestinationOwner = None
        self._DestinationClassPath = None

    @property
    def SourceOwner(self):
        """源分类归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._SourceOwner

    @SourceOwner.setter
    def SourceOwner(self, SourceOwner):
        self._SourceOwner = SourceOwner

    @property
    def SourceClassPathSet(self):
        """源分类路径列表。
        :rtype: list of str
        """
        return self._SourceClassPathSet

    @SourceClassPathSet.setter
    def SourceClassPathSet(self, SourceClassPathSet):
        self._SourceClassPathSet = SourceClassPathSet

    @property
    def DestinationOwner(self):
        """目标分类归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._DestinationOwner

    @DestinationOwner.setter
    def DestinationOwner(self, DestinationOwner):
        self._DestinationOwner = DestinationOwner

    @property
    def DestinationClassPath(self):
        """目标分类归属。
        :rtype: str
        """
        return self._DestinationClassPath

    @DestinationClassPath.setter
    def DestinationClassPath(self, DestinationClassPath):
        self._DestinationClassPath = DestinationClassPath


    def _deserialize(self, params):
        if params.get("SourceOwner") is not None:
            self._SourceOwner = Entity()
            self._SourceOwner._deserialize(params.get("SourceOwner"))
        self._SourceClassPathSet = params.get("SourceClassPathSet")
        if params.get("DestinationOwner") is not None:
            self._DestinationOwner = Entity()
            self._DestinationOwner._deserialize(params.get("DestinationOwner"))
        self._DestinationClassPath = params.get("DestinationClassPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyProjectRequest(AbstractModel):
    """CopyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param _ProjectId: 被复制的项目 ID。
        :type ProjectId: str
        :param _Name: 复制后的项目名称，不填为原项目名称+"(副本)"。
        :type Name: str
        :param _Owner: 复制后的项目归属者，不填为原项目归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self._Platform = None
        self._ProjectId = None
        self._Name = None
        self._Owner = None
        self._Operator = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectId(self):
        """被复制的项目 ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        """复制后的项目名称，不填为原项目名称+"(副本)"。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Owner(self):
        """复制后的项目归属者，不填为原项目归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Operator(self):
        """操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyProjectResponse(AbstractModel):
    """CopyProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 复制后的项目 ID。
        :type ProjectId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectId = None
        self._RequestId = None

    @property
    def ProjectId(self):
        """复制后的项目 ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RequestId = params.get("RequestId")


class CosPublishInputInfo(AbstractModel):
    """COS 发布信息。

    """

    def __init__(self):
        r"""
        :param _Bucket: 发布生成的对象存储文件所在的 COS Bucket 名，如 TopRankVideo-125xxx88。
        :type Bucket: str
        :param _Region: 发布生成的对象存储文件所在的 COS Bucket 所属园区，如 ap-chongqing。
        :type Region: str
        :param _VideoKey: 发布生成的视频在 COS 存储的对象键。对象键（ObjectKey）是对象（Object）在存储桶（Bucket）中的唯一标识。
        :type VideoKey: str
        :param _CoverKey: 发布生成的封面在 COS 存储的对象键。
        :type CoverKey: str
        """
        self._Bucket = None
        self._Region = None
        self._VideoKey = None
        self._CoverKey = None

    @property
    def Bucket(self):
        """发布生成的对象存储文件所在的 COS Bucket 名，如 TopRankVideo-125xxx88。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        """发布生成的对象存储文件所在的 COS Bucket 所属园区，如 ap-chongqing。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VideoKey(self):
        """发布生成的视频在 COS 存储的对象键。对象键（ObjectKey）是对象（Object）在存储桶（Bucket）中的唯一标识。
        :rtype: str
        """
        return self._VideoKey

    @VideoKey.setter
    def VideoKey(self, VideoKey):
        self._VideoKey = VideoKey

    @property
    def CoverKey(self):
        """发布生成的封面在 COS 存储的对象键。
        :rtype: str
        """
        return self._CoverKey

    @CoverKey.setter
    def CoverKey(self, CoverKey):
        self._CoverKey = CoverKey


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._VideoKey = params.get("VideoKey")
        self._CoverKey = params.get("CoverKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClassRequest(AbstractModel):
    """CreateClass请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param _Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _ClassPath: 分类路径。
        :type ClassPath: str
        :param _Operator: 操作者。填写用户的 Id，用于标识调用者及校验分类创建权限。
        :type Operator: str
        """
        self._Platform = None
        self._Owner = None
        self._ClassPath = None
        self._Operator = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Owner(self):
        """归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def ClassPath(self):
        """分类路径。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath

    @property
    def Operator(self):
        """操作者。填写用户的 Id，用于标识调用者及校验分类创建权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._ClassPath = params.get("ClassPath")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClassResponse(AbstractModel):
    """CreateClass返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateLinkRequest(AbstractModel):
    """CreateLink请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Type: 链接类型，可取值有:
<li>CLASS: 分类链接；</li>
<li> MATERIAL：媒体文件链接。</li>
        :type Type: str
        :param _Name: 链接名称，不能超过30个字符。
        :type Name: str
        :param _Owner: 链接归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _DestinationId: 目标资源Id。可取值有：
<li>当 Type 为 MATERIAL 时填媒体 ID；</li>
<li>当 Type 为 CLASS 时填写分类路径。</li>
        :type DestinationId: str
        :param _DestinationOwner: 目标资源归属者。
        :type DestinationOwner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _ClassPath: 链接的分类路径，如填"/a/b"则代表链接属于该分类路径，不填则默认为根路径。
        :type ClassPath: str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以创建任意源及目标资源的链接。如果指定操作者，则操作者必须对源资源有读权限，对目标媒体有写权限。
        :type Operator: str
        """
        self._Platform = None
        self._Type = None
        self._Name = None
        self._Owner = None
        self._DestinationId = None
        self._DestinationOwner = None
        self._ClassPath = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Type(self):
        """链接类型，可取值有:
<li>CLASS: 分类链接；</li>
<li> MATERIAL：媒体文件链接。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        """链接名称，不能超过30个字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Owner(self):
        """链接归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def DestinationId(self):
        """目标资源Id。可取值有：
<li>当 Type 为 MATERIAL 时填媒体 ID；</li>
<li>当 Type 为 CLASS 时填写分类路径。</li>
        :rtype: str
        """
        return self._DestinationId

    @DestinationId.setter
    def DestinationId(self, DestinationId):
        self._DestinationId = DestinationId

    @property
    def DestinationOwner(self):
        """目标资源归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._DestinationOwner

    @DestinationOwner.setter
    def DestinationOwner(self, DestinationOwner):
        self._DestinationOwner = DestinationOwner

    @property
    def ClassPath(self):
        """链接的分类路径，如填"/a/b"则代表链接属于该分类路径，不填则默认为根路径。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以创建任意源及目标资源的链接。如果指定操作者，则操作者必须对源资源有读权限，对目标媒体有写权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._DestinationId = params.get("DestinationId")
        if params.get("DestinationOwner") is not None:
            self._DestinationOwner = Entity()
            self._DestinationOwner._deserialize(params.get("DestinationOwner"))
        self._ClassPath = params.get("ClassPath")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLinkResponse(AbstractModel):
    """CreateLink返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MaterialId: 新建链接的媒体 Id。
        :type MaterialId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MaterialId = None
        self._RequestId = None

    @property
    def MaterialId(self):
        """新建链接的媒体 Id。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MaterialId = params.get("MaterialId")
        self._RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Name: 项目名称，不可超过30个字符。
        :type Name: str
        :param _Owner: 项目归属者，即项目的所有者，后续操作只有该所有者有权限操作。

注：目前所有项目只能设置归属个人，暂不支持团队项目。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Category: 项目类别，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
<li>SWITCHER：导播台。</li>
<li>VIDEO_SEGMENTATION：视频拆条。</li>
<li>STREAM_CONNECT：云转推。</li>
<li>RECORD_REPLAY：录制回放。</li>
<li>MEDIA_CAST：媒体转推。</li>
        :type Category: str
        :param _Mode: 项目模式，一个项目可以有多种模式并相互切换。
当 Category 为 VIDEO_EDIT 时，可选模式有：
<li>Default：默认模式，即普通视频编辑项目。</li>
<li>VideoEditTemplate：剪辑模板制作模式，用于制作剪辑模板。</li>

注：不填则为默认模式。
        :type Mode: str
        :param _AspectRatio: 画布宽高比。
该字段已经废弃，请使用具体项目输入中的 AspectRatio 字段。
        :type AspectRatio: str
        :param _Description: 项目描述信息。
        :type Description: str
        :param _SwitcherProjectInput: 导播台项目输入信息，仅当项目类型为 SWITCHER 时必填。
        :type SwitcherProjectInput: :class:`tencentcloud.cme.v20191029.models.SwitcherProjectInput`
        :param _LiveStreamClipProjectInput: 直播剪辑项目输入信息，暂未开放，请勿使用。
        :type LiveStreamClipProjectInput: :class:`tencentcloud.cme.v20191029.models.LiveStreamClipProjectInput`
        :param _VideoEditProjectInput: 视频编辑项目输入信息，仅当项目类型为 VIDEO_EDIT 时必填。
        :type VideoEditProjectInput: :class:`tencentcloud.cme.v20191029.models.VideoEditProjectInput`
        :param _VideoSegmentationProjectInput: 视频拆条项目输入信息，仅当项目类型为 VIDEO_SEGMENTATION  时必填。
        :type VideoSegmentationProjectInput: :class:`tencentcloud.cme.v20191029.models.VideoSegmentationProjectInput`
        :param _StreamConnectProjectInput: 云转推项目输入信息，仅当项目类型为 STREAM_CONNECT 时必填。
        :type StreamConnectProjectInput: :class:`tencentcloud.cme.v20191029.models.StreamConnectProjectInput`
        :param _RecordReplayProjectInput: 录制回放项目输入信息，仅当项目类型为 RECORD_REPLAY 时必填。
        :type RecordReplayProjectInput: :class:`tencentcloud.cme.v20191029.models.RecordReplayProjectInput`
        :param _MediaCastProjectInput: 媒体转推项目输入信息，仅当项目类型为 MEDIA_CAST 时必填。
        :type MediaCastProjectInput: :class:`tencentcloud.cme.v20191029.models.MediaCastProjectInput`
        """
        self._Platform = None
        self._Name = None
        self._Owner = None
        self._Category = None
        self._Mode = None
        self._AspectRatio = None
        self._Description = None
        self._SwitcherProjectInput = None
        self._LiveStreamClipProjectInput = None
        self._VideoEditProjectInput = None
        self._VideoSegmentationProjectInput = None
        self._StreamConnectProjectInput = None
        self._RecordReplayProjectInput = None
        self._MediaCastProjectInput = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Name(self):
        """项目名称，不可超过30个字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Owner(self):
        """项目归属者，即项目的所有者，后续操作只有该所有者有权限操作。

注：目前所有项目只能设置归属个人，暂不支持团队项目。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Category(self):
        """项目类别，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
<li>SWITCHER：导播台。</li>
<li>VIDEO_SEGMENTATION：视频拆条。</li>
<li>STREAM_CONNECT：云转推。</li>
<li>RECORD_REPLAY：录制回放。</li>
<li>MEDIA_CAST：媒体转推。</li>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Mode(self):
        """项目模式，一个项目可以有多种模式并相互切换。
当 Category 为 VIDEO_EDIT 时，可选模式有：
<li>Default：默认模式，即普通视频编辑项目。</li>
<li>VideoEditTemplate：剪辑模板制作模式，用于制作剪辑模板。</li>

注：不填则为默认模式。
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def AspectRatio(self):
        warnings.warn("parameter `AspectRatio` is deprecated", DeprecationWarning) 

        """画布宽高比。
该字段已经废弃，请使用具体项目输入中的 AspectRatio 字段。
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        warnings.warn("parameter `AspectRatio` is deprecated", DeprecationWarning) 

        self._AspectRatio = AspectRatio

    @property
    def Description(self):
        """项目描述信息。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SwitcherProjectInput(self):
        """导播台项目输入信息，仅当项目类型为 SWITCHER 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.SwitcherProjectInput`
        """
        return self._SwitcherProjectInput

    @SwitcherProjectInput.setter
    def SwitcherProjectInput(self, SwitcherProjectInput):
        self._SwitcherProjectInput = SwitcherProjectInput

    @property
    def LiveStreamClipProjectInput(self):
        """直播剪辑项目输入信息，暂未开放，请勿使用。
        :rtype: :class:`tencentcloud.cme.v20191029.models.LiveStreamClipProjectInput`
        """
        return self._LiveStreamClipProjectInput

    @LiveStreamClipProjectInput.setter
    def LiveStreamClipProjectInput(self, LiveStreamClipProjectInput):
        self._LiveStreamClipProjectInput = LiveStreamClipProjectInput

    @property
    def VideoEditProjectInput(self):
        """视频编辑项目输入信息，仅当项目类型为 VIDEO_EDIT 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoEditProjectInput`
        """
        return self._VideoEditProjectInput

    @VideoEditProjectInput.setter
    def VideoEditProjectInput(self, VideoEditProjectInput):
        self._VideoEditProjectInput = VideoEditProjectInput

    @property
    def VideoSegmentationProjectInput(self):
        """视频拆条项目输入信息，仅当项目类型为 VIDEO_SEGMENTATION  时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoSegmentationProjectInput`
        """
        return self._VideoSegmentationProjectInput

    @VideoSegmentationProjectInput.setter
    def VideoSegmentationProjectInput(self, VideoSegmentationProjectInput):
        self._VideoSegmentationProjectInput = VideoSegmentationProjectInput

    @property
    def StreamConnectProjectInput(self):
        """云转推项目输入信息，仅当项目类型为 STREAM_CONNECT 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamConnectProjectInput`
        """
        return self._StreamConnectProjectInput

    @StreamConnectProjectInput.setter
    def StreamConnectProjectInput(self, StreamConnectProjectInput):
        self._StreamConnectProjectInput = StreamConnectProjectInput

    @property
    def RecordReplayProjectInput(self):
        """录制回放项目输入信息，仅当项目类型为 RECORD_REPLAY 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.RecordReplayProjectInput`
        """
        return self._RecordReplayProjectInput

    @RecordReplayProjectInput.setter
    def RecordReplayProjectInput(self, RecordReplayProjectInput):
        self._RecordReplayProjectInput = RecordReplayProjectInput

    @property
    def MediaCastProjectInput(self):
        """媒体转推项目输入信息，仅当项目类型为 MEDIA_CAST 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastProjectInput`
        """
        return self._MediaCastProjectInput

    @MediaCastProjectInput.setter
    def MediaCastProjectInput(self, MediaCastProjectInput):
        self._MediaCastProjectInput = MediaCastProjectInput


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Name = params.get("Name")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Category = params.get("Category")
        self._Mode = params.get("Mode")
        self._AspectRatio = params.get("AspectRatio")
        self._Description = params.get("Description")
        if params.get("SwitcherProjectInput") is not None:
            self._SwitcherProjectInput = SwitcherProjectInput()
            self._SwitcherProjectInput._deserialize(params.get("SwitcherProjectInput"))
        if params.get("LiveStreamClipProjectInput") is not None:
            self._LiveStreamClipProjectInput = LiveStreamClipProjectInput()
            self._LiveStreamClipProjectInput._deserialize(params.get("LiveStreamClipProjectInput"))
        if params.get("VideoEditProjectInput") is not None:
            self._VideoEditProjectInput = VideoEditProjectInput()
            self._VideoEditProjectInput._deserialize(params.get("VideoEditProjectInput"))
        if params.get("VideoSegmentationProjectInput") is not None:
            self._VideoSegmentationProjectInput = VideoSegmentationProjectInput()
            self._VideoSegmentationProjectInput._deserialize(params.get("VideoSegmentationProjectInput"))
        if params.get("StreamConnectProjectInput") is not None:
            self._StreamConnectProjectInput = StreamConnectProjectInput()
            self._StreamConnectProjectInput._deserialize(params.get("StreamConnectProjectInput"))
        if params.get("RecordReplayProjectInput") is not None:
            self._RecordReplayProjectInput = RecordReplayProjectInput()
            self._RecordReplayProjectInput._deserialize(params.get("RecordReplayProjectInput"))
        if params.get("MediaCastProjectInput") is not None:
            self._MediaCastProjectInput = MediaCastProjectInput()
            self._MediaCastProjectInput._deserialize(params.get("MediaCastProjectInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 Id。
        :type ProjectId: str
        :param _RtmpPushInputInfoSet: <li> 当 Catagory 为 STREAM_CONNECT 时，数组返回长度为2 ，第0个代表主输入源推流信息，第1个代表备输入源推流信息。只有当各自输入源类型为推流时才有有效内容。</li>
        :type RtmpPushInputInfoSet: list of RtmpPushInputInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectId = None
        self._RtmpPushInputInfoSet = None
        self._RequestId = None

    @property
    def ProjectId(self):
        """项目 Id。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RtmpPushInputInfoSet(self):
        """<li> 当 Catagory 为 STREAM_CONNECT 时，数组返回长度为2 ，第0个代表主输入源推流信息，第1个代表备输入源推流信息。只有当各自输入源类型为推流时才有有效内容。</li>
        :rtype: list of RtmpPushInputInfo
        """
        return self._RtmpPushInputInfoSet

    @RtmpPushInputInfoSet.setter
    def RtmpPushInputInfoSet(self, RtmpPushInputInfoSet):
        self._RtmpPushInputInfoSet = RtmpPushInputInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        if params.get("RtmpPushInputInfoSet") is not None:
            self._RtmpPushInputInfoSet = []
            for item in params.get("RtmpPushInputInfoSet"):
                obj = RtmpPushInputInfo()
                obj._deserialize(item)
                self._RtmpPushInputInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateTeamRequest(AbstractModel):
    """CreateTeam请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param _Name: 团队名称，限30个字符。
        :type Name: str
        :param _OwnerId: 团队所有者，指定用户 ID。
        :type OwnerId: str
        :param _OwnerRemark: 团队所有者的备注，限30个字符。
        :type OwnerRemark: str
        :param _TeamId: 自定义团队 ID。创建后不可修改，限20个英文字符及"-"。同时不能以 cmetid_开头。不填会生成默认团队 ID。
        :type TeamId: str
        """
        self._Platform = None
        self._Name = None
        self._OwnerId = None
        self._OwnerRemark = None
        self._TeamId = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Name(self):
        """团队名称，限30个字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OwnerId(self):
        """团队所有者，指定用户 ID。
        :rtype: str
        """
        return self._OwnerId

    @OwnerId.setter
    def OwnerId(self, OwnerId):
        self._OwnerId = OwnerId

    @property
    def OwnerRemark(self):
        """团队所有者的备注，限30个字符。
        :rtype: str
        """
        return self._OwnerRemark

    @OwnerRemark.setter
    def OwnerRemark(self, OwnerRemark):
        self._OwnerRemark = OwnerRemark

    @property
    def TeamId(self):
        """自定义团队 ID。创建后不可修改，限20个英文字符及"-"。同时不能以 cmetid_开头。不填会生成默认团队 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Name = params.get("Name")
        self._OwnerId = params.get("OwnerId")
        self._OwnerRemark = params.get("OwnerRemark")
        self._TeamId = params.get("TeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTeamResponse(AbstractModel):
    """CreateTeam返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TeamId: 创建的团队 ID。
        :type TeamId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TeamId = None
        self._RequestId = None

    @property
    def TeamId(self):
        """创建的团队 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._RequestId = params.get("RequestId")


class CreateVideoEncodingPresetRequest(AbstractModel):
    """CreateVideoEncodingPreset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param _Name: 配置名，可用来简单描述该配置的作用。
        :type Name: str
        :param _Container: 封装格式，可选值：
<li>mp4 ；</li>
<li>mov 。</li>
默认值：mp4。
        :type Container: str
        :param _RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :type RemoveVideo: int
        :param _RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :type RemoveAudio: int
        :param _VideoSetting: 编码配置的视频设置。默认值参考VideoEncodingPresetVideoSetting 定义。
        :type VideoSetting: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetVideoSetting`
        :param _AudioSetting: 编码配置的音频设置。默认值参考VideoEncodingPresetAudioSetting 定义。
        :type AudioSetting: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetAudioSetting`
        """
        self._Platform = None
        self._Name = None
        self._Container = None
        self._RemoveVideo = None
        self._RemoveAudio = None
        self._VideoSetting = None
        self._AudioSetting = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Name(self):
        """配置名，可用来简单描述该配置的作用。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Container(self):
        """封装格式，可选值：
<li>mp4 ；</li>
<li>mov 。</li>
默认值：mp4。
        :rtype: str
        """
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def RemoveVideo(self):
        """是否去除视频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :rtype: int
        """
        return self._RemoveVideo

    @RemoveVideo.setter
    def RemoveVideo(self, RemoveVideo):
        self._RemoveVideo = RemoveVideo

    @property
    def RemoveAudio(self):
        """是否去除音频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :rtype: int
        """
        return self._RemoveAudio

    @RemoveAudio.setter
    def RemoveAudio(self, RemoveAudio):
        self._RemoveAudio = RemoveAudio

    @property
    def VideoSetting(self):
        """编码配置的视频设置。默认值参考VideoEncodingPresetVideoSetting 定义。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetVideoSetting`
        """
        return self._VideoSetting

    @VideoSetting.setter
    def VideoSetting(self, VideoSetting):
        self._VideoSetting = VideoSetting

    @property
    def AudioSetting(self):
        """编码配置的音频设置。默认值参考VideoEncodingPresetAudioSetting 定义。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetAudioSetting`
        """
        return self._AudioSetting

    @AudioSetting.setter
    def AudioSetting(self, AudioSetting):
        self._AudioSetting = AudioSetting


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Name = params.get("Name")
        self._Container = params.get("Container")
        self._RemoveVideo = params.get("RemoveVideo")
        self._RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoSetting") is not None:
            self._VideoSetting = VideoEncodingPresetVideoSetting()
            self._VideoSetting._deserialize(params.get("VideoSetting"))
        if params.get("AudioSetting") is not None:
            self._AudioSetting = VideoEncodingPresetAudioSetting()
            self._AudioSetting._deserialize(params.get("AudioSetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoEncodingPresetResponse(AbstractModel):
    """CreateVideoEncodingPreset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 模板 ID。
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """模板 ID。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class DeleteClassRequest(AbstractModel):
    """DeleteClass请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param _Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _ClassPath: 分类路径。
        :type ClassPath: str
        :param _Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self._Platform = None
        self._Owner = None
        self._ClassPath = None
        self._Operator = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Owner(self):
        """归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def ClassPath(self):
        """分类路径。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath

    @property
    def Operator(self):
        """操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._ClassPath = params.get("ClassPath")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClassResponse(AbstractModel):
    """DeleteClass返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLoginStatusRequest(AbstractModel):
    """DeleteLoginStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param _UserIds: 用户 Id 列表，N 从 0 开始取值，最大 19。
        :type UserIds: list of str
        """
        self._Platform = None
        self._UserIds = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def UserIds(self):
        """用户 Id 列表，N 从 0 开始取值，最大 19。
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoginStatusResponse(AbstractModel):
    """DeleteLoginStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteMaterialRequest(AbstractModel):
    """DeleteMaterial请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param _MaterialId: 媒体 Id。
        :type MaterialId: str
        :param _Operator: 操作者。填写用户的 Id，用于标识调用者及校验媒体删除权限。
        :type Operator: str
        """
        self._Platform = None
        self._MaterialId = None
        self._Operator = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def MaterialId(self):
        """媒体 Id。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def Operator(self):
        """操作者。填写用户的 Id，用于标识调用者及校验媒体删除权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._MaterialId = params.get("MaterialId")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMaterialResponse(AbstractModel):
    """DeleteMaterial返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ProjectId: 要删除的项目 Id。
        :type ProjectId: str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以删除一切项目。如果指定操作者，则操作者必须为项目所有者。
        :type Operator: str
        """
        self._Platform = None
        self._ProjectId = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectId(self):
        """要删除的项目 Id。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以删除一切项目。如果指定操作者，则操作者必须为项目所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectId = params.get("ProjectId")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTeamMembersRequest(AbstractModel):
    """DeleteTeamMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _TeamId: 团队 ID。
        :type TeamId: str
        :param _MemberIds: 要删除的成员列表。
        :type MemberIds: list of str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以删除所有团队的成员。如果指定操作者，则操作者必须为团队管理员或者所有者。
        :type Operator: str
        """
        self._Platform = None
        self._TeamId = None
        self._MemberIds = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TeamId(self):
        """团队 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def MemberIds(self):
        """要删除的成员列表。
        :rtype: list of str
        """
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以删除所有团队的成员。如果指定操作者，则操作者必须为团队管理员或者所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._TeamId = params.get("TeamId")
        self._MemberIds = params.get("MemberIds")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTeamMembersResponse(AbstractModel):
    """DeleteTeamMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTeamRequest(AbstractModel):
    """DeleteTeam请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _TeamId: 要删除的团队  ID。
        :type TeamId: str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以删除所有团队。如果指定操作者，则操作者必须为团队所有者。
        :type Operator: str
        """
        self._Platform = None
        self._TeamId = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TeamId(self):
        """要删除的团队  ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以删除所有团队。如果指定操作者，则操作者必须为团队所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._TeamId = params.get("TeamId")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTeamResponse(AbstractModel):
    """DeleteTeam返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteVideoEncodingPresetRequest(AbstractModel):
    """DeleteVideoEncodingPreset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param _Id: 要删除的视频编码配置 ID。
        :type Id: int
        """
        self._Platform = None
        self._Id = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Id(self):
        """要删除的视频编码配置 ID。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVideoEncodingPresetResponse(AbstractModel):
    """DeleteVideoEncodingPreset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Phone: 手机号码。指定手机号获取账号信息，目前仅支持国内手机号，且号码不加地区码 `+86` 等。
        :type Phone: str
        :param _Offset: 分页返回的起始偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值：10，最大值：20。
        :type Limit: int
        """
        self._Platform = None
        self._Phone = None
        self._Offset = None
        self._Limit = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Phone(self):
        """手机号码。指定手机号获取账号信息，目前仅支持国内手机号，且号码不加地区码 `+86` 等。
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Offset(self):
        """分页返回的起始偏移量，默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页返回的记录条数，默认值：10，最大值：20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Phone = params.get("Phone")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合搜索条件的记录总数。
        :type TotalCount: int
        :param _AccountInfoSet: 账号信息列表。
        :type AccountInfoSet: list of AccountInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccountInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合搜索条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountInfoSet(self):
        """账号信息列表。
        :rtype: list of AccountInfo
        """
        return self._AccountInfoSet

    @AccountInfoSet.setter
    def AccountInfoSet(self, AccountInfoSet):
        self._AccountInfoSet = AccountInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccountInfoSet") is not None:
            self._AccountInfoSet = []
            for item in params.get("AccountInfoSet"):
                obj = AccountInfo()
                obj._deserialize(item)
                self._AccountInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClassRequest(AbstractModel):
    """DescribeClass请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param _Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self._Platform = None
        self._Owner = None
        self._Operator = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Owner(self):
        """归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Operator(self):
        """操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassResponse(AbstractModel):
    """DescribeClass返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClassInfoSet: 分类信息列表。
        :type ClassInfoSet: list of ClassInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClassInfoSet = None
        self._RequestId = None

    @property
    def ClassInfoSet(self):
        """分类信息列表。
        :rtype: list of ClassInfo
        """
        return self._ClassInfoSet

    @ClassInfoSet.setter
    def ClassInfoSet(self, ClassInfoSet):
        self._ClassInfoSet = ClassInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClassInfoSet") is not None:
            self._ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = ClassInfo()
                obj._deserialize(item)
                self._ClassInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJoinTeamsRequest(AbstractModel):
    """DescribeJoinTeams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _MemberId: 团队成员　ID。
        :type MemberId: str
        :param _Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 返回记录条数，默认值：30，最大值：30。
        :type Limit: int
        """
        self._Platform = None
        self._MemberId = None
        self._Offset = None
        self._Limit = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def MemberId(self):
        """团队成员　ID。
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Offset(self):
        """分页偏移量，默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回记录条数，默认值：30，最大值：30。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._MemberId = params.get("MemberId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJoinTeamsResponse(AbstractModel):
    """DescribeJoinTeams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _TeamSet: 团队列表。
        :type TeamSet: list of JoinTeamInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TeamSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TeamSet(self):
        """团队列表。
        :rtype: list of JoinTeamInfo
        """
        return self._TeamSet

    @TeamSet.setter
    def TeamSet(self, TeamSet):
        self._TeamSet = TeamSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TeamSet") is not None:
            self._TeamSet = []
            for item in params.get("TeamSet"):
                obj = JoinTeamInfo()
                obj._deserialize(item)
                self._TeamSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoginStatusRequest(AbstractModel):
    """DescribeLoginStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _UserIds: 用户 Id 列表，N 从0开始取值，最大19。
        :type UserIds: list of str
        """
        self._Platform = None
        self._UserIds = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def UserIds(self):
        """用户 Id 列表，N 从0开始取值，最大19。
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoginStatusResponse(AbstractModel):
    """DescribeLoginStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginStatusInfoSet: 用户登录状态列表。
        :type LoginStatusInfoSet: list of LoginStatusInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoginStatusInfoSet = None
        self._RequestId = None

    @property
    def LoginStatusInfoSet(self):
        """用户登录状态列表。
        :rtype: list of LoginStatusInfo
        """
        return self._LoginStatusInfoSet

    @LoginStatusInfoSet.setter
    def LoginStatusInfoSet(self, LoginStatusInfoSet):
        self._LoginStatusInfoSet = LoginStatusInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoginStatusInfoSet") is not None:
            self._LoginStatusInfoSet = []
            for item in params.get("LoginStatusInfoSet"):
                obj = LoginStatusInfo()
                obj._deserialize(item)
                self._LoginStatusInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMaterialsRequest(AbstractModel):
    """DescribeMaterials请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _MaterialIds: 媒体 ID 列表，一次最多可拉取20个媒体的信息。
        :type MaterialIds: list of str
        :param _Sort: 列表排序，支持下列排序字段：
<li>CreateTime：创建时间；</li>
<li>UpdateTime：更新时间。</li>
        :type Sort: :class:`tencentcloud.cme.v20191029.models.SortBy`
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以获取任意媒体的信息。如果指定操作者，则操作者必须对媒体有读权限。
        :type Operator: str
        """
        self._Platform = None
        self._MaterialIds = None
        self._Sort = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def MaterialIds(self):
        """媒体 ID 列表，一次最多可拉取20个媒体的信息。
        :rtype: list of str
        """
        return self._MaterialIds

    @MaterialIds.setter
    def MaterialIds(self, MaterialIds):
        self._MaterialIds = MaterialIds

    @property
    def Sort(self):
        """列表排序，支持下列排序字段：
<li>CreateTime：创建时间；</li>
<li>UpdateTime：更新时间。</li>
        :rtype: :class:`tencentcloud.cme.v20191029.models.SortBy`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以获取任意媒体的信息。如果指定操作者，则操作者必须对媒体有读权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._MaterialIds = params.get("MaterialIds")
        if params.get("Sort") is not None:
            self._Sort = SortBy()
            self._Sort._deserialize(params.get("Sort"))
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaterialsResponse(AbstractModel):
    """DescribeMaterials返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MaterialInfoSet: 媒体列表信息。
        :type MaterialInfoSet: list of MaterialInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MaterialInfoSet = None
        self._RequestId = None

    @property
    def MaterialInfoSet(self):
        """媒体列表信息。
        :rtype: list of MaterialInfo
        """
        return self._MaterialInfoSet

    @MaterialInfoSet.setter
    def MaterialInfoSet(self, MaterialInfoSet):
        self._MaterialInfoSet = MaterialInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MaterialInfoSet") is not None:
            self._MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self._MaterialInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePlatformsRequest(AbstractModel):
    """DescribePlatforms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platforms: 平台 Id 列表。如果不填，则不按平台 Id 进行过滤。
        :type Platforms: list of str
        :param _LicenseIds: 平台绑定的 License Id 列表。如果不填，则不按平台绑定的 License Id 进行过滤。
        :type LicenseIds: list of str
        :param _Offset: 分页返回的起始偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值：10，最大值：20。
        :type Limit: int
        """
        self._Platforms = None
        self._LicenseIds = None
        self._Offset = None
        self._Limit = None

    @property
    def Platforms(self):
        """平台 Id 列表。如果不填，则不按平台 Id 进行过滤。
        :rtype: list of str
        """
        return self._Platforms

    @Platforms.setter
    def Platforms(self, Platforms):
        self._Platforms = Platforms

    @property
    def LicenseIds(self):
        """平台绑定的 License Id 列表。如果不填，则不按平台绑定的 License Id 进行过滤。
        :rtype: list of str
        """
        return self._LicenseIds

    @LicenseIds.setter
    def LicenseIds(self, LicenseIds):
        self._LicenseIds = LicenseIds

    @property
    def Offset(self):
        """分页返回的起始偏移量，默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页返回的记录条数，默认值：10，最大值：20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Platforms = params.get("Platforms")
        self._LicenseIds = params.get("LicenseIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlatformsResponse(AbstractModel):
    """DescribePlatforms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的记录总数。
        :type TotalCount: int
        :param _PlatformInfoSet: 平台信息列表。
        :type PlatformInfoSet: list of PlatformInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PlatformInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合查询条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PlatformInfoSet(self):
        """平台信息列表。
        :rtype: list of PlatformInfo
        """
        return self._PlatformInfoSet

    @PlatformInfoSet.setter
    def PlatformInfoSet(self, PlatformInfoSet):
        self._PlatformInfoSet = PlatformInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PlatformInfoSet") is not None:
            self._PlatformInfoSet = []
            for item in params.get("PlatformInfoSet"):
                obj = PlatformInfo()
                obj._deserialize(item)
                self._PlatformInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ProjectIds: 项目 Id 过滤参数列表，最大支持20个项目 Id 过滤。如果不填不需要项目 Id 进行过滤。
        :type ProjectIds: list of str
        :param _AspectRatioSet: 画布宽高比过滤参数列表。如果不填则不用画布宽高比进行过滤。
        :type AspectRatioSet: list of str
        :param _CategorySet: 项目类型过滤参数列表，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
<li>SWITCHER：导播台。</li>
<li>VIDEO_SEGMENTATION：视频拆条。</li>
<li>STREAM_CONNECT：云转推。</li>
<li>RECORD_REPLAY：录制回放。</li>
<li>MEDIA_CAST：点播转直播。</li>

注：如果不填则不使用项目类型进行过滤。
        :type CategorySet: list of str
        :param _Modes: 项目模式过滤参数列表，一个项目可以有多种模式并相互切换。
当 Category 为 VIDEO_EDIT 时，可选模式有：
<li>Default：默认模式。</li>
<li>VideoEditTemplate：视频编辑模板制作模式。</li>

注：不填不使用项目模式进行过滤。
        :type Modes: list of str
        :param _Sort: 结果排序方式，支持下列排序字段：
<li>CreateTime：创建时间；</li>
<li>UpdateTime：更新时间。</li>

注：如不填，则使用项目创建时间倒序排列。
        :type Sort: :class:`tencentcloud.cme.v20191029.models.SortBy`
        :param _Owner: 项目所有者，目前仅支持个人项目过滤。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Offset: 分页返回的起始偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值：10。
        :type Limit: int
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以查询一切用户项目信息。如果指定操作者，则操作者必须为项目所有者。
        :type Operator: str
        """
        self._Platform = None
        self._ProjectIds = None
        self._AspectRatioSet = None
        self._CategorySet = None
        self._Modes = None
        self._Sort = None
        self._Owner = None
        self._Offset = None
        self._Limit = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectIds(self):
        """项目 Id 过滤参数列表，最大支持20个项目 Id 过滤。如果不填不需要项目 Id 进行过滤。
        :rtype: list of str
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def AspectRatioSet(self):
        """画布宽高比过滤参数列表。如果不填则不用画布宽高比进行过滤。
        :rtype: list of str
        """
        return self._AspectRatioSet

    @AspectRatioSet.setter
    def AspectRatioSet(self, AspectRatioSet):
        self._AspectRatioSet = AspectRatioSet

    @property
    def CategorySet(self):
        """项目类型过滤参数列表，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
<li>SWITCHER：导播台。</li>
<li>VIDEO_SEGMENTATION：视频拆条。</li>
<li>STREAM_CONNECT：云转推。</li>
<li>RECORD_REPLAY：录制回放。</li>
<li>MEDIA_CAST：点播转直播。</li>

注：如果不填则不使用项目类型进行过滤。
        :rtype: list of str
        """
        return self._CategorySet

    @CategorySet.setter
    def CategorySet(self, CategorySet):
        self._CategorySet = CategorySet

    @property
    def Modes(self):
        """项目模式过滤参数列表，一个项目可以有多种模式并相互切换。
当 Category 为 VIDEO_EDIT 时，可选模式有：
<li>Default：默认模式。</li>
<li>VideoEditTemplate：视频编辑模板制作模式。</li>

注：不填不使用项目模式进行过滤。
        :rtype: list of str
        """
        return self._Modes

    @Modes.setter
    def Modes(self, Modes):
        self._Modes = Modes

    @property
    def Sort(self):
        """结果排序方式，支持下列排序字段：
<li>CreateTime：创建时间；</li>
<li>UpdateTime：更新时间。</li>

注：如不填，则使用项目创建时间倒序排列。
        :rtype: :class:`tencentcloud.cme.v20191029.models.SortBy`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Owner(self):
        """项目所有者，目前仅支持个人项目过滤。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Offset(self):
        """分页返回的起始偏移量，默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页返回的记录条数，默认值：10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以查询一切用户项目信息。如果指定操作者，则操作者必须为项目所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectIds = params.get("ProjectIds")
        self._AspectRatioSet = params.get("AspectRatioSet")
        self._CategorySet = params.get("CategorySet")
        self._Modes = params.get("Modes")
        if params.get("Sort") is not None:
            self._Sort = SortBy()
            self._Sort._deserialize(params.get("Sort"))
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _ProjectInfoSet: 项目信息列表。
        :type ProjectInfoSet: list of ProjectInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProjectInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProjectInfoSet(self):
        """项目信息列表。
        :rtype: list of ProjectInfo
        """
        return self._ProjectInfoSet

    @ProjectInfoSet.setter
    def ProjectInfoSet(self, ProjectInfoSet):
        self._ProjectInfoSet = ProjectInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ProjectInfoSet") is not None:
            self._ProjectInfoSet = []
            for item in params.get("ProjectInfoSet"):
                obj = ProjectInfo()
                obj._deserialize(item)
                self._ProjectInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceAuthorizationRequest(AbstractModel):
    """DescribeResourceAuthorization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Resource: 资源。
        :type Resource: :class:`tencentcloud.cme.v20191029.models.Resource`
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以查询任意资源的被授权情况。如果指定操作者，则操作者必须对被授权资源有读权限。
        :type Operator: str
        """
        self._Platform = None
        self._Owner = None
        self._Resource = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Owner(self):
        """归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Resource(self):
        """资源。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Resource`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以查询任意资源的被授权情况。如果指定操作者，则操作者必须对被授权资源有读权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        if params.get("Resource") is not None:
            self._Resource = Resource()
            self._Resource._deserialize(params.get("Resource"))
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceAuthorizationResponse(AbstractModel):
    """DescribeResourceAuthorization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的资源授权记录总数。
        :type TotalCount: int
        :param _AuthorizationInfoSet: 授权信息列表。
        :type AuthorizationInfoSet: list of AuthorizationInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AuthorizationInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的资源授权记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AuthorizationInfoSet(self):
        """授权信息列表。
        :rtype: list of AuthorizationInfo
        """
        return self._AuthorizationInfoSet

    @AuthorizationInfoSet.setter
    def AuthorizationInfoSet(self, AuthorizationInfoSet):
        self._AuthorizationInfoSet = AuthorizationInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AuthorizationInfoSet") is not None:
            self._AuthorizationInfoSet = []
            for item in params.get("AuthorizationInfoSet"):
                obj = AuthorizationInfo()
                obj._deserialize(item)
                self._AuthorizationInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSharedSpaceRequest(AbstractModel):
    """DescribeSharedSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Authorizee: 被授权目标，个人或团队。
        :type Authorizee: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以查询任意个人或者团队的共享空间。如果指定操作者，则操作者必须本人或者团队成员。
        :type Operator: str
        """
        self._Platform = None
        self._Authorizee = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Authorizee(self):
        """被授权目标，个人或团队。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Authorizee

    @Authorizee.setter
    def Authorizee(self, Authorizee):
        self._Authorizee = Authorizee

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以查询任意个人或者团队的共享空间。如果指定操作者，则操作者必须本人或者团队成员。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("Authorizee") is not None:
            self._Authorizee = Entity()
            self._Authorizee._deserialize(params.get("Authorizee"))
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSharedSpaceResponse(AbstractModel):
    """DescribeSharedSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询到的共享空间总数。
        :type TotalCount: int
        :param _AuthorizerSet: 各个共享空间对应的授权者信息。
        :type AuthorizerSet: list of Authorizer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AuthorizerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """查询到的共享空间总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AuthorizerSet(self):
        """各个共享空间对应的授权者信息。
        :rtype: list of Authorizer
        """
        return self._AuthorizerSet

    @AuthorizerSet.setter
    def AuthorizerSet(self, AuthorizerSet):
        self._AuthorizerSet = AuthorizerSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AuthorizerSet") is not None:
            self._AuthorizerSet = []
            for item in params.get("AuthorizerSet"):
                obj = Authorizer()
                obj._deserialize(item)
                self._AuthorizerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _TaskId: 任务 Id。
        :type TaskId: str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以获取任意任务信息。如果指定操作者，则操作者需要是任务发起者。
        :type Operator: str
        """
        self._Platform = None
        self._TaskId = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TaskId(self):
        """任务 Id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以获取任意任务信息。如果指定操作者，则操作者需要是任务发起者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._TaskId = params.get("TaskId")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，取值有：
<li>PROCESSING：处理中：</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :type Status: str
        :param _Progress: 任务进度，取值为：0~100。
        :type Progress: int
        :param _ErrCode: 错误码。
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param _ErrMsg: 错误信息。
        :type ErrMsg: str
        :param _TaskType: 任务类型，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：视频编辑项目导出。</li>
        :type TaskType: str
        :param _VideoEditProjectOutput: 导出项目输出信息。仅当 TaskType 为 VIDEO_EDIT_PROJECT_EXPORT 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoEditProjectOutput: :class:`tencentcloud.cme.v20191029.models.VideoEditProjectOutput`
        :param _CreateTime: 创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Progress = None
        self._ErrCode = None
        self._ErrMsg = None
        self._TaskType = None
        self._VideoEditProjectOutput = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def Status(self):
        """任务状态，取值有：
<li>PROCESSING：处理中：</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        """任务进度，取值为：0~100。
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def ErrCode(self):
        """错误码。
<li>0：成功；</li>
<li>其他值：失败。</li>
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """错误信息。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def TaskType(self):
        """任务类型，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：视频编辑项目导出。</li>
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def VideoEditProjectOutput(self):
        """导出项目输出信息。仅当 TaskType 为 VIDEO_EDIT_PROJECT_EXPORT 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoEditProjectOutput`
        """
        return self._VideoEditProjectOutput

    @VideoEditProjectOutput.setter
    def VideoEditProjectOutput(self, VideoEditProjectOutput):
        self._VideoEditProjectOutput = VideoEditProjectOutput

    @property
    def CreateTime(self):
        """创建时间，格式按照 ISO 8601 标准表示。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        self._TaskType = params.get("TaskType")
        if params.get("VideoEditProjectOutput") is not None:
            self._VideoEditProjectOutput = VideoEditProjectOutput()
            self._VideoEditProjectOutput._deserialize(params.get("VideoEditProjectOutput"))
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ProjectId: 项目 Id，使用项目 Id 进行过滤。
        :type ProjectId: str
        :param _TaskTypeSet: 任务类型集合，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：视频编辑项目导出。</li>

注：不填不使用任务类型进行过滤。
        :type TaskTypeSet: list of str
        :param _StatusSet: 任务状态集合，取值有：
<li>PROCESSING：处理中；</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>

注：不填则不使用任务状态进行过滤。
        :type StatusSet: list of str
        :param _Offset: 分页返回的起始偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值：10。最大值：20。
        :type Limit: int
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以获取所有任务信息。如果指定操作者，则操作者需要是任务发起者。
        :type Operator: str
        """
        self._Platform = None
        self._ProjectId = None
        self._TaskTypeSet = None
        self._StatusSet = None
        self._Offset = None
        self._Limit = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectId(self):
        """项目 Id，使用项目 Id 进行过滤。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskTypeSet(self):
        """任务类型集合，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：视频编辑项目导出。</li>

注：不填不使用任务类型进行过滤。
        :rtype: list of str
        """
        return self._TaskTypeSet

    @TaskTypeSet.setter
    def TaskTypeSet(self, TaskTypeSet):
        self._TaskTypeSet = TaskTypeSet

    @property
    def StatusSet(self):
        """任务状态集合，取值有：
<li>PROCESSING：处理中；</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>

注：不填则不使用任务状态进行过滤。
        :rtype: list of str
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def Offset(self):
        """分页返回的起始偏移量，默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页返回的记录条数，默认值：10。最大值：20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以获取所有任务信息。如果指定操作者，则操作者需要是任务发起者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectId = params.get("ProjectId")
        self._TaskTypeSet = params.get("TaskTypeSet")
        self._StatusSet = params.get("StatusSet")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合搜索条件的记录总数。
        :type TotalCount: int
        :param _TaskBaseInfoSet: 任务基础信息列表。
        :type TaskBaseInfoSet: list of TaskBaseInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskBaseInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合搜索条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskBaseInfoSet(self):
        """任务基础信息列表。
        :rtype: list of TaskBaseInfo
        """
        return self._TaskBaseInfoSet

    @TaskBaseInfoSet.setter
    def TaskBaseInfoSet(self, TaskBaseInfoSet):
        self._TaskBaseInfoSet = TaskBaseInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskBaseInfoSet") is not None:
            self._TaskBaseInfoSet = []
            for item in params.get("TaskBaseInfoSet"):
                obj = TaskBaseInfo()
                obj._deserialize(item)
                self._TaskBaseInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTeamMembersRequest(AbstractModel):
    """DescribeTeamMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _TeamId: 团队 ID。
        :type TeamId: str
        :param _MemberIds: 成员 ID 列表，限指定30个指定成员。如不填，则返回指定团队下的所有成员。
        :type MemberIds: list of str
        :param _Offset: 分页偏移量，默认值：0
        :type Offset: int
        :param _Limit: 返回记录条数，默认值：30，最大值：30。
        :type Limit: int
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以拉取任意团队成员的信息。如果指定操作者，则操作者必须为团队成员。
        :type Operator: str
        """
        self._Platform = None
        self._TeamId = None
        self._MemberIds = None
        self._Offset = None
        self._Limit = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TeamId(self):
        """团队 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def MemberIds(self):
        """成员 ID 列表，限指定30个指定成员。如不填，则返回指定团队下的所有成员。
        :rtype: list of str
        """
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds

    @property
    def Offset(self):
        """分页偏移量，默认值：0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回记录条数，默认值：30，最大值：30。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以拉取任意团队成员的信息。如果指定操作者，则操作者必须为团队成员。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._TeamId = params.get("TeamId")
        self._MemberIds = params.get("MemberIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTeamMembersResponse(AbstractModel):
    """DescribeTeamMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _MemberSet: 团队成员列表。
        :type MemberSet: list of TeamMemberInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MemberSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MemberSet(self):
        """团队成员列表。
        :rtype: list of TeamMemberInfo
        """
        return self._MemberSet

    @MemberSet.setter
    def MemberSet(self, MemberSet):
        self._MemberSet = MemberSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("MemberSet") is not None:
            self._MemberSet = []
            for item in params.get("MemberSet"):
                obj = TeamMemberInfo()
                obj._deserialize(item)
                self._MemberSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTeamsRequest(AbstractModel):
    """DescribeTeams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _TeamIds: 团队 ID 列表，限30个。若不填，则默认获取平台下所有团队。
        :type TeamIds: list of str
        :param _Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 返回记录条数，默认值：20，最大值：30。
        :type Limit: int
        """
        self._Platform = None
        self._TeamIds = None
        self._Offset = None
        self._Limit = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TeamIds(self):
        """团队 ID 列表，限30个。若不填，则默认获取平台下所有团队。
        :rtype: list of str
        """
        return self._TeamIds

    @TeamIds.setter
    def TeamIds(self, TeamIds):
        self._TeamIds = TeamIds

    @property
    def Offset(self):
        """分页偏移量，默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回记录条数，默认值：20，最大值：30。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._TeamIds = params.get("TeamIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTeamsResponse(AbstractModel):
    """DescribeTeams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _TeamSet: 团队列表。
        :type TeamSet: list of TeamInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TeamSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TeamSet(self):
        """团队列表。
        :rtype: list of TeamInfo
        """
        return self._TeamSet

    @TeamSet.setter
    def TeamSet(self, TeamSet):
        self._TeamSet = TeamSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TeamSet") is not None:
            self._TeamSet = []
            for item in params.get("TeamSet"):
                obj = TeamInfo()
                obj._deserialize(item)
                self._TeamSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVideoEncodingPresetsRequest(AbstractModel):
    """DescribeVideoEncodingPresets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Ids: 要查询的配置 ID 列表。填写该参数则按照配置 ID 进行查询。
        :type Ids: list of int non-negative
        :param _Limit: 分页大小，默认20。最大值50。
        :type Limit: int
        :param _Offset: 分页起始，默认0。
        :type Offset: int
        """
        self._Platform = None
        self._Ids = None
        self._Limit = None
        self._Offset = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Ids(self):
        """要查询的配置 ID 列表。填写该参数则按照配置 ID 进行查询。
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids

    @property
    def Limit(self):
        """分页大小，默认20。最大值50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页起始，默认0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Ids = params.get("Ids")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoEncodingPresetsResponse(AbstractModel):
    """DescribeVideoEncodingPresets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的编码配置总个数。
        :type TotalCount: int
        :param _VideoEncodingPresetSet: 视频编码配置信息。
        :type VideoEncodingPresetSet: list of VideoEncodingPreset
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VideoEncodingPresetSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的编码配置总个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VideoEncodingPresetSet(self):
        """视频编码配置信息。
        :rtype: list of VideoEncodingPreset
        """
        return self._VideoEncodingPresetSet

    @VideoEncodingPresetSet.setter
    def VideoEncodingPresetSet(self, VideoEncodingPresetSet):
        self._VideoEncodingPresetSet = VideoEncodingPresetSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VideoEncodingPresetSet") is not None:
            self._VideoEncodingPresetSet = []
            for item in params.get("VideoEncodingPresetSet"):
                obj = VideoEncodingPreset()
                obj._deserialize(item)
                self._VideoEncodingPresetSet.append(obj)
        self._RequestId = params.get("RequestId")


class EmptyTrackItem(AbstractModel):
    """空的轨道片段，用来进行时间轴的占位。如需要两个音频片段之间有一段时间的静音，可以用 EmptyTrackItem 来进行占位。

    """

    def __init__(self):
        r"""
        :param _Duration: 持续时间，单位为秒。
        :type Duration: float
        """
        self._Duration = None

    @property
    def Duration(self):
        """持续时间，单位为秒。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Entity(AbstractModel):
    """用于描述资源的归属，归属者为个人或者团队。

    """

    def __init__(self):
        r"""
        :param _Type: 类型，取值有：
<li>PERSON：个人。</li>
<li>TEAM：团队。</li>
        :type Type: str
        :param _Id: Id，当 Type=PERSON，取值为用户 Id，当 Type=TEAM，取值为团队 Id。
        :type Id: str
        """
        self._Type = None
        self._Id = None

    @property
    def Type(self):
        """类型，取值有：
<li>PERSON：个人。</li>
<li>TEAM：团队。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Id(self):
        """Id，当 Type=PERSON，取值为用户 Id，当 Type=TEAM，取值为团队 Id。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventContent(AbstractModel):
    """回调事件内容。

    """

    def __init__(self):
        r"""
        :param _EventType: 事件类型，可取值有：
<li>Storage.NewFileCreated：新文件产生事件；</li>
<li>Project.StreamConnect.StatusChanged：云转推项目状态变更事件；</li>
<li>Project.Switcher.StatusChanged：导播台项目状态变更事件；</li>
<li>Material.Imported：媒体导入事件；</li>
<li>Material.Added：媒体添加事件；</li>
<li>Material.Moved：媒体移动事件；</li>
<li>Material.Modified：媒体变更事件；</li>
<li>Material.Deleted：媒体删除事件；</li>
<li>Class.Created：分类新增事件；</li>
<li>Class.Moved：分类移动事件；</li>
<li>Class.Deleted：分类删除事件；</li>
<li>Task.VideoExportCompleted：视频导出完成事件； </li>
<li>Project.MediaCast.StatusChanged：点播转直播项目状态变更事件。 </li>
        :type EventType: str
        :param _Operator: 操作者，表示触发事件的操作者。如果是 `cmeid_system` 表示平台管理员操作。
        :type Operator: str
        :param _StorageNewFileCreatedEvent: 新文件产生事件。仅当 EventType 为 Storage.NewFileCreated 时有效。
        :type StorageNewFileCreatedEvent: :class:`tencentcloud.cme.v20191029.models.StorageNewFileCreatedEvent`
        :param _ProjectStreamConnectStatusChangedEvent: 云转推项目状态变更事件。仅当 EventType 为 Project.StreamConnect.StatusChanged 时有效。
        :type ProjectStreamConnectStatusChangedEvent: :class:`tencentcloud.cme.v20191029.models.ProjectStreamConnectStatusChangedEvent`
        :param _ProjectSwitcherStatusChangedEvent: 导播台项目状态变更事件。仅当 EventType 为 Project.Switcher.StatusChanged 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectSwitcherStatusChangedEvent: :class:`tencentcloud.cme.v20191029.models.ProjectSwitcherStatusChangedEvent`
        :param _MaterialImportedEvent: 媒体导入事件。仅当 EventType 为 Material.Imported 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialImportedEvent: :class:`tencentcloud.cme.v20191029.models.MaterialImportedEvent`
        :param _MaterialAddedEvent: 媒体添加事件。仅当 EventType 为 Material.Added 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialAddedEvent: :class:`tencentcloud.cme.v20191029.models.MaterialAddedEvent`
        :param _MaterialMovedEvent: 媒体移动事件。仅当 EventType 为 Material.Moved 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialMovedEvent: :class:`tencentcloud.cme.v20191029.models.MaterialMovedEvent`
        :param _MaterialModifiedEvent: 媒体更新事件。仅当 EventType 为 Material.Modified 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialModifiedEvent: :class:`tencentcloud.cme.v20191029.models.MaterialModifiedEvent`
        :param _MaterialDeletedEvent: 媒体删除事件。仅当 EventType 为 Material.Deleted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialDeletedEvent: :class:`tencentcloud.cme.v20191029.models.MaterialDeletedEvent`
        :param _ClassCreatedEvent: 分类创建事件。仅当 EventType 为 Class.Created 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassCreatedEvent: :class:`tencentcloud.cme.v20191029.models.ClassCreatedEvent`
        :param _ClassMovedEvent: 分类移动事件。仅当 EventType 为 Class.Moved 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassMovedEvent: :class:`tencentcloud.cme.v20191029.models.ClassMovedEvent`
        :param _ClassDeletedEvent: 分类删除事件。仅当 EventType 为 Class.Deleted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassDeletedEvent: :class:`tencentcloud.cme.v20191029.models.ClassDeletedEvent`
        :param _VideoExportCompletedEvent: 视频导出完成事件。仅当 EventType 为 Task.VideoExportCompleted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoExportCompletedEvent: :class:`tencentcloud.cme.v20191029.models.VideoExportCompletedEvent`
        :param _ProjectMediaCastStatusChangedEvent: 点播转直播项目状态变更事件。仅当 EventType 为 Project.MediaCast.StatusChanged 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectMediaCastStatusChangedEvent: :class:`tencentcloud.cme.v20191029.models.ProjectMediaCastStatusChangedEvent`
        """
        self._EventType = None
        self._Operator = None
        self._StorageNewFileCreatedEvent = None
        self._ProjectStreamConnectStatusChangedEvent = None
        self._ProjectSwitcherStatusChangedEvent = None
        self._MaterialImportedEvent = None
        self._MaterialAddedEvent = None
        self._MaterialMovedEvent = None
        self._MaterialModifiedEvent = None
        self._MaterialDeletedEvent = None
        self._ClassCreatedEvent = None
        self._ClassMovedEvent = None
        self._ClassDeletedEvent = None
        self._VideoExportCompletedEvent = None
        self._ProjectMediaCastStatusChangedEvent = None

    @property
    def EventType(self):
        """事件类型，可取值有：
<li>Storage.NewFileCreated：新文件产生事件；</li>
<li>Project.StreamConnect.StatusChanged：云转推项目状态变更事件；</li>
<li>Project.Switcher.StatusChanged：导播台项目状态变更事件；</li>
<li>Material.Imported：媒体导入事件；</li>
<li>Material.Added：媒体添加事件；</li>
<li>Material.Moved：媒体移动事件；</li>
<li>Material.Modified：媒体变更事件；</li>
<li>Material.Deleted：媒体删除事件；</li>
<li>Class.Created：分类新增事件；</li>
<li>Class.Moved：分类移动事件；</li>
<li>Class.Deleted：分类删除事件；</li>
<li>Task.VideoExportCompleted：视频导出完成事件； </li>
<li>Project.MediaCast.StatusChanged：点播转直播项目状态变更事件。 </li>
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Operator(self):
        """操作者，表示触发事件的操作者。如果是 `cmeid_system` 表示平台管理员操作。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def StorageNewFileCreatedEvent(self):
        """新文件产生事件。仅当 EventType 为 Storage.NewFileCreated 时有效。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StorageNewFileCreatedEvent`
        """
        return self._StorageNewFileCreatedEvent

    @StorageNewFileCreatedEvent.setter
    def StorageNewFileCreatedEvent(self, StorageNewFileCreatedEvent):
        self._StorageNewFileCreatedEvent = StorageNewFileCreatedEvent

    @property
    def ProjectStreamConnectStatusChangedEvent(self):
        """云转推项目状态变更事件。仅当 EventType 为 Project.StreamConnect.StatusChanged 时有效。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ProjectStreamConnectStatusChangedEvent`
        """
        return self._ProjectStreamConnectStatusChangedEvent

    @ProjectStreamConnectStatusChangedEvent.setter
    def ProjectStreamConnectStatusChangedEvent(self, ProjectStreamConnectStatusChangedEvent):
        self._ProjectStreamConnectStatusChangedEvent = ProjectStreamConnectStatusChangedEvent

    @property
    def ProjectSwitcherStatusChangedEvent(self):
        """导播台项目状态变更事件。仅当 EventType 为 Project.Switcher.StatusChanged 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ProjectSwitcherStatusChangedEvent`
        """
        return self._ProjectSwitcherStatusChangedEvent

    @ProjectSwitcherStatusChangedEvent.setter
    def ProjectSwitcherStatusChangedEvent(self, ProjectSwitcherStatusChangedEvent):
        self._ProjectSwitcherStatusChangedEvent = ProjectSwitcherStatusChangedEvent

    @property
    def MaterialImportedEvent(self):
        """媒体导入事件。仅当 EventType 为 Material.Imported 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MaterialImportedEvent`
        """
        return self._MaterialImportedEvent

    @MaterialImportedEvent.setter
    def MaterialImportedEvent(self, MaterialImportedEvent):
        self._MaterialImportedEvent = MaterialImportedEvent

    @property
    def MaterialAddedEvent(self):
        """媒体添加事件。仅当 EventType 为 Material.Added 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MaterialAddedEvent`
        """
        return self._MaterialAddedEvent

    @MaterialAddedEvent.setter
    def MaterialAddedEvent(self, MaterialAddedEvent):
        self._MaterialAddedEvent = MaterialAddedEvent

    @property
    def MaterialMovedEvent(self):
        """媒体移动事件。仅当 EventType 为 Material.Moved 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MaterialMovedEvent`
        """
        return self._MaterialMovedEvent

    @MaterialMovedEvent.setter
    def MaterialMovedEvent(self, MaterialMovedEvent):
        self._MaterialMovedEvent = MaterialMovedEvent

    @property
    def MaterialModifiedEvent(self):
        """媒体更新事件。仅当 EventType 为 Material.Modified 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MaterialModifiedEvent`
        """
        return self._MaterialModifiedEvent

    @MaterialModifiedEvent.setter
    def MaterialModifiedEvent(self, MaterialModifiedEvent):
        self._MaterialModifiedEvent = MaterialModifiedEvent

    @property
    def MaterialDeletedEvent(self):
        """媒体删除事件。仅当 EventType 为 Material.Deleted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MaterialDeletedEvent`
        """
        return self._MaterialDeletedEvent

    @MaterialDeletedEvent.setter
    def MaterialDeletedEvent(self, MaterialDeletedEvent):
        self._MaterialDeletedEvent = MaterialDeletedEvent

    @property
    def ClassCreatedEvent(self):
        """分类创建事件。仅当 EventType 为 Class.Created 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ClassCreatedEvent`
        """
        return self._ClassCreatedEvent

    @ClassCreatedEvent.setter
    def ClassCreatedEvent(self, ClassCreatedEvent):
        self._ClassCreatedEvent = ClassCreatedEvent

    @property
    def ClassMovedEvent(self):
        """分类移动事件。仅当 EventType 为 Class.Moved 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ClassMovedEvent`
        """
        return self._ClassMovedEvent

    @ClassMovedEvent.setter
    def ClassMovedEvent(self, ClassMovedEvent):
        self._ClassMovedEvent = ClassMovedEvent

    @property
    def ClassDeletedEvent(self):
        """分类删除事件。仅当 EventType 为 Class.Deleted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ClassDeletedEvent`
        """
        return self._ClassDeletedEvent

    @ClassDeletedEvent.setter
    def ClassDeletedEvent(self, ClassDeletedEvent):
        self._ClassDeletedEvent = ClassDeletedEvent

    @property
    def VideoExportCompletedEvent(self):
        """视频导出完成事件。仅当 EventType 为 Task.VideoExportCompleted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoExportCompletedEvent`
        """
        return self._VideoExportCompletedEvent

    @VideoExportCompletedEvent.setter
    def VideoExportCompletedEvent(self, VideoExportCompletedEvent):
        self._VideoExportCompletedEvent = VideoExportCompletedEvent

    @property
    def ProjectMediaCastStatusChangedEvent(self):
        """点播转直播项目状态变更事件。仅当 EventType 为 Project.MediaCast.StatusChanged 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ProjectMediaCastStatusChangedEvent`
        """
        return self._ProjectMediaCastStatusChangedEvent

    @ProjectMediaCastStatusChangedEvent.setter
    def ProjectMediaCastStatusChangedEvent(self, ProjectMediaCastStatusChangedEvent):
        self._ProjectMediaCastStatusChangedEvent = ProjectMediaCastStatusChangedEvent


    def _deserialize(self, params):
        self._EventType = params.get("EventType")
        self._Operator = params.get("Operator")
        if params.get("StorageNewFileCreatedEvent") is not None:
            self._StorageNewFileCreatedEvent = StorageNewFileCreatedEvent()
            self._StorageNewFileCreatedEvent._deserialize(params.get("StorageNewFileCreatedEvent"))
        if params.get("ProjectStreamConnectStatusChangedEvent") is not None:
            self._ProjectStreamConnectStatusChangedEvent = ProjectStreamConnectStatusChangedEvent()
            self._ProjectStreamConnectStatusChangedEvent._deserialize(params.get("ProjectStreamConnectStatusChangedEvent"))
        if params.get("ProjectSwitcherStatusChangedEvent") is not None:
            self._ProjectSwitcherStatusChangedEvent = ProjectSwitcherStatusChangedEvent()
            self._ProjectSwitcherStatusChangedEvent._deserialize(params.get("ProjectSwitcherStatusChangedEvent"))
        if params.get("MaterialImportedEvent") is not None:
            self._MaterialImportedEvent = MaterialImportedEvent()
            self._MaterialImportedEvent._deserialize(params.get("MaterialImportedEvent"))
        if params.get("MaterialAddedEvent") is not None:
            self._MaterialAddedEvent = MaterialAddedEvent()
            self._MaterialAddedEvent._deserialize(params.get("MaterialAddedEvent"))
        if params.get("MaterialMovedEvent") is not None:
            self._MaterialMovedEvent = MaterialMovedEvent()
            self._MaterialMovedEvent._deserialize(params.get("MaterialMovedEvent"))
        if params.get("MaterialModifiedEvent") is not None:
            self._MaterialModifiedEvent = MaterialModifiedEvent()
            self._MaterialModifiedEvent._deserialize(params.get("MaterialModifiedEvent"))
        if params.get("MaterialDeletedEvent") is not None:
            self._MaterialDeletedEvent = MaterialDeletedEvent()
            self._MaterialDeletedEvent._deserialize(params.get("MaterialDeletedEvent"))
        if params.get("ClassCreatedEvent") is not None:
            self._ClassCreatedEvent = ClassCreatedEvent()
            self._ClassCreatedEvent._deserialize(params.get("ClassCreatedEvent"))
        if params.get("ClassMovedEvent") is not None:
            self._ClassMovedEvent = ClassMovedEvent()
            self._ClassMovedEvent._deserialize(params.get("ClassMovedEvent"))
        if params.get("ClassDeletedEvent") is not None:
            self._ClassDeletedEvent = ClassDeletedEvent()
            self._ClassDeletedEvent._deserialize(params.get("ClassDeletedEvent"))
        if params.get("VideoExportCompletedEvent") is not None:
            self._VideoExportCompletedEvent = VideoExportCompletedEvent()
            self._VideoExportCompletedEvent._deserialize(params.get("VideoExportCompletedEvent"))
        if params.get("ProjectMediaCastStatusChangedEvent") is not None:
            self._ProjectMediaCastStatusChangedEvent = ProjectMediaCastStatusChangedEvent()
            self._ProjectMediaCastStatusChangedEvent._deserialize(params.get("ProjectMediaCastStatusChangedEvent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVideoByEditorTrackDataRequest(AbstractModel):
    """ExportVideoByEditorTrackData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Definition: 导出视频预设配置 Id，推荐优先使用下面的默认预设配置 Id，有其他需求可通过接口定制预设配置。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :type Definition: int
        :param _ExportDestination: 导出目标，指定导出视频的目标媒资库，可取值有：
<li>CME：多媒体创建引擎，即导出到多媒体创作引擎媒资库，此导出目标在云点播媒资库依然可见；</li>
<li>VOD：云点播，即导出为云点播媒资库，此导出目标在多媒体创作引擎媒资库将不可见。</li>
        :type ExportDestination: str
        :param _TrackData: 轨道数据，用于描述待导出视频的内容。关于轨道数据的格式请查看 [视频合成协议](https://cloud.tencent.com/document/product/1156/51225)。文档中也描述了如何在页面上查看一个剪辑项目的轨道数据，该能力可以帮助开发者更方便地构造自己的轨道数据。
        :type TrackData: str
        :param _AspectRatio: 轨道数据对应的画布宽高比，配合预设配置中的视频短边尺寸，可决定导出画面的尺寸。例：
<li>如果 AspectRatio 取值 16:9，预设配置选为12（短边1080），则导出尺寸为 1920 * 1080；</li>
<li>如果 AspectRatio 取值 9:16，预设配置选为11（短边720），则导出尺寸为 720 *1280。</li>
        :type AspectRatio: str
        :param _CoverData: 视频封面图片文件（如 jpeg, png 等）进行 Base64 编码后的字符串，仅支持 gif、jpeg、png 三种图片格式，原图片文件不能超过2 M大 小。
        :type CoverData: str
        :param _CMEExportInfo: 导出的多媒体创作引擎媒体信息。当导出目标为 CME 时必填。
        :type CMEExportInfo: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        :param _VODExportInfo: 导出的云点播媒资信息。当导出目标为 VOD 时必填。
        :type VODExportInfo: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        :param _ExportExtensionArgs: 视频导出扩展参数。可以覆盖导出模板中的参数，灵活的指定导出规格及参数。
        :type ExportExtensionArgs: :class:`tencentcloud.cme.v20191029.models.VideoExportExtensionArgs`
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，无权限限制。如果指定操作者，轨道数据中使用的媒资该操作者需要拥有使用权限。
        :type Operator: str
        """
        self._Platform = None
        self._Definition = None
        self._ExportDestination = None
        self._TrackData = None
        self._AspectRatio = None
        self._CoverData = None
        self._CMEExportInfo = None
        self._VODExportInfo = None
        self._ExportExtensionArgs = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Definition(self):
        """导出视频预设配置 Id，推荐优先使用下面的默认预设配置 Id，有其他需求可通过接口定制预设配置。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :rtype: int
        """
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        self._Definition = Definition

    @property
    def ExportDestination(self):
        """导出目标，指定导出视频的目标媒资库，可取值有：
<li>CME：多媒体创建引擎，即导出到多媒体创作引擎媒资库，此导出目标在云点播媒资库依然可见；</li>
<li>VOD：云点播，即导出为云点播媒资库，此导出目标在多媒体创作引擎媒资库将不可见。</li>
        :rtype: str
        """
        return self._ExportDestination

    @ExportDestination.setter
    def ExportDestination(self, ExportDestination):
        self._ExportDestination = ExportDestination

    @property
    def TrackData(self):
        """轨道数据，用于描述待导出视频的内容。关于轨道数据的格式请查看 [视频合成协议](https://cloud.tencent.com/document/product/1156/51225)。文档中也描述了如何在页面上查看一个剪辑项目的轨道数据，该能力可以帮助开发者更方便地构造自己的轨道数据。
        :rtype: str
        """
        return self._TrackData

    @TrackData.setter
    def TrackData(self, TrackData):
        self._TrackData = TrackData

    @property
    def AspectRatio(self):
        """轨道数据对应的画布宽高比，配合预设配置中的视频短边尺寸，可决定导出画面的尺寸。例：
<li>如果 AspectRatio 取值 16:9，预设配置选为12（短边1080），则导出尺寸为 1920 * 1080；</li>
<li>如果 AspectRatio 取值 9:16，预设配置选为11（短边720），则导出尺寸为 720 *1280。</li>
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def CoverData(self):
        """视频封面图片文件（如 jpeg, png 等）进行 Base64 编码后的字符串，仅支持 gif、jpeg、png 三种图片格式，原图片文件不能超过2 M大 小。
        :rtype: str
        """
        return self._CoverData

    @CoverData.setter
    def CoverData(self, CoverData):
        self._CoverData = CoverData

    @property
    def CMEExportInfo(self):
        """导出的多媒体创作引擎媒体信息。当导出目标为 CME 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        """
        return self._CMEExportInfo

    @CMEExportInfo.setter
    def CMEExportInfo(self, CMEExportInfo):
        self._CMEExportInfo = CMEExportInfo

    @property
    def VODExportInfo(self):
        """导出的云点播媒资信息。当导出目标为 VOD 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        """
        return self._VODExportInfo

    @VODExportInfo.setter
    def VODExportInfo(self, VODExportInfo):
        self._VODExportInfo = VODExportInfo

    @property
    def ExportExtensionArgs(self):
        """视频导出扩展参数。可以覆盖导出模板中的参数，灵活的指定导出规格及参数。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoExportExtensionArgs`
        """
        return self._ExportExtensionArgs

    @ExportExtensionArgs.setter
    def ExportExtensionArgs(self, ExportExtensionArgs):
        self._ExportExtensionArgs = ExportExtensionArgs

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，无权限限制。如果指定操作者，轨道数据中使用的媒资该操作者需要拥有使用权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Definition = params.get("Definition")
        self._ExportDestination = params.get("ExportDestination")
        self._TrackData = params.get("TrackData")
        self._AspectRatio = params.get("AspectRatio")
        self._CoverData = params.get("CoverData")
        if params.get("CMEExportInfo") is not None:
            self._CMEExportInfo = CMEExportInfo()
            self._CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self._VODExportInfo = VODExportInfo()
            self._VODExportInfo._deserialize(params.get("VODExportInfo"))
        if params.get("ExportExtensionArgs") is not None:
            self._ExportExtensionArgs = VideoExportExtensionArgs()
            self._ExportExtensionArgs._deserialize(params.get("ExportExtensionArgs"))
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVideoByEditorTrackDataResponse(AbstractModel):
    """ExportVideoByEditorTrackData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 Id。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务 Id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ExportVideoByTemplateRequest(AbstractModel):
    """ExportVideoByTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _TemplateId: 视频编辑模板  Id。
        :type TemplateId: str
        :param _Definition: 导出视频预设配置 Id，推荐优先使用下面的默认预设配置 Id，有其他需求可通过接口定制预设配置。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :type Definition: int
        :param _ExportDestination: 导出目标，指定导出视频的目标媒资库，可取值有：
<li>CME：多媒体创作引擎，即导出为多媒体创作引擎媒资库，此导出目标在云点播媒资库依然可见；</li>
<li>VOD：云点播，即导出为云点播媒资库，此导出目标在多媒体创作引擎媒资库将不可见。</li>
        :type ExportDestination: str
        :param _SlotReplacements: 需要替换的素材信息。
        :type SlotReplacements: list of SlotReplacementInfo
        :param _CMEExportInfo: 导出的多媒体创作引擎媒资信息。当导出目标为 CME 时必填。
        :type CMEExportInfo: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        :param _VODExportInfo: 导出的云点播媒资信息。当导出目标为 VOD 时必填。
        :type VODExportInfo: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        :param _ExportExtensionArgs: 视频导出扩展参数。可以覆盖导出模板中的参数，灵活的指定导出规格及参数。
        :type ExportExtensionArgs: :class:`tencentcloud.cme.v20191029.models.VideoExportExtensionArgs`
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，无权限限制。如果指定操作者，则操作者需要有替换媒体及剪辑模板的权限。
        :type Operator: str
        """
        self._Platform = None
        self._TemplateId = None
        self._Definition = None
        self._ExportDestination = None
        self._SlotReplacements = None
        self._CMEExportInfo = None
        self._VODExportInfo = None
        self._ExportExtensionArgs = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TemplateId(self):
        """视频编辑模板  Id。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Definition(self):
        """导出视频预设配置 Id，推荐优先使用下面的默认预设配置 Id，有其他需求可通过接口定制预设配置。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :rtype: int
        """
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        self._Definition = Definition

    @property
    def ExportDestination(self):
        """导出目标，指定导出视频的目标媒资库，可取值有：
<li>CME：多媒体创作引擎，即导出为多媒体创作引擎媒资库，此导出目标在云点播媒资库依然可见；</li>
<li>VOD：云点播，即导出为云点播媒资库，此导出目标在多媒体创作引擎媒资库将不可见。</li>
        :rtype: str
        """
        return self._ExportDestination

    @ExportDestination.setter
    def ExportDestination(self, ExportDestination):
        self._ExportDestination = ExportDestination

    @property
    def SlotReplacements(self):
        """需要替换的素材信息。
        :rtype: list of SlotReplacementInfo
        """
        return self._SlotReplacements

    @SlotReplacements.setter
    def SlotReplacements(self, SlotReplacements):
        self._SlotReplacements = SlotReplacements

    @property
    def CMEExportInfo(self):
        """导出的多媒体创作引擎媒资信息。当导出目标为 CME 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        """
        return self._CMEExportInfo

    @CMEExportInfo.setter
    def CMEExportInfo(self, CMEExportInfo):
        self._CMEExportInfo = CMEExportInfo

    @property
    def VODExportInfo(self):
        """导出的云点播媒资信息。当导出目标为 VOD 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        """
        return self._VODExportInfo

    @VODExportInfo.setter
    def VODExportInfo(self, VODExportInfo):
        self._VODExportInfo = VODExportInfo

    @property
    def ExportExtensionArgs(self):
        """视频导出扩展参数。可以覆盖导出模板中的参数，灵活的指定导出规格及参数。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoExportExtensionArgs`
        """
        return self._ExportExtensionArgs

    @ExportExtensionArgs.setter
    def ExportExtensionArgs(self, ExportExtensionArgs):
        self._ExportExtensionArgs = ExportExtensionArgs

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，无权限限制。如果指定操作者，则操作者需要有替换媒体及剪辑模板的权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._TemplateId = params.get("TemplateId")
        self._Definition = params.get("Definition")
        self._ExportDestination = params.get("ExportDestination")
        if params.get("SlotReplacements") is not None:
            self._SlotReplacements = []
            for item in params.get("SlotReplacements"):
                obj = SlotReplacementInfo()
                obj._deserialize(item)
                self._SlotReplacements.append(obj)
        if params.get("CMEExportInfo") is not None:
            self._CMEExportInfo = CMEExportInfo()
            self._CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self._VODExportInfo = VODExportInfo()
            self._VODExportInfo._deserialize(params.get("VODExportInfo"))
        if params.get("ExportExtensionArgs") is not None:
            self._ExportExtensionArgs = VideoExportExtensionArgs()
            self._ExportExtensionArgs._deserialize(params.get("ExportExtensionArgs"))
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVideoByTemplateResponse(AbstractModel):
    """ExportVideoByTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 导出任务 Id。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """导出任务 Id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ExportVideoByVideoSegmentationDataRequest(AbstractModel):
    """ExportVideoByVideoSegmentationData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ProjectId: 视频拆条项目 Id 。
        :type ProjectId: str
        :param _SegmentGroupId: 指定需要导出的智能拆条片段的组 Id 。
        :type SegmentGroupId: str
        :param _SegmentIds: 指定需要导出的智能拆条片段 Id  集合。
        :type SegmentIds: list of str
        :param _Definition: 导出模板 Id，目前不支持自定义创建，只支持下面的预置模板 Id。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :type Definition: int
        :param _ExportDestination: 导出目标，指定导出视频的目标媒资库，可取值有：
<li>CME：多媒体创作引擎，即导出为多媒体创作引擎媒资库，此导出目标在云点播媒资库依然可见；</li>
<li>VOD：云点播，即导出为云点播媒资库，此导出目标在多媒体创作引擎媒资库将不可见。</li>
        :type ExportDestination: str
        :param _CMEExportInfo: 导出的多媒体创作引擎媒体信息。当导出目标为 CME 时必填。
        :type CMEExportInfo: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        :param _VODExportInfo: 导出的云点播媒资信息。当导出目标为 VOD 时必填。
        :type VODExportInfo: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以操作任意智能拆条项目。如果指定操作者，则操作者必须为项目所有。
        :type Operator: str
        """
        self._Platform = None
        self._ProjectId = None
        self._SegmentGroupId = None
        self._SegmentIds = None
        self._Definition = None
        self._ExportDestination = None
        self._CMEExportInfo = None
        self._VODExportInfo = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectId(self):
        """视频拆条项目 Id 。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SegmentGroupId(self):
        """指定需要导出的智能拆条片段的组 Id 。
        :rtype: str
        """
        return self._SegmentGroupId

    @SegmentGroupId.setter
    def SegmentGroupId(self, SegmentGroupId):
        self._SegmentGroupId = SegmentGroupId

    @property
    def SegmentIds(self):
        """指定需要导出的智能拆条片段 Id  集合。
        :rtype: list of str
        """
        return self._SegmentIds

    @SegmentIds.setter
    def SegmentIds(self, SegmentIds):
        self._SegmentIds = SegmentIds

    @property
    def Definition(self):
        """导出模板 Id，目前不支持自定义创建，只支持下面的预置模板 Id。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :rtype: int
        """
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        self._Definition = Definition

    @property
    def ExportDestination(self):
        """导出目标，指定导出视频的目标媒资库，可取值有：
<li>CME：多媒体创作引擎，即导出为多媒体创作引擎媒资库，此导出目标在云点播媒资库依然可见；</li>
<li>VOD：云点播，即导出为云点播媒资库，此导出目标在多媒体创作引擎媒资库将不可见。</li>
        :rtype: str
        """
        return self._ExportDestination

    @ExportDestination.setter
    def ExportDestination(self, ExportDestination):
        self._ExportDestination = ExportDestination

    @property
    def CMEExportInfo(self):
        """导出的多媒体创作引擎媒体信息。当导出目标为 CME 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        """
        return self._CMEExportInfo

    @CMEExportInfo.setter
    def CMEExportInfo(self, CMEExportInfo):
        self._CMEExportInfo = CMEExportInfo

    @property
    def VODExportInfo(self):
        """导出的云点播媒资信息。当导出目标为 VOD 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        """
        return self._VODExportInfo

    @VODExportInfo.setter
    def VODExportInfo(self, VODExportInfo):
        self._VODExportInfo = VODExportInfo

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以操作任意智能拆条项目。如果指定操作者，则操作者必须为项目所有。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectId = params.get("ProjectId")
        self._SegmentGroupId = params.get("SegmentGroupId")
        self._SegmentIds = params.get("SegmentIds")
        self._Definition = params.get("Definition")
        self._ExportDestination = params.get("ExportDestination")
        if params.get("CMEExportInfo") is not None:
            self._CMEExportInfo = CMEExportInfo()
            self._CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self._VODExportInfo = VODExportInfo()
            self._VODExportInfo._deserialize(params.get("VODExportInfo"))
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVideoByVideoSegmentationDataResponse(AbstractModel):
    """ExportVideoByVideoSegmentationData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 Id。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务 Id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ExportVideoEditProjectRequest(AbstractModel):
    """ExportVideoEditProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param _ProjectId: 项目 Id。
        :type ProjectId: str
        :param _Definition: 视频编码配置 ID，支持自定义创建，推荐优先使用系统预置的导出配置。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :type Definition: int
        :param _ExportDestination: 导出目标，指定导出视频的目标媒资库，可取值有：
<li>CME：多媒体创作引擎，即导出为多媒体创作引擎媒资库，此导出目标在云点播媒资库依然可见；</li>
<li>VOD：云点播，即导出为云点播媒资库，此导出目标在多媒体创作引擎媒资库将不可见。</li>
        :type ExportDestination: str
        :param _CoverData: 视频封面图片文件（如 jpeg, png 等）进行 Base64 编码后的字符串，仅支持 gif、jpeg、png 三种图片格式，原图片文件不能超过2 M大 小。
        :type CoverData: str
        :param _CMEExportInfo: 导出的多媒体创作引擎媒体信息。当导出目标为 CME 时必填。
        :type CMEExportInfo: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        :param _VODExportInfo: 导出的云点播媒资信息。当导出目标为 VOD 时必填。
        :type VODExportInfo: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        :param _ExportExtensionArgs: 视频导出扩展参数。可以覆盖导出模板中的参数，灵活的指定导出规格及参数。
        :type ExportExtensionArgs: :class:`tencentcloud.cme.v20191029.models.VideoExportExtensionArgs`
        :param _Operator: 操作者。填写用户的 Id，用于标识调用者及校验项目导出权限。
        :type Operator: str
        """
        self._Platform = None
        self._ProjectId = None
        self._Definition = None
        self._ExportDestination = None
        self._CoverData = None
        self._CMEExportInfo = None
        self._VODExportInfo = None
        self._ExportExtensionArgs = None
        self._Operator = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectId(self):
        """项目 Id。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Definition(self):
        """视频编码配置 ID，支持自定义创建，推荐优先使用系统预置的导出配置。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :rtype: int
        """
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        self._Definition = Definition

    @property
    def ExportDestination(self):
        """导出目标，指定导出视频的目标媒资库，可取值有：
<li>CME：多媒体创作引擎，即导出为多媒体创作引擎媒资库，此导出目标在云点播媒资库依然可见；</li>
<li>VOD：云点播，即导出为云点播媒资库，此导出目标在多媒体创作引擎媒资库将不可见。</li>
        :rtype: str
        """
        return self._ExportDestination

    @ExportDestination.setter
    def ExportDestination(self, ExportDestination):
        self._ExportDestination = ExportDestination

    @property
    def CoverData(self):
        """视频封面图片文件（如 jpeg, png 等）进行 Base64 编码后的字符串，仅支持 gif、jpeg、png 三种图片格式，原图片文件不能超过2 M大 小。
        :rtype: str
        """
        return self._CoverData

    @CoverData.setter
    def CoverData(self, CoverData):
        self._CoverData = CoverData

    @property
    def CMEExportInfo(self):
        """导出的多媒体创作引擎媒体信息。当导出目标为 CME 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        """
        return self._CMEExportInfo

    @CMEExportInfo.setter
    def CMEExportInfo(self, CMEExportInfo):
        self._CMEExportInfo = CMEExportInfo

    @property
    def VODExportInfo(self):
        """导出的云点播媒资信息。当导出目标为 VOD 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        """
        return self._VODExportInfo

    @VODExportInfo.setter
    def VODExportInfo(self, VODExportInfo):
        self._VODExportInfo = VODExportInfo

    @property
    def ExportExtensionArgs(self):
        """视频导出扩展参数。可以覆盖导出模板中的参数，灵活的指定导出规格及参数。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoExportExtensionArgs`
        """
        return self._ExportExtensionArgs

    @ExportExtensionArgs.setter
    def ExportExtensionArgs(self, ExportExtensionArgs):
        self._ExportExtensionArgs = ExportExtensionArgs

    @property
    def Operator(self):
        """操作者。填写用户的 Id，用于标识调用者及校验项目导出权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectId = params.get("ProjectId")
        self._Definition = params.get("Definition")
        self._ExportDestination = params.get("ExportDestination")
        self._CoverData = params.get("CoverData")
        if params.get("CMEExportInfo") is not None:
            self._CMEExportInfo = CMEExportInfo()
            self._CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self._VODExportInfo = VODExportInfo()
            self._VODExportInfo._deserialize(params.get("VODExportInfo"))
        if params.get("ExportExtensionArgs") is not None:
            self._ExportExtensionArgs = VideoExportExtensionArgs()
            self._ExportExtensionArgs._deserialize(params.get("ExportExtensionArgs"))
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVideoEditProjectResponse(AbstractModel):
    """ExportVideoEditProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 Id。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务 Id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ExternalMediaInfo(AbstractModel):
    """媒资绑定资源信息，包含媒资绑定模板 ID 和文件信息。

    """

    def __init__(self):
        r"""
        :param _MediaKey: 目前仅支持绑定 COS 桶的媒体，请填写存储对象 Key 值，例如：`example-folder/example.mp4`。
        :type MediaKey: str
        :param _Definition: 该字段废弃，请勿使用。
        :type Definition: int
        :param _StorageId: 媒资挂载的存储 Id。
        :type StorageId: str
        """
        self._MediaKey = None
        self._Definition = None
        self._StorageId = None

    @property
    def MediaKey(self):
        """目前仅支持绑定 COS 桶的媒体，请填写存储对象 Key 值，例如：`example-folder/example.mp4`。
        :rtype: str
        """
        return self._MediaKey

    @MediaKey.setter
    def MediaKey(self, MediaKey):
        self._MediaKey = MediaKey

    @property
    def Definition(self):
        warnings.warn("parameter `Definition` is deprecated", DeprecationWarning) 

        """该字段废弃，请勿使用。
        :rtype: int
        """
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        warnings.warn("parameter `Definition` is deprecated", DeprecationWarning) 

        self._Definition = Definition

    @property
    def StorageId(self):
        """媒资挂载的存储 Id。
        :rtype: str
        """
        return self._StorageId

    @StorageId.setter
    def StorageId(self, StorageId):
        self._StorageId = StorageId


    def _deserialize(self, params):
        self._MediaKey = params.get("MediaKey")
        self._Definition = params.get("Definition")
        self._StorageId = params.get("StorageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlattenListMediaRequest(AbstractModel):
    """FlattenListMedia请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ClassPath: 媒体分类路径，例如填写"/a/b"，则代表平铺该分类路径下及其子分类路径下的媒体信息。
        :type ClassPath: str
        :param _Owner: 媒体分类的归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 返回记录条数，默认值：10，最大值：50。
        :type Limit: int
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以平铺查询任意分类下的媒体信息。如果指定操作者，则操作者必须对当前分类有读权限。
        :type Operator: str
        """
        self._Platform = None
        self._ClassPath = None
        self._Owner = None
        self._Offset = None
        self._Limit = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ClassPath(self):
        """媒体分类路径，例如填写"/a/b"，则代表平铺该分类路径下及其子分类路径下的媒体信息。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath

    @property
    def Owner(self):
        """媒体分类的归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Offset(self):
        """分页偏移量，默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回记录条数，默认值：10，最大值：50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以平铺查询任意分类下的媒体信息。如果指定操作者，则操作者必须对当前分类有读权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ClassPath = params.get("ClassPath")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlattenListMediaResponse(AbstractModel):
    """FlattenListMedia返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param _MaterialInfoSet: 该分类路径下及其子分类下的所有媒体基础信息列表。
        :type MaterialInfoSet: list of MaterialInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MaterialInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的记录总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MaterialInfoSet(self):
        """该分类路径下及其子分类下的所有媒体基础信息列表。
        :rtype: list of MaterialInfo
        """
        return self._MaterialInfoSet

    @MaterialInfoSet.setter
    def MaterialInfoSet(self, MaterialInfoSet):
        self._MaterialInfoSet = MaterialInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("MaterialInfoSet") is not None:
            self._MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self._MaterialInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class GenerateVideoSegmentationSchemeByAiRequest(AbstractModel):
    """GenerateVideoSegmentationSchemeByAi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ProjectId: 视频拆条项目 Id 。
        :type ProjectId: str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以对任务视频拆条项目发起拆条任务。如果指定操作者，则操作者必须为项目所有者。
        :type Operator: str
        """
        self._Platform = None
        self._ProjectId = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectId(self):
        """视频拆条项目 Id 。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以对任务视频拆条项目发起拆条任务。如果指定操作者，则操作者必须为项目所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectId = params.get("ProjectId")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateVideoSegmentationSchemeByAiResponse(AbstractModel):
    """GenerateVideoSegmentationSchemeByAi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 视频智能拆条任务 Id 。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """视频智能拆条任务 Id 。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class GrantResourceAuthorizationRequest(AbstractModel):
    """GrantResourceAuthorization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Owner: 资源归属者，个人或者团队。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Resources: 被授权资源。
        :type Resources: list of Resource
        :param _Authorizees: 被授权目标，个人或者团队。
        :type Authorizees: list of Entity
        :param _Permissions: 详细授权值。 取值有：
<li>R：可读，可以浏览媒体，但不能使用该媒体文件（将其添加到 Project），或复制到自己的媒资库中</li>
<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>
<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>
<li>W：可修改、删除媒资。</li>
        :type Permissions: list of str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以授权任意归属者的资源。如果指定操作者，则操作者必须对资源拥有写权限。
        :type Operator: str
        """
        self._Platform = None
        self._Owner = None
        self._Resources = None
        self._Authorizees = None
        self._Permissions = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Owner(self):
        """资源归属者，个人或者团队。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Resources(self):
        """被授权资源。
        :rtype: list of Resource
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Authorizees(self):
        """被授权目标，个人或者团队。
        :rtype: list of Entity
        """
        return self._Authorizees

    @Authorizees.setter
    def Authorizees(self, Authorizees):
        self._Authorizees = Authorizees

    @property
    def Permissions(self):
        """详细授权值。 取值有：
<li>R：可读，可以浏览媒体，但不能使用该媒体文件（将其添加到 Project），或复制到自己的媒资库中</li>
<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>
<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>
<li>W：可修改、删除媒资。</li>
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以授权任意归属者的资源。如果指定操作者，则操作者必须对资源拥有写权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self._Resources.append(obj)
        if params.get("Authorizees") is not None:
            self._Authorizees = []
            for item in params.get("Authorizees"):
                obj = Entity()
                obj._deserialize(item)
                self._Authorizees.append(obj)
        self._Permissions = params.get("Permissions")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantResourceAuthorizationResponse(AbstractModel):
    """GrantResourceAuthorization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class HandleMediaCastProjectRequest(AbstractModel):
    """HandleMediaCastProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ProjectId: 媒体转推项目 Id 。
        :type ProjectId: str
        :param _Operation: 请参考 [操作类型](#Operation)。
        :type Operation: str
        :param _SourceInfos: 输入源信息。具体操作方式详见 [操作类型](#Operation) 及下文示例。
当 Operation 为 AddSource、DeleteSource、SwitchSource 时必填。
        :type SourceInfos: list of MediaCastSourceInfo
        :param _DestinationInfos: 输出源信息。具体操作方式详见 [操作类型](#Operation) 及下文示例。
当 Operation 为 AddDestination、DeleteDestination、EnableDestination、DisableDestination、ModifyDestination 时必填。
        :type DestinationInfos: list of MediaCastDestinationInfo
        :param _OutputMediaSetting: 输出媒体配置。具体操作方式详见 [操作类型](#Operation) 及下文示例。
当 Operation 为 ModifyOutputSetting 时必填。
        :type OutputMediaSetting: :class:`tencentcloud.cme.v20191029.models.MediaCastOutputMediaSetting`
        :param _PlaySetting: 播放控制参数。具体操作方式详见 [操作类型](#Operation) 及下文示例。
当 Operation 为 ModifyPlaySetting 时必填。
        :type PlaySetting: :class:`tencentcloud.cme.v20191029.models.MediaCastPlaySetting`
        :param _Position: 新添加的输入源位于输入源列表的位置，从0开始。默认加在输入源列表的后面。具体操作方式详见 [操作类型](#Operation) 及下文示例。
当 Operation 为 AddSource 时必填。
        :type Position: int
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以操作所有媒体转推项目。如果指定操作者，则操作者必须为项目所有者。
        :type Operator: str
        """
        self._Platform = None
        self._ProjectId = None
        self._Operation = None
        self._SourceInfos = None
        self._DestinationInfos = None
        self._OutputMediaSetting = None
        self._PlaySetting = None
        self._Position = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectId(self):
        """媒体转推项目 Id 。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Operation(self):
        """请参考 [操作类型](#Operation)。
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def SourceInfos(self):
        """输入源信息。具体操作方式详见 [操作类型](#Operation) 及下文示例。
当 Operation 为 AddSource、DeleteSource、SwitchSource 时必填。
        :rtype: list of MediaCastSourceInfo
        """
        return self._SourceInfos

    @SourceInfos.setter
    def SourceInfos(self, SourceInfos):
        self._SourceInfos = SourceInfos

    @property
    def DestinationInfos(self):
        """输出源信息。具体操作方式详见 [操作类型](#Operation) 及下文示例。
当 Operation 为 AddDestination、DeleteDestination、EnableDestination、DisableDestination、ModifyDestination 时必填。
        :rtype: list of MediaCastDestinationInfo
        """
        return self._DestinationInfos

    @DestinationInfos.setter
    def DestinationInfos(self, DestinationInfos):
        self._DestinationInfos = DestinationInfos

    @property
    def OutputMediaSetting(self):
        """输出媒体配置。具体操作方式详见 [操作类型](#Operation) 及下文示例。
当 Operation 为 ModifyOutputSetting 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastOutputMediaSetting`
        """
        return self._OutputMediaSetting

    @OutputMediaSetting.setter
    def OutputMediaSetting(self, OutputMediaSetting):
        self._OutputMediaSetting = OutputMediaSetting

    @property
    def PlaySetting(self):
        """播放控制参数。具体操作方式详见 [操作类型](#Operation) 及下文示例。
当 Operation 为 ModifyPlaySetting 时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastPlaySetting`
        """
        return self._PlaySetting

    @PlaySetting.setter
    def PlaySetting(self, PlaySetting):
        self._PlaySetting = PlaySetting

    @property
    def Position(self):
        """新添加的输入源位于输入源列表的位置，从0开始。默认加在输入源列表的后面。具体操作方式详见 [操作类型](#Operation) 及下文示例。
当 Operation 为 AddSource 时必填。
        :rtype: int
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以操作所有媒体转推项目。如果指定操作者，则操作者必须为项目所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectId = params.get("ProjectId")
        self._Operation = params.get("Operation")
        if params.get("SourceInfos") is not None:
            self._SourceInfos = []
            for item in params.get("SourceInfos"):
                obj = MediaCastSourceInfo()
                obj._deserialize(item)
                self._SourceInfos.append(obj)
        if params.get("DestinationInfos") is not None:
            self._DestinationInfos = []
            for item in params.get("DestinationInfos"):
                obj = MediaCastDestinationInfo()
                obj._deserialize(item)
                self._DestinationInfos.append(obj)
        if params.get("OutputMediaSetting") is not None:
            self._OutputMediaSetting = MediaCastOutputMediaSetting()
            self._OutputMediaSetting._deserialize(params.get("OutputMediaSetting"))
        if params.get("PlaySetting") is not None:
            self._PlaySetting = MediaCastPlaySetting()
            self._PlaySetting._deserialize(params.get("PlaySetting"))
        self._Position = params.get("Position")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HandleMediaCastProjectResponse(AbstractModel):
    """HandleMediaCastProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlayInfo: 播放信息，Operation 为 DescribePlayInfo 时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayInfo: :class:`tencentcloud.cme.v20191029.models.MediaCastPlayInfo`
        :param _SourceInfoSet: 输入源信息， Operation 为 AddSource 时返回添加成功的输入源信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceInfoSet: list of MediaCastSourceInfo
        :param _DestinationInfoSet: 输出源信息， Operation 为 AddDestination 时返回添加成功的输出源信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DestinationInfoSet: list of MediaCastDestinationInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlayInfo = None
        self._SourceInfoSet = None
        self._DestinationInfoSet = None
        self._RequestId = None

    @property
    def PlayInfo(self):
        """播放信息，Operation 为 DescribePlayInfo 时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastPlayInfo`
        """
        return self._PlayInfo

    @PlayInfo.setter
    def PlayInfo(self, PlayInfo):
        self._PlayInfo = PlayInfo

    @property
    def SourceInfoSet(self):
        """输入源信息， Operation 为 AddSource 时返回添加成功的输入源信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MediaCastSourceInfo
        """
        return self._SourceInfoSet

    @SourceInfoSet.setter
    def SourceInfoSet(self, SourceInfoSet):
        self._SourceInfoSet = SourceInfoSet

    @property
    def DestinationInfoSet(self):
        """输出源信息， Operation 为 AddDestination 时返回添加成功的输出源信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MediaCastDestinationInfo
        """
        return self._DestinationInfoSet

    @DestinationInfoSet.setter
    def DestinationInfoSet(self, DestinationInfoSet):
        self._DestinationInfoSet = DestinationInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlayInfo") is not None:
            self._PlayInfo = MediaCastPlayInfo()
            self._PlayInfo._deserialize(params.get("PlayInfo"))
        if params.get("SourceInfoSet") is not None:
            self._SourceInfoSet = []
            for item in params.get("SourceInfoSet"):
                obj = MediaCastSourceInfo()
                obj._deserialize(item)
                self._SourceInfoSet.append(obj)
        if params.get("DestinationInfoSet") is not None:
            self._DestinationInfoSet = []
            for item in params.get("DestinationInfoSet"):
                obj = MediaCastDestinationInfo()
                obj._deserialize(item)
                self._DestinationInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class HandleStreamConnectProjectRequest(AbstractModel):
    """HandleStreamConnectProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ProjectId: 云转推项目 Id 。
        :type ProjectId: str
        :param _Operation: 请参考 [操作类型](#Operation)
        :type Operation: str
        :param _InputInfo: 转推输入源操作参数。具体操作方式详见 [操作类型](#Operation) 及下文示例。
        :type InputInfo: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        :param _InputEndpoint: 主备输入源标识，取值有：
<li> Main ：主源；</li>
<li> Backup ：备源。</li>
        :type InputEndpoint: str
        :param _OutputInfo: 转推输出源操作参数。具体操作方式详见 [操作类型](#Operation) 及下文示例。
        :type OutputInfo: :class:`tencentcloud.cme.v20191029.models.StreamConnectOutput`
        :param _CurrentStopTime: 云转推当前预计结束时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。具体操作方式详见 [操作类型](#Operation) 及下文示例。
        :type CurrentStopTime: str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以操作所有云转推项目。如果指定操作者，则操作者必须为项目所有者。
        :type Operator: str
        """
        self._Platform = None
        self._ProjectId = None
        self._Operation = None
        self._InputInfo = None
        self._InputEndpoint = None
        self._OutputInfo = None
        self._CurrentStopTime = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectId(self):
        """云转推项目 Id 。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Operation(self):
        """请参考 [操作类型](#Operation)
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def InputInfo(self):
        """转推输入源操作参数。具体操作方式详见 [操作类型](#Operation) 及下文示例。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        """
        return self._InputInfo

    @InputInfo.setter
    def InputInfo(self, InputInfo):
        self._InputInfo = InputInfo

    @property
    def InputEndpoint(self):
        """主备输入源标识，取值有：
<li> Main ：主源；</li>
<li> Backup ：备源。</li>
        :rtype: str
        """
        return self._InputEndpoint

    @InputEndpoint.setter
    def InputEndpoint(self, InputEndpoint):
        self._InputEndpoint = InputEndpoint

    @property
    def OutputInfo(self):
        """转推输出源操作参数。具体操作方式详见 [操作类型](#Operation) 及下文示例。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamConnectOutput`
        """
        return self._OutputInfo

    @OutputInfo.setter
    def OutputInfo(self, OutputInfo):
        self._OutputInfo = OutputInfo

    @property
    def CurrentStopTime(self):
        """云转推当前预计结束时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。具体操作方式详见 [操作类型](#Operation) 及下文示例。
        :rtype: str
        """
        return self._CurrentStopTime

    @CurrentStopTime.setter
    def CurrentStopTime(self, CurrentStopTime):
        self._CurrentStopTime = CurrentStopTime

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以操作所有云转推项目。如果指定操作者，则操作者必须为项目所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectId = params.get("ProjectId")
        self._Operation = params.get("Operation")
        if params.get("InputInfo") is not None:
            self._InputInfo = StreamInputInfo()
            self._InputInfo._deserialize(params.get("InputInfo"))
        self._InputEndpoint = params.get("InputEndpoint")
        if params.get("OutputInfo") is not None:
            self._OutputInfo = StreamConnectOutput()
            self._OutputInfo._deserialize(params.get("OutputInfo"))
        self._CurrentStopTime = params.get("CurrentStopTime")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HandleStreamConnectProjectResponse(AbstractModel):
    """HandleStreamConnectProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StreamInputRtmpPushUrl: 输入源推流地址，当 Operation 取值 AddInput 且 InputType 为 RtmpPush 类型时有效。
        :type StreamInputRtmpPushUrl: str
        :param _VodPullInputPlayInfo: 点播输入源播放进度信息，当 Operation 取值 DescribeInputPlayInfo 且 InputType 为 VodPull 类型时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type VodPullInputPlayInfo: :class:`tencentcloud.cme.v20191029.models.VodPullInputPlayInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StreamInputRtmpPushUrl = None
        self._VodPullInputPlayInfo = None
        self._RequestId = None

    @property
    def StreamInputRtmpPushUrl(self):
        """输入源推流地址，当 Operation 取值 AddInput 且 InputType 为 RtmpPush 类型时有效。
        :rtype: str
        """
        return self._StreamInputRtmpPushUrl

    @StreamInputRtmpPushUrl.setter
    def StreamInputRtmpPushUrl(self, StreamInputRtmpPushUrl):
        self._StreamInputRtmpPushUrl = StreamInputRtmpPushUrl

    @property
    def VodPullInputPlayInfo(self):
        """点播输入源播放进度信息，当 Operation 取值 DescribeInputPlayInfo 且 InputType 为 VodPull 类型时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VodPullInputPlayInfo`
        """
        return self._VodPullInputPlayInfo

    @VodPullInputPlayInfo.setter
    def VodPullInputPlayInfo(self, VodPullInputPlayInfo):
        self._VodPullInputPlayInfo = VodPullInputPlayInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StreamInputRtmpPushUrl = params.get("StreamInputRtmpPushUrl")
        if params.get("VodPullInputPlayInfo") is not None:
            self._VodPullInputPlayInfo = VodPullInputPlayInfo()
            self._VodPullInputPlayInfo._deserialize(params.get("VodPullInputPlayInfo"))
        self._RequestId = params.get("RequestId")


class ImageMaterial(AbstractModel):
    """图片素材信息

    """

    def __init__(self):
        r"""
        :param _Height: 图片高度，单位：px。
        :type Height: int
        :param _Width: 图片宽度，单位：px。
        :type Width: int
        :param _MaterialUrl: 素材媒体文件的展示 URL 地址。
        :type MaterialUrl: str
        :param _Size: 图片大小，单位：字节。
        :type Size: int
        :param _OriginalUrl: 素材媒体文件的原始 URL 地址。
        :type OriginalUrl: str
        :param _VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        """
        self._Height = None
        self._Width = None
        self._MaterialUrl = None
        self._Size = None
        self._OriginalUrl = None
        self._VodFileId = None

    @property
    def Height(self):
        """图片高度，单位：px。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        """图片宽度，单位：px。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def MaterialUrl(self):
        """素材媒体文件的展示 URL 地址。
        :rtype: str
        """
        return self._MaterialUrl

    @MaterialUrl.setter
    def MaterialUrl(self, MaterialUrl):
        self._MaterialUrl = MaterialUrl

    @property
    def Size(self):
        """图片大小，单位：字节。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def OriginalUrl(self):
        """素材媒体文件的原始 URL 地址。
        :rtype: str
        """
        return self._OriginalUrl

    @OriginalUrl.setter
    def OriginalUrl(self, OriginalUrl):
        self._OriginalUrl = OriginalUrl

    @property
    def VodFileId(self):
        """云点播媒资 FileId。
        :rtype: str
        """
        return self._VodFileId

    @VodFileId.setter
    def VodFileId(self, VodFileId):
        self._VodFileId = VodFileId


    def _deserialize(self, params):
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._MaterialUrl = params.get("MaterialUrl")
        self._Size = params.get("Size")
        self._OriginalUrl = params.get("OriginalUrl")
        self._VodFileId = params.get("VodFileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportMaterialRequest(AbstractModel):
    """ImportMaterial请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Owner: 媒体归属者，可支持归属团队或个人。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Name: 媒体名称，不能超过30个字符。
        :type Name: str
        :param _SourceType: 导入媒资类型，取值：
<li>VOD：云点播文件；</li>
<li>EXTERNAL：媒资绑定。</li>

注意：如果不填默认为云点播文件，如果媒体存储在非腾讯云点播中，都需要使用媒资绑定。另外，导入云点播的文件，使用云点播的子应用 Id 必须与创建多媒体创作引擎平台时使用的云点播子应用一致。
        :type SourceType: str
        :param _VodFileId: 云点播媒资 FileId，仅当 SourceType 为 VOD 时有效。
        :type VodFileId: str
        :param _ExternalMediaInfo: 原始媒资文件信息，当 SourceType 取值 EXTERNAL 的时候必填。
        :type ExternalMediaInfo: :class:`tencentcloud.cme.v20191029.models.ExternalMediaInfo`
        :param _ClassPath: 媒体分类路径，形如："/a/b"，层级数不能超过10，每个层级长度不能超过15字符。若不填则默认为根路径。
        :type ClassPath: str
        :param _PreProcessDefinition: 媒体预处理任务参数 ID。可取值有：
<li>10：进行编辑预处理。</li>
        :type PreProcessDefinition: int
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以向任意团队或者个人导入媒体。如果指定操作者，如果媒体归属为个人，则操作者必须与归属者一致；如果媒体归属为团队，则必须为团队可导入媒体的团队成员(如果没有特殊设置，所有团队成员可导入媒体)。
        :type Operator: str
        """
        self._Platform = None
        self._Owner = None
        self._Name = None
        self._SourceType = None
        self._VodFileId = None
        self._ExternalMediaInfo = None
        self._ClassPath = None
        self._PreProcessDefinition = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Owner(self):
        """媒体归属者，可支持归属团队或个人。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Name(self):
        """媒体名称，不能超过30个字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceType(self):
        """导入媒资类型，取值：
<li>VOD：云点播文件；</li>
<li>EXTERNAL：媒资绑定。</li>

注意：如果不填默认为云点播文件，如果媒体存储在非腾讯云点播中，都需要使用媒资绑定。另外，导入云点播的文件，使用云点播的子应用 Id 必须与创建多媒体创作引擎平台时使用的云点播子应用一致。
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def VodFileId(self):
        """云点播媒资 FileId，仅当 SourceType 为 VOD 时有效。
        :rtype: str
        """
        return self._VodFileId

    @VodFileId.setter
    def VodFileId(self, VodFileId):
        self._VodFileId = VodFileId

    @property
    def ExternalMediaInfo(self):
        """原始媒资文件信息，当 SourceType 取值 EXTERNAL 的时候必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExternalMediaInfo`
        """
        return self._ExternalMediaInfo

    @ExternalMediaInfo.setter
    def ExternalMediaInfo(self, ExternalMediaInfo):
        self._ExternalMediaInfo = ExternalMediaInfo

    @property
    def ClassPath(self):
        """媒体分类路径，形如："/a/b"，层级数不能超过10，每个层级长度不能超过15字符。若不填则默认为根路径。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath

    @property
    def PreProcessDefinition(self):
        """媒体预处理任务参数 ID。可取值有：
<li>10：进行编辑预处理。</li>
        :rtype: int
        """
        return self._PreProcessDefinition

    @PreProcessDefinition.setter
    def PreProcessDefinition(self, PreProcessDefinition):
        self._PreProcessDefinition = PreProcessDefinition

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以向任意团队或者个人导入媒体。如果指定操作者，如果媒体归属为个人，则操作者必须与归属者一致；如果媒体归属为团队，则必须为团队可导入媒体的团队成员(如果没有特殊设置，所有团队成员可导入媒体)。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Name = params.get("Name")
        self._SourceType = params.get("SourceType")
        self._VodFileId = params.get("VodFileId")
        if params.get("ExternalMediaInfo") is not None:
            self._ExternalMediaInfo = ExternalMediaInfo()
            self._ExternalMediaInfo._deserialize(params.get("ExternalMediaInfo"))
        self._ClassPath = params.get("ClassPath")
        self._PreProcessDefinition = params.get("PreProcessDefinition")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportMaterialResponse(AbstractModel):
    """ImportMaterial返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MaterialId: 媒体 Id。
        :type MaterialId: str
        :param _PreProcessTaskId: 媒体文件预处理任务 ID，如果未指定发起预处理任务则为空。
        :type PreProcessTaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MaterialId = None
        self._PreProcessTaskId = None
        self._RequestId = None

    @property
    def MaterialId(self):
        """媒体 Id。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def PreProcessTaskId(self):
        """媒体文件预处理任务 ID，如果未指定发起预处理任务则为空。
        :rtype: str
        """
        return self._PreProcessTaskId

    @PreProcessTaskId.setter
    def PreProcessTaskId(self, PreProcessTaskId):
        self._PreProcessTaskId = PreProcessTaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MaterialId = params.get("MaterialId")
        self._PreProcessTaskId = params.get("PreProcessTaskId")
        self._RequestId = params.get("RequestId")


class ImportMediaInfo(AbstractModel):
    """导入媒资信息

    """

    def __init__(self):
        r"""
        :param _FileId: 云点播文件 FileId。
        :type FileId: str
        :param _MaterialId: 媒体 Id。
        :type MaterialId: str
        """
        self._FileId = None
        self._MaterialId = None

    @property
    def FileId(self):
        """云点播文件 FileId。
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def MaterialId(self):
        """媒体 Id。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._MaterialId = params.get("MaterialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportMediaToProjectRequest(AbstractModel):
    """ImportMediaToProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ProjectId: 项目 Id。
        :type ProjectId: str
        :param _SourceType: 导入媒资类型，取值：
<li>VOD：云点播文件；</li>
<li>EXTERNAL：媒资绑定。</li>

注意：如果不填默认为云点播文件，如果媒体存储在非腾讯云点播中，都需要使用媒资绑定。
        :type SourceType: str
        :param _VodFileId: 云点播媒资文件 Id，当 SourceType 取值 VOD 或者缺省的时候必填。
        :type VodFileId: str
        :param _ExternalMediaInfo: 原始媒资文件信息，当 SourceType 取值 EXTERNAL 的时候必填。
        :type ExternalMediaInfo: :class:`tencentcloud.cme.v20191029.models.ExternalMediaInfo`
        :param _Name: 媒体名称，不能超过30个字符。如果不填，则媒体名称为点播媒资文件名称。
        :type Name: str
        :param _PreProcessDefinition: 媒体预处理配置 ID，取值：
<li>10：进行视频编辑预处理。</li>

注意：如果填0或者不填则不进行处理，如果原始视频不可在浏览器直接播放将无法在编辑页面编辑。
        :type PreProcessDefinition: int
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以向所有视频编辑项目导入媒体；如果指定操作者，则操作者必须为项目所有者。
        :type Operator: str
        """
        self._Platform = None
        self._ProjectId = None
        self._SourceType = None
        self._VodFileId = None
        self._ExternalMediaInfo = None
        self._Name = None
        self._PreProcessDefinition = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectId(self):
        """项目 Id。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SourceType(self):
        """导入媒资类型，取值：
<li>VOD：云点播文件；</li>
<li>EXTERNAL：媒资绑定。</li>

注意：如果不填默认为云点播文件，如果媒体存储在非腾讯云点播中，都需要使用媒资绑定。
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def VodFileId(self):
        """云点播媒资文件 Id，当 SourceType 取值 VOD 或者缺省的时候必填。
        :rtype: str
        """
        return self._VodFileId

    @VodFileId.setter
    def VodFileId(self, VodFileId):
        self._VodFileId = VodFileId

    @property
    def ExternalMediaInfo(self):
        """原始媒资文件信息，当 SourceType 取值 EXTERNAL 的时候必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExternalMediaInfo`
        """
        return self._ExternalMediaInfo

    @ExternalMediaInfo.setter
    def ExternalMediaInfo(self, ExternalMediaInfo):
        self._ExternalMediaInfo = ExternalMediaInfo

    @property
    def Name(self):
        """媒体名称，不能超过30个字符。如果不填，则媒体名称为点播媒资文件名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PreProcessDefinition(self):
        """媒体预处理配置 ID，取值：
<li>10：进行视频编辑预处理。</li>

注意：如果填0或者不填则不进行处理，如果原始视频不可在浏览器直接播放将无法在编辑页面编辑。
        :rtype: int
        """
        return self._PreProcessDefinition

    @PreProcessDefinition.setter
    def PreProcessDefinition(self, PreProcessDefinition):
        self._PreProcessDefinition = PreProcessDefinition

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以向所有视频编辑项目导入媒体；如果指定操作者，则操作者必须为项目所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectId = params.get("ProjectId")
        self._SourceType = params.get("SourceType")
        self._VodFileId = params.get("VodFileId")
        if params.get("ExternalMediaInfo") is not None:
            self._ExternalMediaInfo = ExternalMediaInfo()
            self._ExternalMediaInfo._deserialize(params.get("ExternalMediaInfo"))
        self._Name = params.get("Name")
        self._PreProcessDefinition = params.get("PreProcessDefinition")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportMediaToProjectResponse(AbstractModel):
    """ImportMediaToProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MaterialId: 媒体 Id。
        :type MaterialId: str
        :param _TaskId: 媒体预处理任务 ID，如果未指定发起预处理任务则为空。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MaterialId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def MaterialId(self):
        """媒体 Id。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def TaskId(self):
        """媒体预处理任务 ID，如果未指定发起预处理任务则为空。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MaterialId = params.get("MaterialId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class IntegerRange(AbstractModel):
    """整型范围

    """

    def __init__(self):
        r"""
        :param _LowerBound: 按整形代表值的下限检索。
        :type LowerBound: int
        :param _UpperBound: 按整形代表值的上限检索。
        :type UpperBound: int
        """
        self._LowerBound = None
        self._UpperBound = None

    @property
    def LowerBound(self):
        """按整形代表值的下限检索。
        :rtype: int
        """
        return self._LowerBound

    @LowerBound.setter
    def LowerBound(self, LowerBound):
        self._LowerBound = LowerBound

    @property
    def UpperBound(self):
        """按整形代表值的上限检索。
        :rtype: int
        """
        return self._UpperBound

    @UpperBound.setter
    def UpperBound(self, UpperBound):
        self._UpperBound = UpperBound


    def _deserialize(self, params):
        self._LowerBound = params.get("LowerBound")
        self._UpperBound = params.get("UpperBound")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinTeamInfo(AbstractModel):
    """加入的团队信息

    """

    def __init__(self):
        r"""
        :param _TeamId: 团队 ID。
        :type TeamId: str
        :param _Name: 团队名称。
        :type Name: str
        :param _MemberCount: 团队成员个数。
        :type MemberCount: int
        :param _Role: 成员在团队中的角色，取值有：
<li>Owner：团队所有者，添加团队成员及修改团队成员解决时不能填此角色；</li>
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :type Role: str
        """
        self._TeamId = None
        self._Name = None
        self._MemberCount = None
        self._Role = None

    @property
    def TeamId(self):
        """团队 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Name(self):
        """团队名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MemberCount(self):
        """团队成员个数。
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount

    @property
    def Role(self):
        """成员在团队中的角色，取值有：
<li>Owner：团队所有者，添加团队成员及修改团队成员解决时不能填此角色；</li>
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._Name = params.get("Name")
        self._MemberCount = params.get("MemberCount")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KuaishouPublishInfo(AbstractModel):
    """快手视频发布信息。

    """

    def __init__(self):
        r"""
        :param _Title: 视频发布标题，限30个字符。
        :type Title: str
        """
        self._Title = None

    @property
    def Title(self):
        """视频发布标题，限30个字符。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkMaterial(AbstractModel):
    """链接类型的素材信息

    """

    def __init__(self):
        r"""
        :param _LinkType: 链接类型取值:
<li>CLASS: 分类链接;</li>
<li> MATERIAL：素材链接。</li>
        :type LinkType: str
        :param _LinkStatus: 链接状态取值：
<li> Normal：正常 ；</li>
<li>NotFound：链接目标不存在；</li> <li>Forbidden：无权限。</li>
        :type LinkStatus: str
        :param _LinkMaterialInfo: 素材链接详细信息，当LinkType="MATERIAL"时有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkMaterialInfo: :class:`tencentcloud.cme.v20191029.models.LinkMaterialInfo`
        :param _LinkClassInfo: 分类链接目标信息，当LinkType=“CLASS”时有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkClassInfo: :class:`tencentcloud.cme.v20191029.models.ClassInfo`
        """
        self._LinkType = None
        self._LinkStatus = None
        self._LinkMaterialInfo = None
        self._LinkClassInfo = None

    @property
    def LinkType(self):
        """链接类型取值:
<li>CLASS: 分类链接;</li>
<li> MATERIAL：素材链接。</li>
        :rtype: str
        """
        return self._LinkType

    @LinkType.setter
    def LinkType(self, LinkType):
        self._LinkType = LinkType

    @property
    def LinkStatus(self):
        """链接状态取值：
<li> Normal：正常 ；</li>
<li>NotFound：链接目标不存在；</li> <li>Forbidden：无权限。</li>
        :rtype: str
        """
        return self._LinkStatus

    @LinkStatus.setter
    def LinkStatus(self, LinkStatus):
        self._LinkStatus = LinkStatus

    @property
    def LinkMaterialInfo(self):
        """素材链接详细信息，当LinkType="MATERIAL"时有值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.LinkMaterialInfo`
        """
        return self._LinkMaterialInfo

    @LinkMaterialInfo.setter
    def LinkMaterialInfo(self, LinkMaterialInfo):
        self._LinkMaterialInfo = LinkMaterialInfo

    @property
    def LinkClassInfo(self):
        """分类链接目标信息，当LinkType=“CLASS”时有值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ClassInfo`
        """
        return self._LinkClassInfo

    @LinkClassInfo.setter
    def LinkClassInfo(self, LinkClassInfo):
        self._LinkClassInfo = LinkClassInfo


    def _deserialize(self, params):
        self._LinkType = params.get("LinkType")
        self._LinkStatus = params.get("LinkStatus")
        if params.get("LinkMaterialInfo") is not None:
            self._LinkMaterialInfo = LinkMaterialInfo()
            self._LinkMaterialInfo._deserialize(params.get("LinkMaterialInfo"))
        if params.get("LinkClassInfo") is not None:
            self._LinkClassInfo = ClassInfo()
            self._LinkClassInfo._deserialize(params.get("LinkClassInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkMaterialInfo(AbstractModel):
    """链接素材信息

    """

    def __init__(self):
        r"""
        :param _BasicInfo: 素材基本信息。
        :type BasicInfo: :class:`tencentcloud.cme.v20191029.models.MaterialBasicInfo`
        :param _VideoMaterial: 视频素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoMaterial: :class:`tencentcloud.cme.v20191029.models.VideoMaterial`
        :param _AudioMaterial: 音频素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioMaterial: :class:`tencentcloud.cme.v20191029.models.AudioMaterial`
        :param _ImageMaterial: 图片素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageMaterial: :class:`tencentcloud.cme.v20191029.models.ImageMaterial`
        """
        self._BasicInfo = None
        self._VideoMaterial = None
        self._AudioMaterial = None
        self._ImageMaterial = None

    @property
    def BasicInfo(self):
        """素材基本信息。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MaterialBasicInfo`
        """
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def VideoMaterial(self):
        """视频素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoMaterial`
        """
        return self._VideoMaterial

    @VideoMaterial.setter
    def VideoMaterial(self, VideoMaterial):
        self._VideoMaterial = VideoMaterial

    @property
    def AudioMaterial(self):
        """音频素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.AudioMaterial`
        """
        return self._AudioMaterial

    @AudioMaterial.setter
    def AudioMaterial(self, AudioMaterial):
        self._AudioMaterial = AudioMaterial

    @property
    def ImageMaterial(self):
        """图片素材信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ImageMaterial`
        """
        return self._ImageMaterial

    @ImageMaterial.setter
    def ImageMaterial(self, ImageMaterial):
        self._ImageMaterial = ImageMaterial


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self._BasicInfo = MaterialBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("VideoMaterial") is not None:
            self._VideoMaterial = VideoMaterial()
            self._VideoMaterial._deserialize(params.get("VideoMaterial"))
        if params.get("AudioMaterial") is not None:
            self._AudioMaterial = AudioMaterial()
            self._AudioMaterial._deserialize(params.get("AudioMaterial"))
        if params.get("ImageMaterial") is not None:
            self._ImageMaterial = ImageMaterial()
            self._ImageMaterial._deserialize(params.get("ImageMaterial"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMediaRequest(AbstractModel):
    """ListMedia请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ClassPath: 媒体分类路径，例如填写"/a/b"，则代表浏览该分类路径下的媒体和子分类信息。
        :type ClassPath: str
        :param _Owner: 媒体和分类的归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 返回记录条数，默认值：10，最大值：50。
        :type Limit: int
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以浏览任意分类的信息。如果指定操作者，则操作者必须对分类有读权限。
        :type Operator: str
        """
        self._Platform = None
        self._ClassPath = None
        self._Owner = None
        self._Offset = None
        self._Limit = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ClassPath(self):
        """媒体分类路径，例如填写"/a/b"，则代表浏览该分类路径下的媒体和子分类信息。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath

    @property
    def Owner(self):
        """媒体和分类的归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Offset(self):
        """分页偏移量，默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回记录条数，默认值：10，最大值：50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以浏览任意分类的信息。如果指定操作者，则操作者必须对分类有读权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ClassPath = params.get("ClassPath")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMediaResponse(AbstractModel):
    """ListMedia返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MaterialTotalCount: 符合条件的媒体记录总数。
        :type MaterialTotalCount: int
        :param _MaterialInfoSet: 浏览分类路径下的媒体列表信息。
        :type MaterialInfoSet: list of MaterialInfo
        :param _ClassInfoSet: 浏览分类路径下的一级子类。
        :type ClassInfoSet: list of ClassInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MaterialTotalCount = None
        self._MaterialInfoSet = None
        self._ClassInfoSet = None
        self._RequestId = None

    @property
    def MaterialTotalCount(self):
        """符合条件的媒体记录总数。
        :rtype: int
        """
        return self._MaterialTotalCount

    @MaterialTotalCount.setter
    def MaterialTotalCount(self, MaterialTotalCount):
        self._MaterialTotalCount = MaterialTotalCount

    @property
    def MaterialInfoSet(self):
        """浏览分类路径下的媒体列表信息。
        :rtype: list of MaterialInfo
        """
        return self._MaterialInfoSet

    @MaterialInfoSet.setter
    def MaterialInfoSet(self, MaterialInfoSet):
        self._MaterialInfoSet = MaterialInfoSet

    @property
    def ClassInfoSet(self):
        """浏览分类路径下的一级子类。
        :rtype: list of ClassInfo
        """
        return self._ClassInfoSet

    @ClassInfoSet.setter
    def ClassInfoSet(self, ClassInfoSet):
        self._ClassInfoSet = ClassInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MaterialTotalCount = params.get("MaterialTotalCount")
        if params.get("MaterialInfoSet") is not None:
            self._MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self._MaterialInfoSet.append(obj)
        if params.get("ClassInfoSet") is not None:
            self._ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = ClassInfo()
                obj._deserialize(item)
                self._ClassInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class LivePullInputInfo(AbstractModel):
    """直播拉流信息

    """

    def __init__(self):
        r"""
        :param _InputUrl: 直播拉流地址。
        :type InputUrl: str
        """
        self._InputUrl = None

    @property
    def InputUrl(self):
        """直播拉流地址。
        :rtype: str
        """
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl


    def _deserialize(self, params):
        self._InputUrl = params.get("InputUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamClipProjectInput(AbstractModel):
    """直播剪辑项目输入参数。

    """

    def __init__(self):
        r"""
        :param _Url: 直播流播放地址，目前仅支持 HLS 和 FLV 格式。
        :type Url: str
        :param _StreamRecordDuration: 直播流录制时长，单位为秒，最大值为 7200。
        :type StreamRecordDuration: int
        """
        self._Url = None
        self._StreamRecordDuration = None

    @property
    def Url(self):
        """直播流播放地址，目前仅支持 HLS 和 FLV 格式。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def StreamRecordDuration(self):
        """直播流录制时长，单位为秒，最大值为 7200。
        :rtype: int
        """
        return self._StreamRecordDuration

    @StreamRecordDuration.setter
    def StreamRecordDuration(self, StreamRecordDuration):
        self._StreamRecordDuration = StreamRecordDuration


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._StreamRecordDuration = params.get("StreamRecordDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginStatusInfo(AbstractModel):
    """登录态信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户 Id。
        :type UserId: str
        :param _Status: 用户登录状态。
<li>Online：在线；</li>
<li>Offline：离线。</li>
        :type Status: str
        """
        self._UserId = None
        self._Status = None

    @property
    def UserId(self):
        """用户 Id。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Status(self):
        """用户登录状态。
<li>Online：在线；</li>
<li>Offline：离线。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialAddedEvent(AbstractModel):
    """媒体添加事件。

    """

    def __init__(self):
        r"""
        :param _MaterialIdSet: 添加的媒体 Id 列表。
        :type MaterialIdSet: list of str
        :param _Owner: 添加的媒体归属。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _ClassPath: 添加的媒体分类路径。
        :type ClassPath: str
        """
        self._MaterialIdSet = None
        self._Owner = None
        self._ClassPath = None

    @property
    def MaterialIdSet(self):
        """添加的媒体 Id 列表。
        :rtype: list of str
        """
        return self._MaterialIdSet

    @MaterialIdSet.setter
    def MaterialIdSet(self, MaterialIdSet):
        self._MaterialIdSet = MaterialIdSet

    @property
    def Owner(self):
        """添加的媒体归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def ClassPath(self):
        """添加的媒体分类路径。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath


    def _deserialize(self, params):
        self._MaterialIdSet = params.get("MaterialIdSet")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._ClassPath = params.get("ClassPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialBasicInfo(AbstractModel):
    """媒体基本信息。

    """

    def __init__(self):
        r"""
        :param _MaterialId: 媒体 Id。
        :type MaterialId: str
        :param _MaterialType: 媒体类型，取值为：
<li> AUDIO :音频;</li>
<li> VIDEO :视频;</li>
<li> IMAGE :图片;</li>
<li> LINK  :链接.</li>
<li> OTHER : 其他.</li>
        :type MaterialType: str
        :param _Owner: 媒体归属实体。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Name: 媒体名称。
        :type Name: str
        :param _CreateTime: 媒体文件的创建时间，使用 ISO 日期格式。
        :type CreateTime: str
        :param _UpdateTime: 媒体文件的最近更新时间（如修改视频属性、发起视频处理等会触发更新媒体文件信息的操作），使用 ISO 日期格式。
        :type UpdateTime: str
        :param _ClassPath: 媒体的分类路径。
        :type ClassPath: str
        :param _PresetTagSet: 预置标签列表。
        :type PresetTagSet: list of PresetTagInfo
        :param _TagSet: 人工标签列表。
        :type TagSet: list of str
        :param _PreviewUrl: 媒体文件的预览图。
        :type PreviewUrl: str
        :param _TagInfoSet: 媒体绑定的标签信息列表 。
该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInfoSet: list of MaterialTagInfo
        """
        self._MaterialId = None
        self._MaterialType = None
        self._Owner = None
        self._Name = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ClassPath = None
        self._PresetTagSet = None
        self._TagSet = None
        self._PreviewUrl = None
        self._TagInfoSet = None

    @property
    def MaterialId(self):
        """媒体 Id。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def MaterialType(self):
        """媒体类型，取值为：
<li> AUDIO :音频;</li>
<li> VIDEO :视频;</li>
<li> IMAGE :图片;</li>
<li> LINK  :链接.</li>
<li> OTHER : 其他.</li>
        :rtype: str
        """
        return self._MaterialType

    @MaterialType.setter
    def MaterialType(self, MaterialType):
        self._MaterialType = MaterialType

    @property
    def Owner(self):
        """媒体归属实体。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Name(self):
        """媒体名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        """媒体文件的创建时间，使用 ISO 日期格式。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """媒体文件的最近更新时间（如修改视频属性、发起视频处理等会触发更新媒体文件信息的操作），使用 ISO 日期格式。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ClassPath(self):
        """媒体的分类路径。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath

    @property
    def PresetTagSet(self):
        """预置标签列表。
        :rtype: list of PresetTagInfo
        """
        return self._PresetTagSet

    @PresetTagSet.setter
    def PresetTagSet(self, PresetTagSet):
        self._PresetTagSet = PresetTagSet

    @property
    def TagSet(self):
        """人工标签列表。
        :rtype: list of str
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def PreviewUrl(self):
        """媒体文件的预览图。
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def TagInfoSet(self):
        warnings.warn("parameter `TagInfoSet` is deprecated", DeprecationWarning) 

        """媒体绑定的标签信息列表 。
该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MaterialTagInfo
        """
        return self._TagInfoSet

    @TagInfoSet.setter
    def TagInfoSet(self, TagInfoSet):
        warnings.warn("parameter `TagInfoSet` is deprecated", DeprecationWarning) 

        self._TagInfoSet = TagInfoSet


    def _deserialize(self, params):
        self._MaterialId = params.get("MaterialId")
        self._MaterialType = params.get("MaterialType")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ClassPath = params.get("ClassPath")
        if params.get("PresetTagSet") is not None:
            self._PresetTagSet = []
            for item in params.get("PresetTagSet"):
                obj = PresetTagInfo()
                obj._deserialize(item)
                self._PresetTagSet.append(obj)
        self._TagSet = params.get("TagSet")
        self._PreviewUrl = params.get("PreviewUrl")
        if params.get("TagInfoSet") is not None:
            self._TagInfoSet = []
            for item in params.get("TagInfoSet"):
                obj = MaterialTagInfo()
                obj._deserialize(item)
                self._TagInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialDeletedEvent(AbstractModel):
    """媒体删除事件。

    """

    def __init__(self):
        r"""
        :param _MaterialIdSet: 删除的媒体 Id 列表。
        :type MaterialIdSet: list of str
        """
        self._MaterialIdSet = None

    @property
    def MaterialIdSet(self):
        """删除的媒体 Id 列表。
        :rtype: list of str
        """
        return self._MaterialIdSet

    @MaterialIdSet.setter
    def MaterialIdSet(self, MaterialIdSet):
        self._MaterialIdSet = MaterialIdSet


    def _deserialize(self, params):
        self._MaterialIdSet = params.get("MaterialIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialImportedEvent(AbstractModel):
    """媒体导入事件

    """

    def __init__(self):
        r"""
        :param _MediaInfoSet: 导入的媒体信息列表。
        :type MediaInfoSet: list of ImportMediaInfo
        :param _Owner: 媒体归属。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _ClassPath: 媒体分类路径。
        :type ClassPath: str
        """
        self._MediaInfoSet = None
        self._Owner = None
        self._ClassPath = None

    @property
    def MediaInfoSet(self):
        """导入的媒体信息列表。
        :rtype: list of ImportMediaInfo
        """
        return self._MediaInfoSet

    @MediaInfoSet.setter
    def MediaInfoSet(self, MediaInfoSet):
        self._MediaInfoSet = MediaInfoSet

    @property
    def Owner(self):
        """媒体归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def ClassPath(self):
        """媒体分类路径。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath


    def _deserialize(self, params):
        if params.get("MediaInfoSet") is not None:
            self._MediaInfoSet = []
            for item in params.get("MediaInfoSet"):
                obj = ImportMediaInfo()
                obj._deserialize(item)
                self._MediaInfoSet.append(obj)
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._ClassPath = params.get("ClassPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialInfo(AbstractModel):
    """媒体详情信息

    """

    def __init__(self):
        r"""
        :param _BasicInfo: 媒体基本信息。
        :type BasicInfo: :class:`tencentcloud.cme.v20191029.models.MaterialBasicInfo`
        :param _VideoMaterial: 视频媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoMaterial: :class:`tencentcloud.cme.v20191029.models.VideoMaterial`
        :param _AudioMaterial: 音频媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioMaterial: :class:`tencentcloud.cme.v20191029.models.AudioMaterial`
        :param _ImageMaterial: 图片媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageMaterial: :class:`tencentcloud.cme.v20191029.models.ImageMaterial`
        :param _LinkMaterial: 链接媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkMaterial: :class:`tencentcloud.cme.v20191029.models.LinkMaterial`
        :param _VideoEditTemplateMaterial: 模板媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoEditTemplateMaterial: :class:`tencentcloud.cme.v20191029.models.VideoEditTemplateMaterial`
        :param _OtherMaterial: 其他类型媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherMaterial: :class:`tencentcloud.cme.v20191029.models.OtherMaterial`
        """
        self._BasicInfo = None
        self._VideoMaterial = None
        self._AudioMaterial = None
        self._ImageMaterial = None
        self._LinkMaterial = None
        self._VideoEditTemplateMaterial = None
        self._OtherMaterial = None

    @property
    def BasicInfo(self):
        """媒体基本信息。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MaterialBasicInfo`
        """
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def VideoMaterial(self):
        """视频媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoMaterial`
        """
        return self._VideoMaterial

    @VideoMaterial.setter
    def VideoMaterial(self, VideoMaterial):
        self._VideoMaterial = VideoMaterial

    @property
    def AudioMaterial(self):
        """音频媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.AudioMaterial`
        """
        return self._AudioMaterial

    @AudioMaterial.setter
    def AudioMaterial(self, AudioMaterial):
        self._AudioMaterial = AudioMaterial

    @property
    def ImageMaterial(self):
        """图片媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ImageMaterial`
        """
        return self._ImageMaterial

    @ImageMaterial.setter
    def ImageMaterial(self, ImageMaterial):
        self._ImageMaterial = ImageMaterial

    @property
    def LinkMaterial(self):
        """链接媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.LinkMaterial`
        """
        return self._LinkMaterial

    @LinkMaterial.setter
    def LinkMaterial(self, LinkMaterial):
        self._LinkMaterial = LinkMaterial

    @property
    def VideoEditTemplateMaterial(self):
        """模板媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoEditTemplateMaterial`
        """
        return self._VideoEditTemplateMaterial

    @VideoEditTemplateMaterial.setter
    def VideoEditTemplateMaterial(self, VideoEditTemplateMaterial):
        self._VideoEditTemplateMaterial = VideoEditTemplateMaterial

    @property
    def OtherMaterial(self):
        """其他类型媒体信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.OtherMaterial`
        """
        return self._OtherMaterial

    @OtherMaterial.setter
    def OtherMaterial(self, OtherMaterial):
        self._OtherMaterial = OtherMaterial


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self._BasicInfo = MaterialBasicInfo()
            self._BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("VideoMaterial") is not None:
            self._VideoMaterial = VideoMaterial()
            self._VideoMaterial._deserialize(params.get("VideoMaterial"))
        if params.get("AudioMaterial") is not None:
            self._AudioMaterial = AudioMaterial()
            self._AudioMaterial._deserialize(params.get("AudioMaterial"))
        if params.get("ImageMaterial") is not None:
            self._ImageMaterial = ImageMaterial()
            self._ImageMaterial._deserialize(params.get("ImageMaterial"))
        if params.get("LinkMaterial") is not None:
            self._LinkMaterial = LinkMaterial()
            self._LinkMaterial._deserialize(params.get("LinkMaterial"))
        if params.get("VideoEditTemplateMaterial") is not None:
            self._VideoEditTemplateMaterial = VideoEditTemplateMaterial()
            self._VideoEditTemplateMaterial._deserialize(params.get("VideoEditTemplateMaterial"))
        if params.get("OtherMaterial") is not None:
            self._OtherMaterial = OtherMaterial()
            self._OtherMaterial._deserialize(params.get("OtherMaterial"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialModifiedEvent(AbstractModel):
    """媒体更新事件。

    """

    def __init__(self):
        r"""
        :param _MaterialId: 媒体 Id。
        :type MaterialId: str
        :param _Name: 更新后的媒体名称。如未更新则为空。
        :type Name: str
        :param _PresetTagIdSet: 更新后的媒体预置标签列表。如未更新媒体预置标签，则该字段为空数组。
        :type PresetTagIdSet: list of str
        :param _TagSet: 更新后的媒体自定义标签列表。如未更新媒体自定义标签，则该字段为空数组。
        :type TagSet: list of str
        """
        self._MaterialId = None
        self._Name = None
        self._PresetTagIdSet = None
        self._TagSet = None

    @property
    def MaterialId(self):
        """媒体 Id。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def Name(self):
        """更新后的媒体名称。如未更新则为空。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PresetTagIdSet(self):
        """更新后的媒体预置标签列表。如未更新媒体预置标签，则该字段为空数组。
        :rtype: list of str
        """
        return self._PresetTagIdSet

    @PresetTagIdSet.setter
    def PresetTagIdSet(self, PresetTagIdSet):
        self._PresetTagIdSet = PresetTagIdSet

    @property
    def TagSet(self):
        """更新后的媒体自定义标签列表。如未更新媒体自定义标签，则该字段为空数组。
        :rtype: list of str
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._MaterialId = params.get("MaterialId")
        self._Name = params.get("Name")
        self._PresetTagIdSet = params.get("PresetTagIdSet")
        self._TagSet = params.get("TagSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialMovedEvent(AbstractModel):
    """媒体移动事件

    """

    def __init__(self):
        r"""
        :param _MaterialIdSet: 要移动的媒体 Id 列表。
        :type MaterialIdSet: list of str
        :param _SourceOwner: 源媒体归属。
        :type SourceOwner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _SourceClassPath: 源媒体分类路径。
        :type SourceClassPath: str
        :param _DestinationOwner: 目标媒体分类归属。
        :type DestinationOwner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _DestinationClassPath: 目标媒体分类路径。
        :type DestinationClassPath: str
        """
        self._MaterialIdSet = None
        self._SourceOwner = None
        self._SourceClassPath = None
        self._DestinationOwner = None
        self._DestinationClassPath = None

    @property
    def MaterialIdSet(self):
        """要移动的媒体 Id 列表。
        :rtype: list of str
        """
        return self._MaterialIdSet

    @MaterialIdSet.setter
    def MaterialIdSet(self, MaterialIdSet):
        self._MaterialIdSet = MaterialIdSet

    @property
    def SourceOwner(self):
        """源媒体归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._SourceOwner

    @SourceOwner.setter
    def SourceOwner(self, SourceOwner):
        self._SourceOwner = SourceOwner

    @property
    def SourceClassPath(self):
        """源媒体分类路径。
        :rtype: str
        """
        return self._SourceClassPath

    @SourceClassPath.setter
    def SourceClassPath(self, SourceClassPath):
        self._SourceClassPath = SourceClassPath

    @property
    def DestinationOwner(self):
        """目标媒体分类归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._DestinationOwner

    @DestinationOwner.setter
    def DestinationOwner(self, DestinationOwner):
        self._DestinationOwner = DestinationOwner

    @property
    def DestinationClassPath(self):
        """目标媒体分类路径。
        :rtype: str
        """
        return self._DestinationClassPath

    @DestinationClassPath.setter
    def DestinationClassPath(self, DestinationClassPath):
        self._DestinationClassPath = DestinationClassPath


    def _deserialize(self, params):
        self._MaterialIdSet = params.get("MaterialIdSet")
        if params.get("SourceOwner") is not None:
            self._SourceOwner = Entity()
            self._SourceOwner._deserialize(params.get("SourceOwner"))
        self._SourceClassPath = params.get("SourceClassPath")
        if params.get("DestinationOwner") is not None:
            self._DestinationOwner = Entity()
            self._DestinationOwner._deserialize(params.get("DestinationOwner"))
        self._DestinationClassPath = params.get("DestinationClassPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialStatus(AbstractModel):
    """素材的状态，目前仅包含素材编辑可用状态。

    """

    def __init__(self):
        r"""
        :param _EditorUsableStatus: 素材编辑可用状态，取值有：
<li>NORMAL：正常，可直接用于编辑；</li>
<li>ABNORMAL : 异常，不可用于编辑；</li>
<li>PROCESSING：处理中，暂不可用于编辑。</li>
        :type EditorUsableStatus: str
        """
        self._EditorUsableStatus = None

    @property
    def EditorUsableStatus(self):
        """素材编辑可用状态，取值有：
<li>NORMAL：正常，可直接用于编辑；</li>
<li>ABNORMAL : 异常，不可用于编辑；</li>
<li>PROCESSING：处理中，暂不可用于编辑。</li>
        :rtype: str
        """
        return self._EditorUsableStatus

    @EditorUsableStatus.setter
    def EditorUsableStatus(self, EditorUsableStatus):
        self._EditorUsableStatus = EditorUsableStatus


    def _deserialize(self, params):
        self._EditorUsableStatus = params.get("EditorUsableStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialTagInfo(AbstractModel):
    """素材标签信息

    """

    def __init__(self):
        r"""
        :param _Type: 标签类型，取值为：
<li>PRESET：预置标签。</li>
        :type Type: str
        :param _Id: 标签 Id 。当标签类型为 PRESET 时，标签 Id 为预置标签 Id 。
        :type Id: str
        :param _Name: 标签名称。
        :type Name: str
        """
        self._Type = None
        self._Id = None
        self._Name = None

    @property
    def Type(self):
        """标签类型，取值为：
<li>PRESET：预置标签。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Id(self):
        """标签 Id 。当标签类型为 PRESET 时，标签 Id 为预置标签 Id 。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """标签名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastDestinationInfo(AbstractModel):
    """点播转直播输出信息。

    """

    def __init__(self):
        r"""
        :param _Id: 输出源 Id。由系统进行分配。
        :type Id: str
        :param _PushUrl: 输出直播流地址。支持的直播流类型为 RTMP 和 SRT。
        :type PushUrl: str
        :param _Name: 输出源的名称。
        :type Name: str
        """
        self._Id = None
        self._PushUrl = None
        self._Name = None

    @property
    def Id(self):
        """输出源 Id。由系统进行分配。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PushUrl(self):
        """输出直播流地址。支持的直播流类型为 RTMP 和 SRT。
        :rtype: str
        """
        return self._PushUrl

    @PushUrl.setter
    def PushUrl(self, PushUrl):
        self._PushUrl = PushUrl

    @property
    def Name(self):
        """输出源的名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PushUrl = params.get("PushUrl")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastDestinationInterruptInfo(AbstractModel):
    """点播转直播输出断流信息。

    """

    def __init__(self):
        r"""
        :param _DestinationInfo: 发生断流的输出源信息。
        :type DestinationInfo: :class:`tencentcloud.cme.v20191029.models.MediaCastDestinationInfo`
        :param _Reason: 输出源断流原因，取值有：
<li>SystemError：系统错误；</li>
<li>Unknown：未知错误。</li>
        :type Reason: str
        """
        self._DestinationInfo = None
        self._Reason = None

    @property
    def DestinationInfo(self):
        """发生断流的输出源信息。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastDestinationInfo`
        """
        return self._DestinationInfo

    @DestinationInfo.setter
    def DestinationInfo(self, DestinationInfo):
        self._DestinationInfo = DestinationInfo

    @property
    def Reason(self):
        """输出源断流原因，取值有：
<li>SystemError：系统错误；</li>
<li>Unknown：未知错误。</li>
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        if params.get("DestinationInfo") is not None:
            self._DestinationInfo = MediaCastDestinationInfo()
            self._DestinationInfo._deserialize(params.get("DestinationInfo"))
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastDestinationStatus(AbstractModel):
    """点播转直播输出源状态信息。

    """

    def __init__(self):
        r"""
        :param _Id: 输出源 Id，由系统分配。
        :type Id: str
        :param _PushUrl: 输出源直播地址。
        :type PushUrl: str
        :param _Status: 输出源的状态。取值有：
<li> Working ：运行中；</li>
<li> Stopped：停止输出；</li>
<li> Failed：输出失败。</li>
        :type Status: str
        """
        self._Id = None
        self._PushUrl = None
        self._Status = None

    @property
    def Id(self):
        """输出源 Id，由系统分配。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PushUrl(self):
        """输出源直播地址。
        :rtype: str
        """
        return self._PushUrl

    @PushUrl.setter
    def PushUrl(self, PushUrl):
        self._PushUrl = PushUrl

    @property
    def Status(self):
        """输出源的状态。取值有：
<li> Working ：运行中；</li>
<li> Stopped：停止输出；</li>
<li> Failed：输出失败。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PushUrl = params.get("PushUrl")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastOutputMediaSetting(AbstractModel):
    """点播转直播输出媒体配置。

    """

    def __init__(self):
        r"""
        :param _VideoSetting: 视频配置。
        :type VideoSetting: :class:`tencentcloud.cme.v20191029.models.MediaCastVideoSetting`
        :param _FollowSourceInfo: 视频配置是否和第一个输入源的视频配置相同，默认值：false。如果 FollowSourceInfo 的值为 true，忽略 VideoSetting 参数。
        :type FollowSourceInfo: bool
        """
        self._VideoSetting = None
        self._FollowSourceInfo = None

    @property
    def VideoSetting(self):
        """视频配置。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastVideoSetting`
        """
        return self._VideoSetting

    @VideoSetting.setter
    def VideoSetting(self, VideoSetting):
        self._VideoSetting = VideoSetting

    @property
    def FollowSourceInfo(self):
        """视频配置是否和第一个输入源的视频配置相同，默认值：false。如果 FollowSourceInfo 的值为 true，忽略 VideoSetting 参数。
        :rtype: bool
        """
        return self._FollowSourceInfo

    @FollowSourceInfo.setter
    def FollowSourceInfo(self, FollowSourceInfo):
        self._FollowSourceInfo = FollowSourceInfo


    def _deserialize(self, params):
        if params.get("VideoSetting") is not None:
            self._VideoSetting = MediaCastVideoSetting()
            self._VideoSetting._deserialize(params.get("VideoSetting"))
        self._FollowSourceInfo = params.get("FollowSourceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastPlayInfo(AbstractModel):
    """点播转直播播放信息。

    """

    def __init__(self):
        r"""
        :param _Status: 点播转直播项目运行状态，取值有：
<li> Working : 运行中；</li>
<li> Idle: 空闲状态。</li>
        :type Status: str
        :param _CurrentSourceId: 当前播放的输入源 Id。
        :type CurrentSourceId: str
        :param _CurrentSourcePosition: 当前播放的输入源的播放位置，单位：秒。
        :type CurrentSourcePosition: float
        :param _CurrentSourceDuration: 当前播放的输入源时长，单位：秒。
        :type CurrentSourceDuration: float
        :param _DestinationStatusSet: 输出源状态信息。
        :type DestinationStatusSet: list of MediaCastDestinationStatus
        :param _LoopCount: 已经循环播放的次数。
        :type LoopCount: int
        """
        self._Status = None
        self._CurrentSourceId = None
        self._CurrentSourcePosition = None
        self._CurrentSourceDuration = None
        self._DestinationStatusSet = None
        self._LoopCount = None

    @property
    def Status(self):
        """点播转直播项目运行状态，取值有：
<li> Working : 运行中；</li>
<li> Idle: 空闲状态。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CurrentSourceId(self):
        """当前播放的输入源 Id。
        :rtype: str
        """
        return self._CurrentSourceId

    @CurrentSourceId.setter
    def CurrentSourceId(self, CurrentSourceId):
        self._CurrentSourceId = CurrentSourceId

    @property
    def CurrentSourcePosition(self):
        """当前播放的输入源的播放位置，单位：秒。
        :rtype: float
        """
        return self._CurrentSourcePosition

    @CurrentSourcePosition.setter
    def CurrentSourcePosition(self, CurrentSourcePosition):
        self._CurrentSourcePosition = CurrentSourcePosition

    @property
    def CurrentSourceDuration(self):
        """当前播放的输入源时长，单位：秒。
        :rtype: float
        """
        return self._CurrentSourceDuration

    @CurrentSourceDuration.setter
    def CurrentSourceDuration(self, CurrentSourceDuration):
        self._CurrentSourceDuration = CurrentSourceDuration

    @property
    def DestinationStatusSet(self):
        """输出源状态信息。
        :rtype: list of MediaCastDestinationStatus
        """
        return self._DestinationStatusSet

    @DestinationStatusSet.setter
    def DestinationStatusSet(self, DestinationStatusSet):
        self._DestinationStatusSet = DestinationStatusSet

    @property
    def LoopCount(self):
        """已经循环播放的次数。
        :rtype: int
        """
        return self._LoopCount

    @LoopCount.setter
    def LoopCount(self, LoopCount):
        self._LoopCount = LoopCount


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._CurrentSourceId = params.get("CurrentSourceId")
        self._CurrentSourcePosition = params.get("CurrentSourcePosition")
        self._CurrentSourceDuration = params.get("CurrentSourceDuration")
        if params.get("DestinationStatusSet") is not None:
            self._DestinationStatusSet = []
            for item in params.get("DestinationStatusSet"):
                obj = MediaCastDestinationStatus()
                obj._deserialize(item)
                self._DestinationStatusSet.append(obj)
        self._LoopCount = params.get("LoopCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastPlaySetting(AbstractModel):
    """播放控制参数。

    """

    def __init__(self):
        r"""
        :param _LoopCount: 循环播放次数。LoopCount 和 EndTime 同时只能有一个生效。默认循环播放次数为一次。如果同时设置了 LoopCount 和 EndTime 参数，优先使用 LoopCount 参数。
        :type LoopCount: int
        :param _EndTime: 结束时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param _AutoStartTime: 自动启动时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type AutoStartTime: str
        """
        self._LoopCount = None
        self._EndTime = None
        self._AutoStartTime = None

    @property
    def LoopCount(self):
        """循环播放次数。LoopCount 和 EndTime 同时只能有一个生效。默认循环播放次数为一次。如果同时设置了 LoopCount 和 EndTime 参数，优先使用 LoopCount 参数。
        :rtype: int
        """
        return self._LoopCount

    @LoopCount.setter
    def LoopCount(self, LoopCount):
        self._LoopCount = LoopCount

    @property
    def EndTime(self):
        """结束时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AutoStartTime(self):
        """自动启动时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :rtype: str
        """
        return self._AutoStartTime

    @AutoStartTime.setter
    def AutoStartTime(self, AutoStartTime):
        self._AutoStartTime = AutoStartTime


    def _deserialize(self, params):
        self._LoopCount = params.get("LoopCount")
        self._EndTime = params.get("EndTime")
        self._AutoStartTime = params.get("AutoStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastProjectInfo(AbstractModel):
    """点播转直播项目信息。

    """

    def __init__(self):
        r"""
        :param _Status: 点播转直播项目状态，取值有：
<li>Working ：运行中；</li>
<li>Idle ：空闲。</li>
        :type Status: str
        :param _SourceInfos: 输入源列表。
        :type SourceInfos: list of MediaCastSourceInfo
        :param _DestinationInfos: 输出源列表。
        :type DestinationInfos: list of MediaCastDestinationInfo
        :param _OutputMediaSetting: 输出媒体配置。
        :type OutputMediaSetting: :class:`tencentcloud.cme.v20191029.models.MediaCastOutputMediaSetting`
        :param _PlaySetting: 播放参数。
        :type PlaySetting: :class:`tencentcloud.cme.v20191029.models.MediaCastPlaySetting`
        :param _StartTime: 项目启动时间。采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param _StopTime: 项目结束时间。采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。如果项目还在运行中，该字段为空。
        :type StopTime: str
        :param _Duration: 推流时长，单位：秒。项目结束后，返回上次项目运行时的推流时长。如果项目是 Working 状态，返回的时长是0。
        :type Duration: float
        """
        self._Status = None
        self._SourceInfos = None
        self._DestinationInfos = None
        self._OutputMediaSetting = None
        self._PlaySetting = None
        self._StartTime = None
        self._StopTime = None
        self._Duration = None

    @property
    def Status(self):
        """点播转直播项目状态，取值有：
<li>Working ：运行中；</li>
<li>Idle ：空闲。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceInfos(self):
        """输入源列表。
        :rtype: list of MediaCastSourceInfo
        """
        return self._SourceInfos

    @SourceInfos.setter
    def SourceInfos(self, SourceInfos):
        self._SourceInfos = SourceInfos

    @property
    def DestinationInfos(self):
        """输出源列表。
        :rtype: list of MediaCastDestinationInfo
        """
        return self._DestinationInfos

    @DestinationInfos.setter
    def DestinationInfos(self, DestinationInfos):
        self._DestinationInfos = DestinationInfos

    @property
    def OutputMediaSetting(self):
        """输出媒体配置。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastOutputMediaSetting`
        """
        return self._OutputMediaSetting

    @OutputMediaSetting.setter
    def OutputMediaSetting(self, OutputMediaSetting):
        self._OutputMediaSetting = OutputMediaSetting

    @property
    def PlaySetting(self):
        """播放参数。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastPlaySetting`
        """
        return self._PlaySetting

    @PlaySetting.setter
    def PlaySetting(self, PlaySetting):
        self._PlaySetting = PlaySetting

    @property
    def StartTime(self):
        """项目启动时间。采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StopTime(self):
        """项目结束时间。采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。如果项目还在运行中，该字段为空。
        :rtype: str
        """
        return self._StopTime

    @StopTime.setter
    def StopTime(self, StopTime):
        self._StopTime = StopTime

    @property
    def Duration(self):
        """推流时长，单位：秒。项目结束后，返回上次项目运行时的推流时长。如果项目是 Working 状态，返回的时长是0。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("SourceInfos") is not None:
            self._SourceInfos = []
            for item in params.get("SourceInfos"):
                obj = MediaCastSourceInfo()
                obj._deserialize(item)
                self._SourceInfos.append(obj)
        if params.get("DestinationInfos") is not None:
            self._DestinationInfos = []
            for item in params.get("DestinationInfos"):
                obj = MediaCastDestinationInfo()
                obj._deserialize(item)
                self._DestinationInfos.append(obj)
        if params.get("OutputMediaSetting") is not None:
            self._OutputMediaSetting = MediaCastOutputMediaSetting()
            self._OutputMediaSetting._deserialize(params.get("OutputMediaSetting"))
        if params.get("PlaySetting") is not None:
            self._PlaySetting = MediaCastPlaySetting()
            self._PlaySetting._deserialize(params.get("PlaySetting"))
        self._StartTime = params.get("StartTime")
        self._StopTime = params.get("StopTime")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastProjectInput(AbstractModel):
    """点播转直播项目输入信息。

    """

    def __init__(self):
        r"""
        :param _SourceInfos: 输入源列表。输入源列表最大个数为100.
        :type SourceInfos: list of MediaCastSourceInfo
        :param _DestinationInfos: 输出源列表。输出源列表最大个数为10.
        :type DestinationInfos: list of MediaCastDestinationInfo
        :param _OutputMediaSetting: 输出媒体配置。
        :type OutputMediaSetting: :class:`tencentcloud.cme.v20191029.models.MediaCastOutputMediaSetting`
        :param _PlaySetting: 播放控制参数。
        :type PlaySetting: :class:`tencentcloud.cme.v20191029.models.MediaCastPlaySetting`
        """
        self._SourceInfos = None
        self._DestinationInfos = None
        self._OutputMediaSetting = None
        self._PlaySetting = None

    @property
    def SourceInfos(self):
        """输入源列表。输入源列表最大个数为100.
        :rtype: list of MediaCastSourceInfo
        """
        return self._SourceInfos

    @SourceInfos.setter
    def SourceInfos(self, SourceInfos):
        self._SourceInfos = SourceInfos

    @property
    def DestinationInfos(self):
        """输出源列表。输出源列表最大个数为10.
        :rtype: list of MediaCastDestinationInfo
        """
        return self._DestinationInfos

    @DestinationInfos.setter
    def DestinationInfos(self, DestinationInfos):
        self._DestinationInfos = DestinationInfos

    @property
    def OutputMediaSetting(self):
        """输出媒体配置。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastOutputMediaSetting`
        """
        return self._OutputMediaSetting

    @OutputMediaSetting.setter
    def OutputMediaSetting(self, OutputMediaSetting):
        self._OutputMediaSetting = OutputMediaSetting

    @property
    def PlaySetting(self):
        """播放控制参数。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastPlaySetting`
        """
        return self._PlaySetting

    @PlaySetting.setter
    def PlaySetting(self, PlaySetting):
        self._PlaySetting = PlaySetting


    def _deserialize(self, params):
        if params.get("SourceInfos") is not None:
            self._SourceInfos = []
            for item in params.get("SourceInfos"):
                obj = MediaCastSourceInfo()
                obj._deserialize(item)
                self._SourceInfos.append(obj)
        if params.get("DestinationInfos") is not None:
            self._DestinationInfos = []
            for item in params.get("DestinationInfos"):
                obj = MediaCastDestinationInfo()
                obj._deserialize(item)
                self._DestinationInfos.append(obj)
        if params.get("OutputMediaSetting") is not None:
            self._OutputMediaSetting = MediaCastOutputMediaSetting()
            self._OutputMediaSetting._deserialize(params.get("OutputMediaSetting"))
        if params.get("PlaySetting") is not None:
            self._PlaySetting = MediaCastPlaySetting()
            self._PlaySetting._deserialize(params.get("PlaySetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastSourceInfo(AbstractModel):
    """点播转直播输入源信息。

    """

    def __init__(self):
        r"""
        :param _Id: 输入源 Id，由系统分配。
        :type Id: str
        :param _Type: 输入源的媒体类型，取值有：
<li>CME：多媒体创作引擎的媒体文件；</li>
<li>VOD：云点播的媒资文件。</li>
<li>EXTERNAL：非多媒体创建引擎或者云点播的媒资文件。</li>
        :type Type: str
        :param _FileId: 云点播媒体文件 ID。当 Type = VOD 时必填。
        :type FileId: str
        :param _MaterialId: 多媒体创作引擎的媒体 ID。当 Type = CME  时必填。
        :type MaterialId: str
        :param _Offset: 文件播放的起始位置，单位：秒。默认为0，从文件头开始播放。当 Type = CME  或者 VOD 时有效。
        :type Offset: float
        :param _Duration: 播放时长，单位：秒。默认播放整个文件。当 Type = CME  或者 VOD 时有效。
        :type Duration: float
        :param _Url: 外部文件的 Url， Type=EXTERNAL 时必填，可以是点播文件或者直播文件，支持的 Scheme 包括HTTP、HTTPS、RTMP。
        :type Url: str
        """
        self._Id = None
        self._Type = None
        self._FileId = None
        self._MaterialId = None
        self._Offset = None
        self._Duration = None
        self._Url = None

    @property
    def Id(self):
        """输入源 Id，由系统分配。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """输入源的媒体类型，取值有：
<li>CME：多媒体创作引擎的媒体文件；</li>
<li>VOD：云点播的媒资文件。</li>
<li>EXTERNAL：非多媒体创建引擎或者云点播的媒资文件。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FileId(self):
        """云点播媒体文件 ID。当 Type = VOD 时必填。
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def MaterialId(self):
        """多媒体创作引擎的媒体 ID。当 Type = CME  时必填。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def Offset(self):
        """文件播放的起始位置，单位：秒。默认为0，从文件头开始播放。当 Type = CME  或者 VOD 时有效。
        :rtype: float
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Duration(self):
        """播放时长，单位：秒。默认播放整个文件。当 Type = CME  或者 VOD 时有效。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Url(self):
        """外部文件的 Url， Type=EXTERNAL 时必填，可以是点播文件或者直播文件，支持的 Scheme 包括HTTP、HTTPS、RTMP。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._FileId = params.get("FileId")
        self._MaterialId = params.get("MaterialId")
        self._Offset = params.get("Offset")
        self._Duration = params.get("Duration")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastSourceInterruptInfo(AbstractModel):
    """点播转直播输入断流信息。

    """

    def __init__(self):
        r"""
        :param _SourceInfo: 发生断流的输入源信息。
        :type SourceInfo: :class:`tencentcloud.cme.v20191029.models.MediaCastSourceInfo`
        :param _Reason: 输入源断开原因。取值有：
<li>SystemError：系统错误；</li>
<li>Unknown：未知错误。</li>
        :type Reason: str
        """
        self._SourceInfo = None
        self._Reason = None

    @property
    def SourceInfo(self):
        """发生断流的输入源信息。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastSourceInfo`
        """
        return self._SourceInfo

    @SourceInfo.setter
    def SourceInfo(self, SourceInfo):
        self._SourceInfo = SourceInfo

    @property
    def Reason(self):
        """输入源断开原因。取值有：
<li>SystemError：系统错误；</li>
<li>Unknown：未知错误。</li>
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        if params.get("SourceInfo") is not None:
            self._SourceInfo = MediaCastSourceInfo()
            self._SourceInfo._deserialize(params.get("SourceInfo"))
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaCastVideoSetting(AbstractModel):
    """点播转直播视频配置

    """

    def __init__(self):
        r"""
        :param _Width: 视频宽度，单位：px，默认值为1280。
        :type Width: int
        :param _Height: 视频高度，单位：px，默认值为720。支持的视频分辨率最大为1920*1080。
        :type Height: int
        :param _Bitrate: 视频码率，单位：kbps，默认值为2500。最大值为10000 kbps。
        :type Bitrate: int
        :param _FrameRate: 视频帧率，单位：Hz，默认值为25。最大值为60。
        :type FrameRate: float
        """
        self._Width = None
        self._Height = None
        self._Bitrate = None
        self._FrameRate = None

    @property
    def Width(self):
        """视频宽度，单位：px，默认值为1280。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """视频高度，单位：px，默认值为720。支持的视频分辨率最大为1920*1080。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Bitrate(self):
        """视频码率，单位：kbps，默认值为2500。最大值为10000 kbps。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def FrameRate(self):
        """视频帧率，单位：Hz，默认值为25。最大值为60。
        :rtype: float
        """
        return self._FrameRate

    @FrameRate.setter
    def FrameRate(self, FrameRate):
        self._FrameRate = FrameRate


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Bitrate = params.get("Bitrate")
        self._FrameRate = params.get("FrameRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaImageSpriteInfo(AbstractModel):
    """雪碧图

    """

    def __init__(self):
        r"""
        :param _Height: 雪碧图小图的高度。
        :type Height: int
        :param _Width: 雪碧图小图的宽度。
        :type Width: int
        :param _TotalCount: 雪碧图小图的总数量。
        :type TotalCount: int
        :param _ImageUrlSet: 截取雪碧图输出的地址。
        :type ImageUrlSet: list of str
        :param _WebVttUrl: 雪碧图子图位置与时间关系的 WebVtt 文件地址。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在雪碧大图里的坐标位置，一般被播放器用于实现预览。
        :type WebVttUrl: str
        """
        self._Height = None
        self._Width = None
        self._TotalCount = None
        self._ImageUrlSet = None
        self._WebVttUrl = None

    @property
    def Height(self):
        """雪碧图小图的高度。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        """雪碧图小图的宽度。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def TotalCount(self):
        """雪碧图小图的总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ImageUrlSet(self):
        """截取雪碧图输出的地址。
        :rtype: list of str
        """
        return self._ImageUrlSet

    @ImageUrlSet.setter
    def ImageUrlSet(self, ImageUrlSet):
        self._ImageUrlSet = ImageUrlSet

    @property
    def WebVttUrl(self):
        """雪碧图子图位置与时间关系的 WebVtt 文件地址。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在雪碧大图里的坐标位置，一般被播放器用于实现预览。
        :rtype: str
        """
        return self._WebVttUrl

    @WebVttUrl.setter
    def WebVttUrl(self, WebVttUrl):
        self._WebVttUrl = WebVttUrl


    def _deserialize(self, params):
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._TotalCount = params.get("TotalCount")
        self._ImageUrlSet = params.get("ImageUrlSet")
        self._WebVttUrl = params.get("WebVttUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaMetaData(AbstractModel):
    """文件元信息。

    """

    def __init__(self):
        r"""
        :param _Size: 大小。
        :type Size: int
        :param _Container: 容器类型。
        :type Container: str
        :param _Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。
        :type Bitrate: int
        :param _Height: 视频流高度的最大值，单位：px。
        :type Height: int
        :param _Width: 视频流宽度的最大值，单位：px。
        :type Width: int
        :param _Duration: 时长，单位：秒。
        :type Duration: float
        :param _Rotate: 视频拍摄时的选择角度，单位：度
        :type Rotate: int
        :param _VideoStreamInfoSet: 视频流信息。
        :type VideoStreamInfoSet: list of VideoStreamInfo
        :param _AudioStreamInfoSet: 音频流信息。
        :type AudioStreamInfoSet: list of AudioStreamInfo
        """
        self._Size = None
        self._Container = None
        self._Bitrate = None
        self._Height = None
        self._Width = None
        self._Duration = None
        self._Rotate = None
        self._VideoStreamInfoSet = None
        self._AudioStreamInfoSet = None

    @property
    def Size(self):
        """大小。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Container(self):
        """容器类型。
        :rtype: str
        """
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def Bitrate(self):
        """视频流码率平均值与音频流码率平均值之和，单位：bps。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Height(self):
        """视频流高度的最大值，单位：px。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        """视频流宽度的最大值，单位：px。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Duration(self):
        """时长，单位：秒。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Rotate(self):
        """视频拍摄时的选择角度，单位：度
        :rtype: int
        """
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate

    @property
    def VideoStreamInfoSet(self):
        """视频流信息。
        :rtype: list of VideoStreamInfo
        """
        return self._VideoStreamInfoSet

    @VideoStreamInfoSet.setter
    def VideoStreamInfoSet(self, VideoStreamInfoSet):
        self._VideoStreamInfoSet = VideoStreamInfoSet

    @property
    def AudioStreamInfoSet(self):
        """音频流信息。
        :rtype: list of AudioStreamInfo
        """
        return self._AudioStreamInfoSet

    @AudioStreamInfoSet.setter
    def AudioStreamInfoSet(self, AudioStreamInfoSet):
        self._AudioStreamInfoSet = AudioStreamInfoSet


    def _deserialize(self, params):
        self._Size = params.get("Size")
        self._Container = params.get("Container")
        self._Bitrate = params.get("Bitrate")
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._Duration = params.get("Duration")
        self._Rotate = params.get("Rotate")
        if params.get("VideoStreamInfoSet") is not None:
            self._VideoStreamInfoSet = []
            for item in params.get("VideoStreamInfoSet"):
                obj = VideoStreamInfo()
                obj._deserialize(item)
                self._VideoStreamInfoSet.append(obj)
        if params.get("AudioStreamInfoSet") is not None:
            self._AudioStreamInfoSet = []
            for item in params.get("AudioStreamInfoSet"):
                obj = AudioStreamInfo()
                obj._deserialize(item)
                self._AudioStreamInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaPreprocessOperation(AbstractModel):
    """媒体处理视频合成任务的预处理操作。

    """

    def __init__(self):
        r"""
        :param _Type: 预处理操作的类型，取值范围：
<li>ImageTextMask：图片文字遮罩。</li>
        :type Type: str
        :param _Args: 预处理操作参数。
当 Type 取值 ImageTextMask 时，参数为要保留的文字。
        :type Args: list of str
        """
        self._Type = None
        self._Args = None

    @property
    def Type(self):
        """预处理操作的类型，取值范围：
<li>ImageTextMask：图片文字遮罩。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Args(self):
        """预处理操作参数。
当 Type 取值 ImageTextMask 时，参数为要保留的文字。
        :rtype: list of str
        """
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Args = params.get("Args")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaReplacementInfo(AbstractModel):
    """媒体替换信息。

    """

    def __init__(self):
        r"""
        :param _MediaType: 替换的媒体类型，取值有：
<li>CMEMaterialId：替换的媒体类型为媒体 ID；</li>
<li>ImageUrl：替换的媒体类型为图片 URL；</li>

注：默认为 CMEMaterialId 。
        :type MediaType: str
        :param _MaterialId: 媒体 ID。
当媒体类型取值为 CMEMaterialId 时有效。
        :type MaterialId: str
        :param _MediaUrl: 媒体 URL。
当媒体类型取值为 ImageUrl 时有效，
图片仅支持 jpg、png 格式，且大小不超过 2M 。
        :type MediaUrl: str
        :param _StartTimeOffset: 替换媒体选取的开始时间，单位为秒，默认为 0。
        :type StartTimeOffset: float
        :param _PreprocessOperation: 预处理操作。
注：目前该功能暂不支持，请勿使用。
        :type PreprocessOperation: :class:`tencentcloud.cme.v20191029.models.MediaPreprocessOperation`
        """
        self._MediaType = None
        self._MaterialId = None
        self._MediaUrl = None
        self._StartTimeOffset = None
        self._PreprocessOperation = None

    @property
    def MediaType(self):
        """替换的媒体类型，取值有：
<li>CMEMaterialId：替换的媒体类型为媒体 ID；</li>
<li>ImageUrl：替换的媒体类型为图片 URL；</li>

注：默认为 CMEMaterialId 。
        :rtype: str
        """
        return self._MediaType

    @MediaType.setter
    def MediaType(self, MediaType):
        self._MediaType = MediaType

    @property
    def MaterialId(self):
        """媒体 ID。
当媒体类型取值为 CMEMaterialId 时有效。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def MediaUrl(self):
        """媒体 URL。
当媒体类型取值为 ImageUrl 时有效，
图片仅支持 jpg、png 格式，且大小不超过 2M 。
        :rtype: str
        """
        return self._MediaUrl

    @MediaUrl.setter
    def MediaUrl(self, MediaUrl):
        self._MediaUrl = MediaUrl

    @property
    def StartTimeOffset(self):
        """替换媒体选取的开始时间，单位为秒，默认为 0。
        :rtype: float
        """
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def PreprocessOperation(self):
        """预处理操作。
注：目前该功能暂不支持，请勿使用。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaPreprocessOperation`
        """
        return self._PreprocessOperation

    @PreprocessOperation.setter
    def PreprocessOperation(self, PreprocessOperation):
        self._PreprocessOperation = PreprocessOperation


    def _deserialize(self, params):
        self._MediaType = params.get("MediaType")
        self._MaterialId = params.get("MaterialId")
        self._MediaUrl = params.get("MediaUrl")
        self._StartTimeOffset = params.get("StartTimeOffset")
        if params.get("PreprocessOperation") is not None:
            self._PreprocessOperation = MediaPreprocessOperation()
            self._PreprocessOperation._deserialize(params.get("PreprocessOperation"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTrack(AbstractModel):
    """轨道信息

    """

    def __init__(self):
        r"""
        :param _Type: 轨道类型，取值有：
<ul>
<li>Video ：视频轨道。视频轨道由以下 Item 组成：<ul><li>VideoTrackItem</li><li>EmptyTrackItem</li><li>MediaTransitionItem</li></ul> </li>
<li>Audio ：音频轨道。音频轨道由以下 Item 组成：<ul><li>AudioTrackItem</li><li>EmptyTrackItem</li></ul> </li>
</ul>
        :type Type: str
        :param _TrackItems: 轨道上的媒体片段列表。
        :type TrackItems: list of MediaTrackItem
        """
        self._Type = None
        self._TrackItems = None

    @property
    def Type(self):
        """轨道类型，取值有：
<ul>
<li>Video ：视频轨道。视频轨道由以下 Item 组成：<ul><li>VideoTrackItem</li><li>EmptyTrackItem</li><li>MediaTransitionItem</li></ul> </li>
<li>Audio ：音频轨道。音频轨道由以下 Item 组成：<ul><li>AudioTrackItem</li><li>EmptyTrackItem</li></ul> </li>
</ul>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TrackItems(self):
        """轨道上的媒体片段列表。
        :rtype: list of MediaTrackItem
        """
        return self._TrackItems

    @TrackItems.setter
    def TrackItems(self, TrackItems):
        self._TrackItems = TrackItems


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("TrackItems") is not None:
            self._TrackItems = []
            for item in params.get("TrackItems"):
                obj = MediaTrackItem()
                obj._deserialize(item)
                self._TrackItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTrackItem(AbstractModel):
    """媒体轨道的片段信息

    """

    def __init__(self):
        r"""
        :param _Type: 片段类型。取值有：
<li>Video：视频片段；</li>
<li>Audio：音频片段；</li>
<li>Empty：空白片段；</li>
<li>Transition：转场。</li>
        :type Type: str
        :param _VideoItem: 视频片段，当 Type = Video 时有效。
        :type VideoItem: :class:`tencentcloud.cme.v20191029.models.VideoTrackItem`
        :param _AudioItem: 音频片段，当 Type = Audio 时有效。
        :type AudioItem: :class:`tencentcloud.cme.v20191029.models.AudioTrackItem`
        :param _EmptyItem: 空白片段，当 Type = Empty 时有效。空片段用于时间轴的占位。<li>如需要两个音频片段之间有一段时间的静音，可以用 EmptyTrackItem 来进行占位。</li>
<li>使用 EmptyTrackItem 进行占位，来定位某个Item。</li>
        :type EmptyItem: :class:`tencentcloud.cme.v20191029.models.EmptyTrackItem`
        :param _TransitionItem: 转场，当 Type = Transition 时有效。
        :type TransitionItem: :class:`tencentcloud.cme.v20191029.models.MediaTransitionItem`
        """
        self._Type = None
        self._VideoItem = None
        self._AudioItem = None
        self._EmptyItem = None
        self._TransitionItem = None

    @property
    def Type(self):
        """片段类型。取值有：
<li>Video：视频片段；</li>
<li>Audio：音频片段；</li>
<li>Empty：空白片段；</li>
<li>Transition：转场。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VideoItem(self):
        """视频片段，当 Type = Video 时有效。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoTrackItem`
        """
        return self._VideoItem

    @VideoItem.setter
    def VideoItem(self, VideoItem):
        self._VideoItem = VideoItem

    @property
    def AudioItem(self):
        """音频片段，当 Type = Audio 时有效。
        :rtype: :class:`tencentcloud.cme.v20191029.models.AudioTrackItem`
        """
        return self._AudioItem

    @AudioItem.setter
    def AudioItem(self, AudioItem):
        self._AudioItem = AudioItem

    @property
    def EmptyItem(self):
        """空白片段，当 Type = Empty 时有效。空片段用于时间轴的占位。<li>如需要两个音频片段之间有一段时间的静音，可以用 EmptyTrackItem 来进行占位。</li>
<li>使用 EmptyTrackItem 进行占位，来定位某个Item。</li>
        :rtype: :class:`tencentcloud.cme.v20191029.models.EmptyTrackItem`
        """
        return self._EmptyItem

    @EmptyItem.setter
    def EmptyItem(self, EmptyItem):
        self._EmptyItem = EmptyItem

    @property
    def TransitionItem(self):
        """转场，当 Type = Transition 时有效。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaTransitionItem`
        """
        return self._TransitionItem

    @TransitionItem.setter
    def TransitionItem(self, TransitionItem):
        self._TransitionItem = TransitionItem


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("VideoItem") is not None:
            self._VideoItem = VideoTrackItem()
            self._VideoItem._deserialize(params.get("VideoItem"))
        if params.get("AudioItem") is not None:
            self._AudioItem = AudioTrackItem()
            self._AudioItem._deserialize(params.get("AudioItem"))
        if params.get("EmptyItem") is not None:
            self._EmptyItem = EmptyTrackItem()
            self._EmptyItem._deserialize(params.get("EmptyItem"))
        if params.get("TransitionItem") is not None:
            self._TransitionItem = MediaTransitionItem()
            self._TransitionItem._deserialize(params.get("TransitionItem"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTransitionItem(AbstractModel):
    """转场信息

    """

    def __init__(self):
        r"""
        :param _TransitionId: 转场 Id 。暂只支持一个转场。
        :type TransitionId: str
        :param _Duration: 转场持续时间，单位为秒，默认为2秒。进行转场处理的两个媒体片段，第二个片段在轨道上的起始时间会自动进行调整，设置为前面一个片段的结束时间减去转场的持续时间。
        :type Duration: float
        """
        self._TransitionId = None
        self._Duration = None

    @property
    def TransitionId(self):
        """转场 Id 。暂只支持一个转场。
        :rtype: str
        """
        return self._TransitionId

    @TransitionId.setter
    def TransitionId(self, TransitionId):
        self._TransitionId = TransitionId

    @property
    def Duration(self):
        """转场持续时间，单位为秒，默认为2秒。进行转场处理的两个媒体片段，第二个片段在轨道上的起始时间会自动进行调整，设置为前面一个片段的结束时间减去转场的持续时间。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._TransitionId = params.get("TransitionId")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaterialRequest(AbstractModel):
    """ModifyMaterial请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _MaterialId: 要修改的媒体 Id。
        :type MaterialId: str
        :param _Owner: 媒体归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Name: 媒体名称，不能超过30个字符，不填则不修改。
        :type Name: str
        :param _ClassPath: 媒体分类路径，例如填写"/a/b"，则代表该媒体存储的路径为"/a/b"。若修改分类路径，则 Owner 字段必填。
        :type ClassPath: str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以修改任意媒体的信息。如果指定操作者，则操作者必须对媒体有写权限。
        :type Operator: str
        """
        self._Platform = None
        self._MaterialId = None
        self._Owner = None
        self._Name = None
        self._ClassPath = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def MaterialId(self):
        """要修改的媒体 Id。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def Owner(self):
        """媒体归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Name(self):
        """媒体名称，不能超过30个字符，不填则不修改。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ClassPath(self):
        """媒体分类路径，例如填写"/a/b"，则代表该媒体存储的路径为"/a/b"。若修改分类路径，则 Owner 字段必填。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以修改任意媒体的信息。如果指定操作者，则操作者必须对媒体有写权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._MaterialId = params.get("MaterialId")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Name = params.get("Name")
        self._ClassPath = params.get("ClassPath")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaterialResponse(AbstractModel):
    """ModifyMaterial返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _ProjectId: 项目 Id。
        :type ProjectId: str
        :param _Name: 项目名称，不可超过30个字符。
        :type Name: str
        :param _AspectRatio: 画布宽高比，值为视频编辑项目画布宽与高的像素值的比值，如 16:9、9:16 等。
        :type AspectRatio: str
        :param _Owner: 项目所有者。目前仅支持个人项目，不支持团队项目。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Mode: 项目模式，一个项目可以有多种模式并相互切换。
当 Category 为 VIDEO_EDIT 时，可选模式有：
<li>Default：默认模式，即普通视频编辑项目。</li>
<li>VideoEditTemplate：剪辑模板制作模式，用于制作剪辑模板。</li>
        :type Mode: str
        """
        self._Platform = None
        self._ProjectId = None
        self._Name = None
        self._AspectRatio = None
        self._Owner = None
        self._Mode = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ProjectId(self):
        """项目 Id。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        """项目名称，不可超过30个字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AspectRatio(self):
        """画布宽高比，值为视频编辑项目画布宽与高的像素值的比值，如 16:9、9:16 等。
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def Owner(self):
        """项目所有者。目前仅支持个人项目，不支持团队项目。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Mode(self):
        """项目模式，一个项目可以有多种模式并相互切换。
当 Category 为 VIDEO_EDIT 时，可选模式有：
<li>Default：默认模式，即普通视频编辑项目。</li>
<li>VideoEditTemplate：剪辑模板制作模式，用于制作剪辑模板。</li>
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._AspectRatio = params.get("AspectRatio")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTeamMemberRequest(AbstractModel):
    """ModifyTeamMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _TeamId: 团队 ID。
        :type TeamId: str
        :param _MemberId: 团队成员 ID。
        :type MemberId: str
        :param _Remark: 成员备注，长度不能超过15个字符。
        :type Remark: str
        :param _Role: 成员角色，可取值有：
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :type Role: str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以修改任意团队成员的信息。如果指定操作者，则操作者必须为团队的管理员或者所有者。
        :type Operator: str
        """
        self._Platform = None
        self._TeamId = None
        self._MemberId = None
        self._Remark = None
        self._Role = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TeamId(self):
        """团队 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def MemberId(self):
        """团队成员 ID。
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Remark(self):
        """成员备注，长度不能超过15个字符。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Role(self):
        """成员角色，可取值有：
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以修改任意团队成员的信息。如果指定操作者，则操作者必须为团队的管理员或者所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._TeamId = params.get("TeamId")
        self._MemberId = params.get("MemberId")
        self._Remark = params.get("Remark")
        self._Role = params.get("Role")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTeamMemberResponse(AbstractModel):
    """ModifyTeamMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTeamRequest(AbstractModel):
    """ModifyTeam请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _TeamId: 团队 ID。
        :type TeamId: str
        :param _Name: 团队名称。团队名称不能置空，并且不能超过30个字符。
        :type Name: str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以修改所有团队的信息。如果指定操作者，则操作者必须为团队管理员或者所有者。
        :type Operator: str
        """
        self._Platform = None
        self._TeamId = None
        self._Name = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TeamId(self):
        """团队 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Name(self):
        """团队名称。团队名称不能置空，并且不能超过30个字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以修改所有团队的信息。如果指定操作者，则操作者必须为团队管理员或者所有者。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._TeamId = params.get("TeamId")
        self._Name = params.get("Name")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTeamResponse(AbstractModel):
    """ModifyTeam返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyVideoEncodingPresetRequest(AbstractModel):
    """ModifyVideoEncodingPreset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Id: 配置 ID。
        :type Id: int
        :param _Name: 更改后的视频编码配置名，不填则不修改。
        :type Name: str
        :param _RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :type RemoveVideo: int
        :param _RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :type RemoveAudio: int
        :param _VideoSetting: 更改后的编码配置的视频设置。
        :type VideoSetting: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetVideoSettingForUpdate`
        :param _AudioSetting: 更改后的编码配置的音频设置。
        :type AudioSetting: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetAudioSettingForUpdate`
        """
        self._Platform = None
        self._Id = None
        self._Name = None
        self._RemoveVideo = None
        self._RemoveAudio = None
        self._VideoSetting = None
        self._AudioSetting = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Id(self):
        """配置 ID。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """更改后的视频编码配置名，不填则不修改。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RemoveVideo(self):
        """是否去除视频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :rtype: int
        """
        return self._RemoveVideo

    @RemoveVideo.setter
    def RemoveVideo(self, RemoveVideo):
        self._RemoveVideo = RemoveVideo

    @property
    def RemoveAudio(self):
        """是否去除音频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :rtype: int
        """
        return self._RemoveAudio

    @RemoveAudio.setter
    def RemoveAudio(self, RemoveAudio):
        self._RemoveAudio = RemoveAudio

    @property
    def VideoSetting(self):
        """更改后的编码配置的视频设置。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetVideoSettingForUpdate`
        """
        return self._VideoSetting

    @VideoSetting.setter
    def VideoSetting(self, VideoSetting):
        self._VideoSetting = VideoSetting

    @property
    def AudioSetting(self):
        """更改后的编码配置的音频设置。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetAudioSettingForUpdate`
        """
        return self._AudioSetting

    @AudioSetting.setter
    def AudioSetting(self, AudioSetting):
        self._AudioSetting = AudioSetting


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._RemoveVideo = params.get("RemoveVideo")
        self._RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoSetting") is not None:
            self._VideoSetting = VideoEncodingPresetVideoSettingForUpdate()
            self._VideoSetting._deserialize(params.get("VideoSetting"))
        if params.get("AudioSetting") is not None:
            self._AudioSetting = VideoEncodingPresetAudioSettingForUpdate()
            self._AudioSetting._deserialize(params.get("AudioSetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVideoEncodingPresetResponse(AbstractModel):
    """ModifyVideoEncodingPreset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MoveClassRequest(AbstractModel):
    """MoveClass请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _SourceClassPath: 源分类路径。
        :type SourceClassPath: str
        :param _DestinationClassPath: 目标分类路径。
        :type DestinationClassPath: str
        :param _Operator: 操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :type Operator: str
        """
        self._Platform = None
        self._Owner = None
        self._SourceClassPath = None
        self._DestinationClassPath = None
        self._Operator = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Owner(self):
        """归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def SourceClassPath(self):
        """源分类路径。
        :rtype: str
        """
        return self._SourceClassPath

    @SourceClassPath.setter
    def SourceClassPath(self, SourceClassPath):
        self._SourceClassPath = SourceClassPath

    @property
    def DestinationClassPath(self):
        """目标分类路径。
        :rtype: str
        """
        return self._DestinationClassPath

    @DestinationClassPath.setter
    def DestinationClassPath(self, DestinationClassPath):
        self._DestinationClassPath = DestinationClassPath

    @property
    def Operator(self):
        """操作者。填写用户的 Id，用于标识调用者及校验操作权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._SourceClassPath = params.get("SourceClassPath")
        self._DestinationClassPath = params.get("DestinationClassPath")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveClassResponse(AbstractModel):
    """MoveClass返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MoveResourceRequest(AbstractModel):
    """MoveResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _SourceResource: 待移动的原始资源信息，包含原始媒体或分类资源，以及资源归属。
        :type SourceResource: :class:`tencentcloud.cme.v20191029.models.ResourceInfo`
        :param _DestinationResource: 目标信息，包含分类及归属，仅支持移动资源到分类。
        :type DestinationResource: :class:`tencentcloud.cme.v20191029.models.ResourceInfo`
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以移动任务资源。如果指定操作者，则操作者必须对源及目标资源有写权限。
        :type Operator: str
        """
        self._Platform = None
        self._SourceResource = None
        self._DestinationResource = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SourceResource(self):
        """待移动的原始资源信息，包含原始媒体或分类资源，以及资源归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ResourceInfo`
        """
        return self._SourceResource

    @SourceResource.setter
    def SourceResource(self, SourceResource):
        self._SourceResource = SourceResource

    @property
    def DestinationResource(self):
        """目标信息，包含分类及归属，仅支持移动资源到分类。
        :rtype: :class:`tencentcloud.cme.v20191029.models.ResourceInfo`
        """
        return self._DestinationResource

    @DestinationResource.setter
    def DestinationResource(self, DestinationResource):
        self._DestinationResource = DestinationResource

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以移动任务资源。如果指定操作者，则操作者必须对源及目标资源有写权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("SourceResource") is not None:
            self._SourceResource = ResourceInfo()
            self._SourceResource._deserialize(params.get("SourceResource"))
        if params.get("DestinationResource") is not None:
            self._DestinationResource = ResourceInfo()
            self._DestinationResource._deserialize(params.get("DestinationResource"))
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveResourceResponse(AbstractModel):
    """MoveResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OtherMaterial(AbstractModel):
    """其他类型素材

    """

    def __init__(self):
        r"""
        :param _MaterialUrl: 素材媒体文件的播放 URL 地址。
        :type MaterialUrl: str
        :param _VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        """
        self._MaterialUrl = None
        self._VodFileId = None

    @property
    def MaterialUrl(self):
        """素材媒体文件的播放 URL 地址。
        :rtype: str
        """
        return self._MaterialUrl

    @MaterialUrl.setter
    def MaterialUrl(self, MaterialUrl):
        self._MaterialUrl = MaterialUrl

    @property
    def VodFileId(self):
        """云点播媒资 FileId。
        :rtype: str
        """
        return self._VodFileId

    @VodFileId.setter
    def VodFileId(self, VodFileId):
        self._VodFileId = VodFileId


    def _deserialize(self, params):
        self._MaterialUrl = params.get("MaterialUrl")
        self._VodFileId = params.get("VodFileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseEventRequest(AbstractModel):
    """ParseEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台名称，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _EventContent: 回调事件内容。
        :type EventContent: str
        """
        self._Platform = None
        self._EventContent = None

    @property
    def Platform(self):
        """平台名称，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def EventContent(self):
        """回调事件内容。
        :rtype: str
        """
        return self._EventContent

    @EventContent.setter
    def EventContent(self, EventContent):
        self._EventContent = EventContent


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._EventContent = params.get("EventContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseEventResponse(AbstractModel):
    """ParseEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventContent: 事件内容。
        :type EventContent: :class:`tencentcloud.cme.v20191029.models.EventContent`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventContent = None
        self._RequestId = None

    @property
    def EventContent(self):
        """事件内容。
        :rtype: :class:`tencentcloud.cme.v20191029.models.EventContent`
        """
        return self._EventContent

    @EventContent.setter
    def EventContent(self, EventContent):
        self._EventContent = EventContent

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EventContent") is not None:
            self._EventContent = EventContent()
            self._EventContent._deserialize(params.get("EventContent"))
        self._RequestId = params.get("RequestId")


class PenguinMediaPlatformPublishInfo(AbstractModel):
    """企鹅号发布信息。

    """

    def __init__(self):
        r"""
        :param _Title: 视频发布标题。
        :type Title: str
        :param _Description: 视频发布描述信息。
        :type Description: str
        :param _Tags: 视频标签。
        :type Tags: list of str
        :param _Category: 视频分类，详见[企鹅号官网](https://open.om.qq.com/resources/resourcesCenter)视频分类。
        :type Category: int
        """
        self._Title = None
        self._Description = None
        self._Tags = None
        self._Category = None

    @property
    def Title(self):
        """视频发布标题。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Description(self):
        """视频发布描述信息。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        """视频标签。
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Category(self):
        """视频分类，详见[企鹅号官网](https://open.om.qq.com/resources/resourcesCenter)视频分类。
        :rtype: int
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlatformInfo(AbstractModel):
    """平台信息。

    """

    def __init__(self):
        r"""
        :param _Platform: 平台标识。
        :type Platform: str
        :param _Description: 平台描述。
        :type Description: str
        :param _VodSubAppId: 云点播子应用 Id。
        :type VodSubAppId: int
        :param _LicenseId: 平台绑定的 license Id。
        :type LicenseId: str
        :param _Status: 平台状态，可取值为：
<li>Normal：正常，可使用。；</li>
<li>Stopped：已停用，暂无法使用；</li>
<li>Expired：已过期，需要重新购买会员包。</li>
        :type Status: str
        :param _CreateTime: 创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        :param _UpdateTime: 更新时间，格式按照 ISO 8601 标准表示。
        :type UpdateTime: str
        """
        self._Platform = None
        self._Description = None
        self._VodSubAppId = None
        self._LicenseId = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Platform(self):
        """平台标识。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Description(self):
        """平台描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VodSubAppId(self):
        """云点播子应用 Id。
        :rtype: int
        """
        return self._VodSubAppId

    @VodSubAppId.setter
    def VodSubAppId(self, VodSubAppId):
        self._VodSubAppId = VodSubAppId

    @property
    def LicenseId(self):
        """平台绑定的 license Id。
        :rtype: str
        """
        return self._LicenseId

    @LicenseId.setter
    def LicenseId(self, LicenseId):
        self._LicenseId = LicenseId

    @property
    def Status(self):
        """平台状态，可取值为：
<li>Normal：正常，可使用。；</li>
<li>Stopped：已停用，暂无法使用；</li>
<li>Expired：已过期，需要重新购买会员包。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间，格式按照 ISO 8601 标准表示。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间，格式按照 ISO 8601 标准表示。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Description = params.get("Description")
        self._VodSubAppId = params.get("VodSubAppId")
        self._LicenseId = params.get("LicenseId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PresetTagInfo(AbstractModel):
    """预置标签信息

    """

    def __init__(self):
        r"""
        :param _Id: 标签 Id 。
        :type Id: str
        :param _Name: 标签名称。
        :type Name: str
        :param _ParentTagId: 父级预设 Id。
        :type ParentTagId: str
        """
        self._Id = None
        self._Name = None
        self._ParentTagId = None

    @property
    def Id(self):
        """标签 Id 。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """标签名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentTagId(self):
        """父级预设 Id。
        :rtype: str
        """
        return self._ParentTagId

    @ParentTagId.setter
    def ParentTagId(self, ParentTagId):
        self._ParentTagId = ParentTagId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ParentTagId = params.get("ParentTagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    """项目信息。

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 Id。
        :type ProjectId: str
        :param _Name: 项目名称。
        :type Name: str
        :param _AspectRatio: 画布宽高比。
        :type AspectRatio: str
        :param _Category: 项目类别，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
<li>SWITCHER：导播台。</li>
<li>VIDEO_SEGMENTATION：视频拆条。</li>
<li>STREAM_CONNECT：云转推。</li>
<li>RECORD_REPLAY：录制回放。</li>
        :type Category: str
        :param _Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _CoverUrl: 项目封面图片地址。
        :type CoverUrl: str
        :param _StreamConnectProjectInfo: 云转推项目信息，仅当项目类别取值 STREAM_CONNECT 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamConnectProjectInfo: :class:`tencentcloud.cme.v20191029.models.StreamConnectProjectInfo`
        :param _MediaCastProjectInfo: 点播转直播项目信息，仅当项目类别取值为 MEDIA_CAST 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaCastProjectInfo: :class:`tencentcloud.cme.v20191029.models.MediaCastProjectInfo`
        :param _UpdateTime: 项目更新时间，格式按照 ISO 8601 标准表示。
        :type UpdateTime: str
        :param _CreateTime: 项目创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        """
        self._ProjectId = None
        self._Name = None
        self._AspectRatio = None
        self._Category = None
        self._Owner = None
        self._CoverUrl = None
        self._StreamConnectProjectInfo = None
        self._MediaCastProjectInfo = None
        self._UpdateTime = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        """项目 Id。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        """项目名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AspectRatio(self):
        """画布宽高比。
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def Category(self):
        """项目类别，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
<li>SWITCHER：导播台。</li>
<li>VIDEO_SEGMENTATION：视频拆条。</li>
<li>STREAM_CONNECT：云转推。</li>
<li>RECORD_REPLAY：录制回放。</li>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Owner(self):
        """归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def CoverUrl(self):
        """项目封面图片地址。
        :rtype: str
        """
        return self._CoverUrl

    @CoverUrl.setter
    def CoverUrl(self, CoverUrl):
        self._CoverUrl = CoverUrl

    @property
    def StreamConnectProjectInfo(self):
        """云转推项目信息，仅当项目类别取值 STREAM_CONNECT 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamConnectProjectInfo`
        """
        return self._StreamConnectProjectInfo

    @StreamConnectProjectInfo.setter
    def StreamConnectProjectInfo(self, StreamConnectProjectInfo):
        self._StreamConnectProjectInfo = StreamConnectProjectInfo

    @property
    def MediaCastProjectInfo(self):
        """点播转直播项目信息，仅当项目类别取值为 MEDIA_CAST 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastProjectInfo`
        """
        return self._MediaCastProjectInfo

    @MediaCastProjectInfo.setter
    def MediaCastProjectInfo(self, MediaCastProjectInfo):
        self._MediaCastProjectInfo = MediaCastProjectInfo

    @property
    def UpdateTime(self):
        """项目更新时间，格式按照 ISO 8601 标准表示。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        """项目创建时间，格式按照 ISO 8601 标准表示。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._AspectRatio = params.get("AspectRatio")
        self._Category = params.get("Category")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._CoverUrl = params.get("CoverUrl")
        if params.get("StreamConnectProjectInfo") is not None:
            self._StreamConnectProjectInfo = StreamConnectProjectInfo()
            self._StreamConnectProjectInfo._deserialize(params.get("StreamConnectProjectInfo"))
        if params.get("MediaCastProjectInfo") is not None:
            self._MediaCastProjectInfo = MediaCastProjectInfo()
            self._MediaCastProjectInfo._deserialize(params.get("MediaCastProjectInfo"))
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectMediaCastStatusChangedEvent(AbstractModel):
    """点播转直播项目状态变更事件。

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 Id。
        :type ProjectId: str
        :param _Status: 项目状态，取值有：
<li>Started：点播转直播开始；</li>
<li>Stopped：点播转直播结束；</li>
<li>SourceInterrupted：点播转直播输入断流；</li>
<li>DestinationInterrupted：点播转直播输出断流。</li>
        :type Status: str
        :param _SourceInterruptInfo: 点播转直播输入断流信息，仅当 Status 取值 SourceInterrupted 时有效。
        :type SourceInterruptInfo: :class:`tencentcloud.cme.v20191029.models.MediaCastSourceInterruptInfo`
        :param _DestinationInterruptInfo: 点播转直播输出断流信息，仅当 Status 取值 DestinationInterrupted 时有效。
        :type DestinationInterruptInfo: :class:`tencentcloud.cme.v20191029.models.MediaCastDestinationInterruptInfo`
        """
        self._ProjectId = None
        self._Status = None
        self._SourceInterruptInfo = None
        self._DestinationInterruptInfo = None

    @property
    def ProjectId(self):
        """项目 Id。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        """项目状态，取值有：
<li>Started：点播转直播开始；</li>
<li>Stopped：点播转直播结束；</li>
<li>SourceInterrupted：点播转直播输入断流；</li>
<li>DestinationInterrupted：点播转直播输出断流。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceInterruptInfo(self):
        """点播转直播输入断流信息，仅当 Status 取值 SourceInterrupted 时有效。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastSourceInterruptInfo`
        """
        return self._SourceInterruptInfo

    @SourceInterruptInfo.setter
    def SourceInterruptInfo(self, SourceInterruptInfo):
        self._SourceInterruptInfo = SourceInterruptInfo

    @property
    def DestinationInterruptInfo(self):
        """点播转直播输出断流信息，仅当 Status 取值 DestinationInterrupted 时有效。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaCastDestinationInterruptInfo`
        """
        return self._DestinationInterruptInfo

    @DestinationInterruptInfo.setter
    def DestinationInterruptInfo(self, DestinationInterruptInfo):
        self._DestinationInterruptInfo = DestinationInterruptInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        if params.get("SourceInterruptInfo") is not None:
            self._SourceInterruptInfo = MediaCastSourceInterruptInfo()
            self._SourceInterruptInfo._deserialize(params.get("SourceInterruptInfo"))
        if params.get("DestinationInterruptInfo") is not None:
            self._DestinationInterruptInfo = MediaCastDestinationInterruptInfo()
            self._DestinationInterruptInfo._deserialize(params.get("DestinationInterruptInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectStreamConnectStatusChangedEvent(AbstractModel):
    """云转推项目状态变更事件。

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 Id。
        :type ProjectId: str
        :param _Status: 项目状态，取值有：
<li>Working：云转推推流开始；</li>
<li>Stopped：云转推推流结束；</li>
<li>InputInterrupted：云转推输入断流；</li>
<li>OutputInterrupted：云转推输出断流。</li>
        :type Status: str
        :param _InputInterruptInfo: 云转推输入断流信息，仅当 Status 取值 InputInterrupted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInterruptInfo: :class:`tencentcloud.cme.v20191029.models.StreamConnectInputInterruptInfo`
        :param _OutputInterruptInfo: 云转推输出断流信息，仅当 Status 取值 OutputInterrupted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputInterruptInfo: :class:`tencentcloud.cme.v20191029.models.StreamConnectOutputInterruptInfo`
        """
        self._ProjectId = None
        self._Status = None
        self._InputInterruptInfo = None
        self._OutputInterruptInfo = None

    @property
    def ProjectId(self):
        """项目 Id。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        """项目状态，取值有：
<li>Working：云转推推流开始；</li>
<li>Stopped：云转推推流结束；</li>
<li>InputInterrupted：云转推输入断流；</li>
<li>OutputInterrupted：云转推输出断流。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InputInterruptInfo(self):
        """云转推输入断流信息，仅当 Status 取值 InputInterrupted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamConnectInputInterruptInfo`
        """
        return self._InputInterruptInfo

    @InputInterruptInfo.setter
    def InputInterruptInfo(self, InputInterruptInfo):
        self._InputInterruptInfo = InputInterruptInfo

    @property
    def OutputInterruptInfo(self):
        """云转推输出断流信息，仅当 Status 取值 OutputInterrupted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamConnectOutputInterruptInfo`
        """
        return self._OutputInterruptInfo

    @OutputInterruptInfo.setter
    def OutputInterruptInfo(self, OutputInterruptInfo):
        self._OutputInterruptInfo = OutputInterruptInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        if params.get("InputInterruptInfo") is not None:
            self._InputInterruptInfo = StreamConnectInputInterruptInfo()
            self._InputInterruptInfo._deserialize(params.get("InputInterruptInfo"))
        if params.get("OutputInterruptInfo") is not None:
            self._OutputInterruptInfo = StreamConnectOutputInterruptInfo()
            self._OutputInterruptInfo._deserialize(params.get("OutputInterruptInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectSwitcherStatusChangedEvent(AbstractModel):
    """导播台项目状态变更事件

    """

    def __init__(self):
        r"""
        :param _ProjectId: 导播台项目 Id。
        :type ProjectId: str
        :param _Status: 导播台项目状态，可取值有：
<li>Started：导播台启动；</li>
<li>Stopped：导播台停止；</li>
<li>PvwStarted：导播台 PVW 开启；</li>
<li>PgmStarted：导播台 PGM 开启，输出推流开始；</li>
<li>PvwStopped：导播台 PVW 停止；</li>
<li>PgmStopped：导播台 PGM 停止，输出推流结束。</li>
        :type Status: str
        """
        self._ProjectId = None
        self._Status = None

    @property
    def ProjectId(self):
        """导播台项目 Id。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        """导播台项目状态，可取值有：
<li>Started：导播台启动；</li>
<li>Stopped：导播台停止；</li>
<li>PvwStarted：导播台 PVW 开启；</li>
<li>PgmStarted：导播台 PGM 开启，输出推流开始；</li>
<li>PvwStopped：导播台 PVW 停止；</li>
<li>PgmStopped：导播台 PGM 停止，输出推流结束。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordReplayProjectInput(AbstractModel):
    """录制回放项目输入信息。

    """

    def __init__(self):
        r"""
        :param _PullStreamUrl: 录制拉流地址。
        :type PullStreamUrl: str
        :param _MaterialOwner: 录制文件归属者。
        :type MaterialOwner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _MaterialClassPath: 录制文件存储分类路径。
        :type MaterialClassPath: str
        :param _PushStreamUrl: 回放推流地址。
        :type PushStreamUrl: str
        """
        self._PullStreamUrl = None
        self._MaterialOwner = None
        self._MaterialClassPath = None
        self._PushStreamUrl = None

    @property
    def PullStreamUrl(self):
        """录制拉流地址。
        :rtype: str
        """
        return self._PullStreamUrl

    @PullStreamUrl.setter
    def PullStreamUrl(self, PullStreamUrl):
        self._PullStreamUrl = PullStreamUrl

    @property
    def MaterialOwner(self):
        """录制文件归属者。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._MaterialOwner

    @MaterialOwner.setter
    def MaterialOwner(self, MaterialOwner):
        self._MaterialOwner = MaterialOwner

    @property
    def MaterialClassPath(self):
        """录制文件存储分类路径。
        :rtype: str
        """
        return self._MaterialClassPath

    @MaterialClassPath.setter
    def MaterialClassPath(self, MaterialClassPath):
        self._MaterialClassPath = MaterialClassPath

    @property
    def PushStreamUrl(self):
        """回放推流地址。
        :rtype: str
        """
        return self._PushStreamUrl

    @PushStreamUrl.setter
    def PushStreamUrl(self, PushStreamUrl):
        self._PushStreamUrl = PushStreamUrl


    def _deserialize(self, params):
        self._PullStreamUrl = params.get("PullStreamUrl")
        if params.get("MaterialOwner") is not None:
            self._MaterialOwner = Entity()
            self._MaterialOwner._deserialize(params.get("MaterialOwner"))
        self._MaterialClassPath = params.get("MaterialClassPath")
        self._PushStreamUrl = params.get("PushStreamUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resource(AbstractModel):
    """用于描述资源

    """

    def __init__(self):
        r"""
        :param _Type: 类型，取值有：
<li>MATERIAL：素材。</li>
<li>CLASS：分类。</li>
        :type Type: str
        :param _Id: 资源 Id，当 Type 为 MATERIAL 时，取值为素材 Id；当 Type 为 CLASS 时，取值为分类路径 ClassPath。
        :type Id: str
        """
        self._Type = None
        self._Id = None

    @property
    def Type(self):
        """类型，取值有：
<li>MATERIAL：素材。</li>
<li>CLASS：分类。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Id(self):
        """资源 Id，当 Type 为 MATERIAL 时，取值为素材 Id；当 Type 为 CLASS 时，取值为分类路径 ClassPath。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceInfo(AbstractModel):
    """资源信息，包含资源以及归属信息

    """

    def __init__(self):
        r"""
        :param _Resource: 媒资和分类资源。
        :type Resource: :class:`tencentcloud.cme.v20191029.models.Resource`
        :param _Owner: 资源归属，个人或团队。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        self._Resource = None
        self._Owner = None

    @property
    def Resource(self):
        """媒资和分类资源。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Resource`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Owner(self):
        """资源归属，个人或团队。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner


    def _deserialize(self, params):
        if params.get("Resource") is not None:
            self._Resource = Resource()
            self._Resource._deserialize(params.get("Resource"))
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeResourceAuthorizationRequest(AbstractModel):
    """RevokeResourceAuthorization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _Owner: 资源所属实体。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _Resources: 被授权资源。
        :type Resources: list of Resource
        :param _Authorizees: 被授权目标实体。
        :type Authorizees: list of Entity
        :param _Permissions: 详细授权值。 取值有：
<li>R：可读，可以浏览素材，但不能使用该素材（将其添加到 Project），或复制到自己的媒资库中</li>
<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>
<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>
<li>W：可修改、删除媒资。</li>
        :type Permissions: list of str
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，撤销任意资源的授权权限。如果指定操作者，则操作者必须对被授权资源有写权限。
        :type Operator: str
        """
        self._Platform = None
        self._Owner = None
        self._Resources = None
        self._Authorizees = None
        self._Permissions = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Owner(self):
        """资源所属实体。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Resources(self):
        """被授权资源。
        :rtype: list of Resource
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Authorizees(self):
        """被授权目标实体。
        :rtype: list of Entity
        """
        return self._Authorizees

    @Authorizees.setter
    def Authorizees(self, Authorizees):
        self._Authorizees = Authorizees

    @property
    def Permissions(self):
        """详细授权值。 取值有：
<li>R：可读，可以浏览素材，但不能使用该素材（将其添加到 Project），或复制到自己的媒资库中</li>
<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>
<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>
<li>W：可修改、删除媒资。</li>
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，撤销任意资源的授权权限。如果指定操作者，则操作者必须对被授权资源有写权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self._Resources.append(obj)
        if params.get("Authorizees") is not None:
            self._Authorizees = []
            for item in params.get("Authorizees"):
                obj = Entity()
                obj._deserialize(item)
                self._Authorizees.append(obj)
        self._Permissions = params.get("Permissions")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeResourceAuthorizationResponse(AbstractModel):
    """RevokeResourceAuthorization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RtmpPushInputInfo(AbstractModel):
    """直播推流信息，包括推流地址有效时长，多媒体创作引擎后端生成直播推流地址。

    """

    def __init__(self):
        r"""
        :param _ExpiredSecond: 直播推流地址有效期，单位：秒 。
        :type ExpiredSecond: int
        :param _PushUrl: 直播推流地址，入参不填默认由多媒体创作引擎生成。
        :type PushUrl: str
        """
        self._ExpiredSecond = None
        self._PushUrl = None

    @property
    def ExpiredSecond(self):
        """直播推流地址有效期，单位：秒 。
        :rtype: int
        """
        return self._ExpiredSecond

    @ExpiredSecond.setter
    def ExpiredSecond(self, ExpiredSecond):
        self._ExpiredSecond = ExpiredSecond

    @property
    def PushUrl(self):
        """直播推流地址，入参不填默认由多媒体创作引擎生成。
        :rtype: str
        """
        return self._PushUrl

    @PushUrl.setter
    def PushUrl(self, PushUrl):
        self._PushUrl = PushUrl


    def _deserialize(self, params):
        self._ExpiredSecond = params.get("ExpiredSecond")
        self._PushUrl = params.get("PushUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchMaterialRequest(AbstractModel):
    """SearchMaterial请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :type Platform: str
        :param _SearchScopes: 指定搜索空间，数组长度不得超过5。
        :type SearchScopes: list of SearchScope
        :param _MaterialTypes: 媒体类型，可取值有：
<li>AUDIO：音频；</li>
<li>VIDEO：视频 ；</li>
<li>IMAGE：图片；</li>
<li>VIDEO_EDIT_TEMPLATE：剪辑模板。</li>
        :type MaterialTypes: list of str
        :param _Text: 搜索文本，模糊匹配媒体名称或描述信息，匹配项越多，匹配度越高，排序越优先。长度限制：15个字符。
        :type Text: str
        :param _Resolution: 按画质检索，取值为：LD/SD/HD/FHD/2K/4K。
        :type Resolution: str
        :param _DurationRange: 按媒体时长检索，单位s。
        :type DurationRange: :class:`tencentcloud.cme.v20191029.models.IntegerRange`
        :param _CreateTimeRange: 按照媒体创建时间检索。
        :type CreateTimeRange: :class:`tencentcloud.cme.v20191029.models.TimeRange`
        :param _Tags: 按标签检索，填入检索的标签名。
        :type Tags: list of str
        :param _Sort: 排序方式。Sort.Field 可选值：CreateTime。指定 Text 搜索时，将根据匹配度排序，该字段无效。
        :type Sort: :class:`tencentcloud.cme.v20191029.models.SortBy`
        :param _Offset: 偏移量。默认值：0。
        :type Offset: int
        :param _Limit: 返回记录条数，默认值：50。
        :type Limit: int
        :param _Operator: 操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以搜索任意媒体的信息。如果指定操作者，则操作者必须对媒体有读权限。
        :type Operator: str
        """
        self._Platform = None
        self._SearchScopes = None
        self._MaterialTypes = None
        self._Text = None
        self._Resolution = None
        self._DurationRange = None
        self._CreateTimeRange = None
        self._Tags = None
        self._Sort = None
        self._Offset = None
        self._Limit = None
        self._Operator = None

    @property
    def Platform(self):
        """平台 Id，指定访问的平台。关于平台概念，请参见文档 [平台](https://cloud.tencent.com/document/product/1156/43767)。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SearchScopes(self):
        """指定搜索空间，数组长度不得超过5。
        :rtype: list of SearchScope
        """
        return self._SearchScopes

    @SearchScopes.setter
    def SearchScopes(self, SearchScopes):
        self._SearchScopes = SearchScopes

    @property
    def MaterialTypes(self):
        """媒体类型，可取值有：
<li>AUDIO：音频；</li>
<li>VIDEO：视频 ；</li>
<li>IMAGE：图片；</li>
<li>VIDEO_EDIT_TEMPLATE：剪辑模板。</li>
        :rtype: list of str
        """
        return self._MaterialTypes

    @MaterialTypes.setter
    def MaterialTypes(self, MaterialTypes):
        self._MaterialTypes = MaterialTypes

    @property
    def Text(self):
        """搜索文本，模糊匹配媒体名称或描述信息，匹配项越多，匹配度越高，排序越优先。长度限制：15个字符。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Resolution(self):
        """按画质检索，取值为：LD/SD/HD/FHD/2K/4K。
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def DurationRange(self):
        """按媒体时长检索，单位s。
        :rtype: :class:`tencentcloud.cme.v20191029.models.IntegerRange`
        """
        return self._DurationRange

    @DurationRange.setter
    def DurationRange(self, DurationRange):
        self._DurationRange = DurationRange

    @property
    def CreateTimeRange(self):
        """按照媒体创建时间检索。
        :rtype: :class:`tencentcloud.cme.v20191029.models.TimeRange`
        """
        return self._CreateTimeRange

    @CreateTimeRange.setter
    def CreateTimeRange(self, CreateTimeRange):
        self._CreateTimeRange = CreateTimeRange

    @property
    def Tags(self):
        """按标签检索，填入检索的标签名。
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Sort(self):
        """排序方式。Sort.Field 可选值：CreateTime。指定 Text 搜索时，将根据匹配度排序，该字段无效。
        :rtype: :class:`tencentcloud.cme.v20191029.models.SortBy`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Offset(self):
        """偏移量。默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回记录条数，默认值：50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Operator(self):
        """操作者。如不填，默认为 `cmeid_system`，表示平台管理员操作，可以搜索任意媒体的信息。如果指定操作者，则操作者必须对媒体有读权限。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        if params.get("SearchScopes") is not None:
            self._SearchScopes = []
            for item in params.get("SearchScopes"):
                obj = SearchScope()
                obj._deserialize(item)
                self._SearchScopes.append(obj)
        self._MaterialTypes = params.get("MaterialTypes")
        self._Text = params.get("Text")
        self._Resolution = params.get("Resolution")
        if params.get("DurationRange") is not None:
            self._DurationRange = IntegerRange()
            self._DurationRange._deserialize(params.get("DurationRange"))
        if params.get("CreateTimeRange") is not None:
            self._CreateTimeRange = TimeRange()
            self._CreateTimeRange._deserialize(params.get("CreateTimeRange"))
        self._Tags = params.get("Tags")
        if params.get("Sort") is not None:
            self._Sort = SortBy()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchMaterialResponse(AbstractModel):
    """SearchMaterial返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合记录总条数。
        :type TotalCount: int
        :param _MaterialInfoSet: 媒体信息，仅返回基础信息。
        :type MaterialInfoSet: list of MaterialInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MaterialInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合记录总条数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MaterialInfoSet(self):
        """媒体信息，仅返回基础信息。
        :rtype: list of MaterialInfo
        """
        return self._MaterialInfoSet

    @MaterialInfoSet.setter
    def MaterialInfoSet(self, MaterialInfoSet):
        self._MaterialInfoSet = MaterialInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("MaterialInfoSet") is not None:
            self._MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self._MaterialInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class SearchScope(AbstractModel):
    """搜索空间

    """

    def __init__(self):
        r"""
        :param _Owner: 分类路径归属。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _ClassPath: 按分类路径检索。 不填则默认按根分类路径检索。
        :type ClassPath: str
        """
        self._Owner = None
        self._ClassPath = None

    @property
    def Owner(self):
        """分类路径归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def ClassPath(self):
        """按分类路径检索。 不填则默认按根分类路径检索。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._ClassPath = params.get("ClassPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlotInfo(AbstractModel):
    """卡槽信息。

    """

    def __init__(self):
        r"""
        :param _Id: 卡槽 Id。
        :type Id: int
        :param _Type: 卡槽类型，可取值有：
<li> AUDIO：音频卡槽，可替换素材类型为 AUDIO 的音频素材;</li>
<li> VIDEO：视频卡槽，可替换素材类型为 VIDEO 的视频素材;</li>
<li> IMAGE：图片卡槽，可替换素材类型为 IMAGE 的图片素材;</li>
<li> TEXT：文本卡槽，可替换文本内容。</li>
        :type Type: str
        :param _DefaultMaterialId: 默认素材ID。当卡槽类型为 AUDIO，VIDEO，或 IMAGE 中的一种时有效。
        :type DefaultMaterialId: str
        :param _DefaultTextSlotInfo: 默认文本卡槽信息。当卡槽类型为 TEXT 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultTextSlotInfo: :class:`tencentcloud.cme.v20191029.models.TextSlotInfo`
        :param _Duration: 素材时长，单位秒。
        :type Duration: float
        :param _StartTime: 卡槽起始时间，单位秒。
        :type StartTime: float
        """
        self._Id = None
        self._Type = None
        self._DefaultMaterialId = None
        self._DefaultTextSlotInfo = None
        self._Duration = None
        self._StartTime = None

    @property
    def Id(self):
        """卡槽 Id。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """卡槽类型，可取值有：
<li> AUDIO：音频卡槽，可替换素材类型为 AUDIO 的音频素材;</li>
<li> VIDEO：视频卡槽，可替换素材类型为 VIDEO 的视频素材;</li>
<li> IMAGE：图片卡槽，可替换素材类型为 IMAGE 的图片素材;</li>
<li> TEXT：文本卡槽，可替换文本内容。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DefaultMaterialId(self):
        """默认素材ID。当卡槽类型为 AUDIO，VIDEO，或 IMAGE 中的一种时有效。
        :rtype: str
        """
        return self._DefaultMaterialId

    @DefaultMaterialId.setter
    def DefaultMaterialId(self, DefaultMaterialId):
        self._DefaultMaterialId = DefaultMaterialId

    @property
    def DefaultTextSlotInfo(self):
        """默认文本卡槽信息。当卡槽类型为 TEXT 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.TextSlotInfo`
        """
        return self._DefaultTextSlotInfo

    @DefaultTextSlotInfo.setter
    def DefaultTextSlotInfo(self, DefaultTextSlotInfo):
        self._DefaultTextSlotInfo = DefaultTextSlotInfo

    @property
    def Duration(self):
        """素材时长，单位秒。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def StartTime(self):
        """卡槽起始时间，单位秒。
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._DefaultMaterialId = params.get("DefaultMaterialId")
        if params.get("DefaultTextSlotInfo") is not None:
            self._DefaultTextSlotInfo = TextSlotInfo()
            self._DefaultTextSlotInfo._deserialize(params.get("DefaultTextSlotInfo"))
        self._Duration = params.get("Duration")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlotReplacementInfo(AbstractModel):
    """卡槽替换信息。

    """

    def __init__(self):
        r"""
        :param _Id: 卡槽 Id。
        :type Id: int
        :param _ReplacementType: 替换类型，可取值有：
<li> AUDIO ：音频；</li>
<li> VIDEO ：视频；</li>
<li> IMAGE ：图片；</li>
<li> TEXT ：文本。</li>
注意：这里必须保证替换的素材类型与模板轨道数据的素材类型一致。如果替换的类型为Text,，则必须保证模板轨道数据中相应卡槽的位置标记的是文本。
        :type ReplacementType: str
        :param _MediaReplacementInfo: 媒体替换信息，仅当要替换的媒体类型为音频、视频、图片时有效。
        :type MediaReplacementInfo: :class:`tencentcloud.cme.v20191029.models.MediaReplacementInfo`
        :param _TextReplacementInfo: 文本替换信息，仅当要替换的卡槽类型为文本时有效。
        :type TextReplacementInfo: :class:`tencentcloud.cme.v20191029.models.TextReplacementInfo`
        """
        self._Id = None
        self._ReplacementType = None
        self._MediaReplacementInfo = None
        self._TextReplacementInfo = None

    @property
    def Id(self):
        """卡槽 Id。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ReplacementType(self):
        """替换类型，可取值有：
<li> AUDIO ：音频；</li>
<li> VIDEO ：视频；</li>
<li> IMAGE ：图片；</li>
<li> TEXT ：文本。</li>
注意：这里必须保证替换的素材类型与模板轨道数据的素材类型一致。如果替换的类型为Text,，则必须保证模板轨道数据中相应卡槽的位置标记的是文本。
        :rtype: str
        """
        return self._ReplacementType

    @ReplacementType.setter
    def ReplacementType(self, ReplacementType):
        self._ReplacementType = ReplacementType

    @property
    def MediaReplacementInfo(self):
        """媒体替换信息，仅当要替换的媒体类型为音频、视频、图片时有效。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaReplacementInfo`
        """
        return self._MediaReplacementInfo

    @MediaReplacementInfo.setter
    def MediaReplacementInfo(self, MediaReplacementInfo):
        self._MediaReplacementInfo = MediaReplacementInfo

    @property
    def TextReplacementInfo(self):
        """文本替换信息，仅当要替换的卡槽类型为文本时有效。
        :rtype: :class:`tencentcloud.cme.v20191029.models.TextReplacementInfo`
        """
        return self._TextReplacementInfo

    @TextReplacementInfo.setter
    def TextReplacementInfo(self, TextReplacementInfo):
        self._TextReplacementInfo = TextReplacementInfo


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ReplacementType = params.get("ReplacementType")
        if params.get("MediaReplacementInfo") is not None:
            self._MediaReplacementInfo = MediaReplacementInfo()
            self._MediaReplacementInfo._deserialize(params.get("MediaReplacementInfo"))
        if params.get("TextReplacementInfo") is not None:
            self._TextReplacementInfo = TextReplacementInfo()
            self._TextReplacementInfo._deserialize(params.get("TextReplacementInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortBy(AbstractModel):
    """排序

    """

    def __init__(self):
        r"""
        :param _Field: 排序字段。
        :type Field: str
        :param _Order: 排序方式，可选值：Asc（升序）、Desc（降序），默认降序。
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        """排序字段。
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        """排序方式，可选值：Asc（升序）、Desc（降序），默认降序。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageNewFileCreatedEvent(AbstractModel):
    """新文件生成事件

    """

    def __init__(self):
        r"""
        :param _FileId: 云点播文件  Id。
        :type FileId: str
        :param _MaterialId: 媒体 Id。
        :type MaterialId: str
        :param _Operator: 操作者 Id。（废弃，请勿使用）
        :type Operator: str
        :param _OperationType: 操作类型，可取值有：
<li>Upload：本地上传；</li>
<li>PullUpload：拉取上传；</li>
<li>VideoEdit：视频剪辑；</li>
<li>LiveStreamClip：直播流剪辑；</li>
<li>LiveStreamRecord：直播流录制。</li>
        :type OperationType: str
        :param _Owner: 媒体归属。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param _ClassPath: 媒体分类路径。
        :type ClassPath: str
        :param _TaskId: 生成文件的任务 Id。当生成新文件是拉取上传、视频剪辑、直播流剪辑时为任务 Id。
        :type TaskId: str
        :param _SourceContext: 来源上下文信息。视频剪辑生成新文件时此字段为项目 Id；直播流剪辑或者直播流录制生成新文件则为原始流地址。
        :type SourceContext: str
        """
        self._FileId = None
        self._MaterialId = None
        self._Operator = None
        self._OperationType = None
        self._Owner = None
        self._ClassPath = None
        self._TaskId = None
        self._SourceContext = None

    @property
    def FileId(self):
        """云点播文件  Id。
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def MaterialId(self):
        """媒体 Id。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        """操作者 Id。（废弃，请勿使用）
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def OperationType(self):
        """操作类型，可取值有：
<li>Upload：本地上传；</li>
<li>PullUpload：拉取上传；</li>
<li>VideoEdit：视频剪辑；</li>
<li>LiveStreamClip：直播流剪辑；</li>
<li>LiveStreamRecord：直播流录制。</li>
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def Owner(self):
        """媒体归属。
        :rtype: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def ClassPath(self):
        """媒体分类路径。
        :rtype: str
        """
        return self._ClassPath

    @ClassPath.setter
    def ClassPath(self, ClassPath):
        self._ClassPath = ClassPath

    @property
    def TaskId(self):
        """生成文件的任务 Id。当生成新文件是拉取上传、视频剪辑、直播流剪辑时为任务 Id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SourceContext(self):
        """来源上下文信息。视频剪辑生成新文件时此字段为项目 Id；直播流剪辑或者直播流录制生成新文件则为原始流地址。
        :rtype: str
        """
        return self._SourceContext

    @SourceContext.setter
    def SourceContext(self, SourceContext):
        self._SourceContext = SourceContext


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._MaterialId = params.get("MaterialId")
        self._Operator = params.get("Operator")
        self._OperationType = params.get("OperationType")
        if params.get("Owner") is not None:
            self._Owner = Entity()
            self._Owner._deserialize(params.get("Owner"))
        self._ClassPath = params.get("ClassPath")
        self._TaskId = params.get("TaskId")
        self._SourceContext = params.get("SourceContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamConnectInputInterruptInfo(AbstractModel):
    """云转推输入断流信息。

    """

    def __init__(self):
        r"""
        :param _EndPoint: 云转推输入源标识，取值有：
<li>Main：主源；</li>
<li>Backup：备源。</li>
        :type EndPoint: str
        """
        self._EndPoint = None

    @property
    def EndPoint(self):
        """云转推输入源标识，取值有：
<li>Main：主源；</li>
<li>Backup：备源。</li>
        :rtype: str
        """
        return self._EndPoint

    @EndPoint.setter
    def EndPoint(self, EndPoint):
        self._EndPoint = EndPoint


    def _deserialize(self, params):
        self._EndPoint = params.get("EndPoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamConnectOutput(AbstractModel):
    """云转推输出源。

    """

    def __init__(self):
        r"""
        :param _Id: 云转推输出源标识，转推项目级别唯一。若不填则由后端生成。
        :type Id: str
        :param _Name: 云转推输出源名称。
        :type Name: str
        :param _Type: 云转推输出源类型，取值：
<li>URL ：URL类型</li>
不填默认为URL类型。
        :type Type: str
        :param _PushUrl: 云转推推流地址。
        :type PushUrl: str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._PushUrl = None

    @property
    def Id(self):
        """云转推输出源标识，转推项目级别唯一。若不填则由后端生成。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """云转推输出源名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """云转推输出源类型，取值：
<li>URL ：URL类型</li>
不填默认为URL类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PushUrl(self):
        """云转推推流地址。
        :rtype: str
        """
        return self._PushUrl

    @PushUrl.setter
    def PushUrl(self, PushUrl):
        self._PushUrl = PushUrl


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._PushUrl = params.get("PushUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamConnectOutputInfo(AbstractModel):
    """云转推输出源信息，包含输出源和输出源转推状态。

    """

    def __init__(self):
        r"""
        :param _StreamConnectOutput: 输出源。
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamConnectOutput: :class:`tencentcloud.cme.v20191029.models.StreamConnectOutput`
        :param _PushSwitch: 输出流状态：
<li>On ：开；</li>
<li>Off ：关 。</li>
        :type PushSwitch: str
        """
        self._StreamConnectOutput = None
        self._PushSwitch = None

    @property
    def StreamConnectOutput(self):
        """输出源。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamConnectOutput`
        """
        return self._StreamConnectOutput

    @StreamConnectOutput.setter
    def StreamConnectOutput(self, StreamConnectOutput):
        self._StreamConnectOutput = StreamConnectOutput

    @property
    def PushSwitch(self):
        """输出流状态：
<li>On ：开；</li>
<li>Off ：关 。</li>
        :rtype: str
        """
        return self._PushSwitch

    @PushSwitch.setter
    def PushSwitch(self, PushSwitch):
        self._PushSwitch = PushSwitch


    def _deserialize(self, params):
        if params.get("StreamConnectOutput") is not None:
            self._StreamConnectOutput = StreamConnectOutput()
            self._StreamConnectOutput._deserialize(params.get("StreamConnectOutput"))
        self._PushSwitch = params.get("PushSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamConnectOutputInterruptInfo(AbstractModel):
    """云转推输出断流信息

    """

    def __init__(self):
        r"""
        :param _Id: 云转推输出标识。
        :type Id: str
        :param _Name: 云转推输出名称。
        :type Name: str
        :param _Url: 云转推输出地址。
        :type Url: str
        """
        self._Id = None
        self._Name = None
        self._Url = None

    @property
    def Id(self):
        """云转推输出标识。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """云转推输出名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Url(self):
        """云转推输出地址。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamConnectProjectInfo(AbstractModel):
    """云转推项目信息，包含输入源、输出源、当前转推开始时间等信息。

    """

    def __init__(self):
        r"""
        :param _Status: 转推项目状态，取值有：
<li>Working ：转推中；</li>
<li>Idle ：空闲中。</li>
        :type Status: str
        :param _CurrentInputEndpoint: 当前转推输入源，取值有：
<li>Main ：主输入源；</li>
<li>Backup ：备输入源。</li>
        :type CurrentInputEndpoint: str
        :param _CurrentStartTime: 当前转推开始时间， 采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。仅 Status 取值 Working 时有效。
        :type CurrentStartTime: str
        :param _CurrentStopTime: 当前转推计划结束时间， 采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。仅 Status 取值 Working 时有效。
        :type CurrentStopTime: str
        :param _LastStopTime: 上一次转推结束时间， 采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。仅 Status 取值 Idle 时有效。
        :type LastStopTime: str
        :param _MainInput: 云转推主输入源。
注意：此字段可能返回 null，表示取不到有效值。
        :type MainInput: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        :param _BackupInput: 云转推备输入源。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupInput: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        :param _OutputSet: 云转推输出源。
        :type OutputSet: list of StreamConnectOutputInfo
        """
        self._Status = None
        self._CurrentInputEndpoint = None
        self._CurrentStartTime = None
        self._CurrentStopTime = None
        self._LastStopTime = None
        self._MainInput = None
        self._BackupInput = None
        self._OutputSet = None

    @property
    def Status(self):
        """转推项目状态，取值有：
<li>Working ：转推中；</li>
<li>Idle ：空闲中。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CurrentInputEndpoint(self):
        """当前转推输入源，取值有：
<li>Main ：主输入源；</li>
<li>Backup ：备输入源。</li>
        :rtype: str
        """
        return self._CurrentInputEndpoint

    @CurrentInputEndpoint.setter
    def CurrentInputEndpoint(self, CurrentInputEndpoint):
        self._CurrentInputEndpoint = CurrentInputEndpoint

    @property
    def CurrentStartTime(self):
        """当前转推开始时间， 采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。仅 Status 取值 Working 时有效。
        :rtype: str
        """
        return self._CurrentStartTime

    @CurrentStartTime.setter
    def CurrentStartTime(self, CurrentStartTime):
        self._CurrentStartTime = CurrentStartTime

    @property
    def CurrentStopTime(self):
        """当前转推计划结束时间， 采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。仅 Status 取值 Working 时有效。
        :rtype: str
        """
        return self._CurrentStopTime

    @CurrentStopTime.setter
    def CurrentStopTime(self, CurrentStopTime):
        self._CurrentStopTime = CurrentStopTime

    @property
    def LastStopTime(self):
        """上一次转推结束时间， 采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。仅 Status 取值 Idle 时有效。
        :rtype: str
        """
        return self._LastStopTime

    @LastStopTime.setter
    def LastStopTime(self, LastStopTime):
        self._LastStopTime = LastStopTime

    @property
    def MainInput(self):
        """云转推主输入源。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        """
        return self._MainInput

    @MainInput.setter
    def MainInput(self, MainInput):
        self._MainInput = MainInput

    @property
    def BackupInput(self):
        """云转推备输入源。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        """
        return self._BackupInput

    @BackupInput.setter
    def BackupInput(self, BackupInput):
        self._BackupInput = BackupInput

    @property
    def OutputSet(self):
        """云转推输出源。
        :rtype: list of StreamConnectOutputInfo
        """
        return self._OutputSet

    @OutputSet.setter
    def OutputSet(self, OutputSet):
        self._OutputSet = OutputSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._CurrentInputEndpoint = params.get("CurrentInputEndpoint")
        self._CurrentStartTime = params.get("CurrentStartTime")
        self._CurrentStopTime = params.get("CurrentStopTime")
        self._LastStopTime = params.get("LastStopTime")
        if params.get("MainInput") is not None:
            self._MainInput = StreamInputInfo()
            self._MainInput._deserialize(params.get("MainInput"))
        if params.get("BackupInput") is not None:
            self._BackupInput = StreamInputInfo()
            self._BackupInput._deserialize(params.get("BackupInput"))
        if params.get("OutputSet") is not None:
            self._OutputSet = []
            for item in params.get("OutputSet"):
                obj = StreamConnectOutputInfo()
                obj._deserialize(item)
                self._OutputSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamConnectProjectInput(AbstractModel):
    """云转推项目输入信息。

    """

    def __init__(self):
        r"""
        :param _MainInput: 云转推主输入源信息。
        :type MainInput: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        :param _BackupInput: 云转推备输入源信息。
        :type BackupInput: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        :param _Outputs: 云转推输出源信息。
        :type Outputs: list of StreamConnectOutput
        """
        self._MainInput = None
        self._BackupInput = None
        self._Outputs = None

    @property
    def MainInput(self):
        """云转推主输入源信息。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        """
        return self._MainInput

    @MainInput.setter
    def MainInput(self, MainInput):
        self._MainInput = MainInput

    @property
    def BackupInput(self):
        """云转推备输入源信息。
        :rtype: :class:`tencentcloud.cme.v20191029.models.StreamInputInfo`
        """
        return self._BackupInput

    @BackupInput.setter
    def BackupInput(self, BackupInput):
        self._BackupInput = BackupInput

    @property
    def Outputs(self):
        """云转推输出源信息。
        :rtype: list of StreamConnectOutput
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs


    def _deserialize(self, params):
        if params.get("MainInput") is not None:
            self._MainInput = StreamInputInfo()
            self._MainInput._deserialize(params.get("MainInput"))
        if params.get("BackupInput") is not None:
            self._BackupInput = StreamInputInfo()
            self._BackupInput._deserialize(params.get("BackupInput"))
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = StreamConnectOutput()
                obj._deserialize(item)
                self._Outputs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamInputInfo(AbstractModel):
    """输入流信息。

    """

    def __init__(self):
        r"""
        :param _InputType: 流输入类型，取值：
<li>VodPull ： 点播拉流；</li>
<li>LivePull ：直播拉流；</li>
<li>RtmpPush ： 直播推流。</li>
        :type InputType: str
        :param _VodPullInputInfo: 点播拉流信息，当 InputType = VodPull 时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type VodPullInputInfo: :class:`tencentcloud.cme.v20191029.models.VodPullInputInfo`
        :param _LivePullInputInfo: 直播拉流信息，当 InputType = LivePull  时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type LivePullInputInfo: :class:`tencentcloud.cme.v20191029.models.LivePullInputInfo`
        :param _RtmpPushInputInfo: 直播推流信息，当 InputType = RtmpPush 时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type RtmpPushInputInfo: :class:`tencentcloud.cme.v20191029.models.RtmpPushInputInfo`
        """
        self._InputType = None
        self._VodPullInputInfo = None
        self._LivePullInputInfo = None
        self._RtmpPushInputInfo = None

    @property
    def InputType(self):
        """流输入类型，取值：
<li>VodPull ： 点播拉流；</li>
<li>LivePull ：直播拉流；</li>
<li>RtmpPush ： 直播推流。</li>
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def VodPullInputInfo(self):
        """点播拉流信息，当 InputType = VodPull 时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VodPullInputInfo`
        """
        return self._VodPullInputInfo

    @VodPullInputInfo.setter
    def VodPullInputInfo(self, VodPullInputInfo):
        self._VodPullInputInfo = VodPullInputInfo

    @property
    def LivePullInputInfo(self):
        """直播拉流信息，当 InputType = LivePull  时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.LivePullInputInfo`
        """
        return self._LivePullInputInfo

    @LivePullInputInfo.setter
    def LivePullInputInfo(self, LivePullInputInfo):
        self._LivePullInputInfo = LivePullInputInfo

    @property
    def RtmpPushInputInfo(self):
        """直播推流信息，当 InputType = RtmpPush 时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.RtmpPushInputInfo`
        """
        return self._RtmpPushInputInfo

    @RtmpPushInputInfo.setter
    def RtmpPushInputInfo(self, RtmpPushInputInfo):
        self._RtmpPushInputInfo = RtmpPushInputInfo


    def _deserialize(self, params):
        self._InputType = params.get("InputType")
        if params.get("VodPullInputInfo") is not None:
            self._VodPullInputInfo = VodPullInputInfo()
            self._VodPullInputInfo._deserialize(params.get("VodPullInputInfo"))
        if params.get("LivePullInputInfo") is not None:
            self._LivePullInputInfo = LivePullInputInfo()
            self._LivePullInputInfo._deserialize(params.get("LivePullInputInfo"))
        if params.get("RtmpPushInputInfo") is not None:
            self._RtmpPushInputInfo = RtmpPushInputInfo()
            self._RtmpPushInputInfo._deserialize(params.get("RtmpPushInputInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitcherPgmOutputConfig(AbstractModel):
    """导播台主监输出配置信息

    """

    def __init__(self):
        r"""
        :param _TemplateId: 导播台输出模板 ID，可取值：
<li>10001：分辨率为1080 P；</li>
<li>10002：分辨率为720 P；</li>
<li>10003：分辨率为480 P。</li>
        :type TemplateId: int
        :param _Width: 导播台输出宽，单位：像素。
        :type Width: int
        :param _Height: 导播台输出高，单位：像素。
        :type Height: int
        :param _Fps: 导播台输出帧率，单位：帧/秒
        :type Fps: int
        :param _BitRate: 导播台输出码率， 单位：bit/s。
        :type BitRate: int
        """
        self._TemplateId = None
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None

    @property
    def TemplateId(self):
        """导播台输出模板 ID，可取值：
<li>10001：分辨率为1080 P；</li>
<li>10002：分辨率为720 P；</li>
<li>10003：分辨率为480 P。</li>
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Width(self):
        """导播台输出宽，单位：像素。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """导播台输出高，单位：像素。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        """导播台输出帧率，单位：帧/秒
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        """导播台输出码率， 单位：bit/s。
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitcherProjectInput(AbstractModel):
    """导播台项目输入信息

    """

    def __init__(self):
        r"""
        :param _StopTime: 导播台停止时间，格式按照 ISO 8601 标准表示。若不填，该值默认为当前时间加七天。
        :type StopTime: str
        :param _PgmOutputConfig: 导播台主监输出配置信息。若不填，默认输出 720P。
        :type PgmOutputConfig: :class:`tencentcloud.cme.v20191029.models.SwitcherPgmOutputConfig`
        """
        self._StopTime = None
        self._PgmOutputConfig = None

    @property
    def StopTime(self):
        """导播台停止时间，格式按照 ISO 8601 标准表示。若不填，该值默认为当前时间加七天。
        :rtype: str
        """
        return self._StopTime

    @StopTime.setter
    def StopTime(self, StopTime):
        self._StopTime = StopTime

    @property
    def PgmOutputConfig(self):
        """导播台主监输出配置信息。若不填，默认输出 720P。
        :rtype: :class:`tencentcloud.cme.v20191029.models.SwitcherPgmOutputConfig`
        """
        return self._PgmOutputConfig

    @PgmOutputConfig.setter
    def PgmOutputConfig(self, PgmOutputConfig):
        self._PgmOutputConfig = PgmOutputConfig


    def _deserialize(self, params):
        self._StopTime = params.get("StopTime")
        if params.get("PgmOutputConfig") is not None:
            self._PgmOutputConfig = SwitcherPgmOutputConfig()
            self._PgmOutputConfig._deserialize(params.get("PgmOutputConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskBaseInfo(AbstractModel):
    """任务基础信息。

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 Id。
        :type TaskId: str
        :param _TaskType: 任务类型，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：项目导出。</li>
        :type TaskType: str
        :param _Status: 任务状态，取值有：
<li>PROCESSING：处理中：</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :type Status: str
        :param _Progress: 任务进度，取值为：0~100。
        :type Progress: int
        :param _ErrCode: 错误码。
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param _ErrMsg: 错误信息。
        :type ErrMsg: str
        :param _CreateTime: 创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        """
        self._TaskId = None
        self._TaskType = None
        self._Status = None
        self._Progress = None
        self._ErrCode = None
        self._ErrMsg = None
        self._CreateTime = None

    @property
    def TaskId(self):
        """任务 Id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        """任务类型，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：项目导出。</li>
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Status(self):
        """任务状态，取值有：
<li>PROCESSING：处理中：</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        """任务进度，取值为：0~100。
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def ErrCode(self):
        """错误码。
<li>0：成功；</li>
<li>其他值：失败。</li>
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """错误信息。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def CreateTime(self):
        """创建时间，格式按照 ISO 8601 标准表示。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeamInfo(AbstractModel):
    """团队信息

    """

    def __init__(self):
        r"""
        :param _TeamId: 团队 ID。
        :type TeamId: str
        :param _Name: 团队名称。
        :type Name: str
        :param _MemberCount: 团队成员个数
        :type MemberCount: int
        :param _CreateTime: 团队创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        :param _UpdateTime: 团队最后更新时间，格式按照 ISO 8601 标准表示。
        :type UpdateTime: str
        """
        self._TeamId = None
        self._Name = None
        self._MemberCount = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def TeamId(self):
        """团队 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Name(self):
        """团队名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MemberCount(self):
        """团队成员个数
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount

    @property
    def CreateTime(self):
        """团队创建时间，格式按照 ISO 8601 标准表示。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """团队最后更新时间，格式按照 ISO 8601 标准表示。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._Name = params.get("Name")
        self._MemberCount = params.get("MemberCount")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeamMemberInfo(AbstractModel):
    """团队成员信息

    """

    def __init__(self):
        r"""
        :param _MemberId: 团队成员 ID。
        :type MemberId: str
        :param _Remark: 团队成员备注。
        :type Remark: str
        :param _Role: 团队成员角色，取值：
<li>Owner：团队所有者，添加团队成员及修改团队成员解决时不能填此角色；</li>
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :type Role: str
        """
        self._MemberId = None
        self._Remark = None
        self._Role = None

    @property
    def MemberId(self):
        """团队成员 ID。
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Remark(self):
        """团队成员备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Role(self):
        """团队成员角色，取值：
<li>Owner：团队所有者，添加团队成员及修改团队成员解决时不能填此角色；</li>
<li>Admin：团队管理员；</li>
<li>Member：普通成员。</li>
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._Remark = params.get("Remark")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextReplacementInfo(AbstractModel):
    """模板插槽文本替换信息。

    """

    def __init__(self):
        r"""
        :param _Text: 替换的文本信息。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        """替换的文本信息。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextSlotInfo(AbstractModel):
    """文本类型卡槽信息。

    """

    def __init__(self):
        r"""
        :param _Text: 文本内容。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        """文本内容。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThirdPartyPublishInfo(AbstractModel):
    """第三方平台视频发布信息。

    """

    def __init__(self):
        r"""
        :param _ChannelMaterialId: 发布通道  ID。
        :type ChannelMaterialId: str
        :param _PenguinMediaPlatformPublishInfo: 企鹅号发布信息，如果使用的发布通道为企鹅号时必填。
        :type PenguinMediaPlatformPublishInfo: :class:`tencentcloud.cme.v20191029.models.PenguinMediaPlatformPublishInfo`
        :param _WeiboPublishInfo: 新浪微博发布信息，如果使用的发布通道为新浪微博时必填。
        :type WeiboPublishInfo: :class:`tencentcloud.cme.v20191029.models.WeiboPublishInfo`
        :param _KuaishouPublishInfo: 快手发布信息，如果使用的发布通道为快手时必填。
        :type KuaishouPublishInfo: :class:`tencentcloud.cme.v20191029.models.KuaishouPublishInfo`
        :param _CosPublishInfo: 腾讯云对象存储发布信息， 如果使用的发布通道为腾讯云对象存储时必填。
        :type CosPublishInfo: :class:`tencentcloud.cme.v20191029.models.CosPublishInputInfo`
        """
        self._ChannelMaterialId = None
        self._PenguinMediaPlatformPublishInfo = None
        self._WeiboPublishInfo = None
        self._KuaishouPublishInfo = None
        self._CosPublishInfo = None

    @property
    def ChannelMaterialId(self):
        """发布通道  ID。
        :rtype: str
        """
        return self._ChannelMaterialId

    @ChannelMaterialId.setter
    def ChannelMaterialId(self, ChannelMaterialId):
        self._ChannelMaterialId = ChannelMaterialId

    @property
    def PenguinMediaPlatformPublishInfo(self):
        """企鹅号发布信息，如果使用的发布通道为企鹅号时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.PenguinMediaPlatformPublishInfo`
        """
        return self._PenguinMediaPlatformPublishInfo

    @PenguinMediaPlatformPublishInfo.setter
    def PenguinMediaPlatformPublishInfo(self, PenguinMediaPlatformPublishInfo):
        self._PenguinMediaPlatformPublishInfo = PenguinMediaPlatformPublishInfo

    @property
    def WeiboPublishInfo(self):
        """新浪微博发布信息，如果使用的发布通道为新浪微博时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.WeiboPublishInfo`
        """
        return self._WeiboPublishInfo

    @WeiboPublishInfo.setter
    def WeiboPublishInfo(self, WeiboPublishInfo):
        self._WeiboPublishInfo = WeiboPublishInfo

    @property
    def KuaishouPublishInfo(self):
        """快手发布信息，如果使用的发布通道为快手时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.KuaishouPublishInfo`
        """
        return self._KuaishouPublishInfo

    @KuaishouPublishInfo.setter
    def KuaishouPublishInfo(self, KuaishouPublishInfo):
        self._KuaishouPublishInfo = KuaishouPublishInfo

    @property
    def CosPublishInfo(self):
        """腾讯云对象存储发布信息， 如果使用的发布通道为腾讯云对象存储时必填。
        :rtype: :class:`tencentcloud.cme.v20191029.models.CosPublishInputInfo`
        """
        return self._CosPublishInfo

    @CosPublishInfo.setter
    def CosPublishInfo(self, CosPublishInfo):
        self._CosPublishInfo = CosPublishInfo


    def _deserialize(self, params):
        self._ChannelMaterialId = params.get("ChannelMaterialId")
        if params.get("PenguinMediaPlatformPublishInfo") is not None:
            self._PenguinMediaPlatformPublishInfo = PenguinMediaPlatformPublishInfo()
            self._PenguinMediaPlatformPublishInfo._deserialize(params.get("PenguinMediaPlatformPublishInfo"))
        if params.get("WeiboPublishInfo") is not None:
            self._WeiboPublishInfo = WeiboPublishInfo()
            self._WeiboPublishInfo._deserialize(params.get("WeiboPublishInfo"))
        if params.get("KuaishouPublishInfo") is not None:
            self._KuaishouPublishInfo = KuaishouPublishInfo()
            self._KuaishouPublishInfo._deserialize(params.get("KuaishouPublishInfo"))
        if params.get("CosPublishInfo") is not None:
            self._CosPublishInfo = CosPublishInputInfo()
            self._CosPublishInfo._deserialize(params.get("CosPublishInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeRange(AbstractModel):
    """时间范围

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param _EndTime: 结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        """开始时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VODExportInfo(AbstractModel):
    """云点播导出信息。

    """

    def __init__(self):
        r"""
        :param _Name: 导出的媒资名称。
        :type Name: str
        :param _ClassId: 导出的媒资分类 Id。
        :type ClassId: int
        :param _ThirdPartyPublishInfos: 第三方平台发布信息列表。暂未正式对外，请勿使用。
        :type ThirdPartyPublishInfos: list of ThirdPartyPublishInfo
        """
        self._Name = None
        self._ClassId = None
        self._ThirdPartyPublishInfos = None

    @property
    def Name(self):
        """导出的媒资名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ClassId(self):
        """导出的媒资分类 Id。
        :rtype: int
        """
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId

    @property
    def ThirdPartyPublishInfos(self):
        """第三方平台发布信息列表。暂未正式对外，请勿使用。
        :rtype: list of ThirdPartyPublishInfo
        """
        return self._ThirdPartyPublishInfos

    @ThirdPartyPublishInfos.setter
    def ThirdPartyPublishInfos(self, ThirdPartyPublishInfos):
        self._ThirdPartyPublishInfos = ThirdPartyPublishInfos


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ClassId = params.get("ClassId")
        if params.get("ThirdPartyPublishInfos") is not None:
            self._ThirdPartyPublishInfos = []
            for item in params.get("ThirdPartyPublishInfos"):
                obj = ThirdPartyPublishInfo()
                obj._deserialize(item)
                self._ThirdPartyPublishInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEditProjectInput(AbstractModel):
    """视频编辑项目输入参数

    """

    def __init__(self):
        r"""
        :param _AspectRatio: 画布宽高比，取值有：
<li>16:9；</li>
<li>9:16；</li>
<li>2:1。</li>
默认值 16:9 。
        :type AspectRatio: str
        :param _VideoEditTemplateId: 视频编辑模板媒体 ID ，通过模板媒体导入项目轨道数据时填写。
        :type VideoEditTemplateId: str
        :param _InitTracks: 输入的媒体轨道列表，包括视频、音频，等媒体组成的多个轨道信息。其中：<li>输入的多个轨道在时间轴上和输出媒体文件的时间轴对齐；</li><li>时间轴上相同时间点的各个轨道的素材进行重叠，视频或者图片按轨道顺序进行图像的叠加，轨道顺序高的素材叠加在上面，音频素材进行混音；</li><li>视频、音频，每一种类型的轨道最多支持10个。</li>
注：当从模板导入项目时（即 VideoEditTemplateId 不为空时），该参数无效。
        :type InitTracks: list of MediaTrack
        """
        self._AspectRatio = None
        self._VideoEditTemplateId = None
        self._InitTracks = None

    @property
    def AspectRatio(self):
        """画布宽高比，取值有：
<li>16:9；</li>
<li>9:16；</li>
<li>2:1。</li>
默认值 16:9 。
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def VideoEditTemplateId(self):
        """视频编辑模板媒体 ID ，通过模板媒体导入项目轨道数据时填写。
        :rtype: str
        """
        return self._VideoEditTemplateId

    @VideoEditTemplateId.setter
    def VideoEditTemplateId(self, VideoEditTemplateId):
        self._VideoEditTemplateId = VideoEditTemplateId

    @property
    def InitTracks(self):
        """输入的媒体轨道列表，包括视频、音频，等媒体组成的多个轨道信息。其中：<li>输入的多个轨道在时间轴上和输出媒体文件的时间轴对齐；</li><li>时间轴上相同时间点的各个轨道的素材进行重叠，视频或者图片按轨道顺序进行图像的叠加，轨道顺序高的素材叠加在上面，音频素材进行混音；</li><li>视频、音频，每一种类型的轨道最多支持10个。</li>
注：当从模板导入项目时（即 VideoEditTemplateId 不为空时），该参数无效。
        :rtype: list of MediaTrack
        """
        return self._InitTracks

    @InitTracks.setter
    def InitTracks(self, InitTracks):
        self._InitTracks = InitTracks


    def _deserialize(self, params):
        self._AspectRatio = params.get("AspectRatio")
        self._VideoEditTemplateId = params.get("VideoEditTemplateId")
        if params.get("InitTracks") is not None:
            self._InitTracks = []
            for item in params.get("InitTracks"):
                obj = MediaTrack()
                obj._deserialize(item)
                self._InitTracks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEditProjectOutput(AbstractModel):
    """项目导出信息。

    """

    def __init__(self):
        r"""
        :param _MaterialId: 导出的多媒体创作引擎媒体 Id，仅当导出目标为多媒体创作引擎媒体时有效。
        :type MaterialId: str
        :param _VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        :param _URL: 导出的媒资 URL。
        :type URL: str
        :param _MetaData: 元信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.cme.v20191029.models.MediaMetaData`
        :param _CoverURL: 导出视频的封面图片 URL。
        :type CoverURL: str
        """
        self._MaterialId = None
        self._VodFileId = None
        self._URL = None
        self._MetaData = None
        self._CoverURL = None

    @property
    def MaterialId(self):
        """导出的多媒体创作引擎媒体 Id，仅当导出目标为多媒体创作引擎媒体时有效。
        :rtype: str
        """
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def VodFileId(self):
        """云点播媒资 FileId。
        :rtype: str
        """
        return self._VodFileId

    @VodFileId.setter
    def VodFileId(self, VodFileId):
        self._VodFileId = VodFileId

    @property
    def URL(self):
        """导出的媒资 URL。
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def MetaData(self):
        """元信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaMetaData`
        """
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData

    @property
    def CoverURL(self):
        """导出视频的封面图片 URL。
        :rtype: str
        """
        return self._CoverURL

    @CoverURL.setter
    def CoverURL(self, CoverURL):
        self._CoverURL = CoverURL


    def _deserialize(self, params):
        self._MaterialId = params.get("MaterialId")
        self._VodFileId = params.get("VodFileId")
        self._URL = params.get("URL")
        if params.get("MetaData") is not None:
            self._MetaData = MediaMetaData()
            self._MetaData._deserialize(params.get("MetaData"))
        self._CoverURL = params.get("CoverURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEditTemplateMaterial(AbstractModel):
    """视频编辑模板素材信息。

    """

    def __init__(self):
        r"""
        :param _AspectRatio: 视频编辑模板宽高比。
        :type AspectRatio: str
        :param _SlotSet: 卡槽信息。
        :type SlotSet: list of SlotInfo
        :param _PreviewVideoUrl: 模板预览视频 URL 地址 。
        :type PreviewVideoUrl: str
        """
        self._AspectRatio = None
        self._SlotSet = None
        self._PreviewVideoUrl = None

    @property
    def AspectRatio(self):
        """视频编辑模板宽高比。
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def SlotSet(self):
        """卡槽信息。
        :rtype: list of SlotInfo
        """
        return self._SlotSet

    @SlotSet.setter
    def SlotSet(self, SlotSet):
        self._SlotSet = SlotSet

    @property
    def PreviewVideoUrl(self):
        """模板预览视频 URL 地址 。
        :rtype: str
        """
        return self._PreviewVideoUrl

    @PreviewVideoUrl.setter
    def PreviewVideoUrl(self, PreviewVideoUrl):
        self._PreviewVideoUrl = PreviewVideoUrl


    def _deserialize(self, params):
        self._AspectRatio = params.get("AspectRatio")
        if params.get("SlotSet") is not None:
            self._SlotSet = []
            for item in params.get("SlotSet"):
                obj = SlotInfo()
                obj._deserialize(item)
                self._SlotSet.append(obj)
        self._PreviewVideoUrl = params.get("PreviewVideoUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncodingPreset(AbstractModel):
    """视频编码配置

    """

    def __init__(self):
        r"""
        :param _Id: 配置 ID。
        :type Id: int
        :param _Name: 配置名。
        :type Name: str
        :param _Container: 封装格式，可选值：
<li>mp4 ；</li>
<li>mov 。</li>
        :type Container: str
        :param _RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :type RemoveVideo: int
        :param _RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :type RemoveAudio: int
        :param _VideoSetting: 视频编码配置中的视频设置。
        :type VideoSetting: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetVideoSetting`
        :param _AudioSetting: 视频编码配置中的音频设置。
        :type AudioSetting: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetAudioSetting`
        """
        self._Id = None
        self._Name = None
        self._Container = None
        self._RemoveVideo = None
        self._RemoveAudio = None
        self._VideoSetting = None
        self._AudioSetting = None

    @property
    def Id(self):
        """配置 ID。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """配置名。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Container(self):
        """封装格式，可选值：
<li>mp4 ；</li>
<li>mov 。</li>
        :rtype: str
        """
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def RemoveVideo(self):
        """是否去除视频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :rtype: int
        """
        return self._RemoveVideo

    @RemoveVideo.setter
    def RemoveVideo(self, RemoveVideo):
        self._RemoveVideo = RemoveVideo

    @property
    def RemoveAudio(self):
        """是否去除音频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。
        :rtype: int
        """
        return self._RemoveAudio

    @RemoveAudio.setter
    def RemoveAudio(self, RemoveAudio):
        self._RemoveAudio = RemoveAudio

    @property
    def VideoSetting(self):
        """视频编码配置中的视频设置。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetVideoSetting`
        """
        return self._VideoSetting

    @VideoSetting.setter
    def VideoSetting(self, VideoSetting):
        self._VideoSetting = VideoSetting

    @property
    def AudioSetting(self):
        """视频编码配置中的音频设置。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoEncodingPresetAudioSetting`
        """
        return self._AudioSetting

    @AudioSetting.setter
    def AudioSetting(self, AudioSetting):
        self._AudioSetting = AudioSetting


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Container = params.get("Container")
        self._RemoveVideo = params.get("RemoveVideo")
        self._RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoSetting") is not None:
            self._VideoSetting = VideoEncodingPresetVideoSetting()
            self._VideoSetting._deserialize(params.get("VideoSetting"))
        if params.get("AudioSetting") is not None:
            self._AudioSetting = VideoEncodingPresetAudioSetting()
            self._AudioSetting._deserialize(params.get("AudioSetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncodingPresetAudioSetting(AbstractModel):
    """视频编码配置中的音频设置

    """

    def __init__(self):
        r"""
        :param _Codec: 音频流的编码格式，可选值：
AAC：AAC 编码。

默认值：AAC。
        :type Codec: str
        :param _Bitrate: 音频码率，单位：bps。
默认值：64K。
        :type Bitrate: int
        :param _Channels: 音频声道数，可选值： 
<li>1：单声道；</li>
<li>2：双声道。</li> 
默认值：2。
        :type Channels: int
        :param _SampleRate: 音频流的采样率，仅支持 16000； 32000； 44100； 48000。单位：Hz。 
默认值：16000。
        :type SampleRate: int
        """
        self._Codec = None
        self._Bitrate = None
        self._Channels = None
        self._SampleRate = None

    @property
    def Codec(self):
        """音频流的编码格式，可选值：
AAC：AAC 编码。

默认值：AAC。
        :rtype: str
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def Bitrate(self):
        """音频码率，单位：bps。
默认值：64K。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Channels(self):
        """音频声道数，可选值： 
<li>1：单声道；</li>
<li>2：双声道。</li> 
默认值：2。
        :rtype: int
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def SampleRate(self):
        """音频流的采样率，仅支持 16000； 32000； 44100； 48000。单位：Hz。 
默认值：16000。
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate


    def _deserialize(self, params):
        self._Codec = params.get("Codec")
        self._Bitrate = params.get("Bitrate")
        self._Channels = params.get("Channels")
        self._SampleRate = params.get("SampleRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncodingPresetAudioSettingForUpdate(AbstractModel):
    """视频编码配置中的音频设置更新信息

    """

    def __init__(self):
        r"""
        :param _Bitrate: 音频码率，单位：bps。
不填则不修改。
        :type Bitrate: str
        :param _Channels: 音频声道数，可选值： 
<li>1：单声道；</li>
<li>2：双声道。</li> 
不填则不修改。
        :type Channels: int
        :param _SampleRate: 音频流的采样率，目前仅支持： 16000； 32000； 44100； 48000。单位：Hz。
不填则不修改。
        :type SampleRate: int
        """
        self._Bitrate = None
        self._Channels = None
        self._SampleRate = None

    @property
    def Bitrate(self):
        """音频码率，单位：bps。
不填则不修改。
        :rtype: str
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Channels(self):
        """音频声道数，可选值： 
<li>1：单声道；</li>
<li>2：双声道。</li> 
不填则不修改。
        :rtype: int
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def SampleRate(self):
        """音频流的采样率，目前仅支持： 16000； 32000； 44100； 48000。单位：Hz。
不填则不修改。
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate


    def _deserialize(self, params):
        self._Bitrate = params.get("Bitrate")
        self._Channels = params.get("Channels")
        self._SampleRate = params.get("SampleRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncodingPresetVideoSetting(AbstractModel):
    """视频编码配置中的视频设置信息

    """

    def __init__(self):
        r"""
        :param _Codec: 视频流的编码格式，可选值：
<li>H264：H.264 编码。</li>
        :type Codec: str
        :param _ShortEdge: 视频短边尺寸，取值范围： [128, 4096]，单位：px。
视频最后的分辨率，根据短边尺寸和宽高比进行计算。
例：如果项目的宽高比是 16：9 ：
<li>短边尺寸为 1080，则导出视频的分辨率为 1920 * 1080。</li>
<li>短边尺寸为 720，则导出视频的分辨率为 1280 * 720。</li>
如果项目的宽高比是 9：16 ：
<li>短边尺寸为 1080，则导出视频的分辨率为 1080 * 1920。</li>
<li>短边尺寸为 720，则导出视频的分辨率为 720 * 1280。</li>
默认值：1080。
        :type ShortEdge: int
        :param _Bitrate: 指定码率，单位 bps。当该参数为'0'时则不强制限定码率。
默认值：0。
        :type Bitrate: int
        """
        self._Codec = None
        self._ShortEdge = None
        self._Bitrate = None

    @property
    def Codec(self):
        """视频流的编码格式，可选值：
<li>H264：H.264 编码。</li>
        :rtype: str
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def ShortEdge(self):
        """视频短边尺寸，取值范围： [128, 4096]，单位：px。
视频最后的分辨率，根据短边尺寸和宽高比进行计算。
例：如果项目的宽高比是 16：9 ：
<li>短边尺寸为 1080，则导出视频的分辨率为 1920 * 1080。</li>
<li>短边尺寸为 720，则导出视频的分辨率为 1280 * 720。</li>
如果项目的宽高比是 9：16 ：
<li>短边尺寸为 1080，则导出视频的分辨率为 1080 * 1920。</li>
<li>短边尺寸为 720，则导出视频的分辨率为 720 * 1280。</li>
默认值：1080。
        :rtype: int
        """
        return self._ShortEdge

    @ShortEdge.setter
    def ShortEdge(self, ShortEdge):
        self._ShortEdge = ShortEdge

    @property
    def Bitrate(self):
        """指定码率，单位 bps。当该参数为'0'时则不强制限定码率。
默认值：0。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate


    def _deserialize(self, params):
        self._Codec = params.get("Codec")
        self._ShortEdge = params.get("ShortEdge")
        self._Bitrate = params.get("Bitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncodingPresetVideoSettingForUpdate(AbstractModel):
    """视频编码配置的视频设置更新信息

    """

    def __init__(self):
        r"""
        :param _ShortEdge: 视频短边尺寸，取值范围： [128, 4096]，单位：px。
视频最后的分辨率，根据短边尺寸和宽高比进行计算。
例：如果项目的宽高比是 16：9 ：
<li>短边尺寸为 1080，则导出视频的分辨率为 1920 * 1080。</li>
<li>短边尺寸为 720，则导出视频的分辨率为 1280 * 720。</li>
如果项目的宽高比是 9：16 ：
<li>短边尺寸为 1080，则导出视频的分辨率为 1080 * 1920。</li>
<li>短边尺寸为 720，则导出视频的分辨率为 720 * 1280。</li>
不填则不修改。
        :type ShortEdge: int
        :param _Bitrate: 指定码率，单位 bps。当该参数为'0' 时则不强制限定码率。
不填则不修改。
        :type Bitrate: int
        :param _FrameRate: 指定帧率。单位 Hz。
不填则不修改。
        :type FrameRate: float
        """
        self._ShortEdge = None
        self._Bitrate = None
        self._FrameRate = None

    @property
    def ShortEdge(self):
        """视频短边尺寸，取值范围： [128, 4096]，单位：px。
视频最后的分辨率，根据短边尺寸和宽高比进行计算。
例：如果项目的宽高比是 16：9 ：
<li>短边尺寸为 1080，则导出视频的分辨率为 1920 * 1080。</li>
<li>短边尺寸为 720，则导出视频的分辨率为 1280 * 720。</li>
如果项目的宽高比是 9：16 ：
<li>短边尺寸为 1080，则导出视频的分辨率为 1080 * 1920。</li>
<li>短边尺寸为 720，则导出视频的分辨率为 720 * 1280。</li>
不填则不修改。
        :rtype: int
        """
        return self._ShortEdge

    @ShortEdge.setter
    def ShortEdge(self, ShortEdge):
        self._ShortEdge = ShortEdge

    @property
    def Bitrate(self):
        """指定码率，单位 bps。当该参数为'0' 时则不强制限定码率。
不填则不修改。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def FrameRate(self):
        """指定帧率。单位 Hz。
不填则不修改。
        :rtype: float
        """
        return self._FrameRate

    @FrameRate.setter
    def FrameRate(self, FrameRate):
        self._FrameRate = FrameRate


    def _deserialize(self, params):
        self._ShortEdge = params.get("ShortEdge")
        self._Bitrate = params.get("Bitrate")
        self._FrameRate = params.get("FrameRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoExportCompletedEvent(AbstractModel):
    """视频导出完成事件。

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 Id。
        :type TaskId: str
        :param _Status: 任务状态，取值有：
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :type Status: str
        :param _ErrCode: 错误码，取值有：
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param _ErrMsg: 错误信息。
        :type ErrMsg: str
        :param _Output: 任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.cme.v20191029.models.VideoEditProjectOutput`
        """
        self._TaskId = None
        self._Status = None
        self._ErrCode = None
        self._ErrMsg = None
        self._Output = None

    @property
    def TaskId(self):
        """任务 Id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """任务状态，取值有：
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrCode(self):
        """错误码，取值有：
<li>0：成功；</li>
<li>其他值：失败。</li>
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        """错误信息。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Output(self):
        """任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.VideoEditProjectOutput`
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        if params.get("Output") is not None:
            self._Output = VideoEditProjectOutput()
            self._Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoExportExtensionArgs(AbstractModel):
    """视频导出扩展参数

    """

    def __init__(self):
        r"""
        :param _Container: 封装格式，可选值：
<li>mp4 </li>
<li>mov </li>
不填则使用视频导出编码配置。
        :type Container: str
        :param _ShortEdge: 视频短边尺寸，取值范围： [128, 4096]，单位：px。
视频最后的分辨率，根据短边尺寸和宽高比进行计算。
例如：项目的宽高比是 16：9 ：
<li>短边尺寸为 1080，则导出视频的分辨率为 1920 * 1080。</li>
<li>短边尺寸为 720，则导出视频的分辨率为 1280 * 720</li>
不填则使用视频导出编码配置。
        :type ShortEdge: int
        :param _VideoBitrate: 指定码率，单位 bps。当该参数为 0 时则不强制限定码率。
不填则使用视频导出编码配置。
        :type VideoBitrate: int
        :param _FrameRate: 帧率。取值范围：[15, 60]，不填默认值为 25。
        :type FrameRate: float
        :param _RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
不填则使用视频导出编码配置。
        :type RemoveVideo: int
        :param _RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
不填则使用视频导出编码配置。
        :type RemoveAudio: int
        :param _StartTime: 片段起始时间，单位：毫秒。
        :type StartTime: int
        :param _EndTime: 片段结束时间，单位：毫秒。
        :type EndTime: int
        """
        self._Container = None
        self._ShortEdge = None
        self._VideoBitrate = None
        self._FrameRate = None
        self._RemoveVideo = None
        self._RemoveAudio = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Container(self):
        """封装格式，可选值：
<li>mp4 </li>
<li>mov </li>
不填则使用视频导出编码配置。
        :rtype: str
        """
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def ShortEdge(self):
        """视频短边尺寸，取值范围： [128, 4096]，单位：px。
视频最后的分辨率，根据短边尺寸和宽高比进行计算。
例如：项目的宽高比是 16：9 ：
<li>短边尺寸为 1080，则导出视频的分辨率为 1920 * 1080。</li>
<li>短边尺寸为 720，则导出视频的分辨率为 1280 * 720</li>
不填则使用视频导出编码配置。
        :rtype: int
        """
        return self._ShortEdge

    @ShortEdge.setter
    def ShortEdge(self, ShortEdge):
        self._ShortEdge = ShortEdge

    @property
    def VideoBitrate(self):
        """指定码率，单位 bps。当该参数为 0 时则不强制限定码率。
不填则使用视频导出编码配置。
        :rtype: int
        """
        return self._VideoBitrate

    @VideoBitrate.setter
    def VideoBitrate(self, VideoBitrate):
        self._VideoBitrate = VideoBitrate

    @property
    def FrameRate(self):
        """帧率。取值范围：[15, 60]，不填默认值为 25。
        :rtype: float
        """
        return self._FrameRate

    @FrameRate.setter
    def FrameRate(self, FrameRate):
        self._FrameRate = FrameRate

    @property
    def RemoveVideo(self):
        """是否去除视频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
不填则使用视频导出编码配置。
        :rtype: int
        """
        return self._RemoveVideo

    @RemoveVideo.setter
    def RemoveVideo(self, RemoveVideo):
        self._RemoveVideo = RemoveVideo

    @property
    def RemoveAudio(self):
        """是否去除音频数据，可选值：
<li>0：保留；</li>
<li>1：去除。</li>
不填则使用视频导出编码配置。
        :rtype: int
        """
        return self._RemoveAudio

    @RemoveAudio.setter
    def RemoveAudio(self, RemoveAudio):
        self._RemoveAudio = RemoveAudio

    @property
    def StartTime(self):
        """片段起始时间，单位：毫秒。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """片段结束时间，单位：毫秒。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Container = params.get("Container")
        self._ShortEdge = params.get("ShortEdge")
        self._VideoBitrate = params.get("VideoBitrate")
        self._FrameRate = params.get("FrameRate")
        self._RemoveVideo = params.get("RemoveVideo")
        self._RemoveAudio = params.get("RemoveAudio")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoMaterial(AbstractModel):
    """视频素材信息

    """

    def __init__(self):
        r"""
        :param _MetaData: 素材元信息。
        :type MetaData: :class:`tencentcloud.cme.v20191029.models.MediaMetaData`
        :param _ImageSpriteInfo: 雪碧图信息。
        :type ImageSpriteInfo: :class:`tencentcloud.cme.v20191029.models.MediaImageSpriteInfo`
        :param _MaterialUrl: 素材媒体文件的播放 URL 地址。
        :type MaterialUrl: str
        :param _CoverUrl: 素材媒体文件的封面图片地址。
        :type CoverUrl: str
        :param _Resolution: 媒体文件分辨率。取值为：LD/SD/HD/FHD/2K/4K。
        :type Resolution: str
        :param _MaterialStatus: 素材状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialStatus: :class:`tencentcloud.cme.v20191029.models.MaterialStatus`
        :param _OriginalUrl: 素材媒体文件的原始 URL 地址。
        :type OriginalUrl: str
        :param _VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        """
        self._MetaData = None
        self._ImageSpriteInfo = None
        self._MaterialUrl = None
        self._CoverUrl = None
        self._Resolution = None
        self._MaterialStatus = None
        self._OriginalUrl = None
        self._VodFileId = None

    @property
    def MetaData(self):
        """素材元信息。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaMetaData`
        """
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData

    @property
    def ImageSpriteInfo(self):
        """雪碧图信息。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MediaImageSpriteInfo`
        """
        return self._ImageSpriteInfo

    @ImageSpriteInfo.setter
    def ImageSpriteInfo(self, ImageSpriteInfo):
        self._ImageSpriteInfo = ImageSpriteInfo

    @property
    def MaterialUrl(self):
        """素材媒体文件的播放 URL 地址。
        :rtype: str
        """
        return self._MaterialUrl

    @MaterialUrl.setter
    def MaterialUrl(self, MaterialUrl):
        self._MaterialUrl = MaterialUrl

    @property
    def CoverUrl(self):
        """素材媒体文件的封面图片地址。
        :rtype: str
        """
        return self._CoverUrl

    @CoverUrl.setter
    def CoverUrl(self, CoverUrl):
        self._CoverUrl = CoverUrl

    @property
    def Resolution(self):
        """媒体文件分辨率。取值为：LD/SD/HD/FHD/2K/4K。
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaterialStatus(self):
        """素材状态。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cme.v20191029.models.MaterialStatus`
        """
        return self._MaterialStatus

    @MaterialStatus.setter
    def MaterialStatus(self, MaterialStatus):
        self._MaterialStatus = MaterialStatus

    @property
    def OriginalUrl(self):
        """素材媒体文件的原始 URL 地址。
        :rtype: str
        """
        return self._OriginalUrl

    @OriginalUrl.setter
    def OriginalUrl(self, OriginalUrl):
        self._OriginalUrl = OriginalUrl

    @property
    def VodFileId(self):
        """云点播媒资 FileId。
        :rtype: str
        """
        return self._VodFileId

    @VodFileId.setter
    def VodFileId(self, VodFileId):
        self._VodFileId = VodFileId


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self._MetaData = MediaMetaData()
            self._MetaData._deserialize(params.get("MetaData"))
        if params.get("ImageSpriteInfo") is not None:
            self._ImageSpriteInfo = MediaImageSpriteInfo()
            self._ImageSpriteInfo._deserialize(params.get("ImageSpriteInfo"))
        self._MaterialUrl = params.get("MaterialUrl")
        self._CoverUrl = params.get("CoverUrl")
        self._Resolution = params.get("Resolution")
        if params.get("MaterialStatus") is not None:
            self._MaterialStatus = MaterialStatus()
            self._MaterialStatus._deserialize(params.get("MaterialStatus"))
        self._OriginalUrl = params.get("OriginalUrl")
        self._VodFileId = params.get("VodFileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoSegmentationProjectInput(AbstractModel):
    """视频拆条项目的输入信息。

    """

    def __init__(self):
        r"""
        :param _AspectRatio: 画布宽高比，取值有：
<li>16:9；</li>
<li>9:16；</li>
<li>2:1。</li>
默认值 16:9 。
        :type AspectRatio: str
        :param _ProcessModel: 视频拆条处理模型，不填则默认为手工分割视频。取值 ：
<li>AI.GameHighlights.PUBG：和平精英集锦 ;</li>
<li>AI.GameHighlights.Honor OfKings：王者荣耀集锦 ;</li>
<li>AI.SportHighlights.Football：足球集锦 </li>
<li>AI.SportHighlights.Basketball：篮球集锦 ；</li>
<li>AI.PersonSegmentation：人物集锦  ;</li>
<li>AI.NewsSegmentation：新闻拆条。</li>
        :type ProcessModel: str
        """
        self._AspectRatio = None
        self._ProcessModel = None

    @property
    def AspectRatio(self):
        """画布宽高比，取值有：
<li>16:9；</li>
<li>9:16；</li>
<li>2:1。</li>
默认值 16:9 。
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def ProcessModel(self):
        """视频拆条处理模型，不填则默认为手工分割视频。取值 ：
<li>AI.GameHighlights.PUBG：和平精英集锦 ;</li>
<li>AI.GameHighlights.Honor OfKings：王者荣耀集锦 ;</li>
<li>AI.SportHighlights.Football：足球集锦 </li>
<li>AI.SportHighlights.Basketball：篮球集锦 ；</li>
<li>AI.PersonSegmentation：人物集锦  ;</li>
<li>AI.NewsSegmentation：新闻拆条。</li>
        :rtype: str
        """
        return self._ProcessModel

    @ProcessModel.setter
    def ProcessModel(self, ProcessModel):
        self._ProcessModel = ProcessModel


    def _deserialize(self, params):
        self._AspectRatio = params.get("AspectRatio")
        self._ProcessModel = params.get("ProcessModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoStreamInfo(AbstractModel):
    """视频流信息。

    """

    def __init__(self):
        r"""
        :param _Bitrate: 码率，单位：bps。
        :type Bitrate: int
        :param _Height: 高度，单位：px。
        :type Height: int
        :param _Width: 宽度，单位：px。
        :type Width: int
        :param _Codec: 编码格式。
        :type Codec: str
        :param _Fps: 帧率，单位：hz。
        :type Fps: int
        """
        self._Bitrate = None
        self._Height = None
        self._Width = None
        self._Codec = None
        self._Fps = None

    @property
    def Bitrate(self):
        """码率，单位：bps。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Height(self):
        """高度，单位：px。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        """宽度，单位：px。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Codec(self):
        """编码格式。
        :rtype: str
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def Fps(self):
        """帧率，单位：hz。
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps


    def _deserialize(self, params):
        self._Bitrate = params.get("Bitrate")
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._Codec = params.get("Codec")
        self._Fps = params.get("Fps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTrackItem(AbstractModel):
    """视频轨的视频片段信息。

    """

    def __init__(self):
        r"""
        :param _SourceType: 视频媒体来源类型，取值有：
<ul>
<li>VOD ：媒体来源于云点播文件 。</li>
<li>CME ：视频来源制作云媒体文件。</li>
<li>EXTERNAL ：视频来源于媒资绑定，如果媒体不是存储在腾讯云点播中或者云创中，都需要使用媒资绑定。</li>
</ul>
        :type SourceType: str
        :param _SourceMedia: 视频媒体，可取值为：
<ul>
<li>当 SourceType 为 VOD 时，参数填云点播 FileId ；</li>
<li>当 SourceType 为 CME 时，参数填多媒体创作引擎媒体 Id；</li>
<li>当 SourceType 为 EXTERNAL 时，目前仅支持外部媒体 URL(如`https://www.example.com/a.mp4`)，参数填写规则请参见注意事项。</li>
</ul>

注意：
<li>当 SourceType 为 EXTERNAL 并且媒体 URL Scheme 为 `https` 时(如：`https://www.example.com/a.mp4`)，参数为：`1000000:www.example.com/a.mp4`。</li>
<li>当 SourceType 为 EXTERNAL 并且媒体 URL Scheme 为 `http` 时(如：`http://www.example.com/b.mp4`)，参数为：`1000001:www.example.com/b.mp4`。</li>
        :type SourceMedia: str
        :param _SourceMediaStartTime: 视频片段取自媒体文件的起始时间，单位为秒。默认为0。
        :type SourceMediaStartTime: float
        :param _Duration: 视频片段时长，单位为秒。默认取视频媒体文件本身长度，表示截取全部媒体文件。如果源文件是图片，Duration需要大于0。
        :type Duration: float
        :param _XPos: 视频片段原点距离画布原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 XPos 为画布宽度指定百分比的位置，如 10% 表示 XPos 为画布口宽度的 10%。</li>
<li>当字符串以 px 结尾，表示视频片段 XPos 单位为像素，如 100px 表示 XPos 为100像素。</li>
默认值：0px。
        :type XPos: str
        :param _YPos: 视频片段原点距离画布原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 YPos 为画布高度指定百分比的位置，如 10% 表示 YPos 为画布高度的 10%。</li>
<li>当字符串以 px 结尾，表示视频片段 YPos 单位为像素，如 100px 表示 YPos 为100像素。</li>
默认值：0px。
        :type YPos: str
        :param _CoordinateOrigin: 视频原点位置，取值有：
<li>Center：坐标原点为中心位置，如画布中心。</li>
默认值 ：Center。
        :type CoordinateOrigin: str
        :param _Height: 视频片段的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 Height 为画布高度的百分比大小，如 10% 表示 Height 为画布高度的 10%；</li>
<li>当字符串以 px 结尾，表示视频片段 Height 单位为像素，如 100px 表示 Height 为100像素；</li>
<li>当 Width、Height 均为空，则 Width 和 Height 取视频媒体文件本身的 Width、Height；</li>
<li>当 Width 为空，Height 非空，则 Width 按比例缩放；</li>
<li>当 Width 非空，Height 为空，则 Height 按比例缩放。</li>
        :type Height: str
        :param _Width: 视频片段的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 Width 为画布宽度的百分比大小，如 10% 表示 Width 为画布宽度的 10%；</li>
<li>当字符串以 px 结尾，表示视频片段 Width 单位为像素，如 100px 表示 Width 为100像素；</li>
<li>当 Width、Height 均为空，则 Width 和 Height 取视频媒体文件本身的 Width、Height；</li>
<li>当 Width 为空，Height 非空，则 Width 按比例缩放；</li>
<li>当 Width 非空，Height 为空，则 Height 按比例缩放。</li>
        :type Width: str
        """
        self._SourceType = None
        self._SourceMedia = None
        self._SourceMediaStartTime = None
        self._Duration = None
        self._XPos = None
        self._YPos = None
        self._CoordinateOrigin = None
        self._Height = None
        self._Width = None

    @property
    def SourceType(self):
        """视频媒体来源类型，取值有：
<ul>
<li>VOD ：媒体来源于云点播文件 。</li>
<li>CME ：视频来源制作云媒体文件。</li>
<li>EXTERNAL ：视频来源于媒资绑定，如果媒体不是存储在腾讯云点播中或者云创中，都需要使用媒资绑定。</li>
</ul>
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceMedia(self):
        """视频媒体，可取值为：
<ul>
<li>当 SourceType 为 VOD 时，参数填云点播 FileId ；</li>
<li>当 SourceType 为 CME 时，参数填多媒体创作引擎媒体 Id；</li>
<li>当 SourceType 为 EXTERNAL 时，目前仅支持外部媒体 URL(如`https://www.example.com/a.mp4`)，参数填写规则请参见注意事项。</li>
</ul>

注意：
<li>当 SourceType 为 EXTERNAL 并且媒体 URL Scheme 为 `https` 时(如：`https://www.example.com/a.mp4`)，参数为：`1000000:www.example.com/a.mp4`。</li>
<li>当 SourceType 为 EXTERNAL 并且媒体 URL Scheme 为 `http` 时(如：`http://www.example.com/b.mp4`)，参数为：`1000001:www.example.com/b.mp4`。</li>
        :rtype: str
        """
        return self._SourceMedia

    @SourceMedia.setter
    def SourceMedia(self, SourceMedia):
        self._SourceMedia = SourceMedia

    @property
    def SourceMediaStartTime(self):
        """视频片段取自媒体文件的起始时间，单位为秒。默认为0。
        :rtype: float
        """
        return self._SourceMediaStartTime

    @SourceMediaStartTime.setter
    def SourceMediaStartTime(self, SourceMediaStartTime):
        self._SourceMediaStartTime = SourceMediaStartTime

    @property
    def Duration(self):
        """视频片段时长，单位为秒。默认取视频媒体文件本身长度，表示截取全部媒体文件。如果源文件是图片，Duration需要大于0。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def XPos(self):
        """视频片段原点距离画布原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 XPos 为画布宽度指定百分比的位置，如 10% 表示 XPos 为画布口宽度的 10%。</li>
<li>当字符串以 px 结尾，表示视频片段 XPos 单位为像素，如 100px 表示 XPos 为100像素。</li>
默认值：0px。
        :rtype: str
        """
        return self._XPos

    @XPos.setter
    def XPos(self, XPos):
        self._XPos = XPos

    @property
    def YPos(self):
        """视频片段原点距离画布原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 YPos 为画布高度指定百分比的位置，如 10% 表示 YPos 为画布高度的 10%。</li>
<li>当字符串以 px 结尾，表示视频片段 YPos 单位为像素，如 100px 表示 YPos 为100像素。</li>
默认值：0px。
        :rtype: str
        """
        return self._YPos

    @YPos.setter
    def YPos(self, YPos):
        self._YPos = YPos

    @property
    def CoordinateOrigin(self):
        """视频原点位置，取值有：
<li>Center：坐标原点为中心位置，如画布中心。</li>
默认值 ：Center。
        :rtype: str
        """
        return self._CoordinateOrigin

    @CoordinateOrigin.setter
    def CoordinateOrigin(self, CoordinateOrigin):
        self._CoordinateOrigin = CoordinateOrigin

    @property
    def Height(self):
        """视频片段的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 Height 为画布高度的百分比大小，如 10% 表示 Height 为画布高度的 10%；</li>
<li>当字符串以 px 结尾，表示视频片段 Height 单位为像素，如 100px 表示 Height 为100像素；</li>
<li>当 Width、Height 均为空，则 Width 和 Height 取视频媒体文件本身的 Width、Height；</li>
<li>当 Width 为空，Height 非空，则 Width 按比例缩放；</li>
<li>当 Width 非空，Height 为空，则 Height 按比例缩放。</li>
        :rtype: str
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        """视频片段的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 Width 为画布宽度的百分比大小，如 10% 表示 Width 为画布宽度的 10%；</li>
<li>当字符串以 px 结尾，表示视频片段 Width 单位为像素，如 100px 表示 Width 为100像素；</li>
<li>当 Width、Height 均为空，则 Width 和 Height 取视频媒体文件本身的 Width、Height；</li>
<li>当 Width 为空，Height 非空，则 Width 按比例缩放；</li>
<li>当 Width 非空，Height 为空，则 Height 按比例缩放。</li>
        :rtype: str
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width


    def _deserialize(self, params):
        self._SourceType = params.get("SourceType")
        self._SourceMedia = params.get("SourceMedia")
        self._SourceMediaStartTime = params.get("SourceMediaStartTime")
        self._Duration = params.get("Duration")
        self._XPos = params.get("XPos")
        self._YPos = params.get("YPos")
        self._CoordinateOrigin = params.get("CoordinateOrigin")
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPullInputInfo(AbstractModel):
    """点播拉流信息，包括输入拉流地址和播放次数。

    """

    def __init__(self):
        r"""
        :param _InputUrls: 点播输入拉流 URL 。
        :type InputUrls: list of str
        :param _LoopTimes: 播放次数，取值有：
<li>-1 : 循环播放，直到转推结束；</li>
<li>0 : 不循环；</li>
<li>大于0 : 具体循环次数，次数和时间以先结束的为准。</li>
默认不循环。
        :type LoopTimes: int
        """
        self._InputUrls = None
        self._LoopTimes = None

    @property
    def InputUrls(self):
        """点播输入拉流 URL 。
        :rtype: list of str
        """
        return self._InputUrls

    @InputUrls.setter
    def InputUrls(self, InputUrls):
        self._InputUrls = InputUrls

    @property
    def LoopTimes(self):
        """播放次数，取值有：
<li>-1 : 循环播放，直到转推结束；</li>
<li>0 : 不循环；</li>
<li>大于0 : 具体循环次数，次数和时间以先结束的为准。</li>
默认不循环。
        :rtype: int
        """
        return self._LoopTimes

    @LoopTimes.setter
    def LoopTimes(self, LoopTimes):
        self._LoopTimes = LoopTimes


    def _deserialize(self, params):
        self._InputUrls = params.get("InputUrls")
        self._LoopTimes = params.get("LoopTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPullInputPlayInfo(AbstractModel):
    """点播文件播放信息，包含当前在播地址和该地址已播时长 。

    """

    def __init__(self):
        r"""
        :param _Url: 当前正在播放文件 Url 。
        :type Url: str
        :param _TimeOffset: 点播文件已播放时长，单位：秒。
        :type TimeOffset: float
        """
        self._Url = None
        self._TimeOffset = None

    @property
    def Url(self):
        """当前正在播放文件 Url 。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def TimeOffset(self):
        """点播文件已播放时长，单位：秒。
        :rtype: float
        """
        return self._TimeOffset

    @TimeOffset.setter
    def TimeOffset(self, TimeOffset):
        self._TimeOffset = TimeOffset


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._TimeOffset = params.get("TimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeiboPublishInfo(AbstractModel):
    """微博发布信息。

    """

    def __init__(self):
        r"""
        :param _Title: 视频发布标题。
        :type Title: str
        :param _Description: 视频发布描述信息。
        :type Description: str
        :param _Visible: 微博可见性，可取值为：
<li>Public：公开，所有人可见；</li>
<li>Private：私有，仅自己可见。</li>

默认为 Public，所有人可见。
        :type Visible: str
        """
        self._Title = None
        self._Description = None
        self._Visible = None

    @property
    def Title(self):
        """视频发布标题。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Description(self):
        """视频发布描述信息。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Visible(self):
        """微博可见性，可取值为：
<li>Public：公开，所有人可见；</li>
<li>Private：私有，仅自己可见。</li>

默认为 Public，所有人可见。
        :rtype: str
        """
        return self._Visible

    @Visible.setter
    def Visible(self, Visible):
        self._Visible = Visible


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Description = params.get("Description")
        self._Visible = params.get("Visible")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        