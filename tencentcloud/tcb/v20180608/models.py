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


class ActivityInfoItem(AbstractModel):
    """活动信息

    """

    def __init__(self):
        r"""
        :param _ActivityId: 活动id
        :type ActivityId: int
        :param _CreateTime: 记录插入时间
        :type CreateTime: str
        :param _UpdateTime: 记录最后一次变更时间
        :type UpdateTime: str
        :param _StartTime: 活动开始时间
        :type StartTime: str
        :param _ExpireTime: 活动结束时间
        :type ExpireTime: str
        :param _Tag: 自定义备注信息
        :type Tag: str
        """
        self._ActivityId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._StartTime = None
        self._ExpireTime = None
        self._Tag = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivityRecordItem(AbstractModel):
    """活动详情

    """

    def __init__(self):
        r"""
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _ActivityId: 活动id
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityId: int
        :param _Status: 自定义状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _SubStatus: 自定义子状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubStatus: str
        :param _SubStatusInt: 整型子状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubStatusInt: int
        :param _IsDeleted: 是否软删除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDeleted: bool
        """
        self._Uin = None
        self._ActivityId = None
        self._Status = None
        self._SubStatus = None
        self._SubStatusInt = None
        self._IsDeleted = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubStatus(self):
        return self._SubStatus

    @SubStatus.setter
    def SubStatus(self, SubStatus):
        self._SubStatus = SubStatus

    @property
    def SubStatusInt(self):
        return self._SubStatusInt

    @SubStatusInt.setter
    def SubStatusInt(self, SubStatusInt):
        self._SubStatusInt = SubStatusInt

    @property
    def IsDeleted(self):
        return self._IsDeleted

    @IsDeleted.setter
    def IsDeleted(self, IsDeleted):
        self._IsDeleted = IsDeleted


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._ActivityId = params.get("ActivityId")
        self._Status = params.get("Status")
        self._SubStatus = params.get("SubStatus")
        self._SubStatusInt = params.get("SubStatusInt")
        self._IsDeleted = params.get("IsDeleted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthDomain(AbstractModel):
    """合法域名

    """

    def __init__(self):
        r"""
        :param _Id: 域名ID
        :type Id: str
        :param _Domain: 域名
        :type Domain: str
        :param _Type: 域名类型。包含以下取值：
<li>SYSTEM</li>
<li>USER</li>
        :type Type: str
        :param _Status: 状态。包含以下取值：
<li>ENABLE</li>
<li>DISABLE</li>
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._Id = None
        self._Domain = None
        self._Type = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._Type = params.get("Type")
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
        


class BaasPackageInfo(AbstractModel):
    """新套餐套餐详情

    """

    def __init__(self):
        r"""
        :param _PackageName: DAU产品套餐ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param _PackageTitle: DAU套餐中文名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTitle: str
        :param _GroupName: 套餐分组
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _GroupTitle: 套餐分组中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupTitle: str
        :param _BillTags: json格式化计费标签，例如：
{"pid":2, "cids":{"create": 2, "renew": 2, "modify": 2}, "productCode":"p_tcb_mp", "subProductCode":"sp_tcb_mp_cloudbase_dau"}
注意：此字段可能返回 null，表示取不到有效值。
        :type BillTags: str
        :param _ResourceLimit: json格式化用户资源限制，例如：
{"Qps":1000,"InvokeNum":{"TimeUnit":"m", "Unit":"万次", "MaxSize": 100},"Capacity":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}, "Cdn":{"Flux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}, "BackFlux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}},"Scf":{"Concurrency":1000,"OutFlux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100},"MemoryUse":{"TimeUnit":"m", "Unit":"WGBS", "MaxSize": 100000}}}
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceLimit: str
        :param _AdvanceLimit: json格式化高级限制，例如：
{"CMSEnable":false,"ProvisionedConcurrencyMem":512000, "PictureProcessing":false, "SecurityAudit":false, "RealTimePush":false, "TemplateMessageBatchPush":false, "Payment":false}
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceLimit: str
        :param _PackageDescription: 套餐描述
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageDescription: str
        :param _IsExternal: 是否对外展示
注意：此字段可能返回 null，表示取不到有效值。
        :type IsExternal: bool
        """
        self._PackageName = None
        self._PackageTitle = None
        self._GroupName = None
        self._GroupTitle = None
        self._BillTags = None
        self._ResourceLimit = None
        self._AdvanceLimit = None
        self._PackageDescription = None
        self._IsExternal = None

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageTitle(self):
        return self._PackageTitle

    @PackageTitle.setter
    def PackageTitle(self, PackageTitle):
        self._PackageTitle = PackageTitle

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupTitle(self):
        return self._GroupTitle

    @GroupTitle.setter
    def GroupTitle(self, GroupTitle):
        self._GroupTitle = GroupTitle

    @property
    def BillTags(self):
        return self._BillTags

    @BillTags.setter
    def BillTags(self, BillTags):
        self._BillTags = BillTags

    @property
    def ResourceLimit(self):
        return self._ResourceLimit

    @ResourceLimit.setter
    def ResourceLimit(self, ResourceLimit):
        self._ResourceLimit = ResourceLimit

    @property
    def AdvanceLimit(self):
        return self._AdvanceLimit

    @AdvanceLimit.setter
    def AdvanceLimit(self, AdvanceLimit):
        self._AdvanceLimit = AdvanceLimit

    @property
    def PackageDescription(self):
        return self._PackageDescription

    @PackageDescription.setter
    def PackageDescription(self, PackageDescription):
        self._PackageDescription = PackageDescription

    @property
    def IsExternal(self):
        return self._IsExternal

    @IsExternal.setter
    def IsExternal(self, IsExternal):
        self._IsExternal = IsExternal


    def _deserialize(self, params):
        self._PackageName = params.get("PackageName")
        self._PackageTitle = params.get("PackageTitle")
        self._GroupName = params.get("GroupName")
        self._GroupTitle = params.get("GroupTitle")
        self._BillTags = params.get("BillTags")
        self._ResourceLimit = params.get("ResourceLimit")
        self._AdvanceLimit = params.get("AdvanceLimit")
        self._PackageDescription = params.get("PackageDescription")
        self._IsExternal = params.get("IsExternal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackendServiceInfo(AbstractModel):
    """网关服务信息

    """

    def __init__(self):
        r"""
        :param _ServiceName: 服务名称
        :type ServiceName: str
        :param _Status: 服务状态
        :type Status: str
        """
        self._ServiceName = None
        self._Status = None

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BanConfig(AbstractModel):
    """封禁配置

    """

    def __init__(self):
        r"""
        :param _IpWhiteList: ip白名单，支持ipv4、ipv6，支持CIDR
        :type IpWhiteList: list of str
        :param _IpBlackList: ip黑名单，支持ipv4、ipv6，支持CIDR
        :type IpBlackList: list of str
        :param _CountryWhiteList: 地域白名单（国家英文名）
        :type CountryWhiteList: list of str
        :param _CountryBlackList: 地域黑名单（国家英文名）
        :type CountryBlackList: list of str
        """
        self._IpWhiteList = None
        self._IpBlackList = None
        self._CountryWhiteList = None
        self._CountryBlackList = None

    @property
    def IpWhiteList(self):
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def IpBlackList(self):
        return self._IpBlackList

    @IpBlackList.setter
    def IpBlackList(self, IpBlackList):
        self._IpBlackList = IpBlackList

    @property
    def CountryWhiteList(self):
        return self._CountryWhiteList

    @CountryWhiteList.setter
    def CountryWhiteList(self, CountryWhiteList):
        self._CountryWhiteList = CountryWhiteList

    @property
    def CountryBlackList(self):
        return self._CountryBlackList

    @CountryBlackList.setter
    def CountryBlackList(self, CountryBlackList):
        self._CountryBlackList = CountryBlackList


    def _deserialize(self, params):
        self._IpWhiteList = params.get("IpWhiteList")
        self._IpBlackList = params.get("IpBlackList")
        self._CountryWhiteList = params.get("CountryWhiteList")
        self._CountryBlackList = params.get("CountryBlackList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvGatewayRequest(AbstractModel):
    """BindEnvGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubEnvId: 子环境id
        :type SubEnvId: str
        """
        self._SubEnvId = None

    @property
    def SubEnvId(self):
        return self._SubEnvId

    @SubEnvId.setter
    def SubEnvId(self, SubEnvId):
        self._SubEnvId = SubEnvId


    def _deserialize(self, params):
        self._SubEnvId = params.get("SubEnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvGatewayResponse(AbstractModel):
    """BindEnvGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CbrPackageInfo(AbstractModel):
    """代码包信息

    """

    def __init__(self):
        r"""
        :param _PackageName: 代码包名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param _PackageVersion: 代码包版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        """
        self._PackageName = None
        self._PackageVersion = None

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion


    def _deserialize(self, params):
        self._PackageName = params.get("PackageName")
        self._PackageVersion = params.get("PackageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CbrRepoInfo(AbstractModel):
    """仓库信息

    """

    def __init__(self):
        r"""
        :param _Repo: 仓库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Repo: str
        :param _RepoType: 仓库平台
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: str
        :param _RepoLanguage: 仓库语言
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoLanguage: str
        :param _Branch: 分支名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        """
        self._Repo = None
        self._RepoType = None
        self._RepoLanguage = None
        self._Branch = None

    @property
    def Repo(self):
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def RepoLanguage(self):
        return self._RepoLanguage

    @RepoLanguage.setter
    def RepoLanguage(self, RepoLanguage):
        self._RepoLanguage = RepoLanguage

    @property
    def Branch(self):
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch


    def _deserialize(self, params):
        self._Repo = params.get("Repo")
        self._RepoType = params.get("RepoType")
        self._RepoLanguage = params.get("RepoLanguage")
        self._Branch = params.get("Branch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckTcbServiceRequest(AbstractModel):
    """CheckTcbService请求参数结构体

    """


class CheckTcbServiceResponse(AbstractModel):
    """CheckTcbService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Initialized: true表示已开通
        :type Initialized: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Initialized = None
        self._RequestId = None

    @property
    def Initialized(self):
        return self._Initialized

    @Initialized.setter
    def Initialized(self, Initialized):
        self._Initialized = Initialized

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Initialized = params.get("Initialized")
        self._RequestId = params.get("RequestId")


class CloudBaseCapabilities(AbstractModel):
    """cloudrun安全特性能力


    """

    def __init__(self):
        r"""
        :param _Add: 启用安全能力项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Add: list of str
        :param _Drop: 禁用安全能力向列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Drop: list of str
        """
        self._Add = None
        self._Drop = None

    @property
    def Add(self):
        return self._Add

    @Add.setter
    def Add(self, Add):
        self._Add = Add

    @property
    def Drop(self):
        return self._Drop

    @Drop.setter
    def Drop(self, Drop):
        self._Drop = Drop


    def _deserialize(self, params):
        self._Add = params.get("Add")
        self._Drop = params.get("Drop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseCodeRepoDetail(AbstractModel):
    """代码仓库里 Repo的信息描述

    """

    def __init__(self):
        r"""
        :param _Name: repo的名字
        :type Name: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoName`
        :param _Url: repo的url
        :type Url: str
        """
        self._Name = None
        self._Url = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        if params.get("Name") is not None:
            self._Name = CloudBaseCodeRepoName()
            self._Name._deserialize(params.get("Name"))
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseCodeRepoName(AbstractModel):
    """代码仓库 repo的名字

    """

    def __init__(self):
        r"""
        :param _Name: repo的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _FullName: repo的完整全名
注意：此字段可能返回 null，表示取不到有效值。
        :type FullName: str
        """
        self._Name = None
        self._FullName = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._FullName = params.get("FullName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseEsInfo(AbstractModel):
    """es信息

    """

    def __init__(self):
        r"""
        :param _Id: es的id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _SecretName: secret名字
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        :param _Ip: ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: str
        :param _Account: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Account: str
        :param _Password: 密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        """
        self._Id = None
        self._SecretName = None
        self._Ip = None
        self._Port = None
        self._Index = None
        self._Account = None
        self._Password = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SecretName = params.get("SecretName")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Index = params.get("Index")
        self._Account = params.get("Account")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseProjectVersion(AbstractModel):
    """云开发项目版本

    """

    def __init__(self):
        r"""
        :param _Name: 项目名
        :type Name: str
        :param _Sam: SAM json
注意：此字段可能返回 null，表示取不到有效值。
        :type Sam: str
        :param _Source: 来源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: :class:`tencentcloud.tcb.v20180608.models.CodeSource`
        :param _CreateTime: 创建时间, unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _UpdateTime: 更新时间 ,unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _Status: 项目状态, 枚举值: 
        "creatingEnv"-创建环境中
	"createEnvFail"-创建环境失败
	"building"-构建中
	"buildFail"-构建失败
	"deploying"-部署中
	 "deployFail"-部署失败
	 "success"-部署成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Parameters: 环境变量
注意：此字段可能返回 null，表示取不到有效值。
        :type Parameters: list of KVPair
        :param _Type: 项目类型, 枚举值:
"framework-oneclick" 控制台一键部署
"framework-local-oneclick" cli本地一键部署
"qci-extension-cicd" 内网coding ci cd
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _CIId: ci的id
注意：此字段可能返回 null，表示取不到有效值。
        :type CIId: str
        :param _CDId: cd的id
注意：此字段可能返回 null，表示取不到有效值。
        :type CDId: str
        :param _EnvId: 环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param _VersionNum: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionNum: int
        :param _FailReason: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param _RcJson: rc.json内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RcJson: str
        :param _AddonConfig: 插件配置内容
注意：此字段可能返回 null，表示取不到有效值。
        :type AddonConfig: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _NetworkConfig: 网络配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConfig: str
        :param _ExtensionId: 扩展id
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtensionId: str
        :param _FailType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FailType: str
        :param _RepoUrl: 私有仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoUrl: str
        :param _AutoDeployOnCodeChange: 是否私有仓库代码变更触发自动部署
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoDeployOnCodeChange: bool
        :param _BuildPercent: ci部署进度（%）
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildPercent: int
        """
        self._Name = None
        self._Sam = None
        self._Source = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Status = None
        self._Parameters = None
        self._Type = None
        self._CIId = None
        self._CDId = None
        self._EnvId = None
        self._VersionNum = None
        self._FailReason = None
        self._RcJson = None
        self._AddonConfig = None
        self._Tags = None
        self._NetworkConfig = None
        self._ExtensionId = None
        self._FailType = None
        self._RepoUrl = None
        self._AutoDeployOnCodeChange = None
        self._BuildPercent = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sam(self):
        return self._Sam

    @Sam.setter
    def Sam(self, Sam):
        self._Sam = Sam

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CIId(self):
        return self._CIId

    @CIId.setter
    def CIId(self, CIId):
        self._CIId = CIId

    @property
    def CDId(self):
        return self._CDId

    @CDId.setter
    def CDId(self, CDId):
        self._CDId = CDId

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def VersionNum(self):
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def RcJson(self):
        return self._RcJson

    @RcJson.setter
    def RcJson(self, RcJson):
        self._RcJson = RcJson

    @property
    def AddonConfig(self):
        return self._AddonConfig

    @AddonConfig.setter
    def AddonConfig(self, AddonConfig):
        self._AddonConfig = AddonConfig

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NetworkConfig(self):
        return self._NetworkConfig

    @NetworkConfig.setter
    def NetworkConfig(self, NetworkConfig):
        self._NetworkConfig = NetworkConfig

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def FailType(self):
        return self._FailType

    @FailType.setter
    def FailType(self, FailType):
        self._FailType = FailType

    @property
    def RepoUrl(self):
        return self._RepoUrl

    @RepoUrl.setter
    def RepoUrl(self, RepoUrl):
        self._RepoUrl = RepoUrl

    @property
    def AutoDeployOnCodeChange(self):
        return self._AutoDeployOnCodeChange

    @AutoDeployOnCodeChange.setter
    def AutoDeployOnCodeChange(self, AutoDeployOnCodeChange):
        self._AutoDeployOnCodeChange = AutoDeployOnCodeChange

    @property
    def BuildPercent(self):
        return self._BuildPercent

    @BuildPercent.setter
    def BuildPercent(self, BuildPercent):
        self._BuildPercent = BuildPercent


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Sam = params.get("Sam")
        if params.get("Source") is not None:
            self._Source = CodeSource()
            self._Source._deserialize(params.get("Source"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = KVPair()
                obj._deserialize(item)
                self._Parameters.append(obj)
        self._Type = params.get("Type")
        self._CIId = params.get("CIId")
        self._CDId = params.get("CDId")
        self._EnvId = params.get("EnvId")
        self._VersionNum = params.get("VersionNum")
        self._FailReason = params.get("FailReason")
        self._RcJson = params.get("RcJson")
        self._AddonConfig = params.get("AddonConfig")
        self._Tags = params.get("Tags")
        self._NetworkConfig = params.get("NetworkConfig")
        self._ExtensionId = params.get("ExtensionId")
        self._FailType = params.get("FailType")
        self._RepoUrl = params.get("RepoUrl")
        self._AutoDeployOnCodeChange = params.get("AutoDeployOnCodeChange")
        self._BuildPercent = params.get("BuildPercent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunEmptyDirVolumeSource(AbstractModel):
    """emptydir 数据卷详细信息

    """

    def __init__(self):
        r"""
        :param _EnableEmptyDirVolume: 启用emptydir数据卷
        :type EnableEmptyDirVolume: bool
        :param _Medium: "","Memory","HugePages"
        :type Medium: str
        :param _SizeLimit: emptydir数据卷大小
        :type SizeLimit: str
        """
        self._EnableEmptyDirVolume = None
        self._Medium = None
        self._SizeLimit = None

    @property
    def EnableEmptyDirVolume(self):
        return self._EnableEmptyDirVolume

    @EnableEmptyDirVolume.setter
    def EnableEmptyDirVolume(self, EnableEmptyDirVolume):
        self._EnableEmptyDirVolume = EnableEmptyDirVolume

    @property
    def Medium(self):
        return self._Medium

    @Medium.setter
    def Medium(self, Medium):
        self._Medium = Medium

    @property
    def SizeLimit(self):
        return self._SizeLimit

    @SizeLimit.setter
    def SizeLimit(self, SizeLimit):
        self._SizeLimit = SizeLimit


    def _deserialize(self, params):
        self._EnableEmptyDirVolume = params.get("EnableEmptyDirVolume")
        self._Medium = params.get("Medium")
        self._SizeLimit = params.get("SizeLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunForGatewayConf(AbstractModel):
    """独立网关云托管服务配置信息

    """

    def __init__(self):
        r"""
        :param _IsZero: 是否缩容到0
        :type IsZero: bool
        :param _Weight: 按百分比灰度的权重
        :type Weight: int
        :param _GrayKey: 按请求/header参数的灰度Key
        :type GrayKey: str
        :param _GrayValue: 按请求/header参数的灰度Value
        :type GrayValue: str
        :param _IsDefault: 是否为默认版本(按请求/header参数)
        :type IsDefault: bool
        :param _AccessType: 访问权限，对应二进制分多段，vpc内网｜公网｜oa
        :type AccessType: int
        :param _URLs: 访问的URL（域名＋路径）列表
        :type URLs: list of str
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerName: 服务名称
        :type ServerName: str
        :param _VersionName: 版本名称
        :type VersionName: str
        :param _GrayType: 灰度类型：FLOW(权重), URL_PARAMS/HEAD_PARAMS
        :type GrayType: str
        :param _LbAddr: CLB的IP:Port
        :type LbAddr: str
        :param _ConfigType: 0:http访问服务配置信息, 1: 服务域名
        :type ConfigType: int
        """
        self._IsZero = None
        self._Weight = None
        self._GrayKey = None
        self._GrayValue = None
        self._IsDefault = None
        self._AccessType = None
        self._URLs = None
        self._EnvId = None
        self._ServerName = None
        self._VersionName = None
        self._GrayType = None
        self._LbAddr = None
        self._ConfigType = None

    @property
    def IsZero(self):
        return self._IsZero

    @IsZero.setter
    def IsZero(self, IsZero):
        self._IsZero = IsZero

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def GrayKey(self):
        return self._GrayKey

    @GrayKey.setter
    def GrayKey(self, GrayKey):
        self._GrayKey = GrayKey

    @property
    def GrayValue(self):
        return self._GrayValue

    @GrayValue.setter
    def GrayValue(self, GrayValue):
        self._GrayValue = GrayValue

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def AccessType(self):
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def URLs(self):
        return self._URLs

    @URLs.setter
    def URLs(self, URLs):
        self._URLs = URLs

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def GrayType(self):
        return self._GrayType

    @GrayType.setter
    def GrayType(self, GrayType):
        self._GrayType = GrayType

    @property
    def LbAddr(self):
        return self._LbAddr

    @LbAddr.setter
    def LbAddr(self, LbAddr):
        self._LbAddr = LbAddr

    @property
    def ConfigType(self):
        return self._ConfigType

    @ConfigType.setter
    def ConfigType(self, ConfigType):
        self._ConfigType = ConfigType


    def _deserialize(self, params):
        self._IsZero = params.get("IsZero")
        self._Weight = params.get("Weight")
        self._GrayKey = params.get("GrayKey")
        self._GrayValue = params.get("GrayValue")
        self._IsDefault = params.get("IsDefault")
        self._AccessType = params.get("AccessType")
        self._URLs = params.get("URLs")
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        self._GrayType = params.get("GrayType")
        self._LbAddr = params.get("LbAddr")
        self._ConfigType = params.get("ConfigType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunImageInfo(AbstractModel):
    """CloudBaseRun 镜像信息

    """

    def __init__(self):
        r"""
        :param _RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param _IsPublic: 是否公有
        :type IsPublic: bool
        :param _TagName: 镜像tag名称
        :type TagName: str
        :param _ServerAddr: 镜像server
        :type ServerAddr: str
        :param _ImageUrl: 镜像拉取地址
        :type ImageUrl: str
        """
        self._RepositoryName = None
        self._IsPublic = None
        self._TagName = None
        self._ServerAddr = None
        self._ImageUrl = None

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._RepositoryName = params.get("RepositoryName")
        self._IsPublic = params.get("IsPublic")
        self._TagName = params.get("TagName")
        self._ServerAddr = params.get("ServerAddr")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunImageSecretInfo(AbstractModel):
    """ImageSecretInfo的信息

    """

    def __init__(self):
        r"""
        :param _RegistryServer: 镜像地址
        :type RegistryServer: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Password: 仓库密码
        :type Password: str
        :param _Email: 邮箱
        :type Email: str
        """
        self._RegistryServer = None
        self._UserName = None
        self._Password = None
        self._Email = None

    @property
    def RegistryServer(self):
        return self._RegistryServer

    @RegistryServer.setter
    def RegistryServer(self, RegistryServer):
        self._RegistryServer = RegistryServer

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._RegistryServer = params.get("RegistryServer")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunKVPriority(AbstractModel):
    """KV参数的优先级

    """

    def __init__(self):
        r"""
        :param _Key: 参数的Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 参数的Value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Priority: 优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        """
        self._Key = None
        self._Value = None
        self._Priority = None

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

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunNfsVolumeSource(AbstractModel):
    """nfs挂载资源

    """

    def __init__(self):
        r"""
        :param _Server: NFS挂载Server
        :type Server: str
        :param _Path: Server路径
        :type Path: str
        :param _ReadOnly: 是否只读
        :type ReadOnly: bool
        :param _SecretName: secret名称
        :type SecretName: str
        :param _EnableEmptyDirVolume: 临时目录
        :type EnableEmptyDirVolume: bool
        """
        self._Server = None
        self._Path = None
        self._ReadOnly = None
        self._SecretName = None
        self._EnableEmptyDirVolume = None

    @property
    def Server(self):
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def EnableEmptyDirVolume(self):
        return self._EnableEmptyDirVolume

    @EnableEmptyDirVolume.setter
    def EnableEmptyDirVolume(self, EnableEmptyDirVolume):
        self._EnableEmptyDirVolume = EnableEmptyDirVolume


    def _deserialize(self, params):
        self._Server = params.get("Server")
        self._Path = params.get("Path")
        self._ReadOnly = params.get("ReadOnly")
        self._SecretName = params.get("SecretName")
        self._EnableEmptyDirVolume = params.get("EnableEmptyDirVolume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunServerVersionItem(AbstractModel):
    """版本的列表

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名称
        :type VersionName: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _FlowRatio: 流量占比
        :type FlowRatio: int
        :param _CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _UpdatedTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        :param _BuildId: 构建ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildId: int
        :param _UploadType: 构建方式
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadType: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _UrlParam: url中的参数路径
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlParam: :class:`tencentcloud.tcb.v20180608.models.ObjectKV`
        :param _Priority: 优先级（数值越小，优先级越高）
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param _IsDefaultPriority: 是否是默认兜底版本
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultPriority: bool
        :param _FlowParams: KV Params
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowParams: list of CloudBaseRunKVPriority
        :param _MinReplicas: 最小副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinReplicas: int
        :param _MaxReplicas: 最大副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReplicas: int
        :param _RunId: 操作记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type RunId: str
        :param _Percent: 进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param _CurrentReplicas: 当前副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentReplicas: int
        :param _Architecture: Monolithic，Microservice
注意：此字段可能返回 null，表示取不到有效值。
        :type Architecture: str
        """
        self._VersionName = None
        self._Status = None
        self._FlowRatio = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._BuildId = None
        self._UploadType = None
        self._Remark = None
        self._UrlParam = None
        self._Priority = None
        self._IsDefaultPriority = None
        self._FlowParams = None
        self._MinReplicas = None
        self._MaxReplicas = None
        self._RunId = None
        self._Percent = None
        self._CurrentReplicas = None
        self._Architecture = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FlowRatio(self):
        return self._FlowRatio

    @FlowRatio.setter
    def FlowRatio(self, FlowRatio):
        self._FlowRatio = FlowRatio

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def BuildId(self):
        return self._BuildId

    @BuildId.setter
    def BuildId(self, BuildId):
        self._BuildId = BuildId

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UrlParam(self):
        return self._UrlParam

    @UrlParam.setter
    def UrlParam(self, UrlParam):
        self._UrlParam = UrlParam

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def IsDefaultPriority(self):
        return self._IsDefaultPriority

    @IsDefaultPriority.setter
    def IsDefaultPriority(self, IsDefaultPriority):
        self._IsDefaultPriority = IsDefaultPriority

    @property
    def FlowParams(self):
        return self._FlowParams

    @FlowParams.setter
    def FlowParams(self, FlowParams):
        self._FlowParams = FlowParams

    @property
    def MinReplicas(self):
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def RunId(self):
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def CurrentReplicas(self):
        return self._CurrentReplicas

    @CurrentReplicas.setter
    def CurrentReplicas(self, CurrentReplicas):
        self._CurrentReplicas = CurrentReplicas

    @property
    def Architecture(self):
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._Status = params.get("Status")
        self._FlowRatio = params.get("FlowRatio")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._BuildId = params.get("BuildId")
        self._UploadType = params.get("UploadType")
        self._Remark = params.get("Remark")
        if params.get("UrlParam") is not None:
            self._UrlParam = ObjectKV()
            self._UrlParam._deserialize(params.get("UrlParam"))
        self._Priority = params.get("Priority")
        self._IsDefaultPriority = params.get("IsDefaultPriority")
        if params.get("FlowParams") is not None:
            self._FlowParams = []
            for item in params.get("FlowParams"):
                obj = CloudBaseRunKVPriority()
                obj._deserialize(item)
                self._FlowParams.append(obj)
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        self._RunId = params.get("RunId")
        self._Percent = params.get("Percent")
        self._CurrentReplicas = params.get("CurrentReplicas")
        self._Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunServiceVolumeHostPath(AbstractModel):
    """主机路径挂载参数

    """


class CloudBaseRunServiceVolumeMount(AbstractModel):
    """对标 EKS VolumeMount

    """

    def __init__(self):
        r"""
        :param _Name: Volume 名称
        :type Name: str
        :param _MountPath: 挂载路径
        :type MountPath: str
        :param _ReadOnly: 是否只读
        :type ReadOnly: bool
        :param _SubPath: 子路径
        :type SubPath: str
        :param _MountPropagation: 传播挂载方式
        :type MountPropagation: str
        """
        self._Name = None
        self._MountPath = None
        self._ReadOnly = None
        self._SubPath = None
        self._MountPropagation = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MountPath(self):
        return self._MountPath

    @MountPath.setter
    def MountPath(self, MountPath):
        self._MountPath = MountPath

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def SubPath(self):
        return self._SubPath

    @SubPath.setter
    def SubPath(self, SubPath):
        self._SubPath = SubPath

    @property
    def MountPropagation(self):
        return self._MountPropagation

    @MountPropagation.setter
    def MountPropagation(self, MountPropagation):
        self._MountPropagation = MountPropagation


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._MountPath = params.get("MountPath")
        self._ReadOnly = params.get("ReadOnly")
        self._SubPath = params.get("SubPath")
        self._MountPropagation = params.get("MountPropagation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunSideSpec(AbstractModel):
    """CloudBaseRun 的 Side 描述定义

    """

    def __init__(self):
        r"""
        :param _ContainerImage: 容器镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerImage: str
        :param _ContainerPort: 容器端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerPort: int
        :param _ContainerName: 容器的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerName: str
        :param _EnvVar: kv的json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvVar: str
        :param _InitialDelaySeconds: InitialDelaySeconds 延迟多长时间启动健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param _Cpu: CPU大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _Mem: 内存大小（单位：M）
注意：此字段可能返回 null，表示取不到有效值。
        :type Mem: int
        :param _Security: 安全特性
注意：此字段可能返回 null，表示取不到有效值。
        :type Security: :class:`tencentcloud.tcb.v20180608.models.CloudBaseSecurityContext`
        :param _VolumeMountInfos: 挂载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeMountInfos: list of CloudBaseRunVolumeMount
        """
        self._ContainerImage = None
        self._ContainerPort = None
        self._ContainerName = None
        self._EnvVar = None
        self._InitialDelaySeconds = None
        self._Cpu = None
        self._Mem = None
        self._Security = None
        self._VolumeMountInfos = None

    @property
    def ContainerImage(self):
        return self._ContainerImage

    @ContainerImage.setter
    def ContainerImage(self, ContainerImage):
        self._ContainerImage = ContainerImage

    @property
    def ContainerPort(self):
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def ContainerName(self):
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def EnvVar(self):
        return self._EnvVar

    @EnvVar.setter
    def EnvVar(self, EnvVar):
        self._EnvVar = EnvVar

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Security(self):
        return self._Security

    @Security.setter
    def Security(self, Security):
        self._Security = Security

    @property
    def VolumeMountInfos(self):
        return self._VolumeMountInfos

    @VolumeMountInfos.setter
    def VolumeMountInfos(self, VolumeMountInfos):
        self._VolumeMountInfos = VolumeMountInfos


    def _deserialize(self, params):
        self._ContainerImage = params.get("ContainerImage")
        self._ContainerPort = params.get("ContainerPort")
        self._ContainerName = params.get("ContainerName")
        self._EnvVar = params.get("EnvVar")
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        if params.get("Security") is not None:
            self._Security = CloudBaseSecurityContext()
            self._Security._deserialize(params.get("Security"))
        if params.get("VolumeMountInfos") is not None:
            self._VolumeMountInfos = []
            for item in params.get("VolumeMountInfos"):
                obj = CloudBaseRunVolumeMount()
                obj._deserialize(item)
                self._VolumeMountInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunVersionFlowItem(AbstractModel):
    """版本流量占比

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _FlowRatio: 流量占比
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowRatio: int
        :param _UrlParam: 流量参数键值对（URL参数/HEADERS参数）
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlParam: :class:`tencentcloud.tcb.v20180608.models.ObjectKV`
        :param _Priority: 优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param _IsDefaultPriority: 是否是默认兜底版本
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultPriority: bool
        """
        self._VersionName = None
        self._FlowRatio = None
        self._UrlParam = None
        self._Priority = None
        self._IsDefaultPriority = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def FlowRatio(self):
        return self._FlowRatio

    @FlowRatio.setter
    def FlowRatio(self, FlowRatio):
        self._FlowRatio = FlowRatio

    @property
    def UrlParam(self):
        return self._UrlParam

    @UrlParam.setter
    def UrlParam(self, UrlParam):
        self._UrlParam = UrlParam

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def IsDefaultPriority(self):
        return self._IsDefaultPriority

    @IsDefaultPriority.setter
    def IsDefaultPriority(self, IsDefaultPriority):
        self._IsDefaultPriority = IsDefaultPriority


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._FlowRatio = params.get("FlowRatio")
        if params.get("UrlParam") is not None:
            self._UrlParam = ObjectKV()
            self._UrlParam._deserialize(params.get("UrlParam"))
        self._Priority = params.get("Priority")
        self._IsDefaultPriority = params.get("IsDefaultPriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunVolumeMount(AbstractModel):
    """cfs挂载点

    """

    def __init__(self):
        r"""
        :param _Name: 资源名
        :type Name: str
        :param _MountPath: 挂载路径
        :type MountPath: str
        :param _ReadOnly: 是否只读
        :type ReadOnly: bool
        :param _NfsVolumes: Nfs挂载信息
        :type NfsVolumes: list of CloudBaseRunNfsVolumeSource
        """
        self._Name = None
        self._MountPath = None
        self._ReadOnly = None
        self._NfsVolumes = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MountPath(self):
        return self._MountPath

    @MountPath.setter
    def MountPath(self, MountPath):
        self._MountPath = MountPath

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def NfsVolumes(self):
        return self._NfsVolumes

    @NfsVolumes.setter
    def NfsVolumes(self, NfsVolumes):
        self._NfsVolumes = NfsVolumes


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._MountPath = params.get("MountPath")
        self._ReadOnly = params.get("ReadOnly")
        if params.get("NfsVolumes") is not None:
            self._NfsVolumes = []
            for item in params.get("NfsVolumes"):
                obj = CloudBaseRunNfsVolumeSource()
                obj._deserialize(item)
                self._NfsVolumes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunVpcInfo(AbstractModel):
    """vpc信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc的id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetIds: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param _CreateType: 创建类型(0=继承; 1=新建; 2=指定)
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateType: int
        """
        self._VpcId = None
        self._SubnetIds = None
        self._CreateType = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def CreateType(self):
        return self._CreateType

    @CreateType.setter
    def CreateType(self, CreateType):
        self._CreateType = CreateType


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._CreateType = params.get("CreateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseRunVpcSubnet(AbstractModel):
    """子网信息

    """

    def __init__(self):
        r"""
        :param _Id: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Cidr: 子网的ipv4
注意：此字段可能返回 null，表示取不到有效值。
        :type Cidr: str
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Target: subnet类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Target: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Id = None
        self._Cidr = None
        self._Zone = None
        self._Type = None
        self._Target = None
        self._Region = None
        self._Name = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Cidr(self):
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Cidr = params.get("Cidr")
        self._Zone = params.get("Zone")
        self._Type = params.get("Type")
        self._Target = params.get("Target")
        self._Region = params.get("Region")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseSecurityContext(AbstractModel):
    """cloudrun安全特性


    """

    def __init__(self):
        r"""
        :param _Capabilities: 安全特性
注意：此字段可能返回 null，表示取不到有效值。
        :type Capabilities: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCapabilities`
        """
        self._Capabilities = None

    @property
    def Capabilities(self):
        return self._Capabilities

    @Capabilities.setter
    def Capabilities(self, Capabilities):
        self._Capabilities = Capabilities


    def _deserialize(self, params):
        if params.get("Capabilities") is not None:
            self._Capabilities = CloudBaseCapabilities()
            self._Capabilities._deserialize(params.get("Capabilities"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudRunServiceSimpleVersionSnapshot(AbstractModel):
    """CloudRunServiceSimpleVersionSnapshot 信息

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _Remark: 版本备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Cpu: cpu规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: float
        :param _Mem: 内存规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Mem: float
        :param _MinNum: 最小副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinNum: int
        :param _MaxNum: 最大副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNum: int
        :param _ImageUrl: 镜像url
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param _PolicyType: 扩容策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param _PolicyThreshold: 策略阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyThreshold: int
        :param _EnvParams: 环境参数
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvParams: str
        :param _ContainerPort: 容器端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerPort: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _UploadType: 更新类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadType: str
        :param _DockerfilePath: dockerfile路径
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerfilePath: str
        :param _BuildDir: 构建路径
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildDir: str
        :param _RepoType: repo类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: str
        :param _Repo: 仓库
注意：此字段可能返回 null，表示取不到有效值。
        :type Repo: str
        :param _Branch: 分支
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        :param _EnvId: 环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param _ServerName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param _PackageName: package名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param _PackageVersion: package版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param _CustomLogs: 自定义log路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogs: str
        :param _InitialDelaySeconds: 延时健康检查时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param _SnapshotName: snapshot名
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotName: str
        :param _ImageInfo: 镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageInfo`
        :param _CodeDetail: 代码仓库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDetail: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoDetail`
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._VersionName = None
        self._Remark = None
        self._Cpu = None
        self._Mem = None
        self._MinNum = None
        self._MaxNum = None
        self._ImageUrl = None
        self._PolicyType = None
        self._PolicyThreshold = None
        self._EnvParams = None
        self._ContainerPort = None
        self._CreateTime = None
        self._UpdateTime = None
        self._UploadType = None
        self._DockerfilePath = None
        self._BuildDir = None
        self._RepoType = None
        self._Repo = None
        self._Branch = None
        self._EnvId = None
        self._ServerName = None
        self._PackageName = None
        self._PackageVersion = None
        self._CustomLogs = None
        self._InitialDelaySeconds = None
        self._SnapshotName = None
        self._ImageInfo = None
        self._CodeDetail = None
        self._Status = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def MinNum(self):
        return self._MinNum

    @MinNum.setter
    def MinNum(self, MinNum):
        self._MinNum = MinNum

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyThreshold(self):
        return self._PolicyThreshold

    @PolicyThreshold.setter
    def PolicyThreshold(self, PolicyThreshold):
        self._PolicyThreshold = PolicyThreshold

    @property
    def EnvParams(self):
        return self._EnvParams

    @EnvParams.setter
    def EnvParams(self, EnvParams):
        self._EnvParams = EnvParams

    @property
    def ContainerPort(self):
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def DockerfilePath(self):
        return self._DockerfilePath

    @DockerfilePath.setter
    def DockerfilePath(self, DockerfilePath):
        self._DockerfilePath = DockerfilePath

    @property
    def BuildDir(self):
        return self._BuildDir

    @BuildDir.setter
    def BuildDir(self, BuildDir):
        self._BuildDir = BuildDir

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def Repo(self):
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def Branch(self):
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def CustomLogs(self):
        return self._CustomLogs

    @CustomLogs.setter
    def CustomLogs(self, CustomLogs):
        self._CustomLogs = CustomLogs

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def CodeDetail(self):
        return self._CodeDetail

    @CodeDetail.setter
    def CodeDetail(self, CodeDetail):
        self._CodeDetail = CodeDetail

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._Remark = params.get("Remark")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._MinNum = params.get("MinNum")
        self._MaxNum = params.get("MaxNum")
        self._ImageUrl = params.get("ImageUrl")
        self._PolicyType = params.get("PolicyType")
        self._PolicyThreshold = params.get("PolicyThreshold")
        self._EnvParams = params.get("EnvParams")
        self._ContainerPort = params.get("ContainerPort")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._UploadType = params.get("UploadType")
        self._DockerfilePath = params.get("DockerfilePath")
        self._BuildDir = params.get("BuildDir")
        self._RepoType = params.get("RepoType")
        self._Repo = params.get("Repo")
        self._Branch = params.get("Branch")
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._PackageName = params.get("PackageName")
        self._PackageVersion = params.get("PackageVersion")
        self._CustomLogs = params.get("CustomLogs")
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        self._SnapshotName = params.get("SnapshotName")
        if params.get("ImageInfo") is not None:
            self._ImageInfo = CloudBaseRunImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodeDetail") is not None:
            self._CodeDetail = CloudBaseCodeRepoDetail()
            self._CodeDetail._deserialize(params.get("CodeDetail"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudRunServiceVolume(AbstractModel):
    """服务的volume

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _NFS: NFS的挂载方式
注意：此字段可能返回 null，表示取不到有效值。
        :type NFS: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunNfsVolumeSource`
        :param _SecretName: secret名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        :param _EnableEmptyDirVolume: 是否开启临时目录逐步废弃，请使用 EmptyDir
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableEmptyDirVolume: bool
        :param _EmptyDir: emptydir数据卷详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EmptyDir: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunEmptyDirVolumeSource`
        :param _HostPath: 主机路径挂载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HostPath: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunServiceVolumeHostPath`
        """
        self._Name = None
        self._NFS = None
        self._SecretName = None
        self._EnableEmptyDirVolume = None
        self._EmptyDir = None
        self._HostPath = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NFS(self):
        return self._NFS

    @NFS.setter
    def NFS(self, NFS):
        self._NFS = NFS

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def EnableEmptyDirVolume(self):
        return self._EnableEmptyDirVolume

    @EnableEmptyDirVolume.setter
    def EnableEmptyDirVolume(self, EnableEmptyDirVolume):
        self._EnableEmptyDirVolume = EnableEmptyDirVolume

    @property
    def EmptyDir(self):
        return self._EmptyDir

    @EmptyDir.setter
    def EmptyDir(self, EmptyDir):
        self._EmptyDir = EmptyDir

    @property
    def HostPath(self):
        return self._HostPath

    @HostPath.setter
    def HostPath(self, HostPath):
        self._HostPath = HostPath


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("NFS") is not None:
            self._NFS = CloudBaseRunNfsVolumeSource()
            self._NFS._deserialize(params.get("NFS"))
        self._SecretName = params.get("SecretName")
        self._EnableEmptyDirVolume = params.get("EnableEmptyDirVolume")
        if params.get("EmptyDir") is not None:
            self._EmptyDir = CloudBaseRunEmptyDirVolumeSource()
            self._EmptyDir._deserialize(params.get("EmptyDir"))
        if params.get("HostPath") is not None:
            self._HostPath = CloudBaseRunServiceVolumeHostPath()
            self._HostPath._deserialize(params.get("HostPath"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsInfo(AbstractModel):
    """cls日志信息

    """

    def __init__(self):
        r"""
        :param _ClsRegion: cls所属地域
        :type ClsRegion: str
        :param _ClsLogsetId: cls日志集ID
        :type ClsLogsetId: str
        :param _ClsTopicId: cls日志主题ID
        :type ClsTopicId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._ClsRegion = None
        self._ClsLogsetId = None
        self._ClsTopicId = None
        self._CreateTime = None

    @property
    def ClsRegion(self):
        return self._ClsRegion

    @ClsRegion.setter
    def ClsRegion(self, ClsRegion):
        self._ClsRegion = ClsRegion

    @property
    def ClsLogsetId(self):
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsTopicId(self):
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ClsRegion = params.get("ClsRegion")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._ClsTopicId = params.get("ClsTopicId")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeSource(AbstractModel):
    """云开发项目来源

    """

    def __init__(self):
        r"""
        :param _Type: 类型, 可能的枚举: "coding","package","package_url","github","gitlab","gitee","rawcode"
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Url: 下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _WorkDir: 工作目录
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkDir: str
        :param _CodingPackageName: code包名, type为coding的时候需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type CodingPackageName: str
        :param _CodingPackageVersion: coding版本名, type为coding的时候需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type CodingPackageVersion: str
        :param _RawCode: 源码
注意：此字段可能返回 null，表示取不到有效值。
        :type RawCode: str
        :param _Branch: 代码分支
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        :param _ProjectId: coding项目ID，type为coding时需要填写
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _ProjectName: coding项目
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        """
        self._Type = None
        self._Url = None
        self._Name = None
        self._WorkDir = None
        self._CodingPackageName = None
        self._CodingPackageVersion = None
        self._RawCode = None
        self._Branch = None
        self._ProjectId = None
        self._ProjectName = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def WorkDir(self):
        return self._WorkDir

    @WorkDir.setter
    def WorkDir(self, WorkDir):
        self._WorkDir = WorkDir

    @property
    def CodingPackageName(self):
        return self._CodingPackageName

    @CodingPackageName.setter
    def CodingPackageName(self, CodingPackageName):
        self._CodingPackageName = CodingPackageName

    @property
    def CodingPackageVersion(self):
        return self._CodingPackageVersion

    @CodingPackageVersion.setter
    def CodingPackageVersion(self, CodingPackageVersion):
        self._CodingPackageVersion = CodingPackageVersion

    @property
    def RawCode(self):
        return self._RawCode

    @RawCode.setter
    def RawCode(self, RawCode):
        self._RawCode = RawCode

    @property
    def Branch(self):
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        self._Name = params.get("Name")
        self._WorkDir = params.get("WorkDir")
        self._CodingPackageName = params.get("CodingPackageName")
        self._CodingPackageVersion = params.get("CodingPackageVersion")
        self._RawCode = params.get("RawCode")
        self._Branch = params.get("Branch")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonServiceAPIRequest(AbstractModel):
    """CommonServiceAPI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: Service名，需要转发访问的接口名
        :type Service: str
        :param _JSONData: 需要转发的云API参数，要转成JSON格式
        :type JSONData: str
        :param _ApiRole: 指定角色
        :type ApiRole: str
        """
        self._Service = None
        self._JSONData = None
        self._ApiRole = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def JSONData(self):
        return self._JSONData

    @JSONData.setter
    def JSONData(self, JSONData):
        self._JSONData = JSONData

    @property
    def ApiRole(self):
        return self._ApiRole

    @ApiRole.setter
    def ApiRole(self, ApiRole):
        self._ApiRole = ApiRole


    def _deserialize(self, params):
        self._Service = params.get("Service")
        self._JSONData = params.get("JSONData")
        self._ApiRole = params.get("ApiRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonServiceAPIResponse(AbstractModel):
    """CommonServiceAPI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JSONResp: json格式response
        :type JSONResp: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JSONResp = None
        self._RequestId = None

    @property
    def JSONResp(self):
        return self._JSONResp

    @JSONResp.setter
    def JSONResp(self, JSONResp):
        self._JSONResp = JSONResp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JSONResp = params.get("JSONResp")
        self._RequestId = params.get("RequestId")


class CreateAndDeployCloudBaseProjectRequest(AbstractModel):
    """CreateAndDeployCloudBaseProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 项目名
        :type Name: str
        :param _Source: 来源
        :type Source: :class:`tencentcloud.tcb.v20180608.models.CodeSource`
        :param _EnvId: 环境id
        :type EnvId: str
        :param _Type: 项目类型, 枚举值为: framework-oneclick,qci-extension-cicd
        :type Type: str
        :param _Parameters: 环境变量
        :type Parameters: list of KVPair
        :param _EnvAlias: 环境别名。要以a-z开头，不能包含a-zA-z0-9-以外的字符
        :type EnvAlias: str
        :param _RcJson: rc.json的内容
        :type RcJson: str
        :param _AddonConfig: 插件配置内容
        :type AddonConfig: str
        :param _Tags: 标签
        :type Tags: list of str
        :param _NetworkConfig: 网络配置
        :type NetworkConfig: str
        :param _FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。
        :type FreeQuota: str
        :param _AutoDeployOnCodeChange: 是否代码变更触发自动部署
        :type AutoDeployOnCodeChange: bool
        :param _RepoUrl: 私有仓库地址
        :type RepoUrl: str
        """
        self._Name = None
        self._Source = None
        self._EnvId = None
        self._Type = None
        self._Parameters = None
        self._EnvAlias = None
        self._RcJson = None
        self._AddonConfig = None
        self._Tags = None
        self._NetworkConfig = None
        self._FreeQuota = None
        self._AutoDeployOnCodeChange = None
        self._RepoUrl = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def EnvAlias(self):
        return self._EnvAlias

    @EnvAlias.setter
    def EnvAlias(self, EnvAlias):
        self._EnvAlias = EnvAlias

    @property
    def RcJson(self):
        return self._RcJson

    @RcJson.setter
    def RcJson(self, RcJson):
        self._RcJson = RcJson

    @property
    def AddonConfig(self):
        return self._AddonConfig

    @AddonConfig.setter
    def AddonConfig(self, AddonConfig):
        self._AddonConfig = AddonConfig

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NetworkConfig(self):
        return self._NetworkConfig

    @NetworkConfig.setter
    def NetworkConfig(self, NetworkConfig):
        self._NetworkConfig = NetworkConfig

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def AutoDeployOnCodeChange(self):
        return self._AutoDeployOnCodeChange

    @AutoDeployOnCodeChange.setter
    def AutoDeployOnCodeChange(self, AutoDeployOnCodeChange):
        self._AutoDeployOnCodeChange = AutoDeployOnCodeChange

    @property
    def RepoUrl(self):
        return self._RepoUrl

    @RepoUrl.setter
    def RepoUrl(self, RepoUrl):
        self._RepoUrl = RepoUrl


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Source") is not None:
            self._Source = CodeSource()
            self._Source._deserialize(params.get("Source"))
        self._EnvId = params.get("EnvId")
        self._Type = params.get("Type")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = KVPair()
                obj._deserialize(item)
                self._Parameters.append(obj)
        self._EnvAlias = params.get("EnvAlias")
        self._RcJson = params.get("RcJson")
        self._AddonConfig = params.get("AddonConfig")
        self._Tags = params.get("Tags")
        self._NetworkConfig = params.get("NetworkConfig")
        self._FreeQuota = params.get("FreeQuota")
        self._AutoDeployOnCodeChange = params.get("AutoDeployOnCodeChange")
        self._RepoUrl = params.get("RepoUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndDeployCloudBaseProjectResponse(AbstractModel):
    """CreateAndDeployCloudBaseProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._RequestId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._RequestId = params.get("RequestId")


class CreateAuthDomainRequest(AbstractModel):
    """CreateAuthDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Domains: 安全域名
        :type Domains: list of str
        """
        self._EnvId = None
        self._Domains = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuthDomainResponse(AbstractModel):
    """CreateAuthDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CreateCloudBaseRunResourceRequest(AbstractModel):
    """CreateCloudBaseRunResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _VpcId: vpc的ID
        :type VpcId: str
        :param _SubnetIds: 子网ID列表，当VpcId不为空，SubnetIds也不能为空
        :type SubnetIds: list of str
        """
        self._EnvId = None
        self._VpcId = None
        self._SubnetIds = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudBaseRunResourceResponse(AbstractModel):
    """CreateCloudBaseRunResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回集群创建是否成功 succ为成功。并且中间无err
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CreateCloudBaseRunServerVersionRequest(AbstractModel):
    """CreateCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _UploadType: 枚举（package/repository/image/jar/war)
        :type UploadType: str
        :param _FlowRatio: 流量占比
        :type FlowRatio: int
        :param _Cpu: Cpu的大小，单位：核
        :type Cpu: float
        :param _Mem: Mem的大小，单位：G
        :type Mem: float
        :param _MinNum: 最小副本数，最小值：0
        :type MinNum: int
        :param _MaxNum: 副本最大数，最大值：50
        :type MaxNum: int
        :param _PolicyType: 策略类型(枚举值：比如cpu)
        :type PolicyType: str
        :param _PolicyThreshold: 策略阈值
        :type PolicyThreshold: int
        :param _ContainerPort: 服务端口
        :type ContainerPort: int
        :param _ServerName: 服务名称
        :type ServerName: str
        :param _RepositoryType: repository的类型(coding/gitlab/github/coding)
        :type RepositoryType: str
        :param _DockerfilePath: Dockerfile地址
        :type DockerfilePath: str
        :param _BuildDir: 构建目录
        :type BuildDir: str
        :param _EnvParams: 环境变量
        :type EnvParams: str
        :param _Repository: repository地址
        :type Repository: str
        :param _Branch: 分支
        :type Branch: str
        :param _VersionRemark: 版本备注
        :type VersionRemark: str
        :param _PackageName: 代码包名字
        :type PackageName: str
        :param _PackageVersion: 代码包的版本
        :type PackageVersion: str
        :param _ImageInfo: Image的详情
        :type ImageInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageInfo`
        :param _CodeDetail: Github等拉取代码的详情
        :type CodeDetail: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoDetail`
        :param _ImageSecretInfo: 私有镜像秘钥信息
        :type ImageSecretInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageSecretInfo`
        :param _ImagePullSecret: 私有镜像 认证名称
        :type ImagePullSecret: str
        :param _CustomLogs: 用户自定义采集日志路径
        :type CustomLogs: str
        :param _InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
        :type InitialDelaySeconds: int
        :param _MountVolumeInfo: cfs挂载信息
        :type MountVolumeInfo: list of CloudBaseRunVolumeMount
        :param _AccessType: 4 代表只能微信链路访问
        :type AccessType: int
        :param _EsInfo: es信息
        :type EsInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseEsInfo`
        :param _EnableUnion: 是否使用统一域名
        :type EnableUnion: bool
        :param _OperatorRemark: 操作备注
        :type OperatorRemark: str
        :param _ServerPath: 服务路径
        :type ServerPath: str
        :param _ImageReuseKey: 镜像复用的key
        :type ImageReuseKey: str
        :param _SidecarSpecs: 容器的描述文件
        :type SidecarSpecs: list of CloudBaseRunSideSpec
        :param _Security: 安全特性
        :type Security: :class:`tencentcloud.tcb.v20180608.models.CloudBaseSecurityContext`
        :param _ServiceVolumes: 服务磁盘挂载
        :type ServiceVolumes: list of CloudRunServiceVolume
        :param _IsCreateJnsGw: 是否创建JnsGw 0未传默认创建 1创建 2不创建
        :type IsCreateJnsGw: int
        :param _ServiceVolumeMounts: 数据卷挂载参数
        :type ServiceVolumeMounts: list of CloudBaseRunServiceVolumeMount
        :param _HasDockerfile: 是否有Dockerfile：0-default has, 1-has, 2-has not
        :type HasDockerfile: int
        :param _BaseImage: 基础镜像
        :type BaseImage: str
        :param _EntryPoint: 容器启动入口命令
        :type EntryPoint: str
        :param _RepoLanguage: 仓库语言
        :type RepoLanguage: str
        :param _UploadFilename: 用户实际上传文件名（仅UploadType为jar/war时必填）
        :type UploadFilename: str
        :param _PolicyDetail: 自动扩缩容策略组
        :type PolicyDetail: list of HpaPolicy
        """
        self._EnvId = None
        self._UploadType = None
        self._FlowRatio = None
        self._Cpu = None
        self._Mem = None
        self._MinNum = None
        self._MaxNum = None
        self._PolicyType = None
        self._PolicyThreshold = None
        self._ContainerPort = None
        self._ServerName = None
        self._RepositoryType = None
        self._DockerfilePath = None
        self._BuildDir = None
        self._EnvParams = None
        self._Repository = None
        self._Branch = None
        self._VersionRemark = None
        self._PackageName = None
        self._PackageVersion = None
        self._ImageInfo = None
        self._CodeDetail = None
        self._ImageSecretInfo = None
        self._ImagePullSecret = None
        self._CustomLogs = None
        self._InitialDelaySeconds = None
        self._MountVolumeInfo = None
        self._AccessType = None
        self._EsInfo = None
        self._EnableUnion = None
        self._OperatorRemark = None
        self._ServerPath = None
        self._ImageReuseKey = None
        self._SidecarSpecs = None
        self._Security = None
        self._ServiceVolumes = None
        self._IsCreateJnsGw = None
        self._ServiceVolumeMounts = None
        self._HasDockerfile = None
        self._BaseImage = None
        self._EntryPoint = None
        self._RepoLanguage = None
        self._UploadFilename = None
        self._PolicyDetail = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def FlowRatio(self):
        return self._FlowRatio

    @FlowRatio.setter
    def FlowRatio(self, FlowRatio):
        self._FlowRatio = FlowRatio

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def MinNum(self):
        return self._MinNum

    @MinNum.setter
    def MinNum(self, MinNum):
        self._MinNum = MinNum

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyThreshold(self):
        return self._PolicyThreshold

    @PolicyThreshold.setter
    def PolicyThreshold(self, PolicyThreshold):
        self._PolicyThreshold = PolicyThreshold

    @property
    def ContainerPort(self):
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def RepositoryType(self):
        return self._RepositoryType

    @RepositoryType.setter
    def RepositoryType(self, RepositoryType):
        self._RepositoryType = RepositoryType

    @property
    def DockerfilePath(self):
        return self._DockerfilePath

    @DockerfilePath.setter
    def DockerfilePath(self, DockerfilePath):
        self._DockerfilePath = DockerfilePath

    @property
    def BuildDir(self):
        return self._BuildDir

    @BuildDir.setter
    def BuildDir(self, BuildDir):
        self._BuildDir = BuildDir

    @property
    def EnvParams(self):
        return self._EnvParams

    @EnvParams.setter
    def EnvParams(self, EnvParams):
        self._EnvParams = EnvParams

    @property
    def Repository(self):
        return self._Repository

    @Repository.setter
    def Repository(self, Repository):
        self._Repository = Repository

    @property
    def Branch(self):
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def VersionRemark(self):
        return self._VersionRemark

    @VersionRemark.setter
    def VersionRemark(self, VersionRemark):
        self._VersionRemark = VersionRemark

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def CodeDetail(self):
        return self._CodeDetail

    @CodeDetail.setter
    def CodeDetail(self, CodeDetail):
        self._CodeDetail = CodeDetail

    @property
    def ImageSecretInfo(self):
        return self._ImageSecretInfo

    @ImageSecretInfo.setter
    def ImageSecretInfo(self, ImageSecretInfo):
        self._ImageSecretInfo = ImageSecretInfo

    @property
    def ImagePullSecret(self):
        return self._ImagePullSecret

    @ImagePullSecret.setter
    def ImagePullSecret(self, ImagePullSecret):
        self._ImagePullSecret = ImagePullSecret

    @property
    def CustomLogs(self):
        return self._CustomLogs

    @CustomLogs.setter
    def CustomLogs(self, CustomLogs):
        self._CustomLogs = CustomLogs

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def MountVolumeInfo(self):
        return self._MountVolumeInfo

    @MountVolumeInfo.setter
    def MountVolumeInfo(self, MountVolumeInfo):
        self._MountVolumeInfo = MountVolumeInfo

    @property
    def AccessType(self):
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def EsInfo(self):
        return self._EsInfo

    @EsInfo.setter
    def EsInfo(self, EsInfo):
        self._EsInfo = EsInfo

    @property
    def EnableUnion(self):
        return self._EnableUnion

    @EnableUnion.setter
    def EnableUnion(self, EnableUnion):
        self._EnableUnion = EnableUnion

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark

    @property
    def ServerPath(self):
        return self._ServerPath

    @ServerPath.setter
    def ServerPath(self, ServerPath):
        self._ServerPath = ServerPath

    @property
    def ImageReuseKey(self):
        return self._ImageReuseKey

    @ImageReuseKey.setter
    def ImageReuseKey(self, ImageReuseKey):
        self._ImageReuseKey = ImageReuseKey

    @property
    def SidecarSpecs(self):
        return self._SidecarSpecs

    @SidecarSpecs.setter
    def SidecarSpecs(self, SidecarSpecs):
        self._SidecarSpecs = SidecarSpecs

    @property
    def Security(self):
        return self._Security

    @Security.setter
    def Security(self, Security):
        self._Security = Security

    @property
    def ServiceVolumes(self):
        return self._ServiceVolumes

    @ServiceVolumes.setter
    def ServiceVolumes(self, ServiceVolumes):
        self._ServiceVolumes = ServiceVolumes

    @property
    def IsCreateJnsGw(self):
        return self._IsCreateJnsGw

    @IsCreateJnsGw.setter
    def IsCreateJnsGw(self, IsCreateJnsGw):
        self._IsCreateJnsGw = IsCreateJnsGw

    @property
    def ServiceVolumeMounts(self):
        return self._ServiceVolumeMounts

    @ServiceVolumeMounts.setter
    def ServiceVolumeMounts(self, ServiceVolumeMounts):
        self._ServiceVolumeMounts = ServiceVolumeMounts

    @property
    def HasDockerfile(self):
        return self._HasDockerfile

    @HasDockerfile.setter
    def HasDockerfile(self, HasDockerfile):
        self._HasDockerfile = HasDockerfile

    @property
    def BaseImage(self):
        return self._BaseImage

    @BaseImage.setter
    def BaseImage(self, BaseImage):
        self._BaseImage = BaseImage

    @property
    def EntryPoint(self):
        return self._EntryPoint

    @EntryPoint.setter
    def EntryPoint(self, EntryPoint):
        self._EntryPoint = EntryPoint

    @property
    def RepoLanguage(self):
        return self._RepoLanguage

    @RepoLanguage.setter
    def RepoLanguage(self, RepoLanguage):
        self._RepoLanguage = RepoLanguage

    @property
    def UploadFilename(self):
        return self._UploadFilename

    @UploadFilename.setter
    def UploadFilename(self, UploadFilename):
        self._UploadFilename = UploadFilename

    @property
    def PolicyDetail(self):
        return self._PolicyDetail

    @PolicyDetail.setter
    def PolicyDetail(self, PolicyDetail):
        self._PolicyDetail = PolicyDetail


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._UploadType = params.get("UploadType")
        self._FlowRatio = params.get("FlowRatio")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._MinNum = params.get("MinNum")
        self._MaxNum = params.get("MaxNum")
        self._PolicyType = params.get("PolicyType")
        self._PolicyThreshold = params.get("PolicyThreshold")
        self._ContainerPort = params.get("ContainerPort")
        self._ServerName = params.get("ServerName")
        self._RepositoryType = params.get("RepositoryType")
        self._DockerfilePath = params.get("DockerfilePath")
        self._BuildDir = params.get("BuildDir")
        self._EnvParams = params.get("EnvParams")
        self._Repository = params.get("Repository")
        self._Branch = params.get("Branch")
        self._VersionRemark = params.get("VersionRemark")
        self._PackageName = params.get("PackageName")
        self._PackageVersion = params.get("PackageVersion")
        if params.get("ImageInfo") is not None:
            self._ImageInfo = CloudBaseRunImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodeDetail") is not None:
            self._CodeDetail = CloudBaseCodeRepoDetail()
            self._CodeDetail._deserialize(params.get("CodeDetail"))
        if params.get("ImageSecretInfo") is not None:
            self._ImageSecretInfo = CloudBaseRunImageSecretInfo()
            self._ImageSecretInfo._deserialize(params.get("ImageSecretInfo"))
        self._ImagePullSecret = params.get("ImagePullSecret")
        self._CustomLogs = params.get("CustomLogs")
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        if params.get("MountVolumeInfo") is not None:
            self._MountVolumeInfo = []
            for item in params.get("MountVolumeInfo"):
                obj = CloudBaseRunVolumeMount()
                obj._deserialize(item)
                self._MountVolumeInfo.append(obj)
        self._AccessType = params.get("AccessType")
        if params.get("EsInfo") is not None:
            self._EsInfo = CloudBaseEsInfo()
            self._EsInfo._deserialize(params.get("EsInfo"))
        self._EnableUnion = params.get("EnableUnion")
        self._OperatorRemark = params.get("OperatorRemark")
        self._ServerPath = params.get("ServerPath")
        self._ImageReuseKey = params.get("ImageReuseKey")
        if params.get("SidecarSpecs") is not None:
            self._SidecarSpecs = []
            for item in params.get("SidecarSpecs"):
                obj = CloudBaseRunSideSpec()
                obj._deserialize(item)
                self._SidecarSpecs.append(obj)
        if params.get("Security") is not None:
            self._Security = CloudBaseSecurityContext()
            self._Security._deserialize(params.get("Security"))
        if params.get("ServiceVolumes") is not None:
            self._ServiceVolumes = []
            for item in params.get("ServiceVolumes"):
                obj = CloudRunServiceVolume()
                obj._deserialize(item)
                self._ServiceVolumes.append(obj)
        self._IsCreateJnsGw = params.get("IsCreateJnsGw")
        if params.get("ServiceVolumeMounts") is not None:
            self._ServiceVolumeMounts = []
            for item in params.get("ServiceVolumeMounts"):
                obj = CloudBaseRunServiceVolumeMount()
                obj._deserialize(item)
                self._ServiceVolumeMounts.append(obj)
        self._HasDockerfile = params.get("HasDockerfile")
        self._BaseImage = params.get("BaseImage")
        self._EntryPoint = params.get("EntryPoint")
        self._RepoLanguage = params.get("RepoLanguage")
        self._UploadFilename = params.get("UploadFilename")
        if params.get("PolicyDetail") is not None:
            self._PolicyDetail = []
            for item in params.get("PolicyDetail"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self._PolicyDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudBaseRunServerVersionResponse(AbstractModel):
    """CreateCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 状态(creating/succ)
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _VersionName: 版本名称（只有Result为succ的时候，才会返回VersionName)
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _RunId: 操作记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type RunId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._VersionName = None
        self._RunId = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def RunId(self):
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._VersionName = params.get("VersionName")
        self._RunId = params.get("RunId")
        self._RequestId = params.get("RequestId")


class CreateHostingDomainRequest(AbstractModel):
    """CreateHostingDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 证书ID
        :type CertId: str
        """
        self._EnvId = None
        self._Domain = None
        self._CertId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHostingDomainResponse(AbstractModel):
    """CreateHostingDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CreatePostpayPackageRequest(AbstractModel):
    """CreatePostpayPackage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID，需要系统自动创建环境时，此字段不传
        :type EnvId: str
        :param _WxAppId: 微信 AppId，微信必传
        :type WxAppId: str
        :param _Source: 付费来源
<li>miniapp</li>
<li>qcloud</li>
        :type Source: str
        :param _FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，表示不享受免费额度。
        :type FreeQuota: str
        :param _EnvSource: 环境创建来源，取值：
<li>miniapp</li>
<li>qcloud</li>
用法同CreateEnv接口的Source参数
和 Channel 参数同时传，或者同时不传；EnvId 为空时必传。
        :type EnvSource: str
        :param _Alias: 环境别名，要以a-z开头，不能包含  a-z,0-9,-  以外的字符
        :type Alias: str
        :param _Channel: 如果envsource为miniapp, channel可以为ide或api;
如果envsource为qcloud, channel可以为qc_console,cocos, qq, cloudgame,dcloud,serverless_framework
和 EnvSource 参数同时传，或者同时不传；EnvId 为空时必传。
        :type Channel: str
        :param _ExtensionId: 扩展ID
        :type ExtensionId: str
        :param _Flag: 订单标记。建议使用方统一转大小写之后再判断。
<li>QuickStart：快速启动来源</li>
<li>Activity：活动来源</li>
        :type Flag: str
        :param _EnvAlias: 环境别名，无字符类型限制
        :type EnvAlias: str
        :param _Extra: 附加字段，用于透传额外的自定义信息
        :type Extra: str
        """
        self._EnvId = None
        self._WxAppId = None
        self._Source = None
        self._FreeQuota = None
        self._EnvSource = None
        self._Alias = None
        self._Channel = None
        self._ExtensionId = None
        self._Flag = None
        self._EnvAlias = None
        self._Extra = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def WxAppId(self):
        return self._WxAppId

    @WxAppId.setter
    def WxAppId(self, WxAppId):
        self._WxAppId = WxAppId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def EnvSource(self):
        return self._EnvSource

    @EnvSource.setter
    def EnvSource(self, EnvSource):
        self._EnvSource = EnvSource

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def EnvAlias(self):
        return self._EnvAlias

    @EnvAlias.setter
    def EnvAlias(self, EnvAlias):
        self._EnvAlias = EnvAlias

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._WxAppId = params.get("WxAppId")
        self._Source = params.get("Source")
        self._FreeQuota = params.get("FreeQuota")
        self._EnvSource = params.get("EnvSource")
        self._Alias = params.get("Alias")
        self._Channel = params.get("Channel")
        self._ExtensionId = params.get("ExtensionId")
        self._Flag = params.get("Flag")
        self._EnvAlias = params.get("EnvAlias")
        self._Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePostpayPackageResponse(AbstractModel):
    """CreatePostpayPackage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TranId: 后付费订单号
        :type TranId: str
        :param _EnvId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TranId = None
        self._EnvId = None
        self._RequestId = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._EnvId = params.get("EnvId")
        self._RequestId = params.get("RequestId")


class CreateStandaloneGatewayRequest(AbstractModel):
    """CreateStandaloneGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _GatewayAlias: 网关名
        :type GatewayAlias: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetIds: 子网ID
        :type SubnetIds: list of str
        :param _GatewayDesc: 网关描述
        :type GatewayDesc: str
        :param _PackageVersion: 网关套餐版本
        :type PackageVersion: str
        """
        self._EnvId = None
        self._GatewayAlias = None
        self._VpcId = None
        self._SubnetIds = None
        self._GatewayDesc = None
        self._PackageVersion = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayAlias(self):
        return self._GatewayAlias

    @GatewayAlias.setter
    def GatewayAlias(self, GatewayAlias):
        self._GatewayAlias = GatewayAlias

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def GatewayDesc(self):
        return self._GatewayDesc

    @GatewayDesc.setter
    def GatewayDesc(self, GatewayDesc):
        self._GatewayDesc = GatewayDesc

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayAlias = params.get("GatewayAlias")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._GatewayDesc = params.get("GatewayDesc")
        self._PackageVersion = params.get("PackageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStandaloneGatewayResponse(AbstractModel):
    """CreateStandaloneGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayName: 网关名称
        :type GatewayName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GatewayName = None
        self._RequestId = None

    @property
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GatewayName = params.get("GatewayName")
        self._RequestId = params.get("RequestId")


class CreateStaticStoreRequest(AbstractModel):
    """CreateStaticStore请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _EnableUnion: 是否启用统一域名
        :type EnableUnion: bool
        """
        self._EnvId = None
        self._EnableUnion = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnableUnion(self):
        return self._EnableUnion

    @EnableUnion.setter
    def EnableUnion(self, EnableUnion):
        self._EnableUnion = EnableUnion


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._EnableUnion = params.get("EnableUnion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStaticStoreResponse(AbstractModel):
    """CreateStaticStore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建静态资源结果(succ/fail)
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CreateWxCloudBaseRunEnvRequest(AbstractModel):
    """CreateWxCloudBaseRunEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WxAppId: wx应用Id
        :type WxAppId: str
        :param _Alias: 环境别名，要以a-z开头，不能包含 a-z,0-9,- 以外的字符
        :type Alias: str
        :param _FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。
        :type FreeQuota: str
        :param _Flag: 订单标记。建议使用方统一转大小写之后再判断。
QuickStart：快速启动来源
Activity：活动来源
        :type Flag: str
        :param _VpcId: 私有网络Id
        :type VpcId: str
        :param _SubNetIds: 子网列表
        :type SubNetIds: list of str
        :param _IsOpenCloudInvoke: 是否打开云调用
        :type IsOpenCloudInvoke: bool
        :param _Source: 创建来源：wechat | cloud
        :type Source: str
        :param _Channel: 渠道：wechat | cloud
        :type Channel: str
        """
        self._WxAppId = None
        self._Alias = None
        self._FreeQuota = None
        self._Flag = None
        self._VpcId = None
        self._SubNetIds = None
        self._IsOpenCloudInvoke = None
        self._Source = None
        self._Channel = None

    @property
    def WxAppId(self):
        return self._WxAppId

    @WxAppId.setter
    def WxAppId(self, WxAppId):
        self._WxAppId = WxAppId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubNetIds(self):
        return self._SubNetIds

    @SubNetIds.setter
    def SubNetIds(self, SubNetIds):
        self._SubNetIds = SubNetIds

    @property
    def IsOpenCloudInvoke(self):
        return self._IsOpenCloudInvoke

    @IsOpenCloudInvoke.setter
    def IsOpenCloudInvoke(self, IsOpenCloudInvoke):
        self._IsOpenCloudInvoke = IsOpenCloudInvoke

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._WxAppId = params.get("WxAppId")
        self._Alias = params.get("Alias")
        self._FreeQuota = params.get("FreeQuota")
        self._Flag = params.get("Flag")
        self._VpcId = params.get("VpcId")
        self._SubNetIds = params.get("SubNetIds")
        self._IsOpenCloudInvoke = params.get("IsOpenCloudInvoke")
        self._Source = params.get("Source")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWxCloudBaseRunEnvResponse(AbstractModel):
    """CreateWxCloudBaseRunEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _TranId: 后付费订单号
        :type TranId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._TranId = None
        self._RequestId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._TranId = params.get("TranId")
        self._RequestId = params.get("RequestId")


class CreateWxCloudBaseRunServerDBClusterRequest(AbstractModel):
    """CreateWxCloudBaseRunServerDBCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountPassword: 账户密码
        :type AccountPassword: str
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _WxAppId: 微信appid
        :type WxAppId: str
        :param _DbVersion: mysql内核版本，支持5.7,8.0
        :type DbVersion: str
        :param _LowerCaseTableName: 0: 非大小写敏感
1: 大小写敏感
默认 0
        :type LowerCaseTableName: str
        """
        self._AccountPassword = None
        self._EnvId = None
        self._WxAppId = None
        self._DbVersion = None
        self._LowerCaseTableName = None

    @property
    def AccountPassword(self):
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def WxAppId(self):
        return self._WxAppId

    @WxAppId.setter
    def WxAppId(self, WxAppId):
        self._WxAppId = WxAppId

    @property
    def DbVersion(self):
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def LowerCaseTableName(self):
        return self._LowerCaseTableName

    @LowerCaseTableName.setter
    def LowerCaseTableName(self, LowerCaseTableName):
        self._LowerCaseTableName = LowerCaseTableName


    def _deserialize(self, params):
        self._AccountPassword = params.get("AccountPassword")
        self._EnvId = params.get("EnvId")
        self._WxAppId = params.get("WxAppId")
        self._DbVersion = params.get("DbVersion")
        self._LowerCaseTableName = params.get("LowerCaseTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWxCloudBaseRunServerDBClusterResponse(AbstractModel):
    """CreateWxCloudBaseRunServerDBCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CustomHeader(AbstractModel):
    """安全网关自定义头部

    """

    def __init__(self):
        r"""
        :param _RequestToAddList: 请求添加头部配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestToAddList: list of CustomRequestToAdd
        """
        self._RequestToAddList = None

    @property
    def RequestToAddList(self):
        return self._RequestToAddList

    @RequestToAddList.setter
    def RequestToAddList(self, RequestToAddList):
        self._RequestToAddList = RequestToAddList


    def _deserialize(self, params):
        if params.get("RequestToAddList") is not None:
            self._RequestToAddList = []
            for item in params.get("RequestToAddList"):
                obj = CustomRequestToAdd()
                obj._deserialize(item)
                self._RequestToAddList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomLogConfig(AbstractModel):
    """安全网关自定义日志配置

    """

    def __init__(self):
        r"""
        :param _NeedReqBodyLog: 是否需要请求体
        :type NeedReqBodyLog: bool
        :param _NeedReqHeaderLog: 是否需要请求头
        :type NeedReqHeaderLog: bool
        :param _NeedRspBodyLog: 是否需要回包体
        :type NeedRspBodyLog: bool
        :param _NeedRspHeaderLog: 是否需要回包头部信息
        :type NeedRspHeaderLog: bool
        :param _LogSetId: cls set信息
        :type LogSetId: str
        :param _LogTopicId: cls topicId
        :type LogTopicId: str
        """
        self._NeedReqBodyLog = None
        self._NeedReqHeaderLog = None
        self._NeedRspBodyLog = None
        self._NeedRspHeaderLog = None
        self._LogSetId = None
        self._LogTopicId = None

    @property
    def NeedReqBodyLog(self):
        return self._NeedReqBodyLog

    @NeedReqBodyLog.setter
    def NeedReqBodyLog(self, NeedReqBodyLog):
        self._NeedReqBodyLog = NeedReqBodyLog

    @property
    def NeedReqHeaderLog(self):
        return self._NeedReqHeaderLog

    @NeedReqHeaderLog.setter
    def NeedReqHeaderLog(self, NeedReqHeaderLog):
        self._NeedReqHeaderLog = NeedReqHeaderLog

    @property
    def NeedRspBodyLog(self):
        return self._NeedRspBodyLog

    @NeedRspBodyLog.setter
    def NeedRspBodyLog(self, NeedRspBodyLog):
        self._NeedRspBodyLog = NeedRspBodyLog

    @property
    def NeedRspHeaderLog(self):
        return self._NeedRspHeaderLog

    @NeedRspHeaderLog.setter
    def NeedRspHeaderLog(self, NeedRspHeaderLog):
        self._NeedRspHeaderLog = NeedRspHeaderLog

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId


    def _deserialize(self, params):
        self._NeedReqBodyLog = params.get("NeedReqBodyLog")
        self._NeedReqHeaderLog = params.get("NeedReqHeaderLog")
        self._NeedRspBodyLog = params.get("NeedRspBodyLog")
        self._NeedRspHeaderLog = params.get("NeedRspHeaderLog")
        self._LogSetId = params.get("LogSetId")
        self._LogTopicId = params.get("LogTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomRequestToAdd(AbstractModel):
    """安全网关请求自定义头部

    """

    def __init__(self):
        r"""
        :param _Key: Header名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: Header值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _AppendAction: Header类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AppendAction: str
        """
        self._Key = None
        self._Value = None
        self._AppendAction = None

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

    @property
    def AppendAction(self):
        return self._AppendAction

    @AppendAction.setter
    def AppendAction(self, AppendAction):
        self._AppendAction = AppendAction


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._AppendAction = params.get("AppendAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasesInfo(AbstractModel):
    """数据库资源信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 数据库唯一标识
        :type InstanceId: str
        :param _Status: 状态。包含以下取值：
<li>INITIALIZING：资源初始化中</li>
<li>RUNNING：运行中，可正常使用的状态</li>
<li>UNUSABLE：禁用，不可用</li>
<li>OVERDUE：资源过期</li>
        :type Status: str
        :param _Region: 所属地域。
当前支持ap-shanghai
        :type Region: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._InstanceId = None
        self._Status = None
        self._Region = None
        self._UpdateTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudBaseProjectLatestVersionRequest(AbstractModel):
    """DeleteCloudBaseProjectLatestVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _ProjectName: 项目名
        :type ProjectName: str
        :param _KeepResource: 是否保留资源
        :type KeepResource: bool
        """
        self._EnvId = None
        self._ProjectName = None
        self._KeepResource = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def KeepResource(self):
        return self._KeepResource

    @KeepResource.setter
    def KeepResource(self, KeepResource):
        self._KeepResource = KeepResource


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ProjectName = params.get("ProjectName")
        self._KeepResource = params.get("KeepResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudBaseProjectLatestVersionResponse(AbstractModel):
    """DeleteCloudBaseProjectLatestVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DeleteCloudBaseRunServerVersionRequest(AbstractModel):
    """DeleteCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerName: 服务名称
        :type ServerName: str
        :param _VersionName: 版本名称
        :type VersionName: str
        :param _IsDeleteServer: 是否删除服务，只有最后一个版本的时候，才生效。
        :type IsDeleteServer: bool
        :param _IsDeleteImage: 只有删除服务的时候，才会起作用
        :type IsDeleteImage: bool
        :param _OperatorRemark: 操作备注
        :type OperatorRemark: str
        """
        self._EnvId = None
        self._ServerName = None
        self._VersionName = None
        self._IsDeleteServer = None
        self._IsDeleteImage = None
        self._OperatorRemark = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def IsDeleteServer(self):
        return self._IsDeleteServer

    @IsDeleteServer.setter
    def IsDeleteServer(self, IsDeleteServer):
        self._IsDeleteServer = IsDeleteServer

    @property
    def IsDeleteImage(self):
        return self._IsDeleteImage

    @IsDeleteImage.setter
    def IsDeleteImage(self, IsDeleteImage):
        self._IsDeleteImage = IsDeleteImage

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        self._IsDeleteServer = params.get("IsDeleteServer")
        self._IsDeleteImage = params.get("IsDeleteImage")
        self._OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudBaseRunServerVersionResponse(AbstractModel):
    """DeleteCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果，succ为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DeleteEndUserRequest(AbstractModel):
    """DeleteEndUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _UserList: 用户列表，每一项都是uuid
        :type UserList: list of str
        """
        self._EnvId = None
        self._UserList = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._UserList = params.get("UserList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEndUserResponse(AbstractModel):
    """DeleteEndUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DeleteGatewayVersionRequest(AbstractModel):
    """DeleteGatewayVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _GatewayId: 网关id
        :type GatewayId: str
        :param _VersionName: 版本名
        :type VersionName: str
        :param _IsDeleteServer: 是否删除服务
        :type IsDeleteServer: bool
        :param _IsDeleteImage: 是否删除镜像
        :type IsDeleteImage: bool
        :param _IsForce: 是否强制删除
        :type IsForce: bool
        :param _OperatorRemark: 操作记录
        :type OperatorRemark: str
        """
        self._EnvId = None
        self._GatewayId = None
        self._VersionName = None
        self._IsDeleteServer = None
        self._IsDeleteImage = None
        self._IsForce = None
        self._OperatorRemark = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def IsDeleteServer(self):
        return self._IsDeleteServer

    @IsDeleteServer.setter
    def IsDeleteServer(self, IsDeleteServer):
        self._IsDeleteServer = IsDeleteServer

    @property
    def IsDeleteImage(self):
        return self._IsDeleteImage

    @IsDeleteImage.setter
    def IsDeleteImage(self, IsDeleteImage):
        self._IsDeleteImage = IsDeleteImage

    @property
    def IsForce(self):
        return self._IsForce

    @IsForce.setter
    def IsForce(self, IsForce):
        self._IsForce = IsForce

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayId = params.get("GatewayId")
        self._VersionName = params.get("VersionName")
        self._IsDeleteServer = params.get("IsDeleteServer")
        self._IsDeleteImage = params.get("IsDeleteImage")
        self._IsForce = params.get("IsForce")
        self._OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGatewayVersionResponse(AbstractModel):
    """DeleteGatewayVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除结果
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DeleteWxGatewayRouteRequest(AbstractModel):
    """DeleteWxGatewayRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _GatewayRouteName: 服务名称
        :type GatewayRouteName: str
        """
        self._EnvId = None
        self._GatewayRouteName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayRouteName(self):
        return self._GatewayRouteName

    @GatewayRouteName.setter
    def GatewayRouteName(self, GatewayRouteName):
        self._GatewayRouteName = GatewayRouteName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayRouteName = params.get("GatewayRouteName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWxGatewayRouteResponse(AbstractModel):
    """DeleteWxGatewayRoute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeActivityInfoRequest(AbstractModel):
    """DescribeActivityInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityIdList: 活动id列表
        :type ActivityIdList: list of int
        """
        self._ActivityIdList = None

    @property
    def ActivityIdList(self):
        return self._ActivityIdList

    @ActivityIdList.setter
    def ActivityIdList(self, ActivityIdList):
        self._ActivityIdList = ActivityIdList


    def _deserialize(self, params):
        self._ActivityIdList = params.get("ActivityIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActivityInfoResponse(AbstractModel):
    """DescribeActivityInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityInfoList: 活动详情
        :type ActivityInfoList: list of ActivityInfoItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityInfoList = None
        self._RequestId = None

    @property
    def ActivityInfoList(self):
        return self._ActivityInfoList

    @ActivityInfoList.setter
    def ActivityInfoList(self, ActivityInfoList):
        self._ActivityInfoList = ActivityInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ActivityInfoList") is not None:
            self._ActivityInfoList = []
            for item in params.get("ActivityInfoList"):
                obj = ActivityInfoItem()
                obj._deserialize(item)
                self._ActivityInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeActivityRecordRequest(AbstractModel):
    """DescribeActivityRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelToken: 渠道加密token
        :type ChannelToken: str
        :param _Channel: 渠道来源，每个来源对应不同secretKey
        :type Channel: str
        :param _ActivityIdList: 活动id列表
        :type ActivityIdList: list of int
        :param _Status: 过滤状态码，已废弃
        :type Status: int
        :param _Statuses: 状态码过滤数组，空数组时不过滤
        :type Statuses: list of int
        :param _IsDeletedList: 根据是否软删除进行过滤，[0]未删除, [1] 删除，不传不过滤
        :type IsDeletedList: list of int
        """
        self._ChannelToken = None
        self._Channel = None
        self._ActivityIdList = None
        self._Status = None
        self._Statuses = None
        self._IsDeletedList = None

    @property
    def ChannelToken(self):
        return self._ChannelToken

    @ChannelToken.setter
    def ChannelToken(self, ChannelToken):
        self._ChannelToken = ChannelToken

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def ActivityIdList(self):
        return self._ActivityIdList

    @ActivityIdList.setter
    def ActivityIdList(self, ActivityIdList):
        self._ActivityIdList = ActivityIdList

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Statuses(self):
        return self._Statuses

    @Statuses.setter
    def Statuses(self, Statuses):
        self._Statuses = Statuses

    @property
    def IsDeletedList(self):
        return self._IsDeletedList

    @IsDeletedList.setter
    def IsDeletedList(self, IsDeletedList):
        self._IsDeletedList = IsDeletedList


    def _deserialize(self, params):
        self._ChannelToken = params.get("ChannelToken")
        self._Channel = params.get("Channel")
        self._ActivityIdList = params.get("ActivityIdList")
        self._Status = params.get("Status")
        self._Statuses = params.get("Statuses")
        self._IsDeletedList = params.get("IsDeletedList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActivityRecordResponse(AbstractModel):
    """DescribeActivityRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityRecords: 活动记录详情
        :type ActivityRecords: list of ActivityRecordItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityRecords = None
        self._RequestId = None

    @property
    def ActivityRecords(self):
        return self._ActivityRecords

    @ActivityRecords.setter
    def ActivityRecords(self, ActivityRecords):
        self._ActivityRecords = ActivityRecords

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ActivityRecords") is not None:
            self._ActivityRecords = []
            for item in params.get("ActivityRecords"):
                obj = ActivityRecordItem()
                obj._deserialize(item)
                self._ActivityRecords.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuthDomainsRequest(AbstractModel):
    """DescribeAuthDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthDomainsResponse(AbstractModel):
    """DescribeAuthDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domains: 安全域名列表
        :type Domains: list of AuthDomain
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domains = None
        self._RequestId = None

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = AuthDomain()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBaasPackageListRequest(AbstractModel):
    """DescribeBaasPackageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageName: tcb产品套餐ID，不填拉取全量package信息。
        :type PackageName: str
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Source: 套餐归属方，填写后只返回对应的套餐 包含miniapp与qcloud两种 默认为miniapp
        :type Source: str
        :param _EnvChannel: 套餐归属环境渠道
        :type EnvChannel: str
        :param _TargetAction: 拉取套餐用途：
1）new 新购
2）modify变配
3）renew续费
        :type TargetAction: str
        :param _GroupName: 预留字段，同一商品会对应多个类型套餐，对指标有不同侧重。
计算型calculation
流量型flux
容量型capactiy
        :type GroupName: str
        :param _PackageTypeList: 类型分组过滤。默认为["default"]
        :type PackageTypeList: list of str
        :param _PaymentChannel: 付费渠道，与回包billTags中的计费参数相关，不填返回默认值。
        :type PaymentChannel: str
        """
        self._PackageName = None
        self._EnvId = None
        self._Source = None
        self._EnvChannel = None
        self._TargetAction = None
        self._GroupName = None
        self._PackageTypeList = None
        self._PaymentChannel = None

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def EnvChannel(self):
        return self._EnvChannel

    @EnvChannel.setter
    def EnvChannel(self, EnvChannel):
        self._EnvChannel = EnvChannel

    @property
    def TargetAction(self):
        return self._TargetAction

    @TargetAction.setter
    def TargetAction(self, TargetAction):
        self._TargetAction = TargetAction

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def PackageTypeList(self):
        return self._PackageTypeList

    @PackageTypeList.setter
    def PackageTypeList(self, PackageTypeList):
        self._PackageTypeList = PackageTypeList

    @property
    def PaymentChannel(self):
        return self._PaymentChannel

    @PaymentChannel.setter
    def PaymentChannel(self, PaymentChannel):
        self._PaymentChannel = PaymentChannel


    def _deserialize(self, params):
        self._PackageName = params.get("PackageName")
        self._EnvId = params.get("EnvId")
        self._Source = params.get("Source")
        self._EnvChannel = params.get("EnvChannel")
        self._TargetAction = params.get("TargetAction")
        self._GroupName = params.get("GroupName")
        self._PackageTypeList = params.get("PackageTypeList")
        self._PaymentChannel = params.get("PaymentChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaasPackageListResponse(AbstractModel):
    """DescribeBaasPackageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageList: 套餐列表
        :type PackageList: list of BaasPackageInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PackageList = None
        self._RequestId = None

    @property
    def PackageList(self):
        return self._PackageList

    @PackageList.setter
    def PackageList(self, PackageList):
        self._PackageList = PackageList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PackageList") is not None:
            self._PackageList = []
            for item in params.get("PackageList"):
                obj = BaasPackageInfo()
                obj._deserialize(item)
                self._PackageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillingInfoRequest(AbstractModel):
    """DescribeBillingInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingInfoResponse(AbstractModel):
    """DescribeBillingInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvBillingInfoList: 环境计费信息列表
        :type EnvBillingInfoList: list of EnvBillingInfoItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvBillingInfoList = None
        self._RequestId = None

    @property
    def EnvBillingInfoList(self):
        return self._EnvBillingInfoList

    @EnvBillingInfoList.setter
    def EnvBillingInfoList(self, EnvBillingInfoList):
        self._EnvBillingInfoList = EnvBillingInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnvBillingInfoList") is not None:
            self._EnvBillingInfoList = []
            for item in params.get("EnvBillingInfoList"):
                obj = EnvBillingInfoItem()
                obj._deserialize(item)
                self._EnvBillingInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCbrServerVersionRequest(AbstractModel):
    """DescribeCbrServerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerName: 服务名称
        :type ServerName: str
        :param _VersionName: 版本名称
        :type VersionName: str
        """
        self._EnvId = None
        self._ServerName = None
        self._VersionName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCbrServerVersionResponse(AbstractModel):
    """DescribeCbrServerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名称
        :type VersionName: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _DockerfilePath: Dockefile的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerfilePath: str
        :param _BuildDir: DockerBuild的目录
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildDir: str
        :param _Cpu: Cpu大小
        :type Cpu: float
        :param _Mem: Mem大小
        :type Mem: float
        :param _MinNum: 副本最小值
        :type MinNum: int
        :param _MaxNum: 副本最大值
        :type MaxNum: int
        :param _EnvParams: 环境变量
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvParams: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param _VersionIP: 版本的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionIP: str
        :param _VersionPort: 版本的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionPort: int
        :param _Status: 版本状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _UploadType: 枚举（package/repository/image)
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadType: str
        :param _ServerName: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param _IsPublic: 是否对于外网开放
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublic: bool
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetIds: 子网实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param _CustomLogs: 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogs: str
        :param _ContainerPort: 监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerPort: int
        :param _InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param _ImageUrl: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param _HasDockerfile: 是否有Dockerfile：0-default has, 1-has, 2-has not
注意：此字段可能返回 null，表示取不到有效值。
        :type HasDockerfile: int
        :param _BaseImage: 基础镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseImage: str
        :param _EntryPoint: 容器启动入口命令
注意：此字段可能返回 null，表示取不到有效值。
        :type EntryPoint: str
        :param _PolicyDetail: 自动扩缩容策略组
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDetail: list of HpaPolicy
        :param _TkeClusterInfo: Tke集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TkeClusterInfo: :class:`tencentcloud.tcb.v20180608.models.TkeClusterInfo`
        :param _TkeWorkloadType: 版本工作负载类型；deployment/deamonset
注意：此字段可能返回 null，表示取不到有效值。
        :type TkeWorkloadType: str
        :param _PackageInfo: 代码包信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageInfo: :class:`tencentcloud.tcb.v20180608.models.CbrPackageInfo`
        :param _RepoInfo: 仓库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoInfo: :class:`tencentcloud.tcb.v20180608.models.CbrRepoInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionName = None
        self._Remark = None
        self._DockerfilePath = None
        self._BuildDir = None
        self._Cpu = None
        self._Mem = None
        self._MinNum = None
        self._MaxNum = None
        self._EnvParams = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._VersionIP = None
        self._VersionPort = None
        self._Status = None
        self._UploadType = None
        self._ServerName = None
        self._IsPublic = None
        self._VpcId = None
        self._SubnetIds = None
        self._CustomLogs = None
        self._ContainerPort = None
        self._InitialDelaySeconds = None
        self._ImageUrl = None
        self._HasDockerfile = None
        self._BaseImage = None
        self._EntryPoint = None
        self._PolicyDetail = None
        self._TkeClusterInfo = None
        self._TkeWorkloadType = None
        self._PackageInfo = None
        self._RepoInfo = None
        self._RequestId = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DockerfilePath(self):
        return self._DockerfilePath

    @DockerfilePath.setter
    def DockerfilePath(self, DockerfilePath):
        self._DockerfilePath = DockerfilePath

    @property
    def BuildDir(self):
        return self._BuildDir

    @BuildDir.setter
    def BuildDir(self, BuildDir):
        self._BuildDir = BuildDir

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def MinNum(self):
        return self._MinNum

    @MinNum.setter
    def MinNum(self, MinNum):
        self._MinNum = MinNum

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum

    @property
    def EnvParams(self):
        return self._EnvParams

    @EnvParams.setter
    def EnvParams(self, EnvParams):
        self._EnvParams = EnvParams

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def VersionIP(self):
        return self._VersionIP

    @VersionIP.setter
    def VersionIP(self, VersionIP):
        self._VersionIP = VersionIP

    @property
    def VersionPort(self):
        return self._VersionPort

    @VersionPort.setter
    def VersionPort(self, VersionPort):
        self._VersionPort = VersionPort

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def CustomLogs(self):
        return self._CustomLogs

    @CustomLogs.setter
    def CustomLogs(self, CustomLogs):
        self._CustomLogs = CustomLogs

    @property
    def ContainerPort(self):
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def HasDockerfile(self):
        return self._HasDockerfile

    @HasDockerfile.setter
    def HasDockerfile(self, HasDockerfile):
        self._HasDockerfile = HasDockerfile

    @property
    def BaseImage(self):
        return self._BaseImage

    @BaseImage.setter
    def BaseImage(self, BaseImage):
        self._BaseImage = BaseImage

    @property
    def EntryPoint(self):
        return self._EntryPoint

    @EntryPoint.setter
    def EntryPoint(self, EntryPoint):
        self._EntryPoint = EntryPoint

    @property
    def PolicyDetail(self):
        return self._PolicyDetail

    @PolicyDetail.setter
    def PolicyDetail(self, PolicyDetail):
        self._PolicyDetail = PolicyDetail

    @property
    def TkeClusterInfo(self):
        return self._TkeClusterInfo

    @TkeClusterInfo.setter
    def TkeClusterInfo(self, TkeClusterInfo):
        self._TkeClusterInfo = TkeClusterInfo

    @property
    def TkeWorkloadType(self):
        return self._TkeWorkloadType

    @TkeWorkloadType.setter
    def TkeWorkloadType(self, TkeWorkloadType):
        self._TkeWorkloadType = TkeWorkloadType

    @property
    def PackageInfo(self):
        return self._PackageInfo

    @PackageInfo.setter
    def PackageInfo(self, PackageInfo):
        self._PackageInfo = PackageInfo

    @property
    def RepoInfo(self):
        return self._RepoInfo

    @RepoInfo.setter
    def RepoInfo(self, RepoInfo):
        self._RepoInfo = RepoInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._Remark = params.get("Remark")
        self._DockerfilePath = params.get("DockerfilePath")
        self._BuildDir = params.get("BuildDir")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._MinNum = params.get("MinNum")
        self._MaxNum = params.get("MaxNum")
        self._EnvParams = params.get("EnvParams")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._VersionIP = params.get("VersionIP")
        self._VersionPort = params.get("VersionPort")
        self._Status = params.get("Status")
        self._UploadType = params.get("UploadType")
        self._ServerName = params.get("ServerName")
        self._IsPublic = params.get("IsPublic")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._CustomLogs = params.get("CustomLogs")
        self._ContainerPort = params.get("ContainerPort")
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        self._ImageUrl = params.get("ImageUrl")
        self._HasDockerfile = params.get("HasDockerfile")
        self._BaseImage = params.get("BaseImage")
        self._EntryPoint = params.get("EntryPoint")
        if params.get("PolicyDetail") is not None:
            self._PolicyDetail = []
            for item in params.get("PolicyDetail"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self._PolicyDetail.append(obj)
        if params.get("TkeClusterInfo") is not None:
            self._TkeClusterInfo = TkeClusterInfo()
            self._TkeClusterInfo._deserialize(params.get("TkeClusterInfo"))
        self._TkeWorkloadType = params.get("TkeWorkloadType")
        if params.get("PackageInfo") is not None:
            self._PackageInfo = CbrPackageInfo()
            self._PackageInfo._deserialize(params.get("PackageInfo"))
        if params.get("RepoInfo") is not None:
            self._RepoInfo = CbrRepoInfo()
            self._RepoInfo._deserialize(params.get("RepoInfo"))
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseBuildServiceRequest(AbstractModel):
    """DescribeCloudBaseBuildService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _ServiceName: 服务名
        :type ServiceName: str
        :param _CIBusiness: build类型,枚举值有: cloudbaserun, framework-ci
        :type CIBusiness: str
        :param _ServiceVersion: 服务版本
        :type ServiceVersion: str
        :param _Suffix: 文件后缀
        :type Suffix: str
        """
        self._EnvId = None
        self._ServiceName = None
        self._CIBusiness = None
        self._ServiceVersion = None
        self._Suffix = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def CIBusiness(self):
        return self._CIBusiness

    @CIBusiness.setter
    def CIBusiness(self, CIBusiness):
        self._CIBusiness = CIBusiness

    @property
    def ServiceVersion(self):
        return self._ServiceVersion

    @ServiceVersion.setter
    def ServiceVersion(self, ServiceVersion):
        self._ServiceVersion = ServiceVersion

    @property
    def Suffix(self):
        return self._Suffix

    @Suffix.setter
    def Suffix(self, Suffix):
        self._Suffix = Suffix


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServiceName = params.get("ServiceName")
        self._CIBusiness = params.get("CIBusiness")
        self._ServiceVersion = params.get("ServiceVersion")
        self._Suffix = params.get("Suffix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseBuildServiceResponse(AbstractModel):
    """DescribeCloudBaseBuildService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UploadUrl: 上传url
        :type UploadUrl: str
        :param _UploadHeaders: 上传heder
        :type UploadHeaders: list of KVPair
        :param _PackageName: 包名
        :type PackageName: str
        :param _PackageVersion: 包版本
        :type PackageVersion: str
        :param _DownloadUrl: 下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param _DownloadHeaders: 下载Httpheader
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadHeaders: list of KVPair
        :param _OutDate: 下载链接是否过期
注意：此字段可能返回 null，表示取不到有效值。
        :type OutDate: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UploadUrl = None
        self._UploadHeaders = None
        self._PackageName = None
        self._PackageVersion = None
        self._DownloadUrl = None
        self._DownloadHeaders = None
        self._OutDate = None
        self._RequestId = None

    @property
    def UploadUrl(self):
        return self._UploadUrl

    @UploadUrl.setter
    def UploadUrl(self, UploadUrl):
        self._UploadUrl = UploadUrl

    @property
    def UploadHeaders(self):
        return self._UploadHeaders

    @UploadHeaders.setter
    def UploadHeaders(self, UploadHeaders):
        self._UploadHeaders = UploadHeaders

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def DownloadHeaders(self):
        return self._DownloadHeaders

    @DownloadHeaders.setter
    def DownloadHeaders(self, DownloadHeaders):
        self._DownloadHeaders = DownloadHeaders

    @property
    def OutDate(self):
        return self._OutDate

    @OutDate.setter
    def OutDate(self, OutDate):
        self._OutDate = OutDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UploadUrl = params.get("UploadUrl")
        if params.get("UploadHeaders") is not None:
            self._UploadHeaders = []
            for item in params.get("UploadHeaders"):
                obj = KVPair()
                obj._deserialize(item)
                self._UploadHeaders.append(obj)
        self._PackageName = params.get("PackageName")
        self._PackageVersion = params.get("PackageVersion")
        self._DownloadUrl = params.get("DownloadUrl")
        if params.get("DownloadHeaders") is not None:
            self._DownloadHeaders = []
            for item in params.get("DownloadHeaders"):
                obj = KVPair()
                obj._deserialize(item)
                self._DownloadHeaders.append(obj)
        self._OutDate = params.get("OutDate")
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseProjectLatestVersionListRequest(AbstractModel):
    """DescribeCloudBaseProjectLatestVersionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _PageSize: 个数
        :type PageSize: int
        :param _EnvId: 环境id, 非必填
        :type EnvId: str
        :param _ProjectName: 项目名称, 非必填
        :type ProjectName: str
        :param _ProjectType: 项目类型: framework-oneclick,qci-extension-cicd
        :type ProjectType: str
        :param _Tags: 标签
        :type Tags: list of str
        :param _CiId: ci的id
        :type CiId: str
        """
        self._Offset = None
        self._PageSize = None
        self._EnvId = None
        self._ProjectName = None
        self._ProjectType = None
        self._Tags = None
        self._CiId = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectType(self):
        return self._ProjectType

    @ProjectType.setter
    def ProjectType(self, ProjectType):
        self._ProjectType = ProjectType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CiId(self):
        return self._CiId

    @CiId.setter
    def CiId(self, CiId):
        self._CiId = CiId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._PageSize = params.get("PageSize")
        self._EnvId = params.get("EnvId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectType = params.get("ProjectType")
        self._Tags = params.get("Tags")
        self._CiId = params.get("CiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseProjectLatestVersionListResponse(AbstractModel):
    """DescribeCloudBaseProjectLatestVersionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectList: 项目列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectList: list of CloudBaseProjectVersion
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProjectList(self):
        return self._ProjectList

    @ProjectList.setter
    def ProjectList(self, ProjectList):
        self._ProjectList = ProjectList

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
        if params.get("ProjectList") is not None:
            self._ProjectList = []
            for item in params.get("ProjectList"):
                obj = CloudBaseProjectVersion()
                obj._deserialize(item)
                self._ProjectList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseProjectVersionListRequest(AbstractModel):
    """DescribeCloudBaseProjectVersionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _PageSize: 页大小
        :type PageSize: int
        :param _PageNum: 第几页,从0开始
        :type PageNum: int
        :param _StartTime: 起始时间 2021-03-27 12:00:00
        :type StartTime: str
        :param _EndTime: 终止时间 2021-03-27 12:00:00
        :type EndTime: str
        """
        self._EnvId = None
        self._ProjectName = None
        self._PageSize = None
        self._PageNum = None
        self._StartTime = None
        self._EndTime = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

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
        self._EnvId = params.get("EnvId")
        self._ProjectName = params.get("ProjectName")
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseProjectVersionListResponse(AbstractModel):
    """DescribeCloudBaseProjectVersionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectVersions: 版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectVersions: list of CloudBaseProjectVersion
        :param _TotalCount: 总个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectVersions = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProjectVersions(self):
        return self._ProjectVersions

    @ProjectVersions.setter
    def ProjectVersions(self, ProjectVersions):
        self._ProjectVersions = ProjectVersions

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
        if params.get("ProjectVersions") is not None:
            self._ProjectVersions = []
            for item in params.get("ProjectVersions"):
                obj = CloudBaseProjectVersion()
                obj._deserialize(item)
                self._ProjectVersions.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunAllVpcsRequest(AbstractModel):
    """DescribeCloudBaseRunAllVpcs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunAllVpcsResponse(AbstractModel):
    """DescribeCloudBaseRunAllVpcs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Vpcs: 所有vpcid
注意：此字段可能返回 null，表示取不到有效值。
        :type Vpcs: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Vpcs = None
        self._RequestId = None

    @property
    def Vpcs(self):
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        self._Vpcs = Vpcs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Vpcs = params.get("Vpcs")
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunConfForGateWayRequest(AbstractModel):
    """DescribeCloudBaseRunConfForGateWay请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvID: 环境ID
        :type EnvID: str
        :param _VpcID: vpc信息
        :type VpcID: str
        """
        self._EnvID = None
        self._VpcID = None

    @property
    def EnvID(self):
        return self._EnvID

    @EnvID.setter
    def EnvID(self, EnvID):
        self._EnvID = EnvID

    @property
    def VpcID(self):
        return self._VpcID

    @VpcID.setter
    def VpcID(self, VpcID):
        self._VpcID = VpcID


    def _deserialize(self, params):
        self._EnvID = params.get("EnvID")
        self._VpcID = params.get("VpcID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunConfForGateWayResponse(AbstractModel):
    """DescribeCloudBaseRunConfForGateWay返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LastUpTime: 最近更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpTime: str
        :param _Data: 配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CloudBaseRunForGatewayConf
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LastUpTime = None
        self._Data = None
        self._RequestId = None

    @property
    def LastUpTime(self):
        return self._LastUpTime

    @LastUpTime.setter
    def LastUpTime(self, LastUpTime):
        self._LastUpTime = LastUpTime

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
        self._LastUpTime = params.get("LastUpTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CloudBaseRunForGatewayConf()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunOneClickTaskExternalRequest(AbstractModel):
    """DescribeCloudBaseRunOneClickTaskExternal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExternalId: 外部任务Id 最长64字节
        :type ExternalId: str
        """
        self._ExternalId = None

    @property
    def ExternalId(self):
        return self._ExternalId

    @ExternalId.setter
    def ExternalId(self, ExternalId):
        self._ExternalId = ExternalId


    def _deserialize(self, params):
        self._ExternalId = params.get("ExternalId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunOneClickTaskExternalResponse(AbstractModel):
    """DescribeCloudBaseRunOneClickTaskExternal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExternalId: 外部任务Id
        :type ExternalId: str
        :param _EnvId: 弃用
        :type EnvId: str
        :param _UserUin: 用户uin
        :type UserUin: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _VersionName: 版本名
        :type VersionName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Stage: 当前阶段
微信云托管环境创建阶段：envStage
存储资源创建阶段：storageStage
服务创建阶段：serverStage
        :type Stage: str
        :param _Status: 状态
running
stopped
failed
finished
        :type Status: str
        :param _FailReason: 失败原因
        :type FailReason: str
        :param _UserEnvId: 用户envId
        :type UserEnvId: str
        :param _StartTime: 创建时间
        :type StartTime: str
        :param _Steps: 步骤信息
        :type Steps: list of OneClickTaskStepInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExternalId = None
        self._EnvId = None
        self._UserUin = None
        self._ServerName = None
        self._VersionName = None
        self._CreateTime = None
        self._Stage = None
        self._Status = None
        self._FailReason = None
        self._UserEnvId = None
        self._StartTime = None
        self._Steps = None
        self._RequestId = None

    @property
    def ExternalId(self):
        return self._ExternalId

    @ExternalId.setter
    def ExternalId(self, ExternalId):
        self._ExternalId = ExternalId

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def UserUin(self):
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Stage(self):
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def UserEnvId(self):
        return self._UserEnvId

    @UserEnvId.setter
    def UserEnvId(self, UserEnvId):
        self._UserEnvId = UserEnvId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Steps(self):
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExternalId = params.get("ExternalId")
        self._EnvId = params.get("EnvId")
        self._UserUin = params.get("UserUin")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        self._CreateTime = params.get("CreateTime")
        self._Stage = params.get("Stage")
        self._Status = params.get("Status")
        self._FailReason = params.get("FailReason")
        self._UserEnvId = params.get("UserEnvId")
        self._StartTime = params.get("StartTime")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = OneClickTaskStepInfo()
                obj._deserialize(item)
                self._Steps.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunOperationTypesRequest(AbstractModel):
    """DescribeCloudBaseRunOperationTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerName: 服务名称，精确匹配
        :type ServerName: str
        """
        self._EnvId = None
        self._ServerName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunOperationTypesResponse(AbstractModel):
    """DescribeCloudBaseRunOperationTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Action: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: list of str
        :param _ServerName: 服务名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Action = None
        self._ServerName = None
        self._RequestId = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._ServerName = params.get("ServerName")
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunPodListRequest(AbstractModel):
    """DescribeCloudBaseRunPodList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _ServerName: 服务名
        :type ServerName: str
        :param _VersionName: 版本名
        :type VersionName: str
        :param _Limit: 分页限制
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Status: 容器状态
        :type Status: str
        :param _PodName: 容器名
        :type PodName: str
        """
        self._EnvId = None
        self._ServerName = None
        self._VersionName = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._PodName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunPodListResponse(AbstractModel):
    """DescribeCloudBaseRunPodList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeCloudBaseRunResourceForExtendRequest(AbstractModel):
    """DescribeCloudBaseRunResourceForExtend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunResourceForExtendResponse(AbstractModel):
    """DescribeCloudBaseRunResourceForExtend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterStatus: 集群状态(creating/succ)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStatus: str
        :param _VirtualClusterId: 虚拟集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualClusterId: str
        :param _VpcId: vpc id信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _SubnetIds: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of CloudBaseRunVpcSubnet
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterStatus = None
        self._VirtualClusterId = None
        self._VpcId = None
        self._Region = None
        self._SubnetIds = None
        self._RequestId = None

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def VirtualClusterId(self):
        return self._VirtualClusterId

    @VirtualClusterId.setter
    def VirtualClusterId(self, VirtualClusterId):
        self._VirtualClusterId = VirtualClusterId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterStatus = params.get("ClusterStatus")
        self._VirtualClusterId = params.get("VirtualClusterId")
        self._VpcId = params.get("VpcId")
        self._Region = params.get("Region")
        if params.get("SubnetIds") is not None:
            self._SubnetIds = []
            for item in params.get("SubnetIds"):
                obj = CloudBaseRunVpcSubnet()
                obj._deserialize(item)
                self._SubnetIds.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunResourceRequest(AbstractModel):
    """DescribeCloudBaseRunResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunResourceResponse(AbstractModel):
    """DescribeCloudBaseRunResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterStatus: 集群状态(creating/succ)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStatus: str
        :param _VirtualClusterId: 虚拟集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualClusterId: str
        :param _VpcId: vpc id信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _SubnetIds: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of CloudBaseRunVpcSubnet
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterStatus = None
        self._VirtualClusterId = None
        self._VpcId = None
        self._Region = None
        self._SubnetIds = None
        self._RequestId = None

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def VirtualClusterId(self):
        return self._VirtualClusterId

    @VirtualClusterId.setter
    def VirtualClusterId(self, VirtualClusterId):
        self._VirtualClusterId = VirtualClusterId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterStatus = params.get("ClusterStatus")
        self._VirtualClusterId = params.get("VirtualClusterId")
        self._VpcId = params.get("VpcId")
        self._Region = params.get("Region")
        if params.get("SubnetIds") is not None:
            self._SubnetIds = []
            for item in params.get("SubnetIds"):
                obj = CloudBaseRunVpcSubnet()
                obj._deserialize(item)
                self._SubnetIds.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunServerDomainNameRequest(AbstractModel):
    """DescribeCloudBaseRunServerDomainName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerName: 服务名
        :type ServerName: str
        :param _UserEnvId: 环境Id
        :type UserEnvId: str
        :param _UserUin: 用户Uin
        :type UserUin: str
        :param _ExternalId: 外部Id
        :type ExternalId: str
        """
        self._ServerName = None
        self._UserEnvId = None
        self._UserUin = None
        self._ExternalId = None

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def UserEnvId(self):
        return self._UserEnvId

    @UserEnvId.setter
    def UserEnvId(self, UserEnvId):
        self._UserEnvId = UserEnvId

    @property
    def UserUin(self):
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def ExternalId(self):
        return self._ExternalId

    @ExternalId.setter
    def ExternalId(self, ExternalId):
        self._ExternalId = ExternalId


    def _deserialize(self, params):
        self._ServerName = params.get("ServerName")
        self._UserEnvId = params.get("UserEnvId")
        self._UserUin = params.get("UserUin")
        self._ExternalId = params.get("ExternalId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunServerDomainNameResponse(AbstractModel):
    """DescribeCloudBaseRunServerDomainName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PublicDomain: 公网服务域名
        :type PublicDomain: str
        :param _InternalDomain: 内部服务域名
        :type InternalDomain: str
        :param _DomainName: 弃用
        :type DomainName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PublicDomain = None
        self._InternalDomain = None
        self._DomainName = None
        self._RequestId = None

    @property
    def PublicDomain(self):
        return self._PublicDomain

    @PublicDomain.setter
    def PublicDomain(self, PublicDomain):
        self._PublicDomain = PublicDomain

    @property
    def InternalDomain(self):
        return self._InternalDomain

    @InternalDomain.setter
    def InternalDomain(self, InternalDomain):
        self._InternalDomain = InternalDomain

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PublicDomain = params.get("PublicDomain")
        self._InternalDomain = params.get("InternalDomain")
        self._DomainName = params.get("DomainName")
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunServerRequest(AbstractModel):
    """DescribeCloudBaseRunServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerName: 服务名称
        :type ServerName: str
        :param _Offset: 分页偏移
        :type Offset: int
        :param _Limit: 分页数量
        :type Limit: int
        :param _VersionName: 版本名字（精确匹配）
        :type VersionName: str
        """
        self._EnvId = None
        self._ServerName = None
        self._Offset = None
        self._Limit = None
        self._VersionName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunServerResponse(AbstractModel):
    """DescribeCloudBaseRunServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _VersionItems: 版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionItems: list of CloudBaseRunServerVersionItem
        :param _ServerName: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param _IsPublic: 是否对于外网开放
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublic: bool
        :param _ImageRepo: 镜像仓库
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageRepo: str
        :param _TrafficType: 流量配置的类型（FLOW,URL_PARAMS)
注意：此字段可能返回 null，表示取不到有效值。
        :type TrafficType: str
        :param _SourceType: 服务创建类型，默认为空，一键部署为oneclick
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VersionItems = None
        self._ServerName = None
        self._IsPublic = None
        self._ImageRepo = None
        self._TrafficType = None
        self._SourceType = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VersionItems(self):
        return self._VersionItems

    @VersionItems.setter
    def VersionItems(self, VersionItems):
        self._VersionItems = VersionItems

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def ImageRepo(self):
        return self._ImageRepo

    @ImageRepo.setter
    def ImageRepo(self, ImageRepo):
        self._ImageRepo = ImageRepo

    @property
    def TrafficType(self):
        return self._TrafficType

    @TrafficType.setter
    def TrafficType(self, TrafficType):
        self._TrafficType = TrafficType

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VersionItems") is not None:
            self._VersionItems = []
            for item in params.get("VersionItems"):
                obj = CloudBaseRunServerVersionItem()
                obj._deserialize(item)
                self._VersionItems.append(obj)
        self._ServerName = params.get("ServerName")
        self._IsPublic = params.get("IsPublic")
        self._ImageRepo = params.get("ImageRepo")
        self._TrafficType = params.get("TrafficType")
        self._SourceType = params.get("SourceType")
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunServerVersionRequest(AbstractModel):
    """DescribeCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerName: 服务名称
        :type ServerName: str
        :param _VersionName: 版本名称
        :type VersionName: str
        """
        self._EnvId = None
        self._ServerName = None
        self._VersionName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunServerVersionResponse(AbstractModel):
    """DescribeCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名称
        :type VersionName: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _DockerfilePath: Dockefile的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerfilePath: str
        :param _BuildDir: DockerBuild的目录
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildDir: str
        :param _Cpu: 请使用CPUSize
        :type Cpu: float
        :param _Mem: 请使用MemSize
        :type Mem: float
        :param _MinNum: 副本最小值
        :type MinNum: int
        :param _MaxNum: 副本最大值
        :type MaxNum: int
        :param _PolicyType: 策略类型
        :type PolicyType: str
        :param _PolicyThreshold: 策略阈值
        :type PolicyThreshold: float
        :param _EnvParams: 环境变量
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvParams: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param _VersionIP: 版本的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionIP: str
        :param _VersionPort: 版本的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionPort: int
        :param _Status: 版本状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _PackageName: 代码包的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param _PackageVersion: 代码版本的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param _UploadType: 枚举（package/repository/image)
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadType: str
        :param _RepoType: Repo的类型(gitlab/github/coding)
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: str
        :param _Repo: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Repo: str
        :param _Branch: 分支
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        :param _ServerName: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param _IsPublic: 是否对于外网开放
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublic: bool
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetIds: 子网实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param _CustomLogs: 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogs: str
        :param _ContainerPort: 监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerPort: int
        :param _InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param _ImageUrl: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param _CpuSize: CPU 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuSize: float
        :param _MemSize: MEM 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: float
        :param _HasDockerfile: 是否有Dockerfile：0-default has, 1-has, 2-has not
注意：此字段可能返回 null，表示取不到有效值。
        :type HasDockerfile: int
        :param _BaseImage: 基础镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseImage: str
        :param _EntryPoint: 容器启动入口命令
注意：此字段可能返回 null，表示取不到有效值。
        :type EntryPoint: str
        :param _RepoLanguage: 仓库语言
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoLanguage: str
        :param _PolicyDetail: 自动扩缩容策略组
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDetail: list of HpaPolicy
        :param _TkeClusterInfo: Tke集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TkeClusterInfo: :class:`tencentcloud.tcb.v20180608.models.TkeClusterInfo`
        :param _TkeWorkloadType: 版本工作负载类型；deployment/deamonset
注意：此字段可能返回 null，表示取不到有效值。
        :type TkeWorkloadType: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionName = None
        self._Remark = None
        self._DockerfilePath = None
        self._BuildDir = None
        self._Cpu = None
        self._Mem = None
        self._MinNum = None
        self._MaxNum = None
        self._PolicyType = None
        self._PolicyThreshold = None
        self._EnvParams = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._VersionIP = None
        self._VersionPort = None
        self._Status = None
        self._PackageName = None
        self._PackageVersion = None
        self._UploadType = None
        self._RepoType = None
        self._Repo = None
        self._Branch = None
        self._ServerName = None
        self._IsPublic = None
        self._VpcId = None
        self._SubnetIds = None
        self._CustomLogs = None
        self._ContainerPort = None
        self._InitialDelaySeconds = None
        self._ImageUrl = None
        self._CpuSize = None
        self._MemSize = None
        self._HasDockerfile = None
        self._BaseImage = None
        self._EntryPoint = None
        self._RepoLanguage = None
        self._PolicyDetail = None
        self._TkeClusterInfo = None
        self._TkeWorkloadType = None
        self._RequestId = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DockerfilePath(self):
        return self._DockerfilePath

    @DockerfilePath.setter
    def DockerfilePath(self, DockerfilePath):
        self._DockerfilePath = DockerfilePath

    @property
    def BuildDir(self):
        return self._BuildDir

    @BuildDir.setter
    def BuildDir(self, BuildDir):
        self._BuildDir = BuildDir

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def MinNum(self):
        return self._MinNum

    @MinNum.setter
    def MinNum(self, MinNum):
        self._MinNum = MinNum

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyThreshold(self):
        return self._PolicyThreshold

    @PolicyThreshold.setter
    def PolicyThreshold(self, PolicyThreshold):
        self._PolicyThreshold = PolicyThreshold

    @property
    def EnvParams(self):
        return self._EnvParams

    @EnvParams.setter
    def EnvParams(self, EnvParams):
        self._EnvParams = EnvParams

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def VersionIP(self):
        return self._VersionIP

    @VersionIP.setter
    def VersionIP(self, VersionIP):
        self._VersionIP = VersionIP

    @property
    def VersionPort(self):
        return self._VersionPort

    @VersionPort.setter
    def VersionPort(self, VersionPort):
        self._VersionPort = VersionPort

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def Repo(self):
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def Branch(self):
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def CustomLogs(self):
        return self._CustomLogs

    @CustomLogs.setter
    def CustomLogs(self, CustomLogs):
        self._CustomLogs = CustomLogs

    @property
    def ContainerPort(self):
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CpuSize(self):
        return self._CpuSize

    @CpuSize.setter
    def CpuSize(self, CpuSize):
        self._CpuSize = CpuSize

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def HasDockerfile(self):
        return self._HasDockerfile

    @HasDockerfile.setter
    def HasDockerfile(self, HasDockerfile):
        self._HasDockerfile = HasDockerfile

    @property
    def BaseImage(self):
        return self._BaseImage

    @BaseImage.setter
    def BaseImage(self, BaseImage):
        self._BaseImage = BaseImage

    @property
    def EntryPoint(self):
        return self._EntryPoint

    @EntryPoint.setter
    def EntryPoint(self, EntryPoint):
        self._EntryPoint = EntryPoint

    @property
    def RepoLanguage(self):
        return self._RepoLanguage

    @RepoLanguage.setter
    def RepoLanguage(self, RepoLanguage):
        self._RepoLanguage = RepoLanguage

    @property
    def PolicyDetail(self):
        return self._PolicyDetail

    @PolicyDetail.setter
    def PolicyDetail(self, PolicyDetail):
        self._PolicyDetail = PolicyDetail

    @property
    def TkeClusterInfo(self):
        return self._TkeClusterInfo

    @TkeClusterInfo.setter
    def TkeClusterInfo(self, TkeClusterInfo):
        self._TkeClusterInfo = TkeClusterInfo

    @property
    def TkeWorkloadType(self):
        return self._TkeWorkloadType

    @TkeWorkloadType.setter
    def TkeWorkloadType(self, TkeWorkloadType):
        self._TkeWorkloadType = TkeWorkloadType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._Remark = params.get("Remark")
        self._DockerfilePath = params.get("DockerfilePath")
        self._BuildDir = params.get("BuildDir")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._MinNum = params.get("MinNum")
        self._MaxNum = params.get("MaxNum")
        self._PolicyType = params.get("PolicyType")
        self._PolicyThreshold = params.get("PolicyThreshold")
        self._EnvParams = params.get("EnvParams")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._VersionIP = params.get("VersionIP")
        self._VersionPort = params.get("VersionPort")
        self._Status = params.get("Status")
        self._PackageName = params.get("PackageName")
        self._PackageVersion = params.get("PackageVersion")
        self._UploadType = params.get("UploadType")
        self._RepoType = params.get("RepoType")
        self._Repo = params.get("Repo")
        self._Branch = params.get("Branch")
        self._ServerName = params.get("ServerName")
        self._IsPublic = params.get("IsPublic")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._CustomLogs = params.get("CustomLogs")
        self._ContainerPort = params.get("ContainerPort")
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        self._ImageUrl = params.get("ImageUrl")
        self._CpuSize = params.get("CpuSize")
        self._MemSize = params.get("MemSize")
        self._HasDockerfile = params.get("HasDockerfile")
        self._BaseImage = params.get("BaseImage")
        self._EntryPoint = params.get("EntryPoint")
        self._RepoLanguage = params.get("RepoLanguage")
        if params.get("PolicyDetail") is not None:
            self._PolicyDetail = []
            for item in params.get("PolicyDetail"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self._PolicyDetail.append(obj)
        if params.get("TkeClusterInfo") is not None:
            self._TkeClusterInfo = TkeClusterInfo()
            self._TkeClusterInfo._deserialize(params.get("TkeClusterInfo"))
        self._TkeWorkloadType = params.get("TkeWorkloadType")
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunVersionRequest(AbstractModel):
    """DescribeCloudBaseRunVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerName: 服务名称
        :type ServerName: str
        :param _VersionName: 版本名称
        :type VersionName: str
        """
        self._EnvId = None
        self._ServerName = None
        self._VersionName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunVersionResponse(AbstractModel):
    """DescribeCloudBaseRunVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名称
        :type VersionName: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _DockerfilePath: Dockefile的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerfilePath: str
        :param _BuildDir: DockerBuild的目录
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildDir: str
        :param _MinNum: 副本最小值
        :type MinNum: int
        :param _MaxNum: 副本最大值
        :type MaxNum: int
        :param _PolicyType: 策略类型
        :type PolicyType: str
        :param _PolicyThreshold: 策略阈值
        :type PolicyThreshold: float
        :param _EnvParams: 环境变量
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvParams: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param _VersionIP: 版本的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionIP: str
        :param _VersionPort: 版本的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionPort: int
        :param _Status: 版本状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _PackageName: 代码包的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param _PackageVersion: 代码版本的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param _UploadType: 枚举（package/repository/image)
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadType: str
        :param _RepoType: Repo的类型(coding/gitlab/github/coding)
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoType: str
        :param _Repo: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Repo: str
        :param _Branch: 分支
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        :param _ServerName: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param _IsPublic: 是否对于外网开放
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublic: bool
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetIds: 子网实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param _CustomLogs: 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogs: str
        :param _ContainerPort: 监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerPort: int
        :param _InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param _ImageUrl: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param _CpuSize: CPU 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuSize: float
        :param _MemSize: MEM 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: float
        :param _PolicyDetail: 扩缩容策略详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDetail: list of HpaPolicy
        :param _Cpu: Cpu的Request值
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: float
        :param _Mem: Mem的Request值
注意：此字段可能返回 null，表示取不到有效值。
        :type Mem: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionName = None
        self._Remark = None
        self._DockerfilePath = None
        self._BuildDir = None
        self._MinNum = None
        self._MaxNum = None
        self._PolicyType = None
        self._PolicyThreshold = None
        self._EnvParams = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._VersionIP = None
        self._VersionPort = None
        self._Status = None
        self._PackageName = None
        self._PackageVersion = None
        self._UploadType = None
        self._RepoType = None
        self._Repo = None
        self._Branch = None
        self._ServerName = None
        self._IsPublic = None
        self._VpcId = None
        self._SubnetIds = None
        self._CustomLogs = None
        self._ContainerPort = None
        self._InitialDelaySeconds = None
        self._ImageUrl = None
        self._CpuSize = None
        self._MemSize = None
        self._PolicyDetail = None
        self._Cpu = None
        self._Mem = None
        self._RequestId = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DockerfilePath(self):
        return self._DockerfilePath

    @DockerfilePath.setter
    def DockerfilePath(self, DockerfilePath):
        self._DockerfilePath = DockerfilePath

    @property
    def BuildDir(self):
        return self._BuildDir

    @BuildDir.setter
    def BuildDir(self, BuildDir):
        self._BuildDir = BuildDir

    @property
    def MinNum(self):
        return self._MinNum

    @MinNum.setter
    def MinNum(self, MinNum):
        self._MinNum = MinNum

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyThreshold(self):
        return self._PolicyThreshold

    @PolicyThreshold.setter
    def PolicyThreshold(self, PolicyThreshold):
        self._PolicyThreshold = PolicyThreshold

    @property
    def EnvParams(self):
        return self._EnvParams

    @EnvParams.setter
    def EnvParams(self, EnvParams):
        self._EnvParams = EnvParams

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def VersionIP(self):
        return self._VersionIP

    @VersionIP.setter
    def VersionIP(self, VersionIP):
        self._VersionIP = VersionIP

    @property
    def VersionPort(self):
        return self._VersionPort

    @VersionPort.setter
    def VersionPort(self, VersionPort):
        self._VersionPort = VersionPort

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def Repo(self):
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def Branch(self):
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def CustomLogs(self):
        return self._CustomLogs

    @CustomLogs.setter
    def CustomLogs(self, CustomLogs):
        self._CustomLogs = CustomLogs

    @property
    def ContainerPort(self):
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CpuSize(self):
        return self._CpuSize

    @CpuSize.setter
    def CpuSize(self, CpuSize):
        self._CpuSize = CpuSize

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def PolicyDetail(self):
        return self._PolicyDetail

    @PolicyDetail.setter
    def PolicyDetail(self, PolicyDetail):
        self._PolicyDetail = PolicyDetail

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._Remark = params.get("Remark")
        self._DockerfilePath = params.get("DockerfilePath")
        self._BuildDir = params.get("BuildDir")
        self._MinNum = params.get("MinNum")
        self._MaxNum = params.get("MaxNum")
        self._PolicyType = params.get("PolicyType")
        self._PolicyThreshold = params.get("PolicyThreshold")
        self._EnvParams = params.get("EnvParams")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._VersionIP = params.get("VersionIP")
        self._VersionPort = params.get("VersionPort")
        self._Status = params.get("Status")
        self._PackageName = params.get("PackageName")
        self._PackageVersion = params.get("PackageVersion")
        self._UploadType = params.get("UploadType")
        self._RepoType = params.get("RepoType")
        self._Repo = params.get("Repo")
        self._Branch = params.get("Branch")
        self._ServerName = params.get("ServerName")
        self._IsPublic = params.get("IsPublic")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._CustomLogs = params.get("CustomLogs")
        self._ContainerPort = params.get("ContainerPort")
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        self._ImageUrl = params.get("ImageUrl")
        self._CpuSize = params.get("CpuSize")
        self._MemSize = params.get("MemSize")
        if params.get("PolicyDetail") is not None:
            self._PolicyDetail = []
            for item in params.get("PolicyDetail"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self._PolicyDetail.append(obj)
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseRunVersionRsByConditionRequest(AbstractModel):
    """DescribeCloudBaseRunVersionRsByCondition请求参数结构体

    """


class DescribeCloudBaseRunVersionRsByConditionResponse(AbstractModel):
    """DescribeCloudBaseRunVersionRsByCondition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeCloudBaseRunVersionSnapshotRequest(AbstractModel):
    """DescribeCloudBaseRunVersionSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerName: 服务名
        :type ServerName: str
        :param _VersionName: 版本名
        :type VersionName: str
        :param _EnvId: 环境id
        :type EnvId: str
        :param _SnapshotName: 版本历史名
        :type SnapshotName: str
        :param _Offset: 偏移量。默认0
        :type Offset: int
        :param _Limit: 限制大小。默认10，最大20
        :type Limit: int
        """
        self._ServerName = None
        self._VersionName = None
        self._EnvId = None
        self._SnapshotName = None
        self._Offset = None
        self._Limit = None

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        self._EnvId = params.get("EnvId")
        self._SnapshotName = params.get("SnapshotName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseRunVersionSnapshotResponse(AbstractModel):
    """DescribeCloudBaseRunVersionSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Snapshots: 版本历史
注意：此字段可能返回 null，表示取不到有效值。
        :type Snapshots: list of CloudRunServiceSimpleVersionSnapshot
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Snapshots = None
        self._RequestId = None

    @property
    def Snapshots(self):
        return self._Snapshots

    @Snapshots.setter
    def Snapshots(self, Snapshots):
        self._Snapshots = Snapshots

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Snapshots") is not None:
            self._Snapshots = []
            for item in params.get("Snapshots"):
                obj = CloudRunServiceSimpleVersionSnapshot()
                obj._deserialize(item)
                self._Snapshots.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCurveDataRequest(AbstractModel):
    """DescribeCurveData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _MetricName: <li> 指标名: </li>
<li> StorageRead: 存储读请求次数 </li>
<li> StorageWrite: 存储写请求次数 </li>
<li> StorageCdnOriginFlux: CDN回源流量, 单位字节 </li>
<li> CDNFlux: CDN回源流量, 单位字节 </li>
<li> FunctionInvocation: 云函数调用次数 </li>
<li> FunctionGBs: 云函数资源使用量, 单位Mb*Ms </li>
<li> FunctionFlux: 云函数流量, 单位千字节(KB) </li>
<li> FunctionError: 云函数调用错误次数 </li>
<li> FunctionDuration: 云函数运行时间, 单位毫秒 </li>
<li> DbRead: 数据库读请求数 </li>
<li> DbWrite: 数据库写请求数 </li>
<li> DbCostTime10ms: 数据库耗时在10ms~50ms请求数 </li>
<li> DbCostTime50ms: 数据库耗时在50ms~100ms请求数 </li>
<li> DbCostTime100ms: 数据库耗时在100ms以上请求数 </li>
<li> TkeCpuRatio: 容器CPU占用率 </li>
<li> TkeMemRatio: 容器内存占用率 </li>
<li> TkeCpuUsed: 容器CPU使用量 </li>
<li> TkeMemUsed: 容器内存使用量 </li>
<li> TkeInvokeNum: 调用量 </li>
<li> FunctionConcurrentExecutions: 云函数并发执行个数</li>
<li> FunctionIdleProvisioned: 云函数预置并发闲置量 </li>
<li> FunctionConcurrencyMemoryMB: 云函数并发执行内存量 </li>
<li> FunctionThrottle: 云函数受限次数 </li>
<li> FunctionProvisionedConcurrency: 云函数预置并发 </li>
        :type MetricName: str
        :param _StartTime: 开始时间，如2018-08-24 10:50:00, 开始时间需要早于结束时间至少五分钟(原因是因为目前统计粒度最小是5分钟).
        :type StartTime: str
        :param _EndTime: 结束时间，如2018-08-24 10:50:00, 结束时间需要晚于开始时间至少五分钟(原因是因为目前统计粒度最小是5分钟)..
        :type EndTime: str
        :param _ResourceID: 资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocation, FunctionGBs, FunctionFlux, FunctionError, FunctionDuration)、容器托管（服务名称）, 如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传.如果想查询数据库某个集合相关信息，传入集合名称
        :type ResourceID: str
        """
        self._EnvId = None
        self._MetricName = None
        self._StartTime = None
        self._EndTime = None
        self._ResourceID = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

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
    def ResourceID(self):
        return self._ResourceID

    @ResourceID.setter
    def ResourceID(self, ResourceID):
        self._ResourceID = ResourceID


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._MetricName = params.get("MetricName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ResourceID = params.get("ResourceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCurveDataResponse(AbstractModel):
    """DescribeCurveData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间, 会根据数据的统计周期进行取整.
        :type StartTime: str
        :param _EndTime: 结束时间, 会根据数据的统计周期进行取整.
        :type EndTime: str
        :param _MetricName: 指标名.
        :type MetricName: str
        :param _Period: 统计周期(单位秒), 当时间区间为1天内, 统计周期为5分钟; 当时间区间选择为1天以上, 15天以下, 统计周期为1小时; 当时间区间选择为15天以上, 180天以下, 统计周期为1天.
        :type Period: int
        :param _Values: 有效的监控数据, 每个有效监控数据的上报时间可以从时间数组中的对应位置上获取到.
        :type Values: list of int
        :param _Time: 时间数据, 标识监控数据Values中的点是哪个时间段上报的.
        :type Time: list of int
        :param _NewValues: 有效的监控数据, 每个有效监控数据的上报时间可以从时间数组中的对应位置上获取到.
        :type NewValues: list of float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Period = None
        self._Values = None
        self._Time = None
        self._NewValues = None
        self._RequestId = None

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
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def NewValues(self):
        return self._NewValues

    @NewValues.setter
    def NewValues(self, NewValues):
        self._NewValues = NewValues

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._Values = params.get("Values")
        self._Time = params.get("Time")
        self._NewValues = params.get("NewValues")
        self._RequestId = params.get("RequestId")


class DescribeDatabaseACLRequest(AbstractModel):
    """DescribeDatabaseACL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _CollectionName: 集合名称
        :type CollectionName: str
        """
        self._EnvId = None
        self._CollectionName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionName(self):
        return self._CollectionName

    @CollectionName.setter
    def CollectionName(self, CollectionName):
        self._CollectionName = CollectionName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CollectionName = params.get("CollectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseACLResponse(AbstractModel):
    """DescribeDatabaseACL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AclTag: 权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
        :type AclTag: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AclTag = None
        self._RequestId = None

    @property
    def AclTag(self):
        return self._AclTag

    @AclTag.setter
    def AclTag(self, AclTag):
        self._AclTag = AclTag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AclTag = params.get("AclTag")
        self._RequestId = params.get("RequestId")


class DescribeDownloadFileRequest(AbstractModel):
    """DescribeDownloadFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeUri: 代码uri，格式如：extension://abcdefhhxxx.zip，对应 DescribeExtensionUploadInfo 接口的返回值
        :type CodeUri: str
        """
        self._CodeUri = None

    @property
    def CodeUri(self):
        return self._CodeUri

    @CodeUri.setter
    def CodeUri(self, CodeUri):
        self._CodeUri = CodeUri


    def _deserialize(self, params):
        self._CodeUri = params.get("CodeUri")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDownloadFileResponse(AbstractModel):
    """DescribeDownloadFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FilePath: 文件路径，该字段已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param _CustomKey: 加密key，用于计算下载加密文件的header。参考SSE-C https://cloud.tencent.com/document/product/436/7728#sse-c
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomKey: str
        :param _DownloadUrl: 下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FilePath = None
        self._CustomKey = None
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def CustomKey(self):
        return self._CustomKey

    @CustomKey.setter
    def CustomKey(self, CustomKey):
        self._CustomKey = CustomKey

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FilePath = params.get("FilePath")
        self._CustomKey = params.get("CustomKey")
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeEndUserLoginStatisticRequest(AbstractModel):
    """DescribeEndUserLoginStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _Source: 终端用户来源
<li> qcloud </li>
<li>miniapp</li>
        :type Source: str
        """
        self._EnvId = None
        self._Source = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEndUserLoginStatisticResponse(AbstractModel):
    """DescribeEndUserLoginStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginStatistics: 环境终端用户新增与登录统计
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginStatistics: list of LoginStatistic
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoginStatistics = None
        self._RequestId = None

    @property
    def LoginStatistics(self):
        return self._LoginStatistics

    @LoginStatistics.setter
    def LoginStatistics(self, LoginStatistics):
        self._LoginStatistics = LoginStatistics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoginStatistics") is not None:
            self._LoginStatistics = []
            for item in params.get("LoginStatistics"):
                obj = LoginStatistic()
                obj._deserialize(item)
                self._LoginStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEndUserStatisticRequest(AbstractModel):
    """DescribeEndUserStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEndUserStatisticResponse(AbstractModel):
    """DescribeEndUserStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlatformStatistics: 终端用户各平台统计
注意：此字段可能返回 null，表示取不到有效值。
        :type PlatformStatistics: list of PlatformStatistic
        :param _TotalCount: 终端用户总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlatformStatistics = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PlatformStatistics(self):
        return self._PlatformStatistics

    @PlatformStatistics.setter
    def PlatformStatistics(self, PlatformStatistics):
        self._PlatformStatistics = PlatformStatistics

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
        if params.get("PlatformStatistics") is not None:
            self._PlatformStatistics = []
            for item in params.get("PlatformStatistics"):
                obj = PlatformStatistic()
                obj._deserialize(item)
                self._PlatformStatistics.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEndUsersRequest(AbstractModel):
    """DescribeEndUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 开发者的环境ID
        :type EnvId: str
        :param _Offset: 可选参数，偏移量，默认 0
        :type Offset: int
        :param _Limit: 可选参数，拉取数量，默认 20
        :type Limit: int
        :param _UUIds: 按照 uuid 列表过滤，最大个数为100
        :type UUIds: list of str
        """
        self._EnvId = None
        self._Offset = None
        self._Limit = None
        self._UUIds = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def UUIds(self):
        return self._UUIds

    @UUIds.setter
    def UUIds(self, UUIds):
        self._UUIds = UUIds


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._UUIds = params.get("UUIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEndUsersResponse(AbstractModel):
    """DescribeEndUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 用户总数
        :type Total: int
        :param _Users: 用户列表
        :type Users: list of EndUserInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Users = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = EndUserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvDealRegionRequest(AbstractModel):
    """DescribeEnvDealRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _DealType: 订单类型：
ENV_PREPAY_MINIAPP= 预付费环境(微信小程序)
ENV_PREPAY_CLOUD= 预付费环境(腾讯云)
ENV_POSTPAY = 后付费环境
HOSTING_PREPAY = 预付费静态托管
PACKAGE=套餐包
        :type DealType: str
        :param _DealAction: 下单类型：
CREATE = 新购
RENEW = 续费
MODIFY = 套餐调整(升级/降级)
REFUND = 退费
        :type DealAction: str
        :param _DealRegion: 下单地域：
ap-guangzhou = 广州地域
ap-shanghai = 上海地域
ap-beijing = 北京地域
        :type DealRegion: str
        """
        self._EnvId = None
        self._DealType = None
        self._DealAction = None
        self._DealRegion = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def DealType(self):
        return self._DealType

    @DealType.setter
    def DealType(self, DealType):
        self._DealType = DealType

    @property
    def DealAction(self):
        return self._DealAction

    @DealAction.setter
    def DealAction(self, DealAction):
        self._DealAction = DealAction

    @property
    def DealRegion(self):
        return self._DealRegion

    @DealRegion.setter
    def DealRegion(self, DealRegion):
        self._DealRegion = DealRegion


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._DealType = params.get("DealType")
        self._DealAction = params.get("DealAction")
        self._DealRegion = params.get("DealRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvDealRegionResponse(AbstractModel):
    """DescribeEnvDealRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Region: 下单region
        :type Region: str
        :param _Zone: 下单zone
        :type Zone: str
        :param _RegionId: 下单regionId
        :type RegionId: int
        :param _ZoneId: 下单zoneId
        :type ZoneId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Region = None
        self._Zone = None
        self._RegionId = None
        self._ZoneId = None
        self._RequestId = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._RequestId = params.get("RequestId")


class DescribeEnvFreeQuotaRequest(AbstractModel):
    """DescribeEnvFreeQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ResourceTypes: 资源类型：可选值：CDN, COS, FLEXDB, HOSTING, SCF
不传则返回全部资源指标
        :type ResourceTypes: list of str
        """
        self._EnvId = None
        self._ResourceTypes = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ResourceTypes(self):
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ResourceTypes = params.get("ResourceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvFreeQuotaResponse(AbstractModel):
    """DescribeEnvFreeQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QuotaItems: 免费抵扣配额详情
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaItems: list of PostpayEnvQuota
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QuotaItems = None
        self._RequestId = None

    @property
    def QuotaItems(self):
        return self._QuotaItems

    @QuotaItems.setter
    def QuotaItems(self, QuotaItems):
        self._QuotaItems = QuotaItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QuotaItems") is not None:
            self._QuotaItems = []
            for item in params.get("QuotaItems"):
                obj = PostpayEnvQuota()
                obj._deserialize(item)
                self._QuotaItems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvLimitRequest(AbstractModel):
    """DescribeEnvLimit请求参数结构体

    """


class DescribeEnvLimitResponse(AbstractModel):
    """DescribeEnvLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MaxEnvNum: 环境总数上限
        :type MaxEnvNum: int
        :param _CurrentEnvNum: 目前环境总数
        :type CurrentEnvNum: int
        :param _MaxFreeEnvNum: 免费环境数量上限
        :type MaxFreeEnvNum: int
        :param _CurrentFreeEnvNum: 目前免费环境数量
        :type CurrentFreeEnvNum: int
        :param _MaxDeleteTotal: 总计允许销毁环境次数上限
        :type MaxDeleteTotal: int
        :param _CurrentDeleteTotal: 目前已销毁环境次数
        :type CurrentDeleteTotal: int
        :param _MaxDeleteMonthly: 每月允许销毁环境次数上限
        :type MaxDeleteMonthly: int
        :param _CurrentDeleteMonthly: 本月已销毁环境次数
        :type CurrentDeleteMonthly: int
        :param _MaxFreeTrialNum: 微信网关体验版可购买月份数
        :type MaxFreeTrialNum: int
        :param _CurrentFreeTrialNum: 微信网关体验版已购买月份数
        :type CurrentFreeTrialNum: int
        :param _ChangePayTotal: 转支付限额总数
        :type ChangePayTotal: int
        :param _CurrentChangePayTotal: 当前已用转支付次数
        :type CurrentChangePayTotal: int
        :param _ChangePayMonthly: 转支付每月限额
        :type ChangePayMonthly: int
        :param _CurrentChangePayMonthly: 本月已用转支付额度
        :type CurrentChangePayMonthly: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MaxEnvNum = None
        self._CurrentEnvNum = None
        self._MaxFreeEnvNum = None
        self._CurrentFreeEnvNum = None
        self._MaxDeleteTotal = None
        self._CurrentDeleteTotal = None
        self._MaxDeleteMonthly = None
        self._CurrentDeleteMonthly = None
        self._MaxFreeTrialNum = None
        self._CurrentFreeTrialNum = None
        self._ChangePayTotal = None
        self._CurrentChangePayTotal = None
        self._ChangePayMonthly = None
        self._CurrentChangePayMonthly = None
        self._RequestId = None

    @property
    def MaxEnvNum(self):
        return self._MaxEnvNum

    @MaxEnvNum.setter
    def MaxEnvNum(self, MaxEnvNum):
        self._MaxEnvNum = MaxEnvNum

    @property
    def CurrentEnvNum(self):
        return self._CurrentEnvNum

    @CurrentEnvNum.setter
    def CurrentEnvNum(self, CurrentEnvNum):
        self._CurrentEnvNum = CurrentEnvNum

    @property
    def MaxFreeEnvNum(self):
        return self._MaxFreeEnvNum

    @MaxFreeEnvNum.setter
    def MaxFreeEnvNum(self, MaxFreeEnvNum):
        self._MaxFreeEnvNum = MaxFreeEnvNum

    @property
    def CurrentFreeEnvNum(self):
        return self._CurrentFreeEnvNum

    @CurrentFreeEnvNum.setter
    def CurrentFreeEnvNum(self, CurrentFreeEnvNum):
        self._CurrentFreeEnvNum = CurrentFreeEnvNum

    @property
    def MaxDeleteTotal(self):
        return self._MaxDeleteTotal

    @MaxDeleteTotal.setter
    def MaxDeleteTotal(self, MaxDeleteTotal):
        self._MaxDeleteTotal = MaxDeleteTotal

    @property
    def CurrentDeleteTotal(self):
        return self._CurrentDeleteTotal

    @CurrentDeleteTotal.setter
    def CurrentDeleteTotal(self, CurrentDeleteTotal):
        self._CurrentDeleteTotal = CurrentDeleteTotal

    @property
    def MaxDeleteMonthly(self):
        return self._MaxDeleteMonthly

    @MaxDeleteMonthly.setter
    def MaxDeleteMonthly(self, MaxDeleteMonthly):
        self._MaxDeleteMonthly = MaxDeleteMonthly

    @property
    def CurrentDeleteMonthly(self):
        return self._CurrentDeleteMonthly

    @CurrentDeleteMonthly.setter
    def CurrentDeleteMonthly(self, CurrentDeleteMonthly):
        self._CurrentDeleteMonthly = CurrentDeleteMonthly

    @property
    def MaxFreeTrialNum(self):
        return self._MaxFreeTrialNum

    @MaxFreeTrialNum.setter
    def MaxFreeTrialNum(self, MaxFreeTrialNum):
        self._MaxFreeTrialNum = MaxFreeTrialNum

    @property
    def CurrentFreeTrialNum(self):
        return self._CurrentFreeTrialNum

    @CurrentFreeTrialNum.setter
    def CurrentFreeTrialNum(self, CurrentFreeTrialNum):
        self._CurrentFreeTrialNum = CurrentFreeTrialNum

    @property
    def ChangePayTotal(self):
        return self._ChangePayTotal

    @ChangePayTotal.setter
    def ChangePayTotal(self, ChangePayTotal):
        self._ChangePayTotal = ChangePayTotal

    @property
    def CurrentChangePayTotal(self):
        return self._CurrentChangePayTotal

    @CurrentChangePayTotal.setter
    def CurrentChangePayTotal(self, CurrentChangePayTotal):
        self._CurrentChangePayTotal = CurrentChangePayTotal

    @property
    def ChangePayMonthly(self):
        return self._ChangePayMonthly

    @ChangePayMonthly.setter
    def ChangePayMonthly(self, ChangePayMonthly):
        self._ChangePayMonthly = ChangePayMonthly

    @property
    def CurrentChangePayMonthly(self):
        return self._CurrentChangePayMonthly

    @CurrentChangePayMonthly.setter
    def CurrentChangePayMonthly(self, CurrentChangePayMonthly):
        self._CurrentChangePayMonthly = CurrentChangePayMonthly

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MaxEnvNum = params.get("MaxEnvNum")
        self._CurrentEnvNum = params.get("CurrentEnvNum")
        self._MaxFreeEnvNum = params.get("MaxFreeEnvNum")
        self._CurrentFreeEnvNum = params.get("CurrentFreeEnvNum")
        self._MaxDeleteTotal = params.get("MaxDeleteTotal")
        self._CurrentDeleteTotal = params.get("CurrentDeleteTotal")
        self._MaxDeleteMonthly = params.get("MaxDeleteMonthly")
        self._CurrentDeleteMonthly = params.get("CurrentDeleteMonthly")
        self._MaxFreeTrialNum = params.get("MaxFreeTrialNum")
        self._CurrentFreeTrialNum = params.get("CurrentFreeTrialNum")
        self._ChangePayTotal = params.get("ChangePayTotal")
        self._CurrentChangePayTotal = params.get("CurrentChangePayTotal")
        self._ChangePayMonthly = params.get("ChangePayMonthly")
        self._CurrentChangePayMonthly = params.get("CurrentChangePayMonthly")
        self._RequestId = params.get("RequestId")


class DescribeEnvPostpaidDeductRequest(AbstractModel):
    """DescribeEnvPostpaidDeduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceTypes: 资源方列表
        :type ResourceTypes: list of str
        :param _EnvId: 环境id
        :type EnvId: str
        :param _StartTime: 查询开始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        """
        self._ResourceTypes = None
        self._EnvId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ResourceTypes(self):
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

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
        self._ResourceTypes = params.get("ResourceTypes")
        self._EnvId = params.get("EnvId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvPostpaidDeductResponse(AbstractModel):
    """DescribeEnvPostpaidDeduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PostPaidEnvDeductInfoList: 指标抵扣详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PostPaidEnvDeductInfoList: list of PostPaidEnvDeductInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PostPaidEnvDeductInfoList = None
        self._RequestId = None

    @property
    def PostPaidEnvDeductInfoList(self):
        return self._PostPaidEnvDeductInfoList

    @PostPaidEnvDeductInfoList.setter
    def PostPaidEnvDeductInfoList(self, PostPaidEnvDeductInfoList):
        self._PostPaidEnvDeductInfoList = PostPaidEnvDeductInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PostPaidEnvDeductInfoList") is not None:
            self._PostPaidEnvDeductInfoList = []
            for item in params.get("PostPaidEnvDeductInfoList"):
                obj = PostPaidEnvDeductInfo()
                obj._deserialize(item)
                self._PostPaidEnvDeductInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvsRequest(AbstractModel):
    """DescribeEnvs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID，如果传了这个参数则只返回该环境的相关信息
        :type EnvId: str
        :param _IsVisible: 指定Channels字段为可见渠道列表或不可见渠道列表
如只想获取渠道A的环境 就填写IsVisible= true,Channels = ["A"], 过滤渠道A拉取其他渠道环境时填写IsVisible= false,Channels = ["A"]
        :type IsVisible: bool
        :param _Channels: 渠道列表，代表可见或不可见渠道由IsVisible参数指定
        :type Channels: list of str
        """
        self._EnvId = None
        self._IsVisible = None
        self._Channels = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def IsVisible(self):
        return self._IsVisible

    @IsVisible.setter
    def IsVisible(self, IsVisible):
        self._IsVisible = IsVisible

    @property
    def Channels(self):
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._IsVisible = params.get("IsVisible")
        self._Channels = params.get("Channels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvsResponse(AbstractModel):
    """DescribeEnvs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvList: 环境信息列表
        :type EnvList: list of EnvInfo
        :param _Total: 环境个数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvList = None
        self._Total = None
        self._RequestId = None

    @property
    def EnvList(self):
        return self._EnvList

    @EnvList.setter
    def EnvList(self, EnvList):
        self._EnvList = EnvList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnvList") is not None:
            self._EnvList = []
            for item in params.get("EnvList"):
                obj = EnvInfo()
                obj._deserialize(item)
                self._EnvList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeExtensionUploadInfoRequest(AbstractModel):
    """DescribeExtensionUploadInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExtensionFiles: 待上传的文件
        :type ExtensionFiles: list of ExtensionFile
        """
        self._ExtensionFiles = None

    @property
    def ExtensionFiles(self):
        return self._ExtensionFiles

    @ExtensionFiles.setter
    def ExtensionFiles(self, ExtensionFiles):
        self._ExtensionFiles = ExtensionFiles


    def _deserialize(self, params):
        if params.get("ExtensionFiles") is not None:
            self._ExtensionFiles = []
            for item in params.get("ExtensionFiles"):
                obj = ExtensionFile()
                obj._deserialize(item)
                self._ExtensionFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtensionUploadInfoResponse(AbstractModel):
    """DescribeExtensionUploadInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FilesData: 待上传文件的信息数组
        :type FilesData: list of ExtensionFileInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FilesData = None
        self._RequestId = None

    @property
    def FilesData(self):
        return self._FilesData

    @FilesData.setter
    def FilesData(self, FilesData):
        self._FilesData = FilesData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FilesData") is not None:
            self._FilesData = []
            for item in params.get("FilesData"):
                obj = ExtensionFileInfo()
                obj._deserialize(item)
                self._FilesData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExtraPkgBillingInfoRequest(AbstractModel):
    """DescribeExtraPkgBillingInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 已购买增值包的环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtraPkgBillingInfoResponse(AbstractModel):
    """DescribeExtraPkgBillingInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvInfoList: 增值包计费信息列表
        :type EnvInfoList: list of EnvBillingInfoItem
        :param _Total: 增值包数目
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvInfoList = None
        self._Total = None
        self._RequestId = None

    @property
    def EnvInfoList(self):
        return self._EnvInfoList

    @EnvInfoList.setter
    def EnvInfoList(self, EnvInfoList):
        self._EnvInfoList = EnvInfoList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnvInfoList") is not None:
            self._EnvInfoList = []
            for item in params.get("EnvInfoList"):
                obj = EnvBillingInfoItem()
                obj._deserialize(item)
                self._EnvInfoList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeGatewayCurveDataRequest(AbstractModel):
    """DescribeGatewayCurveData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _GatewayId: 网关id
        :type GatewayId: str
        :param _MetricName: 监控类型 GWQps GWBandwidth GwHttpError GwHttp404 GwHttp502 GwConnect GwCircuit
        :type MetricName: str
        :param _StartTime: 监控起始时间
        :type StartTime: str
        :param _EndTime: 监控结束时间
        :type EndTime: str
        :param _GatewayVersion: 网关版本
        :type GatewayVersion: str
        :param _GatewayRoute: 网关路由名称
        :type GatewayRoute: str
        """
        self._EnvId = None
        self._GatewayId = None
        self._MetricName = None
        self._StartTime = None
        self._EndTime = None
        self._GatewayVersion = None
        self._GatewayRoute = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

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
    def GatewayVersion(self):
        return self._GatewayVersion

    @GatewayVersion.setter
    def GatewayVersion(self, GatewayVersion):
        self._GatewayVersion = GatewayVersion

    @property
    def GatewayRoute(self):
        return self._GatewayRoute

    @GatewayRoute.setter
    def GatewayRoute(self, GatewayRoute):
        self._GatewayRoute = GatewayRoute


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayId = params.get("GatewayId")
        self._MetricName = params.get("MetricName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._GatewayVersion = params.get("GatewayVersion")
        self._GatewayRoute = params.get("GatewayRoute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayCurveDataResponse(AbstractModel):
    """DescribeGatewayCurveData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricName: 监控类型
        :type MetricName: str
        :param _StartTime: 监控起始时间
        :type StartTime: str
        :param _EndTime: 监控结束时间
        :type EndTime: str
        :param _Period: 监控数据间隔
        :type Period: int
        :param _Values: 监控值
        :type Values: list of float
        :param _Time: 监控时间
        :type Time: list of int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricName = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None
        self._Values = None
        self._Time = None
        self._RequestId = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

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
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        self._Values = params.get("Values")
        self._Time = params.get("Time")
        self._RequestId = params.get("RequestId")


class DescribeGatewayVersionsRequest(AbstractModel):
    """DescribeGatewayVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _GatewayId: 网关id
        :type GatewayId: str
        :param _VersionName: 版本名
        :type VersionName: str
        """
        self._EnvId = None
        self._GatewayId = None
        self._VersionName = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayId = params.get("GatewayId")
        self._VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayVersionsResponse(AbstractModel):
    """DescribeGatewayVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关id
        :type GatewayId: str
        :param _TotalCount: 版本总数
        :type TotalCount: int
        :param _GatewayVersionItems: 版本信息详情
        :type GatewayVersionItems: list of GatewayVersionItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GatewayId = None
        self._TotalCount = None
        self._GatewayVersionItems = None
        self._RequestId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GatewayVersionItems(self):
        return self._GatewayVersionItems

    @GatewayVersionItems.setter
    def GatewayVersionItems(self, GatewayVersionItems):
        self._GatewayVersionItems = GatewayVersionItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._TotalCount = params.get("TotalCount")
        if params.get("GatewayVersionItems") is not None:
            self._GatewayVersionItems = []
            for item in params.get("GatewayVersionItems"):
                obj = GatewayVersionItem()
                obj._deserialize(item)
                self._GatewayVersionItems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGraphDataRequest(AbstractModel):
    """DescribeGraphData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _MetricName: 指标名: 
StorageRead: 存储读请求次数 
StorageWrite: 存储写请求次数 
StorageCdnOriginFlux: CDN回源流量, 单位字节 
CDNFlux: CDN回源流量, 单位字节 
FunctionInvocation: 云函数调用次数 
FunctionGBs: 云函数资源使用量, 单位Mb*Ms 
FunctionFlux: 云函数流量, 单位千字节(KB) 
FunctionError: 云函数调用错误次数 
FunctionDuration: 云函数运行时间, 单位毫秒 
DbRead: 数据库读请求数 
DbWrite: 数据库写请求数 
DbCostTime10ms: 数据库耗时在10ms~50ms请求数 
DbCostTime50ms: 数据库耗时在50ms~100ms请求数 
DbCostTime100ms: 数据库耗时在100ms以上请求数 
TkeCpuRatio: 容器CPU占用率 
TkeMemRatio: 容器内存占用率 
TkeCpuUsed: 容器CPU使用量 
TkeMemUsed: 容器内存使用量 
TkeInvokeNum: 调用量 
FunctionConcurrentExecutions: 云函数并发执行个数
FunctionIdleProvisioned: 云函数预置并发闲置量 
FunctionConcurrencyMemoryMB: 云函数并发执行内存量 
FunctionThrottle: 云函数受限次数 
FunctionProvisionedConcurrency: 云函数预置并发 
        :type MetricName: str
        :param _StartTime: 开始时间，如2018-08-24 10:50:00, 开始时间需要早于结束时间至少五分钟(原因是因为目前统计粒度最小是5分钟).
        :type StartTime: str
        :param _EndTime: 结束时间，如2018-08-24 10:50:00, 结束时间需要晚于开始时间至少五分钟(原因是因为目前统计粒度最小是5分钟)..
        :type EndTime: str
        :param _ResourceID: 资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocation, FunctionGBs, FunctionFlux, FunctionError, FunctionDuration)、容器托管（服务名称）, 如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传.如果想查询数据库某个集合相关信息，传入集合名称
        :type ResourceID: str
        """
        self._EnvId = None
        self._MetricName = None
        self._StartTime = None
        self._EndTime = None
        self._ResourceID = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

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
    def ResourceID(self):
        return self._ResourceID

    @ResourceID.setter
    def ResourceID(self, ResourceID):
        self._ResourceID = ResourceID


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._MetricName = params.get("MetricName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ResourceID = params.get("ResourceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGraphDataResponse(AbstractModel):
    """DescribeGraphData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间, 会根据数据的统计周期进行取整.
        :type StartTime: str
        :param _EndTime: 结束时间, 会根据数据的统计周期进行取整.
        :type EndTime: str
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Period: 统计周期(单位秒), 当时间区间为1天内, 统计周期为5分钟; 当时间区间选择为1天以上, 15天以下, 统计周期为1小时; 当时间区间选择为15天以上, 180天以下, 统计周期为1天.
        :type Period: int
        :param _Values: 有效的监控数据, 每个有效监控数据的上报时间可以从时间数组中的对应位置上获取到.
        :type Values: list of float
        :param _Time: 时间数据, 标识监控数据Values中的点是哪个时间段上报的.
        :type Time: list of int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Period = None
        self._Values = None
        self._Time = None
        self._RequestId = None

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
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._Values = params.get("Values")
        self._Time = params.get("Time")
        self._RequestId = params.get("RequestId")


class DescribeHostingDomainTaskRequest(AbstractModel):
    """DescribeHostingDomainTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostingDomainTaskResponse(AbstractModel):
    """DescribeHostingDomainTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: todo/doing/done/error
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribePostpayFreeQuotasRequest(AbstractModel):
    """DescribePostpayFreeQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePostpayFreeQuotasResponse(AbstractModel):
    """DescribePostpayFreeQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FreequotaInfoList: 免费量资源信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FreequotaInfoList: list of FreequotaInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FreequotaInfoList = None
        self._RequestId = None

    @property
    def FreequotaInfoList(self):
        return self._FreequotaInfoList

    @FreequotaInfoList.setter
    def FreequotaInfoList(self, FreequotaInfoList):
        self._FreequotaInfoList = FreequotaInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FreequotaInfoList") is not None:
            self._FreequotaInfoList = []
            for item in params.get("FreequotaInfoList"):
                obj = FreequotaInfo()
                obj._deserialize(item)
                self._FreequotaInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePostpayPackageFreeQuotasRequest(AbstractModel):
    """DescribePostpayPackageFreeQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _FreeQuotaType: 免费额度类型标识
        :type FreeQuotaType: str
        """
        self._EnvId = None
        self._FreeQuotaType = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def FreeQuotaType(self):
        return self._FreeQuotaType

    @FreeQuotaType.setter
    def FreeQuotaType(self, FreeQuotaType):
        self._FreeQuotaType = FreeQuotaType


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._FreeQuotaType = params.get("FreeQuotaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePostpayPackageFreeQuotasResponse(AbstractModel):
    """DescribePostpayPackageFreeQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageFreeQuotaInfos: 免费量资源信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageFreeQuotaInfos: list of PackageFreeQuotaInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PackageFreeQuotaInfos = None
        self._RequestId = None

    @property
    def PackageFreeQuotaInfos(self):
        return self._PackageFreeQuotaInfos

    @PackageFreeQuotaInfos.setter
    def PackageFreeQuotaInfos(self, PackageFreeQuotaInfos):
        self._PackageFreeQuotaInfos = PackageFreeQuotaInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PackageFreeQuotaInfos") is not None:
            self._PackageFreeQuotaInfos = []
            for item in params.get("PackageFreeQuotaInfos"):
                obj = PackageFreeQuotaInfo()
                obj._deserialize(item)
                self._PackageFreeQuotaInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeQuotaDataRequest(AbstractModel):
    """DescribeQuotaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _MetricName: <li> 指标名: </li>
<li> StorageSizepkg: 当月存储空间容量, 单位MB </li>
<li> StorageReadpkg: 当月存储读请求次数 </li>
<li> StorageWritepkg: 当月存储写请求次数 </li>
<li> StorageCdnOriginFluxpkg: 当月CDN回源流量, 单位字节 </li>
<li> StorageCdnOriginFluxpkgDay: 当日CDN回源流量, 单位字节 </li>
<li> StorageReadpkgDay: 当日存储读请求次数 </li>
<li> StorageWritepkgDay: 当日写请求次数 </li>
<li> CDNFluxpkg: 当月CDN流量, 单位为字节 </li>
<li> CDNFluxpkgDay: 当日CDN流量, 单位为字节 </li>
<li> FunctionInvocationpkg: 当月云函数调用次数 </li>
<li> FunctionGBspkg: 当月云函数资源使用量, 单位Mb*Ms </li>
<li> FunctionFluxpkg: 当月云函数流量, 单位千字节(KB) </li>
<li> FunctionInvocationpkgDay: 当日云函数调用次数 </li>
<li> FunctionGBspkgDay: 当日云函数资源使用量, 单位Mb*Ms </li>
<li> FunctionFluxpkgDay: 当日云函数流量, 单位千字节(KB) </li>
<li> DbSizepkg: 当月数据库容量大小, 单位MB </li>
<li> DbReadpkg: 当日数据库读请求数 </li>
<li> DbWritepkg: 当日数据库写请求数 </li>
<li> StaticFsFluxPkgDay: 当日静态托管流量 </li>
<li> StaticFsFluxPkg: 当月静态托管流量</li>
<li> StaticFsSizePkg: 当月静态托管容量 </li>
<li> TkeCpuUsedPkg: 当月容器托管CPU使用量，单位核*秒 </li>
<li> TkeCpuUsedPkgDay: 当天容器托管CPU使用量，单位核*秒 </li>
<li> TkeMemUsedPkg: 当月容器托管内存使用量，单位MB*秒 </li>
<li> TkeMemUsedPkgDay: 当天容器托管内存使用量，单位MB*秒 </li>
<li> CodingBuildTimePkgDay: 当天容器托管构建时间使用量，单位毫秒 </li>
<li> TkeHttpServiceNatPkgDay: 当天容器托管流量使用量，单位B </li>
        :type MetricName: str
        :param _ResourceID: 资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocationpkg, FunctionGBspkg, FunctionFluxpkg)、容器托管（服务名称）。如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传。
        :type ResourceID: str
        """
        self._EnvId = None
        self._MetricName = None
        self._ResourceID = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def ResourceID(self):
        return self._ResourceID

    @ResourceID.setter
    def ResourceID(self, ResourceID):
        self._ResourceID = ResourceID


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._MetricName = params.get("MetricName")
        self._ResourceID = params.get("ResourceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQuotaDataResponse(AbstractModel):
    """DescribeQuotaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Value: 指标的值
        :type Value: int
        :param _SubValue: 指标的附加值信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubValue: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricName = None
        self._Value = None
        self._SubValue = None
        self._RequestId = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def SubValue(self):
        return self._SubValue

    @SubValue.setter
    def SubValue(self, SubValue):
        self._SubValue = SubValue

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._Value = params.get("Value")
        self._SubValue = params.get("SubValue")
        self._RequestId = params.get("RequestId")


class DescribeSmsQuotasRequest(AbstractModel):
    """DescribeSmsQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsQuotasResponse(AbstractModel):
    """DescribeSmsQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SmsFreeQuotaList: 短信免费量信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsFreeQuotaList: list of SmsFreeQuota
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SmsFreeQuotaList = None
        self._RequestId = None

    @property
    def SmsFreeQuotaList(self):
        return self._SmsFreeQuotaList

    @SmsFreeQuotaList.setter
    def SmsFreeQuotaList(self, SmsFreeQuotaList):
        self._SmsFreeQuotaList = SmsFreeQuotaList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SmsFreeQuotaList") is not None:
            self._SmsFreeQuotaList = []
            for item in params.get("SmsFreeQuotaList"):
                obj = SmsFreeQuota()
                obj._deserialize(item)
                self._SmsFreeQuotaList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSpecialCostItemsRequest(AbstractModel):
    """DescribeSpecialCostItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _StartTime: 查询开始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        """
        self._EnvId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

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
        self._EnvId = params.get("EnvId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecialCostItemsResponse(AbstractModel):
    """DescribeSpecialCostItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpecialCostItems: 1分钱抵扣详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialCostItems: list of SpecialCostItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpecialCostItems = None
        self._RequestId = None

    @property
    def SpecialCostItems(self):
        return self._SpecialCostItems

    @SpecialCostItems.setter
    def SpecialCostItems(self, SpecialCostItems):
        self._SpecialCostItems = SpecialCostItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SpecialCostItems") is not None:
            self._SpecialCostItems = []
            for item in params.get("SpecialCostItems"):
                obj = SpecialCostItem()
                obj._deserialize(item)
                self._SpecialCostItems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStandaloneGatewayPackageRequest(AbstractModel):
    """DescribeStandaloneGatewayPackage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _PackageVersion: 套餐版本，包含starter、basic、advanced、enterprise
        :type PackageVersion: str
        """
        self._EnvId = None
        self._PackageVersion = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._PackageVersion = params.get("PackageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStandaloneGatewayPackageResponse(AbstractModel):
    """DescribeStandaloneGatewayPackage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _StandaloneGatewayPackageList: 套餐详情
        :type StandaloneGatewayPackageList: list of StandaloneGatewayPackageInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._StandaloneGatewayPackageList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def StandaloneGatewayPackageList(self):
        return self._StandaloneGatewayPackageList

    @StandaloneGatewayPackageList.setter
    def StandaloneGatewayPackageList(self, StandaloneGatewayPackageList):
        self._StandaloneGatewayPackageList = StandaloneGatewayPackageList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("StandaloneGatewayPackageList") is not None:
            self._StandaloneGatewayPackageList = []
            for item in params.get("StandaloneGatewayPackageList"):
                obj = StandaloneGatewayPackageInfo()
                obj._deserialize(item)
                self._StandaloneGatewayPackageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStandaloneGatewayRequest(AbstractModel):
    """DescribeStandaloneGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _GatewayName: 网关名称
        :type GatewayName: str
        :param _GatewayAlias: 网关别名
        :type GatewayAlias: str
        """
        self._EnvId = None
        self._GatewayName = None
        self._GatewayAlias = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def GatewayAlias(self):
        return self._GatewayAlias

    @GatewayAlias.setter
    def GatewayAlias(self, GatewayAlias):
        self._GatewayAlias = GatewayAlias


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayName = params.get("GatewayName")
        self._GatewayAlias = params.get("GatewayAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStandaloneGatewayResponse(AbstractModel):
    """DescribeStandaloneGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StandaloneGatewayList: 独立网关信息列表
        :type StandaloneGatewayList: list of StandaloneGatewayInfo
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StandaloneGatewayList = None
        self._Total = None
        self._RequestId = None

    @property
    def StandaloneGatewayList(self):
        return self._StandaloneGatewayList

    @StandaloneGatewayList.setter
    def StandaloneGatewayList(self, StandaloneGatewayList):
        self._StandaloneGatewayList = StandaloneGatewayList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StandaloneGatewayList") is not None:
            self._StandaloneGatewayList = []
            for item in params.get("StandaloneGatewayList"):
                obj = StandaloneGatewayInfo()
                obj._deserialize(item)
                self._StandaloneGatewayList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeUserActivityInfoRequest(AbstractModel):
    """DescribeUserActivityInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 活动id
        :type ActivityId: int
        :param _ChannelToken: 渠道加密token
        :type ChannelToken: str
        :param _Channel: 渠道来源，每个来源对应不同secretKey
        :type Channel: str
        :param _GroupId: 团id, 1元钱裂变中活动团id不为空时根据团id来查询记录，为空时查询uin最新记录
        :type GroupId: str
        """
        self._ActivityId = None
        self._ChannelToken = None
        self._Channel = None
        self._GroupId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ChannelToken(self):
        return self._ChannelToken

    @ChannelToken.setter
    def ChannelToken(self, ChannelToken):
        self._ChannelToken = ChannelToken

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._ChannelToken = params.get("ChannelToken")
        self._Channel = params.get("Channel")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserActivityInfoResponse(AbstractModel):
    """DescribeUserActivityInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tag: 自定义标记，1元钱裂变需求中即代指`团id`
        :type Tag: str
        :param _Notes: 自定义备注，1元钱裂变需求中返回`团列表`，uin列表通过","拼接
        :type Notes: str
        :param _ActivityTimeLeft: 活动剩余时间，单位为s.1元钱裂变需求中即为 time(活动过期时间)-Now()), 过期后为0，即返回必为自然数
        :type ActivityTimeLeft: int
        :param _GroupTimeLeft: 拼团剩余时间，单位为s.1元钱裂变需求中即为time(成团时间)+24H-Now()，过期后为0，即返回必为自然数
        :type GroupTimeLeft: int
        :param _NickNameList: 昵称列表,通过","拼接， 1元钱裂变活动中与Notes中uin一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type NickNameList: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tag = None
        self._Notes = None
        self._ActivityTimeLeft = None
        self._GroupTimeLeft = None
        self._NickNameList = None
        self._RequestId = None

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Notes(self):
        return self._Notes

    @Notes.setter
    def Notes(self, Notes):
        self._Notes = Notes

    @property
    def ActivityTimeLeft(self):
        return self._ActivityTimeLeft

    @ActivityTimeLeft.setter
    def ActivityTimeLeft(self, ActivityTimeLeft):
        self._ActivityTimeLeft = ActivityTimeLeft

    @property
    def GroupTimeLeft(self):
        return self._GroupTimeLeft

    @GroupTimeLeft.setter
    def GroupTimeLeft(self, GroupTimeLeft):
        self._GroupTimeLeft = GroupTimeLeft

    @property
    def NickNameList(self):
        return self._NickNameList

    @NickNameList.setter
    def NickNameList(self, NickNameList):
        self._NickNameList = NickNameList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Tag = params.get("Tag")
        self._Notes = params.get("Notes")
        self._ActivityTimeLeft = params.get("ActivityTimeLeft")
        self._GroupTimeLeft = params.get("GroupTimeLeft")
        self._NickNameList = params.get("NickNameList")
        self._RequestId = params.get("RequestId")


class DescribeWxCloudBaseRunEnvsRequest(AbstractModel):
    """DescribeWxCloudBaseRunEnvs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WxAppId: wx应用Id
        :type WxAppId: str
        :param _AllRegions: 是否查询全地域
        :type AllRegions: bool
        """
        self._WxAppId = None
        self._AllRegions = None

    @property
    def WxAppId(self):
        return self._WxAppId

    @WxAppId.setter
    def WxAppId(self, WxAppId):
        self._WxAppId = WxAppId

    @property
    def AllRegions(self):
        return self._AllRegions

    @AllRegions.setter
    def AllRegions(self, AllRegions):
        self._AllRegions = AllRegions


    def _deserialize(self, params):
        self._WxAppId = params.get("WxAppId")
        self._AllRegions = params.get("AllRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWxCloudBaseRunEnvsResponse(AbstractModel):
    """DescribeWxCloudBaseRunEnvs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvList: env列表
        :type EnvList: list of EnvInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvList = None
        self._RequestId = None

    @property
    def EnvList(self):
        return self._EnvList

    @EnvList.setter
    def EnvList(self, EnvList):
        self._EnvList = EnvList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnvList") is not None:
            self._EnvList = []
            for item in params.get("EnvList"):
                obj = EnvInfo()
                obj._deserialize(item)
                self._EnvList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWxCloudBaseRunSubNetsRequest(AbstractModel):
    """DescribeWxCloudBaseRunSubNets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC id
        :type VpcId: str
        :param _Limit: 查询个数限制，不填或小于等于0，等于不限制
        :type Limit: int
        """
        self._VpcId = None
        self._Limit = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWxCloudBaseRunSubNetsResponse(AbstractModel):
    """DescribeWxCloudBaseRunSubNets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubNetIds: 子网Id列表
        :type SubNetIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubNetIds = None
        self._RequestId = None

    @property
    def SubNetIds(self):
        return self._SubNetIds

    @SubNetIds.setter
    def SubNetIds(self, SubNetIds):
        self._SubNetIds = SubNetIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubNetIds = params.get("SubNetIds")
        self._RequestId = params.get("RequestId")


class DescribeWxGatewayRoutesRequest(AbstractModel):
    """DescribeWxGatewayRoutes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _GatewayId: 网关名称
        :type GatewayId: str
        :param _GatewayRouteName: 网关路由名称
        :type GatewayRouteName: str
        :param _GatewayVersion: 网关版本名
        :type GatewayVersion: str
        """
        self._EnvId = None
        self._GatewayId = None
        self._GatewayRouteName = None
        self._GatewayVersion = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GatewayRouteName(self):
        return self._GatewayRouteName

    @GatewayRouteName.setter
    def GatewayRouteName(self, GatewayRouteName):
        self._GatewayRouteName = GatewayRouteName

    @property
    def GatewayVersion(self):
        return self._GatewayVersion

    @GatewayVersion.setter
    def GatewayVersion(self, GatewayVersion):
        self._GatewayVersion = GatewayVersion


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayId = params.get("GatewayId")
        self._GatewayRouteName = params.get("GatewayRouteName")
        self._GatewayVersion = params.get("GatewayVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWxGatewayRoutesResponse(AbstractModel):
    """DescribeWxGatewayRoutes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的服务个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _WxGatewayRouteSet: 返回的服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type WxGatewayRouteSet: list of WxGatewayRountItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._WxGatewayRouteSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def WxGatewayRouteSet(self):
        return self._WxGatewayRouteSet

    @WxGatewayRouteSet.setter
    def WxGatewayRouteSet(self, WxGatewayRouteSet):
        self._WxGatewayRouteSet = WxGatewayRouteSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("WxGatewayRouteSet") is not None:
            self._WxGatewayRouteSet = []
            for item in params.get("WxGatewayRouteSet"):
                obj = WxGatewayRountItem()
                obj._deserialize(item)
                self._WxGatewayRouteSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWxGatewaysRequest(AbstractModel):
    """DescribeWxGateways请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _GatewayName: 服务名称，精确匹配
        :type GatewayName: str
        :param _Limit: 分页参数
        :type Limit: int
        :param _Offset: 分页参数
        :type Offset: int
        """
        self._EnvId = None
        self._GatewayName = None
        self._Limit = None
        self._Offset = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

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
        self._EnvId = params.get("EnvId")
        self._GatewayName = params.get("GatewayName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWxGatewaysResponse(AbstractModel):
    """DescribeWxGateways返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Gateways: 返回的服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Gateways: list of GatewayItem
        :param _TotalCount: 网关总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Gateways = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Gateways(self):
        return self._Gateways

    @Gateways.setter
    def Gateways(self, Gateways):
        self._Gateways = Gateways

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
        if params.get("Gateways") is not None:
            self._Gateways = []
            for item in params.get("Gateways"):
                obj = GatewayItem()
                obj._deserialize(item)
                self._Gateways.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DestroyEnvRequest(AbstractModel):
    """DestroyEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境Id
        :type EnvId: str
        :param _IsForce: 针对预付费 删除隔离中的环境时要传true 正常环境直接跳过隔离期删除
        :type IsForce: bool
        :param _BypassCheck: 是否绕过资源检查，资源包等额外资源，默认为false，如果为true，则不检查资源是否有数据，直接删除。
        :type BypassCheck: bool
        """
        self._EnvId = None
        self._IsForce = None
        self._BypassCheck = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def IsForce(self):
        return self._IsForce

    @IsForce.setter
    def IsForce(self, IsForce):
        self._IsForce = IsForce

    @property
    def BypassCheck(self):
        return self._BypassCheck

    @BypassCheck.setter
    def BypassCheck(self, BypassCheck):
        self._BypassCheck = BypassCheck


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._IsForce = params.get("IsForce")
        self._BypassCheck = params.get("BypassCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyEnvResponse(AbstractModel):
    """DestroyEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DestroyStandaloneGatewayRequest(AbstractModel):
    """DestroyStandaloneGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _GatewayName: 网名名称
        :type GatewayName: str
        :param _IsForce: 是否强制释放
        :type IsForce: bool
        """
        self._EnvId = None
        self._GatewayName = None
        self._IsForce = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def IsForce(self):
        return self._IsForce

    @IsForce.setter
    def IsForce(self, IsForce):
        self._IsForce = IsForce


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayName = params.get("GatewayName")
        self._IsForce = params.get("IsForce")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyStandaloneGatewayResponse(AbstractModel):
    """DestroyStandaloneGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 删除独立网关状态
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DestroyStaticStoreRequest(AbstractModel):
    """DestroyStaticStore请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _CdnDomain: cdn域名
        :type CdnDomain: str
        """
        self._EnvId = None
        self._CdnDomain = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CdnDomain(self):
        return self._CdnDomain

    @CdnDomain.setter
    def CdnDomain(self, CdnDomain):
        self._CdnDomain = CdnDomain


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CdnDomain = params.get("CdnDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyStaticStoreResponse(AbstractModel):
    """DestroyStaticStore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 条件任务结果(succ/fail)
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class EndUserInfo(AbstractModel):
    """终端用户信息

    """

    def __init__(self):
        r"""
        :param _UUId: 用户唯一ID
        :type UUId: str
        :param _WXOpenId: 微信ID
        :type WXOpenId: str
        :param _QQOpenId: qq ID
        :type QQOpenId: str
        :param _Phone: 手机号
        :type Phone: str
        :param _Email: 邮箱
        :type Email: str
        :param _NickName: 昵称
        :type NickName: str
        :param _Gender: 性别
        :type Gender: str
        :param _AvatarUrl: 头像地址
        :type AvatarUrl: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IsAnonymous: 是否为匿名用户
        :type IsAnonymous: bool
        :param _IsDisabled: 是否禁用账户
        :type IsDisabled: bool
        :param _HasPassword: 是否设置过密码
        :type HasPassword: bool
        :param _UserName: 用户名
        :type UserName: str
        """
        self._UUId = None
        self._WXOpenId = None
        self._QQOpenId = None
        self._Phone = None
        self._Email = None
        self._NickName = None
        self._Gender = None
        self._AvatarUrl = None
        self._UpdateTime = None
        self._CreateTime = None
        self._IsAnonymous = None
        self._IsDisabled = None
        self._HasPassword = None
        self._UserName = None

    @property
    def UUId(self):
        return self._UUId

    @UUId.setter
    def UUId(self, UUId):
        self._UUId = UUId

    @property
    def WXOpenId(self):
        return self._WXOpenId

    @WXOpenId.setter
    def WXOpenId(self, WXOpenId):
        self._WXOpenId = WXOpenId

    @property
    def QQOpenId(self):
        return self._QQOpenId

    @QQOpenId.setter
    def QQOpenId(self, QQOpenId):
        self._QQOpenId = QQOpenId

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def AvatarUrl(self):
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsAnonymous(self):
        return self._IsAnonymous

    @IsAnonymous.setter
    def IsAnonymous(self, IsAnonymous):
        self._IsAnonymous = IsAnonymous

    @property
    def IsDisabled(self):
        return self._IsDisabled

    @IsDisabled.setter
    def IsDisabled(self, IsDisabled):
        self._IsDisabled = IsDisabled

    @property
    def HasPassword(self):
        return self._HasPassword

    @HasPassword.setter
    def HasPassword(self, HasPassword):
        self._HasPassword = HasPassword

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._UUId = params.get("UUId")
        self._WXOpenId = params.get("WXOpenId")
        self._QQOpenId = params.get("QQOpenId")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._NickName = params.get("NickName")
        self._Gender = params.get("Gender")
        self._AvatarUrl = params.get("AvatarUrl")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._IsAnonymous = params.get("IsAnonymous")
        self._IsDisabled = params.get("IsDisabled")
        self._HasPassword = params.get("HasPassword")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvBillingInfoItem(AbstractModel):
    """环境计费信息

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。
        :type PackageId: str
        :param _IsAutoRenew: 自动续费标记
        :type IsAutoRenew: bool
        :param _Status: 状态。包含以下取值：
<li> 空字符串：初始化中</li>
<li> NORMAL：正常</li>
<li> ISOLATE：隔离</li>
        :type Status: str
        :param _PayMode: 支付方式。包含以下取值：
<li> PREPAYMENT：预付费</li>
<li> POSTPAID：后付费</li>
        :type PayMode: str
        :param _IsolatedTime: 隔离时间，最近一次隔离的时间
        :type IsolatedTime: str
        :param _ExpireTime: 过期时间，套餐即将到期的时间
        :type ExpireTime: str
        :param _CreateTime: 创建时间，第一次接入计费方案的时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间，计费信息最近一次更新的时间。
        :type UpdateTime: str
        :param _IsAlwaysFree: true表示从未升级过付费版。
        :type IsAlwaysFree: bool
        :param _PaymentChannel: 付费渠道。
<li> miniapp：小程序</li>
<li> qcloud：腾讯云</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentChannel: str
        :param _OrderInfo: 最新的订单信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderInfo: :class:`tencentcloud.tcb.v20180608.models.OrderInfo`
        :param _FreeQuota: 免费配额信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuota: str
        :param _EnableOverrun: 是否开启 `超过套餐额度部分转按量付费`
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableOverrun: bool
        :param _ExtPackageType: 环境套餐类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtPackageType: str
        """
        self._EnvId = None
        self._PackageId = None
        self._IsAutoRenew = None
        self._Status = None
        self._PayMode = None
        self._IsolatedTime = None
        self._ExpireTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._IsAlwaysFree = None
        self._PaymentChannel = None
        self._OrderInfo = None
        self._FreeQuota = None
        self._EnableOverrun = None
        self._ExtPackageType = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def IsAutoRenew(self):
        return self._IsAutoRenew

    @IsAutoRenew.setter
    def IsAutoRenew(self, IsAutoRenew):
        self._IsAutoRenew = IsAutoRenew

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def IsolatedTime(self):
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IsAlwaysFree(self):
        return self._IsAlwaysFree

    @IsAlwaysFree.setter
    def IsAlwaysFree(self, IsAlwaysFree):
        self._IsAlwaysFree = IsAlwaysFree

    @property
    def PaymentChannel(self):
        return self._PaymentChannel

    @PaymentChannel.setter
    def PaymentChannel(self, PaymentChannel):
        self._PaymentChannel = PaymentChannel

    @property
    def OrderInfo(self):
        return self._OrderInfo

    @OrderInfo.setter
    def OrderInfo(self, OrderInfo):
        self._OrderInfo = OrderInfo

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def EnableOverrun(self):
        return self._EnableOverrun

    @EnableOverrun.setter
    def EnableOverrun(self, EnableOverrun):
        self._EnableOverrun = EnableOverrun

    @property
    def ExtPackageType(self):
        return self._ExtPackageType

    @ExtPackageType.setter
    def ExtPackageType(self, ExtPackageType):
        self._ExtPackageType = ExtPackageType


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._PackageId = params.get("PackageId")
        self._IsAutoRenew = params.get("IsAutoRenew")
        self._Status = params.get("Status")
        self._PayMode = params.get("PayMode")
        self._IsolatedTime = params.get("IsolatedTime")
        self._ExpireTime = params.get("ExpireTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._IsAlwaysFree = params.get("IsAlwaysFree")
        self._PaymentChannel = params.get("PaymentChannel")
        if params.get("OrderInfo") is not None:
            self._OrderInfo = OrderInfo()
            self._OrderInfo._deserialize(params.get("OrderInfo"))
        self._FreeQuota = params.get("FreeQuota")
        self._EnableOverrun = params.get("EnableOverrun")
        self._ExtPackageType = params.get("ExtPackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvInfo(AbstractModel):
    """环境信息

    """

    def __init__(self):
        r"""
        :param _EnvId: 账户下该环境唯一标识
        :type EnvId: str
        :param _Source: 环境来源。包含以下取值：
<li>miniapp：微信小程序</li>
<li>qcloud ：腾讯云</li>
        :type Source: str
        :param _Alias: 环境别名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :type Alias: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 最后修改时间
        :type UpdateTime: str
        :param _Status: 环境状态。包含以下取值：
<li>NORMAL：正常可用</li>
<li>UNAVAILABLE：服务不可用，可能是尚未初始化或者初始化过程中</li>
        :type Status: str
        :param _Databases: 数据库列表
        :type Databases: list of DatabasesInfo
        :param _Storages: 存储列表
        :type Storages: list of StorageInfo
        :param _Functions: 函数列表
        :type Functions: list of FunctionInfo
        :param _PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param _PackageName: 套餐中文名称，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param _LogServices: 云日志服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogServices: list of LogServiceInfo
        :param _StaticStorages: 静态资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticStorages: list of StaticStorageInfo
        :param _IsAutoDegrade: 是否到期自动降为免费版
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoDegrade: bool
        :param _EnvChannel: 环境渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvChannel: str
        :param _PayMode: 支付方式。包含以下取值：
<li> prepayment：预付费</li>
<li> postpaid：后付费</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _IsDefault: 是否为默认环境
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: bool
        :param _Region: 环境所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Tags: 环境标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _CustomLogServices: 自定义日志服务
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogServices: list of ClsInfo
        :param _EnvType: 环境类型：baas, run, hoting, weda
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvType: str
        :param _IsDauPackage: 是否是dau新套餐
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDauPackage: bool
        :param _PackageType: 套餐类型:空\baas\tcbr
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _ArchitectureType: 架构类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ArchitectureType: str
        :param _Recycle: 回收标志，默认为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Recycle: str
        """
        self._EnvId = None
        self._Source = None
        self._Alias = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Status = None
        self._Databases = None
        self._Storages = None
        self._Functions = None
        self._PackageId = None
        self._PackageName = None
        self._LogServices = None
        self._StaticStorages = None
        self._IsAutoDegrade = None
        self._EnvChannel = None
        self._PayMode = None
        self._IsDefault = None
        self._Region = None
        self._Tags = None
        self._CustomLogServices = None
        self._EnvType = None
        self._IsDauPackage = None
        self._PackageType = None
        self._ArchitectureType = None
        self._Recycle = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Databases(self):
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def Storages(self):
        return self._Storages

    @Storages.setter
    def Storages(self, Storages):
        self._Storages = Storages

    @property
    def Functions(self):
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def LogServices(self):
        return self._LogServices

    @LogServices.setter
    def LogServices(self, LogServices):
        self._LogServices = LogServices

    @property
    def StaticStorages(self):
        return self._StaticStorages

    @StaticStorages.setter
    def StaticStorages(self, StaticStorages):
        self._StaticStorages = StaticStorages

    @property
    def IsAutoDegrade(self):
        return self._IsAutoDegrade

    @IsAutoDegrade.setter
    def IsAutoDegrade(self, IsAutoDegrade):
        self._IsAutoDegrade = IsAutoDegrade

    @property
    def EnvChannel(self):
        return self._EnvChannel

    @EnvChannel.setter
    def EnvChannel(self, EnvChannel):
        self._EnvChannel = EnvChannel

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CustomLogServices(self):
        return self._CustomLogServices

    @CustomLogServices.setter
    def CustomLogServices(self, CustomLogServices):
        self._CustomLogServices = CustomLogServices

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def IsDauPackage(self):
        return self._IsDauPackage

    @IsDauPackage.setter
    def IsDauPackage(self, IsDauPackage):
        self._IsDauPackage = IsDauPackage

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ArchitectureType(self):
        return self._ArchitectureType

    @ArchitectureType.setter
    def ArchitectureType(self, ArchitectureType):
        self._ArchitectureType = ArchitectureType

    @property
    def Recycle(self):
        return self._Recycle

    @Recycle.setter
    def Recycle(self, Recycle):
        self._Recycle = Recycle


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Source = params.get("Source")
        self._Alias = params.get("Alias")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = DatabasesInfo()
                obj._deserialize(item)
                self._Databases.append(obj)
        if params.get("Storages") is not None:
            self._Storages = []
            for item in params.get("Storages"):
                obj = StorageInfo()
                obj._deserialize(item)
                self._Storages.append(obj)
        if params.get("Functions") is not None:
            self._Functions = []
            for item in params.get("Functions"):
                obj = FunctionInfo()
                obj._deserialize(item)
                self._Functions.append(obj)
        self._PackageId = params.get("PackageId")
        self._PackageName = params.get("PackageName")
        if params.get("LogServices") is not None:
            self._LogServices = []
            for item in params.get("LogServices"):
                obj = LogServiceInfo()
                obj._deserialize(item)
                self._LogServices.append(obj)
        if params.get("StaticStorages") is not None:
            self._StaticStorages = []
            for item in params.get("StaticStorages"):
                obj = StaticStorageInfo()
                obj._deserialize(item)
                self._StaticStorages.append(obj)
        self._IsAutoDegrade = params.get("IsAutoDegrade")
        self._EnvChannel = params.get("EnvChannel")
        self._PayMode = params.get("PayMode")
        self._IsDefault = params.get("IsDefault")
        self._Region = params.get("Region")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("CustomLogServices") is not None:
            self._CustomLogServices = []
            for item in params.get("CustomLogServices"):
                obj = ClsInfo()
                obj._deserialize(item)
                self._CustomLogServices.append(obj)
        self._EnvType = params.get("EnvType")
        self._IsDauPackage = params.get("IsDauPackage")
        self._PackageType = params.get("PackageType")
        self._ArchitectureType = params.get("ArchitectureType")
        self._Recycle = params.get("Recycle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EstablishCloudBaseRunServerRequest(AbstractModel):
    """EstablishCloudBaseRunServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _ServiceName: 服务名称
        :type ServiceName: str
        :param _IsPublic: 是否开通外网访问
        :type IsPublic: bool
        :param _ImageRepo: 镜像仓库
        :type ImageRepo: str
        :param _Remark: 服务描述
        :type Remark: str
        :param _EsInfo: es信息
        :type EsInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseEsInfo`
        :param _LogType: 日志类型; es/cls
        :type LogType: str
        :param _OperatorRemark: 操作备注
        :type OperatorRemark: str
        :param _Source: 来源方（默认值：qcloud，微信侧来源miniapp)
        :type Source: str
        :param _VpcInfo: vpc信息
        :type VpcInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunVpcInfo`
        :param _PublicAccess: 0/1=允许公网访问;2=关闭公网访问
        :type PublicAccess: int
        :param _OpenAccessTypes: OA PUBLIC MINIAPP VPC
        :type OpenAccessTypes: list of str
        :param _IsCreatePath: 是否创建Path 0未传默认创建 1创建 2不创建
        :type IsCreatePath: int
        :param _ServerPath: 指定创建路径（如不存在，则创建。存在，则忽略）
        :type ServerPath: str
        """
        self._EnvId = None
        self._ServiceName = None
        self._IsPublic = None
        self._ImageRepo = None
        self._Remark = None
        self._EsInfo = None
        self._LogType = None
        self._OperatorRemark = None
        self._Source = None
        self._VpcInfo = None
        self._PublicAccess = None
        self._OpenAccessTypes = None
        self._IsCreatePath = None
        self._ServerPath = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def ImageRepo(self):
        return self._ImageRepo

    @ImageRepo.setter
    def ImageRepo(self, ImageRepo):
        self._ImageRepo = ImageRepo

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def EsInfo(self):
        return self._EsInfo

    @EsInfo.setter
    def EsInfo(self, EsInfo):
        self._EsInfo = EsInfo

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def VpcInfo(self):
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo

    @property
    def PublicAccess(self):
        return self._PublicAccess

    @PublicAccess.setter
    def PublicAccess(self, PublicAccess):
        self._PublicAccess = PublicAccess

    @property
    def OpenAccessTypes(self):
        return self._OpenAccessTypes

    @OpenAccessTypes.setter
    def OpenAccessTypes(self, OpenAccessTypes):
        self._OpenAccessTypes = OpenAccessTypes

    @property
    def IsCreatePath(self):
        return self._IsCreatePath

    @IsCreatePath.setter
    def IsCreatePath(self, IsCreatePath):
        self._IsCreatePath = IsCreatePath

    @property
    def ServerPath(self):
        return self._ServerPath

    @ServerPath.setter
    def ServerPath(self, ServerPath):
        self._ServerPath = ServerPath


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServiceName = params.get("ServiceName")
        self._IsPublic = params.get("IsPublic")
        self._ImageRepo = params.get("ImageRepo")
        self._Remark = params.get("Remark")
        if params.get("EsInfo") is not None:
            self._EsInfo = CloudBaseEsInfo()
            self._EsInfo._deserialize(params.get("EsInfo"))
        self._LogType = params.get("LogType")
        self._OperatorRemark = params.get("OperatorRemark")
        self._Source = params.get("Source")
        if params.get("VpcInfo") is not None:
            self._VpcInfo = CloudBaseRunVpcInfo()
            self._VpcInfo._deserialize(params.get("VpcInfo"))
        self._PublicAccess = params.get("PublicAccess")
        self._OpenAccessTypes = params.get("OpenAccessTypes")
        self._IsCreatePath = params.get("IsCreatePath")
        self._ServerPath = params.get("ServerPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EstablishCloudBaseRunServerResponse(AbstractModel):
    """EstablishCloudBaseRunServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建服务是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class EstablishWxGatewayRouteRequest(AbstractModel):
    """EstablishWxGatewayRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关id
        :type GatewayId: str
        :param _GatewayRouteName: 服务名称
        :type GatewayRouteName: str
        :param _GatewayRouteAddr: 服务地址
        :type GatewayRouteAddr: str
        :param _GatewayRouteProtocol: 协议类型 http/https
        :type GatewayRouteProtocol: str
        :param _GatewayRouteDesc: 服务描述
        :type GatewayRouteDesc: str
        """
        self._GatewayId = None
        self._GatewayRouteName = None
        self._GatewayRouteAddr = None
        self._GatewayRouteProtocol = None
        self._GatewayRouteDesc = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GatewayRouteName(self):
        return self._GatewayRouteName

    @GatewayRouteName.setter
    def GatewayRouteName(self, GatewayRouteName):
        self._GatewayRouteName = GatewayRouteName

    @property
    def GatewayRouteAddr(self):
        return self._GatewayRouteAddr

    @GatewayRouteAddr.setter
    def GatewayRouteAddr(self, GatewayRouteAddr):
        self._GatewayRouteAddr = GatewayRouteAddr

    @property
    def GatewayRouteProtocol(self):
        return self._GatewayRouteProtocol

    @GatewayRouteProtocol.setter
    def GatewayRouteProtocol(self, GatewayRouteProtocol):
        self._GatewayRouteProtocol = GatewayRouteProtocol

    @property
    def GatewayRouteDesc(self):
        return self._GatewayRouteDesc

    @GatewayRouteDesc.setter
    def GatewayRouteDesc(self, GatewayRouteDesc):
        self._GatewayRouteDesc = GatewayRouteDesc


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GatewayRouteName = params.get("GatewayRouteName")
        self._GatewayRouteAddr = params.get("GatewayRouteAddr")
        self._GatewayRouteProtocol = params.get("GatewayRouteProtocol")
        self._GatewayRouteDesc = params.get("GatewayRouteDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EstablishWxGatewayRouteResponse(AbstractModel):
    """EstablishWxGatewayRoute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ExtensionFile(AbstractModel):
    """扩展文件

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型。枚举值
<li>FUNCTION：函数代码</li>
<li>STATIC：静态托管代码</li>
<li>SMS：短信文件</li>
        :type FileType: str
        :param _FileName: 文件名，长度不超过24
        :type FileName: str
        """
        self._FileType = None
        self._FileName = None

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensionFileInfo(AbstractModel):
    """扩展文件信息

    """

    def __init__(self):
        r"""
        :param _CodeUri: 模板里使用的地址
        :type CodeUri: str
        :param _UploadUrl: 上传文件的临时地址，含签名
        :type UploadUrl: str
        :param _CustomKey: 自定义密钥。如果为空，则表示不需要加密
        :type CustomKey: str
        :param _MaxSize: 文件大小限制，单位M，客户端上传前需要主动检查文件大小，超过限制的文件会被删除。
        :type MaxSize: int
        """
        self._CodeUri = None
        self._UploadUrl = None
        self._CustomKey = None
        self._MaxSize = None

    @property
    def CodeUri(self):
        return self._CodeUri

    @CodeUri.setter
    def CodeUri(self, CodeUri):
        self._CodeUri = CodeUri

    @property
    def UploadUrl(self):
        return self._UploadUrl

    @UploadUrl.setter
    def UploadUrl(self, UploadUrl):
        self._UploadUrl = UploadUrl

    @property
    def CustomKey(self):
        return self._CustomKey

    @CustomKey.setter
    def CustomKey(self, CustomKey):
        self._CustomKey = CustomKey

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._CodeUri = params.get("CodeUri")
        self._UploadUrl = params.get("UploadUrl")
        self._CustomKey = params.get("CustomKey")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreequotaInfo(AbstractModel):
    """后付费资源免费量信息

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型
<li>COS</li>
<li>CDN</li>
<li>FLEXDB</li>
<li>SCF</li>
        :type ResourceType: str
        :param _ResourceMetric: 资源指标名称
        :type ResourceMetric: str
        :param _FreeQuota: 资源指标免费量
        :type FreeQuota: int
        :param _MetricUnit: 指标单位
        :type MetricUnit: str
        :param _DeductType: 免费量抵扣周期
<li>sum-month:以月为单位抵扣</li>
<li>sum-day:以天为单位抵扣</li>
<li>totalize:总容量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductType: str
        :param _FreeQuotaType: 免费量类型
<li>basic:通用量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuotaType: str
        """
        self._ResourceType = None
        self._ResourceMetric = None
        self._FreeQuota = None
        self._MetricUnit = None
        self._DeductType = None
        self._FreeQuotaType = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceMetric(self):
        return self._ResourceMetric

    @ResourceMetric.setter
    def ResourceMetric(self, ResourceMetric):
        self._ResourceMetric = ResourceMetric

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def MetricUnit(self):
        return self._MetricUnit

    @MetricUnit.setter
    def MetricUnit(self, MetricUnit):
        self._MetricUnit = MetricUnit

    @property
    def DeductType(self):
        return self._DeductType

    @DeductType.setter
    def DeductType(self, DeductType):
        self._DeductType = DeductType

    @property
    def FreeQuotaType(self):
        return self._FreeQuotaType

    @FreeQuotaType.setter
    def FreeQuotaType(self, FreeQuotaType):
        self._FreeQuotaType = FreeQuotaType


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceMetric = params.get("ResourceMetric")
        self._FreeQuota = params.get("FreeQuota")
        self._MetricUnit = params.get("MetricUnit")
        self._DeductType = params.get("DeductType")
        self._FreeQuotaType = params.get("FreeQuotaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreezeCloudBaseRunServersRequest(AbstractModel):
    """FreezeCloudBaseRunServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerNameList: 服务名列表
        :type ServerNameList: list of str
        """
        self._EnvId = None
        self._ServerNameList = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerNameList(self):
        return self._ServerNameList

    @ServerNameList.setter
    def ServerNameList(self, ServerNameList):
        self._ServerNameList = ServerNameList


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerNameList = params.get("ServerNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreezeCloudBaseRunServersResponse(AbstractModel):
    """FreezeCloudBaseRunServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 批量状态
成功：succ
失败：fail
部分：partial（部分成功、部分失败）
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _FailServerList: 冻结失败服务列表
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailServerList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._FailServerList = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def FailServerList(self):
        return self._FailServerList

    @FailServerList.setter
    def FailServerList(self, FailServerList):
        self._FailServerList = FailServerList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._FailServerList = params.get("FailServerList")
        self._RequestId = params.get("RequestId")


class FrequencyLimitConfig(AbstractModel):
    """安全网关版本路由信息限额配置

    """

    def __init__(self):
        r"""
        :param _LimitObject: 限额对象 "ConnectionsLimit" 或 "QPSLimit"
注意：此字段可能返回 null，表示取不到有效值。
        :type LimitObject: str
        :param _LimitConfig: 限额配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LimitConfig: str
        """
        self._LimitObject = None
        self._LimitConfig = None

    @property
    def LimitObject(self):
        return self._LimitObject

    @LimitObject.setter
    def LimitObject(self, LimitObject):
        self._LimitObject = LimitObject

    @property
    def LimitConfig(self):
        return self._LimitConfig

    @LimitConfig.setter
    def LimitConfig(self, LimitConfig):
        self._LimitConfig = LimitConfig


    def _deserialize(self, params):
        self._LimitObject = params.get("LimitObject")
        self._LimitConfig = params.get("LimitConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionInfo(AbstractModel):
    """函数的信息

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Region: 所属地域。
当前支持ap-shanghai
        :type Region: str
        """
        self._Namespace = None
        self._Region = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayItem(AbstractModel):
    """网关信息

    """

    def __init__(self):
        r"""
        :param _Uin: 用户uin
        :type Uin: str
        :param _AppId: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _EnvId: 环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param _GatewayId: Gateway唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _GatewayName: Gateway名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayName: str
        :param _GatewayType: Gateway类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayType: str
        :param _GatewayDesc: Gateway描述
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayDesc: str
        :param _PackageVersion: 套餐版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param _PackageId: 套餐唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: int
        :param _VpcId: vpc唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetIds: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param _Status: 网关状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _L5Addr: l5地址
注意：此字段可能返回 null，表示取不到有效值。
        :type L5Addr: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _IsolateTime: 隔离时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
        :param _ExpireTime: 到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 变更时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _AllowUncertified: 允许未登录访问
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowUncertified: int
        :param _VersionNumLimit: 网关版本限额
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionNumLimit: int
        """
        self._Uin = None
        self._AppId = None
        self._EnvId = None
        self._GatewayId = None
        self._GatewayName = None
        self._GatewayType = None
        self._GatewayDesc = None
        self._PackageVersion = None
        self._PackageId = None
        self._VpcId = None
        self._SubnetIds = None
        self._Status = None
        self._L5Addr = None
        self._Region = None
        self._IsolateTime = None
        self._ExpireTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AllowUncertified = None
        self._VersionNumLimit = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def GatewayType(self):
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType

    @property
    def GatewayDesc(self):
        return self._GatewayDesc

    @GatewayDesc.setter
    def GatewayDesc(self, GatewayDesc):
        self._GatewayDesc = GatewayDesc

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def L5Addr(self):
        return self._L5Addr

    @L5Addr.setter
    def L5Addr(self, L5Addr):
        self._L5Addr = L5Addr

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AllowUncertified(self):
        return self._AllowUncertified

    @AllowUncertified.setter
    def AllowUncertified(self, AllowUncertified):
        self._AllowUncertified = AllowUncertified

    @property
    def VersionNumLimit(self):
        return self._VersionNumLimit

    @VersionNumLimit.setter
    def VersionNumLimit(self, VersionNumLimit):
        self._VersionNumLimit = VersionNumLimit


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._AppId = params.get("AppId")
        self._EnvId = params.get("EnvId")
        self._GatewayId = params.get("GatewayId")
        self._GatewayName = params.get("GatewayName")
        self._GatewayType = params.get("GatewayType")
        self._GatewayDesc = params.get("GatewayDesc")
        self._PackageVersion = params.get("PackageVersion")
        self._PackageId = params.get("PackageId")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._Status = params.get("Status")
        self._L5Addr = params.get("L5Addr")
        self._Region = params.get("Region")
        self._IsolateTime = params.get("IsolateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AllowUncertified = params.get("AllowUncertified")
        self._VersionNumLimit = params.get("VersionNumLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayVersionItem(AbstractModel):
    """网关版本详情

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本名
        :type VersionName: str
        :param _Weight: 版本流量权重
        :type Weight: int
        :param _Status: 创建状态
        :type Status: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param _BuildId: 构建ID
        :type BuildId: int
        :param _Remark: 备注
        :type Remark: str
        :param _Priority: 优先级
        :type Priority: int
        :param _IsDefault: 是否默认版本
        :type IsDefault: bool
        :param _CustomConfig: 网关版本自定义配置
        :type CustomConfig: :class:`tencentcloud.tcb.v20180608.models.WxGatewayCustomConfig`
        """
        self._VersionName = None
        self._Weight = None
        self._Status = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._BuildId = None
        self._Remark = None
        self._Priority = None
        self._IsDefault = None
        self._CustomConfig = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def BuildId(self):
        return self._BuildId

    @BuildId.setter
    def BuildId(self, BuildId):
        self._BuildId = BuildId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def CustomConfig(self):
        return self._CustomConfig

    @CustomConfig.setter
    def CustomConfig(self, CustomConfig):
        self._CustomConfig = CustomConfig


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._Weight = params.get("Weight")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._BuildId = params.get("BuildId")
        self._Remark = params.get("Remark")
        self._Priority = params.get("Priority")
        self._IsDefault = params.get("IsDefault")
        if params.get("CustomConfig") is not None:
            self._CustomConfig = WxGatewayCustomConfig()
            self._CustomConfig._deserialize(params.get("CustomConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HpaPolicy(AbstractModel):
    """扩缩容策略

    """

    def __init__(self):
        r"""
        :param _PolicyType: 策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param _PolicyThreshold: 策略阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyThreshold: int
        """
        self._PolicyType = None
        self._PolicyThreshold = None

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyThreshold(self):
        return self._PolicyThreshold

    @PolicyThreshold.setter
    def PolicyThreshold(self, PolicyThreshold):
        self._PolicyThreshold = PolicyThreshold


    def _deserialize(self, params):
        self._PolicyType = params.get("PolicyType")
        self._PolicyThreshold = params.get("PolicyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVPair(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param _Key: 键
        :type Key: str
        :param _Value: 值
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
        


class LogObject(AbstractModel):
    """CLS日志单条信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志属于的 topic ID
        :type TopicId: str
        :param _TopicName: 日志主题的名字
        :type TopicName: str
        :param _Timestamp: 日志时间
        :type Timestamp: str
        :param _Content: 日志内容
        :type Content: str
        :param _FileName: 采集路径
        :type FileName: str
        :param _Source: 日志来源设备
        :type Source: str
        """
        self._TopicId = None
        self._TopicName = None
        self._Timestamp = None
        self._Content = None
        self._FileName = None
        self._Source = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Timestamp = params.get("Timestamp")
        self._Content = params.get("Content")
        self._FileName = params.get("FileName")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogResObject(AbstractModel):
    """CLS日志结果

    """

    def __init__(self):
        r"""
        :param _Context: 获取更多检索结果的游标
        :type Context: str
        :param _ListOver: 搜索结果是否已经全部返回
        :type ListOver: bool
        :param _Results: 日志内容信息
        :type Results: list of LogObject
        """
        self._Context = None
        self._ListOver = None
        self._Results = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = LogObject()
                obj._deserialize(item)
                self._Results.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogServiceInfo(AbstractModel):
    """云日志服务相关信息

    """

    def __init__(self):
        r"""
        :param _LogsetName: log名
        :type LogsetName: str
        :param _LogsetId: log-id
        :type LogsetId: str
        :param _TopicName: topic名
        :type TopicName: str
        :param _TopicId: topic-id
        :type TopicId: str
        :param _Region: cls日志所属地域
        :type Region: str
        :param _Period: topic保存时长 默认7天
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        """
        self._LogsetName = None
        self._LogsetId = None
        self._TopicName = None
        self._TopicId = None
        self._Region = None
        self._Period = None

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._LogsetName = params.get("LogsetName")
        self._LogsetId = params.get("LogsetId")
        self._TopicName = params.get("TopicName")
        self._TopicId = params.get("TopicId")
        self._Region = params.get("Region")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginStatistic(AbstractModel):
    """终端用户登录新增统计

    """

    def __init__(self):
        r"""
        :param _StatisticalType: 统计类型 新增NEWUSER 和登录 LOGIN
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticalType: str
        :param _StatisticalCycle: 统计周期：日DAY，周WEEK，月MONTH
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticalCycle: str
        :param _Count: 统计总量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._StatisticalType = None
        self._StatisticalCycle = None
        self._Count = None
        self._UpdateTime = None

    @property
    def StatisticalType(self):
        return self._StatisticalType

    @StatisticalType.setter
    def StatisticalType(self, StatisticalType):
        self._StatisticalType = StatisticalType

    @property
    def StatisticalCycle(self):
        return self._StatisticalCycle

    @StatisticalCycle.setter
    def StatisticalCycle(self, StatisticalCycle):
        self._StatisticalCycle = StatisticalCycle

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._StatisticalType = params.get("StatisticalType")
        self._StatisticalCycle = params.get("StatisticalCycle")
        self._Count = params.get("Count")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudBaseRunServerFlowConfRequest(AbstractModel):
    """ModifyCloudBaseRunServerFlowConf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerName: 服务名称
        :type ServerName: str
        :param _VersionFlowItems: 流量占比
        :type VersionFlowItems: list of CloudBaseRunVersionFlowItem
        :param _TrafficType: 流量类型（URL_PARAMS / FLOW / HEADERS)
        :type TrafficType: str
        :param _OperatorRemark: 操作备注
        :type OperatorRemark: str
        """
        self._EnvId = None
        self._ServerName = None
        self._VersionFlowItems = None
        self._TrafficType = None
        self._OperatorRemark = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionFlowItems(self):
        return self._VersionFlowItems

    @VersionFlowItems.setter
    def VersionFlowItems(self, VersionFlowItems):
        self._VersionFlowItems = VersionFlowItems

    @property
    def TrafficType(self):
        return self._TrafficType

    @TrafficType.setter
    def TrafficType(self, TrafficType):
        self._TrafficType = TrafficType

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        if params.get("VersionFlowItems") is not None:
            self._VersionFlowItems = []
            for item in params.get("VersionFlowItems"):
                obj = CloudBaseRunVersionFlowItem()
                obj._deserialize(item)
                self._VersionFlowItems.append(obj)
        self._TrafficType = params.get("TrafficType")
        self._OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudBaseRunServerFlowConfResponse(AbstractModel):
    """ModifyCloudBaseRunServerFlowConf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果，succ代表成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyCloudBaseRunServerVersionRequest(AbstractModel):
    """ModifyCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerName: 服务名称
        :type ServerName: str
        :param _VersionName: 版本名称
        :type VersionName: str
        :param _EnvParams: 环境变量
        :type EnvParams: str
        :param _MinNum: 最小副本数
        :type MinNum: str
        :param _MaxNum: 最大副本数
        :type MaxNum: str
        :param _ContainerPort: 端口
        :type ContainerPort: str
        :param _Remark: 备注
        :type Remark: str
        :param _CustomLogs: 日志采集路径
        :type CustomLogs: str
        :param _IsResetRemark: 是否重设备注
        :type IsResetRemark: bool
        :param _BasicModify: 修改基础信息
        :type BasicModify: bool
        :param _OperatorRemark: 操作备注
        :type OperatorRemark: str
        """
        self._EnvId = None
        self._ServerName = None
        self._VersionName = None
        self._EnvParams = None
        self._MinNum = None
        self._MaxNum = None
        self._ContainerPort = None
        self._Remark = None
        self._CustomLogs = None
        self._IsResetRemark = None
        self._BasicModify = None
        self._OperatorRemark = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def EnvParams(self):
        return self._EnvParams

    @EnvParams.setter
    def EnvParams(self, EnvParams):
        self._EnvParams = EnvParams

    @property
    def MinNum(self):
        return self._MinNum

    @MinNum.setter
    def MinNum(self, MinNum):
        self._MinNum = MinNum

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum

    @property
    def ContainerPort(self):
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CustomLogs(self):
        return self._CustomLogs

    @CustomLogs.setter
    def CustomLogs(self, CustomLogs):
        self._CustomLogs = CustomLogs

    @property
    def IsResetRemark(self):
        return self._IsResetRemark

    @IsResetRemark.setter
    def IsResetRemark(self, IsResetRemark):
        self._IsResetRemark = IsResetRemark

    @property
    def BasicModify(self):
        return self._BasicModify

    @BasicModify.setter
    def BasicModify(self, BasicModify):
        self._BasicModify = BasicModify

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerName = params.get("ServerName")
        self._VersionName = params.get("VersionName")
        self._EnvParams = params.get("EnvParams")
        self._MinNum = params.get("MinNum")
        self._MaxNum = params.get("MaxNum")
        self._ContainerPort = params.get("ContainerPort")
        self._Remark = params.get("Remark")
        self._CustomLogs = params.get("CustomLogs")
        self._IsResetRemark = params.get("IsResetRemark")
        self._BasicModify = params.get("BasicModify")
        self._OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudBaseRunServerVersionResponse(AbstractModel):
    """ModifyCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果（succ为成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyClsTopicRequest(AbstractModel):
    """ModifyClsTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Period: 日志生命周期，单位天，可取值范围1~3600，取值为3640时代表永久保存
        :type Period: int
        """
        self._EnvId = None
        self._Period = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClsTopicResponse(AbstractModel):
    """ModifyClsTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyDatabaseACLRequest(AbstractModel):
    """ModifyDatabaseACL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _CollectionName: 集合名称
        :type CollectionName: str
        :param _AclTag: 权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
        :type AclTag: str
        """
        self._EnvId = None
        self._CollectionName = None
        self._AclTag = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionName(self):
        return self._CollectionName

    @CollectionName.setter
    def CollectionName(self, CollectionName):
        self._CollectionName = CollectionName

    @property
    def AclTag(self):
        return self._AclTag

    @AclTag.setter
    def AclTag(self, AclTag):
        self._AclTag = AclTag


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CollectionName = params.get("CollectionName")
        self._AclTag = params.get("AclTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatabaseACLResponse(AbstractModel):
    """ModifyDatabaseACL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyEndUserRequest(AbstractModel):
    """ModifyEndUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _UUId: C端用户端的唯一ID
        :type UUId: str
        :param _Status: 账号的状态
<li>ENABLE</li>
<li>DISABLE</li>
        :type Status: str
        """
        self._EnvId = None
        self._UUId = None
        self._Status = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def UUId(self):
        return self._UUId

    @UUId.setter
    def UUId(self, UUId):
        self._UUId = UUId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._UUId = params.get("UUId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEndUserResponse(AbstractModel):
    """ModifyEndUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyEnvRequest(AbstractModel):
    """ModifyEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Alias: 环境备注名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :type Alias: str
        """
        self._EnvId = None
        self._Alias = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvResponse(AbstractModel):
    """ModifyEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyGatewayVersionTrafficRequest(AbstractModel):
    """ModifyGatewayVersionTraffic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _GatewayId: 网关id
        :type GatewayId: str
        :param _VersionsWeight: 网关版本流量比例信息
        :type VersionsWeight: list of GatewayVersionItem
        """
        self._EnvId = None
        self._GatewayId = None
        self._VersionsWeight = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def VersionsWeight(self):
        return self._VersionsWeight

    @VersionsWeight.setter
    def VersionsWeight(self, VersionsWeight):
        self._VersionsWeight = VersionsWeight


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayId = params.get("GatewayId")
        if params.get("VersionsWeight") is not None:
            self._VersionsWeight = []
            for item in params.get("VersionsWeight"):
                obj = GatewayVersionItem()
                obj._deserialize(item)
                self._VersionsWeight.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGatewayVersionTrafficResponse(AbstractModel):
    """ModifyGatewayVersionTraffic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ObjectKV(AbstractModel):
    """Key-Value类型，模拟的 object 类型

    """

    def __init__(self):
        r"""
        :param _Key: object 的 key
        :type Key: str
        :param _Value: object key 对应的 value
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
        


class OneClickTaskStepInfo(AbstractModel):
    """一键部署步骤信息

    """

    def __init__(self):
        r"""
        :param _Status: 未启动："todo"
运行中："running"
失败："failed"
成功结束："finished"
        :type Status: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _CostTime: 耗时：秒
        :type CostTime: int
        :param _FailReason: 失败原因
        :type FailReason: str
        :param _Name: 步骤名
        :type Name: str
        """
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._CostTime = None
        self._FailReason = None
        self._Name = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CostTime = params.get("CostTime")
        self._FailReason = params.get("FailReason")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderInfo(AbstractModel):
    """订单信息

    """

    def __init__(self):
        r"""
        :param _TranId: 订单号
        :type TranId: str
        :param _PackageId: 订单要切换的套餐ID
        :type PackageId: str
        :param _TranType: 订单类型
<li>1 购买</li>
<li>2 续费</li>
<li>3 变配</li>
        :type TranType: str
        :param _TranStatus: 订单状态。
<li>1未支付</li>
<li>2 支付中</li>
<li>3 发货中</li>
<li>4 发货成功</li>
<li>5 发货失败</li>
<li>6 已退款</li>
<li>7 已取消</li>
<li>100 已删除</li>
        :type TranStatus: str
        :param _UpdateTime: 订单更新时间
        :type UpdateTime: str
        :param _CreateTime: 订单创建时间
        :type CreateTime: str
        :param _PayMode: 付费模式.
<li>prepayment 预付费</li>
<li>postpaid 后付费</li>
        :type PayMode: str
        :param _ExtensionId: 订单绑定的扩展ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtensionId: str
        :param _ResourceReady: 资源初始化结果(仅当ExtensionId不为空时有效): successful(初始化成功), failed(初始化失败), doing(初始化进行中), init(准备初始化)
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceReady: str
        :param _Flag: 安装标记。建议使用方统一转大小写之后再判断。
<li>QuickStart：快速启动来源</li>
<li>Activity：活动来源</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Flag: str
        :param _ReqBody: 下单时的参数
        :type ReqBody: str
        """
        self._TranId = None
        self._PackageId = None
        self._TranType = None
        self._TranStatus = None
        self._UpdateTime = None
        self._CreateTime = None
        self._PayMode = None
        self._ExtensionId = None
        self._ResourceReady = None
        self._Flag = None
        self._ReqBody = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def TranType(self):
        return self._TranType

    @TranType.setter
    def TranType(self, TranType):
        self._TranType = TranType

    @property
    def TranStatus(self):
        return self._TranStatus

    @TranStatus.setter
    def TranStatus(self, TranStatus):
        self._TranStatus = TranStatus

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ResourceReady(self):
        return self._ResourceReady

    @ResourceReady.setter
    def ResourceReady(self, ResourceReady):
        self._ResourceReady = ResourceReady

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def ReqBody(self):
        return self._ReqBody

    @ReqBody.setter
    def ReqBody(self, ReqBody):
        self._ReqBody = ReqBody


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._PackageId = params.get("PackageId")
        self._TranType = params.get("TranType")
        self._TranStatus = params.get("TranStatus")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._PayMode = params.get("PayMode")
        self._ExtensionId = params.get("ExtensionId")
        self._ResourceReady = params.get("ResourceReady")
        self._Flag = params.get("Flag")
        self._ReqBody = params.get("ReqBody")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageFreeQuotaInfo(AbstractModel):
    """后付费免费额度

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型
<li>COS</li>
<li>CDN</li>
<li>FLEXDB</li>
<li>SCF</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _ResourceMetric: 资源指标名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceMetric: str
        :param _FreeQuota: 资源指标免费量
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuota: int
        :param _MetricUnit: 指标单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricUnit: str
        :param _DeductType: 免费量抵扣周期
<li>sum-month:以月为单位抵扣</li>
<li>sum-day:以天为单位抵扣</li>
<li>totalize:总容量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductType: str
        :param _FreeQuotaType: 免费量类型
<li>basic:通用量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuotaType: str
        """
        self._ResourceType = None
        self._ResourceMetric = None
        self._FreeQuota = None
        self._MetricUnit = None
        self._DeductType = None
        self._FreeQuotaType = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceMetric(self):
        return self._ResourceMetric

    @ResourceMetric.setter
    def ResourceMetric(self, ResourceMetric):
        self._ResourceMetric = ResourceMetric

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def MetricUnit(self):
        return self._MetricUnit

    @MetricUnit.setter
    def MetricUnit(self, MetricUnit):
        self._MetricUnit = MetricUnit

    @property
    def DeductType(self):
        return self._DeductType

    @DeductType.setter
    def DeductType(self, DeductType):
        self._DeductType = DeductType

    @property
    def FreeQuotaType(self):
        return self._FreeQuotaType

    @FreeQuotaType.setter
    def FreeQuotaType(self, FreeQuotaType):
        self._FreeQuotaType = FreeQuotaType


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceMetric = params.get("ResourceMetric")
        self._FreeQuota = params.get("FreeQuota")
        self._MetricUnit = params.get("MetricUnit")
        self._DeductType = params.get("DeductType")
        self._FreeQuotaType = params.get("FreeQuotaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlatformStatistic(AbstractModel):
    """终端用户平台统计信息

    """

    def __init__(self):
        r"""
        :param _Platform: 终端用户从属平台
注意：此字段可能返回 null，表示取不到有效值。
        :type Platform: str
        :param _Count: 平台终端用户数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._Platform = None
        self._Count = None
        self._UpdateTime = None

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Count = params.get("Count")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostPaidEnvDeductInfo(AbstractModel):
    """后付费计费详情

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源方
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _MetricName: 指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param _ResQuota: 按量计费详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ResQuota: float
        :param _PkgQuota: 资源包抵扣详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgQuota: float
        :param _FreeQuota: 免费额度抵扣详情
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuota: float
        :param _EnvId: 环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        """
        self._ResourceType = None
        self._MetricName = None
        self._ResQuota = None
        self._PkgQuota = None
        self._FreeQuota = None
        self._EnvId = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def ResQuota(self):
        return self._ResQuota

    @ResQuota.setter
    def ResQuota(self, ResQuota):
        self._ResQuota = ResQuota

    @property
    def PkgQuota(self):
        return self._PkgQuota

    @PkgQuota.setter
    def PkgQuota(self, PkgQuota):
        self._PkgQuota = PkgQuota

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._MetricName = params.get("MetricName")
        self._ResQuota = params.get("ResQuota")
        self._PkgQuota = params.get("PkgQuota")
        self._FreeQuota = params.get("FreeQuota")
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostpayEnvQuota(AbstractModel):
    """按量付费免费配额信息

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Value: 配额值
        :type Value: int
        :param _StartTime: 配额生效时间
为空表示没有时间限制
        :type StartTime: str
        :param _EndTime: 配额失效时间
为空表示没有时间限制
        :type EndTime: str
        """
        self._ResourceType = None
        self._MetricName = None
        self._Value = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

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
        self._ResourceType = params.get("ResourceType")
        self._MetricName = params.get("MetricName")
        self._Value = params.get("Value")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReinstateEnvRequest(AbstractModel):
    """ReinstateEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReinstateEnvResponse(AbstractModel):
    """ReinstateEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ReplaceActivityRecordRequest(AbstractModel):
    """ReplaceActivityRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 活动id
        :type ActivityId: int
        :param _Status: 状态码
        :type Status: int
        :param _SubStatus: 自定义子状态
        :type SubStatus: str
        :param _ChannelToken: 鉴权token
        :type ChannelToken: str
        :param _Channel: 渠道名，不同渠道对应不同secretKey
        :type Channel: str
        """
        self._ActivityId = None
        self._Status = None
        self._SubStatus = None
        self._ChannelToken = None
        self._Channel = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubStatus(self):
        return self._SubStatus

    @SubStatus.setter
    def SubStatus(self, SubStatus):
        self._SubStatus = SubStatus

    @property
    def ChannelToken(self):
        return self._ChannelToken

    @ChannelToken.setter
    def ChannelToken(self, ChannelToken):
        self._ChannelToken = ChannelToken

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._Status = params.get("Status")
        self._SubStatus = params.get("SubStatus")
        self._ChannelToken = params.get("ChannelToken")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceActivityRecordResponse(AbstractModel):
    """ReplaceActivityRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class RollUpdateCloudBaseRunServerVersionRequest(AbstractModel):
    """RollUpdateCloudBaseRunServerVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _VersionName: 要替换的版本名称，可以为latest
        :type VersionName: str
        :param _UploadType: 枚举（package/repository/image)
        :type UploadType: str
        :param _RepositoryType: repository的类型(coding/gitlab/github)
        :type RepositoryType: str
        :param _FlowRatio: 流量占比
        :type FlowRatio: int
        :param _DockerfilePath: dockerfile地址
        :type DockerfilePath: str
        :param _BuildDir: 构建目录
        :type BuildDir: str
        :param _Cpu: Cpu的大小，单位：核
        :type Cpu: str
        :param _Mem: Mem的大小，单位：G
        :type Mem: str
        :param _MinNum: 最小副本数，最小值：0
        :type MinNum: str
        :param _MaxNum: 最大副本数
        :type MaxNum: str
        :param _PolicyType: 策略类型
        :type PolicyType: str
        :param _PolicyThreshold: 策略阈值
        :type PolicyThreshold: str
        :param _EnvParams: 环境变量
        :type EnvParams: str
        :param _ContainerPort: 容器端口
        :type ContainerPort: int
        :param _ServerName: 服务名称
        :type ServerName: str
        :param _Repository: repository地址
        :type Repository: str
        :param _Branch: 分支
        :type Branch: str
        :param _VersionRemark: 版本备注
        :type VersionRemark: str
        :param _PackageName: 代码包名字
        :type PackageName: str
        :param _PackageVersion: 代码包版本
        :type PackageVersion: str
        :param _ImageInfo: Image的详情
        :type ImageInfo: :class:`tencentcloud.tcb.v20180608.models.CloudBaseRunImageInfo`
        :param _CodeDetail: Github等拉取代码的详情
        :type CodeDetail: :class:`tencentcloud.tcb.v20180608.models.CloudBaseCodeRepoDetail`
        :param _IsRebuild: 是否回放流量
        :type IsRebuild: bool
        :param _InitialDelaySeconds: 延迟多长时间开始健康检查（单位s）
        :type InitialDelaySeconds: int
        :param _MountVolumeInfo: cfs挂载信息
        :type MountVolumeInfo: list of CloudBaseRunVolumeMount
        :param _Rollback: 是否回滚
        :type Rollback: bool
        :param _SnapshotName: 版本历史名
        :type SnapshotName: str
        :param _CustomLogs: 自定义采集路径
        :type CustomLogs: str
        :param _EnableUnion: 是否启用统一域名
        :type EnableUnion: bool
        :param _OperatorRemark: 操作备注
        :type OperatorRemark: str
        :param _ServerPath: 服务路径（只会第一次生效）
        :type ServerPath: str
        :param _IsUpdateCls: 是否更新Cls
        :type IsUpdateCls: bool
        :param _PolicyDetail: 自动扩缩容策略组
        :type PolicyDetail: list of HpaPolicy
        """
        self._EnvId = None
        self._VersionName = None
        self._UploadType = None
        self._RepositoryType = None
        self._FlowRatio = None
        self._DockerfilePath = None
        self._BuildDir = None
        self._Cpu = None
        self._Mem = None
        self._MinNum = None
        self._MaxNum = None
        self._PolicyType = None
        self._PolicyThreshold = None
        self._EnvParams = None
        self._ContainerPort = None
        self._ServerName = None
        self._Repository = None
        self._Branch = None
        self._VersionRemark = None
        self._PackageName = None
        self._PackageVersion = None
        self._ImageInfo = None
        self._CodeDetail = None
        self._IsRebuild = None
        self._InitialDelaySeconds = None
        self._MountVolumeInfo = None
        self._Rollback = None
        self._SnapshotName = None
        self._CustomLogs = None
        self._EnableUnion = None
        self._OperatorRemark = None
        self._ServerPath = None
        self._IsUpdateCls = None
        self._PolicyDetail = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def UploadType(self):
        return self._UploadType

    @UploadType.setter
    def UploadType(self, UploadType):
        self._UploadType = UploadType

    @property
    def RepositoryType(self):
        return self._RepositoryType

    @RepositoryType.setter
    def RepositoryType(self, RepositoryType):
        self._RepositoryType = RepositoryType

    @property
    def FlowRatio(self):
        return self._FlowRatio

    @FlowRatio.setter
    def FlowRatio(self, FlowRatio):
        self._FlowRatio = FlowRatio

    @property
    def DockerfilePath(self):
        return self._DockerfilePath

    @DockerfilePath.setter
    def DockerfilePath(self, DockerfilePath):
        self._DockerfilePath = DockerfilePath

    @property
    def BuildDir(self):
        return self._BuildDir

    @BuildDir.setter
    def BuildDir(self, BuildDir):
        self._BuildDir = BuildDir

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def MinNum(self):
        return self._MinNum

    @MinNum.setter
    def MinNum(self, MinNum):
        self._MinNum = MinNum

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyThreshold(self):
        return self._PolicyThreshold

    @PolicyThreshold.setter
    def PolicyThreshold(self, PolicyThreshold):
        self._PolicyThreshold = PolicyThreshold

    @property
    def EnvParams(self):
        return self._EnvParams

    @EnvParams.setter
    def EnvParams(self, EnvParams):
        self._EnvParams = EnvParams

    @property
    def ContainerPort(self):
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def Repository(self):
        return self._Repository

    @Repository.setter
    def Repository(self, Repository):
        self._Repository = Repository

    @property
    def Branch(self):
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def VersionRemark(self):
        return self._VersionRemark

    @VersionRemark.setter
    def VersionRemark(self, VersionRemark):
        self._VersionRemark = VersionRemark

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def CodeDetail(self):
        return self._CodeDetail

    @CodeDetail.setter
    def CodeDetail(self, CodeDetail):
        self._CodeDetail = CodeDetail

    @property
    def IsRebuild(self):
        return self._IsRebuild

    @IsRebuild.setter
    def IsRebuild(self, IsRebuild):
        self._IsRebuild = IsRebuild

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def MountVolumeInfo(self):
        return self._MountVolumeInfo

    @MountVolumeInfo.setter
    def MountVolumeInfo(self, MountVolumeInfo):
        self._MountVolumeInfo = MountVolumeInfo

    @property
    def Rollback(self):
        return self._Rollback

    @Rollback.setter
    def Rollback(self, Rollback):
        self._Rollback = Rollback

    @property
    def SnapshotName(self):
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def CustomLogs(self):
        return self._CustomLogs

    @CustomLogs.setter
    def CustomLogs(self, CustomLogs):
        self._CustomLogs = CustomLogs

    @property
    def EnableUnion(self):
        return self._EnableUnion

    @EnableUnion.setter
    def EnableUnion(self, EnableUnion):
        self._EnableUnion = EnableUnion

    @property
    def OperatorRemark(self):
        return self._OperatorRemark

    @OperatorRemark.setter
    def OperatorRemark(self, OperatorRemark):
        self._OperatorRemark = OperatorRemark

    @property
    def ServerPath(self):
        return self._ServerPath

    @ServerPath.setter
    def ServerPath(self, ServerPath):
        self._ServerPath = ServerPath

    @property
    def IsUpdateCls(self):
        return self._IsUpdateCls

    @IsUpdateCls.setter
    def IsUpdateCls(self, IsUpdateCls):
        self._IsUpdateCls = IsUpdateCls

    @property
    def PolicyDetail(self):
        return self._PolicyDetail

    @PolicyDetail.setter
    def PolicyDetail(self, PolicyDetail):
        self._PolicyDetail = PolicyDetail


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._VersionName = params.get("VersionName")
        self._UploadType = params.get("UploadType")
        self._RepositoryType = params.get("RepositoryType")
        self._FlowRatio = params.get("FlowRatio")
        self._DockerfilePath = params.get("DockerfilePath")
        self._BuildDir = params.get("BuildDir")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._MinNum = params.get("MinNum")
        self._MaxNum = params.get("MaxNum")
        self._PolicyType = params.get("PolicyType")
        self._PolicyThreshold = params.get("PolicyThreshold")
        self._EnvParams = params.get("EnvParams")
        self._ContainerPort = params.get("ContainerPort")
        self._ServerName = params.get("ServerName")
        self._Repository = params.get("Repository")
        self._Branch = params.get("Branch")
        self._VersionRemark = params.get("VersionRemark")
        self._PackageName = params.get("PackageName")
        self._PackageVersion = params.get("PackageVersion")
        if params.get("ImageInfo") is not None:
            self._ImageInfo = CloudBaseRunImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodeDetail") is not None:
            self._CodeDetail = CloudBaseCodeRepoDetail()
            self._CodeDetail._deserialize(params.get("CodeDetail"))
        self._IsRebuild = params.get("IsRebuild")
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        if params.get("MountVolumeInfo") is not None:
            self._MountVolumeInfo = []
            for item in params.get("MountVolumeInfo"):
                obj = CloudBaseRunVolumeMount()
                obj._deserialize(item)
                self._MountVolumeInfo.append(obj)
        self._Rollback = params.get("Rollback")
        self._SnapshotName = params.get("SnapshotName")
        self._CustomLogs = params.get("CustomLogs")
        self._EnableUnion = params.get("EnableUnion")
        self._OperatorRemark = params.get("OperatorRemark")
        self._ServerPath = params.get("ServerPath")
        self._IsUpdateCls = params.get("IsUpdateCls")
        if params.get("PolicyDetail") is not None:
            self._PolicyDetail = []
            for item in params.get("PolicyDetail"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self._PolicyDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollUpdateCloudBaseRunServerVersionResponse(AbstractModel):
    """RollUpdateCloudBaseRunServerVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: succ为成功
        :type Result: str
        :param _VersionName: 滚动更新的VersionName
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _RunId: 操作记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type RunId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._VersionName = None
        self._RunId = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def RunId(self):
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._VersionName = params.get("VersionName")
        self._RunId = params.get("RunId")
        self._RequestId = params.get("RequestId")


class SearchClsLogRequest(AbstractModel):
    """SearchClsLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境唯一ID
        :type EnvId: str
        :param _StartTime: 查询起始时间条件
        :type StartTime: str
        :param _EndTime: 查询结束时间条件
        :type EndTime: str
        :param _QueryString: 查询语句，详情参考 https://cloud.tencent.com/document/product/614/47044
        :type QueryString: str
        :param _Limit: 单次要返回的日志条数，单次返回的最大条数为100
        :type Limit: int
        :param _Context: 加载更多使用，透传上次返回的 context 值，获取后续的日志内容，通过游标最多可获取10000条，请尽可能缩小时间范围
        :type Context: str
        :param _Sort: 按时间排序 asc（升序）或者 desc（降序），默认为 desc
        :type Sort: str
        :param _UseLucene: 是否使用Lucene语法，默认为false
        :type UseLucene: bool
        """
        self._EnvId = None
        self._StartTime = None
        self._EndTime = None
        self._QueryString = None
        self._Limit = None
        self._Context = None
        self._Sort = None
        self._UseLucene = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

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
    def QueryString(self):
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def UseLucene(self):
        return self._UseLucene

    @UseLucene.setter
    def UseLucene(self, UseLucene):
        self._UseLucene = UseLucene


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._QueryString = params.get("QueryString")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Sort = params.get("Sort")
        self._UseLucene = params.get("UseLucene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogResponse(AbstractModel):
    """SearchClsLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogResults: 日志内容结果
        :type LogResults: :class:`tencentcloud.tcb.v20180608.models.LogResObject`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogResults = None
        self._RequestId = None

    @property
    def LogResults(self):
        return self._LogResults

    @LogResults.setter
    def LogResults(self, LogResults):
        self._LogResults = LogResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LogResults") is not None:
            self._LogResults = LogResObject()
            self._LogResults._deserialize(params.get("LogResults"))
        self._RequestId = params.get("RequestId")


class SmsFreeQuota(AbstractModel):
    """短信免费量

    """

    def __init__(self):
        r"""
        :param _FreeQuota: 免费量总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuota: int
        :param _TotalUsedQuota: 共计已使用总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUsedQuota: int
        :param _CycleStart: 免费周期起点，0000-00-00 00:00:00 形式
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleStart: str
        :param _CycleEnd: 免费周期终点，0000-00-00 00:00:00 形式
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleEnd: str
        :param _TodayUsedQuota: 今天已使用总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TodayUsedQuota: int
        """
        self._FreeQuota = None
        self._TotalUsedQuota = None
        self._CycleStart = None
        self._CycleEnd = None
        self._TodayUsedQuota = None

    @property
    def FreeQuota(self):
        return self._FreeQuota

    @FreeQuota.setter
    def FreeQuota(self, FreeQuota):
        self._FreeQuota = FreeQuota

    @property
    def TotalUsedQuota(self):
        return self._TotalUsedQuota

    @TotalUsedQuota.setter
    def TotalUsedQuota(self, TotalUsedQuota):
        self._TotalUsedQuota = TotalUsedQuota

    @property
    def CycleStart(self):
        return self._CycleStart

    @CycleStart.setter
    def CycleStart(self, CycleStart):
        self._CycleStart = CycleStart

    @property
    def CycleEnd(self):
        return self._CycleEnd

    @CycleEnd.setter
    def CycleEnd(self, CycleEnd):
        self._CycleEnd = CycleEnd

    @property
    def TodayUsedQuota(self):
        return self._TodayUsedQuota

    @TodayUsedQuota.setter
    def TodayUsedQuota(self, TodayUsedQuota):
        self._TodayUsedQuota = TodayUsedQuota


    def _deserialize(self, params):
        self._FreeQuota = params.get("FreeQuota")
        self._TotalUsedQuota = params.get("TotalUsedQuota")
        self._CycleStart = params.get("CycleStart")
        self._CycleEnd = params.get("CycleEnd")
        self._TodayUsedQuota = params.get("TodayUsedQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecialCostItem(AbstractModel):
    """1分钱计费详情

    """

    def __init__(self):
        r"""
        :param _ReportDate: 上报日期
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportDate: str
        :param _Uin: 腾讯云uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _EnvId: 资源id:环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param _Status: 上报任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._ReportDate = None
        self._Uin = None
        self._EnvId = None
        self._Status = None

    @property
    def ReportDate(self):
        return self._ReportDate

    @ReportDate.setter
    def ReportDate(self, ReportDate):
        self._ReportDate = ReportDate

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ReportDate = params.get("ReportDate")
        self._Uin = params.get("Uin")
        self._EnvId = params.get("EnvId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandaloneGatewayInfo(AbstractModel):
    """独立网关信息

    """

    def __init__(self):
        r"""
        :param _GatewayName: 独立网关名称
        :type GatewayName: str
        :param _CPU: CPU核心数
        :type CPU: float
        :param _Mem: 内存大小，单位MB
        :type Mem: int
        :param _PackageVersion: 套餐包版本名称
        :type PackageVersion: str
        :param _GatewayAlias: 网关别名
        :type GatewayAlias: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetIds: 子网ID列表
        :type SubnetIds: list of str
        :param _GatewayDesc: 网关描述
        :type GatewayDesc: str
        :param _GateWayStatus: 网关状态
        :type GateWayStatus: str
        :param _ServiceInfo: 服务信息
        :type ServiceInfo: :class:`tencentcloud.tcb.v20180608.models.BackendServiceInfo`
        :param _PublicClbIp: 公网CLBIP
        :type PublicClbIp: str
        :param _InternalClbIp: 内网CLBIP
        :type InternalClbIp: str
        """
        self._GatewayName = None
        self._CPU = None
        self._Mem = None
        self._PackageVersion = None
        self._GatewayAlias = None
        self._VpcId = None
        self._SubnetIds = None
        self._GatewayDesc = None
        self._GateWayStatus = None
        self._ServiceInfo = None
        self._PublicClbIp = None
        self._InternalClbIp = None

    @property
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def GatewayAlias(self):
        return self._GatewayAlias

    @GatewayAlias.setter
    def GatewayAlias(self, GatewayAlias):
        self._GatewayAlias = GatewayAlias

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def GatewayDesc(self):
        return self._GatewayDesc

    @GatewayDesc.setter
    def GatewayDesc(self, GatewayDesc):
        self._GatewayDesc = GatewayDesc

    @property
    def GateWayStatus(self):
        return self._GateWayStatus

    @GateWayStatus.setter
    def GateWayStatus(self, GateWayStatus):
        self._GateWayStatus = GateWayStatus

    @property
    def ServiceInfo(self):
        return self._ServiceInfo

    @ServiceInfo.setter
    def ServiceInfo(self, ServiceInfo):
        self._ServiceInfo = ServiceInfo

    @property
    def PublicClbIp(self):
        return self._PublicClbIp

    @PublicClbIp.setter
    def PublicClbIp(self, PublicClbIp):
        self._PublicClbIp = PublicClbIp

    @property
    def InternalClbIp(self):
        return self._InternalClbIp

    @InternalClbIp.setter
    def InternalClbIp(self, InternalClbIp):
        self._InternalClbIp = InternalClbIp


    def _deserialize(self, params):
        self._GatewayName = params.get("GatewayName")
        self._CPU = params.get("CPU")
        self._Mem = params.get("Mem")
        self._PackageVersion = params.get("PackageVersion")
        self._GatewayAlias = params.get("GatewayAlias")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._GatewayDesc = params.get("GatewayDesc")
        self._GateWayStatus = params.get("GateWayStatus")
        if params.get("ServiceInfo") is not None:
            self._ServiceInfo = BackendServiceInfo()
            self._ServiceInfo._deserialize(params.get("ServiceInfo"))
        self._PublicClbIp = params.get("PublicClbIp")
        self._InternalClbIp = params.get("InternalClbIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandaloneGatewayPackageInfo(AbstractModel):
    """小租户网关套餐配置

    """

    def __init__(self):
        r"""
        :param _CPU: CPU核心数
        :type CPU: float
        :param _Mem: 内存大小，单位MB
        :type Mem: int
        :param _PackageVersion: 套餐包版本名称
        :type PackageVersion: str
        """
        self._CPU = None
        self._Mem = None
        self._PackageVersion = None

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def PackageVersion(self):
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion


    def _deserialize(self, params):
        self._CPU = params.get("CPU")
        self._Mem = params.get("Mem")
        self._PackageVersion = params.get("PackageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaticStorageInfo(AbstractModel):
    """静态CDN资源信息

    """

    def __init__(self):
        r"""
        :param _StaticDomain: 静态CDN域名
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticDomain: str
        :param _DefaultDirName: 静态CDN默认文件夹，当前为根目录
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultDirName: str
        :param _Status: 资源状态(process/online/offline/init)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Region: cos所属区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Bucket: bucket信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        """
        self._StaticDomain = None
        self._DefaultDirName = None
        self._Status = None
        self._Region = None
        self._Bucket = None

    @property
    def StaticDomain(self):
        return self._StaticDomain

    @StaticDomain.setter
    def StaticDomain(self, StaticDomain):
        self._StaticDomain = StaticDomain

    @property
    def DefaultDirName(self):
        return self._DefaultDirName

    @DefaultDirName.setter
    def DefaultDirName(self, DefaultDirName):
        self._DefaultDirName = DefaultDirName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._StaticDomain = params.get("StaticDomain")
        self._DefaultDirName = params.get("DefaultDirName")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    """StorageInfo 资源信息

    """

    def __init__(self):
        r"""
        :param _Region: 资源所属地域。
当前支持ap-shanghai
        :type Region: str
        :param _Bucket: 桶名，存储资源的唯一标识
        :type Bucket: str
        :param _CdnDomain: cdn 域名
        :type CdnDomain: str
        :param _AppId: 资源所属用户的腾讯云appId
        :type AppId: str
        """
        self._Region = None
        self._Bucket = None
        self._CdnDomain = None
        self._AppId = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def CdnDomain(self):
        return self._CdnDomain

    @CdnDomain.setter
    def CdnDomain(self, CdnDomain):
        self._CdnDomain = CdnDomain

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._CdnDomain = params.get("CdnDomain")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
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
        


class TkeClusterInfo(AbstractModel):
    """tke集群信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _VpcId: 集群的vpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VersionClbSubnetId: 版本内网CLB所在子网Id
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionClbSubnetId: str
        """
        self._ClusterId = None
        self._VpcId = None
        self._VersionClbSubnetId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VersionClbSubnetId(self):
        return self._VersionClbSubnetId

    @VersionClbSubnetId.setter
    def VersionClbSubnetId(self, VersionClbSubnetId):
        self._VersionClbSubnetId = VersionClbSubnetId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._VpcId = params.get("VpcId")
        self._VersionClbSubnetId = params.get("VersionClbSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TurnOffStandaloneGatewayRequest(AbstractModel):
    """TurnOffStandaloneGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _GatewayName: 网关名称
        :type GatewayName: str
        :param _ServiceNameList: 服务名称列表
        :type ServiceNameList: list of str
        """
        self._EnvId = None
        self._GatewayName = None
        self._ServiceNameList = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def ServiceNameList(self):
        return self._ServiceNameList

    @ServiceNameList.setter
    def ServiceNameList(self, ServiceNameList):
        self._ServiceNameList = ServiceNameList


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayName = params.get("GatewayName")
        self._ServiceNameList = params.get("ServiceNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TurnOffStandaloneGatewayResponse(AbstractModel):
    """TurnOffStandaloneGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 关闭独立网关状态
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class TurnOnStandaloneGatewayRequest(AbstractModel):
    """TurnOnStandaloneGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _GatewayName: 网关名称
        :type GatewayName: str
        :param _ServiceNameList: 服务名称列表
        :type ServiceNameList: list of str
        """
        self._EnvId = None
        self._GatewayName = None
        self._ServiceNameList = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def ServiceNameList(self):
        return self._ServiceNameList

    @ServiceNameList.setter
    def ServiceNameList(self, ServiceNameList):
        self._ServiceNameList = ServiceNameList


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._GatewayName = params.get("GatewayName")
        self._ServiceNameList = params.get("ServiceNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TurnOnStandaloneGatewayResponse(AbstractModel):
    """TurnOnStandaloneGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 小租户网关开启状态
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class UnfreezeCloudBaseRunServersRequest(AbstractModel):
    """UnfreezeCloudBaseRunServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _ServerNameList: 服务名称列表
        :type ServerNameList: list of str
        """
        self._EnvId = None
        self._ServerNameList = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServerNameList(self):
        return self._ServerNameList

    @ServerNameList.setter
    def ServerNameList(self, ServerNameList):
        self._ServerNameList = ServerNameList


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ServerNameList = params.get("ServerNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnfreezeCloudBaseRunServersResponse(AbstractModel):
    """UnfreezeCloudBaseRunServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 批量执行结果
成功：succ
失败：fail
部分：partial（部分成功、部分失败）
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _FailServerList: 解冻失败列表
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailServerList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._FailServerList = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def FailServerList(self):
        return self._FailServerList

    @FailServerList.setter
    def FailServerList(self, FailServerList):
        self._FailServerList = FailServerList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._FailServerList = params.get("FailServerList")
        self._RequestId = params.get("RequestId")


class WxGatewayCustomConfig(AbstractModel):
    """安全网关自定义配置

    """

    def __init__(self):
        r"""
        :param _IsOpenXRealIp: 是否开启x-real-ip
        :type IsOpenXRealIp: bool
        :param _BanConfig: 封禁配置
        :type BanConfig: :class:`tencentcloud.tcb.v20180608.models.BanConfig`
        :param _SourceIpType: 获取源ip方式，PPV1(Proxy Protocol V1)、PPV2(Proxy Protocol V2)、TOA(tcp option address)
        :type SourceIpType: str
        :param _LogConfig: 日志信息
        :type LogConfig: :class:`tencentcloud.tcb.v20180608.models.CustomLogConfig`
        :param _IsAcceptHttpOne: 是否开启http1.0
        :type IsAcceptHttpOne: bool
        """
        self._IsOpenXRealIp = None
        self._BanConfig = None
        self._SourceIpType = None
        self._LogConfig = None
        self._IsAcceptHttpOne = None

    @property
    def IsOpenXRealIp(self):
        return self._IsOpenXRealIp

    @IsOpenXRealIp.setter
    def IsOpenXRealIp(self, IsOpenXRealIp):
        self._IsOpenXRealIp = IsOpenXRealIp

    @property
    def BanConfig(self):
        return self._BanConfig

    @BanConfig.setter
    def BanConfig(self, BanConfig):
        self._BanConfig = BanConfig

    @property
    def SourceIpType(self):
        return self._SourceIpType

    @SourceIpType.setter
    def SourceIpType(self, SourceIpType):
        self._SourceIpType = SourceIpType

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def IsAcceptHttpOne(self):
        return self._IsAcceptHttpOne

    @IsAcceptHttpOne.setter
    def IsAcceptHttpOne(self, IsAcceptHttpOne):
        self._IsAcceptHttpOne = IsAcceptHttpOne


    def _deserialize(self, params):
        self._IsOpenXRealIp = params.get("IsOpenXRealIp")
        if params.get("BanConfig") is not None:
            self._BanConfig = BanConfig()
            self._BanConfig._deserialize(params.get("BanConfig"))
        self._SourceIpType = params.get("SourceIpType")
        if params.get("LogConfig") is not None:
            self._LogConfig = CustomLogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._IsAcceptHttpOne = params.get("IsAcceptHttpOne")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WxGatewayRountItem(AbstractModel):
    """安全网关路由

    """

    def __init__(self):
        r"""
        :param _GatewayRouteName: 安全网关路由名称
        :type GatewayRouteName: str
        :param _GatewayRouteProtocol: 安全网关路由协议
        :type GatewayRouteProtocol: str
        :param _GatewayRouteAddr: 安全网关路由地址
        :type GatewayRouteAddr: str
        :param _GatewayRouteDesc: 安全网关路由描述
        :type GatewayRouteDesc: str
        :param _GatewayRouteClusterId: 安全网关后端集群id，如果是外网服务，该id与GatewayRountName相同
        :type GatewayRouteClusterId: str
        :param _GatewayRouteCreateTime: 安全网关创建时间
        :type GatewayRouteCreateTime: str
        :param _FrequencyLimitConfig: 安全网关路由限制
注意：此字段可能返回 null，表示取不到有效值。
        :type FrequencyLimitConfig: list of FrequencyLimitConfig
        :param _GatewayRouteServerType: ip代表绑定后端ip。cbr代表云托管服务
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayRouteServerType: str
        :param _GatewayRouteServerName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayRouteServerName: str
        :param _GatewayRewriteHost: ip
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayRewriteHost: str
        :param _GatewayVersion: 网关版本
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayVersion: str
        :param _GatewayRoutePath: 请求路径
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayRoutePath: str
        :param _GatewayRouteMethod: 请求模式
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayRouteMethod: str
        :param _GatewayRoutePort: 4层端口
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayRoutePort: int
        :param _GatewayRouteEnvId: 路由环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayRouteEnvId: str
        :param _GatewayRoutePathMatchType: 路径匹配类型，支持prefix(前缀匹配)，regex(正则匹配)， 默认prefix
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayRoutePathMatchType: str
        :param _CustomHeader: 安全网关自定义头部
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomHeader: :class:`tencentcloud.tcb.v20180608.models.CustomHeader`
        """
        self._GatewayRouteName = None
        self._GatewayRouteProtocol = None
        self._GatewayRouteAddr = None
        self._GatewayRouteDesc = None
        self._GatewayRouteClusterId = None
        self._GatewayRouteCreateTime = None
        self._FrequencyLimitConfig = None
        self._GatewayRouteServerType = None
        self._GatewayRouteServerName = None
        self._GatewayRewriteHost = None
        self._GatewayVersion = None
        self._GatewayRoutePath = None
        self._GatewayRouteMethod = None
        self._GatewayRoutePort = None
        self._GatewayRouteEnvId = None
        self._GatewayRoutePathMatchType = None
        self._CustomHeader = None

    @property
    def GatewayRouteName(self):
        return self._GatewayRouteName

    @GatewayRouteName.setter
    def GatewayRouteName(self, GatewayRouteName):
        self._GatewayRouteName = GatewayRouteName

    @property
    def GatewayRouteProtocol(self):
        return self._GatewayRouteProtocol

    @GatewayRouteProtocol.setter
    def GatewayRouteProtocol(self, GatewayRouteProtocol):
        self._GatewayRouteProtocol = GatewayRouteProtocol

    @property
    def GatewayRouteAddr(self):
        return self._GatewayRouteAddr

    @GatewayRouteAddr.setter
    def GatewayRouteAddr(self, GatewayRouteAddr):
        self._GatewayRouteAddr = GatewayRouteAddr

    @property
    def GatewayRouteDesc(self):
        return self._GatewayRouteDesc

    @GatewayRouteDesc.setter
    def GatewayRouteDesc(self, GatewayRouteDesc):
        self._GatewayRouteDesc = GatewayRouteDesc

    @property
    def GatewayRouteClusterId(self):
        return self._GatewayRouteClusterId

    @GatewayRouteClusterId.setter
    def GatewayRouteClusterId(self, GatewayRouteClusterId):
        self._GatewayRouteClusterId = GatewayRouteClusterId

    @property
    def GatewayRouteCreateTime(self):
        return self._GatewayRouteCreateTime

    @GatewayRouteCreateTime.setter
    def GatewayRouteCreateTime(self, GatewayRouteCreateTime):
        self._GatewayRouteCreateTime = GatewayRouteCreateTime

    @property
    def FrequencyLimitConfig(self):
        return self._FrequencyLimitConfig

    @FrequencyLimitConfig.setter
    def FrequencyLimitConfig(self, FrequencyLimitConfig):
        self._FrequencyLimitConfig = FrequencyLimitConfig

    @property
    def GatewayRouteServerType(self):
        return self._GatewayRouteServerType

    @GatewayRouteServerType.setter
    def GatewayRouteServerType(self, GatewayRouteServerType):
        self._GatewayRouteServerType = GatewayRouteServerType

    @property
    def GatewayRouteServerName(self):
        return self._GatewayRouteServerName

    @GatewayRouteServerName.setter
    def GatewayRouteServerName(self, GatewayRouteServerName):
        self._GatewayRouteServerName = GatewayRouteServerName

    @property
    def GatewayRewriteHost(self):
        return self._GatewayRewriteHost

    @GatewayRewriteHost.setter
    def GatewayRewriteHost(self, GatewayRewriteHost):
        self._GatewayRewriteHost = GatewayRewriteHost

    @property
    def GatewayVersion(self):
        return self._GatewayVersion

    @GatewayVersion.setter
    def GatewayVersion(self, GatewayVersion):
        self._GatewayVersion = GatewayVersion

    @property
    def GatewayRoutePath(self):
        return self._GatewayRoutePath

    @GatewayRoutePath.setter
    def GatewayRoutePath(self, GatewayRoutePath):
        self._GatewayRoutePath = GatewayRoutePath

    @property
    def GatewayRouteMethod(self):
        return self._GatewayRouteMethod

    @GatewayRouteMethod.setter
    def GatewayRouteMethod(self, GatewayRouteMethod):
        self._GatewayRouteMethod = GatewayRouteMethod

    @property
    def GatewayRoutePort(self):
        return self._GatewayRoutePort

    @GatewayRoutePort.setter
    def GatewayRoutePort(self, GatewayRoutePort):
        self._GatewayRoutePort = GatewayRoutePort

    @property
    def GatewayRouteEnvId(self):
        return self._GatewayRouteEnvId

    @GatewayRouteEnvId.setter
    def GatewayRouteEnvId(self, GatewayRouteEnvId):
        self._GatewayRouteEnvId = GatewayRouteEnvId

    @property
    def GatewayRoutePathMatchType(self):
        return self._GatewayRoutePathMatchType

    @GatewayRoutePathMatchType.setter
    def GatewayRoutePathMatchType(self, GatewayRoutePathMatchType):
        self._GatewayRoutePathMatchType = GatewayRoutePathMatchType

    @property
    def CustomHeader(self):
        return self._CustomHeader

    @CustomHeader.setter
    def CustomHeader(self, CustomHeader):
        self._CustomHeader = CustomHeader


    def _deserialize(self, params):
        self._GatewayRouteName = params.get("GatewayRouteName")
        self._GatewayRouteProtocol = params.get("GatewayRouteProtocol")
        self._GatewayRouteAddr = params.get("GatewayRouteAddr")
        self._GatewayRouteDesc = params.get("GatewayRouteDesc")
        self._GatewayRouteClusterId = params.get("GatewayRouteClusterId")
        self._GatewayRouteCreateTime = params.get("GatewayRouteCreateTime")
        if params.get("FrequencyLimitConfig") is not None:
            self._FrequencyLimitConfig = []
            for item in params.get("FrequencyLimitConfig"):
                obj = FrequencyLimitConfig()
                obj._deserialize(item)
                self._FrequencyLimitConfig.append(obj)
        self._GatewayRouteServerType = params.get("GatewayRouteServerType")
        self._GatewayRouteServerName = params.get("GatewayRouteServerName")
        self._GatewayRewriteHost = params.get("GatewayRewriteHost")
        self._GatewayVersion = params.get("GatewayVersion")
        self._GatewayRoutePath = params.get("GatewayRoutePath")
        self._GatewayRouteMethod = params.get("GatewayRouteMethod")
        self._GatewayRoutePort = params.get("GatewayRoutePort")
        self._GatewayRouteEnvId = params.get("GatewayRouteEnvId")
        self._GatewayRoutePathMatchType = params.get("GatewayRoutePathMatchType")
        if params.get("CustomHeader") is not None:
            self._CustomHeader = CustomHeader()
            self._CustomHeader._deserialize(params.get("CustomHeader"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        