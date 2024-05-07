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


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 应用名称(不为空且最长为 200)
        :type Name: str
        :param _InstanceID: 业务系统 ID
        :type InstanceID: str
        :param _Rate: 项目抽样率(大于等于 0)
        :type Rate: str
        :param _EnableURLGroup: 是否开启聚类
        :type EnableURLGroup: int
        :param _Type: 项目类型("web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param _Repo: 项目对应仓库地址(可选，最长为 256)
        :type Repo: str
        :param _URL: 项目对应网页地址(可选，最长为 256)
        :type URL: str
        :param _Desc: 应用描述(可选，最长为 1000)
        :type Desc: str
        """
        self._Name = None
        self._InstanceID = None
        self._Rate = None
        self._EnableURLGroup = None
        self._Type = None
        self._Repo = None
        self._URL = None
        self._Desc = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def EnableURLGroup(self):
        return self._EnableURLGroup

    @EnableURLGroup.setter
    def EnableURLGroup(self, EnableURLGroup):
        self._EnableURLGroup = EnableURLGroup

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Repo(self):
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._InstanceID = params.get("InstanceID")
        self._Rate = params.get("Rate")
        self._EnableURLGroup = params.get("EnableURLGroup")
        self._Type = params.get("Type")
        self._Repo = params.get("Repo")
        self._URL = params.get("URL")
        self._Desc = params.get("Desc")
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
        :param _ID: 项目 id
        :type ID: int
        :param _Key: 项目唯一key
        :type Key: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ID = None
        self._Key = None
        self._RequestId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Key = params.get("Key")
        self._RequestId = params.get("RequestId")


class CreateReleaseFileRequest(AbstractModel):
    """CreateReleaseFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: 项目 id
        :type ProjectID: int
        :param _Files: 文件信息列表
        :type Files: list of ReleaseFile
        """
        self._ProjectID = None
        self._Files = None

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def Files(self):
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = ReleaseFile()
                obj._deserialize(item)
                self._Files.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReleaseFileResponse(AbstractModel):
    """CreateReleaseFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 调用结果
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateStarProjectRequest(AbstractModel):
    """CreateStarProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID：taw-123
        :type InstanceID: str
        :param _ID: 项目ID
        :type ID: int
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStarProjectResponse(AbstractModel):
    """CreateStarProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 接口返回信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateTawInstanceRequest(AbstractModel):
    """CreateTawInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AreaId: 片区Id，(至少大于0)
        :type AreaId: int
        :param _ChargeType: 计费类型, (1=后付费)
        :type ChargeType: int
        :param _DataRetentionDays: 数据保存时间，(至少大于0)
        :type DataRetentionDays: int
        :param _InstanceName: 实例名称，(最大长度不超过255字节)
        :type InstanceName: str
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _InstanceDesc: 实例描述，(最大长度不超过1024字节)
        :type InstanceDesc: str
        :param _CountNum: 每天数据上报量，（不作量级限制）
        :type CountNum: str
        :param _PeriodRetain: 数据存储时长计费
        :type PeriodRetain: str
        :param _BuyingChannel: 实例购买渠道("cdn" 等)
        :type BuyingChannel: str
        :param _ResourcePackageType: 预付费资源包类型(仅预付费需要)
        :type ResourcePackageType: int
        :param _ResourcePackageNum: 预付费资源包数量(仅预付费需要)
        :type ResourcePackageNum: int
        :param _InstanceType: 实例类型 1:原web相关类型 2:app端类型
        :type InstanceType: int
        """
        self._AreaId = None
        self._ChargeType = None
        self._DataRetentionDays = None
        self._InstanceName = None
        self._Tags = None
        self._InstanceDesc = None
        self._CountNum = None
        self._PeriodRetain = None
        self._BuyingChannel = None
        self._ResourcePackageType = None
        self._ResourcePackageNum = None
        self._InstanceType = None

    @property
    def AreaId(self):
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def DataRetentionDays(self):
        return self._DataRetentionDays

    @DataRetentionDays.setter
    def DataRetentionDays(self, DataRetentionDays):
        self._DataRetentionDays = DataRetentionDays

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceDesc(self):
        return self._InstanceDesc

    @InstanceDesc.setter
    def InstanceDesc(self, InstanceDesc):
        self._InstanceDesc = InstanceDesc

    @property
    def CountNum(self):
        return self._CountNum

    @CountNum.setter
    def CountNum(self, CountNum):
        self._CountNum = CountNum

    @property
    def PeriodRetain(self):
        return self._PeriodRetain

    @PeriodRetain.setter
    def PeriodRetain(self, PeriodRetain):
        self._PeriodRetain = PeriodRetain

    @property
    def BuyingChannel(self):
        return self._BuyingChannel

    @BuyingChannel.setter
    def BuyingChannel(self, BuyingChannel):
        self._BuyingChannel = BuyingChannel

    @property
    def ResourcePackageType(self):
        return self._ResourcePackageType

    @ResourcePackageType.setter
    def ResourcePackageType(self, ResourcePackageType):
        self._ResourcePackageType = ResourcePackageType

    @property
    def ResourcePackageNum(self):
        return self._ResourcePackageNum

    @ResourcePackageNum.setter
    def ResourcePackageNum(self, ResourcePackageNum):
        self._ResourcePackageNum = ResourcePackageNum

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._AreaId = params.get("AreaId")
        self._ChargeType = params.get("ChargeType")
        self._DataRetentionDays = params.get("DataRetentionDays")
        self._InstanceName = params.get("InstanceName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceDesc = params.get("InstanceDesc")
        self._CountNum = params.get("CountNum")
        self._PeriodRetain = params.get("PeriodRetain")
        self._BuyingChannel = params.get("BuyingChannel")
        self._ResourcePackageType = params.get("ResourcePackageType")
        self._ResourcePackageNum = params.get("ResourcePackageNum")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTawInstanceResponse(AbstractModel):
    """CreateTawInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _DealName: 预付费订单 id
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._DealName = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateWhitelistRequest(AbstractModel):
    """CreateWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID：taw-123
        :type InstanceID: str
        :param _Remark: 备注（暂未作字节数限制）
        :type Remark: str
        :param _WhitelistUin: uin：业务方标识
        :type WhitelistUin: str
        :param _Aid: 业务方标识
        :type Aid: str
        """
        self._InstanceID = None
        self._Remark = None
        self._WhitelistUin = None
        self._Aid = None

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def WhitelistUin(self):
        return self._WhitelistUin

    @WhitelistUin.setter
    def WhitelistUin(self, WhitelistUin):
        self._WhitelistUin = WhitelistUin

    @property
    def Aid(self):
        return self._Aid

    @Aid.setter
    def Aid(self, Aid):
        self._Aid = Aid


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Remark = params.get("Remark")
        self._WhitelistUin = params.get("WhitelistUin")
        self._Aid = params.get("Aid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWhitelistResponse(AbstractModel):
    """CreateWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 消息
        :type Msg: str
        :param _ID: 白名单ID
        :type ID: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._ID = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._ID = params.get("ID")
        self._RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要删除的实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
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
        :param _ID: 需要删除的项目 ID
        :type ID: int
        """
        self._ID = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
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
        :param _Msg: 操作信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteReleaseFileRequest(AbstractModel):
    """DeleteReleaseFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 文件 id
        :type ID: int
        """
        self._ID = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReleaseFileResponse(AbstractModel):
    """DeleteReleaseFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 接口请求返回字符串
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteStarProjectRequest(AbstractModel):
    """DeleteStarProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID：taw-123
        :type InstanceID: str
        :param _ID: 项目ID
        :type ID: int
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStarProjectResponse(AbstractModel):
    """DeleteStarProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteWhitelistRequest(AbstractModel):
    """DeleteWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 名单ID
        :type ID: str
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWhitelistResponse(AbstractModel):
    """DeleteWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 消息success
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeAppDimensionMetricsRequest(AbstractModel):
    """DescribeAppDimensionMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: app 项目ID
        :type ProjectID: int
        :param _From: 查询的表名
        :type From: str
        :param _Fields: 查询指标 fields
        :type Fields: str
        :param _Filter: 查询的过滤条件
        :type Filter: str
        :param _FilterSimple: 查询简单过滤条件
        :type FilterSimple: str
        :param _GroupBy: group by 条件
        :type GroupBy: list of str
        :param _OrderBy: order by 条件
        :type OrderBy: list of str
        :param _Limit: limit 参数
        :type Limit: int
        :param _Offset: offset 参数
        :type Offset: int
        :param _BusinessContext: 业务上下文参数
        :type BusinessContext: str
        """
        self._ProjectID = None
        self._From = None
        self._Fields = None
        self._Filter = None
        self._FilterSimple = None
        self._GroupBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._BusinessContext = None

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def FilterSimple(self):
        return self._FilterSimple

    @FilterSimple.setter
    def FilterSimple(self, FilterSimple):
        self._FilterSimple = FilterSimple

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def BusinessContext(self):
        return self._BusinessContext

    @BusinessContext.setter
    def BusinessContext(self, BusinessContext):
        self._BusinessContext = BusinessContext


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._From = params.get("From")
        self._Fields = params.get("Fields")
        self._Filter = params.get("Filter")
        self._FilterSimple = params.get("FilterSimple")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BusinessContext = params.get("BusinessContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppDimensionMetricsResponse(AbstractModel):
    """DescribeAppDimensionMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询数据返回
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeAppMetricsDataRequest(AbstractModel):
    """DescribeAppMetricsData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: app 项目ID
        :type ProjectID: int
        :param _From: 查询的表名
        :type From: str
        :param _Fields: 查询指标 field
        :type Fields: str
        :param _Filter: 查询的过滤条件
        :type Filter: str
        :param _FilterSimple: 查询简单过滤条件
        :type FilterSimple: str
        :param _GroupBy: group by 条件
        :type GroupBy: list of str
        :param _OrderBy: order by 条件
        :type OrderBy: list of str
        :param _Limit: limit 参数
        :type Limit: int
        :param _Offset: offset 参数
        :type Offset: int
        :param _GroupByModifier: group by 参数
        :type GroupByModifier: str
        """
        self._ProjectID = None
        self._From = None
        self._Fields = None
        self._Filter = None
        self._FilterSimple = None
        self._GroupBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._GroupByModifier = None

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def FilterSimple(self):
        return self._FilterSimple

    @FilterSimple.setter
    def FilterSimple(self, FilterSimple):
        self._FilterSimple = FilterSimple

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def GroupByModifier(self):
        return self._GroupByModifier

    @GroupByModifier.setter
    def GroupByModifier(self, GroupByModifier):
        self._GroupByModifier = GroupByModifier


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._From = params.get("From")
        self._Fields = params.get("Fields")
        self._Filter = params.get("Filter")
        self._FilterSimple = params.get("FilterSimple")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._GroupByModifier = params.get("GroupByModifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppMetricsDataResponse(AbstractModel):
    """DescribeAppMetricsData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询数据返回
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeAppSingleCaseDetailListRequest(AbstractModel):
    """DescribeAppSingleCaseDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: app 项目ID
        :type ProjectID: int
        :param _From: 查询的表名
        :type From: str
        :param _Fields: 查询指标 field
        :type Fields: str
        :param _Filter: 查询的过滤条件
        :type Filter: str
        :param _FilterSimple: 查询简单过滤条件
        :type FilterSimple: str
        :param _GroupBy: group by 条件
        :type GroupBy: list of str
        :param _OrderBy: order by 条件
        :type OrderBy: list of str
        :param _Limit: limit 参数
        :type Limit: int
        :param _Offset: offset 参数
        :type Offset: int
        """
        self._ProjectID = None
        self._From = None
        self._Fields = None
        self._Filter = None
        self._FilterSimple = None
        self._GroupBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def FilterSimple(self):
        return self._FilterSimple

    @FilterSimple.setter
    def FilterSimple(self, FilterSimple):
        self._FilterSimple = FilterSimple

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._From = params.get("From")
        self._Fields = params.get("Fields")
        self._Filter = params.get("Filter")
        self._FilterSimple = params.get("FilterSimple")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppSingleCaseDetailListResponse(AbstractModel):
    """DescribeAppSingleCaseDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询数据返回
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeAppSingleCaseListRequest(AbstractModel):
    """DescribeAppSingleCaseList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: app 项目 ID
        :type ProjectID: int
        :param _From: 查询的表名
        :type From: str
        :param _Fields: 查询指标 field
        :type Fields: str
        :param _Filter: 查询的过滤条件
        :type Filter: str
        :param _FilterSimple: 查询简单过滤条件
        :type FilterSimple: str
        :param _GroupBy: group by 条件
        :type GroupBy: list of str
        :param _OrderBy: order by 条件
        :type OrderBy: list of str
        :param _Limit: limit 参数
        :type Limit: int
        :param _Offset: offset 参数
        :type Offset: int
        """
        self._ProjectID = None
        self._From = None
        self._Fields = None
        self._Filter = None
        self._FilterSimple = None
        self._GroupBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def FilterSimple(self):
        return self._FilterSimple

    @FilterSimple.setter
    def FilterSimple(self, FilterSimple):
        self._FilterSimple = FilterSimple

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._From = params.get("From")
        self._Fields = params.get("Fields")
        self._Filter = params.get("Filter")
        self._FilterSimple = params.get("FilterSimple")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppSingleCaseListResponse(AbstractModel):
    """DescribeAppSingleCaseList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询数据返回
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeDataCustomUrlRequest(AbstractModel):
    """DescribeDataCustomUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: top：资源top视图，allcount：性能视图，day：14天数据，condition：条件列表，pagepv：性能视图，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Url: 自定义测速的key的值
        :type Url: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataCustomUrlResponse(AbstractModel):
    """DescribeDataCustomUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataEventUrlRequest(AbstractModel):
    """DescribeDataEventUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，day：14天数据，condition：条件列表，ckuv：获取uv趋势，ckpv：获取pv趋势，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Name: 筛选条件
        :type Name: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Name = None
        self._Env = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Name = params.get("Name")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEventUrlResponse(AbstractModel):
    """DescribeDataEventUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataFetchProjectRequest(AbstractModel):
    """DescribeDataFetchProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间，示例值：1625454840
        :type StartTime: int
        :param _Type: allcount：性能视图，day：14天数据，condition：条件列表，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间，示例值：1625454840
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级（1表示白名单日志，2表示一般日志，4表示错误日志，8表示Promise 错误，16表示Ajax 请求异常，32表示JS 加载异常，64表示图片加载异常，128表示css 加载异常，256表示console.error，512表示音视频资源异常，1024表示retcode 异常，2048表示aegis report，4096表示PV日志，8192表示自定义事件，16384表示小程序 页面不存在，32768表示websocket错误，65536表示js bridge错误）
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        :param _Status: httpcode响应码
        :type Status: str
        :param _Ret: retcode
        :type Ret: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._Status = None
        self._Ret = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._Status = params.get("Status")
        self._Ret = params.get("Ret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchProjectResponse(AbstractModel):
    """DescribeDataFetchProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataFetchUrlInfoRequest(AbstractModel):
    """DescribeDataFetchUrlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: 类型
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlInfoResponse(AbstractModel):
    """DescribeDataFetchUrlInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataFetchUrlRequest(AbstractModel):
    """DescribeDataFetchUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，pagepv：pv视图，day：14天数据，count40x：40X视图，count50x：50X视图，count5xand4x：40∑50视图，top：资源top视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        :param _Status: httpcode响应码
        :type Status: str
        :param _Ret: retcode
        :type Ret: str
        :param _NetStatus: 网络状态
        :type NetStatus: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._Status = None
        self._Ret = None
        self._NetStatus = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def NetStatus(self):
        return self._NetStatus

    @NetStatus.setter
    def NetStatus(self, NetStatus):
        self._NetStatus = NetStatus


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._Status = params.get("Status")
        self._Ret = params.get("Ret")
        self._NetStatus = params.get("NetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlResponse(AbstractModel):
    """DescribeDataFetchUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataLogUrlInfoRequest(AbstractModel):
    """DescribeDataLogUrlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 项目ID
        :type ID: int
        :param _StartTime: 时间戳
        :type StartTime: int
        :param _EndTime: 时间戳
        :type EndTime: int
        """
        self._ID = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlInfoResponse(AbstractModel):
    """DescribeDataLogUrlInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataLogUrlStatisticsRequest(AbstractModel):
    """DescribeDataLogUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: analysis：异常分析，compare：异常列表对比，allcount：性能视图，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Env: 环境区分
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlStatisticsResponse(AbstractModel):
    """DescribeDataLogUrlStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataPerformancePageRequest(AbstractModel):
    """DescribeDataPerformancePage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 项目ID
        :type ID: int
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _Type: pagepv：pv视图，allcount：性能视图，falls：页面加载瀑布图，samp：首屏时间，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :type Type: str
        :param _Level: 日志等级
        :type Level: str
        :param _Isp: 运营商
        :type Isp: str
        :param _Area: 地区
        :type Area: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Platform: 平台
        :type Platform: str
        :param _Device: 机型
        :type Device: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Os: 操作系统
        :type Os: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Brand: 品牌
        :type Brand: str
        :param _From: 来源页面
        :type From: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Env: 环境变量
        :type Env: str
        :param _NetStatus: 网络状态
        :type NetStatus: str
        """
        self._ID = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._Level = None
        self._Isp = None
        self._Area = None
        self._NetType = None
        self._Platform = None
        self._Device = None
        self._VersionNum = None
        self._ExtFirst = None
        self._ExtSecond = None
        self._ExtThird = None
        self._IsAbroad = None
        self._Browser = None
        self._Os = None
        self._Engine = None
        self._Brand = None
        self._From = None
        self._CostType = None
        self._Env = None
        self._NetStatus = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def NetStatus(self):
        return self._NetStatus

    @NetStatus.setter
    def NetStatus(self, NetStatus):
        self._NetStatus = NetStatus


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._Level = params.get("Level")
        self._Isp = params.get("Isp")
        self._Area = params.get("Area")
        self._NetType = params.get("NetType")
        self._Platform = params.get("Platform")
        self._Device = params.get("Device")
        self._VersionNum = params.get("VersionNum")
        self._ExtFirst = params.get("ExtFirst")
        self._ExtSecond = params.get("ExtSecond")
        self._ExtThird = params.get("ExtThird")
        self._IsAbroad = params.get("IsAbroad")
        self._Browser = params.get("Browser")
        self._Os = params.get("Os")
        self._Engine = params.get("Engine")
        self._Brand = params.get("Brand")
        self._From = params.get("From")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        self._NetStatus = params.get("NetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPerformancePageResponse(AbstractModel):
    """DescribeDataPerformancePage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataPvUrlInfoRequest(AbstractModel):
    """DescribeDataPvUrlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: 类型
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlInfoResponse(AbstractModel):
    """DescribeDataPvUrlInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataPvUrlStatisticsRequest(AbstractModel):
    """DescribeDataPvUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，day：14天数据，vp：性能，ckuv：uv，ckpv：pv，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Env: 环境
        :type Env: str
        :param _GroupByType: group by 参数值枚举1:1m  2:5m  3:30m  4:1h 
 5:1d
        :type GroupByType: int
        :param _IsNewData: 1: 查询智研
0: 走旧逻辑，已下线，勿使用
        :type IsNewData: int
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None
        self._GroupByType = None
        self._IsNewData = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def GroupByType(self):
        return self._GroupByType

    @GroupByType.setter
    def GroupByType(self, GroupByType):
        self._GroupByType = GroupByType

    @property
    def IsNewData(self):
        return self._IsNewData

    @IsNewData.setter
    def IsNewData(self, IsNewData):
        self._IsNewData = IsNewData


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        self._GroupByType = params.get("GroupByType")
        self._IsNewData = params.get("IsNewData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlStatisticsResponse(AbstractModel):
    """DescribeDataPvUrlStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataReportCountRequest(AbstractModel):
    """DescribeDataReportCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ReportType: 上报类型（custom，event，log，miniProgramData，performance，pv，speed，webvitals）
        :type ReportType: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ID = None
        self._ReportType = None
        self._InstanceID = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ReportType = params.get("ReportType")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataReportCountResponse(AbstractModel):
    """DescribeDataReportCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataRequest(AbstractModel):
    """DescribeData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 查询字符串
        :type Query: str
        :param _ID: 项目ID
        :type ID: int
        """
        self._Query = None
        self._ID = None

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataResponse(AbstractModel):
    """DescribeData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataSetUrlStatisticsRequest(AbstractModel):
    """DescribeDataSetUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，data：小程序，component：小程序相关，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算
        :type CostType: str
        :param _Env: 环境
        :type Env: str
        :param _PackageType: 获取package
        :type PackageType: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Env = None
        self._PackageType = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        self._PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataSetUrlStatisticsResponse(AbstractModel):
    """DescribeDataSetUrlStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataStaticProjectRequest(AbstractModel):
    """DescribeDataStaticProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，day：14天数据，condition：条件列表，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级（1表示白名单日志，2表示一般日志，4表示错误日志，8表示Promise 错误，16表示Ajax 请求异常，32表示JS 加载异常，64表示图片加载异常，128表示css 加载异常，256表示console.error，512表示音视频资源异常，1024表示retcode 异常，2048表示aegis report，4096表示PV日志，8192表示自定义事件，16384表示小程序 页面不存在，32768表示websocket错误，65536表示js bridge错误）
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算
        :type CostType: str
        :param _Url: 来源
        :type Url: list of str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticProjectResponse(AbstractModel):
    """DescribeDataStaticProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataStaticResourceRequest(AbstractModel):
    """DescribeDataStaticResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: top：资源top视图，count40x：40X视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticResourceResponse(AbstractModel):
    """DescribeDataStaticResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataStaticUrlRequest(AbstractModel):
    """DescribeDataStaticUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: pagepv：性能视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticUrlResponse(AbstractModel):
    """DescribeDataStaticUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataWebVitalsPageRequest(AbstractModel):
    """DescribeDataWebVitalsPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Type: 类型暂无
        :type Type: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算
        :type CostType: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Type = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Env = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Type = params.get("Type")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataWebVitalsPageResponse(AbstractModel):
    """DescribeDataWebVitalsPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeErrorRequest(AbstractModel):
    """DescribeError请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Date: 日期
        :type Date: str
        :param _ID: 项目ID
        :type ID: int
        """
        self._Date = None
        self._ID = None

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorResponse(AbstractModel):
    """DescribeError返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 内容
        :type Content: str
        :param _ID: 项目ID
        :type ID: int
        :param _CreateTime: 时间
        :type CreateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._ID = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._ID = params.get("ID")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class DescribeProjectLimitsRequest(AbstractModel):
    """DescribeProjectLimits请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: 项目ID
        :type ProjectID: int
        """
        self._ProjectID = None

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectLimitsResponse(AbstractModel):
    """DescribeProjectLimits返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectLimitSet: 上报率数组列表
        :type ProjectLimitSet: list of ProjectLimit
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectLimitSet = None
        self._RequestId = None

    @property
    def ProjectLimitSet(self):
        return self._ProjectLimitSet

    @ProjectLimitSet.setter
    def ProjectLimitSet(self, ProjectLimitSet):
        self._ProjectLimitSet = ProjectLimitSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProjectLimitSet") is not None:
            self._ProjectLimitSet = []
            for item in params.get("ProjectLimitSet"):
                obj = ProjectLimit()
                obj._deserialize(item)
                self._ProjectLimitSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页每页数目，整型
        :type Limit: int
        :param _Offset: 分页页码，整型
        :type Offset: int
        :param _Filters: 过滤参数；demo模式传{"Name": "IsDemo", "Values":["1"]}
        :type Filters: list of Filter
        :param _IsDemo: 该参数已废弃，demo模式请在Filters内注明
        :type IsDemo: int
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._IsDemo = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def IsDemo(self):
        return self._IsDemo

    @IsDemo.setter
    def IsDemo(self, IsDemo):
        self._IsDemo = IsDemo


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._IsDemo = params.get("IsDemo")
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
        :param _TotalCount: 列表总数
        :type TotalCount: int
        :param _ProjectSet: 项目列表
        :type ProjectSet: list of RumProject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProjectSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProjectSet(self):
        return self._ProjectSet

    @ProjectSet.setter
    def ProjectSet(self, ProjectSet):
        self._ProjectSet = ProjectSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ProjectSet") is not None:
            self._ProjectSet = []
            for item in params.get("ProjectSet"):
                obj = RumProject()
                obj._deserialize(item)
                self._ProjectSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePvListRequest(AbstractModel):
    """DescribePvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: ID
        :type ProjectId: int
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _Dimension: 获取day：d，   获取min则不填
        :type Dimension: str
        """
        self._ProjectId = None
        self._EndTime = None
        self._StartTime = None
        self._Dimension = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Dimension(self):
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePvListResponse(AbstractModel):
    """DescribePvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectPvSet: pv列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectPvSet: list of RumPvInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectPvSet = None
        self._RequestId = None

    @property
    def ProjectPvSet(self):
        return self._ProjectPvSet

    @ProjectPvSet.setter
    def ProjectPvSet(self, ProjectPvSet):
        self._ProjectPvSet = ProjectPvSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProjectPvSet") is not None:
            self._ProjectPvSet = []
            for item in params.get("ProjectPvSet"):
                obj = RumPvInfo()
                obj._deserialize(item)
                self._ProjectPvSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReleaseFileSignRequest(AbstractModel):
    """DescribeReleaseFileSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Timeout: 超时时间，不填默认是 5 分钟
        :type Timeout: int
        :param _FileType: bucket类型，不填默认1:web，2:app
        :type FileType: int
        """
        self._Timeout = None
        self._FileType = None

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._Timeout = params.get("Timeout")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseFileSignResponse(AbstractModel):
    """DescribeReleaseFileSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretKey: 临时密钥key
        :type SecretKey: str
        :param _SecretID: 临时密钥 id
        :type SecretID: str
        :param _SessionToken: 临时密钥临时 token
        :type SessionToken: str
        :param _StartTime: 开始时间戳
        :type StartTime: int
        :param _ExpiredTime: 过期时间戳
        :type ExpiredTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretKey = None
        self._SecretID = None
        self._SessionToken = None
        self._StartTime = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SecretID(self):
        return self._SecretID

    @SecretID.setter
    def SecretID(self, SecretID):
        self._SecretID = SecretID

    @property
    def SessionToken(self):
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._SecretID = params.get("SecretID")
        self._SessionToken = params.get("SessionToken")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class DescribeReleaseFilesRequest(AbstractModel):
    """DescribeReleaseFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: 项目 id
        :type ProjectID: int
        :param _FileVersion: 文件版本
        :type FileVersion: str
        """
        self._ProjectID = None
        self._FileVersion = None

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def FileVersion(self):
        return self._FileVersion

    @FileVersion.setter
    def FileVersion(self, FileVersion):
        self._FileVersion = FileVersion


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._FileVersion = params.get("FileVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseFilesResponse(AbstractModel):
    """DescribeReleaseFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Files: 文件信息列表
        :type Files: list of ReleaseFile
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Files = None
        self._RequestId = None

    @property
    def Files(self):
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = ReleaseFile()
                obj._deserialize(item)
                self._Files.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRumGroupLogRequest(AbstractModel):
    """DescribeRumGroupLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderBy: 排序方式  desc  asc（必填）
        :type OrderBy: str
        :param _StartTime: 开始时间（必填）
        :type StartTime: str
        :param _Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param _Page: 页数，第几页
        :type Page: int
        :param _Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param _EndTime: 结束时间（必填）
        :type EndTime: str
        :param _ID: 项目ID（必填）
        :type ID: int
        :param _GroupField: 聚合字段
        :type GroupField: str
        """
        self._OrderBy = None
        self._StartTime = None
        self._Limit = None
        self._Page = None
        self._Query = None
        self._EndTime = None
        self._ID = None
        self._GroupField = None

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def GroupField(self):
        return self._GroupField

    @GroupField.setter
    def GroupField(self, GroupField):
        self._GroupField = GroupField


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Page = params.get("Page")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._GroupField = params.get("GroupField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumGroupLogResponse(AbstractModel):
    """DescribeRumGroupLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumLogExportRequest(AbstractModel):
    """DescribeRumLogExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 导出标识name
        :type Name: str
        :param _StartTime: 开始时间（必填）
        :type StartTime: str
        :param _Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param _EndTime: 结束时间（必填）
        :type EndTime: str
        :param _ID: 项目ID（必填）
        :type ID: int
        :param _Fields: field条件
        :type Fields: list of str
        """
        self._Name = None
        self._StartTime = None
        self._Query = None
        self._EndTime = None
        self._ID = None
        self._Fields = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._Fields = params.get("Fields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogExportResponse(AbstractModel):
    """DescribeRumLogExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumLogExportsRequest(AbstractModel):
    """DescribeRumLogExports请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 页面大小
        :type PageSize: int
        :param _PageNum: 页数，第几页
        :type PageNum: int
        :param _ID: 项目ID（必填）
        :type ID: int
        """
        self._PageSize = None
        self._PageNum = None
        self._ID = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogExportsResponse(AbstractModel):
    """DescribeRumLogExports返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumLogListRequest(AbstractModel):
    """DescribeRumLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderBy: 排序方式  desc  asc（必填）
        :type OrderBy: str
        :param _StartTime: 开始时间（必填）格式为时间戳 毫秒
        :type StartTime: str
        :param _Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param _Page: 页数，第几页
        :type Page: int
        :param _Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param _EndTime: 结束时间（必填）格式为时间戳 毫秒
        :type EndTime: str
        :param _ID: 项目ID（必填）
        :type ID: int
        """
        self._OrderBy = None
        self._StartTime = None
        self._Limit = None
        self._Page = None
        self._Query = None
        self._EndTime = None
        self._ID = None

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Page = params.get("Page")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogListResponse(AbstractModel):
    """DescribeRumLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumStatsLogListRequest(AbstractModel):
    """DescribeRumStatsLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间（必填）
        :type StartTime: str
        :param _Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param _Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param _EndTime: 结束时间（必填）
        :type EndTime: str
        :param _ID: 项目ID（必填）
        :type ID: int
        """
        self._StartTime = None
        self._Limit = None
        self._Query = None
        self._EndTime = None
        self._ID = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumStatsLogListResponse(AbstractModel):
    """DescribeRumStatsLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeScoresRequest(AbstractModel):
    """DescribeScores请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _ID: 项目ID
        :type ID: int
        :param _IsDemo: 该参数已废弃
        :type IsDemo: int
        """
        self._EndTime = None
        self._StartTime = None
        self._ID = None
        self._IsDemo = None

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def IsDemo(self):
        return self._IsDemo

    @IsDemo.setter
    def IsDemo(self, IsDemo):
        self._IsDemo = IsDemo


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._ID = params.get("ID")
        self._IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScoresResponse(AbstractModel):
    """DescribeScores返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScoreSet: 数组
        :type ScoreSet: list of ScoreInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScoreSet = None
        self._RequestId = None

    @property
    def ScoreSet(self):
        return self._ScoreSet

    @ScoreSet.setter
    def ScoreSet(self, ScoreSet):
        self._ScoreSet = ScoreSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ScoreSet") is not None:
            self._ScoreSet = []
            for item in params.get("ScoreSet"):
                obj = ScoreInfo()
                obj._deserialize(item)
                self._ScoreSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTawAreasRequest(AbstractModel):
    """DescribeTawAreas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AreaIds: 片区Id
        :type AreaIds: list of int
        :param _AreaKeys: 片区Key
        :type AreaKeys: list of str
        :param _Limit: 分页Limit
        :type Limit: int
        :param _AreaStatuses: 片区状态(1=有效，2=无效)
        :type AreaStatuses: list of int
        :param _Offset: 分页Offset
        :type Offset: int
        """
        self._AreaIds = None
        self._AreaKeys = None
        self._Limit = None
        self._AreaStatuses = None
        self._Offset = None

    @property
    def AreaIds(self):
        return self._AreaIds

    @AreaIds.setter
    def AreaIds(self, AreaIds):
        self._AreaIds = AreaIds

    @property
    def AreaKeys(self):
        return self._AreaKeys

    @AreaKeys.setter
    def AreaKeys(self, AreaKeys):
        self._AreaKeys = AreaKeys

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AreaStatuses(self):
        return self._AreaStatuses

    @AreaStatuses.setter
    def AreaStatuses(self, AreaStatuses):
        self._AreaStatuses = AreaStatuses

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._AreaIds = params.get("AreaIds")
        self._AreaKeys = params.get("AreaKeys")
        self._Limit = params.get("Limit")
        self._AreaStatuses = params.get("AreaStatuses")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTawAreasResponse(AbstractModel):
    """DescribeTawAreas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 片区总数
        :type TotalCount: int
        :param _AreaSet: 片区列表
        :type AreaSet: list of RumAreaInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AreaSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AreaSet(self):
        return self._AreaSet

    @AreaSet.setter
    def AreaSet(self, AreaSet):
        self._AreaSet = AreaSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AreaSet") is not None:
            self._AreaSet = []
            for item in params.get("AreaSet"):
                obj = RumAreaInfo()
                obj._deserialize(item)
                self._AreaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTawInstancesRequest(AbstractModel):
    """DescribeTawInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChargeStatuses: 计费状态
        :type ChargeStatuses: list of int
        :param _ChargeTypes: 计费类型
        :type ChargeTypes: list of int
        :param _Limit: 分页Limit
        :type Limit: int
        :param _Offset: 分页Offset
        :type Offset: int
        :param _AreaIds: 片区Id
        :type AreaIds: list of int
        :param _InstanceStatuses: 实例状态(1=创建中，2=运行中，3=异常，4=重启中，5=停止中，6=已停止，7=销毁中，8=已销毁), 该参数已废弃，请在Filters内注明
        :type InstanceStatuses: list of int
        :param _InstanceIds: 实例Id, 该参数已废弃，请在Filters内注明
        :type InstanceIds: list of str
        :param _Filters: 过滤参数；demo模式传{"Name": "IsDemo", "Values":["1"]}
        :type Filters: list of Filter
        :param _IsDemo: 该参数已废弃，demo模式请在Filters内注明
        :type IsDemo: int
        """
        self._ChargeStatuses = None
        self._ChargeTypes = None
        self._Limit = None
        self._Offset = None
        self._AreaIds = None
        self._InstanceStatuses = None
        self._InstanceIds = None
        self._Filters = None
        self._IsDemo = None

    @property
    def ChargeStatuses(self):
        return self._ChargeStatuses

    @ChargeStatuses.setter
    def ChargeStatuses(self, ChargeStatuses):
        self._ChargeStatuses = ChargeStatuses

    @property
    def ChargeTypes(self):
        return self._ChargeTypes

    @ChargeTypes.setter
    def ChargeTypes(self, ChargeTypes):
        self._ChargeTypes = ChargeTypes

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AreaIds(self):
        return self._AreaIds

    @AreaIds.setter
    def AreaIds(self, AreaIds):
        self._AreaIds = AreaIds

    @property
    def InstanceStatuses(self):
        return self._InstanceStatuses

    @InstanceStatuses.setter
    def InstanceStatuses(self, InstanceStatuses):
        self._InstanceStatuses = InstanceStatuses

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def IsDemo(self):
        return self._IsDemo

    @IsDemo.setter
    def IsDemo(self, IsDemo):
        self._IsDemo = IsDemo


    def _deserialize(self, params):
        self._ChargeStatuses = params.get("ChargeStatuses")
        self._ChargeTypes = params.get("ChargeTypes")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AreaIds = params.get("AreaIds")
        self._InstanceStatuses = params.get("InstanceStatuses")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTawInstancesResponse(AbstractModel):
    """DescribeTawInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSet: 实例列表
        :type InstanceSet: list of RumInstanceInfo
        :param _TotalCount: 实例总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = RumInstanceInfo()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUvListRequest(AbstractModel):
    """DescribeUvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: ID
        :type ProjectId: int
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _Dimension: 获取day：d，   min:m
        :type Dimension: str
        """
        self._ProjectId = None
        self._EndTime = None
        self._StartTime = None
        self._Dimension = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Dimension(self):
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUvListResponse(AbstractModel):
    """DescribeUvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectUvSet: uv列表
        :type ProjectUvSet: list of RumUvInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectUvSet = None
        self._RequestId = None

    @property
    def ProjectUvSet(self):
        return self._ProjectUvSet

    @ProjectUvSet.setter
    def ProjectUvSet(self, ProjectUvSet):
        self._ProjectUvSet = ProjectUvSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProjectUvSet") is not None:
            self._ProjectUvSet = []
            for item in params.get("ProjectUvSet"):
                obj = RumUvInfo()
                obj._deserialize(item)
                self._ProjectUvSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWhitelistsRequest(AbstractModel):
    """DescribeWhitelists请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例instance-ID
        :type InstanceID: str
        """
        self._InstanceID = None

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhitelistsResponse(AbstractModel):
    """DescribeWhitelists返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WhitelistSet: 白名单列表
        :type WhitelistSet: list of Whitelist
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WhitelistSet = None
        self._RequestId = None

    @property
    def WhitelistSet(self):
        return self._WhitelistSet

    @WhitelistSet.setter
    def WhitelistSet(self, WhitelistSet):
        self._WhitelistSet = WhitelistSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WhitelistSet") is not None:
            self._WhitelistSet = []
            for item in params.get("WhitelistSet"):
                obj = Whitelist()
                obj._deserialize(item)
                self._WhitelistSet.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    · 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    · 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Values: 一个或者多个过滤值。
        :type Values: list of str
        :param _Name: 过滤键的名称。
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 要修改的实例id
        :type InstanceId: str
        :param _InstanceName: 新的实例名称(长度最大不超过255)
        :type InstanceName: str
        :param _InstanceDesc: 新的实例描述(长度最大不超过1024)
        :type InstanceDesc: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceDesc = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceDesc(self):
        return self._InstanceDesc

    @InstanceDesc.setter
    def InstanceDesc(self, InstanceDesc):
        self._InstanceDesc = InstanceDesc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceDesc = params.get("InstanceDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyProjectLimitRequest(AbstractModel):
    """ModifyProjectLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: 项目ID
        :type ProjectID: int
        :param _ProjectInterface: 项目接口
        :type ProjectInterface: str
        :param _ReportRate: 上报比例   10代表10%
        :type ReportRate: int
        :param _ReportType: 上报类型 1：比例  2：上报量
        :type ReportType: int
        :param _ID: 主键ID
        :type ID: int
        """
        self._ProjectID = None
        self._ProjectInterface = None
        self._ReportRate = None
        self._ReportType = None
        self._ID = None

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def ProjectInterface(self):
        return self._ProjectInterface

    @ProjectInterface.setter
    def ProjectInterface(self, ProjectInterface):
        self._ProjectInterface = ProjectInterface

    @property
    def ReportRate(self):
        return self._ReportRate

    @ReportRate.setter
    def ReportRate(self, ReportRate):
        self._ReportRate = ReportRate

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._ProjectInterface = params.get("ProjectInterface")
        self._ReportRate = params.get("ReportRate")
        self._ReportType = params.get("ReportType")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectLimitResponse(AbstractModel):
    """ModifyProjectLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 项目 id
        :type ID: int
        :param _Name: 应用名称(可选，不为空且最长为 200字符)
        :type Name: str
        :param _URL: 项目网页地址(可选，最长为 256)
        :type URL: str
        :param _Repo: 项目仓库地址(可选，最长为 256)
        :type Repo: str
        :param _InstanceID: 项目需要转移到的实例 id(可选)
        :type InstanceID: str
        :param _Rate: 项目采样率(可选)
        :type Rate: str
        :param _EnableURLGroup: 是否开启聚类(可选)
        :type EnableURLGroup: int
        :param _Type: 项目类型(可接受值为 "web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param _Desc: 应用描述(可选，最长为 1000字符)
        :type Desc: str
        """
        self._ID = None
        self._Name = None
        self._URL = None
        self._Repo = None
        self._InstanceID = None
        self._Rate = None
        self._EnableURLGroup = None
        self._Type = None
        self._Desc = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Repo(self):
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def EnableURLGroup(self):
        return self._EnableURLGroup

    @EnableURLGroup.setter
    def EnableURLGroup(self, EnableURLGroup):
        self._EnableURLGroup = EnableURLGroup

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._URL = params.get("URL")
        self._Repo = params.get("Repo")
        self._InstanceID = params.get("InstanceID")
        self._Rate = params.get("Rate")
        self._EnableURLGroup = params.get("EnableURLGroup")
        self._Type = params.get("Type")
        self._Desc = params.get("Desc")
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
        :param _Msg: 操作信息
        :type Msg: str
        :param _ID: 项目id
        :type ID: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._ID = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._ID = params.get("ID")
        self._RequestId = params.get("RequestId")


class ProjectLimit(AbstractModel):
    """项目接口限制类型

    """

    def __init__(self):
        r"""
        :param _ProjectInterface: 接口
        :type ProjectInterface: str
        :param _ReportRate: 上报率
        :type ReportRate: int
        :param _ReportType: 上报类型 1：上报率  2：上报量限制
        :type ReportType: int
        :param _ID: 主键ID
        :type ID: int
        :param _ProjectID: 项目ID
        :type ProjectID: int
        """
        self._ProjectInterface = None
        self._ReportRate = None
        self._ReportType = None
        self._ID = None
        self._ProjectID = None

    @property
    def ProjectInterface(self):
        return self._ProjectInterface

    @ProjectInterface.setter
    def ProjectInterface(self, ProjectInterface):
        self._ProjectInterface = ProjectInterface

    @property
    def ReportRate(self):
        return self._ReportRate

    @ReportRate.setter
    def ReportRate(self, ReportRate):
        self._ReportRate = ReportRate

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID


    def _deserialize(self, params):
        self._ProjectInterface = params.get("ProjectInterface")
        self._ReportRate = params.get("ReportRate")
        self._ReportType = params.get("ReportType")
        self._ID = params.get("ID")
        self._ProjectID = params.get("ProjectID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseFile(AbstractModel):
    """发布文件列表(SOURCEMAP)

    """

    def __init__(self):
        r"""
        :param _Version: 文件版本
        :type Version: str
        :param _FileKey: 文件唯一 key
        :type FileKey: str
        :param _FileName: 文件名
        :type FileName: str
        :param _FileHash: 文件哈希值
        :type FileHash: str
        :param _ID: 文件 id
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        """
        self._Version = None
        self._FileKey = None
        self._FileName = None
        self._FileHash = None
        self._ID = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def FileKey(self):
        return self._FileKey

    @FileKey.setter
    def FileKey(self, FileKey):
        self._FileKey = FileKey

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileHash(self):
        return self._FileHash

    @FileHash.setter
    def FileHash(self, FileHash):
        self._FileHash = FileHash

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._FileKey = params.get("FileKey")
        self._FileName = params.get("FileName")
        self._FileHash = params.get("FileHash")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceRequest(AbstractModel):
    """ResumeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要恢复的实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceResponse(AbstractModel):
    """ResumeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResumeProjectRequest(AbstractModel):
    """ResumeProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 id
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeProjectResponse(AbstractModel):
    """ResumeProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RumAreaInfo(AbstractModel):
    """Rum片区信息

    """

    def __init__(self):
        r"""
        :param _AreaId: 片区Id
        :type AreaId: int
        :param _AreaStatus: 片区状态(1=有效，2=无效)
        :type AreaStatus: int
        :param _AreaName: 片区名称
        :type AreaName: str
        :param _AreaKey: 片区Key
        :type AreaKey: str
        :param _AreaRegionID: 地域码表 id
        :type AreaRegionID: str
        :param _AreaRegionCode: 地域码表 code 如 ap-xxx（xxx 为地域词）
        :type AreaRegionCode: str
        :param _AreaAbbr: 地域缩写
        :type AreaAbbr: str
        """
        self._AreaId = None
        self._AreaStatus = None
        self._AreaName = None
        self._AreaKey = None
        self._AreaRegionID = None
        self._AreaRegionCode = None
        self._AreaAbbr = None

    @property
    def AreaId(self):
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def AreaStatus(self):
        return self._AreaStatus

    @AreaStatus.setter
    def AreaStatus(self, AreaStatus):
        self._AreaStatus = AreaStatus

    @property
    def AreaName(self):
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName

    @property
    def AreaKey(self):
        return self._AreaKey

    @AreaKey.setter
    def AreaKey(self, AreaKey):
        self._AreaKey = AreaKey

    @property
    def AreaRegionID(self):
        return self._AreaRegionID

    @AreaRegionID.setter
    def AreaRegionID(self, AreaRegionID):
        self._AreaRegionID = AreaRegionID

    @property
    def AreaRegionCode(self):
        return self._AreaRegionCode

    @AreaRegionCode.setter
    def AreaRegionCode(self, AreaRegionCode):
        self._AreaRegionCode = AreaRegionCode

    @property
    def AreaAbbr(self):
        return self._AreaAbbr

    @AreaAbbr.setter
    def AreaAbbr(self, AreaAbbr):
        self._AreaAbbr = AreaAbbr


    def _deserialize(self, params):
        self._AreaId = params.get("AreaId")
        self._AreaStatus = params.get("AreaStatus")
        self._AreaName = params.get("AreaName")
        self._AreaKey = params.get("AreaKey")
        self._AreaRegionID = params.get("AreaRegionID")
        self._AreaRegionCode = params.get("AreaRegionCode")
        self._AreaAbbr = params.get("AreaAbbr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumInstanceInfo(AbstractModel):
    """Rum实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceStatus: 实例状态(1=创建中，2=运行中，3=异常，4=重启中，5=停止中，6=已停止，7=已删除)
        :type InstanceStatus: int
        :param _AreaId: 片区Id
        :type AreaId: int
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _ClusterId: 集群Id
        :type ClusterId: int
        :param _InstanceDesc: 实例描述
        :type InstanceDesc: str
        :param _ChargeStatus: 计费状态(1=使用中，2=已过期，3=已销毁，4=分配中，5=分配失败)
        :type ChargeStatus: int
        :param _ChargeType: 计费类型(1=免费版，2=预付费，3=后付费)
        :type ChargeType: int
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _DataRetentionDays: 数据保留时间(天)
        :type DataRetentionDays: int
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _InstanceType: 实例类型 1:原web相关类型 2:app端类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: int
        """
        self._InstanceStatus = None
        self._AreaId = None
        self._Tags = None
        self._InstanceId = None
        self._ClusterId = None
        self._InstanceDesc = None
        self._ChargeStatus = None
        self._ChargeType = None
        self._UpdatedAt = None
        self._DataRetentionDays = None
        self._InstanceName = None
        self._CreatedAt = None
        self._InstanceType = None

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def AreaId(self):
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceDesc(self):
        return self._InstanceDesc

    @InstanceDesc.setter
    def InstanceDesc(self, InstanceDesc):
        self._InstanceDesc = InstanceDesc

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def DataRetentionDays(self):
        return self._DataRetentionDays

    @DataRetentionDays.setter
    def DataRetentionDays(self, DataRetentionDays):
        self._DataRetentionDays = DataRetentionDays

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._InstanceStatus = params.get("InstanceStatus")
        self._AreaId = params.get("AreaId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._ClusterId = params.get("ClusterId")
        self._InstanceDesc = params.get("InstanceDesc")
        self._ChargeStatus = params.get("ChargeStatus")
        self._ChargeType = params.get("ChargeType")
        self._UpdatedAt = params.get("UpdatedAt")
        self._DataRetentionDays = params.get("DataRetentionDays")
        self._InstanceName = params.get("InstanceName")
        self._CreatedAt = params.get("CreatedAt")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumProject(AbstractModel):
    """Rum 项目信息

    """

    def __init__(self):
        r"""
        :param _Name: 项目名
        :type Name: str
        :param _Creator: 创建者 id
        :type Creator: str
        :param _InstanceID: 实例 id
        :type InstanceID: str
        :param _Type: 项目类型
        :type Type: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Repo: 项目仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Repo: str
        :param _URL: 项目网址地址
注意：此字段可能返回 null，表示取不到有效值。
        :type URL: str
        :param _Rate: 项目采样频率
        :type Rate: str
        :param _Key: 项目唯一key（长度 12 位）
        :type Key: str
        :param _EnableURLGroup: 是否开启url聚类
        :type EnableURLGroup: int
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _ID: 项目 ID
        :type ID: int
        :param _InstanceKey: 实例 key
        :type InstanceKey: str
        :param _Desc: 项目描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _IsStar: 是否星标  1:是 0:否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsStar: int
        :param _ProjectStatus: 项目状态(1 创建中，2 运行中，3 异常，4 重启中，5 停止中，6 已停止， 7 销毁中，8 已销毁)
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectStatus: int
        :param _AccessPoint: 日志接入点，用户忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessPoint: str
        """
        self._Name = None
        self._Creator = None
        self._InstanceID = None
        self._Type = None
        self._CreateTime = None
        self._Repo = None
        self._URL = None
        self._Rate = None
        self._Key = None
        self._EnableURLGroup = None
        self._InstanceName = None
        self._ID = None
        self._InstanceKey = None
        self._Desc = None
        self._IsStar = None
        self._ProjectStatus = None
        self._AccessPoint = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Repo(self):
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def EnableURLGroup(self):
        return self._EnableURLGroup

    @EnableURLGroup.setter
    def EnableURLGroup(self, EnableURLGroup):
        self._EnableURLGroup = EnableURLGroup

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceKey(self):
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IsStar(self):
        return self._IsStar

    @IsStar.setter
    def IsStar(self, IsStar):
        self._IsStar = IsStar

    @property
    def ProjectStatus(self):
        return self._ProjectStatus

    @ProjectStatus.setter
    def ProjectStatus(self, ProjectStatus):
        self._ProjectStatus = ProjectStatus

    @property
    def AccessPoint(self):
        return self._AccessPoint

    @AccessPoint.setter
    def AccessPoint(self, AccessPoint):
        self._AccessPoint = AccessPoint


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Creator = params.get("Creator")
        self._InstanceID = params.get("InstanceID")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        self._Repo = params.get("Repo")
        self._URL = params.get("URL")
        self._Rate = params.get("Rate")
        self._Key = params.get("Key")
        self._EnableURLGroup = params.get("EnableURLGroup")
        self._InstanceName = params.get("InstanceName")
        self._ID = params.get("ID")
        self._InstanceKey = params.get("InstanceKey")
        self._Desc = params.get("Desc")
        self._IsStar = params.get("IsStar")
        self._ProjectStatus = params.get("ProjectStatus")
        self._AccessPoint = params.get("AccessPoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumPvInfo(AbstractModel):
    """rum 日志对象

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Pv: pv访问量
注意：此字段可能返回 null，表示取不到有效值。
        :type Pv: str
        :param _CreateTime: 时间
        :type CreateTime: str
        """
        self._ProjectId = None
        self._Pv = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Pv(self):
        return self._Pv

    @Pv.setter
    def Pv(self, Pv):
        self._Pv = Pv

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Pv = params.get("Pv")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumUvInfo(AbstractModel):
    """RumUv 访问量

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Uv: uv访问量
        :type Uv: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._ProjectId = None
        self._Uv = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Uv(self):
        return self._Uv

    @Uv.setter
    def Uv(self, Uv):
        self._Uv = Uv

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Uv = params.get("Uv")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreInfo(AbstractModel):
    """project Score分数实体

    """

    def __init__(self):
        r"""
        :param _StaticDuration: duration
        :type StaticDuration: str
        :param _PagePv: pv
        :type PagePv: str
        :param _ApiFail: 失败
        :type ApiFail: str
        :param _ApiNum: 请求
        :type ApiNum: str
        :param _StaticFail: fail
        :type StaticFail: str
        :param _ProjectID: 项目id
        :type ProjectID: int
        :param _PageUv: uv
        :type PageUv: str
        :param _ApiDuration: 请求次数
        :type ApiDuration: str
        :param _Score: 分数
        :type Score: str
        :param _PageError: error
        :type PageError: str
        :param _StaticNum: num
        :type StaticNum: str
        :param _RecordNum: num
        :type RecordNum: int
        :param _PageDuration: Duration
        :type PageDuration: str
        :param _CreateTime: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._StaticDuration = None
        self._PagePv = None
        self._ApiFail = None
        self._ApiNum = None
        self._StaticFail = None
        self._ProjectID = None
        self._PageUv = None
        self._ApiDuration = None
        self._Score = None
        self._PageError = None
        self._StaticNum = None
        self._RecordNum = None
        self._PageDuration = None
        self._CreateTime = None

    @property
    def StaticDuration(self):
        return self._StaticDuration

    @StaticDuration.setter
    def StaticDuration(self, StaticDuration):
        self._StaticDuration = StaticDuration

    @property
    def PagePv(self):
        return self._PagePv

    @PagePv.setter
    def PagePv(self, PagePv):
        self._PagePv = PagePv

    @property
    def ApiFail(self):
        return self._ApiFail

    @ApiFail.setter
    def ApiFail(self, ApiFail):
        self._ApiFail = ApiFail

    @property
    def ApiNum(self):
        return self._ApiNum

    @ApiNum.setter
    def ApiNum(self, ApiNum):
        self._ApiNum = ApiNum

    @property
    def StaticFail(self):
        return self._StaticFail

    @StaticFail.setter
    def StaticFail(self, StaticFail):
        self._StaticFail = StaticFail

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def PageUv(self):
        return self._PageUv

    @PageUv.setter
    def PageUv(self, PageUv):
        self._PageUv = PageUv

    @property
    def ApiDuration(self):
        return self._ApiDuration

    @ApiDuration.setter
    def ApiDuration(self, ApiDuration):
        self._ApiDuration = ApiDuration

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def PageError(self):
        return self._PageError

    @PageError.setter
    def PageError(self, PageError):
        self._PageError = PageError

    @property
    def StaticNum(self):
        return self._StaticNum

    @StaticNum.setter
    def StaticNum(self, StaticNum):
        self._StaticNum = StaticNum

    @property
    def RecordNum(self):
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def PageDuration(self):
        return self._PageDuration

    @PageDuration.setter
    def PageDuration(self, PageDuration):
        self._PageDuration = PageDuration

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._StaticDuration = params.get("StaticDuration")
        self._PagePv = params.get("PagePv")
        self._ApiFail = params.get("ApiFail")
        self._ApiNum = params.get("ApiNum")
        self._StaticFail = params.get("StaticFail")
        self._ProjectID = params.get("ProjectID")
        self._PageUv = params.get("PageUv")
        self._ApiDuration = params.get("ApiDuration")
        self._Score = params.get("Score")
        self._PageError = params.get("PageError")
        self._StaticNum = params.get("StaticNum")
        self._RecordNum = params.get("RecordNum")
        self._PageDuration = params.get("PageDuration")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceRequest(AbstractModel):
    """StopInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要停止的实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceResponse(AbstractModel):
    """StopInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopProjectRequest(AbstractModel):
    """StopProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 id
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopProjectResponse(AbstractModel):
    """StopProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签key
        :type Key: str
        :param _Value: 标签value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Whitelist(AbstractModel):
    """白名单

    """

    def __init__(self):
        r"""
        :param _Remark: 备注
        :type Remark: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _Ttl: 截止时间
        :type Ttl: str
        :param _ID: 白名单自增ID
        :type ID: str
        :param _WhitelistUin: 业务唯一标识
        :type WhitelistUin: str
        :param _CreateUser: 创建者ID
        :type CreateUser: str
        :param _Aid: aid标识
        :type Aid: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._Remark = None
        self._InstanceID = None
        self._Ttl = None
        self._ID = None
        self._WhitelistUin = None
        self._CreateUser = None
        self._Aid = None
        self._CreateTime = None

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Ttl(self):
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def WhitelistUin(self):
        return self._WhitelistUin

    @WhitelistUin.setter
    def WhitelistUin(self, WhitelistUin):
        self._WhitelistUin = WhitelistUin

    @property
    def CreateUser(self):
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def Aid(self):
        return self._Aid

    @Aid.setter
    def Aid(self, Aid):
        self._Aid = Aid

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Remark = params.get("Remark")
        self._InstanceID = params.get("InstanceID")
        self._Ttl = params.get("Ttl")
        self._ID = params.get("ID")
        self._WhitelistUin = params.get("WhitelistUin")
        self._CreateUser = params.get("CreateUser")
        self._Aid = params.get("Aid")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        