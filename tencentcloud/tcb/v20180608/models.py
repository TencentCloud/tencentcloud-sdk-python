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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AuthDomain(AbstractModel):
    r"""合法域名

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
        r"""域名ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        r"""域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Type(self):
        r"""域名类型。包含以下取值：
<li>SYSTEM</li>
<li>USER</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""状态。包含以下取值：
<li>ENABLE</li>
<li>DISABLE</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
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
    r"""云开发新套餐详情

    """

    def __init__(self):
        r"""
        :param _PackageName: DAU产品套餐ID
        :type PackageName: str
        :param _PackageTitle: DAU套餐中文名称
        :type PackageTitle: str
        :param _GroupName: 套餐分组
        :type GroupName: str
        :param _GroupTitle: 套餐分组中文名
        :type GroupTitle: str
        :param _BillTags: json格式化计费标签，例如：
{"pid":2, "cids":{"create": 2, "renew": 2, "modify": 2}, "productCode":"p_tcb_mp", "subProductCode":"sp_tcb_mp_cloudbase_dau"}
        :type BillTags: str
        :param _ResourceLimit: json格式化用户资源限制，例如：
{"Qps":1000,"InvokeNum":{"TimeUnit":"m", "Unit":"万次", "MaxSize": 100},"Capacity":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}, "Cdn":{"Flux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}, "BackFlux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}},"Scf":{"Concurrency":1000,"OutFlux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100},"MemoryUse":{"TimeUnit":"m", "Unit":"WGBS", "MaxSize": 100000}}}
        :type ResourceLimit: str
        :param _AdvanceLimit: json格式化高级限制，例如：
{"CMSEnable":false,"ProvisionedConcurrencyMem":512000, "PictureProcessing":false, "SecurityAudit":false, "RealTimePush":false, "TemplateMessageBatchPush":false, "Payment":false}
        :type AdvanceLimit: str
        :param _PackageDescription: 套餐描述
        :type PackageDescription: str
        :param _IsExternal: 是否对外展示
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
        r"""DAU产品套餐ID
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageTitle(self):
        r"""DAU套餐中文名称
        :rtype: str
        """
        return self._PackageTitle

    @PackageTitle.setter
    def PackageTitle(self, PackageTitle):
        self._PackageTitle = PackageTitle

    @property
    def GroupName(self):
        r"""套餐分组
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupTitle(self):
        r"""套餐分组中文名
        :rtype: str
        """
        return self._GroupTitle

    @GroupTitle.setter
    def GroupTitle(self, GroupTitle):
        self._GroupTitle = GroupTitle

    @property
    def BillTags(self):
        r"""json格式化计费标签，例如：
{"pid":2, "cids":{"create": 2, "renew": 2, "modify": 2}, "productCode":"p_tcb_mp", "subProductCode":"sp_tcb_mp_cloudbase_dau"}
        :rtype: str
        """
        return self._BillTags

    @BillTags.setter
    def BillTags(self, BillTags):
        self._BillTags = BillTags

    @property
    def ResourceLimit(self):
        r"""json格式化用户资源限制，例如：
{"Qps":1000,"InvokeNum":{"TimeUnit":"m", "Unit":"万次", "MaxSize": 100},"Capacity":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}, "Cdn":{"Flux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}, "BackFlux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100}},"Scf":{"Concurrency":1000,"OutFlux":{"TimeUnit":"m", "Unit":"GB", "MaxSize": 100},"MemoryUse":{"TimeUnit":"m", "Unit":"WGBS", "MaxSize": 100000}}}
        :rtype: str
        """
        return self._ResourceLimit

    @ResourceLimit.setter
    def ResourceLimit(self, ResourceLimit):
        self._ResourceLimit = ResourceLimit

    @property
    def AdvanceLimit(self):
        r"""json格式化高级限制，例如：
{"CMSEnable":false,"ProvisionedConcurrencyMem":512000, "PictureProcessing":false, "SecurityAudit":false, "RealTimePush":false, "TemplateMessageBatchPush":false, "Payment":false}
        :rtype: str
        """
        return self._AdvanceLimit

    @AdvanceLimit.setter
    def AdvanceLimit(self, AdvanceLimit):
        self._AdvanceLimit = AdvanceLimit

    @property
    def PackageDescription(self):
        r"""套餐描述
        :rtype: str
        """
        return self._PackageDescription

    @PackageDescription.setter
    def PackageDescription(self, PackageDescription):
        self._PackageDescription = PackageDescription

    @property
    def IsExternal(self):
        r"""是否对外展示
        :rtype: bool
        """
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
        


class BindCloudBaseAccessDomainRequest(AbstractModel):
    r"""BindCloudBaseAccessDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务Id，目前是指环境Id
        :type ServiceId: str
        :param _Domain: 自定义域名
        :type Domain: str
        :param _CertId: 腾讯云证书Id
        :type CertId: str
        :param _BindFlag: 默认1，1 绑定默认Cdn，2 绑定TcbIngress（不经过cdn），4 绑定自定义cdn
        :type BindFlag: int
        :param _CustomCname: 自定义cdn cname域名
        :type CustomCname: str
        """
        self._ServiceId = None
        self._Domain = None
        self._CertId = None
        self._BindFlag = None
        self._CustomCname = None

    @property
    def ServiceId(self):
        r"""服务Id，目前是指环境Id
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Domain(self):
        r"""自定义域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        r"""腾讯云证书Id
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def BindFlag(self):
        r"""默认1，1 绑定默认Cdn，2 绑定TcbIngress（不经过cdn），4 绑定自定义cdn
        :rtype: int
        """
        return self._BindFlag

    @BindFlag.setter
    def BindFlag(self, BindFlag):
        self._BindFlag = BindFlag

    @property
    def CustomCname(self):
        r"""自定义cdn cname域名
        :rtype: str
        """
        return self._CustomCname

    @CustomCname.setter
    def CustomCname(self, CustomCname):
        self._CustomCname = CustomCname


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._BindFlag = params.get("BindFlag")
        self._CustomCname = params.get("CustomCname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudBaseAccessDomainResponse(AbstractModel):
    r"""BindCloudBaseAccessDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务Id，目前是指环境Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceId = None
        self._RequestId = None

    @property
    def ServiceId(self):
        r"""服务Id，目前是指环境Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._RequestId = params.get("RequestId")


class BindCloudBaseGWDomainRequest(AbstractModel):
    r"""BindCloudBaseGWDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _Domain: 服务域名
        :type Domain: str
        :param _CertId: 证书ID
        :type CertId: str
        :param _EnableRegion: 是否启用多地域
        :type EnableRegion: bool
        """
        self._ServiceId = None
        self._Domain = None
        self._CertId = None
        self._EnableRegion = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Domain(self):
        r"""服务域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        r"""证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def EnableRegion(self):
        r"""是否启用多地域
        :rtype: bool
        """
        return self._EnableRegion

    @EnableRegion.setter
    def EnableRegion(self, EnableRegion):
        self._EnableRegion = EnableRegion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._EnableRegion = params.get("EnableRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudBaseGWDomainResponse(AbstractModel):
    r"""BindCloudBaseGWDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CheckTcbServiceRequest(AbstractModel):
    r"""CheckTcbService请求参数结构体

    """


class CheckTcbServiceResponse(AbstractModel):
    r"""CheckTcbService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Initialized: true表示已开通
        :type Initialized: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Initialized = None
        self._RequestId = None

    @property
    def Initialized(self):
        r"""true表示已开通
        :rtype: bool
        """
        return self._Initialized

    @Initialized.setter
    def Initialized(self, Initialized):
        self._Initialized = Initialized

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Initialized = params.get("Initialized")
        self._RequestId = params.get("RequestId")


class CloudBaseClientQPSPolicy(AbstractModel):
    r"""http访问服务客户端限频

    """

    def __init__(self):
        r"""
        :param _LimitBy: UserID 或 ClientIP 或 None，如果为 None 代表不限制
        :type LimitBy: str
        :param _LimitValue: 限制值
        :type LimitValue: int
        """
        self._LimitBy = None
        self._LimitValue = None

    @property
    def LimitBy(self):
        r"""UserID 或 ClientIP 或 None，如果为 None 代表不限制
        :rtype: str
        """
        return self._LimitBy

    @LimitBy.setter
    def LimitBy(self, LimitBy):
        self._LimitBy = LimitBy

    @property
    def LimitValue(self):
        r"""限制值
        :rtype: int
        """
        return self._LimitValue

    @LimitValue.setter
    def LimitValue(self, LimitValue):
        self._LimitValue = LimitValue


    def _deserialize(self, params):
        self._LimitBy = params.get("LimitBy")
        self._LimitValue = params.get("LimitValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseGWAPI(AbstractModel):
    r"""tcb 网关API

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _APIId: API ID
        :type APIId: str
        :param _Path: API Path
        :type Path: str
        :param _Type: API 类型
        :type Type: int
        :param _Name: API 名
        :type Name: str
        :param _CreateTime: API创建时间
        :type CreateTime: int
        :param _Custom: 自定义值通用字段：
Type为1时，该值为空。
Type为2时，该值为容器的代理IP:PORT数组。
        :type Custom: str
        :param _EnableAuth: 表示是否开启认证
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableAuth: bool
        :param _EnvId: 云开发环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param _AccessType: 访问类型（该参数暂不对外暴露）
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessType: int
        :param _UnionStatus: 统一发布状态
注意：此字段可能返回 null，表示取不到有效值。
        :type UnionStatus: int
        :param _Domain: 域名（*表示所有域名）
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _ConflictFlag: 是否有路径冲突
注意：此字段可能返回 null，表示取不到有效值。
        :type ConflictFlag: bool
        :param _DomainStatus: 域名状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainStatus: int
        :param _IsShortPath: 是否开启路径透传，默认true表示短路径，即不开启(已弃用)
注意：此字段可能返回 null，表示取不到有效值。
        :type IsShortPath: bool
        :param _PathTransmission: 路径透传，默认0关闭，1开启，2关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type PathTransmission: int
        :param _EnableCheckAcrossDomain: 跨域校验，默认0开启，1开启，2关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableCheckAcrossDomain: int
        :param _StaticFileDirectory: 静态托管文件目录
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticFileDirectory: str
        :param _QPSPolicy: QPS策略
        :type QPSPolicy: :class:`tencentcloud.tcb.v20180608.models.CloudBaseGWAPIQPSPolicy`
        """
        self._ServiceId = None
        self._APIId = None
        self._Path = None
        self._Type = None
        self._Name = None
        self._CreateTime = None
        self._Custom = None
        self._EnableAuth = None
        self._EnvId = None
        self._AccessType = None
        self._UnionStatus = None
        self._Domain = None
        self._ConflictFlag = None
        self._DomainStatus = None
        self._IsShortPath = None
        self._PathTransmission = None
        self._EnableCheckAcrossDomain = None
        self._StaticFileDirectory = None
        self._QPSPolicy = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def APIId(self):
        r"""API ID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def Path(self):
        r"""API Path
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Type(self):
        r"""API 类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""API 名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        r"""API创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Custom(self):
        r"""自定义值通用字段：
Type为1时，该值为空。
Type为2时，该值为容器的代理IP:PORT数组。
        :rtype: str
        """
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom

    @property
    def EnableAuth(self):
        r"""表示是否开启认证
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableAuth

    @EnableAuth.setter
    def EnableAuth(self, EnableAuth):
        self._EnableAuth = EnableAuth

    @property
    def EnvId(self):
        r"""云开发环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def AccessType(self):
        r"""访问类型（该参数暂不对外暴露）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def UnionStatus(self):
        r"""统一发布状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UnionStatus

    @UnionStatus.setter
    def UnionStatus(self, UnionStatus):
        self._UnionStatus = UnionStatus

    @property
    def Domain(self):
        r"""域名（*表示所有域名）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ConflictFlag(self):
        r"""是否有路径冲突
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ConflictFlag

    @ConflictFlag.setter
    def ConflictFlag(self, ConflictFlag):
        self._ConflictFlag = ConflictFlag

    @property
    def DomainStatus(self):
        r"""域名状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DomainStatus

    @DomainStatus.setter
    def DomainStatus(self, DomainStatus):
        self._DomainStatus = DomainStatus

    @property
    def IsShortPath(self):
        r"""是否开启路径透传，默认true表示短路径，即不开启(已弃用)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsShortPath

    @IsShortPath.setter
    def IsShortPath(self, IsShortPath):
        self._IsShortPath = IsShortPath

    @property
    def PathTransmission(self):
        r"""路径透传，默认0关闭，1开启，2关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PathTransmission

    @PathTransmission.setter
    def PathTransmission(self, PathTransmission):
        self._PathTransmission = PathTransmission

    @property
    def EnableCheckAcrossDomain(self):
        r"""跨域校验，默认0开启，1开启，2关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EnableCheckAcrossDomain

    @EnableCheckAcrossDomain.setter
    def EnableCheckAcrossDomain(self, EnableCheckAcrossDomain):
        self._EnableCheckAcrossDomain = EnableCheckAcrossDomain

    @property
    def StaticFileDirectory(self):
        r"""静态托管文件目录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StaticFileDirectory

    @StaticFileDirectory.setter
    def StaticFileDirectory(self, StaticFileDirectory):
        self._StaticFileDirectory = StaticFileDirectory

    @property
    def QPSPolicy(self):
        r"""QPS策略
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CloudBaseGWAPIQPSPolicy`
        """
        return self._QPSPolicy

    @QPSPolicy.setter
    def QPSPolicy(self, QPSPolicy):
        self._QPSPolicy = QPSPolicy


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._APIId = params.get("APIId")
        self._Path = params.get("Path")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        self._Custom = params.get("Custom")
        self._EnableAuth = params.get("EnableAuth")
        self._EnvId = params.get("EnvId")
        self._AccessType = params.get("AccessType")
        self._UnionStatus = params.get("UnionStatus")
        self._Domain = params.get("Domain")
        self._ConflictFlag = params.get("ConflictFlag")
        self._DomainStatus = params.get("DomainStatus")
        self._IsShortPath = params.get("IsShortPath")
        self._PathTransmission = params.get("PathTransmission")
        self._EnableCheckAcrossDomain = params.get("EnableCheckAcrossDomain")
        self._StaticFileDirectory = params.get("StaticFileDirectory")
        if params.get("QPSPolicy") is not None:
            self._QPSPolicy = CloudBaseGWAPIQPSPolicy()
            self._QPSPolicy._deserialize(params.get("QPSPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseGWAPIQPSPolicy(AbstractModel):
    r"""http访问服务路由qps策略

    """

    def __init__(self):
        r"""
        :param _QPSTotal: qps限额总量
        :type QPSTotal: int
        :param _QPSPerClient: 客户端限频，如果不限制，LimitBy=None
        :type QPSPerClient: :class:`tencentcloud.tcb.v20180608.models.CloudBaseClientQPSPolicy`
        """
        self._QPSTotal = None
        self._QPSPerClient = None

    @property
    def QPSTotal(self):
        r"""qps限额总量
        :rtype: int
        """
        return self._QPSTotal

    @QPSTotal.setter
    def QPSTotal(self, QPSTotal):
        self._QPSTotal = QPSTotal

    @property
    def QPSPerClient(self):
        r"""客户端限频，如果不限制，LimitBy=None
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CloudBaseClientQPSPolicy`
        """
        return self._QPSPerClient

    @QPSPerClient.setter
    def QPSPerClient(self, QPSPerClient):
        self._QPSPerClient = QPSPerClient


    def _deserialize(self, params):
        self._QPSTotal = params.get("QPSTotal")
        if params.get("QPSPerClient") is not None:
            self._QPSPerClient = CloudBaseClientQPSPolicy()
            self._QPSPerClient._deserialize(params.get("QPSPerClient"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseGWService(AbstractModel):
    r"""网关服务

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _Domain: 服务域名
        :type Domain: str
        :param _OpenTime: 开启时间
        :type OpenTime: int
        :param _Status: 绑定状态，1 绑定中；2绑定失败；3绑定成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _IsPreempted: 是否被抢占, 被抢占表示域名被其他环境绑定了，需要解绑或者重新绑定。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPreempted: bool
        :param _EnableRegion: 是否开启多地域
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableRegion: bool
        :param _Cname: cdn CName地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param _UnionStatus: 统一域名状态
注意：此字段可能返回 null，表示取不到有效值。
        :type UnionStatus: int
        :param _CnameStatus: CName状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CnameStatus: int
        :param _CertId: 证书Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _ForceHttps: 是否强制https
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceHttps: bool
        :param _IcpForbidStatus: icp黑名单封禁状态，0-未封禁，1-封禁
注意：此字段可能返回 null，表示取不到有效值。
        :type IcpForbidStatus: int
        :param _CustomRoutingRules: 自定义路由规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomRoutingRules: str
        :param _BindFlag: 绑定类型，1绑定cdn，2源站，4自定义
        :type BindFlag: int
        :param _OriginCname: TcbIngress源站cname
        :type OriginCname: str
        :param _CustomCname: 自定义cname
        :type CustomCname: str
        """
        self._ServiceId = None
        self._Domain = None
        self._OpenTime = None
        self._Status = None
        self._IsPreempted = None
        self._EnableRegion = None
        self._Cname = None
        self._UnionStatus = None
        self._CnameStatus = None
        self._CertId = None
        self._ForceHttps = None
        self._IcpForbidStatus = None
        self._CustomRoutingRules = None
        self._BindFlag = None
        self._OriginCname = None
        self._CustomCname = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Domain(self):
        r"""服务域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def OpenTime(self):
        r"""开启时间
        :rtype: int
        """
        return self._OpenTime

    @OpenTime.setter
    def OpenTime(self, OpenTime):
        self._OpenTime = OpenTime

    @property
    def Status(self):
        r"""绑定状态，1 绑定中；2绑定失败；3绑定成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsPreempted(self):
        r"""是否被抢占, 被抢占表示域名被其他环境绑定了，需要解绑或者重新绑定。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsPreempted

    @IsPreempted.setter
    def IsPreempted(self, IsPreempted):
        self._IsPreempted = IsPreempted

    @property
    def EnableRegion(self):
        r"""是否开启多地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableRegion

    @EnableRegion.setter
    def EnableRegion(self, EnableRegion):
        self._EnableRegion = EnableRegion

    @property
    def Cname(self):
        r"""cdn CName地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def UnionStatus(self):
        r"""统一域名状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UnionStatus

    @UnionStatus.setter
    def UnionStatus(self, UnionStatus):
        self._UnionStatus = UnionStatus

    @property
    def CnameStatus(self):
        r"""CName状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CnameStatus

    @CnameStatus.setter
    def CnameStatus(self, CnameStatus):
        self._CnameStatus = CnameStatus

    @property
    def CertId(self):
        r"""证书Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def ForceHttps(self):
        r"""是否强制https
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ForceHttps

    @ForceHttps.setter
    def ForceHttps(self, ForceHttps):
        self._ForceHttps = ForceHttps

    @property
    def IcpForbidStatus(self):
        r"""icp黑名单封禁状态，0-未封禁，1-封禁
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IcpForbidStatus

    @IcpForbidStatus.setter
    def IcpForbidStatus(self, IcpForbidStatus):
        self._IcpForbidStatus = IcpForbidStatus

    @property
    def CustomRoutingRules(self):
        r"""自定义路由规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CustomRoutingRules

    @CustomRoutingRules.setter
    def CustomRoutingRules(self, CustomRoutingRules):
        self._CustomRoutingRules = CustomRoutingRules

    @property
    def BindFlag(self):
        r"""绑定类型，1绑定cdn，2源站，4自定义
        :rtype: int
        """
        return self._BindFlag

    @BindFlag.setter
    def BindFlag(self, BindFlag):
        self._BindFlag = BindFlag

    @property
    def OriginCname(self):
        r"""TcbIngress源站cname
        :rtype: str
        """
        return self._OriginCname

    @OriginCname.setter
    def OriginCname(self, OriginCname):
        self._OriginCname = OriginCname

    @property
    def CustomCname(self):
        r"""自定义cname
        :rtype: str
        """
        return self._CustomCname

    @CustomCname.setter
    def CustomCname(self, CustomCname):
        self._CustomCname = CustomCname


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Domain = params.get("Domain")
        self._OpenTime = params.get("OpenTime")
        self._Status = params.get("Status")
        self._IsPreempted = params.get("IsPreempted")
        self._EnableRegion = params.get("EnableRegion")
        self._Cname = params.get("Cname")
        self._UnionStatus = params.get("UnionStatus")
        self._CnameStatus = params.get("CnameStatus")
        self._CertId = params.get("CertId")
        self._ForceHttps = params.get("ForceHttps")
        self._IcpForbidStatus = params.get("IcpForbidStatus")
        self._CustomRoutingRules = params.get("CustomRoutingRules")
        self._BindFlag = params.get("BindFlag")
        self._OriginCname = params.get("OriginCname")
        self._CustomCname = params.get("CustomCname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudBaseOption(AbstractModel):
    r"""http service选项

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
        r"""键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""值
        :rtype: str
        """
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
        


class ClsInfo(AbstractModel):
    r"""cls日志信息

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
        r"""cls所属地域
        :rtype: str
        """
        return self._ClsRegion

    @ClsRegion.setter
    def ClsRegion(self, ClsRegion):
        self._ClsRegion = ClsRegion

    @property
    def ClsLogsetId(self):
        r"""cls日志集ID
        :rtype: str
        """
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsTopicId(self):
        r"""cls日志主题ID
        :rtype: str
        """
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
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
        


class ClusterDetail(AbstractModel):
    r"""TDSQL-C数据库详情

    """

    def __init__(self):
        r"""
        :param _IsOpenPubNetAccess: 是否开启公网访问
        :type IsOpenPubNetAccess: bool
        :param _MaxCpu: 最大算力
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxCpu: float
        :param _MinCpu: 最小算力
注意：此字段可能返回 null，表示取不到有效值。
        :type MinCpu: float
        :param _Status: TDSQL-C集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _UsedStorage: 存储用量（单位：MB）
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedStorage: int
        :param _StorageLimit: 最大存储量（单位：GB）
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLimit: int
        :param _DbType: 数据库类型
        :type DbType: str
        :param _DbVersion: 数据库类型
        :type DbVersion: str
        :param _WanStatus: 公网访问状态；open开启，opening开启中，closed关闭，closing关闭中
        :type WanStatus: str
        :param _ClusterStatus: 数据库集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStatus: str
        :param _ServerlessStatus: serverless状态
        :type ServerlessStatus: str
        """
        self._IsOpenPubNetAccess = None
        self._MaxCpu = None
        self._MinCpu = None
        self._Status = None
        self._UsedStorage = None
        self._StorageLimit = None
        self._DbType = None
        self._DbVersion = None
        self._WanStatus = None
        self._ClusterStatus = None
        self._ServerlessStatus = None

    @property
    def IsOpenPubNetAccess(self):
        r"""是否开启公网访问
        :rtype: bool
        """
        return self._IsOpenPubNetAccess

    @IsOpenPubNetAccess.setter
    def IsOpenPubNetAccess(self, IsOpenPubNetAccess):
        self._IsOpenPubNetAccess = IsOpenPubNetAccess

    @property
    def MaxCpu(self):
        r"""最大算力
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MaxCpu

    @MaxCpu.setter
    def MaxCpu(self, MaxCpu):
        self._MaxCpu = MaxCpu

    @property
    def MinCpu(self):
        r"""最小算力
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MinCpu

    @MinCpu.setter
    def MinCpu(self, MinCpu):
        self._MinCpu = MinCpu

    @property
    def Status(self):
        r"""TDSQL-C集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UsedStorage(self):
        r"""存储用量（单位：MB）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UsedStorage

    @UsedStorage.setter
    def UsedStorage(self, UsedStorage):
        self._UsedStorage = UsedStorage

    @property
    def StorageLimit(self):
        r"""最大存储量（单位：GB）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def DbType(self):
        r"""数据库类型
        :rtype: str
        """
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbVersion(self):
        r"""数据库类型
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def WanStatus(self):
        r"""公网访问状态；open开启，opening开启中，closed关闭，closing关闭中
        :rtype: str
        """
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def ClusterStatus(self):
        r"""数据库集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def ServerlessStatus(self):
        r"""serverless状态
        :rtype: str
        """
        return self._ServerlessStatus

    @ServerlessStatus.setter
    def ServerlessStatus(self, ServerlessStatus):
        self._ServerlessStatus = ServerlessStatus


    def _deserialize(self, params):
        self._IsOpenPubNetAccess = params.get("IsOpenPubNetAccess")
        self._MaxCpu = params.get("MaxCpu")
        self._MinCpu = params.get("MinCpu")
        self._Status = params.get("Status")
        self._UsedStorage = params.get("UsedStorage")
        self._StorageLimit = params.get("StorageLimit")
        self._DbType = params.get("DbType")
        self._DbVersion = params.get("DbVersion")
        self._WanStatus = params.get("WanStatus")
        self._ClusterStatus = params.get("ClusterStatus")
        self._ServerlessStatus = params.get("ServerlessStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuthDomainRequest(AbstractModel):
    r"""CreateAuthDomain请求参数结构体

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
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Domains(self):
        r"""安全域名
        :rtype: list of str
        """
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
    r"""CreateAuthDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateBillDealRequest(AbstractModel):
    r"""CreateBillDeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealType: 当前下单的操作类型，可取[purchase,renew,modify]三种值，分别代表新购，续费，变配。
        :type DealType: str
        :param _ProductType: 购买的产品类型，可取[tcb-baas,tcb-promotion,tcb-package], 分别代表baas套餐、大促包、资源包
        :type ProductType: str
        :param _PackageId: 目标下单产品/套餐Id。
对于云开发环境套餐，可通过 DescribeBaasPackageList 接口获取，对应其出参的PackageName
        :type PackageId: str
        :param _CreateAndPay: 默认只下单不支付，为ture则下单并支付。
如果需要下单并支付，请确保账户下有足够的余额，否则会导致下单失败。
        :type CreateAndPay: bool
        :param _TimeSpan: 购买时长，与TimeUnit字段搭配使用。
        :type TimeSpan: int
        :param _TimeUnit: 购买时长单位,按各产品规则可选d(天),m(月),y(年),p(一次性)。
对于 云开发环境的 新购和续费，目前仅支持 按月购买（即 TimeUnit=m）。
        :type TimeUnit: str
        :param _ResourceId: 资源唯一标识。
在云开发环境 续费和变配 场景下必传，取值为环境ID。
        :type ResourceId: str
        :param _Source: 来源可选[qcloud,miniapp]，默认qcloud。
miniapp表示微信云开发，主要适用于[小程序云开发](https://developers.weixin.qq.com/miniprogram/dev/wxcloudservice/wxcloud/billing/price.html)。

        :type Source: str
        :param _Alias: 环境别名，用于新购云开发环境时，给云开发环境起别名。
仅当 新购云开发环境（DealType=purchase 并且 ProductType=tcb-baas ）时有效。

### 格式要求
- 可选字符： 小写字母(a~z)、数字、减号(-)
- 不能以 减号(-) 开头或结尾
- 不能有连个连续的 减号(-)
- 长度不超过20位
        :type Alias: str
        :param _EnvId: 环境id，当购买资源包和大促包时（ProductType取值为tcb-promotion 或 tcb-package）必传，表示资源包在哪个环境下生效。
        :type EnvId: str
        :param _EnableExcess: 开启超限按量。
开启后，当 套餐内的资源点 和 资源包 都用尽后，会自动按量计费。
详见 [计费说明](https://cloud.tencent.com/document/product/876/127357)。
        :type EnableExcess: bool
        :param _ModifyPackageId: 变配目标套餐id，对于云开发环境变配场景下必传。
对于云开发环境套餐，可通过 DescribeBaasPackageList 接口获取，对应其出参的PackageName
        :type ModifyPackageId: str
        :param _Extension: jsonstr附加信息
        :type Extension: str
        :param _AutoVoucher: 是否自动选择代金券支付。
        :type AutoVoucher: bool
        :param _ResourceTypes: 资源类型。
代表新购环境（DealType=purchase 并且 ProductType=tcb-baas ）时需要发货哪些资源。
可取值：flexdb, cos, cdn, scf

        :type ResourceTypes: list of str
        :param _EnvTags: 环境标签。
 代表新购环境（DealType=purchase 并且 ProductType=tcb-baas ）时需要打的标签。

        :type EnvTags: list of Tag
        """
        self._DealType = None
        self._ProductType = None
        self._PackageId = None
        self._CreateAndPay = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._ResourceId = None
        self._Source = None
        self._Alias = None
        self._EnvId = None
        self._EnableExcess = None
        self._ModifyPackageId = None
        self._Extension = None
        self._AutoVoucher = None
        self._ResourceTypes = None
        self._EnvTags = None

    @property
    def DealType(self):
        r"""当前下单的操作类型，可取[purchase,renew,modify]三种值，分别代表新购，续费，变配。
        :rtype: str
        """
        return self._DealType

    @DealType.setter
    def DealType(self, DealType):
        self._DealType = DealType

    @property
    def ProductType(self):
        r"""购买的产品类型，可取[tcb-baas,tcb-promotion,tcb-package], 分别代表baas套餐、大促包、资源包
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def PackageId(self):
        r"""目标下单产品/套餐Id。
对于云开发环境套餐，可通过 DescribeBaasPackageList 接口获取，对应其出参的PackageName
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def CreateAndPay(self):
        r"""默认只下单不支付，为ture则下单并支付。
如果需要下单并支付，请确保账户下有足够的余额，否则会导致下单失败。
        :rtype: bool
        """
        return self._CreateAndPay

    @CreateAndPay.setter
    def CreateAndPay(self, CreateAndPay):
        self._CreateAndPay = CreateAndPay

    @property
    def TimeSpan(self):
        r"""购买时长，与TimeUnit字段搭配使用。
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""购买时长单位,按各产品规则可选d(天),m(月),y(年),p(一次性)。
对于 云开发环境的 新购和续费，目前仅支持 按月购买（即 TimeUnit=m）。
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def ResourceId(self):
        r"""资源唯一标识。
在云开发环境 续费和变配 场景下必传，取值为环境ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Source(self):
        r"""来源可选[qcloud,miniapp]，默认qcloud。
miniapp表示微信云开发，主要适用于[小程序云开发](https://developers.weixin.qq.com/miniprogram/dev/wxcloudservice/wxcloud/billing/price.html)。

        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Alias(self):
        r"""环境别名，用于新购云开发环境时，给云开发环境起别名。
仅当 新购云开发环境（DealType=purchase 并且 ProductType=tcb-baas ）时有效。

### 格式要求
- 可选字符： 小写字母(a~z)、数字、减号(-)
- 不能以 减号(-) 开头或结尾
- 不能有连个连续的 减号(-)
- 长度不超过20位
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def EnvId(self):
        r"""环境id，当购买资源包和大促包时（ProductType取值为tcb-promotion 或 tcb-package）必传，表示资源包在哪个环境下生效。
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnableExcess(self):
        r"""开启超限按量。
开启后，当 套餐内的资源点 和 资源包 都用尽后，会自动按量计费。
详见 [计费说明](https://cloud.tencent.com/document/product/876/127357)。
        :rtype: bool
        """
        return self._EnableExcess

    @EnableExcess.setter
    def EnableExcess(self, EnableExcess):
        self._EnableExcess = EnableExcess

    @property
    def ModifyPackageId(self):
        r"""变配目标套餐id，对于云开发环境变配场景下必传。
对于云开发环境套餐，可通过 DescribeBaasPackageList 接口获取，对应其出参的PackageName
        :rtype: str
        """
        return self._ModifyPackageId

    @ModifyPackageId.setter
    def ModifyPackageId(self, ModifyPackageId):
        self._ModifyPackageId = ModifyPackageId

    @property
    def Extension(self):
        r"""jsonstr附加信息
        :rtype: str
        """
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension

    @property
    def AutoVoucher(self):
        r"""是否自动选择代金券支付。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def ResourceTypes(self):
        r"""资源类型。
代表新购环境（DealType=purchase 并且 ProductType=tcb-baas ）时需要发货哪些资源。
可取值：flexdb, cos, cdn, scf

        :rtype: list of str
        """
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def EnvTags(self):
        r"""环境标签。
 代表新购环境（DealType=purchase 并且 ProductType=tcb-baas ）时需要打的标签。

        :rtype: list of Tag
        """
        return self._EnvTags

    @EnvTags.setter
    def EnvTags(self, EnvTags):
        self._EnvTags = EnvTags


    def _deserialize(self, params):
        self._DealType = params.get("DealType")
        self._ProductType = params.get("ProductType")
        self._PackageId = params.get("PackageId")
        self._CreateAndPay = params.get("CreateAndPay")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._ResourceId = params.get("ResourceId")
        self._Source = params.get("Source")
        self._Alias = params.get("Alias")
        self._EnvId = params.get("EnvId")
        self._EnableExcess = params.get("EnableExcess")
        self._ModifyPackageId = params.get("ModifyPackageId")
        self._Extension = params.get("Extension")
        self._AutoVoucher = params.get("AutoVoucher")
        self._ResourceTypes = params.get("ResourceTypes")
        if params.get("EnvTags") is not None:
            self._EnvTags = []
            for item in params.get("EnvTags"):
                obj = Tag()
                obj._deserialize(item)
                self._EnvTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBillDealResponse(AbstractModel):
    r"""CreateBillDeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCloudBaseGWAPIRequest(AbstractModel):
    r"""CreateCloudBaseGWAPI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _Path: API Path
        :type Path: str
        :param _Type: API类型（1表示云函数，2表示容器）
        :type Type: int
        :param _Name: API Name
        :type Name: str
        :param _APIId: APIId，如果非空，表示修改绑定Path
        :type APIId: str
        :param _Custom: 自定义值通用字段（当Type为容器时必填）
        :type Custom: str
        :param _AuthSwitch: 认证开关 1为开启 2为关闭
        :type AuthSwitch: int
        :param _EnableRegion: 是否开启多地域
        :type EnableRegion: bool
        :param _EnableUnion: 是否启用统一域名
        :type EnableUnion: bool
        :param _Domain: 域名
        :type Domain: str
        :param _AccessTypes: 访问类型："OA", "PUBLIC", "MINIAPP", "VPC" （不传默认PUBLIC+MINIAPP+VPC）
        :type AccessTypes: list of str
        :param _IsShortPath: 是否开启路径透传，默认true表示短路径，即不开启路径透传(已弃用)
        :type IsShortPath: bool
        :param _PathTransmission: 路径透传，默认0关闭，1开启，2关闭
        :type PathTransmission: int
        :param _EnableCheckAcrossDomain: 跨域校验，默认0开启，1开启，2关闭
        :type EnableCheckAcrossDomain: int
        :param _StaticFileDirectory: 静态托管资源目录
        :type StaticFileDirectory: str
        """
        self._ServiceId = None
        self._Path = None
        self._Type = None
        self._Name = None
        self._APIId = None
        self._Custom = None
        self._AuthSwitch = None
        self._EnableRegion = None
        self._EnableUnion = None
        self._Domain = None
        self._AccessTypes = None
        self._IsShortPath = None
        self._PathTransmission = None
        self._EnableCheckAcrossDomain = None
        self._StaticFileDirectory = None

    @property
    def ServiceId(self):
        r"""Service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Path(self):
        r"""API Path
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Type(self):
        r"""API类型（1表示云函数，2表示容器）
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""API Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def APIId(self):
        r"""APIId，如果非空，表示修改绑定Path
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def Custom(self):
        r"""自定义值通用字段（当Type为容器时必填）
        :rtype: str
        """
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom

    @property
    def AuthSwitch(self):
        r"""认证开关 1为开启 2为关闭
        :rtype: int
        """
        return self._AuthSwitch

    @AuthSwitch.setter
    def AuthSwitch(self, AuthSwitch):
        self._AuthSwitch = AuthSwitch

    @property
    def EnableRegion(self):
        r"""是否开启多地域
        :rtype: bool
        """
        return self._EnableRegion

    @EnableRegion.setter
    def EnableRegion(self, EnableRegion):
        self._EnableRegion = EnableRegion

    @property
    def EnableUnion(self):
        r"""是否启用统一域名
        :rtype: bool
        """
        return self._EnableUnion

    @EnableUnion.setter
    def EnableUnion(self, EnableUnion):
        self._EnableUnion = EnableUnion

    @property
    def Domain(self):
        r"""域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AccessTypes(self):
        r"""访问类型："OA", "PUBLIC", "MINIAPP", "VPC" （不传默认PUBLIC+MINIAPP+VPC）
        :rtype: list of str
        """
        return self._AccessTypes

    @AccessTypes.setter
    def AccessTypes(self, AccessTypes):
        self._AccessTypes = AccessTypes

    @property
    def IsShortPath(self):
        r"""是否开启路径透传，默认true表示短路径，即不开启路径透传(已弃用)
        :rtype: bool
        """
        return self._IsShortPath

    @IsShortPath.setter
    def IsShortPath(self, IsShortPath):
        self._IsShortPath = IsShortPath

    @property
    def PathTransmission(self):
        r"""路径透传，默认0关闭，1开启，2关闭
        :rtype: int
        """
        return self._PathTransmission

    @PathTransmission.setter
    def PathTransmission(self, PathTransmission):
        self._PathTransmission = PathTransmission

    @property
    def EnableCheckAcrossDomain(self):
        r"""跨域校验，默认0开启，1开启，2关闭
        :rtype: int
        """
        return self._EnableCheckAcrossDomain

    @EnableCheckAcrossDomain.setter
    def EnableCheckAcrossDomain(self, EnableCheckAcrossDomain):
        self._EnableCheckAcrossDomain = EnableCheckAcrossDomain

    @property
    def StaticFileDirectory(self):
        r"""静态托管资源目录
        :rtype: str
        """
        return self._StaticFileDirectory

    @StaticFileDirectory.setter
    def StaticFileDirectory(self, StaticFileDirectory):
        self._StaticFileDirectory = StaticFileDirectory


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Path = params.get("Path")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._APIId = params.get("APIId")
        self._Custom = params.get("Custom")
        self._AuthSwitch = params.get("AuthSwitch")
        self._EnableRegion = params.get("EnableRegion")
        self._EnableUnion = params.get("EnableUnion")
        self._Domain = params.get("Domain")
        self._AccessTypes = params.get("AccessTypes")
        self._IsShortPath = params.get("IsShortPath")
        self._PathTransmission = params.get("PathTransmission")
        self._EnableCheckAcrossDomain = params.get("EnableCheckAcrossDomain")
        self._StaticFileDirectory = params.get("StaticFileDirectory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudBaseGWAPIResponse(AbstractModel):
    r"""CreateCloudBaseGWAPI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _APIId: API ID
注意：此字段可能返回 null，表示取不到有效值。
        :type APIId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._APIId = None
        self._RequestId = None

    @property
    def APIId(self):
        r"""API ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._APIId = params.get("APIId")
        self._RequestId = params.get("RequestId")


class CreateEnvRequest(AbstractModel):
    r"""CreateEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Alias: 环境别名。

### 格式要求
- 可选字符： 小写字母(a~z)、数字、减号(-)
- 不能以 减号(-) 开头或结尾
- 不能有连个连续的 减号(-)
- 长度不超过20位
示例值：cloud
        :type Alias: str
        :param _PackageId: 云开发环境套餐Id。
对于云开发环境套餐，可通过 [DescribeBaasPackageList](https://cloud.tencent.com/document/product/876/78167) 接口获取，对应其出参的PackageName。
        :type PackageId: str
        :param _Resources: 资源类型。代表新购环境时需要发货哪些资源。
可取值以及含义：
- flexdb : 表示文档型数据库
- storage : 表示云存储
- function : 表示云函数

**该字段不可为空**
        :type Resources: list of str
        :param _Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24。
默认值为1，即1个月。
        :type Period: int
        :param _AutoVoucher: 是否自动选择代金券支付。
        :type AutoVoucher: bool
        :param _Tags: 环境标签。
可取值通过接口 [tag:DescribeTags](https://cloud.tencent.com/document/product/651/35316) 可获取到。
不传或为空则默认不打任何标签。
        :type Tags: list of Tag
        :param _RenewFlag: 自动续费标识。取值范围：
- NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
- NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费（需要手动续费，可通过接口 [RenewEnv](https://cloud.tencent.com/document/product/876/128590) 来续费）

默认取值：NOTIFY_AND_MANUAL_RENEW。
若该参数指定为NOTIFY_AND_AUTO_RENEW（即：自动续费），在账户余额充足的情况下，实例到期后将按月自动续费；但如果账户余额不足，将无法自动续费。请留意腾讯云短信和邮件通知。
        :type RenewFlag: str
        """
        self._Alias = None
        self._PackageId = None
        self._Resources = None
        self._Period = None
        self._AutoVoucher = None
        self._Tags = None
        self._RenewFlag = None

    @property
    def Alias(self):
        r"""环境别名。

### 格式要求
- 可选字符： 小写字母(a~z)、数字、减号(-)
- 不能以 减号(-) 开头或结尾
- 不能有连个连续的 减号(-)
- 长度不超过20位
示例值：cloud
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def PackageId(self):
        r"""云开发环境套餐Id。
对于云开发环境套餐，可通过 [DescribeBaasPackageList](https://cloud.tencent.com/document/product/876/78167) 接口获取，对应其出参的PackageName。
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Resources(self):
        r"""资源类型。代表新购环境时需要发货哪些资源。
可取值以及含义：
- flexdb : 表示文档型数据库
- storage : 表示云存储
- function : 表示云函数

**该字段不可为空**
        :rtype: list of str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Period(self):
        r"""购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24。
默认值为1，即1个月。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        r"""是否自动选择代金券支付。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def Tags(self):
        r"""环境标签。
可取值通过接口 [tag:DescribeTags](https://cloud.tencent.com/document/product/651/35316) 可获取到。
不传或为空则默认不打任何标签。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RenewFlag(self):
        r"""自动续费标识。取值范围：
- NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
- NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费（需要手动续费，可通过接口 [RenewEnv](https://cloud.tencent.com/document/product/876/128590) 来续费）

默认取值：NOTIFY_AND_MANUAL_RENEW。
若该参数指定为NOTIFY_AND_AUTO_RENEW（即：自动续费），在账户余额充足的情况下，实例到期后将按月自动续费；但如果账户余额不足，将无法自动续费。请留意腾讯云短信和邮件通知。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._PackageId = params.get("PackageId")
        self._Resources = params.get("Resources")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvResponse(AbstractModel):
    r"""CreateEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 自动生成的环境ID
        :type EnvId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvId = None
        self._RequestId = None

    @property
    def EnvId(self):
        r"""自动生成的环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._RequestId = params.get("RequestId")


class CreateHostingDomainRequest(AbstractModel):
    r"""CreateHostingDomain请求参数结构体

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
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Domain(self):
        r"""域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        r"""证书ID
        :rtype: str
        """
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
    r"""CreateHostingDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateIndex(AbstractModel):
    r"""本类型用于UpdateTable接口中描述待创建索引信息

    """

    def __init__(self):
        r"""
        :param _IndexName: 索引名称
        :type IndexName: str
        :param _MgoKeySchema: 索引结构
        :type MgoKeySchema: :class:`tencentcloud.tcb.v20180608.models.MgoKeySchema`
        """
        self._IndexName = None
        self._MgoKeySchema = None

    @property
    def IndexName(self):
        r"""索引名称
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def MgoKeySchema(self):
        r"""索引结构
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MgoKeySchema`
        """
        return self._MgoKeySchema

    @MgoKeySchema.setter
    def MgoKeySchema(self, MgoKeySchema):
        self._MgoKeySchema = MgoKeySchema


    def _deserialize(self, params):
        self._IndexName = params.get("IndexName")
        if params.get("MgoKeySchema") is not None:
            self._MgoKeySchema = MgoKeySchema()
            self._MgoKeySchema._deserialize(params.get("MgoKeySchema"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMySQLRequest(AbstractModel):
    r"""CreateMySQL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _DbInstanceType: Db类型: MYSQL
        :type DbInstanceType: str
        :param _MysqlVersion: mysql版本
        :type MysqlVersion: str
        :param _VpcId: vpc Id
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _LowerCaseTableNames: 0 区分表名大小写；1 不区分表名大小写(默认)
        :type LowerCaseTableNames: str
        """
        self._EnvId = None
        self._DbInstanceType = None
        self._MysqlVersion = None
        self._VpcId = None
        self._SubnetId = None
        self._LowerCaseTableNames = None

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def DbInstanceType(self):
        r"""Db类型: MYSQL
        :rtype: str
        """
        return self._DbInstanceType

    @DbInstanceType.setter
    def DbInstanceType(self, DbInstanceType):
        self._DbInstanceType = DbInstanceType

    @property
    def MysqlVersion(self):
        r"""mysql版本
        :rtype: str
        """
        return self._MysqlVersion

    @MysqlVersion.setter
    def MysqlVersion(self, MysqlVersion):
        self._MysqlVersion = MysqlVersion

    @property
    def VpcId(self):
        r"""vpc Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def LowerCaseTableNames(self):
        r"""0 区分表名大小写；1 不区分表名大小写(默认)
        :rtype: str
        """
        return self._LowerCaseTableNames

    @LowerCaseTableNames.setter
    def LowerCaseTableNames(self, LowerCaseTableNames):
        self._LowerCaseTableNames = LowerCaseTableNames


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._DbInstanceType = params.get("DbInstanceType")
        self._MysqlVersion = params.get("MysqlVersion")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._LowerCaseTableNames = params.get("LowerCaseTableNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMySQLResponse(AbstractModel):
    r"""CreateMySQL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 开通结果
        :type Data: :class:`tencentcloud.tcb.v20180608.models.CreateMySQLResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""开通结果
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateMySQLResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateMySQLResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateMySQLResult(AbstractModel):
    r"""开通Mysql 结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStaticStoreRequest(AbstractModel):
    r"""CreateStaticStore请求参数结构体

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
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnableUnion(self):
        r"""是否启用统一域名
        :rtype: bool
        """
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
    r"""CreateStaticStore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建静态资源结果(succ/fail)
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""创建静态资源结果(succ/fail)
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateTableRequest(AbstractModel):
    r"""CreateTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TableName: 数据表名；长度不超过96个字符，可以为英文字母、数字、下划线(_)和短横线(-)的组合，且不能以下划线开头
        :type TableName: str
        :param _Tag: FlexDB实例ID，如：tnt-nl7hjzasw
        :type Tag: str
        :param _PermissionInfo: FlexDB数据库权限信息
        :type PermissionInfo: :class:`tencentcloud.tcb.v20180608.models.PermissionInfo`
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _MongoConnector: MongoDB连接器配置
        :type MongoConnector: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        self._TableName = None
        self._Tag = None
        self._PermissionInfo = None
        self._EnvId = None
        self._MongoConnector = None

    @property
    def TableName(self):
        r"""数据表名；长度不超过96个字符，可以为英文字母、数字、下划线(_)和短横线(-)的组合，且不能以下划线开头
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Tag(self):
        r"""FlexDB实例ID，如：tnt-nl7hjzasw
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def PermissionInfo(self):
        r"""FlexDB数据库权限信息
        :rtype: :class:`tencentcloud.tcb.v20180608.models.PermissionInfo`
        """
        return self._PermissionInfo

    @PermissionInfo.setter
    def PermissionInfo(self, PermissionInfo):
        self._PermissionInfo = PermissionInfo

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MongoConnector(self):
        r"""MongoDB连接器配置
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        return self._MongoConnector

    @MongoConnector.setter
    def MongoConnector(self, MongoConnector):
        self._MongoConnector = MongoConnector


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._Tag = params.get("Tag")
        if params.get("PermissionInfo") is not None:
            self._PermissionInfo = PermissionInfo()
            self._PermissionInfo._deserialize(params.get("PermissionInfo"))
        self._EnvId = params.get("EnvId")
        if params.get("MongoConnector") is not None:
            self._MongoConnector = MongoConnector()
            self._MongoConnector._deserialize(params.get("MongoConnector"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTableResponse(AbstractModel):
    r"""CreateTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    r"""CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _Name: 用户名，用户名规则：1. 长度1-64字符 2. 只能包含大小写英文字母、数字和符号 . _ - 3. 只能以字母或数字开头 4. 不能重复
        :type Name: str
        :param _Uid: 用户ID，最多64字符，如不传则系统自动生成
        :type Uid: str
        :param _Type: 用户类型：internalUser-内部用户、externalUser-外部用户，默认internalUser（内部用户）
        :type Type: str
        :param _Password: 密码，传入Uid时密码可不传。密码规则：1. 长度8-32字符（推荐12位以上） 2. 不能以特殊字符开头 3. 至少包含以下四项中的三项：小写字母a-z、大写字母A-Z、数字0-9、特殊字符()!@#$%^&*\|?><_-
        :type Password: str
        :param _UserStatus: 用户状态：ACTIVE（激活）、BLOCKED（冻结），默认激活
        :type UserStatus: str
        :param _NickName: 用户昵称，长度2-64字符
        :type NickName: str
        :param _Phone: 手机号，不能重复
        :type Phone: str
        :param _Email: 邮箱地址，不能重复
        :type Email: str
        :param _AvatarUrl: 头像链接，可访问的公网URL
        :type AvatarUrl: str
        :param _Description: 用户描述，最多200字符
        :type Description: str
        """
        self._EnvId = None
        self._Name = None
        self._Uid = None
        self._Type = None
        self._Password = None
        self._UserStatus = None
        self._NickName = None
        self._Phone = None
        self._Email = None
        self._AvatarUrl = None
        self._Description = None

    @property
    def EnvId(self):
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Name(self):
        r"""用户名，用户名规则：1. 长度1-64字符 2. 只能包含大小写英文字母、数字和符号 . _ - 3. 只能以字母或数字开头 4. 不能重复
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        r"""用户ID，最多64字符，如不传则系统自动生成
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Type(self):
        r"""用户类型：internalUser-内部用户、externalUser-外部用户，默认internalUser（内部用户）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Password(self):
        r"""密码，传入Uid时密码可不传。密码规则：1. 长度8-32字符（推荐12位以上） 2. 不能以特殊字符开头 3. 至少包含以下四项中的三项：小写字母a-z、大写字母A-Z、数字0-9、特殊字符()!@#$%^&*\|?><_-
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def UserStatus(self):
        r"""用户状态：ACTIVE（激活）、BLOCKED（冻结），默认激活
        :rtype: str
        """
        return self._UserStatus

    @UserStatus.setter
    def UserStatus(self, UserStatus):
        self._UserStatus = UserStatus

    @property
    def NickName(self):
        r"""用户昵称，长度2-64字符
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Phone(self):
        r"""手机号，不能重复
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""邮箱地址，不能重复
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def AvatarUrl(self):
        r"""头像链接，可访问的公网URL
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def Description(self):
        r"""用户描述，最多200字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._Type = params.get("Type")
        self._Password = params.get("Password")
        self._UserStatus = params.get("UserStatus")
        self._NickName = params.get("NickName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._AvatarUrl = params.get("AvatarUrl")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResp(AbstractModel):
    r"""创建用户返回结果

    """

    def __init__(self):
        r"""
        :param _Uid: 用户ID
        :type Uid: str
        """
        self._Uid = None

    @property
    def Uid(self):
        r"""用户ID
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid


    def _deserialize(self, params):
        self._Uid = params.get("Uid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    r"""CreateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果返回
        :type Data: :class:`tencentcloud.tcb.v20180608.models.CreateUserResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果返回
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateUserResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateUserResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DatabasesInfo(AbstractModel):
    r"""数据库资源信息

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
        :type UpdateTime: str
        """
        self._InstanceId = None
        self._Status = None
        self._Region = None
        self._UpdateTime = None

    @property
    def InstanceId(self):
        r"""数据库唯一标识
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        r"""状态。包含以下取值：
<li>INITIALIZING：资源初始化中</li>
<li>RUNNING：运行中，可正常使用的状态</li>
<li>UNUSABLE：禁用，不可用</li>
<li>OVERDUE：资源过期</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""所属地域。
当前支持ap-shanghai
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
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
        


class DbInstance(AbstractModel):
    r"""数据库连接器实例信息

    """

    def __init__(self):
        r"""
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _InstanceId: MySQL 连接器实例 ID；`"default"` 或为空表示使用 TCB 环境的默认连接器
        :type InstanceId: str
        :param _Schema: 数据库名；为空时使用连接器配置的默认数据库名
        :type Schema: str
        """
        self._EnvId = None
        self._InstanceId = None
        self._Schema = None

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def InstanceId(self):
        r"""MySQL 连接器实例 ID；`"default"` 或为空表示使用 TCB 环境的默认连接器
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Schema(self):
        r"""数据库名；为空时使用连接器配置的默认数据库名
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._InstanceId = params.get("InstanceId")
        self._Schema = params.get("Schema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuthDomainRequest(AbstractModel):
    r"""DeleteAuthDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 开发者的环境ID
        :type EnvId: str
        :param _DomainIds: 域名ID列表，支持批量
        :type DomainIds: list of str
        """
        self._EnvId = None
        self._DomainIds = None

    @property
    def EnvId(self):
        r"""开发者的环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def DomainIds(self):
        r"""域名ID列表，支持批量
        :rtype: list of str
        """
        return self._DomainIds

    @DomainIds.setter
    def DomainIds(self, DomainIds):
        self._DomainIds = DomainIds


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._DomainIds = params.get("DomainIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuthDomainResponse(AbstractModel):
    r"""DeleteAuthDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Deleted: 删除的域名个数
        :type Deleted: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Deleted = None
        self._RequestId = None

    @property
    def Deleted(self):
        r"""删除的域名个数
        :rtype: int
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Deleted = params.get("Deleted")
        self._RequestId = params.get("RequestId")


class DeleteCloudBaseGWAPIRequest(AbstractModel):
    r"""DeleteCloudBaseGWAPI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _Path: API Path
        :type Path: str
        :param _APIId: API ID
        :type APIId: str
        :param _Type: API类型
        :type Type: int
        :param _Name: API Name
        :type Name: str
        :param _Custom: 自定义值字段（Type为2时，传递容器服务名表示需要删除JNSGW）
        :type Custom: str
        :param _Domain: 域名
        :type Domain: str
        """
        self._ServiceId = None
        self._Path = None
        self._APIId = None
        self._Type = None
        self._Name = None
        self._Custom = None
        self._Domain = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Path(self):
        r"""API Path
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def APIId(self):
        r"""API ID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def Type(self):
        r"""API类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""API Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Custom(self):
        r"""自定义值字段（Type为2时，传递容器服务名表示需要删除JNSGW）
        :rtype: str
        """
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom

    @property
    def Domain(self):
        r"""域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Path = params.get("Path")
        self._APIId = params.get("APIId")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Custom = params.get("Custom")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudBaseGWAPIResponse(AbstractModel):
    r"""DeleteCloudBaseGWAPI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 最终删除API个数
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        r"""最终删除API个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DeleteCloudBaseGWDomainRequest(AbstractModel):
    r"""DeleteCloudBaseGWDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _Domain: 服务域名
        :type Domain: str
        """
        self._ServiceId = None
        self._Domain = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Domain(self):
        r"""服务域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudBaseGWDomainResponse(AbstractModel):
    r"""DeleteCloudBaseGWDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 删除个数
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        r"""删除个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DeleteTableRequest(AbstractModel):
    r"""DeleteTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TableName: 待删除的表名
        :type TableName: str
        :param _Tag: FlexDB实例ID
        :type Tag: str
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _MongoConnector: MongoDB连接器配置
        :type MongoConnector: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        self._TableName = None
        self._Tag = None
        self._EnvId = None
        self._MongoConnector = None

    @property
    def TableName(self):
        r"""待删除的表名
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Tag(self):
        r"""FlexDB实例ID
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MongoConnector(self):
        r"""MongoDB连接器配置
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        return self._MongoConnector

    @MongoConnector.setter
    def MongoConnector(self, MongoConnector):
        self._MongoConnector = MongoConnector


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._Tag = params.get("Tag")
        self._EnvId = params.get("EnvId")
        if params.get("MongoConnector") is not None:
            self._MongoConnector = MongoConnector()
            self._MongoConnector._deserialize(params.get("MongoConnector"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableResponse(AbstractModel):
    r"""DeleteTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteUsersRequest(AbstractModel):
    r"""DeleteUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _Uids: tcb用户id列表, 一次最多支持删除100个
        :type Uids: list of str
        """
        self._EnvId = None
        self._Uids = None

    @property
    def EnvId(self):
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Uids(self):
        r"""tcb用户id列表, 一次最多支持删除100个
        :rtype: list of str
        """
        return self._Uids

    @Uids.setter
    def Uids(self, Uids):
        self._Uids = Uids


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Uids = params.get("Uids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersResp(AbstractModel):
    r"""删除tcb用户返回值

    """

    def __init__(self):
        r"""
        :param _SuccessCount: 成功个数
        :type SuccessCount: int
        :param _FailedCount: 失败个数
        :type FailedCount: int
        """
        self._SuccessCount = None
        self._FailedCount = None

    @property
    def SuccessCount(self):
        r"""成功个数
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailedCount(self):
        r"""失败个数
        :rtype: int
        """
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount


    def _deserialize(self, params):
        self._SuccessCount = params.get("SuccessCount")
        self._FailedCount = params.get("FailedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersResponse(AbstractModel):
    r"""DeleteUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 删除用户结果
        :type Data: :class:`tencentcloud.tcb.v20180608.models.DeleteUsersResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""删除用户结果
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteUsersResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DeleteUsersResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAuthDomainsRequest(AbstractModel):
    r"""DescribeAuthDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
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
    r"""DescribeAuthDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domains: 安全域名列表
        :type Domains: list of AuthDomain
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domains = None
        self._RequestId = None

    @property
    def Domains(self):
        r"""安全域名列表
        :rtype: list of AuthDomain
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""DescribeBaasPackageList请求参数结构体

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
        r"""tcb产品套餐ID，不填拉取全量package信息。
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Source(self):
        r"""套餐归属方，填写后只返回对应的套餐 包含miniapp与qcloud两种 默认为miniapp
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def EnvChannel(self):
        r"""套餐归属环境渠道
        :rtype: str
        """
        return self._EnvChannel

    @EnvChannel.setter
    def EnvChannel(self, EnvChannel):
        self._EnvChannel = EnvChannel

    @property
    def TargetAction(self):
        r"""拉取套餐用途：
1）new 新购
2）modify变配
3）renew续费
        :rtype: str
        """
        return self._TargetAction

    @TargetAction.setter
    def TargetAction(self, TargetAction):
        self._TargetAction = TargetAction

    @property
    def GroupName(self):
        r"""预留字段，同一商品会对应多个类型套餐，对指标有不同侧重。
计算型calculation
流量型flux
容量型capactiy
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def PackageTypeList(self):
        r"""类型分组过滤。默认为["default"]
        :rtype: list of str
        """
        return self._PackageTypeList

    @PackageTypeList.setter
    def PackageTypeList(self, PackageTypeList):
        self._PackageTypeList = PackageTypeList

    @property
    def PaymentChannel(self):
        r"""付费渠道，与回包billTags中的计费参数相关，不填返回默认值。
        :rtype: str
        """
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
    r"""DescribeBaasPackageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageList: 套餐列表
        :type PackageList: list of BaasPackageInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PackageList = None
        self._RequestId = None

    @property
    def PackageList(self):
        r"""套餐列表
        :rtype: list of BaasPackageInfo
        """
        return self._PackageList

    @PackageList.setter
    def PackageList(self, PackageList):
        self._PackageList = PackageList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeCloudBaseBuildServiceRequest(AbstractModel):
    r"""DescribeCloudBaseBuildService请求参数结构体

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
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ServiceName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def CIBusiness(self):
        r"""build类型,枚举值有: cloudbaserun, framework-ci
        :rtype: str
        """
        return self._CIBusiness

    @CIBusiness.setter
    def CIBusiness(self, CIBusiness):
        self._CIBusiness = CIBusiness

    @property
    def ServiceVersion(self):
        r"""服务版本
        :rtype: str
        """
        return self._ServiceVersion

    @ServiceVersion.setter
    def ServiceVersion(self, ServiceVersion):
        self._ServiceVersion = ServiceVersion

    @property
    def Suffix(self):
        r"""文件后缀
        :rtype: str
        """
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
    r"""DescribeCloudBaseBuildService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UploadUrl: 上传url
        :type UploadUrl: str
        :param _UploadHeaders: 上传header
        :type UploadHeaders: list of KVPair
        :param _PackageName: 包名
        :type PackageName: str
        :param _PackageVersion: 包版本
        :type PackageVersion: str
        :param _DownloadUrl: 下载链接
        :type DownloadUrl: str
        :param _DownloadHeaders: 下载Httpheader
        :type DownloadHeaders: list of KVPair
        :param _OutDate: 下载链接是否过期
        :type OutDate: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        r"""上传url
        :rtype: str
        """
        return self._UploadUrl

    @UploadUrl.setter
    def UploadUrl(self, UploadUrl):
        self._UploadUrl = UploadUrl

    @property
    def UploadHeaders(self):
        r"""上传header
        :rtype: list of KVPair
        """
        return self._UploadHeaders

    @UploadHeaders.setter
    def UploadHeaders(self, UploadHeaders):
        self._UploadHeaders = UploadHeaders

    @property
    def PackageName(self):
        r"""包名
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def PackageVersion(self):
        r"""包版本
        :rtype: str
        """
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion

    @property
    def DownloadUrl(self):
        r"""下载链接
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def DownloadHeaders(self):
        r"""下载Httpheader
        :rtype: list of KVPair
        """
        return self._DownloadHeaders

    @DownloadHeaders.setter
    def DownloadHeaders(self, DownloadHeaders):
        self._DownloadHeaders = DownloadHeaders

    @property
    def OutDate(self):
        r"""下载链接是否过期
        :rtype: bool
        """
        return self._OutDate

    @OutDate.setter
    def OutDate(self, OutDate):
        self._OutDate = OutDate

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeCloudBaseGWAPIRequest(AbstractModel):
    r"""DescribeCloudBaseGWAPI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _Domain: API域名
        :type Domain: str
        :param _Path: API Path
        :type Path: str
        :param _APIId: API ID
        :type APIId: str
        :param _Type: API类型，1为云函数，2为容器
        :type Type: int
        :param _Name: API名，Type为1时为云函数名，Type为2时为容器服务名
        :type Name: str
        :param _Offset: 查询的分页参数，用于设置查询的偏移位置，0表示从头开始
        :type Offset: int
        :param _Limit: 查询的分页参数，用于表示每次查询的最大返回数据量
        :type Limit: int
        :param _EnableRegion: 是否启用多地域
        :type EnableRegion: bool
        :param _EnableUnion: 是否使用统一域名
        :type EnableUnion: bool
        """
        self._ServiceId = None
        self._Domain = None
        self._Path = None
        self._APIId = None
        self._Type = None
        self._Name = None
        self._Offset = None
        self._Limit = None
        self._EnableRegion = None
        self._EnableUnion = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Domain(self):
        r"""API域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Path(self):
        r"""API Path
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def APIId(self):
        r"""API ID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def Type(self):
        r"""API类型，1为云函数，2为容器
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""API名，Type为1时为云函数名，Type为2时为容器服务名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Offset(self):
        r"""查询的分页参数，用于设置查询的偏移位置，0表示从头开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询的分页参数，用于表示每次查询的最大返回数据量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EnableRegion(self):
        r"""是否启用多地域
        :rtype: bool
        """
        return self._EnableRegion

    @EnableRegion.setter
    def EnableRegion(self, EnableRegion):
        self._EnableRegion = EnableRegion

    @property
    def EnableUnion(self):
        r"""是否使用统一域名
        :rtype: bool
        """
        return self._EnableUnion

    @EnableUnion.setter
    def EnableUnion(self, EnableUnion):
        self._EnableUnion = EnableUnion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Domain = params.get("Domain")
        self._Path = params.get("Path")
        self._APIId = params.get("APIId")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EnableRegion = params.get("EnableRegion")
        self._EnableUnion = params.get("EnableUnion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseGWAPIResponse(AbstractModel):
    r"""DescribeCloudBaseGWAPI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _APISet: API列表
注意：此字段可能返回 null，表示取不到有效值。
        :type APISet: list of CloudBaseGWAPI
        :param _EnableService: 是否开启http调用
        :type EnableService: bool
        :param _Total: 查询结果的数据总量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Offset: 查询的分页参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param _Limit: 查询的分页参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._APISet = None
        self._EnableService = None
        self._Total = None
        self._Offset = None
        self._Limit = None
        self._RequestId = None

    @property
    def APISet(self):
        r"""API列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CloudBaseGWAPI
        """
        return self._APISet

    @APISet.setter
    def APISet(self, APISet):
        self._APISet = APISet

    @property
    def EnableService(self):
        r"""是否开启http调用
        :rtype: bool
        """
        return self._EnableService

    @EnableService.setter
    def EnableService(self, EnableService):
        self._EnableService = EnableService

    @property
    def Total(self):
        r"""查询结果的数据总量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Offset(self):
        r"""查询的分页参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询的分页参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("APISet") is not None:
            self._APISet = []
            for item in params.get("APISet"):
                obj = CloudBaseGWAPI()
                obj._deserialize(item)
                self._APISet.append(obj)
        self._EnableService = params.get("EnableService")
        self._Total = params.get("Total")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._RequestId = params.get("RequestId")


class DescribeCloudBaseGWServiceRequest(AbstractModel):
    r"""DescribeCloudBaseGWService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _Domain: 服务域名
        :type Domain: str
        :param _EnableRegion: 是否启用多地域
        :type EnableRegion: bool
        :param _EnableUnion: 是否启用统一域名
        :type EnableUnion: bool
        """
        self._ServiceId = None
        self._Domain = None
        self._EnableRegion = None
        self._EnableUnion = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Domain(self):
        r"""服务域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def EnableRegion(self):
        r"""是否启用多地域
        :rtype: bool
        """
        return self._EnableRegion

    @EnableRegion.setter
    def EnableRegion(self, EnableRegion):
        self._EnableRegion = EnableRegion

    @property
    def EnableUnion(self):
        r"""是否启用统一域名
        :rtype: bool
        """
        return self._EnableUnion

    @EnableUnion.setter
    def EnableUnion(self, EnableUnion):
        self._EnableUnion = EnableUnion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Domain = params.get("Domain")
        self._EnableRegion = params.get("EnableRegion")
        self._EnableUnion = params.get("EnableUnion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudBaseGWServiceResponse(AbstractModel):
    r"""DescribeCloudBaseGWService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceSet: 服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceSet: list of CloudBaseGWService
        :param _EnableService: 是否开启服务
        :type EnableService: bool
        :param _DefaultDomain: 默认域名信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultDomain: str
        :param _EnableUnion: 是否开启CDN迁移
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableUnion: bool
        :param _EnableCheckAcrossDomain: 是否开启跨域校验，默认开启 true
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableCheckAcrossDomain: bool
        :param _CustomRoutingRules: 自定义路由规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomRoutingRules: str
        :param _AccessFlag: 默认域名绑定类型，1绑定TCB-CDN，2绑定tcbingres（不经过cdn）
        :type AccessFlag: int
        :param _OriginDomain: 云接入源站域名
        :type OriginDomain: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceSet = None
        self._EnableService = None
        self._DefaultDomain = None
        self._EnableUnion = None
        self._EnableCheckAcrossDomain = None
        self._CustomRoutingRules = None
        self._AccessFlag = None
        self._OriginDomain = None
        self._RequestId = None

    @property
    def ServiceSet(self):
        r"""服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CloudBaseGWService
        """
        return self._ServiceSet

    @ServiceSet.setter
    def ServiceSet(self, ServiceSet):
        self._ServiceSet = ServiceSet

    @property
    def EnableService(self):
        r"""是否开启服务
        :rtype: bool
        """
        return self._EnableService

    @EnableService.setter
    def EnableService(self, EnableService):
        self._EnableService = EnableService

    @property
    def DefaultDomain(self):
        r"""默认域名信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DefaultDomain

    @DefaultDomain.setter
    def DefaultDomain(self, DefaultDomain):
        self._DefaultDomain = DefaultDomain

    @property
    def EnableUnion(self):
        r"""是否开启CDN迁移
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableUnion

    @EnableUnion.setter
    def EnableUnion(self, EnableUnion):
        self._EnableUnion = EnableUnion

    @property
    def EnableCheckAcrossDomain(self):
        r"""是否开启跨域校验，默认开启 true
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableCheckAcrossDomain

    @EnableCheckAcrossDomain.setter
    def EnableCheckAcrossDomain(self, EnableCheckAcrossDomain):
        self._EnableCheckAcrossDomain = EnableCheckAcrossDomain

    @property
    def CustomRoutingRules(self):
        r"""自定义路由规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CustomRoutingRules

    @CustomRoutingRules.setter
    def CustomRoutingRules(self, CustomRoutingRules):
        self._CustomRoutingRules = CustomRoutingRules

    @property
    def AccessFlag(self):
        r"""默认域名绑定类型，1绑定TCB-CDN，2绑定tcbingres（不经过cdn）
        :rtype: int
        """
        return self._AccessFlag

    @AccessFlag.setter
    def AccessFlag(self, AccessFlag):
        self._AccessFlag = AccessFlag

    @property
    def OriginDomain(self):
        r"""云接入源站域名
        :rtype: str
        """
        return self._OriginDomain

    @OriginDomain.setter
    def OriginDomain(self, OriginDomain):
        self._OriginDomain = OriginDomain

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceSet") is not None:
            self._ServiceSet = []
            for item in params.get("ServiceSet"):
                obj = CloudBaseGWService()
                obj._deserialize(item)
                self._ServiceSet.append(obj)
        self._EnableService = params.get("EnableService")
        self._DefaultDomain = params.get("DefaultDomain")
        self._EnableUnion = params.get("EnableUnion")
        self._EnableCheckAcrossDomain = params.get("EnableCheckAcrossDomain")
        self._CustomRoutingRules = params.get("CustomRoutingRules")
        self._AccessFlag = params.get("AccessFlag")
        self._OriginDomain = params.get("OriginDomain")
        self._RequestId = params.get("RequestId")


class DescribeCreateMySQLResult(AbstractModel):
    r"""查询开通Mysql结果

    """

    def __init__(self):
        r"""
        :param _Status: 状态 notexist | init | doing | success | fail
        :type Status: str
        :param _FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param _FreezeStatus: 是否已被冻结（只在 Status=success时有效）
        :type FreezeStatus: bool
        """
        self._Status = None
        self._FailReason = None
        self._FreezeStatus = None

    @property
    def Status(self):
        r"""状态 notexist | init | doing | success | fail
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailReason(self):
        r"""失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def FreezeStatus(self):
        r"""是否已被冻结（只在 Status=success时有效）
        :rtype: bool
        """
        return self._FreezeStatus

    @FreezeStatus.setter
    def FreezeStatus(self, FreezeStatus):
        self._FreezeStatus = FreezeStatus


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FailReason = params.get("FailReason")
        self._FreezeStatus = params.get("FreezeStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCreateMySQLResultRequest(AbstractModel):
    r"""DescribeCreateMySQLResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _TaskId: OpenMysql 返回任务 Id
        :type TaskId: str
        """
        self._EnvId = None
        self._TaskId = None

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TaskId(self):
        r"""OpenMysql 返回任务 Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCreateMySQLResultResponse(AbstractModel):
    r"""DescribeCreateMySQLResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询开通结果
        :type Data: :class:`tencentcloud.tcb.v20180608.models.DescribeCreateMySQLResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""查询开通结果
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCreateMySQLResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeCreateMySQLResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDatabaseACLRequest(AbstractModel):
    r"""DescribeDatabaseACL请求参数结构体

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
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionName(self):
        r"""集合名称
        :rtype: str
        """
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
    r"""DescribeDatabaseACL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AclTag: 权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
        :type AclTag: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AclTag = None
        self._RequestId = None

    @property
    def AclTag(self):
        r"""权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
        :rtype: str
        """
        return self._AclTag

    @AclTag.setter
    def AclTag(self, AclTag):
        self._AclTag = AclTag

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AclTag = params.get("AclTag")
        self._RequestId = params.get("RequestId")


class DescribeEnvAccountCircleRequest(AbstractModel):
    r"""DescribeEnvAccountCircle请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
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
        


class DescribeEnvAccountCircleResponse(AbstractModel):
    r"""DescribeEnvAccountCircle返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 环境计费周期开始时间
        :type StartTime: str
        :param _EndTime: 环境计费周期结束时间
        :type EndTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._RequestId = None

    @property
    def StartTime(self):
        r"""环境计费周期开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""环境计费周期结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeEnvLimitRequest(AbstractModel):
    r"""DescribeEnvLimit请求参数结构体

    """


class DescribeEnvLimitResponse(AbstractModel):
    r"""DescribeEnvLimit返回参数结构体

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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        r"""环境总数上限
        :rtype: int
        """
        return self._MaxEnvNum

    @MaxEnvNum.setter
    def MaxEnvNum(self, MaxEnvNum):
        self._MaxEnvNum = MaxEnvNum

    @property
    def CurrentEnvNum(self):
        r"""目前环境总数
        :rtype: int
        """
        return self._CurrentEnvNum

    @CurrentEnvNum.setter
    def CurrentEnvNum(self, CurrentEnvNum):
        self._CurrentEnvNum = CurrentEnvNum

    @property
    def MaxFreeEnvNum(self):
        r"""免费环境数量上限
        :rtype: int
        """
        return self._MaxFreeEnvNum

    @MaxFreeEnvNum.setter
    def MaxFreeEnvNum(self, MaxFreeEnvNum):
        self._MaxFreeEnvNum = MaxFreeEnvNum

    @property
    def CurrentFreeEnvNum(self):
        r"""目前免费环境数量
        :rtype: int
        """
        return self._CurrentFreeEnvNum

    @CurrentFreeEnvNum.setter
    def CurrentFreeEnvNum(self, CurrentFreeEnvNum):
        self._CurrentFreeEnvNum = CurrentFreeEnvNum

    @property
    def MaxDeleteTotal(self):
        r"""总计允许销毁环境次数上限
        :rtype: int
        """
        return self._MaxDeleteTotal

    @MaxDeleteTotal.setter
    def MaxDeleteTotal(self, MaxDeleteTotal):
        self._MaxDeleteTotal = MaxDeleteTotal

    @property
    def CurrentDeleteTotal(self):
        r"""目前已销毁环境次数
        :rtype: int
        """
        return self._CurrentDeleteTotal

    @CurrentDeleteTotal.setter
    def CurrentDeleteTotal(self, CurrentDeleteTotal):
        self._CurrentDeleteTotal = CurrentDeleteTotal

    @property
    def MaxDeleteMonthly(self):
        r"""每月允许销毁环境次数上限
        :rtype: int
        """
        return self._MaxDeleteMonthly

    @MaxDeleteMonthly.setter
    def MaxDeleteMonthly(self, MaxDeleteMonthly):
        self._MaxDeleteMonthly = MaxDeleteMonthly

    @property
    def CurrentDeleteMonthly(self):
        r"""本月已销毁环境次数
        :rtype: int
        """
        return self._CurrentDeleteMonthly

    @CurrentDeleteMonthly.setter
    def CurrentDeleteMonthly(self, CurrentDeleteMonthly):
        self._CurrentDeleteMonthly = CurrentDeleteMonthly

    @property
    def MaxFreeTrialNum(self):
        r"""微信网关体验版可购买月份数
        :rtype: int
        """
        return self._MaxFreeTrialNum

    @MaxFreeTrialNum.setter
    def MaxFreeTrialNum(self, MaxFreeTrialNum):
        self._MaxFreeTrialNum = MaxFreeTrialNum

    @property
    def CurrentFreeTrialNum(self):
        r"""微信网关体验版已购买月份数
        :rtype: int
        """
        return self._CurrentFreeTrialNum

    @CurrentFreeTrialNum.setter
    def CurrentFreeTrialNum(self, CurrentFreeTrialNum):
        self._CurrentFreeTrialNum = CurrentFreeTrialNum

    @property
    def ChangePayTotal(self):
        r"""转支付限额总数
        :rtype: int
        """
        return self._ChangePayTotal

    @ChangePayTotal.setter
    def ChangePayTotal(self, ChangePayTotal):
        self._ChangePayTotal = ChangePayTotal

    @property
    def CurrentChangePayTotal(self):
        r"""当前已用转支付次数
        :rtype: int
        """
        return self._CurrentChangePayTotal

    @CurrentChangePayTotal.setter
    def CurrentChangePayTotal(self, CurrentChangePayTotal):
        self._CurrentChangePayTotal = CurrentChangePayTotal

    @property
    def ChangePayMonthly(self):
        r"""转支付每月限额
        :rtype: int
        """
        return self._ChangePayMonthly

    @ChangePayMonthly.setter
    def ChangePayMonthly(self, ChangePayMonthly):
        self._ChangePayMonthly = ChangePayMonthly

    @property
    def CurrentChangePayMonthly(self):
        r"""本月已用转支付额度
        :rtype: int
        """
        return self._CurrentChangePayMonthly

    @CurrentChangePayMonthly.setter
    def CurrentChangePayMonthly(self, CurrentChangePayMonthly):
        self._CurrentChangePayMonthly = CurrentChangePayMonthly

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeEnvsRequest(AbstractModel):
    r"""DescribeEnvs请求参数结构体

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
        :param _Limit: 分页参数，单页限制个数
        :type Limit: int
        :param _Offset: 分页参数，偏移量
        :type Offset: int
        """
        self._EnvId = None
        self._IsVisible = None
        self._Channels = None
        self._Limit = None
        self._Offset = None

    @property
    def EnvId(self):
        r"""环境ID，如果传了这个参数则只返回该环境的相关信息
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def IsVisible(self):
        r"""指定Channels字段为可见渠道列表或不可见渠道列表
如只想获取渠道A的环境 就填写IsVisible= true,Channels = ["A"], 过滤渠道A拉取其他渠道环境时填写IsVisible= false,Channels = ["A"]
        :rtype: bool
        """
        return self._IsVisible

    @IsVisible.setter
    def IsVisible(self, IsVisible):
        self._IsVisible = IsVisible

    @property
    def Channels(self):
        r"""渠道列表，代表可见或不可见渠道由IsVisible参数指定
        :rtype: list of str
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def Limit(self):
        r"""分页参数，单页限制个数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页参数，偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._IsVisible = params.get("IsVisible")
        self._Channels = params.get("Channels")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvsResponse(AbstractModel):
    r"""DescribeEnvs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvList: 环境信息列表
        :type EnvList: list of EnvInfo
        :param _Total: 环境个数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvList = None
        self._Total = None
        self._RequestId = None

    @property
    def EnvList(self):
        r"""环境信息列表
        :rtype: list of EnvInfo
        """
        return self._EnvList

    @EnvList.setter
    def EnvList(self, EnvList):
        self._EnvList = EnvList

    @property
    def Total(self):
        r"""环境个数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeHostingDomainTaskRequest(AbstractModel):
    r"""DescribeHostingDomainTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
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
    r"""DescribeHostingDomainTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: todo/doing/done/error
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""todo/doing/done/error
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeMySQLClusterDetailRequest(AbstractModel):
    r"""DescribeMySQLClusterDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
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
        


class DescribeMySQLClusterDetailResponse(AbstractModel):
    r"""DescribeMySQLClusterDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 集群详情
        :type Data: :class:`tencentcloud.tcb.v20180608.models.MySQLClusterDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""集群详情
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MySQLClusterDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = MySQLClusterDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMySQLTaskStatusRequest(AbstractModel):
    r"""DescribeMySQLTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _TaskName: 任务名
        :type TaskName: str
        """
        self._EnvId = None
        self._TaskId = None
        self._TaskName = None

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMySQLTaskStatusResponse(AbstractModel):
    r"""DescribeMySQLTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务状态
        :type Data: :class:`tencentcloud.tcb.v20180608.models.MySQLTaskStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""任务状态
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MySQLTaskStatus`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = MySQLTaskStatus()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeQuotaDataRequest(AbstractModel):
    r"""DescribeQuotaData请求参数结构体

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
<li> CynosdbCcupkg: 当月微信云托管MySQL CCU使用量，单位个  （需要除以1000）</li>
<li> CynosdbStoragepkg: 当月微信云托管MySQL 存储使用量，单位MB  （需要除以1000）</li>
<li> CynosdbCcupkgDay: 当天微信云托管MySQL 存储使用量，单位个 （需要除以1000） </li>
<li> CynosdbStoragepkgDay: 当天微信云托管MySQL 存储使用量，单位MB （需要除以1000） </li>
        :type MetricName: str
        :param _ResourceID: 资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocationpkg, FunctionGBspkg, FunctionFluxpkg)、容器托管（服务名称）。如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传。
        :type ResourceID: str
        """
        self._EnvId = None
        self._MetricName = None
        self._ResourceID = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MetricName(self):
        r"""<li> 指标名: </li>
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
<li> CynosdbCcupkg: 当月微信云托管MySQL CCU使用量，单位个  （需要除以1000）</li>
<li> CynosdbStoragepkg: 当月微信云托管MySQL 存储使用量，单位MB  （需要除以1000）</li>
<li> CynosdbCcupkgDay: 当天微信云托管MySQL 存储使用量，单位个 （需要除以1000） </li>
<li> CynosdbStoragepkgDay: 当天微信云托管MySQL 存储使用量，单位MB （需要除以1000） </li>
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def ResourceID(self):
        r"""资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocationpkg, FunctionGBspkg, FunctionFluxpkg)、容器托管（服务名称）。如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传。
        :rtype: str
        """
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
    r"""DescribeQuotaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Value: 指标的值
        :type Value: int
        :param _SubValue: 指标的附加值信息
        :type SubValue: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricName = None
        self._Value = None
        self._SubValue = None
        self._RequestId = None

    @property
    def MetricName(self):
        r"""指标名
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Value(self):
        r"""指标的值
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def SubValue(self):
        r"""指标的附加值信息
        :rtype: str
        """
        return self._SubValue

    @SubValue.setter
    def SubValue(self, SubValue):
        self._SubValue = SubValue

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._Value = params.get("Value")
        self._SubValue = params.get("SubValue")
        self._RequestId = params.get("RequestId")


class DescribeSafeRuleRequest(AbstractModel):
    r"""DescribeSafeRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _CollectionName: 集合名称
        :type CollectionName: str
        :param _WxAppId: 微信AppId，微信必传
        :type WxAppId: str
        """
        self._EnvId = None
        self._CollectionName = None
        self._WxAppId = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionName(self):
        r"""集合名称
        :rtype: str
        """
        return self._CollectionName

    @CollectionName.setter
    def CollectionName(self, CollectionName):
        self._CollectionName = CollectionName

    @property
    def WxAppId(self):
        r"""微信AppId，微信必传
        :rtype: str
        """
        return self._WxAppId

    @WxAppId.setter
    def WxAppId(self, WxAppId):
        self._WxAppId = WxAppId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CollectionName = params.get("CollectionName")
        self._WxAppId = params.get("WxAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSafeRuleResponse(AbstractModel):
    r"""DescribeSafeRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rule: 规则内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Rule: str
        :param _AclTag: 权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
<li> CUSTOM：自定义安全规则</li>
        :type AclTag: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rule = None
        self._AclTag = None
        self._RequestId = None

    @property
    def Rule(self):
        r"""规则内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def AclTag(self):
        r"""权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
<li> CUSTOM：自定义安全规则</li>
        :rtype: str
        """
        return self._AclTag

    @AclTag.setter
    def AclTag(self, AclTag):
        self._AclTag = AclTag

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Rule = params.get("Rule")
        self._AclTag = params.get("AclTag")
        self._RequestId = params.get("RequestId")


class DescribeStaticStoreRequest(AbstractModel):
    r"""DescribeStaticStore请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
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
        


class DescribeStaticStoreResponse(AbstractModel):
    r"""DescribeStaticStore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 静态托管资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of StaticStoreInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""静态托管资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StaticStoreInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = StaticStoreInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTableRequest(AbstractModel):
    r"""DescribeTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TableName: 表名
        :type TableName: str
        :param _Tag: FlecDB实例ID
        :type Tag: str
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _MongoConnector: MongoDB连接器配置
        :type MongoConnector: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        self._TableName = None
        self._Tag = None
        self._EnvId = None
        self._MongoConnector = None

    @property
    def TableName(self):
        r"""表名
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Tag(self):
        r"""FlecDB实例ID
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MongoConnector(self):
        r"""MongoDB连接器配置
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        return self._MongoConnector

    @MongoConnector.setter
    def MongoConnector(self, MongoConnector):
        self._MongoConnector = MongoConnector


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._Tag = params.get("Tag")
        self._EnvId = params.get("EnvId")
        if params.get("MongoConnector") is not None:
            self._MongoConnector = MongoConnector()
            self._MongoConnector._deserialize(params.get("MongoConnector"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableResponse(AbstractModel):
    r"""DescribeTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Indexes: 索引相关信息
        :type Indexes: list of IndexInfo
        :param _IndexNum: 索引个数
        :type IndexNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Indexes = None
        self._IndexNum = None
        self._RequestId = None

    @property
    def Indexes(self):
        r"""索引相关信息
        :rtype: list of IndexInfo
        """
        return self._Indexes

    @Indexes.setter
    def Indexes(self, Indexes):
        self._Indexes = Indexes

    @property
    def IndexNum(self):
        r"""索引个数
        :rtype: int
        """
        return self._IndexNum

    @IndexNum.setter
    def IndexNum(self, IndexNum):
        self._IndexNum = IndexNum

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Indexes") is not None:
            self._Indexes = []
            for item in params.get("Indexes"):
                obj = IndexInfo()
                obj._deserialize(item)
                self._Indexes.append(obj)
        self._IndexNum = params.get("IndexNum")
        self._RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    r"""DescribeTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MgoLimit: 分页条件
        :type MgoLimit: int
        :param _Tag: 实例ID
        :type Tag: str
        :param _MgoOffset: 分页条件
        :type MgoOffset: int
        :param _EnvId: 环境id
        :type EnvId: str
        :param _MongoConnector: MongoConnector
        :type MongoConnector: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        :param _TableNames: 指定表名过滤，为空时返回所有表
        :type TableNames: list of str
        """
        self._MgoLimit = None
        self._Tag = None
        self._MgoOffset = None
        self._EnvId = None
        self._MongoConnector = None
        self._TableNames = None

    @property
    def MgoLimit(self):
        r"""分页条件
        :rtype: int
        """
        return self._MgoLimit

    @MgoLimit.setter
    def MgoLimit(self, MgoLimit):
        self._MgoLimit = MgoLimit

    @property
    def Tag(self):
        r"""实例ID
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def MgoOffset(self):
        r"""分页条件
        :rtype: int
        """
        return self._MgoOffset

    @MgoOffset.setter
    def MgoOffset(self, MgoOffset):
        self._MgoOffset = MgoOffset

    @property
    def EnvId(self):
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MongoConnector(self):
        r"""MongoConnector
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        return self._MongoConnector

    @MongoConnector.setter
    def MongoConnector(self, MongoConnector):
        self._MongoConnector = MongoConnector

    @property
    def TableNames(self):
        r"""指定表名过滤，为空时返回所有表
        :rtype: list of str
        """
        return self._TableNames

    @TableNames.setter
    def TableNames(self, TableNames):
        self._TableNames = TableNames


    def _deserialize(self, params):
        self._MgoLimit = params.get("MgoLimit")
        self._Tag = params.get("Tag")
        self._MgoOffset = params.get("MgoOffset")
        self._EnvId = params.get("EnvId")
        if params.get("MongoConnector") is not None:
            self._MongoConnector = MongoConnector()
            self._MongoConnector._deserialize(params.get("MongoConnector"))
        self._TableNames = params.get("TableNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesResponse(AbstractModel):
    r"""DescribeTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tables: 表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of TableInfo
        :param _Pager: 分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Pager: :class:`tencentcloud.tcb.v20180608.models.Pager`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tables = None
        self._Pager = None
        self._RequestId = None

    @property
    def Tables(self):
        r"""表信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TableInfo
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def Pager(self):
        r"""分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcb.v20180608.models.Pager`
        """
        return self._Pager

    @Pager.setter
    def Pager(self, Pager):
        self._Pager = Pager

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = TableInfo()
                obj._deserialize(item)
                self._Tables.append(obj)
        if params.get("Pager") is not None:
            self._Pager = Pager()
            self._Pager._deserialize(params.get("Pager"))
        self._RequestId = params.get("RequestId")


class DescribeUserListRequest(AbstractModel):
    r"""DescribeUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _PageNo: 页码，从1开始，默认1
        :type PageNo: int
        :param _PageSize: 每页数量，默认20，最大100
        :type PageSize: int
        :param _Name: 用户名，模糊查询
        :type Name: str
        :param _NickName: 用户昵称，模糊查询
        :type NickName: str
        :param _Phone: 手机号，模糊查询
        :type Phone: str
        :param _Email: 邮箱，模糊查询
        :type Email: str
        """
        self._EnvId = None
        self._PageNo = None
        self._PageSize = None
        self._Name = None
        self._NickName = None
        self._Phone = None
        self._Email = None

    @property
    def EnvId(self):
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def PageNo(self):
        r"""页码，从1开始，默认1
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        r"""每页数量，默认20，最大100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Name(self):
        r"""用户名，模糊查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NickName(self):
        r"""用户昵称，模糊查询
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Phone(self):
        r"""手机号，模糊查询
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""邮箱，模糊查询
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Name = params.get("Name")
        self._NickName = params.get("NickName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListResp(AbstractModel):
    r"""查询用户返回结果

    """

    def __init__(self):
        r"""
        :param _Total: 用户总数
        :type Total: int
        :param _UserList: 用户列表
        :type UserList: list of User
        """
        self._Total = None
        self._UserList = None

    @property
    def Total(self):
        r"""用户总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserList(self):
        r"""用户列表
        :rtype: list of User
        """
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = User()
                obj._deserialize(item)
                self._UserList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListResponse(AbstractModel):
    r"""DescribeUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果返回
        :type Data: :class:`tencentcloud.tcb.v20180608.models.DescribeUserListResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果返回
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeUserListResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeUserListResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DestroyEnvRequest(AbstractModel):
    r"""DestroyEnv请求参数结构体

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
        r"""环境Id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def IsForce(self):
        r"""针对预付费 删除隔离中的环境时要传true 正常环境直接跳过隔离期删除
        :rtype: bool
        """
        return self._IsForce

    @IsForce.setter
    def IsForce(self, IsForce):
        self._IsForce = IsForce

    @property
    def BypassCheck(self):
        r"""是否绕过资源检查，资源包等额外资源，默认为false，如果为true，则不检查资源是否有数据，直接删除。
        :rtype: bool
        """
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
    r"""DestroyEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DestroyMySQLRequest(AbstractModel):
    r"""DestroyMySQL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
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
        


class DestroyMySQLResponse(AbstractModel):
    r"""DestroyMySQL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 销毁结果
        :type Data: :class:`tencentcloud.tcb.v20180608.models.DestroyMySQLResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""销毁结果
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DestroyMySQLResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DestroyMySQLResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DestroyMySQLResult(AbstractModel):
    r"""销毁 Mysql 结果

    """

    def __init__(self):
        r"""
        :param _IsSuccess: 是否成功
        :type IsSuccess: bool
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskName: 任务名
        :type TaskName: str
        """
        self._IsSuccess = None
        self._TaskId = None
        self._TaskName = None

    @property
    def IsSuccess(self):
        r"""是否成功
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName


    def _deserialize(self, params):
        self._IsSuccess = params.get("IsSuccess")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyStaticStoreRequest(AbstractModel):
    r"""DestroyStaticStore请求参数结构体

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
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CdnDomain(self):
        r"""cdn域名
        :rtype: str
        """
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
    r"""DestroyStaticStore返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 条件任务结果(succ/fail)
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""条件任务结果(succ/fail)
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DropIndex(AbstractModel):
    r"""本类型用于UpdateTable接口中描述待删除索引信息

    """

    def __init__(self):
        r"""
        :param _IndexName: 索引名称
        :type IndexName: str
        """
        self._IndexName = None

    @property
    def IndexName(self):
        r"""索引名称
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName


    def _deserialize(self, params):
        self._IndexName = params.get("IndexName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditAuthConfigRequest(AbstractModel):
    r"""EditAuthConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _PhoneNumberLogin: 手机号登录配置 "TRUE",  "FALSE", "LOGIN_ONLY"
        :type PhoneNumberLogin: str
        :param _AnonymousLogin: 匿名登录配置 "TRUE",  "FALSE"
        :type AnonymousLogin: str
        :param _UsernameLogin: 用户名密码登录配置 "TRUE",  "FALSE"
        :type UsernameLogin: str
        """
        self._EnvId = None
        self._PhoneNumberLogin = None
        self._AnonymousLogin = None
        self._UsernameLogin = None

    @property
    def EnvId(self):
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def PhoneNumberLogin(self):
        r"""手机号登录配置 "TRUE",  "FALSE", "LOGIN_ONLY"
        :rtype: str
        """
        return self._PhoneNumberLogin

    @PhoneNumberLogin.setter
    def PhoneNumberLogin(self, PhoneNumberLogin):
        self._PhoneNumberLogin = PhoneNumberLogin

    @property
    def AnonymousLogin(self):
        r"""匿名登录配置 "TRUE",  "FALSE"
        :rtype: str
        """
        return self._AnonymousLogin

    @AnonymousLogin.setter
    def AnonymousLogin(self, AnonymousLogin):
        self._AnonymousLogin = AnonymousLogin

    @property
    def UsernameLogin(self):
        r"""用户名密码登录配置 "TRUE",  "FALSE"
        :rtype: str
        """
        return self._UsernameLogin

    @UsernameLogin.setter
    def UsernameLogin(self, UsernameLogin):
        self._UsernameLogin = UsernameLogin


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._PhoneNumberLogin = params.get("PhoneNumberLogin")
        self._AnonymousLogin = params.get("AnonymousLogin")
        self._UsernameLogin = params.get("UsernameLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditAuthConfigResponse(AbstractModel):
    r"""EditAuthConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnvInfo(AbstractModel):
    r"""环境信息

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
        :type PackageId: str
        :param _PackageName: 套餐中文名称，参考DescribePackages接口的返回值。
        :type PackageName: str
        :param _LogServices: 云日志服务列表
        :type LogServices: list of LogServiceInfo
        :param _StaticStorages: 静态资源信息
        :type StaticStorages: list of StaticStorageInfo
        :param _IsAutoDegrade: 是否到期自动降为免费版
        :type IsAutoDegrade: bool
        :param _EnvChannel: 环境渠道
        :type EnvChannel: str
        :param _PayMode: 支付方式。包含以下取值：
<li> prepayment：预付费</li>
<li> postpaid：后付费</li>
        :type PayMode: str
        :param _IsDefault: 是否为默认环境
        :type IsDefault: bool
        :param _Region: 环境所属地域
        :type Region: str
        :param _Tags: 环境标签列表
        :type Tags: list of Tag
        :param _CustomLogServices: 自定义日志服务
        :type CustomLogServices: list of ClsInfo
        :param _EnvType: 环境类型：baas, run, hoting, weda
        :type EnvType: str
        :param _IsDauPackage: 是否是dau新套餐
        :type IsDauPackage: bool
        :param _PackageType: 套餐类型:空\baas\tcbr
        :type PackageType: str
        :param _ArchitectureType: 架构类型
        :type ArchitectureType: str
        :param _Recycle: 回收标志，默认为空
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
        r"""账户下该环境唯一标识
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Source(self):
        r"""环境来源。包含以下取值：
<li>miniapp：微信小程序</li>
<li>qcloud ：腾讯云</li>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Alias(self):
        r"""环境别名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""最后修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        r"""环境状态。包含以下取值：
<li>NORMAL：正常可用</li>
<li>UNAVAILABLE：服务不可用，可能是尚未初始化或者初始化过程中</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Databases(self):
        r"""数据库列表
        :rtype: list of DatabasesInfo
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def Storages(self):
        r"""存储列表
        :rtype: list of StorageInfo
        """
        return self._Storages

    @Storages.setter
    def Storages(self, Storages):
        self._Storages = Storages

    @property
    def Functions(self):
        r"""函数列表
        :rtype: list of FunctionInfo
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def PackageId(self):
        r"""tcb产品套餐ID，参考DescribePackages接口的返回值。
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def PackageName(self):
        r"""套餐中文名称，参考DescribePackages接口的返回值。
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def LogServices(self):
        r"""云日志服务列表
        :rtype: list of LogServiceInfo
        """
        return self._LogServices

    @LogServices.setter
    def LogServices(self, LogServices):
        self._LogServices = LogServices

    @property
    def StaticStorages(self):
        r"""静态资源信息
        :rtype: list of StaticStorageInfo
        """
        return self._StaticStorages

    @StaticStorages.setter
    def StaticStorages(self, StaticStorages):
        self._StaticStorages = StaticStorages

    @property
    def IsAutoDegrade(self):
        r"""是否到期自动降为免费版
        :rtype: bool
        """
        return self._IsAutoDegrade

    @IsAutoDegrade.setter
    def IsAutoDegrade(self, IsAutoDegrade):
        self._IsAutoDegrade = IsAutoDegrade

    @property
    def EnvChannel(self):
        r"""环境渠道
        :rtype: str
        """
        return self._EnvChannel

    @EnvChannel.setter
    def EnvChannel(self, EnvChannel):
        self._EnvChannel = EnvChannel

    @property
    def PayMode(self):
        r"""支付方式。包含以下取值：
<li> prepayment：预付费</li>
<li> postpaid：后付费</li>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def IsDefault(self):
        r"""是否为默认环境
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Region(self):
        r"""环境所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Tags(self):
        r"""环境标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CustomLogServices(self):
        r"""自定义日志服务
        :rtype: list of ClsInfo
        """
        return self._CustomLogServices

    @CustomLogServices.setter
    def CustomLogServices(self, CustomLogServices):
        self._CustomLogServices = CustomLogServices

    @property
    def EnvType(self):
        r"""环境类型：baas, run, hoting, weda
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def IsDauPackage(self):
        r"""是否是dau新套餐
        :rtype: bool
        """
        return self._IsDauPackage

    @IsDauPackage.setter
    def IsDauPackage(self, IsDauPackage):
        self._IsDauPackage = IsDauPackage

    @property
    def PackageType(self):
        r"""套餐类型:空\baas\tcbr
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ArchitectureType(self):
        r"""架构类型
        :rtype: str
        """
        return self._ArchitectureType

    @ArchitectureType.setter
    def ArchitectureType(self, ArchitectureType):
        self._ArchitectureType = ArchitectureType

    @property
    def Recycle(self):
        r"""回收标志，默认为空
        :rtype: str
        """
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
        


class FunctionInfo(AbstractModel):
    r"""函数的信息

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
        r"""命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Region(self):
        r"""所属地域。
当前支持ap-shanghai
        :rtype: str
        """
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
        


class IndexAccesses(AbstractModel):
    r"""索引命中信息

    """

    def __init__(self):
        r"""
        :param _Ops: 索引命中次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Ops: int
        :param _Since: 命中次数从何时开始计数
注意：此字段可能返回 null，表示取不到有效值。
        :type Since: str
        """
        self._Ops = None
        self._Since = None

    @property
    def Ops(self):
        r"""索引命中次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Ops

    @Ops.setter
    def Ops(self, Ops):
        self._Ops = Ops

    @property
    def Since(self):
        r"""命中次数从何时开始计数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Since

    @Since.setter
    def Since(self, Since):
        self._Since = Since


    def _deserialize(self, params):
        self._Ops = params.get("Ops")
        self._Since = params.get("Since")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexInfo(AbstractModel):
    r"""索引信息

    """

    def __init__(self):
        r"""
        :param _Name: 索引名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Size: 索引大小，单位: 字节
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param _Keys: 索引键值
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of Indexkey
        :param _Accesses: 索引使用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Accesses: :class:`tencentcloud.tcb.v20180608.models.IndexAccesses`
        :param _Unique: 是否为唯一索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Unique: bool
        """
        self._Name = None
        self._Size = None
        self._Keys = None
        self._Accesses = None
        self._Unique = None

    @property
    def Name(self):
        r"""索引名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        r"""索引大小，单位: 字节
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Keys(self):
        r"""索引键值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Indexkey
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Accesses(self):
        r"""索引使用信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcb.v20180608.models.IndexAccesses`
        """
        return self._Accesses

    @Accesses.setter
    def Accesses(self, Accesses):
        self._Accesses = Accesses

    @property
    def Unique(self):
        r"""是否为唯一索引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Unique

    @Unique.setter
    def Unique(self, Unique):
        self._Unique = Unique


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        if params.get("Keys") is not None:
            self._Keys = []
            for item in params.get("Keys"):
                obj = Indexkey()
                obj._deserialize(item)
                self._Keys.append(obj)
        if params.get("Accesses") is not None:
            self._Accesses = IndexAccesses()
            self._Accesses._deserialize(params.get("Accesses"))
        self._Unique = params.get("Unique")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Indexkey(AbstractModel):
    r"""索引的key值

    """

    def __init__(self):
        r"""
        :param _Name: 键名
        :type Name: str
        :param _Direction: 方向：specify 1 for ascending or -1 for descending
        :type Direction: str
        """
        self._Name = None
        self._Direction = None

    @property
    def Name(self):
        r"""键名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Direction(self):
        r"""方向：specify 1 for ascending or -1 for descending
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVPair(AbstractModel):
    r"""键值对

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
        r"""键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""值
        :rtype: str
        """
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
        


class ListTablesRequest(AbstractModel):
    r"""ListTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MgoLimit: 每页返回数量（0-1000)
        :type MgoLimit: int
        :param _Tag: FlexDB实例ID
        :type Tag: str
        :param _MgoOffset: 分页偏移量
        :type MgoOffset: int
        :param _Filters: 过滤标签数组，用于过滤表名，可选值如：HIDDEN、WEDA、WEDA_SYSTEM
        :type Filters: list of str
        :param _SearchValue: 模糊搜索查询值
        :type SearchValue: str
        :param _ShowHidden: 是否展示隐藏表
        :type ShowHidden: bool
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _MongoConnector: mongo连接器信息
        :type MongoConnector: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        self._MgoLimit = None
        self._Tag = None
        self._MgoOffset = None
        self._Filters = None
        self._SearchValue = None
        self._ShowHidden = None
        self._EnvId = None
        self._MongoConnector = None

    @property
    def MgoLimit(self):
        r"""每页返回数量（0-1000)
        :rtype: int
        """
        return self._MgoLimit

    @MgoLimit.setter
    def MgoLimit(self, MgoLimit):
        self._MgoLimit = MgoLimit

    @property
    def Tag(self):
        r"""FlexDB实例ID
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def MgoOffset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._MgoOffset

    @MgoOffset.setter
    def MgoOffset(self, MgoOffset):
        self._MgoOffset = MgoOffset

    @property
    def Filters(self):
        r"""过滤标签数组，用于过滤表名，可选值如：HIDDEN、WEDA、WEDA_SYSTEM
        :rtype: list of str
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SearchValue(self):
        r"""模糊搜索查询值
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def ShowHidden(self):
        r"""是否展示隐藏表
        :rtype: bool
        """
        return self._ShowHidden

    @ShowHidden.setter
    def ShowHidden(self, ShowHidden):
        self._ShowHidden = ShowHidden

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MongoConnector(self):
        r"""mongo连接器信息
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        return self._MongoConnector

    @MongoConnector.setter
    def MongoConnector(self, MongoConnector):
        self._MongoConnector = MongoConnector


    def _deserialize(self, params):
        self._MgoLimit = params.get("MgoLimit")
        self._Tag = params.get("Tag")
        self._MgoOffset = params.get("MgoOffset")
        self._Filters = params.get("Filters")
        self._SearchValue = params.get("SearchValue")
        self._ShowHidden = params.get("ShowHidden")
        self._EnvId = params.get("EnvId")
        if params.get("MongoConnector") is not None:
            self._MongoConnector = MongoConnector()
            self._MongoConnector._deserialize(params.get("MongoConnector"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTablesResponse(AbstractModel):
    r"""ListTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tables: 表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of TableInfo
        :param _Pager: 分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Pager: :class:`tencentcloud.tcb.v20180608.models.Pager`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tables = None
        self._Pager = None
        self._RequestId = None

    @property
    def Tables(self):
        r"""表信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TableInfo
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def Pager(self):
        r"""分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcb.v20180608.models.Pager`
        """
        return self._Pager

    @Pager.setter
    def Pager(self, Pager):
        self._Pager = Pager

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = TableInfo()
                obj._deserialize(item)
                self._Tables.append(obj)
        if params.get("Pager") is not None:
            self._Pager = Pager()
            self._Pager._deserialize(params.get("Pager"))
        self._RequestId = params.get("RequestId")


class LogObject(AbstractModel):
    r"""CLS日志单条信息

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
        r"""日志属于的 topic ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        r"""日志主题的名字
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Timestamp(self):
        r"""日志时间
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Content(self):
        r"""日志内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FileName(self):
        r"""采集路径
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Source(self):
        r"""日志来源设备
        :rtype: str
        """
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
    r"""CLS日志结果

    """

    def __init__(self):
        r"""
        :param _Context: 获取更多检索结果的游标
        :type Context: str
        :param _ListOver: 搜索结果是否已经全部返回
        :type ListOver: bool
        :param _Results: 日志内容信息
        :type Results: list of LogObject
        :param _AnalysisRecords: 日志聚合结果
        :type AnalysisRecords: list of str
        """
        self._Context = None
        self._ListOver = None
        self._Results = None
        self._AnalysisRecords = None

    @property
    def Context(self):
        r"""获取更多检索结果的游标
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        r"""搜索结果是否已经全部返回
        :rtype: bool
        """
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Results(self):
        r"""日志内容信息
        :rtype: list of LogObject
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def AnalysisRecords(self):
        r"""日志聚合结果
        :rtype: list of str
        """
        return self._AnalysisRecords

    @AnalysisRecords.setter
    def AnalysisRecords(self, AnalysisRecords):
        self._AnalysisRecords = AnalysisRecords


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = LogObject()
                obj._deserialize(item)
                self._Results.append(obj)
        self._AnalysisRecords = params.get("AnalysisRecords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogServiceInfo(AbstractModel):
    r"""云日志服务相关信息

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
        r"""log名
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def LogsetId(self):
        r"""log-id
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicName(self):
        r"""topic名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicId(self):
        r"""topic-id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Region(self):
        r"""cls日志所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Period(self):
        r"""topic保存时长 默认7天
        :rtype: int
        """
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
        


class MgoCommandParam(AbstractModel):
    r"""待执行命令

    """

    def __init__(self):
        r"""
        :param _TableName: 表名
        :type TableName: str
        :param _CommandType: 操作类型，可选类型为：UPDATE/QUERY/INSERT/DELETE/COMMAND，本操作必须按实际填写，监控会依赖该字段统计本次操作的类型，并实时减少用户配额，如果填写错误会误扣用户请求配额
        :type CommandType: str
        :param _Command: 待执行命令
        :type Command: str
        """
        self._TableName = None
        self._CommandType = None
        self._Command = None

    @property
    def TableName(self):
        r"""表名
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def CommandType(self):
        r"""操作类型，可选类型为：UPDATE/QUERY/INSERT/DELETE/COMMAND，本操作必须按实际填写，监控会依赖该字段统计本次操作的类型，并实时减少用户配额，如果填写错误会误扣用户请求配额
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def Command(self):
        r"""待执行命令
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._CommandType = params.get("CommandType")
        self._Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MgoIndexKeys(AbstractModel):
    r"""本类型用于UpdateTable接口中描述待创建索引信息

    """

    def __init__(self):
        r"""
        :param _Name: 无
        :type Name: str
        :param _Direction: 无
        :type Direction: str
        """
        self._Name = None
        self._Direction = None

    @property
    def Name(self):
        r"""无
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Direction(self):
        r"""无
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MgoKeySchema(AbstractModel):
    r"""本类型用于接口中描述待创建索引结构

    """

    def __init__(self):
        r"""
        :param _MgoIndexKeys: 索引字段
        :type MgoIndexKeys: list of MgoIndexKeys
        :param _MgoIsUnique: 是否唯一索引
        :type MgoIsUnique: bool
        :param _MgoIsSparse: 是否稀疏索引
        :type MgoIsSparse: bool
        """
        self._MgoIndexKeys = None
        self._MgoIsUnique = None
        self._MgoIsSparse = None

    @property
    def MgoIndexKeys(self):
        r"""索引字段
        :rtype: list of MgoIndexKeys
        """
        return self._MgoIndexKeys

    @MgoIndexKeys.setter
    def MgoIndexKeys(self, MgoIndexKeys):
        self._MgoIndexKeys = MgoIndexKeys

    @property
    def MgoIsUnique(self):
        r"""是否唯一索引
        :rtype: bool
        """
        return self._MgoIsUnique

    @MgoIsUnique.setter
    def MgoIsUnique(self, MgoIsUnique):
        self._MgoIsUnique = MgoIsUnique

    @property
    def MgoIsSparse(self):
        r"""是否稀疏索引
        :rtype: bool
        """
        return self._MgoIsSparse

    @MgoIsSparse.setter
    def MgoIsSparse(self, MgoIsSparse):
        self._MgoIsSparse = MgoIsSparse


    def _deserialize(self, params):
        if params.get("MgoIndexKeys") is not None:
            self._MgoIndexKeys = []
            for item in params.get("MgoIndexKeys"):
                obj = MgoIndexKeys()
                obj._deserialize(item)
                self._MgoIndexKeys.append(obj)
        self._MgoIsUnique = params.get("MgoIsUnique")
        self._MgoIsSparse = params.get("MgoIsSparse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudBaseGWAPIRequest(AbstractModel):
    r"""ModifyCloudBaseGWAPI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _APIId: API ID
        :type APIId: str
        :param _Options: 选项列表，key取值：domain, path。
        :type Options: list of CloudBaseOption
        """
        self._ServiceId = None
        self._APIId = None
        self._Options = None

    @property
    def ServiceId(self):
        r"""Service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def APIId(self):
        r"""API ID
        :rtype: str
        """
        return self._APIId

    @APIId.setter
    def APIId(self, APIId):
        self._APIId = APIId

    @property
    def Options(self):
        r"""选项列表，key取值：domain, path。
        :rtype: list of CloudBaseOption
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._APIId = params.get("APIId")
        if params.get("Options") is not None:
            self._Options = []
            for item in params.get("Options"):
                obj = CloudBaseOption()
                obj._deserialize(item)
                self._Options.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudBaseGWAPIResponse(AbstractModel):
    r"""ModifyCloudBaseGWAPI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyClsTopicRequest(AbstractModel):
    r"""ModifyClsTopic请求参数结构体

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
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Period(self):
        r"""日志生命周期，单位天，可取值范围1~3600，取值为3640时代表永久保存
        :rtype: int
        """
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
    r"""ModifyClsTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDatabaseACLRequest(AbstractModel):
    r"""ModifyDatabaseACL请求参数结构体

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
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionName(self):
        r"""集合名称
        :rtype: str
        """
        return self._CollectionName

    @CollectionName.setter
    def CollectionName(self, CollectionName):
        self._CollectionName = CollectionName

    @property
    def AclTag(self):
        r"""权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
        :rtype: str
        """
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
    r"""ModifyDatabaseACL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyEnvPlanRequest(AbstractModel):
    r"""ModifyEnvPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 所需变更套餐的环境ID
        :type EnvId: str
        :param _PackageId: 目标套餐Id。
对于云开发环境套餐，可通过 [DescribeBaasPackageList](https://cloud.tencent.com/document/product/876/78167) 接口获取，对应其出参的PackageName
        :type PackageId: str
        :param _AutoVoucher: 是否自动选择代金券支付。
        :type AutoVoucher: bool
        """
        self._EnvId = None
        self._PackageId = None
        self._AutoVoucher = None

    @property
    def EnvId(self):
        r"""所需变更套餐的环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def PackageId(self):
        r"""目标套餐Id。
对于云开发环境套餐，可通过 [DescribeBaasPackageList](https://cloud.tencent.com/document/product/876/78167) 接口获取，对应其出参的PackageName
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def AutoVoucher(self):
        r"""是否自动选择代金券支付。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._PackageId = params.get("PackageId")
        self._AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvPlanResponse(AbstractModel):
    r"""ModifyEnvPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyEnvRequest(AbstractModel):
    r"""ModifyEnv请求参数结构体

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
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Alias(self):
        r"""环境备注名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :rtype: str
        """
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
    r"""ModifyEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySafeRuleRequest(AbstractModel):
    r"""ModifySafeRule请求参数结构体

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
<li> CUSTOM：自定义安全规则</li>
        :type AclTag: str
        :param _Rule: 安全规则内容。
当 AclTag=CUSTOM 时，此参数必填。
详情参考：[文档型数据库安全规则](https://docs.cloudbase.net/database/security-rules)
        :type Rule: str
        """
        self._EnvId = None
        self._CollectionName = None
        self._AclTag = None
        self._Rule = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionName(self):
        r"""集合名称
        :rtype: str
        """
        return self._CollectionName

    @CollectionName.setter
    def CollectionName(self, CollectionName):
        self._CollectionName = CollectionName

    @property
    def AclTag(self):
        r"""权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
<li> CUSTOM：自定义安全规则</li>
        :rtype: str
        """
        return self._AclTag

    @AclTag.setter
    def AclTag(self, AclTag):
        self._AclTag = AclTag

    @property
    def Rule(self):
        r"""安全规则内容。
当 AclTag=CUSTOM 时，此参数必填。
详情参考：[文档型数据库安全规则](https://docs.cloudbase.net/database/security-rules)
        :rtype: str
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CollectionName = params.get("CollectionName")
        self._AclTag = params.get("AclTag")
        self._Rule = params.get("Rule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySafeRuleResponse(AbstractModel):
    r"""ModifySafeRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyUserRequest(AbstractModel):
    r"""ModifyUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境id
        :type EnvId: str
        :param _Uid: 用户Id, 不做修改
        :type Uid: str
        :param _Name: 用户名，用户名规则：1. 长度1-64字符 2. 只能包含大小写英文字母、数字和符号 . _ - 3. 只能以字母或数字开头 4. 不能重复，不传该字段或传空字符不修改
        :type Name: str
        :param _Type: 用户类型：0-内部用户、1-外部用户，默认0（内部用户），不传该字段或传空字符串不修改
        :type Type: str
        :param _Password: 密码，传入Uid时密码可不传。密码规则：1. 长度8-32字符（推荐12位以上） 2. 不能以特殊字符开头 3. 至少包含以下四项中的三项：小写字母a-z、大写字母A-Z、数字0-9、特殊字符()!@#$%^&*\|?><_-，不传该字段或传空字符串不修改
        :type Password: str
        :param _UserStatus: 用户状态：ACTIVE（激活）、BLOCKED（冻结），默认冻结，不传该字段或传空字符串不修改
        :type UserStatus: str
        :param _NickName: 用户昵称，长度2-64字符，不传该字段不修改，传空字符修改为空
        :type NickName: str
        :param _Phone: 手机号，11位数字，不传该字段不修改，传空字符串修改为空
        :type Phone: str
        :param _Email: 邮箱地址，不传该字段不修改，传空字符修改为空
        :type Email: str
        :param _AvatarUrl: 头像链接，可访问的公网URL，不传该字段不修改，传空字符串修改为空
        :type AvatarUrl: str
        :param _Description: 用户描述，最多200字符，不传该字段不修改，传空字符修改为空
        :type Description: str
        """
        self._EnvId = None
        self._Uid = None
        self._Name = None
        self._Type = None
        self._Password = None
        self._UserStatus = None
        self._NickName = None
        self._Phone = None
        self._Email = None
        self._AvatarUrl = None
        self._Description = None

    @property
    def EnvId(self):
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Uid(self):
        r"""用户Id, 不做修改
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Name(self):
        r"""用户名，用户名规则：1. 长度1-64字符 2. 只能包含大小写英文字母、数字和符号 . _ - 3. 只能以字母或数字开头 4. 不能重复，不传该字段或传空字符不修改
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""用户类型：0-内部用户、1-外部用户，默认0（内部用户），不传该字段或传空字符串不修改
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Password(self):
        r"""密码，传入Uid时密码可不传。密码规则：1. 长度8-32字符（推荐12位以上） 2. 不能以特殊字符开头 3. 至少包含以下四项中的三项：小写字母a-z、大写字母A-Z、数字0-9、特殊字符()!@#$%^&*\|?><_-，不传该字段或传空字符串不修改
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def UserStatus(self):
        r"""用户状态：ACTIVE（激活）、BLOCKED（冻结），默认冻结，不传该字段或传空字符串不修改
        :rtype: str
        """
        return self._UserStatus

    @UserStatus.setter
    def UserStatus(self, UserStatus):
        self._UserStatus = UserStatus

    @property
    def NickName(self):
        r"""用户昵称，长度2-64字符，不传该字段不修改，传空字符修改为空
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Phone(self):
        r"""手机号，11位数字，不传该字段不修改，传空字符串修改为空
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""邮箱地址，不传该字段不修改，传空字符修改为空
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def AvatarUrl(self):
        r"""头像链接，可访问的公网URL，不传该字段不修改，传空字符串修改为空
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def Description(self):
        r"""用户描述，最多200字符，不传该字段不修改，传空字符修改为空
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Uid = params.get("Uid")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Password = params.get("Password")
        self._UserStatus = params.get("UserStatus")
        self._NickName = params.get("NickName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._AvatarUrl = params.get("AvatarUrl")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResp(AbstractModel):
    r"""修改用户返回值

    """

    def __init__(self):
        r"""
        :param _Success: 是否成功
        :type Success: bool
        """
        self._Success = None

    @property
    def Success(self):
        r"""是否成功
        :rtype: bool
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success


    def _deserialize(self, params):
        self._Success = params.get("Success")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResponse(AbstractModel):
    r"""ModifyUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 修改用户返回值
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.tcb.v20180608.models.ModifyUserResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""修改用户返回值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyUserResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ModifyUserResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class MongoConnector(AbstractModel):
    r"""MongoDB连接器配置

    """

    def __init__(self):
        r"""
        :param _InstanceId: 连接器实例ID
        :type InstanceId: str
        :param _DatabaseName: MongoDB数据库名
        :type DatabaseName: str
        """
        self._InstanceId = None
        self._DatabaseName = None

    @property
    def InstanceId(self):
        r"""连接器实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DatabaseName(self):
        r"""MongoDB数据库名
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DatabaseName = params.get("DatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySQLClusterDetail(AbstractModel):
    r"""MySql 集群详情

    """

    def __init__(self):
        r"""
        :param _DbClusterId: 集群ID
        :type DbClusterId: str
        :param _NetInfo: 网络详情
        :type NetInfo: :class:`tencentcloud.tcb.v20180608.models.MySQLNetDetail`
        :param _DbInfo: 数据库详情
        :type DbInfo: :class:`tencentcloud.tcb.v20180608.models.ClusterDetail`
        """
        self._DbClusterId = None
        self._NetInfo = None
        self._DbInfo = None

    @property
    def DbClusterId(self):
        r"""集群ID
        :rtype: str
        """
        return self._DbClusterId

    @DbClusterId.setter
    def DbClusterId(self, DbClusterId):
        self._DbClusterId = DbClusterId

    @property
    def NetInfo(self):
        r"""网络详情
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MySQLNetDetail`
        """
        return self._NetInfo

    @NetInfo.setter
    def NetInfo(self, NetInfo):
        self._NetInfo = NetInfo

    @property
    def DbInfo(self):
        r"""数据库详情
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ClusterDetail`
        """
        return self._DbInfo

    @DbInfo.setter
    def DbInfo(self, DbInfo):
        self._DbInfo = DbInfo


    def _deserialize(self, params):
        self._DbClusterId = params.get("DbClusterId")
        if params.get("NetInfo") is not None:
            self._NetInfo = MySQLNetDetail()
            self._NetInfo._deserialize(params.get("NetInfo"))
        if params.get("DbInfo") is not None:
            self._DbInfo = ClusterDetail()
            self._DbInfo._deserialize(params.get("DbInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySQLNetDetail(AbstractModel):
    r"""TDSQL-C网络信息类型

    """

    def __init__(self):
        r"""
        :param _PrivateNetAddress: 内网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateNetAddress: str
        :param _PubNetAddress: 外网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PubNetAddress: str
        :param _Net: 网络信息（VPCID/SubnetID）
注意：此字段可能返回 null，表示取不到有效值。
        :type Net: str
        :param _PubNetAccessEnabled: 是否开通公网
        :type PubNetAccessEnabled: bool
        :param _VpcId: vpc id 
        :type VpcId: str
        :param _VpcName: vpc name
        :type VpcName: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _SubnetName: 子网名
        :type SubnetName: str
        """
        self._PrivateNetAddress = None
        self._PubNetAddress = None
        self._Net = None
        self._PubNetAccessEnabled = None
        self._VpcId = None
        self._VpcName = None
        self._SubnetId = None
        self._SubnetName = None

    @property
    def PrivateNetAddress(self):
        r"""内网地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateNetAddress

    @PrivateNetAddress.setter
    def PrivateNetAddress(self, PrivateNetAddress):
        self._PrivateNetAddress = PrivateNetAddress

    @property
    def PubNetAddress(self):
        r"""外网地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PubNetAddress

    @PubNetAddress.setter
    def PubNetAddress(self, PubNetAddress):
        self._PubNetAddress = PubNetAddress

    @property
    def Net(self):
        r"""网络信息（VPCID/SubnetID）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Net

    @Net.setter
    def Net(self, Net):
        self._Net = Net

    @property
    def PubNetAccessEnabled(self):
        r"""是否开通公网
        :rtype: bool
        """
        return self._PubNetAccessEnabled

    @PubNetAccessEnabled.setter
    def PubNetAccessEnabled(self, PubNetAccessEnabled):
        self._PubNetAccessEnabled = PubNetAccessEnabled

    @property
    def VpcId(self):
        r"""vpc id 
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""vpc name
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetId(self):
        r"""子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        r"""子网名
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName


    def _deserialize(self, params):
        self._PrivateNetAddress = params.get("PrivateNetAddress")
        self._PubNetAddress = params.get("PubNetAddress")
        self._Net = params.get("Net")
        self._PubNetAccessEnabled = params.get("PubNetAccessEnabled")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MySQLTaskStatus(AbstractModel):
    r"""MySql 任务状态

    """

    def __init__(self):
        r"""
        :param _Status: SUCCESS | FAILED | PENDING
        :type Status: str
        :param _StatusDesc: 状态描述
        :type StatusDesc: str
        """
        self._Status = None
        self._StatusDesc = None

    @property
    def Status(self):
        r"""SUCCESS | FAILED | PENDING
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pager(AbstractModel):
    r"""分页信息

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param _Limit: 每页返回记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        :param _Total: 文档集合总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._Offset = None
        self._Limit = None
        self._Total = None

    @property
    def Offset(self):
        r"""分页偏移量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页返回记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Total(self):
        r"""文档集合总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermissionInfo(AbstractModel):
    r"""FlexDB数据库权限信息

    """

    def __init__(self):
        r"""
        :param _AclTag: "READONLY",   //公有读，私有写。所有用户可读，仅创建者及管理员可写  
"PRIVATE",    //私有读写，仅创建者及管理员可读写  
"ADMINWRITE", //所有用户可读，仅管理员可写  
"ADMINONLY",  //仅管理员可操作  
"CUSTOM",     // 安全规则
        :type AclTag: str
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _Rule: 自定义规则
        :type Rule: str
        """
        self._AclTag = None
        self._EnvId = None
        self._Rule = None

    @property
    def AclTag(self):
        r""""READONLY",   //公有读，私有写。所有用户可读，仅创建者及管理员可写  
"PRIVATE",    //私有读写，仅创建者及管理员可读写  
"ADMINWRITE", //所有用户可读，仅管理员可写  
"ADMINONLY",  //仅管理员可操作  
"CUSTOM",     // 安全规则
        :rtype: str
        """
        return self._AclTag

    @AclTag.setter
    def AclTag(self, AclTag):
        self._AclTag = AclTag

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Rule(self):
        r"""自定义规则
        :rtype: str
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._AclTag = params.get("AclTag")
        self._EnvId = params.get("EnvId")
        self._Rule = params.get("Rule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReinstateEnvRequest(AbstractModel):
    r"""ReinstateEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
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
    r"""ReinstateEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RenewEnvRequest(AbstractModel):
    r"""RenewEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Period: 续费周期，单位：月。
默认值为 1，即续费1个月。
        :type Period: int
        :param _AutoVoucher: 是否自动选择代金券支付。
        :type AutoVoucher: bool
        """
        self._EnvId = None
        self._Period = None
        self._AutoVoucher = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Period(self):
        r"""续费周期，单位：月。
默认值为 1，即续费1个月。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoVoucher(self):
        r"""是否自动选择代金券支付。
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Period = params.get("Period")
        self._AutoVoucher = params.get("AutoVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewEnvResponse(AbstractModel):
    r"""RenewEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RunCommandsRequest(AbstractModel):
    r"""RunCommands请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MgoCommands: 待执行命令
        :type MgoCommands: list of MgoCommandParam
        :param _Tag: 实例ID
        :type Tag: str
        :param _EnvId: 环境id
        :type EnvId: str
        :param _MongoConnector: Mongo连接器实例信息
        :type MongoConnector: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        self._MgoCommands = None
        self._Tag = None
        self._EnvId = None
        self._MongoConnector = None

    @property
    def MgoCommands(self):
        r"""待执行命令
        :rtype: list of MgoCommandParam
        """
        return self._MgoCommands

    @MgoCommands.setter
    def MgoCommands(self, MgoCommands):
        self._MgoCommands = MgoCommands

    @property
    def Tag(self):
        r"""实例ID
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def EnvId(self):
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MongoConnector(self):
        r"""Mongo连接器实例信息
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        return self._MongoConnector

    @MongoConnector.setter
    def MongoConnector(self, MongoConnector):
        self._MongoConnector = MongoConnector


    def _deserialize(self, params):
        if params.get("MgoCommands") is not None:
            self._MgoCommands = []
            for item in params.get("MgoCommands"):
                obj = MgoCommandParam()
                obj._deserialize(item)
                self._MgoCommands.append(obj)
        self._Tag = params.get("Tag")
        self._EnvId = params.get("EnvId")
        if params.get("MongoConnector") is not None:
            self._MongoConnector = MongoConnector()
            self._MongoConnector._deserialize(params.get("MongoConnector"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunCommandsResponse(AbstractModel):
    r"""RunCommands返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果，返回结果为一个json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回结果，返回结果为一个json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class RunSqlRequest(AbstractModel):
    r"""RunSql请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sql: 要执行的SQL语句
        :type Sql: str
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _DbInstance: 数据库连接器实例信息
        :type DbInstance: :class:`tencentcloud.tcb.v20180608.models.DbInstance`
        :param _ReadOnly: 是否只读；当 `true` 时仅允许以 `SELECT/WITH/SHOW/DESCRIBE/DESC/EXPLAIN` 开头的 SQL
        :type ReadOnly: bool
        """
        self._Sql = None
        self._EnvId = None
        self._DbInstance = None
        self._ReadOnly = None

    @property
    def Sql(self):
        r"""要执行的SQL语句
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def DbInstance(self):
        r"""数据库连接器实例信息
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DbInstance`
        """
        return self._DbInstance

    @DbInstance.setter
    def DbInstance(self, DbInstance):
        self._DbInstance = DbInstance

    @property
    def ReadOnly(self):
        r"""是否只读；当 `true` 时仅允许以 `SELECT/WITH/SHOW/DESCRIBE/DESC/EXPLAIN` 开头的 SQL
        :rtype: bool
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly


    def _deserialize(self, params):
        self._Sql = params.get("Sql")
        self._EnvId = params.get("EnvId")
        if params.get("DbInstance") is not None:
            self._DbInstance = DbInstance()
            self._DbInstance._deserialize(params.get("DbInstance"))
        self._ReadOnly = params.get("ReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSqlResponse(AbstractModel):
    r"""RunSql返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 查询结果行，每个元素为 JSON 字符串
        :type Items: list of str
        :param _Infos: 列元数据信息，每个元素为 JSON 字符串，字段包含 `name/databaseType/nullable/length/precision/scale`
        :type Infos: list of str
        :param _RowsAffected: 受影响的行数（INSERT/UPDATE/DELETE 等语句）
        :type RowsAffected: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Infos = None
        self._RowsAffected = None
        self._RequestId = None

    @property
    def Items(self):
        r"""查询结果行，每个元素为 JSON 字符串
        :rtype: list of str
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Infos(self):
        r"""列元数据信息，每个元素为 JSON 字符串，字段包含 `name/databaseType/nullable/length/precision/scale`
        :rtype: list of str
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RowsAffected(self):
        r"""受影响的行数（INSERT/UPDATE/DELETE 等语句）
        :rtype: int
        """
        return self._RowsAffected

    @RowsAffected.setter
    def RowsAffected(self, RowsAffected):
        self._RowsAffected = RowsAffected

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Items = params.get("Items")
        self._Infos = params.get("Infos")
        self._RowsAffected = params.get("RowsAffected")
        self._RequestId = params.get("RequestId")


class SearchClsLogRequest(AbstractModel):
    r"""SearchClsLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境唯一ID
        :type EnvId: str
        :param _StartTime: 查询起始时间条件
        :type StartTime: str
        :param _EndTime: 查询结束时间条件
        :type EndTime: str
        :param _QueryString: 查询语句，例如查询云函数：(src:app OR src:system) AND log:\"START RequestId*\"， 查询云数据库：module:database，查询审批流：module:workflow，查询模型：module:model，查询用户权限：module:auth，以上仅为示例语句，实际使用时请根据具体日志内容进行调整，查询语句需严格遵循CLS（Cloud Log Service）语法规范 详细的语法规则请参考官方档：https://cloud.tencent.com/document/product/614/47044
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
        r"""环境唯一ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def StartTime(self):
        r"""查询起始时间条件
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间条件
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def QueryString(self):
        r"""查询语句，例如查询云函数：(src:app OR src:system) AND log:\"START RequestId*\"， 查询云数据库：module:database，查询审批流：module:workflow，查询模型：module:model，查询用户权限：module:auth，以上仅为示例语句，实际使用时请根据具体日志内容进行调整，查询语句需严格遵循CLS（Cloud Log Service）语法规范 详细的语法规则请参考官方档：https://cloud.tencent.com/document/product/614/47044
        :rtype: str
        """
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString

    @property
    def Limit(self):
        r"""单次要返回的日志条数，单次返回的最大条数为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        r"""加载更多使用，透传上次返回的 context 值，获取后续的日志内容，通过游标最多可获取10000条，请尽可能缩小时间范围
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        r"""按时间排序 asc（升序）或者 desc（降序），默认为 desc
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def UseLucene(self):
        r"""是否使用Lucene语法，默认为false
        :rtype: bool
        """
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
    r"""SearchClsLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogResults: 日志内容结果
        :type LogResults: :class:`tencentcloud.tcb.v20180608.models.LogResObject`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogResults = None
        self._RequestId = None

    @property
    def LogResults(self):
        r"""日志内容结果
        :rtype: :class:`tencentcloud.tcb.v20180608.models.LogResObject`
        """
        return self._LogResults

    @LogResults.setter
    def LogResults(self, LogResults):
        self._LogResults = LogResults

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LogResults") is not None:
            self._LogResults = LogResObject()
            self._LogResults._deserialize(params.get("LogResults"))
        self._RequestId = params.get("RequestId")


class StaticStorageInfo(AbstractModel):
    r"""静态CDN资源信息

    """

    def __init__(self):
        r"""
        :param _StaticDomain: 静态CDN域名
        :type StaticDomain: str
        :param _DefaultDirName: 静态CDN默认文件夹，当前为根目录
        :type DefaultDirName: str
        :param _Status: 资源状态(process/online/offline/init)
        :type Status: str
        :param _Region: cos所属区域
        :type Region: str
        :param _Bucket: bucket信息
        :type Bucket: str
        """
        self._StaticDomain = None
        self._DefaultDirName = None
        self._Status = None
        self._Region = None
        self._Bucket = None

    @property
    def StaticDomain(self):
        r"""静态CDN域名
        :rtype: str
        """
        return self._StaticDomain

    @StaticDomain.setter
    def StaticDomain(self, StaticDomain):
        self._StaticDomain = StaticDomain

    @property
    def DefaultDirName(self):
        r"""静态CDN默认文件夹，当前为根目录
        :rtype: str
        """
        return self._DefaultDirName

    @DefaultDirName.setter
    def DefaultDirName(self, DefaultDirName):
        self._DefaultDirName = DefaultDirName

    @property
    def Status(self):
        r"""资源状态(process/online/offline/init)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""cos所属区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""bucket信息
        :rtype: str
        """
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
        


class StaticStoreInfo(AbstractModel):
    r"""静态托管资源信息

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param _CdnDomain: 静态域名
注意：此字段可能返回 null，表示取不到有效值。
        :type CdnDomain: str
        :param _Bucket: COS桶
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param _Regoin: cos区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Regoin: str
        :param _Status: 资源状态:init(初始化)/process(处理中)/online(上线)/destroying(销毁中)/offline(下线))
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._EnvId = None
        self._CdnDomain = None
        self._Bucket = None
        self._Regoin = None
        self._Status = None
        self._Region = None

    @property
    def EnvId(self):
        r"""环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CdnDomain(self):
        r"""静态域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CdnDomain

    @CdnDomain.setter
    def CdnDomain(self, CdnDomain):
        self._CdnDomain = CdnDomain

    @property
    def Bucket(self):
        r"""COS桶
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Regoin(self):
        warnings.warn("parameter `Regoin` is deprecated", DeprecationWarning) 

        r"""cos区域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Regoin

    @Regoin.setter
    def Regoin(self, Regoin):
        warnings.warn("parameter `Regoin` is deprecated", DeprecationWarning) 

        self._Regoin = Regoin

    @property
    def Status(self):
        r"""资源状态:init(初始化)/process(处理中)/online(上线)/destroying(销毁中)/offline(下线))
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CdnDomain = params.get("CdnDomain")
        self._Bucket = params.get("Bucket")
        self._Regoin = params.get("Regoin")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    r"""StorageInfo 资源信息

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
        r"""资源所属地域。
当前支持ap-shanghai
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""桶名，存储资源的唯一标识
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def CdnDomain(self):
        r"""cdn 域名
        :rtype: str
        """
        return self._CdnDomain

    @CdnDomain.setter
    def CdnDomain(self, CdnDomain):
        self._CdnDomain = CdnDomain

    @property
    def AppId(self):
        r"""资源所属用户的腾讯云appId
        :rtype: str
        """
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
        


class TableInfo(AbstractModel):
    r"""表信息

    """

    def __init__(self):
        r"""
        :param _TableName: 表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param _Count: 表中文档数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Size: 表的大小（即表中文档总大小），单位：字节
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param _IndexCount: 索引数量
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexCount: int
        :param _IndexSize: 索引占用空间，单位：字节
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexSize: int
        """
        self._TableName = None
        self._Count = None
        self._Size = None
        self._IndexCount = None
        self._IndexSize = None

    @property
    def TableName(self):
        r"""表名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Count(self):
        r"""表中文档数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Size(self):
        r"""表的大小（即表中文档总大小），单位：字节
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def IndexCount(self):
        r"""索引数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IndexCount

    @IndexCount.setter
    def IndexCount(self, IndexCount):
        self._IndexCount = IndexCount

    @property
    def IndexSize(self):
        r"""索引占用空间，单位：字节
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IndexSize

    @IndexSize.setter
    def IndexSize(self, IndexSize):
        self._IndexSize = IndexSize


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._Count = params.get("Count")
        self._Size = params.get("Size")
        self._IndexCount = params.get("IndexCount")
        self._IndexSize = params.get("IndexSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签键值对

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
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
        :rtype: str
        """
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
        


class UpdateTableRequest(AbstractModel):
    r"""UpdateTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TableName: 表名
        :type TableName: str
        :param _Tag: FlexDB实例ID
        :type Tag: str
        :param _DropIndexes: 待删除索引信息
        :type DropIndexes: list of DropIndex
        :param _CreateIndexes: 待创建索引信息
        :type CreateIndexes: list of CreateIndex
        :param _EnvId: 云开发环境ID
        :type EnvId: str
        :param _MongoConnector: MongoDB连接器配置
        :type MongoConnector: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        self._TableName = None
        self._Tag = None
        self._DropIndexes = None
        self._CreateIndexes = None
        self._EnvId = None
        self._MongoConnector = None

    @property
    def TableName(self):
        r"""表名
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def Tag(self):
        r"""FlexDB实例ID
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def DropIndexes(self):
        r"""待删除索引信息
        :rtype: list of DropIndex
        """
        return self._DropIndexes

    @DropIndexes.setter
    def DropIndexes(self, DropIndexes):
        self._DropIndexes = DropIndexes

    @property
    def CreateIndexes(self):
        r"""待创建索引信息
        :rtype: list of CreateIndex
        """
        return self._CreateIndexes

    @CreateIndexes.setter
    def CreateIndexes(self, CreateIndexes):
        self._CreateIndexes = CreateIndexes

    @property
    def EnvId(self):
        r"""云开发环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def MongoConnector(self):
        r"""MongoDB连接器配置
        :rtype: :class:`tencentcloud.tcb.v20180608.models.MongoConnector`
        """
        return self._MongoConnector

    @MongoConnector.setter
    def MongoConnector(self, MongoConnector):
        self._MongoConnector = MongoConnector


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._Tag = params.get("Tag")
        if params.get("DropIndexes") is not None:
            self._DropIndexes = []
            for item in params.get("DropIndexes"):
                obj = DropIndex()
                obj._deserialize(item)
                self._DropIndexes.append(obj)
        if params.get("CreateIndexes") is not None:
            self._CreateIndexes = []
            for item in params.get("CreateIndexes"):
                obj = CreateIndex()
                obj._deserialize(item)
                self._CreateIndexes.append(obj)
        self._EnvId = params.get("EnvId")
        if params.get("MongoConnector") is not None:
            self._MongoConnector = MongoConnector()
            self._MongoConnector._deserialize(params.get("MongoConnector"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTableResponse(AbstractModel):
    r"""UpdateTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class User(AbstractModel):
    r"""用户信息

    """

    def __init__(self):
        r"""
        :param _Uid: 用户ID
        :type Uid: str
        :param _Name: 用户名
        :type Name: str
        :param _Type: 用户类型：internalUser-内部用户、externalUser-外部用户
        :type Type: str
        :param _UserStatus: 用户状态：ACTIVE（激活）、BLOCKED（冻结）
        :type UserStatus: str
        :param _NickName: 用户昵称
        :type NickName: str
        :param _Phone: 手机号
        :type Phone: str
        :param _Email: 邮箱
        :type Email: str
        :param _AvatarUrl: 头像链接
        :type AvatarUrl: str
        :param _Description: 用户描述
        :type Description: str
        """
        self._Uid = None
        self._Name = None
        self._Type = None
        self._UserStatus = None
        self._NickName = None
        self._Phone = None
        self._Email = None
        self._AvatarUrl = None
        self._Description = None

    @property
    def Uid(self):
        r"""用户ID
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Name(self):
        r"""用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""用户类型：internalUser-内部用户、externalUser-外部用户
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UserStatus(self):
        r"""用户状态：ACTIVE（激活）、BLOCKED（冻结）
        :rtype: str
        """
        return self._UserStatus

    @UserStatus.setter
    def UserStatus(self, UserStatus):
        self._UserStatus = UserStatus

    @property
    def NickName(self):
        r"""用户昵称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Phone(self):
        r"""手机号
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def AvatarUrl(self):
        r"""头像链接
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def Description(self):
        r"""用户描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Uid = params.get("Uid")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._UserStatus = params.get("UserStatus")
        self._NickName = params.get("NickName")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._AvatarUrl = params.get("AvatarUrl")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        