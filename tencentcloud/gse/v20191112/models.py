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


class Alias(AbstractModel):
    """别名对象

    """

    def __init__(self):
        r"""
        :param _AliasId: 别名的唯一标识符
        :type AliasId: str
        :param _AliasArn: 别名的全局唯一资源标识符
        :type AliasArn: str
        :param _Name: 名字，长度不小于1字符不超过1024字符
        :type Name: str
        :param _Description: 别名的可读说明，长度不小于1字符不超过1024字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _RoutingStrategy: 别名的路由配置
        :type RoutingStrategy: :class:`tencentcloud.gse.v20191112.models.RoutingStrategy`
        :param _CreationTime: 创建时间
        :type CreationTime: str
        :param _LastUpdatedTime: 上次修改此数据对象的时间
        :type LastUpdatedTime: str
        :param _Tags: 标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._AliasId = None
        self._AliasArn = None
        self._Name = None
        self._Description = None
        self._RoutingStrategy = None
        self._CreationTime = None
        self._LastUpdatedTime = None
        self._Tags = None

    @property
    def AliasId(self):
        """别名的唯一标识符
        :rtype: str
        """
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId

    @property
    def AliasArn(self):
        """别名的全局唯一资源标识符
        :rtype: str
        """
        return self._AliasArn

    @AliasArn.setter
    def AliasArn(self, AliasArn):
        self._AliasArn = AliasArn

    @property
    def Name(self):
        """名字，长度不小于1字符不超过1024字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """别名的可读说明，长度不小于1字符不超过1024字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RoutingStrategy(self):
        """别名的路由配置
        :rtype: :class:`tencentcloud.gse.v20191112.models.RoutingStrategy`
        """
        return self._RoutingStrategy

    @RoutingStrategy.setter
    def RoutingStrategy(self, RoutingStrategy):
        self._RoutingStrategy = RoutingStrategy

    @property
    def CreationTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LastUpdatedTime(self):
        """上次修改此数据对象的时间
        :rtype: str
        """
        return self._LastUpdatedTime

    @LastUpdatedTime.setter
    def LastUpdatedTime(self, LastUpdatedTime):
        self._LastUpdatedTime = LastUpdatedTime

    @property
    def Tags(self):
        """标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        self._AliasArn = params.get("AliasArn")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("RoutingStrategy") is not None:
            self._RoutingStrategy = RoutingStrategy()
            self._RoutingStrategy._deserialize(params.get("RoutingStrategy"))
        self._CreationTime = params.get("CreationTime")
        self._LastUpdatedTime = params.get("LastUpdatedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Asset(AbstractModel):
    """生成包信息

    """

    def __init__(self):
        r"""
        :param _AssetId: 生成包ID
        :type AssetId: str
        :param _AssetName: 生成包名字，最小长度为1，最大长度为64
        :type AssetName: str
        :param _AssetVersion: 生成包版本，最小长度为1，最大长度为64
        :type AssetVersion: str
        :param _OperateSystem: 生成包可运行的操作系统，暂时只支持CentOS7.16
        :type OperateSystem: str
        :param _Stauts: 生成包状态，0代表上传中，1代表上传失败，2代表上传成功
        :type Stauts: int
        :param _Size: 生成包大小
        :type Size: str
        :param _CreateTime: 生成包创建时间
        :type CreateTime: str
        :param _BindFleetNum: 生成包绑定的Fleet个数，最小值为0
        :type BindFleetNum: int
        :param _AssetArn: 生成包的全局唯一资源标识符
        :type AssetArn: str
        :param _ImageId: 生成包支持的操作系统镜像id
        :type ImageId: str
        :param _OsType: 生成包支持的操作系统类型
        :type OsType: str
        :param _ResourceType: 生成包资源类型，ASSET 或者 IMAGE；ASSET 代表是原有生成包类型，IMAGE 为扩充使用镜像类型
        :type ResourceType: str
        :param _SharingStatus: 镜像资源共享类型，当 ResourceType 为 IMAGE 时该字段有意义，SHARED 表示共享、SHARED_IMAGE 表示未共享；ResourceType 为 ASSET 时这里返回 UNKNOWN_SHARED 用于占位
        :type SharingStatus: str
        :param _Tags: 标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetVersion = None
        self._OperateSystem = None
        self._Stauts = None
        self._Size = None
        self._CreateTime = None
        self._BindFleetNum = None
        self._AssetArn = None
        self._ImageId = None
        self._OsType = None
        self._ResourceType = None
        self._SharingStatus = None
        self._Tags = None

    @property
    def AssetId(self):
        """生成包ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        """生成包名字，最小长度为1，最大长度为64
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetVersion(self):
        """生成包版本，最小长度为1，最大长度为64
        :rtype: str
        """
        return self._AssetVersion

    @AssetVersion.setter
    def AssetVersion(self, AssetVersion):
        self._AssetVersion = AssetVersion

    @property
    def OperateSystem(self):
        """生成包可运行的操作系统，暂时只支持CentOS7.16
        :rtype: str
        """
        return self._OperateSystem

    @OperateSystem.setter
    def OperateSystem(self, OperateSystem):
        self._OperateSystem = OperateSystem

    @property
    def Stauts(self):
        """生成包状态，0代表上传中，1代表上传失败，2代表上传成功
        :rtype: int
        """
        return self._Stauts

    @Stauts.setter
    def Stauts(self, Stauts):
        self._Stauts = Stauts

    @property
    def Size(self):
        """生成包大小
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def CreateTime(self):
        """生成包创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BindFleetNum(self):
        """生成包绑定的Fleet个数，最小值为0
        :rtype: int
        """
        return self._BindFleetNum

    @BindFleetNum.setter
    def BindFleetNum(self, BindFleetNum):
        self._BindFleetNum = BindFleetNum

    @property
    def AssetArn(self):
        """生成包的全局唯一资源标识符
        :rtype: str
        """
        return self._AssetArn

    @AssetArn.setter
    def AssetArn(self, AssetArn):
        self._AssetArn = AssetArn

    @property
    def ImageId(self):
        """生成包支持的操作系统镜像id
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def OsType(self):
        """生成包支持的操作系统类型
        :rtype: str
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def ResourceType(self):
        """生成包资源类型，ASSET 或者 IMAGE；ASSET 代表是原有生成包类型，IMAGE 为扩充使用镜像类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def SharingStatus(self):
        """镜像资源共享类型，当 ResourceType 为 IMAGE 时该字段有意义，SHARED 表示共享、SHARED_IMAGE 表示未共享；ResourceType 为 ASSET 时这里返回 UNKNOWN_SHARED 用于占位
        :rtype: str
        """
        return self._SharingStatus

    @SharingStatus.setter
    def SharingStatus(self, SharingStatus):
        self._SharingStatus = SharingStatus

    @property
    def Tags(self):
        """标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetVersion = params.get("AssetVersion")
        self._OperateSystem = params.get("OperateSystem")
        self._Stauts = params.get("Stauts")
        self._Size = params.get("Size")
        self._CreateTime = params.get("CreateTime")
        self._BindFleetNum = params.get("BindFleetNum")
        self._AssetArn = params.get("AssetArn")
        self._ImageId = params.get("ImageId")
        self._OsType = params.get("OsType")
        self._ResourceType = params.get("ResourceType")
        self._SharingStatus = params.get("SharingStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetCredentials(AbstractModel):
    """上传Asset的临时证书

    """

    def __init__(self):
        r"""
        :param _TmpSecretId: 临时证书密钥ID
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时证书密钥Key
        :type TmpSecretKey: str
        :param _Token: 临时证书Token
        :type Token: str
        """
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._Token = None

    @property
    def TmpSecretId(self):
        """临时证书密钥ID
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """临时证书密钥Key
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def Token(self):
        """临时证书Token
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetSupportSys(AbstractModel):
    """生成包支持操作系统详细信息

    """

    def __init__(self):
        r"""
        :param _ImageId: 生成包操作系统的镜像Id
        :type ImageId: str
        :param _OsType: 生成包操作系统的类型
        :type OsType: str
        :param _OsBit: 生成包操作系统的位数
        :type OsBit: int
        :param _OsVersion: 生成包操作系统的版本
        :type OsVersion: str
        """
        self._ImageId = None
        self._OsType = None
        self._OsBit = None
        self._OsVersion = None

    @property
    def ImageId(self):
        """生成包操作系统的镜像Id
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def OsType(self):
        """生成包操作系统的类型
        :rtype: str
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OsBit(self):
        """生成包操作系统的位数
        :rtype: int
        """
        return self._OsBit

    @OsBit.setter
    def OsBit(self, OsBit):
        self._OsBit = OsBit

    @property
    def OsVersion(self):
        """生成包操作系统的版本
        :rtype: str
        """
        return self._OsVersion

    @OsVersion.setter
    def OsVersion(self, OsVersion):
        self._OsVersion = OsVersion


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._OsType = params.get("OsType")
        self._OsBit = params.get("OsBit")
        self._OsVersion = params.get("OsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCcnInstancesRequest(AbstractModel):
    """AttachCcnInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        :param _AccountId: 云联网账号 Uin
        :type AccountId: str
        :param _CcnId: 云联网 Id
        :type CcnId: str
        """
        self._FleetId = None
        self._AccountId = None
        self._CcnId = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def AccountId(self):
        """云联网账号 Uin
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def CcnId(self):
        """云联网 Id
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._AccountId = params.get("AccountId")
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCcnInstancesResponse(AbstractModel):
    """AttachCcnInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CcnInfo(AbstractModel):
    """云联网相关信息

    """

    def __init__(self):
        r"""
        :param _AccountId: 云联网所属账号
        :type AccountId: str
        :param _CcnId: 云联网id
        :type CcnId: str
        """
        self._AccountId = None
        self._CcnId = None

    @property
    def AccountId(self):
        """云联网所属账号
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def CcnId(self):
        """云联网id
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnInstanceSets(AbstractModel):
    """云联网实例信息

    """

    def __init__(self):
        r"""
        :param _AccountId: 云联网账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountId: str
        :param _CcnId: 云联网 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CcnId: str
        :param _CreateTime: 云联网关联时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _InstanceName: 云联网实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _State: 云联网状态：申请中、已连接、已过期、已拒绝、已删除、失败的、关联中、解关联中、解关联失败
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        """
        self._AccountId = None
        self._CcnId = None
        self._CreateTime = None
        self._InstanceName = None
        self._State = None

    @property
    def AccountId(self):
        """云联网账号 Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def CcnId(self):
        """云联网 Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def CreateTime(self):
        """云联网关联时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def InstanceName(self):
        """云联网实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def State(self):
        """云联网状态：申请中、已连接、已过期、已拒绝、已删除、失败的、关联中、解关联中、解关联失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._CcnId = params.get("CcnId")
        self._CreateTime = params.get("CreateTime")
        self._InstanceName = params.get("InstanceName")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFleetRequest(AbstractModel):
    """CopyFleet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        :param _CopyNumber: 复制数量，最小值1，最大值为剩余配额，可以根据[获取用户配额](https://cloud.tencent.com/document/product/1165/48732)接口获取。
        :type CopyNumber: int
        :param _AssetId: 生成包 Id
        :type AssetId: str
        :param _Description: 描述，最小长度0，最大长度100
        :type Description: str
        :param _InboundPermissions: 网络配置
        :type InboundPermissions: list of InboundPermission
        :param _InstanceType: 服务器类型，参数根据[获取服务器实例类型列表](https://cloud.tencent.com/document/product/1165/48732)接口获取。
        :type InstanceType: str
        :param _FleetType: 服务器舰队类型，目前只支持ON_DEMAND类型
        :type FleetType: str
        :param _Name: 服务器舰队名称，最小长度1，最大长度50
        :type Name: str
        :param _NewGameServerSessionProtectionPolicy: 保护策略：不保护NoProtection、完全保护FullProtection、时限保护TimeLimitProtection
        :type NewGameServerSessionProtectionPolicy: str
        :param _ResourceCreationLimitPolicy: 资源创建限制策略
        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`
        :param _RuntimeConfiguration: 进程配置
        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        :param _GameServerSessionProtectionTimeLimit: 时限保护超时时间，默认60分钟，最小值5，最大值1440；当NewGameSessionProtectionPolicy为TimeLimitProtection时参数有效
        :type GameServerSessionProtectionTimeLimit: int
        :param _SelectedScalingType: 是否选择扩缩容：SCALING_SELECTED 或者 SCALING_UNSELECTED；默认是 SCALING_UNSELECTED
        :type SelectedScalingType: str
        :param _SelectedCcnType: 是否选择云联网：CCN_SELECTED_BEFORE_CREATE（创建前关联）， CCN_SELECTED_AFTER_CREATE（创建后关联）或者 CCN_UNSELECTED（不关联）；默认是 CCN_UNSELECTED
        :type SelectedCcnType: str
        :param _Tags: 标签列表，最大长度50组
        :type Tags: list of Tag
        :param _SystemDiskInfo: 系统盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-500GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，50-500GB；容量以1为单位
        :type SystemDiskInfo: :class:`tencentcloud.gse.v20191112.models.DiskInfo`
        :param _DataDiskInfo: 数据盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-32000GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，10-32000GB；容量以10为单位
        :type DataDiskInfo: list of DiskInfo
        :param _SelectedTimerType: 是否选择复制定时器策略：TIMER_SELECTED 或者 TIMER_UNSELECTED；默认是 TIMER_UNSELECTED
        :type SelectedTimerType: str
        :param _CcnInfos: 云联网信息，包含对应的账号信息及所属id
        :type CcnInfos: list of CcnInfo
        :param _InternetMaxBandwidthOut: fleet公网出带宽最大值，默认100Mbps，范围1-200Mbps
        :type InternetMaxBandwidthOut: int
        """
        self._FleetId = None
        self._CopyNumber = None
        self._AssetId = None
        self._Description = None
        self._InboundPermissions = None
        self._InstanceType = None
        self._FleetType = None
        self._Name = None
        self._NewGameServerSessionProtectionPolicy = None
        self._ResourceCreationLimitPolicy = None
        self._RuntimeConfiguration = None
        self._GameServerSessionProtectionTimeLimit = None
        self._SelectedScalingType = None
        self._SelectedCcnType = None
        self._Tags = None
        self._SystemDiskInfo = None
        self._DataDiskInfo = None
        self._SelectedTimerType = None
        self._CcnInfos = None
        self._InternetMaxBandwidthOut = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def CopyNumber(self):
        """复制数量，最小值1，最大值为剩余配额，可以根据[获取用户配额](https://cloud.tencent.com/document/product/1165/48732)接口获取。
        :rtype: int
        """
        return self._CopyNumber

    @CopyNumber.setter
    def CopyNumber(self, CopyNumber):
        self._CopyNumber = CopyNumber

    @property
    def AssetId(self):
        """生成包 Id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Description(self):
        """描述，最小长度0，最大长度100
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InboundPermissions(self):
        """网络配置
        :rtype: list of InboundPermission
        """
        return self._InboundPermissions

    @InboundPermissions.setter
    def InboundPermissions(self, InboundPermissions):
        self._InboundPermissions = InboundPermissions

    @property
    def InstanceType(self):
        """服务器类型，参数根据[获取服务器实例类型列表](https://cloud.tencent.com/document/product/1165/48732)接口获取。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def FleetType(self):
        """服务器舰队类型，目前只支持ON_DEMAND类型
        :rtype: str
        """
        return self._FleetType

    @FleetType.setter
    def FleetType(self, FleetType):
        self._FleetType = FleetType

    @property
    def Name(self):
        """服务器舰队名称，最小长度1，最大长度50
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NewGameServerSessionProtectionPolicy(self):
        """保护策略：不保护NoProtection、完全保护FullProtection、时限保护TimeLimitProtection
        :rtype: str
        """
        return self._NewGameServerSessionProtectionPolicy

    @NewGameServerSessionProtectionPolicy.setter
    def NewGameServerSessionProtectionPolicy(self, NewGameServerSessionProtectionPolicy):
        self._NewGameServerSessionProtectionPolicy = NewGameServerSessionProtectionPolicy

    @property
    def ResourceCreationLimitPolicy(self):
        """资源创建限制策略
        :rtype: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`
        """
        return self._ResourceCreationLimitPolicy

    @ResourceCreationLimitPolicy.setter
    def ResourceCreationLimitPolicy(self, ResourceCreationLimitPolicy):
        self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy

    @property
    def RuntimeConfiguration(self):
        """进程配置
        :rtype: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        """
        return self._RuntimeConfiguration

    @RuntimeConfiguration.setter
    def RuntimeConfiguration(self, RuntimeConfiguration):
        self._RuntimeConfiguration = RuntimeConfiguration

    @property
    def GameServerSessionProtectionTimeLimit(self):
        """时限保护超时时间，默认60分钟，最小值5，最大值1440；当NewGameSessionProtectionPolicy为TimeLimitProtection时参数有效
        :rtype: int
        """
        return self._GameServerSessionProtectionTimeLimit

    @GameServerSessionProtectionTimeLimit.setter
    def GameServerSessionProtectionTimeLimit(self, GameServerSessionProtectionTimeLimit):
        self._GameServerSessionProtectionTimeLimit = GameServerSessionProtectionTimeLimit

    @property
    def SelectedScalingType(self):
        """是否选择扩缩容：SCALING_SELECTED 或者 SCALING_UNSELECTED；默认是 SCALING_UNSELECTED
        :rtype: str
        """
        return self._SelectedScalingType

    @SelectedScalingType.setter
    def SelectedScalingType(self, SelectedScalingType):
        self._SelectedScalingType = SelectedScalingType

    @property
    def SelectedCcnType(self):
        """是否选择云联网：CCN_SELECTED_BEFORE_CREATE（创建前关联）， CCN_SELECTED_AFTER_CREATE（创建后关联）或者 CCN_UNSELECTED（不关联）；默认是 CCN_UNSELECTED
        :rtype: str
        """
        return self._SelectedCcnType

    @SelectedCcnType.setter
    def SelectedCcnType(self, SelectedCcnType):
        self._SelectedCcnType = SelectedCcnType

    @property
    def Tags(self):
        """标签列表，最大长度50组
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SystemDiskInfo(self):
        """系统盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-500GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，50-500GB；容量以1为单位
        :rtype: :class:`tencentcloud.gse.v20191112.models.DiskInfo`
        """
        return self._SystemDiskInfo

    @SystemDiskInfo.setter
    def SystemDiskInfo(self, SystemDiskInfo):
        self._SystemDiskInfo = SystemDiskInfo

    @property
    def DataDiskInfo(self):
        """数据盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-32000GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，10-32000GB；容量以10为单位
        :rtype: list of DiskInfo
        """
        return self._DataDiskInfo

    @DataDiskInfo.setter
    def DataDiskInfo(self, DataDiskInfo):
        self._DataDiskInfo = DataDiskInfo

    @property
    def SelectedTimerType(self):
        """是否选择复制定时器策略：TIMER_SELECTED 或者 TIMER_UNSELECTED；默认是 TIMER_UNSELECTED
        :rtype: str
        """
        return self._SelectedTimerType

    @SelectedTimerType.setter
    def SelectedTimerType(self, SelectedTimerType):
        self._SelectedTimerType = SelectedTimerType

    @property
    def CcnInfos(self):
        """云联网信息，包含对应的账号信息及所属id
        :rtype: list of CcnInfo
        """
        return self._CcnInfos

    @CcnInfos.setter
    def CcnInfos(self, CcnInfos):
        self._CcnInfos = CcnInfos

    @property
    def InternetMaxBandwidthOut(self):
        """fleet公网出带宽最大值，默认100Mbps，范围1-200Mbps
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._CopyNumber = params.get("CopyNumber")
        self._AssetId = params.get("AssetId")
        self._Description = params.get("Description")
        if params.get("InboundPermissions") is not None:
            self._InboundPermissions = []
            for item in params.get("InboundPermissions"):
                obj = InboundPermission()
                obj._deserialize(item)
                self._InboundPermissions.append(obj)
        self._InstanceType = params.get("InstanceType")
        self._FleetType = params.get("FleetType")
        self._Name = params.get("Name")
        self._NewGameServerSessionProtectionPolicy = params.get("NewGameServerSessionProtectionPolicy")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self._ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        if params.get("RuntimeConfiguration") is not None:
            self._RuntimeConfiguration = RuntimeConfiguration()
            self._RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        self._GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        self._SelectedScalingType = params.get("SelectedScalingType")
        self._SelectedCcnType = params.get("SelectedCcnType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("SystemDiskInfo") is not None:
            self._SystemDiskInfo = DiskInfo()
            self._SystemDiskInfo._deserialize(params.get("SystemDiskInfo"))
        if params.get("DataDiskInfo") is not None:
            self._DataDiskInfo = []
            for item in params.get("DataDiskInfo"):
                obj = DiskInfo()
                obj._deserialize(item)
                self._DataDiskInfo.append(obj)
        self._SelectedTimerType = params.get("SelectedTimerType")
        if params.get("CcnInfos") is not None:
            self._CcnInfos = []
            for item in params.get("CcnInfos"):
                obj = CcnInfo()
                obj._deserialize(item)
                self._CcnInfos.append(obj)
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFleetResponse(AbstractModel):
    """CopyFleet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetAttributes: 服务器舰队属性
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetAttributes: list of FleetAttributes
        :param _TotalCount: 服务器舰队数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetAttributes = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FleetAttributes(self):
        """服务器舰队属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FleetAttributes
        """
        return self._FleetAttributes

    @FleetAttributes.setter
    def FleetAttributes(self, FleetAttributes):
        self._FleetAttributes = FleetAttributes

    @property
    def TotalCount(self):
        """服务器舰队数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FleetAttributes") is not None:
            self._FleetAttributes = []
            for item in params.get("FleetAttributes"):
                obj = FleetAttributes()
                obj._deserialize(item)
                self._FleetAttributes.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class CreateAliasRequest(AbstractModel):
    """CreateAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名字，长度不小于1字符不超过1024字符
        :type Name: str
        :param _RoutingStrategy: 别名的路由配置
        :type RoutingStrategy: :class:`tencentcloud.gse.v20191112.models.RoutingStrategy`
        :param _Description: 别名的可读说明，长度不小于1字符不超过1024字符
        :type Description: str
        :param _Tags: 标签列表，最大长度50组
        :type Tags: list of Tag
        """
        self._Name = None
        self._RoutingStrategy = None
        self._Description = None
        self._Tags = None

    @property
    def Name(self):
        """名字，长度不小于1字符不超过1024字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoutingStrategy(self):
        """别名的路由配置
        :rtype: :class:`tencentcloud.gse.v20191112.models.RoutingStrategy`
        """
        return self._RoutingStrategy

    @RoutingStrategy.setter
    def RoutingStrategy(self, RoutingStrategy):
        self._RoutingStrategy = RoutingStrategy

    @property
    def Description(self):
        """别名的可读说明，长度不小于1字符不超过1024字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        """标签列表，最大长度50组
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("RoutingStrategy") is not None:
            self._RoutingStrategy = RoutingStrategy()
            self._RoutingStrategy._deserialize(params.get("RoutingStrategy"))
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAliasResponse(AbstractModel):
    """CreateAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Alias: 别名对象
        :type Alias: :class:`tencentcloud.gse.v20191112.models.Alias`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Alias = None
        self._RequestId = None

    @property
    def Alias(self):
        """别名对象
        :rtype: :class:`tencentcloud.gse.v20191112.models.Alias`
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Alias") is not None:
            self._Alias = Alias()
            self._Alias._deserialize(params.get("Alias"))
        self._RequestId = params.get("RequestId")


class CreateAssetRequest(AbstractModel):
    """CreateAsset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BucketKey: 生成包的ZIP包名，例如：server.zip
        :type BucketKey: str
        :param _AssetName: 生成包名字，最小长度为1，最大长度为64
        :type AssetName: str
        :param _AssetVersion: 生成包版本，最小长度为1，最大长度为64
        :type AssetVersion: str
        :param _AssetRegion: 生成包所在地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)
        :type AssetRegion: str
        :param _OperateSystem: 生成包可运行的操作系统，若传入参数为CentOS7.16则不需要传入ImageId字段，否则，需要传入Imageid字段（该方式是为了兼容之前的版本，后续建议使用ImageId来替代该字段）。这里可通过[DescribeAssetSystems](https://cloud.tencent.com/document/product/1165/49191)接口获取asset支持的操作系统进行传入（使用AssetSupportSys的OsVersion字段）
        :type OperateSystem: str
        :param _ImageId: 生成包支持的操作系统镜像id，若传入OperateSystem字段的值是CentOS7.16，则不需要传入该值；如果不是，则需要通过[DescribeAssetSystems](https://cloud.tencent.com/document/product/1165/49191)接口获取asset支持的操作系统ImageId进行传入
        :type ImageId: str
        :param _Tags: 标签列表，最大长度50组
        :type Tags: list of Tag
        """
        self._BucketKey = None
        self._AssetName = None
        self._AssetVersion = None
        self._AssetRegion = None
        self._OperateSystem = None
        self._ImageId = None
        self._Tags = None

    @property
    def BucketKey(self):
        """生成包的ZIP包名，例如：server.zip
        :rtype: str
        """
        return self._BucketKey

    @BucketKey.setter
    def BucketKey(self, BucketKey):
        self._BucketKey = BucketKey

    @property
    def AssetName(self):
        """生成包名字，最小长度为1，最大长度为64
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetVersion(self):
        """生成包版本，最小长度为1，最大长度为64
        :rtype: str
        """
        return self._AssetVersion

    @AssetVersion.setter
    def AssetVersion(self, AssetVersion):
        self._AssetVersion = AssetVersion

    @property
    def AssetRegion(self):
        """生成包所在地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)
        :rtype: str
        """
        return self._AssetRegion

    @AssetRegion.setter
    def AssetRegion(self, AssetRegion):
        self._AssetRegion = AssetRegion

    @property
    def OperateSystem(self):
        """生成包可运行的操作系统，若传入参数为CentOS7.16则不需要传入ImageId字段，否则，需要传入Imageid字段（该方式是为了兼容之前的版本，后续建议使用ImageId来替代该字段）。这里可通过[DescribeAssetSystems](https://cloud.tencent.com/document/product/1165/49191)接口获取asset支持的操作系统进行传入（使用AssetSupportSys的OsVersion字段）
        :rtype: str
        """
        return self._OperateSystem

    @OperateSystem.setter
    def OperateSystem(self, OperateSystem):
        self._OperateSystem = OperateSystem

    @property
    def ImageId(self):
        """生成包支持的操作系统镜像id，若传入OperateSystem字段的值是CentOS7.16，则不需要传入该值；如果不是，则需要通过[DescribeAssetSystems](https://cloud.tencent.com/document/product/1165/49191)接口获取asset支持的操作系统ImageId进行传入
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Tags(self):
        """标签列表，最大长度50组
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._BucketKey = params.get("BucketKey")
        self._AssetName = params.get("AssetName")
        self._AssetVersion = params.get("AssetVersion")
        self._AssetRegion = params.get("AssetRegion")
        self._OperateSystem = params.get("OperateSystem")
        self._ImageId = params.get("ImageId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetResponse(AbstractModel):
    """CreateAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 生成包ID
        :type AssetId: str
        :param _AssetArn: 生成包的全局唯一资源标识符
        :type AssetArn: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AssetId = None
        self._AssetArn = None
        self._RequestId = None

    @property
    def AssetId(self):
        """生成包ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetArn(self):
        """生成包的全局唯一资源标识符
        :rtype: str
        """
        return self._AssetArn

    @AssetArn.setter
    def AssetArn(self, AssetArn):
        self._AssetArn = AssetArn

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetArn = params.get("AssetArn")
        self._RequestId = params.get("RequestId")


class CreateAssetWithImageRequest(AbstractModel):
    """CreateAssetWithImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetName: 生成包名字，最小长度为1，最大长度为64
        :type AssetName: str
        :param _AssetVersion: 生成包版本，最小长度为1，最大长度为64
        :type AssetVersion: str
        :param _AssetRegion: 生成包所在地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)
        :type AssetRegion: str
        :param _ImageId: 生成包支持的操作系统镜像id
        :type ImageId: str
        :param _ImageSize: 操作系统镜像包大小，比如：40GB，支持单位 KB、MB、GB
        :type ImageSize: str
        :param _ImageOs: 操作系统镜像包名称，最小长度为1，最大长度为64
        :type ImageOs: str
        :param _OsType: 操作系统镜像包类型，CentOS 或者 Windows
        :type OsType: str
        :param _ImageType: 操作系统镜像包类型，当前只支持 SHARED_IMAGE
        :type ImageType: str
        :param _OsBit: 操作系统镜像包位数，32 或者 64
        :type OsBit: int
        """
        self._AssetName = None
        self._AssetVersion = None
        self._AssetRegion = None
        self._ImageId = None
        self._ImageSize = None
        self._ImageOs = None
        self._OsType = None
        self._ImageType = None
        self._OsBit = None

    @property
    def AssetName(self):
        """生成包名字，最小长度为1，最大长度为64
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetVersion(self):
        """生成包版本，最小长度为1，最大长度为64
        :rtype: str
        """
        return self._AssetVersion

    @AssetVersion.setter
    def AssetVersion(self, AssetVersion):
        self._AssetVersion = AssetVersion

    @property
    def AssetRegion(self):
        """生成包所在地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)
        :rtype: str
        """
        return self._AssetRegion

    @AssetRegion.setter
    def AssetRegion(self, AssetRegion):
        self._AssetRegion = AssetRegion

    @property
    def ImageId(self):
        """生成包支持的操作系统镜像id
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageSize(self):
        """操作系统镜像包大小，比如：40GB，支持单位 KB、MB、GB
        :rtype: str
        """
        return self._ImageSize

    @ImageSize.setter
    def ImageSize(self, ImageSize):
        self._ImageSize = ImageSize

    @property
    def ImageOs(self):
        """操作系统镜像包名称，最小长度为1，最大长度为64
        :rtype: str
        """
        return self._ImageOs

    @ImageOs.setter
    def ImageOs(self, ImageOs):
        self._ImageOs = ImageOs

    @property
    def OsType(self):
        """操作系统镜像包类型，CentOS 或者 Windows
        :rtype: str
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def ImageType(self):
        """操作系统镜像包类型，当前只支持 SHARED_IMAGE
        :rtype: str
        """
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def OsBit(self):
        """操作系统镜像包位数，32 或者 64
        :rtype: int
        """
        return self._OsBit

    @OsBit.setter
    def OsBit(self, OsBit):
        self._OsBit = OsBit


    def _deserialize(self, params):
        self._AssetName = params.get("AssetName")
        self._AssetVersion = params.get("AssetVersion")
        self._AssetRegion = params.get("AssetRegion")
        self._ImageId = params.get("ImageId")
        self._ImageSize = params.get("ImageSize")
        self._ImageOs = params.get("ImageOs")
        self._OsType = params.get("OsType")
        self._ImageType = params.get("ImageType")
        self._OsBit = params.get("OsBit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetWithImageResponse(AbstractModel):
    """CreateAssetWithImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 生成包ID
        :type AssetId: str
        :param _AssetArn: 生成包的全局唯一资源标识符
        :type AssetArn: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AssetId = None
        self._AssetArn = None
        self._RequestId = None

    @property
    def AssetId(self):
        """生成包ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetArn(self):
        """生成包的全局唯一资源标识符
        :rtype: str
        """
        return self._AssetArn

    @AssetArn.setter
    def AssetArn(self, AssetArn):
        self._AssetArn = AssetArn

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetArn = params.get("AssetArn")
        self._RequestId = params.get("RequestId")


class CreateFleetRequest(AbstractModel):
    """CreateFleet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 生成包 Id
        :type AssetId: str
        :param _Description: 描述，最小长度0，最大长度100
        :type Description: str
        :param _InboundPermissions: 网络配置
        :type InboundPermissions: list of InboundPermission
        :param _InstanceType: 服务器类型，参数根据[获取服务器实例类型列表](https://cloud.tencent.com/document/product/1165/48732)接口获取。
        :type InstanceType: str
        :param _FleetType: 服务器舰队类型，目前只支持ON_DEMAND类型
        :type FleetType: str
        :param _Name: 服务器舰队名称，最小长度1，最大长度50
        :type Name: str
        :param _NewGameServerSessionProtectionPolicy: 保护策略：不保护NoProtection、完全保护FullProtection、时限保护TimeLimitProtection
        :type NewGameServerSessionProtectionPolicy: str
        :param _PeerVpcId: VPC 网络 Id，对等连接已不再使用
        :type PeerVpcId: str
        :param _ResourceCreationLimitPolicy: 资源创建限制策略
        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`
        :param _RuntimeConfiguration: 进程配置
        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        :param _SubNetId: VPC 子网，对等连接已不再使用
        :type SubNetId: str
        :param _GameServerSessionProtectionTimeLimit: 时限保护超时时间，默认60分钟，最小值5，最大值1440；当NewGameSessionProtectionPolicy为TimeLimitProtection时参数有效
        :type GameServerSessionProtectionTimeLimit: int
        :param _Tags: 标签列表，最大长度50组
        :type Tags: list of Tag
        :param _SystemDiskInfo: 系统盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-500GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，50-500GB；容量以1为单位
        :type SystemDiskInfo: :class:`tencentcloud.gse.v20191112.models.DiskInfo`
        :param _DataDiskInfo: 数据盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-32000GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，10-32000GB；容量以10为单位
        :type DataDiskInfo: list of DiskInfo
        :param _CcnInfos: 云联网信息，包含对应的账号信息及所属id
        :type CcnInfos: list of CcnInfo
        :param _InternetMaxBandwidthOut: fleet公网出带宽最大值，默认100Mbps，范围1-200Mbps
        :type InternetMaxBandwidthOut: int
        """
        self._AssetId = None
        self._Description = None
        self._InboundPermissions = None
        self._InstanceType = None
        self._FleetType = None
        self._Name = None
        self._NewGameServerSessionProtectionPolicy = None
        self._PeerVpcId = None
        self._ResourceCreationLimitPolicy = None
        self._RuntimeConfiguration = None
        self._SubNetId = None
        self._GameServerSessionProtectionTimeLimit = None
        self._Tags = None
        self._SystemDiskInfo = None
        self._DataDiskInfo = None
        self._CcnInfos = None
        self._InternetMaxBandwidthOut = None

    @property
    def AssetId(self):
        """生成包 Id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Description(self):
        """描述，最小长度0，最大长度100
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InboundPermissions(self):
        """网络配置
        :rtype: list of InboundPermission
        """
        return self._InboundPermissions

    @InboundPermissions.setter
    def InboundPermissions(self, InboundPermissions):
        self._InboundPermissions = InboundPermissions

    @property
    def InstanceType(self):
        """服务器类型，参数根据[获取服务器实例类型列表](https://cloud.tencent.com/document/product/1165/48732)接口获取。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def FleetType(self):
        """服务器舰队类型，目前只支持ON_DEMAND类型
        :rtype: str
        """
        return self._FleetType

    @FleetType.setter
    def FleetType(self, FleetType):
        self._FleetType = FleetType

    @property
    def Name(self):
        """服务器舰队名称，最小长度1，最大长度50
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NewGameServerSessionProtectionPolicy(self):
        """保护策略：不保护NoProtection、完全保护FullProtection、时限保护TimeLimitProtection
        :rtype: str
        """
        return self._NewGameServerSessionProtectionPolicy

    @NewGameServerSessionProtectionPolicy.setter
    def NewGameServerSessionProtectionPolicy(self, NewGameServerSessionProtectionPolicy):
        self._NewGameServerSessionProtectionPolicy = NewGameServerSessionProtectionPolicy

    @property
    def PeerVpcId(self):
        """VPC 网络 Id，对等连接已不再使用
        :rtype: str
        """
        return self._PeerVpcId

    @PeerVpcId.setter
    def PeerVpcId(self, PeerVpcId):
        self._PeerVpcId = PeerVpcId

    @property
    def ResourceCreationLimitPolicy(self):
        """资源创建限制策略
        :rtype: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`
        """
        return self._ResourceCreationLimitPolicy

    @ResourceCreationLimitPolicy.setter
    def ResourceCreationLimitPolicy(self, ResourceCreationLimitPolicy):
        self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy

    @property
    def RuntimeConfiguration(self):
        """进程配置
        :rtype: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        """
        return self._RuntimeConfiguration

    @RuntimeConfiguration.setter
    def RuntimeConfiguration(self, RuntimeConfiguration):
        self._RuntimeConfiguration = RuntimeConfiguration

    @property
    def SubNetId(self):
        """VPC 子网，对等连接已不再使用
        :rtype: str
        """
        return self._SubNetId

    @SubNetId.setter
    def SubNetId(self, SubNetId):
        self._SubNetId = SubNetId

    @property
    def GameServerSessionProtectionTimeLimit(self):
        """时限保护超时时间，默认60分钟，最小值5，最大值1440；当NewGameSessionProtectionPolicy为TimeLimitProtection时参数有效
        :rtype: int
        """
        return self._GameServerSessionProtectionTimeLimit

    @GameServerSessionProtectionTimeLimit.setter
    def GameServerSessionProtectionTimeLimit(self, GameServerSessionProtectionTimeLimit):
        self._GameServerSessionProtectionTimeLimit = GameServerSessionProtectionTimeLimit

    @property
    def Tags(self):
        """标签列表，最大长度50组
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SystemDiskInfo(self):
        """系统盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-500GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，50-500GB；容量以1为单位
        :rtype: :class:`tencentcloud.gse.v20191112.models.DiskInfo`
        """
        return self._SystemDiskInfo

    @SystemDiskInfo.setter
    def SystemDiskInfo(self, SystemDiskInfo):
        self._SystemDiskInfo = SystemDiskInfo

    @property
    def DataDiskInfo(self):
        """数据盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-32000GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，10-32000GB；容量以10为单位
        :rtype: list of DiskInfo
        """
        return self._DataDiskInfo

    @DataDiskInfo.setter
    def DataDiskInfo(self, DataDiskInfo):
        self._DataDiskInfo = DataDiskInfo

    @property
    def CcnInfos(self):
        """云联网信息，包含对应的账号信息及所属id
        :rtype: list of CcnInfo
        """
        return self._CcnInfos

    @CcnInfos.setter
    def CcnInfos(self, CcnInfos):
        self._CcnInfos = CcnInfos

    @property
    def InternetMaxBandwidthOut(self):
        """fleet公网出带宽最大值，默认100Mbps，范围1-200Mbps
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._Description = params.get("Description")
        if params.get("InboundPermissions") is not None:
            self._InboundPermissions = []
            for item in params.get("InboundPermissions"):
                obj = InboundPermission()
                obj._deserialize(item)
                self._InboundPermissions.append(obj)
        self._InstanceType = params.get("InstanceType")
        self._FleetType = params.get("FleetType")
        self._Name = params.get("Name")
        self._NewGameServerSessionProtectionPolicy = params.get("NewGameServerSessionProtectionPolicy")
        self._PeerVpcId = params.get("PeerVpcId")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self._ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        if params.get("RuntimeConfiguration") is not None:
            self._RuntimeConfiguration = RuntimeConfiguration()
            self._RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        self._SubNetId = params.get("SubNetId")
        self._GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("SystemDiskInfo") is not None:
            self._SystemDiskInfo = DiskInfo()
            self._SystemDiskInfo._deserialize(params.get("SystemDiskInfo"))
        if params.get("DataDiskInfo") is not None:
            self._DataDiskInfo = []
            for item in params.get("DataDiskInfo"):
                obj = DiskInfo()
                obj._deserialize(item)
                self._DataDiskInfo.append(obj)
        if params.get("CcnInfos") is not None:
            self._CcnInfos = []
            for item in params.get("CcnInfos"):
                obj = CcnInfo()
                obj._deserialize(item)
                self._CcnInfos.append(obj)
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFleetResponse(AbstractModel):
    """CreateFleet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetAttributes: 服务器舰队属性
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetAttributes: :class:`tencentcloud.gse.v20191112.models.FleetAttributes`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetAttributes = None
        self._RequestId = None

    @property
    def FleetAttributes(self):
        """服务器舰队属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.FleetAttributes`
        """
        return self._FleetAttributes

    @FleetAttributes.setter
    def FleetAttributes(self, FleetAttributes):
        self._FleetAttributes = FleetAttributes

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FleetAttributes") is not None:
            self._FleetAttributes = FleetAttributes()
            self._FleetAttributes._deserialize(params.get("FleetAttributes"))
        self._RequestId = params.get("RequestId")


class CreateGameServerSessionQueueRequest(AbstractModel):
    """CreateGameServerSessionQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 游戏服务器会话队列名称，长度1~128
        :type Name: str
        :param _Destinations: 目的服务器舰队（可为别名）列表
        :type Destinations: list of GameServerSessionQueueDestination
        :param _PlayerLatencyPolicies: 延迟策略集合
        :type PlayerLatencyPolicies: list of PlayerLatencyPolicy
        :param _TimeoutInSeconds: 超时时间（单位秒，默认值为600秒）
        :type TimeoutInSeconds: int
        :param _Tags: 标签列表，最大长度50组
        :type Tags: list of Tag
        """
        self._Name = None
        self._Destinations = None
        self._PlayerLatencyPolicies = None
        self._TimeoutInSeconds = None
        self._Tags = None

    @property
    def Name(self):
        """游戏服务器会话队列名称，长度1~128
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Destinations(self):
        """目的服务器舰队（可为别名）列表
        :rtype: list of GameServerSessionQueueDestination
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def PlayerLatencyPolicies(self):
        """延迟策略集合
        :rtype: list of PlayerLatencyPolicy
        """
        return self._PlayerLatencyPolicies

    @PlayerLatencyPolicies.setter
    def PlayerLatencyPolicies(self, PlayerLatencyPolicies):
        self._PlayerLatencyPolicies = PlayerLatencyPolicies

    @property
    def TimeoutInSeconds(self):
        """超时时间（单位秒，默认值为600秒）
        :rtype: int
        """
        return self._TimeoutInSeconds

    @TimeoutInSeconds.setter
    def TimeoutInSeconds(self, TimeoutInSeconds):
        self._TimeoutInSeconds = TimeoutInSeconds

    @property
    def Tags(self):
        """标签列表，最大长度50组
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = GameServerSessionQueueDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        if params.get("PlayerLatencyPolicies") is not None:
            self._PlayerLatencyPolicies = []
            for item in params.get("PlayerLatencyPolicies"):
                obj = PlayerLatencyPolicy()
                obj._deserialize(item)
                self._PlayerLatencyPolicies.append(obj)
        self._TimeoutInSeconds = params.get("TimeoutInSeconds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGameServerSessionQueueResponse(AbstractModel):
    """CreateGameServerSessionQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionQueue: 游戏服务器会话队列
        :type GameServerSessionQueue: :class:`tencentcloud.gse.v20191112.models.GameServerSessionQueue`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSessionQueue = None
        self._RequestId = None

    @property
    def GameServerSessionQueue(self):
        """游戏服务器会话队列
        :rtype: :class:`tencentcloud.gse.v20191112.models.GameServerSessionQueue`
        """
        return self._GameServerSessionQueue

    @GameServerSessionQueue.setter
    def GameServerSessionQueue(self, GameServerSessionQueue):
        self._GameServerSessionQueue = GameServerSessionQueue

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionQueue") is not None:
            self._GameServerSessionQueue = GameServerSessionQueue()
            self._GameServerSessionQueue._deserialize(params.get("GameServerSessionQueue"))
        self._RequestId = params.get("RequestId")


class CreateGameServerSessionRequest(AbstractModel):
    """CreateGameServerSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MaximumPlayerSessionCount: 最大玩家数量，最小值不小于0
        :type MaximumPlayerSessionCount: int
        :param _AliasId: 别名ID。每个请求需要指定别名ID 或者舰队 ID，如果两个同时指定时，优先选择舰队 ID
        :type AliasId: str
        :param _CreatorId: 创建者ID，最大长度不超过1024个ASCII字符
        :type CreatorId: str
        :param _FleetId: 舰队ID。每个请求需要指定别名ID 或者舰队 ID，如果两个同时指定时，优先选择舰队 ID
        :type FleetId: str
        :param _GameProperties: 游戏属性，最大长度不超过16组
        :type GameProperties: list of GameProperty
        :param _GameServerSessionData: 游戏服务器会话属性详情，最大长度不超过4096个ASCII字符
        :type GameServerSessionData: str
        :param _GameServerSessionId: 游戏服务器会话自定义ID，最大长度不超过4096个ASCII字符
        :type GameServerSessionId: str
        :param _IdempotencyToken: 幂等token，最大长度不超过48个ASCII字符
        :type IdempotencyToken: str
        :param _Name: 游戏服务器会话名称，最大长度不超过1024个ASCII字符
        :type Name: str
        """
        self._MaximumPlayerSessionCount = None
        self._AliasId = None
        self._CreatorId = None
        self._FleetId = None
        self._GameProperties = None
        self._GameServerSessionData = None
        self._GameServerSessionId = None
        self._IdempotencyToken = None
        self._Name = None

    @property
    def MaximumPlayerSessionCount(self):
        """最大玩家数量，最小值不小于0
        :rtype: int
        """
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount

    @property
    def AliasId(self):
        """别名ID。每个请求需要指定别名ID 或者舰队 ID，如果两个同时指定时，优先选择舰队 ID
        :rtype: str
        """
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId

    @property
    def CreatorId(self):
        """创建者ID，最大长度不超过1024个ASCII字符
        :rtype: str
        """
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def FleetId(self):
        """舰队ID。每个请求需要指定别名ID 或者舰队 ID，如果两个同时指定时，优先选择舰队 ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def GameProperties(self):
        """游戏属性，最大长度不超过16组
        :rtype: list of GameProperty
        """
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def GameServerSessionData(self):
        """游戏服务器会话属性详情，最大长度不超过4096个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionData

    @GameServerSessionData.setter
    def GameServerSessionData(self, GameServerSessionData):
        self._GameServerSessionData = GameServerSessionData

    @property
    def GameServerSessionId(self):
        """游戏服务器会话自定义ID，最大长度不超过4096个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def IdempotencyToken(self):
        """幂等token，最大长度不超过48个ASCII字符
        :rtype: str
        """
        return self._IdempotencyToken

    @IdempotencyToken.setter
    def IdempotencyToken(self, IdempotencyToken):
        self._IdempotencyToken = IdempotencyToken

    @property
    def Name(self):
        """游戏服务器会话名称，最大长度不超过1024个ASCII字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self._AliasId = params.get("AliasId")
        self._CreatorId = params.get("CreatorId")
        self._FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._GameServerSessionData = params.get("GameServerSessionData")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._IdempotencyToken = params.get("IdempotencyToken")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGameServerSessionResponse(AbstractModel):
    """CreateGameServerSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSession: 游戏服务器会话
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSession = None
        self._RequestId = None

    @property
    def GameServerSession(self):
        """游戏服务器会话
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        """
        return self._GameServerSession

    @GameServerSession.setter
    def GameServerSession(self, GameServerSession):
        self._GameServerSession = GameServerSession

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self._GameServerSession = GameServerSession()
            self._GameServerSession._deserialize(params.get("GameServerSession"))
        self._RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """访问实例所需要的凭据

    """

    def __init__(self):
        r"""
        :param _Secret: ssh私钥
        :type Secret: str
        :param _UserName: 用户名
        :type UserName: str
        """
        self._Secret = None
        self._UserName = None

    @property
    def Secret(self):
        """ssh私钥
        :rtype: str
        """
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret

    @property
    def UserName(self):
        """用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._Secret = params.get("Secret")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasRequest(AbstractModel):
    """DeleteAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AliasId: 要删除的别名ID
        :type AliasId: str
        """
        self._AliasId = None

    @property
    def AliasId(self):
        """要删除的别名ID
        :rtype: str
        """
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasResponse(AbstractModel):
    """DeleteAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteAssetRequest(AbstractModel):
    """DeleteAsset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 生成包ID
        :type AssetId: str
        """
        self._AssetId = None

    @property
    def AssetId(self):
        """生成包ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAssetResponse(AbstractModel):
    """DeleteAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteFleetRequest(AbstractModel):
    """DeleteFleet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        """
        self._FleetId = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFleetResponse(AbstractModel):
    """DeleteFleet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteGameServerSessionQueueRequest(AbstractModel):
    """DeleteGameServerSessionQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 游戏服务器会话队列名字，长度1~128
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """游戏服务器会话队列名字，长度1~128
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGameServerSessionQueueResponse(AbstractModel):
    """DeleteGameServerSessionQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteScalingPolicyRequest(AbstractModel):
    """DeleteScalingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
        :type FleetId: str
        :param _Name: 扩缩容策略名称，最小长度为0，最大长度为1024
        :type Name: str
        """
        self._FleetId = None
        self._Name = None

    @property
    def FleetId(self):
        """服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Name(self):
        """扩缩容策略名称，最小长度为0，最大长度为1024
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScalingPolicyResponse(AbstractModel):
    """DeleteScalingPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTimerScalingPolicyRequest(AbstractModel):
    """DeleteTimerScalingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimerId: 定时器ID, 进行encode
        :type TimerId: str
        :param _FleetId: 扩缩容配置服务器舰队ID
        :type FleetId: str
        :param _TimerName: 定时器名称
        :type TimerName: str
        """
        self._TimerId = None
        self._FleetId = None
        self._TimerName = None

    @property
    def TimerId(self):
        """定时器ID, 进行encode
        :rtype: str
        """
        return self._TimerId

    @TimerId.setter
    def TimerId(self, TimerId):
        self._TimerId = TimerId

    @property
    def FleetId(self):
        """扩缩容配置服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def TimerName(self):
        """定时器名称
        :rtype: str
        """
        return self._TimerName

    @TimerName.setter
    def TimerName(self, TimerName):
        self._TimerName = TimerName


    def _deserialize(self, params):
        self._TimerId = params.get("TimerId")
        self._FleetId = params.get("FleetId")
        self._TimerName = params.get("TimerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimerScalingPolicyResponse(AbstractModel):
    """DeleteTimerScalingPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAliasRequest(AbstractModel):
    """DescribeAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AliasId: 要检索的队列别名的唯一标识符
        :type AliasId: str
        """
        self._AliasId = None

    @property
    def AliasId(self):
        """要检索的队列别名的唯一标识符
        :rtype: str
        """
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAliasResponse(AbstractModel):
    """DescribeAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Alias: 别名对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: :class:`tencentcloud.gse.v20191112.models.Alias`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Alias = None
        self._RequestId = None

    @property
    def Alias(self):
        """别名对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.Alias`
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Alias") is not None:
            self._Alias = Alias()
            self._Alias._deserialize(params.get("Alias"))
        self._RequestId = params.get("RequestId")


class DescribeAssetRequest(AbstractModel):
    """DescribeAsset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 生成包ID
        :type AssetId: str
        """
        self._AssetId = None

    @property
    def AssetId(self):
        """生成包ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetResponse(AbstractModel):
    """DescribeAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Asset: 生成包信息
        :type Asset: :class:`tencentcloud.gse.v20191112.models.Asset`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Asset = None
        self._RequestId = None

    @property
    def Asset(self):
        """生成包信息
        :rtype: :class:`tencentcloud.gse.v20191112.models.Asset`
        """
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Asset") is not None:
            self._Asset = Asset()
            self._Asset._deserialize(params.get("Asset"))
        self._RequestId = params.get("RequestId")


class DescribeAssetSystemsRequest(AbstractModel):
    """DescribeAssetSystems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OsType: 生成包支持的操作系统类型
        :type OsType: str
        :param _OsBit: 生成包支持的操作系统位数
        :type OsBit: int
        """
        self._OsType = None
        self._OsBit = None

    @property
    def OsType(self):
        """生成包支持的操作系统类型
        :rtype: str
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OsBit(self):
        """生成包支持的操作系统位数
        :rtype: int
        """
        return self._OsBit

    @OsBit.setter
    def OsBit(self, OsBit):
        self._OsBit = OsBit


    def _deserialize(self, params):
        self._OsType = params.get("OsType")
        self._OsBit = params.get("OsBit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetSystemsResponse(AbstractModel):
    """DescribeAssetSystems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetSupportSys: 生成包支持的操作系统类型列表
        :type AssetSupportSys: list of AssetSupportSys
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AssetSupportSys = None
        self._RequestId = None

    @property
    def AssetSupportSys(self):
        """生成包支持的操作系统类型列表
        :rtype: list of AssetSupportSys
        """
        return self._AssetSupportSys

    @AssetSupportSys.setter
    def AssetSupportSys(self, AssetSupportSys):
        self._AssetSupportSys = AssetSupportSys

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AssetSupportSys") is not None:
            self._AssetSupportSys = []
            for item in params.get("AssetSupportSys"):
                obj = AssetSupportSys()
                obj._deserialize(item)
                self._AssetSupportSys.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAssetsRequest(AbstractModel):
    """DescribeAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetRegion: 生成包支持的可部署 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)
        :type AssetRegion: str
        :param _Offset: 偏移，代表页数，与asset实际数量相关
        :type Offset: int
        :param _Limit: 前端界面每页显示的最大条数，不超过100
        :type Limit: int
        :param _Filter: 搜索条件，支持包ID或包名字过滤，该字段会逐步废弃，建议使用 Filters 字段
        :type Filter: str
        :param _Filters: 资源过滤字段，可以按照资源名称、资源ID和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（生成包当前仅支持单个名称的过滤）- 资源ID过滤    - Key: 固定字符串 "resource:resourceId"    - Values: 生成包ID数组（生成包当前仅支持单个生成包ID的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]
        :type Filters: list of Filter
        """
        self._AssetRegion = None
        self._Offset = None
        self._Limit = None
        self._Filter = None
        self._Filters = None

    @property
    def AssetRegion(self):
        """生成包支持的可部署 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)
        :rtype: str
        """
        return self._AssetRegion

    @AssetRegion.setter
    def AssetRegion(self, AssetRegion):
        self._AssetRegion = AssetRegion

    @property
    def Offset(self):
        """偏移，代表页数，与asset实际数量相关
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """前端界面每页显示的最大条数，不超过100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filter(self):
        """搜索条件，支持包ID或包名字过滤，该字段会逐步废弃，建议使用 Filters 字段
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Filters(self):
        """资源过滤字段，可以按照资源名称、资源ID和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（生成包当前仅支持单个名称的过滤）- 资源ID过滤    - Key: 固定字符串 "resource:resourceId"    - Values: 生成包ID数组（生成包当前仅支持单个生成包ID的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._AssetRegion = params.get("AssetRegion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Filter = params.get("Filter")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetsResponse(AbstractModel):
    """DescribeAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 生成包总数
        :type TotalCount: int
        :param _Assets: 生成包列表
        :type Assets: list of Asset
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Assets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """生成包总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Assets(self):
        """生成包列表
        :rtype: list of Asset
        """
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = Asset()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCcnInstancesRequest(AbstractModel):
    """DescribeCcnInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        """
        self._FleetId = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcnInstancesResponse(AbstractModel):
    """DescribeCcnInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CcnInstanceSets: 云联网实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CcnInstanceSets: list of CcnInstanceSets
        :param _TotalCount: 云联网实例个数，最小值为0
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CcnInstanceSets = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CcnInstanceSets(self):
        """云联网实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CcnInstanceSets
        """
        return self._CcnInstanceSets

    @CcnInstanceSets.setter
    def CcnInstanceSets(self, CcnInstanceSets):
        self._CcnInstanceSets = CcnInstanceSets

    @property
    def TotalCount(self):
        """云联网实例个数，最小值为0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CcnInstanceSets") is not None:
            self._CcnInstanceSets = []
            for item in params.get("CcnInstanceSets"):
                obj = CcnInstanceSets()
                obj._deserialize(item)
                self._CcnInstanceSets.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeFleetAttributesRequest(AbstractModel):
    """DescribeFleetAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetIds: 服务器舰队 Ids
        :type FleetIds: list of str
        :param _Limit: 结果返回最大数量，默认值20，最大值100
        :type Limit: int
        :param _Offset: 返回结果偏移，最小值0
        :type Offset: int
        """
        self._FleetIds = None
        self._Limit = None
        self._Offset = None

    @property
    def FleetIds(self):
        """服务器舰队 Ids
        :rtype: list of str
        """
        return self._FleetIds

    @FleetIds.setter
    def FleetIds(self, FleetIds):
        self._FleetIds = FleetIds

    @property
    def Limit(self):
        """结果返回最大数量，默认值20，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """返回结果偏移，最小值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._FleetIds = params.get("FleetIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetAttributesResponse(AbstractModel):
    """DescribeFleetAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetAttributes: 服务器舰队属性
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetAttributes: list of FleetAttributes
        :param _TotalCount: 服务器舰队总数，最小值0
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetAttributes = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FleetAttributes(self):
        """服务器舰队属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FleetAttributes
        """
        return self._FleetAttributes

    @FleetAttributes.setter
    def FleetAttributes(self, FleetAttributes):
        self._FleetAttributes = FleetAttributes

    @property
    def TotalCount(self):
        """服务器舰队总数，最小值0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FleetAttributes") is not None:
            self._FleetAttributes = []
            for item in params.get("FleetAttributes"):
                obj = FleetAttributes()
                obj._deserialize(item)
                self._FleetAttributes.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeFleetCapacityRequest(AbstractModel):
    """DescribeFleetCapacity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetIds: 服务器舰队ID列表
        :type FleetIds: list of str
        :param _Limit: 结果返回最大数量，最大值 100
        :type Limit: int
        :param _Offset: 返回结果偏移，最小值 0
        :type Offset: int
        """
        self._FleetIds = None
        self._Limit = None
        self._Offset = None

    @property
    def FleetIds(self):
        """服务器舰队ID列表
        :rtype: list of str
        """
        return self._FleetIds

    @FleetIds.setter
    def FleetIds(self, FleetIds):
        self._FleetIds = FleetIds

    @property
    def Limit(self):
        """结果返回最大数量，最大值 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """返回结果偏移，最小值 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._FleetIds = params.get("FleetIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetCapacityResponse(AbstractModel):
    """DescribeFleetCapacity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetCapacity: 服务器舰队的容量配置
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetCapacity: list of FleetCapacity
        :param _TotalCount: 结果返回最大数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetCapacity = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FleetCapacity(self):
        """服务器舰队的容量配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FleetCapacity
        """
        return self._FleetCapacity

    @FleetCapacity.setter
    def FleetCapacity(self, FleetCapacity):
        self._FleetCapacity = FleetCapacity

    @property
    def TotalCount(self):
        """结果返回最大数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FleetCapacity") is not None:
            self._FleetCapacity = []
            for item in params.get("FleetCapacity"):
                obj = FleetCapacity()
                obj._deserialize(item)
                self._FleetCapacity.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeFleetEventsRequest(AbstractModel):
    """DescribeFleetEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        :param _Limit: 分页时返回服务器舰队事件的数量，默认为20，最大值为100
        :type Limit: int
        :param _Offset: 分页时的数据偏移量，默认为0
        :type Offset: int
        :param _EventCode: 事件代码
        :type EventCode: str
        :param _StartTime: 发生事件的开始时间
        :type StartTime: str
        :param _EndTime: 发生事件的结束时间
        :type EndTime: str
        """
        self._FleetId = None
        self._Limit = None
        self._Offset = None
        self._EventCode = None
        self._StartTime = None
        self._EndTime = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Limit(self):
        """分页时返回服务器舰队事件的数量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页时的数据偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EventCode(self):
        """事件代码
        :rtype: str
        """
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def StartTime(self):
        """发生事件的开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """发生事件的结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EventCode = params.get("EventCode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetEventsResponse(AbstractModel):
    """DescribeFleetEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 返回的事件列表
        :type Events: list of Event
        :param _TotalCount: 返回的事件总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Events(self):
        """返回的事件列表
        :rtype: list of Event
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TotalCount(self):
        """返回的事件总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeFleetPortSettingsRequest(AbstractModel):
    """DescribeFleetPortSettings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        """
        self._FleetId = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetPortSettingsResponse(AbstractModel):
    """DescribeFleetPortSettings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InboundPermissions: 安全组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InboundPermissions: list of InboundPermission
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InboundPermissions = None
        self._RequestId = None

    @property
    def InboundPermissions(self):
        """安全组信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InboundPermission
        """
        return self._InboundPermissions

    @InboundPermissions.setter
    def InboundPermissions(self, InboundPermissions):
        self._InboundPermissions = InboundPermissions

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InboundPermissions") is not None:
            self._InboundPermissions = []
            for item in params.get("InboundPermissions"):
                obj = InboundPermission()
                obj._deserialize(item)
                self._InboundPermissions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFleetRelatedResourcesRequest(AbstractModel):
    """DescribeFleetRelatedResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        """
        self._FleetId = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetRelatedResourcesResponse(AbstractModel):
    """DescribeFleetRelatedResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Resources: 与服务器舰队关联的资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: list of FleetRelatedResource
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Resources = None
        self._RequestId = None

    @property
    def Resources(self):
        """与服务器舰队关联的资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FleetRelatedResource
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = FleetRelatedResource()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFleetStatisticDetailsRequest(AbstractModel):
    """DescribeFleetStatisticDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
        :type FleetId: str
        :param _BeginTime: 查询开始时间，时间格式：YYYY-MM-DD hh:mm:ss
        :type BeginTime: str
        :param _EndTime: 查询结束时间，时间格式：YYYY-MM-DD hh:mm:ss
        :type EndTime: str
        :param _Limit: 结果返回最大数量，最小值0，最大值100
        :type Limit: int
        :param _Offset: 返回结果偏移，最小值0
        :type Offset: int
        """
        self._FleetId = None
        self._BeginTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None

    @property
    def FleetId(self):
        """服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def BeginTime(self):
        """查询开始时间，时间格式：YYYY-MM-DD hh:mm:ss
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """查询结束时间，时间格式：YYYY-MM-DD hh:mm:ss
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """结果返回最大数量，最小值0，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """返回结果偏移，最小值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetStatisticDetailsResponse(AbstractModel):
    """DescribeFleetStatisticDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetailList: 服务部署统计详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailList: list of FleetStatisticDetail
        :param _TotalCount: 记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TimeType: 统计时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailList = None
        self._TotalCount = None
        self._TimeType = None
        self._RequestId = None

    @property
    def DetailList(self):
        """服务部署统计详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FleetStatisticDetail
        """
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def TotalCount(self):
        """记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TimeType(self):
        """统计时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = FleetStatisticDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._TimeType = params.get("TimeType")
        self._RequestId = params.get("RequestId")


class DescribeFleetStatisticFlowsRequest(AbstractModel):
    """DescribeFleetStatisticFlows请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
        :type FleetId: str
        :param _BeginTime: 查询开始时间，时间格式：YYYY-MM-DD hh:mm:ss
        :type BeginTime: str
        :param _EndTime: 查询结束时间，时间格式：YYYY-MM-DD hh:mm:ss
        :type EndTime: str
        :param _Limit: 结果返回最大数量，最小值0，最大值100
        :type Limit: int
        :param _Offset: 返回结果偏移，最小值0
        :type Offset: int
        """
        self._FleetId = None
        self._BeginTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None

    @property
    def FleetId(self):
        """服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def BeginTime(self):
        """查询开始时间，时间格式：YYYY-MM-DD hh:mm:ss
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """查询结束时间，时间格式：YYYY-MM-DD hh:mm:ss
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """结果返回最大数量，最小值0，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """返回结果偏移，最小值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetStatisticFlowsResponse(AbstractModel):
    """DescribeFleetStatisticFlows返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UsedFlowList: 流量统计列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedFlowList: list of FleetStatisticFlows
        :param _UsedTimeList: 时长统计列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedTimeList: list of FleetStatisticTimes
        :param _TotalCount: 记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _TimeType: 统计时间类型，取值：小时和天
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsedFlowList = None
        self._UsedTimeList = None
        self._TotalCount = None
        self._TimeType = None
        self._RequestId = None

    @property
    def UsedFlowList(self):
        """流量统计列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FleetStatisticFlows
        """
        return self._UsedFlowList

    @UsedFlowList.setter
    def UsedFlowList(self, UsedFlowList):
        self._UsedFlowList = UsedFlowList

    @property
    def UsedTimeList(self):
        """时长统计列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FleetStatisticTimes
        """
        return self._UsedTimeList

    @UsedTimeList.setter
    def UsedTimeList(self, UsedTimeList):
        self._UsedTimeList = UsedTimeList

    @property
    def TotalCount(self):
        """记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TimeType(self):
        """统计时间类型，取值：小时和天
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UsedFlowList") is not None:
            self._UsedFlowList = []
            for item in params.get("UsedFlowList"):
                obj = FleetStatisticFlows()
                obj._deserialize(item)
                self._UsedFlowList.append(obj)
        if params.get("UsedTimeList") is not None:
            self._UsedTimeList = []
            for item in params.get("UsedTimeList"):
                obj = FleetStatisticTimes()
                obj._deserialize(item)
                self._UsedTimeList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._TimeType = params.get("TimeType")
        self._RequestId = params.get("RequestId")


class DescribeFleetStatisticSummaryRequest(AbstractModel):
    """DescribeFleetStatisticSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
        :type FleetId: str
        :param _BeginTime: 查询开始时间，时间格式: YYYY-MM-DD hh:mm:ss
        :type BeginTime: str
        :param _EndTime: 查询结束时间，时间格式: YYYY-MM-DD hh:mm:ss
        :type EndTime: str
        """
        self._FleetId = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def FleetId(self):
        """服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def BeginTime(self):
        """查询开始时间，时间格式: YYYY-MM-DD hh:mm:ss
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """查询结束时间，时间格式: YYYY-MM-DD hh:mm:ss
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetStatisticSummaryResponse(AbstractModel):
    """DescribeFleetStatisticSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalUsedTimeSeconds: 总时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUsedTimeSeconds: str
        :param _TotalUsedFlowMegaBytes: 总流量，单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUsedFlowMegaBytes: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalUsedTimeSeconds = None
        self._TotalUsedFlowMegaBytes = None
        self._RequestId = None

    @property
    def TotalUsedTimeSeconds(self):
        """总时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TotalUsedTimeSeconds

    @TotalUsedTimeSeconds.setter
    def TotalUsedTimeSeconds(self, TotalUsedTimeSeconds):
        self._TotalUsedTimeSeconds = TotalUsedTimeSeconds

    @property
    def TotalUsedFlowMegaBytes(self):
        """总流量，单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TotalUsedFlowMegaBytes

    @TotalUsedFlowMegaBytes.setter
    def TotalUsedFlowMegaBytes(self, TotalUsedFlowMegaBytes):
        self._TotalUsedFlowMegaBytes = TotalUsedFlowMegaBytes

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalUsedTimeSeconds = params.get("TotalUsedTimeSeconds")
        self._TotalUsedFlowMegaBytes = params.get("TotalUsedFlowMegaBytes")
        self._RequestId = params.get("RequestId")


class DescribeFleetUtilizationRequest(AbstractModel):
    """DescribeFleetUtilization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetIds: 服务器舰队 Ids
        :type FleetIds: list of str
        """
        self._FleetIds = None

    @property
    def FleetIds(self):
        """服务器舰队 Ids
        :rtype: list of str
        """
        return self._FleetIds

    @FleetIds.setter
    def FleetIds(self, FleetIds):
        self._FleetIds = FleetIds


    def _deserialize(self, params):
        self._FleetIds = params.get("FleetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetUtilizationResponse(AbstractModel):
    """DescribeFleetUtilization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetUtilization: 服务器舰队利用率
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetUtilization: list of FleetUtilization
        :param _TotalCount: 总数，最小值0
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetUtilization = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FleetUtilization(self):
        """服务器舰队利用率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FleetUtilization
        """
        return self._FleetUtilization

    @FleetUtilization.setter
    def FleetUtilization(self, FleetUtilization):
        self._FleetUtilization = FleetUtilization

    @property
    def TotalCount(self):
        """总数，最小值0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FleetUtilization") is not None:
            self._FleetUtilization = []
            for item in params.get("FleetUtilization"):
                obj = FleetUtilization()
                obj._deserialize(item)
                self._FleetUtilization.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGameServerSessionDetailsRequest(AbstractModel):
    """DescribeGameServerSessionDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AliasId: 别名ID
        :type AliasId: str
        :param _FleetId: 舰队ID
        :type FleetId: str
        :param _GameServerSessionId: 游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符
        :type GameServerSessionId: str
        :param _Limit: 单次查询记录数上限
        :type Limit: int
        :param _NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :type NextToken: str
        :param _StatusFilter: 游戏服务器会话状态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)
        :type StatusFilter: str
        """
        self._AliasId = None
        self._FleetId = None
        self._GameServerSessionId = None
        self._Limit = None
        self._NextToken = None
        self._StatusFilter = None

    @property
    def AliasId(self):
        """别名ID
        :rtype: str
        """
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId

    @property
    def FleetId(self):
        """舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def GameServerSessionId(self):
        """游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def Limit(self):
        """单次查询记录数上限
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NextToken(self):
        """页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def StatusFilter(self):
        """游戏服务器会话状态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)
        :rtype: str
        """
        return self._StatusFilter

    @StatusFilter.setter
    def StatusFilter(self, StatusFilter):
        self._StatusFilter = StatusFilter


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        self._FleetId = params.get("FleetId")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._Limit = params.get("Limit")
        self._NextToken = params.get("NextToken")
        self._StatusFilter = params.get("StatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionDetailsResponse(AbstractModel):
    """DescribeGameServerSessionDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionDetails: 游戏服务器会话详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionDetails: list of GameServerSessionDetail
        :param _NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSessionDetails = None
        self._NextToken = None
        self._RequestId = None

    @property
    def GameServerSessionDetails(self):
        """游戏服务器会话详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of GameServerSessionDetail
        """
        return self._GameServerSessionDetails

    @GameServerSessionDetails.setter
    def GameServerSessionDetails(self, GameServerSessionDetails):
        self._GameServerSessionDetails = GameServerSessionDetails

    @property
    def NextToken(self):
        """页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionDetails") is not None:
            self._GameServerSessionDetails = []
            for item in params.get("GameServerSessionDetails"):
                obj = GameServerSessionDetail()
                obj._deserialize(item)
                self._GameServerSessionDetails.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class DescribeGameServerSessionPlacementRequest(AbstractModel):
    """DescribeGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlacementId: 游戏服务器会话放置的唯一标识符
        :type PlacementId: str
        """
        self._PlacementId = None

    @property
    def PlacementId(self):
        """游戏服务器会话放置的唯一标识符
        :rtype: str
        """
        return self._PlacementId

    @PlacementId.setter
    def PlacementId(self, PlacementId):
        self._PlacementId = PlacementId


    def _deserialize(self, params):
        self._PlacementId = params.get("PlacementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionPlacementResponse(AbstractModel):
    """DescribeGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionPlacement: 游戏服务器会话放置
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSessionPlacement = None
        self._RequestId = None

    @property
    def GameServerSessionPlacement(self):
        """游戏服务器会话放置
        :rtype: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        """
        return self._GameServerSessionPlacement

    @GameServerSessionPlacement.setter
    def GameServerSessionPlacement(self, GameServerSessionPlacement):
        self._GameServerSessionPlacement = GameServerSessionPlacement

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self._GameServerSessionPlacement = GameServerSessionPlacement()
            self._GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self._RequestId = params.get("RequestId")


class DescribeGameServerSessionQueuesRequest(AbstractModel):
    """DescribeGameServerSessionQueues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Names: 游戏服务器会话队列名称数组，单个名字长度1~128
        :type Names: list of str
        :param _Limit: 结果返回最大数量，最小值0，最大值100
        :type Limit: int
        :param _Offset: 返回结果偏移，最小值0
        :type Offset: int
        :param _Filters: 资源过滤字段，可以按照资源名称、资源ID和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（游戏服务器会话队列支持多个名称的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]
        :type Filters: list of Filter
        """
        self._Names = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Names(self):
        """游戏服务器会话队列名称数组，单个名字长度1~128
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Limit(self):
        """结果返回最大数量，最小值0，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """返回结果偏移，最小值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """资源过滤字段，可以按照资源名称、资源ID和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（游戏服务器会话队列支持多个名称的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Names = params.get("Names")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionQueuesResponse(AbstractModel):
    """DescribeGameServerSessionQueues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionQueues: 游戏服务器会话队列数组
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionQueues: list of GameServerSessionQueue
        :param _TotalCount: 游戏服务器会话队列总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSessionQueues = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def GameServerSessionQueues(self):
        """游戏服务器会话队列数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of GameServerSessionQueue
        """
        return self._GameServerSessionQueues

    @GameServerSessionQueues.setter
    def GameServerSessionQueues(self, GameServerSessionQueues):
        self._GameServerSessionQueues = GameServerSessionQueues

    @property
    def TotalCount(self):
        """游戏服务器会话队列总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionQueues") is not None:
            self._GameServerSessionQueues = []
            for item in params.get("GameServerSessionQueues"):
                obj = GameServerSessionQueue()
                obj._deserialize(item)
                self._GameServerSessionQueues.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGameServerSessionsRequest(AbstractModel):
    """DescribeGameServerSessions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AliasId: 别名ID
        :type AliasId: str
        :param _FleetId: 舰队ID
        :type FleetId: str
        :param _GameServerSessionId: 游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符
        :type GameServerSessionId: str
        :param _Limit: 单次查询记录数上限
        :type Limit: int
        :param _NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :type NextToken: str
        :param _StatusFilter: 游戏服务器会话状态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)
        :type StatusFilter: str
        """
        self._AliasId = None
        self._FleetId = None
        self._GameServerSessionId = None
        self._Limit = None
        self._NextToken = None
        self._StatusFilter = None

    @property
    def AliasId(self):
        """别名ID
        :rtype: str
        """
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId

    @property
    def FleetId(self):
        """舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def GameServerSessionId(self):
        """游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def Limit(self):
        """单次查询记录数上限
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NextToken(self):
        """页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def StatusFilter(self):
        """游戏服务器会话状态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)
        :rtype: str
        """
        return self._StatusFilter

    @StatusFilter.setter
    def StatusFilter(self, StatusFilter):
        self._StatusFilter = StatusFilter


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        self._FleetId = params.get("FleetId")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._Limit = params.get("Limit")
        self._NextToken = params.get("NextToken")
        self._StatusFilter = params.get("StatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionsResponse(AbstractModel):
    """DescribeGameServerSessions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessions: 游戏服务器会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessions: list of GameServerSession
        :param _NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSessions = None
        self._NextToken = None
        self._RequestId = None

    @property
    def GameServerSessions(self):
        """游戏服务器会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of GameServerSession
        """
        return self._GameServerSessions

    @GameServerSessions.setter
    def GameServerSessions(self, GameServerSessions):
        self._GameServerSessions = GameServerSessions

    @property
    def NextToken(self):
        """页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self._GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self._GameServerSessions.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class DescribeInstanceLimitRequest(AbstractModel):
    """DescribeInstanceLimit请求参数结构体

    """


class DescribeInstanceLimitResponse(AbstractModel):
    """DescribeInstanceLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 限额
        :type Limit: int
        :param _ExtraInfos: 详细信息
        :type ExtraInfos: list of ExtraInfos
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Limit = None
        self._ExtraInfos = None
        self._RequestId = None

    @property
    def Limit(self):
        """限额
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ExtraInfos(self):
        """详细信息
        :rtype: list of ExtraInfos
        """
        return self._ExtraInfos

    @ExtraInfos.setter
    def ExtraInfos(self, ExtraInfos):
        self._ExtraInfos = ExtraInfos

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        if params.get("ExtraInfos") is not None:
            self._ExtraInfos = []
            for item in params.get("ExtraInfos"):
                obj = ExtraInfos()
                obj._deserialize(item)
                self._ExtraInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceTypesRequest(AbstractModel):
    """DescribeInstanceTypes请求参数结构体

    """


class DescribeInstanceTypesResponse(AbstractModel):
    """DescribeInstanceTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceTypeList: 服务器实例类型列表
        :type InstanceTypeList: list of InstanceTypeInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceTypeList = None
        self._RequestId = None

    @property
    def InstanceTypeList(self):
        """服务器实例类型列表
        :rtype: list of InstanceTypeInfo
        """
        return self._InstanceTypeList

    @InstanceTypeList.setter
    def InstanceTypeList(self, InstanceTypeList):
        self._InstanceTypeList = InstanceTypeList

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceTypeList") is not None:
            self._InstanceTypeList = []
            for item in params.get("InstanceTypeList"):
                obj = InstanceTypeInfo()
                obj._deserialize(item)
                self._InstanceTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesExtendRequest(AbstractModel):
    """DescribeInstancesExtend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
        :type FleetId: str
        :param _Offset: 返回结果偏移，最小值0
        :type Offset: int
        :param _Limit: 结果返回最大数量，最小值0，最大值100
        :type Limit: int
        :param _IpAddress: CVM实例公网IP
        :type IpAddress: str
        """
        self._FleetId = None
        self._Offset = None
        self._Limit = None
        self._IpAddress = None

    @property
    def FleetId(self):
        """服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Offset(self):
        """返回结果偏移，最小值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """结果返回最大数量，最小值0，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def IpAddress(self):
        """CVM实例公网IP
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IpAddress = params.get("IpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesExtendResponse(AbstractModel):
    """DescribeInstancesExtend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of InstanceExtend
        :param _TotalCount: 梳理信息总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        """实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceExtend
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def TotalCount(self):
        """梳理信息总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = InstanceExtend()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
        :type FleetId: str
        :param _InstanceId: CVM实例ID
        :type InstanceId: str
        :param _Offset: 结果返回最大数量，最小值0，最大值100
        :type Offset: int
        :param _Limit: 返回结果偏移，最小值0
        :type Limit: int
        :param _IpAddress: CVM实例公网IP
        :type IpAddress: str
        """
        self._FleetId = None
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._IpAddress = None

    @property
    def FleetId(self):
        """服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        """CVM实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """结果返回最大数量，最小值0，最大值100
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回结果偏移，最小值0
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def IpAddress(self):
        """CVM实例公网IP
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IpAddress = params.get("IpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of Instance
        :param _TotalCount: 结果返回最大数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        """实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Instance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def TotalCount(self):
        """结果返回最大数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePlayerSessionsRequest(AbstractModel):
    """DescribePlayerSessions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: 游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符
        :type GameServerSessionId: str
        :param _Limit: 单次查询记录数上限
        :type Limit: int
        :param _NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :type NextToken: str
        :param _PlayerId: 玩家ID，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :type PlayerId: str
        :param _PlayerSessionId: 玩家会话ID，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :type PlayerSessionId: str
        :param _PlayerSessionStatusFilter: 玩家会话状态（RESERVED,ACTIVE,COMPLETED,TIMEDOUT）
        :type PlayerSessionStatusFilter: str
        """
        self._GameServerSessionId = None
        self._Limit = None
        self._NextToken = None
        self._PlayerId = None
        self._PlayerSessionId = None
        self._PlayerSessionStatusFilter = None

    @property
    def GameServerSessionId(self):
        """游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def Limit(self):
        """单次查询记录数上限
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NextToken(self):
        """页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def PlayerId(self):
        """玩家ID，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :rtype: str
        """
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def PlayerSessionId(self):
        """玩家会话ID，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :rtype: str
        """
        return self._PlayerSessionId

    @PlayerSessionId.setter
    def PlayerSessionId(self, PlayerSessionId):
        self._PlayerSessionId = PlayerSessionId

    @property
    def PlayerSessionStatusFilter(self):
        """玩家会话状态（RESERVED,ACTIVE,COMPLETED,TIMEDOUT）
        :rtype: str
        """
        return self._PlayerSessionStatusFilter

    @PlayerSessionStatusFilter.setter
    def PlayerSessionStatusFilter(self, PlayerSessionStatusFilter):
        self._PlayerSessionStatusFilter = PlayerSessionStatusFilter


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._Limit = params.get("Limit")
        self._NextToken = params.get("NextToken")
        self._PlayerId = params.get("PlayerId")
        self._PlayerSessionId = params.get("PlayerSessionId")
        self._PlayerSessionStatusFilter = params.get("PlayerSessionStatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlayerSessionsResponse(AbstractModel):
    """DescribePlayerSessions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlayerSessions: 玩家会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSessions: list of PlayerSession
        :param _NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlayerSessions = None
        self._NextToken = None
        self._RequestId = None

    @property
    def PlayerSessions(self):
        """玩家会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PlayerSession
        """
        return self._PlayerSessions

    @PlayerSessions.setter
    def PlayerSessions(self, PlayerSessions):
        self._PlayerSessions = PlayerSessions

    @property
    def NextToken(self):
        """页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self._PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self._PlayerSessions.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class DescribeRuntimeConfigurationRequest(AbstractModel):
    """DescribeRuntimeConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        """
        self._FleetId = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuntimeConfigurationResponse(AbstractModel):
    """DescribeRuntimeConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuntimeConfiguration: 服务器舰队运行配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuntimeConfiguration = None
        self._RequestId = None

    @property
    def RuntimeConfiguration(self):
        """服务器舰队运行配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        """
        return self._RuntimeConfiguration

    @RuntimeConfiguration.setter
    def RuntimeConfiguration(self, RuntimeConfiguration):
        self._RuntimeConfiguration = RuntimeConfiguration

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuntimeConfiguration") is not None:
            self._RuntimeConfiguration = RuntimeConfiguration()
            self._RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        self._RequestId = params.get("RequestId")


class DescribeScalingPoliciesRequest(AbstractModel):
    """DescribeScalingPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
        :type FleetId: str
        :param _StatusFilter: 状态过滤条件，取值：ACTIVE表示活跃
        :type StatusFilter: str
        :param _Offset: 返回结果偏移，最小值0
        :type Offset: int
        :param _Limit: 结果返回最大数量，最小值0，最大值100
        :type Limit: int
        """
        self._FleetId = None
        self._StatusFilter = None
        self._Offset = None
        self._Limit = None

    @property
    def FleetId(self):
        """服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def StatusFilter(self):
        """状态过滤条件，取值：ACTIVE表示活跃
        :rtype: str
        """
        return self._StatusFilter

    @StatusFilter.setter
    def StatusFilter(self, StatusFilter):
        self._StatusFilter = StatusFilter

    @property
    def Offset(self):
        """返回结果偏移，最小值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """结果返回最大数量，最小值0，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._StatusFilter = params.get("StatusFilter")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScalingPoliciesResponse(AbstractModel):
    """DescribeScalingPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScalingPolicies: 动态扩缩容配置策略数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingPolicies: list of ScalingPolicy
        :param _TotalCount: 动态扩缩容配置策略总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScalingPolicies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ScalingPolicies(self):
        """动态扩缩容配置策略数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScalingPolicy
        """
        return self._ScalingPolicies

    @ScalingPolicies.setter
    def ScalingPolicies(self, ScalingPolicies):
        self._ScalingPolicies = ScalingPolicies

    @property
    def TotalCount(self):
        """动态扩缩容配置策略总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ScalingPolicies") is not None:
            self._ScalingPolicies = []
            for item in params.get("ScalingPolicies"):
                obj = ScalingPolicy()
                obj._deserialize(item)
                self._ScalingPolicies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTimerScalingPoliciesRequest(AbstractModel):
    """DescribeTimerScalingPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 扩缩容配置服务器舰队ID
        :type FleetId: str
        :param _TimerName: 定时器名称
        :type TimerName: str
        :param _BeginTime: 定时器开始时间
        :type BeginTime: str
        :param _EndTime: 定时器结束时间
        :type EndTime: str
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 页大小
        :type Limit: int
        """
        self._FleetId = None
        self._TimerName = None
        self._BeginTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def FleetId(self):
        """扩缩容配置服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def TimerName(self):
        """定时器名称
        :rtype: str
        """
        return self._TimerName

    @TimerName.setter
    def TimerName(self, TimerName):
        self._TimerName = TimerName

    @property
    def BeginTime(self):
        """定时器开始时间
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """定时器结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._TimerName = params.get("TimerName")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimerScalingPoliciesResponse(AbstractModel):
    """DescribeTimerScalingPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TimerScalingPolicies: 定时器扩缩容策略配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TimerScalingPolicies: list of TimerScalingPolicy
        :param _TotalCount: 定时器总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TimerScalingPolicies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TimerScalingPolicies(self):
        """定时器扩缩容策略配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TimerScalingPolicy
        """
        return self._TimerScalingPolicies

    @TimerScalingPolicies.setter
    def TimerScalingPolicies(self, TimerScalingPolicies):
        self._TimerScalingPolicies = TimerScalingPolicies

    @property
    def TotalCount(self):
        """定时器总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TimerScalingPolicies") is not None:
            self._TimerScalingPolicies = []
            for item in params.get("TimerScalingPolicies"):
                obj = TimerScalingPolicy()
                obj._deserialize(item)
                self._TimerScalingPolicies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserQuotaRequest(AbstractModel):
    """DescribeUserQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型
        :type ResourceType: int
        """
        self._ResourceType = None

    @property
    def ResourceType(self):
        """资源类型
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserQuotaResponse(AbstractModel):
    """DescribeUserQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QuotaResource: 配额资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaResource: :class:`tencentcloud.gse.v20191112.models.QuotaResource`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QuotaResource = None
        self._RequestId = None

    @property
    def QuotaResource(self):
        """配额资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.QuotaResource`
        """
        return self._QuotaResource

    @QuotaResource.setter
    def QuotaResource(self, QuotaResource):
        self._QuotaResource = QuotaResource

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QuotaResource") is not None:
            self._QuotaResource = QuotaResource()
            self._QuotaResource._deserialize(params.get("QuotaResource"))
        self._RequestId = params.get("RequestId")


class DescribeUserQuotasRequest(AbstractModel):
    """DescribeUserQuotas请求参数结构体

    """


class DescribeUserQuotasResponse(AbstractModel):
    """DescribeUserQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QuotaResource: 配额信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaResource: list of QuotaResource
        :param _Total: 配额信息列表总数，最小值0
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QuotaResource = None
        self._Total = None
        self._RequestId = None

    @property
    def QuotaResource(self):
        """配额信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QuotaResource
        """
        return self._QuotaResource

    @QuotaResource.setter
    def QuotaResource(self, QuotaResource):
        self._QuotaResource = QuotaResource

    @property
    def Total(self):
        """配额信息列表总数，最小值0
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QuotaResource") is not None:
            self._QuotaResource = []
            for item in params.get("QuotaResource"):
                obj = QuotaResource()
                obj._deserialize(item)
                self._QuotaResource.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DesiredPlayerSession(AbstractModel):
    """玩家游戏会话信息

    """

    def __init__(self):
        r"""
        :param _PlayerId: 与玩家会话关联的唯一玩家标识
        :type PlayerId: str
        :param _PlayerData: 开发人员定义的玩家数据
        :type PlayerData: str
        """
        self._PlayerId = None
        self._PlayerData = None

    @property
    def PlayerId(self):
        """与玩家会话关联的唯一玩家标识
        :rtype: str
        """
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def PlayerData(self):
        """开发人员定义的玩家数据
        :rtype: str
        """
        return self._PlayerData

    @PlayerData.setter
    def PlayerData(self, PlayerData):
        self._PlayerData = PlayerData


    def _deserialize(self, params):
        self._PlayerId = params.get("PlayerId")
        self._PlayerData = params.get("PlayerData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnInstancesRequest(AbstractModel):
    """DetachCcnInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        """
        self._FleetId = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnInstancesResponse(AbstractModel):
    """DetachCcnInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DiskInfo(AbstractModel):
    """磁盘存储信息

    """

    def __init__(self):
        r"""
        :param _DiskType: 磁盘类型，支持：高性能云硬盘（CLOUD_PREMIUM）、SSD云硬盘（CLOUD_SSD）
        :type DiskType: str
        :param _DiskSize: 系统盘：可选硬盘容量，50-500GB，数字以1为单位，数据盘：可选硬盘容量：10-32000GB，数字以10为单位；当磁盘类型为SSD云硬盘（CLOUD_SSD）最小大小为 100GB
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        """磁盘类型，支持：高性能云硬盘（CLOUD_PREMIUM）、SSD云硬盘（CLOUD_SSD）
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """系统盘：可选硬盘容量，50-500GB，数字以1为单位，数据盘：可选硬盘容量：10-32000GB，数字以10为单位；当磁盘类型为SSD云硬盘（CLOUD_SSD）最小大小为 100GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndGameServerSessionAndProcessRequest(AbstractModel):
    """EndGameServerSessionAndProcess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: 游戏服务器会话ID，如果传入游戏服务器会话ID，结束对应进程以及游戏服务器会话和玩家会话。
        :type GameServerSessionId: str
        :param _IpAddress: CVM的公网IP地址，需同时传入IpAddress和Port，结束IpAddress和Port对应的进程以及游戏服务器会话（如果存在）和玩家会话（如果存在），单独传入IpAddress不生效。
        :type IpAddress: str
        :param _Port: 端口号，取值范围1025-60000，需同时传入IpAddress和Port，结束IpAddress和Port对应的进程以及游戏服务器会话（如果存在）和玩家会话（如果存在），单独传入Port不生效。
        :type Port: int
        """
        self._GameServerSessionId = None
        self._IpAddress = None
        self._Port = None

    @property
    def GameServerSessionId(self):
        """游戏服务器会话ID，如果传入游戏服务器会话ID，结束对应进程以及游戏服务器会话和玩家会话。
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def IpAddress(self):
        """CVM的公网IP地址，需同时传入IpAddress和Port，结束IpAddress和Port对应的进程以及游戏服务器会话（如果存在）和玩家会话（如果存在），单独传入IpAddress不生效。
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def Port(self):
        """端口号，取值范围1025-60000，需同时传入IpAddress和Port，结束IpAddress和Port对应的进程以及游戏服务器会话（如果存在）和玩家会话（如果存在），单独传入Port不生效。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._IpAddress = params.get("IpAddress")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndGameServerSessionAndProcessResponse(AbstractModel):
    """EndGameServerSessionAndProcess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Event(AbstractModel):
    """事件对象

    """

    def __init__(self):
        r"""
        :param _EventCode: 事件代码，支持以下的事件代码

- FLEET_CREATED 
- FLEET_STATE_DOWNLOADING 
- FLEET_BINARY_DOWNLOAD_FAILED 
- FLEET_CREATION_EXTRACTING_BUILD
- FLEET_CREATION_VALIDATING_RUNTIME_CONFIG
- FLEET_STATE_VALIDATING
- FLEET_STATE_BUILDING 
- FLEET_STATE_ACTIVATING
- FLEET_STATE_ACTIVE
- FLEET_SCALING_EVENT
- FLEET_STATE_ERROR
- FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND
- FLEET_ACTIVATION_FAILED_NO_INSTANCES
- FLEET_VPC_PEERING_SUCCEEDED
- FLEET_VPC_PEERING_FAILED
- FLEET_VPC_PEERING_DELETE
- FLEET_INITIALIZATION_FAILED
- FLEET_DELETED
- FLEET_STATE_DELETING
- FLEET_ACTIVATION_FAILED
- GAME_SESSION_ACTIVATION_TIMEOUT
        :type EventCode: str
        :param _EventId: 事件的唯一标识 ID
        :type EventId: str
        :param _EventTime: 事件的发生时间，UTC 时间格式
        :type EventTime: str
        :param _Message: 事件的消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _PreSignedLogUrl: 事件相关的日志存储路径
注意：此字段可能返回 null，表示取不到有效值。
        :type PreSignedLogUrl: str
        :param _ResourceId: 事件对应的资源对象唯一标识 ID，例如服务器舰队 ID
        :type ResourceId: str
        """
        self._EventCode = None
        self._EventId = None
        self._EventTime = None
        self._Message = None
        self._PreSignedLogUrl = None
        self._ResourceId = None

    @property
    def EventCode(self):
        """事件代码，支持以下的事件代码

- FLEET_CREATED 
- FLEET_STATE_DOWNLOADING 
- FLEET_BINARY_DOWNLOAD_FAILED 
- FLEET_CREATION_EXTRACTING_BUILD
- FLEET_CREATION_VALIDATING_RUNTIME_CONFIG
- FLEET_STATE_VALIDATING
- FLEET_STATE_BUILDING 
- FLEET_STATE_ACTIVATING
- FLEET_STATE_ACTIVE
- FLEET_SCALING_EVENT
- FLEET_STATE_ERROR
- FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND
- FLEET_ACTIVATION_FAILED_NO_INSTANCES
- FLEET_VPC_PEERING_SUCCEEDED
- FLEET_VPC_PEERING_FAILED
- FLEET_VPC_PEERING_DELETE
- FLEET_INITIALIZATION_FAILED
- FLEET_DELETED
- FLEET_STATE_DELETING
- FLEET_ACTIVATION_FAILED
- GAME_SESSION_ACTIVATION_TIMEOUT
        :rtype: str
        """
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventId(self):
        """事件的唯一标识 ID
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def EventTime(self):
        """事件的发生时间，UTC 时间格式
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def Message(self):
        """事件的消息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def PreSignedLogUrl(self):
        """事件相关的日志存储路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PreSignedLogUrl

    @PreSignedLogUrl.setter
    def PreSignedLogUrl(self, PreSignedLogUrl):
        self._PreSignedLogUrl = PreSignedLogUrl

    @property
    def ResourceId(self):
        """事件对应的资源对象唯一标识 ID，例如服务器舰队 ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._EventCode = params.get("EventCode")
        self._EventId = params.get("EventId")
        self._EventTime = params.get("EventTime")
        self._Message = params.get("Message")
        self._PreSignedLogUrl = params.get("PreSignedLogUrl")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtraInfos(AbstractModel):
    """实例类型限额配置额外信息

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型，例如S5.LARGE8
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _TotalInstances: 实例限额数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalInstances: int
        """
        self._InstanceType = None
        self._TotalInstances = None

    @property
    def InstanceType(self):
        """实例类型，例如S5.LARGE8
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def TotalInstances(self):
        """实例限额数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalInstances

    @TotalInstances.setter
    def TotalInstances(self, TotalInstances):
        self._TotalInstances = TotalInstances


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._TotalInstances = params.get("TotalInstances")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤字段内容

    """

    def __init__(self):
        r"""
        :param _Key: 过滤属性的 key
        :type Key: str
        :param _Values: 过滤属性的 values 值
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        """过滤属性的 key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        """过滤属性的 values 值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetAttributes(AbstractModel):
    """服务部署属性

    """

    def __init__(self):
        r"""
        :param _AssetId: 生成包 Id
        :type AssetId: str
        :param _CreationTime: 创建服务器舰队时间
        :type CreationTime: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _FleetArn: 服务器舰队资源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetArn: str
        :param _FleetId: 服务器舰队 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _FleetType: 服务器舰队类型，目前只支持ON_DEMAND
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetType: str
        :param _InstanceType: 服务器类型，例如S5.LARGE8
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _Name: 服务器舰队名称
        :type Name: str
        :param _NewGameServerSessionProtectionPolicy: 游戏会话保护策略
注意：此字段可能返回 null，表示取不到有效值。
        :type NewGameServerSessionProtectionPolicy: str
        :param _OperatingSystem: 操作系统类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatingSystem: str
        :param _ResourceCreationLimitPolicy: 资源创建限制策略
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`
        :param _Status: 状态：新建、下载中、验证中、生成中、激活中、活跃、异常、删除中、结束
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _StoppedActions: 服务器舰队停止状态，为空时表示自动扩缩容
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppedActions: list of str
        :param _TerminationTime: 服务器舰队终止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminationTime: str
        :param _GameServerSessionProtectionTimeLimit: 时限保护超时时间，默认60分钟，最小值5，最大值1440
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionProtectionTimeLimit: int
        :param _BillingStatus: 计费状态：未开通、已开通、异常、欠费隔离、销毁、解冻
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingStatus: str
        :param _Tags: 标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _DataDiskInfo: 数据盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-32000GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，10-32000GB；容量以10为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDiskInfo: list of DiskInfo
        :param _SystemDiskInfo: 系统盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-500GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，50-500GB；容量以1为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDiskInfo: :class:`tencentcloud.gse.v20191112.models.DiskInfo`
        :param _RelatedCcnInfos: 云联网相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RelatedCcnInfos: list of RelatedCcnInfo
        :param _InternetMaxBandwidthOut: fleet公网出带宽最大值，默认100Mbps，范围1-200Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        """
        self._AssetId = None
        self._CreationTime = None
        self._Description = None
        self._FleetArn = None
        self._FleetId = None
        self._FleetType = None
        self._InstanceType = None
        self._Name = None
        self._NewGameServerSessionProtectionPolicy = None
        self._OperatingSystem = None
        self._ResourceCreationLimitPolicy = None
        self._Status = None
        self._StoppedActions = None
        self._TerminationTime = None
        self._GameServerSessionProtectionTimeLimit = None
        self._BillingStatus = None
        self._Tags = None
        self._DataDiskInfo = None
        self._SystemDiskInfo = None
        self._RelatedCcnInfos = None
        self._InternetMaxBandwidthOut = None

    @property
    def AssetId(self):
        """生成包 Id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def CreationTime(self):
        """创建服务器舰队时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def Description(self):
        """描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def FleetArn(self):
        """服务器舰队资源描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetArn

    @FleetArn.setter
    def FleetArn(self, FleetArn):
        self._FleetArn = FleetArn

    @property
    def FleetId(self):
        """服务器舰队 Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def FleetType(self):
        """服务器舰队类型，目前只支持ON_DEMAND
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetType

    @FleetType.setter
    def FleetType(self, FleetType):
        self._FleetType = FleetType

    @property
    def InstanceType(self):
        """服务器类型，例如S5.LARGE8
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Name(self):
        """服务器舰队名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NewGameServerSessionProtectionPolicy(self):
        """游戏会话保护策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NewGameServerSessionProtectionPolicy

    @NewGameServerSessionProtectionPolicy.setter
    def NewGameServerSessionProtectionPolicy(self, NewGameServerSessionProtectionPolicy):
        self._NewGameServerSessionProtectionPolicy = NewGameServerSessionProtectionPolicy

    @property
    def OperatingSystem(self):
        """操作系统类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OperatingSystem

    @OperatingSystem.setter
    def OperatingSystem(self, OperatingSystem):
        self._OperatingSystem = OperatingSystem

    @property
    def ResourceCreationLimitPolicy(self):
        """资源创建限制策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`
        """
        return self._ResourceCreationLimitPolicy

    @ResourceCreationLimitPolicy.setter
    def ResourceCreationLimitPolicy(self, ResourceCreationLimitPolicy):
        self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy

    @property
    def Status(self):
        """状态：新建、下载中、验证中、生成中、激活中、活跃、异常、删除中、结束
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StoppedActions(self):
        """服务器舰队停止状态，为空时表示自动扩缩容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._StoppedActions

    @StoppedActions.setter
    def StoppedActions(self, StoppedActions):
        self._StoppedActions = StoppedActions

    @property
    def TerminationTime(self):
        """服务器舰队终止时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TerminationTime

    @TerminationTime.setter
    def TerminationTime(self, TerminationTime):
        self._TerminationTime = TerminationTime

    @property
    def GameServerSessionProtectionTimeLimit(self):
        """时限保护超时时间，默认60分钟，最小值5，最大值1440
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._GameServerSessionProtectionTimeLimit

    @GameServerSessionProtectionTimeLimit.setter
    def GameServerSessionProtectionTimeLimit(self, GameServerSessionProtectionTimeLimit):
        self._GameServerSessionProtectionTimeLimit = GameServerSessionProtectionTimeLimit

    @property
    def BillingStatus(self):
        """计费状态：未开通、已开通、异常、欠费隔离、销毁、解冻
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BillingStatus

    @BillingStatus.setter
    def BillingStatus(self, BillingStatus):
        self._BillingStatus = BillingStatus

    @property
    def Tags(self):
        """标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DataDiskInfo(self):
        """数据盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-32000GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，10-32000GB；容量以10为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DiskInfo
        """
        return self._DataDiskInfo

    @DataDiskInfo.setter
    def DataDiskInfo(self, DataDiskInfo):
        self._DataDiskInfo = DataDiskInfo

    @property
    def SystemDiskInfo(self):
        """系统盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-500GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，50-500GB；容量以1为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.DiskInfo`
        """
        return self._SystemDiskInfo

    @SystemDiskInfo.setter
    def SystemDiskInfo(self, SystemDiskInfo):
        self._SystemDiskInfo = SystemDiskInfo

    @property
    def RelatedCcnInfos(self):
        """云联网相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RelatedCcnInfo
        """
        return self._RelatedCcnInfos

    @RelatedCcnInfos.setter
    def RelatedCcnInfos(self, RelatedCcnInfos):
        self._RelatedCcnInfos = RelatedCcnInfos

    @property
    def InternetMaxBandwidthOut(self):
        """fleet公网出带宽最大值，默认100Mbps，范围1-200Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._CreationTime = params.get("CreationTime")
        self._Description = params.get("Description")
        self._FleetArn = params.get("FleetArn")
        self._FleetId = params.get("FleetId")
        self._FleetType = params.get("FleetType")
        self._InstanceType = params.get("InstanceType")
        self._Name = params.get("Name")
        self._NewGameServerSessionProtectionPolicy = params.get("NewGameServerSessionProtectionPolicy")
        self._OperatingSystem = params.get("OperatingSystem")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self._ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        self._Status = params.get("Status")
        self._StoppedActions = params.get("StoppedActions")
        self._TerminationTime = params.get("TerminationTime")
        self._GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        self._BillingStatus = params.get("BillingStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("DataDiskInfo") is not None:
            self._DataDiskInfo = []
            for item in params.get("DataDiskInfo"):
                obj = DiskInfo()
                obj._deserialize(item)
                self._DataDiskInfo.append(obj)
        if params.get("SystemDiskInfo") is not None:
            self._SystemDiskInfo = DiskInfo()
            self._SystemDiskInfo._deserialize(params.get("SystemDiskInfo"))
        if params.get("RelatedCcnInfos") is not None:
            self._RelatedCcnInfos = []
            for item in params.get("RelatedCcnInfos"):
                obj = RelatedCcnInfo()
                obj._deserialize(item)
                self._RelatedCcnInfos.append(obj)
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetCapacity(AbstractModel):
    """服务部署组容量配置

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务部署 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _InstanceType: 服务器类型，如S3.LARGE8,S2.LARGE8,S5.LARGE8等
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _InstanceCounts: 服务器实例统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCounts: :class:`tencentcloud.gse.v20191112.models.InstanceCounts`
        :param _ScalingInterval: 服务器伸缩容间隔，单位分钟，最小值3，最大值30，默认值10
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingInterval: int
        """
        self._FleetId = None
        self._InstanceType = None
        self._InstanceCounts = None
        self._ScalingInterval = None

    @property
    def FleetId(self):
        """服务部署 Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceType(self):
        """服务器类型，如S3.LARGE8,S2.LARGE8,S5.LARGE8等
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceCounts(self):
        """服务器实例统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.InstanceCounts`
        """
        return self._InstanceCounts

    @InstanceCounts.setter
    def InstanceCounts(self, InstanceCounts):
        self._InstanceCounts = InstanceCounts

    @property
    def ScalingInterval(self):
        """服务器伸缩容间隔，单位分钟，最小值3，最大值30，默认值10
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ScalingInterval

    @ScalingInterval.setter
    def ScalingInterval(self, ScalingInterval):
        self._ScalingInterval = ScalingInterval


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._InstanceType = params.get("InstanceType")
        if params.get("InstanceCounts") is not None:
            self._InstanceCounts = InstanceCounts()
            self._InstanceCounts._deserialize(params.get("InstanceCounts"))
        self._ScalingInterval = params.get("ScalingInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetRelatedResource(AbstractModel):
    """与服务器舰队关联的资源，如别名和队列

    """

    def __init__(self):
        r"""
        :param _Type: 资源类型。
- ALIAS：别名
- QUEUE：队列
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _ResourceId: 资源ID，目前仅支持别名ID和队列名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _ResourceRegion: 资源所在区域，如ap-shanghai、na-siliconvalley等
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRegion: str
        """
        self._Type = None
        self._ResourceId = None
        self._ResourceRegion = None

    @property
    def Type(self):
        """资源类型。
- ALIAS：别名
- QUEUE：队列
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ResourceId(self):
        """资源ID，目前仅支持别名ID和队列名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        """资源所在区域，如ap-shanghai、na-siliconvalley等
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetStatisticDetail(AbstractModel):
    """舰队统计详情

    """

    def __init__(self):
        r"""
        :param _FleetId: 舰队ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceIP: 实例IP
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIP: str
        :param _BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _TotalUsedTimeSeconds: 总时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUsedTimeSeconds: str
        :param _TotalUsedFlowMegaBytes: 总流量，单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUsedFlowMegaBytes: float
        """
        self._FleetId = None
        self._InstanceId = None
        self._InstanceIP = None
        self._BeginTime = None
        self._EndTime = None
        self._TotalUsedTimeSeconds = None
        self._TotalUsedFlowMegaBytes = None

    @property
    def FleetId(self):
        """舰队ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        """实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceIP(self):
        """实例IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceIP

    @InstanceIP.setter
    def InstanceIP(self, InstanceIP):
        self._InstanceIP = InstanceIP

    @property
    def BeginTime(self):
        """开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TotalUsedTimeSeconds(self):
        """总时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TotalUsedTimeSeconds

    @TotalUsedTimeSeconds.setter
    def TotalUsedTimeSeconds(self, TotalUsedTimeSeconds):
        self._TotalUsedTimeSeconds = TotalUsedTimeSeconds

    @property
    def TotalUsedFlowMegaBytes(self):
        """总流量，单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TotalUsedFlowMegaBytes

    @TotalUsedFlowMegaBytes.setter
    def TotalUsedFlowMegaBytes(self, TotalUsedFlowMegaBytes):
        self._TotalUsedFlowMegaBytes = TotalUsedFlowMegaBytes


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceIP = params.get("InstanceIP")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._TotalUsedTimeSeconds = params.get("TotalUsedTimeSeconds")
        self._TotalUsedFlowMegaBytes = params.get("TotalUsedFlowMegaBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetStatisticFlows(AbstractModel):
    """舰队统计流量

    """

    def __init__(self):
        r"""
        :param _TotalUsedFlowMegaBytes: 总流量，单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUsedFlowMegaBytes: float
        :param _BeginTime: 统计开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        """
        self._TotalUsedFlowMegaBytes = None
        self._BeginTime = None

    @property
    def TotalUsedFlowMegaBytes(self):
        """总流量，单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TotalUsedFlowMegaBytes

    @TotalUsedFlowMegaBytes.setter
    def TotalUsedFlowMegaBytes(self, TotalUsedFlowMegaBytes):
        self._TotalUsedFlowMegaBytes = TotalUsedFlowMegaBytes

    @property
    def BeginTime(self):
        """统计开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime


    def _deserialize(self, params):
        self._TotalUsedFlowMegaBytes = params.get("TotalUsedFlowMegaBytes")
        self._BeginTime = params.get("BeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetStatisticTimes(AbstractModel):
    """舰队统计总时长

    """

    def __init__(self):
        r"""
        :param _BeginTime: 统计开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param _TotalUsedTimeSeconds: 统计总时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalUsedTimeSeconds: str
        """
        self._BeginTime = None
        self._TotalUsedTimeSeconds = None

    @property
    def BeginTime(self):
        """统计开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def TotalUsedTimeSeconds(self):
        """统计总时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TotalUsedTimeSeconds

    @TotalUsedTimeSeconds.setter
    def TotalUsedTimeSeconds(self, TotalUsedTimeSeconds):
        self._TotalUsedTimeSeconds = TotalUsedTimeSeconds


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._TotalUsedTimeSeconds = params.get("TotalUsedTimeSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetUtilization(AbstractModel):
    """服务部署利用率

    """

    def __init__(self):
        r"""
        :param _ActiveGameServerSessionCount: 游戏会话数
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveGameServerSessionCount: int
        :param _ActiveServerProcessCount: 活跃进程数
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveServerProcessCount: int
        :param _CurrentPlayerSessionCount: 当前游戏玩家数
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentPlayerSessionCount: int
        :param _FleetId: 服务部署 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _MaximumPlayerSessionCount: 最大玩家会话数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaximumPlayerSessionCount: int
        """
        self._ActiveGameServerSessionCount = None
        self._ActiveServerProcessCount = None
        self._CurrentPlayerSessionCount = None
        self._FleetId = None
        self._MaximumPlayerSessionCount = None

    @property
    def ActiveGameServerSessionCount(self):
        """游戏会话数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ActiveGameServerSessionCount

    @ActiveGameServerSessionCount.setter
    def ActiveGameServerSessionCount(self, ActiveGameServerSessionCount):
        self._ActiveGameServerSessionCount = ActiveGameServerSessionCount

    @property
    def ActiveServerProcessCount(self):
        """活跃进程数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ActiveServerProcessCount

    @ActiveServerProcessCount.setter
    def ActiveServerProcessCount(self, ActiveServerProcessCount):
        self._ActiveServerProcessCount = ActiveServerProcessCount

    @property
    def CurrentPlayerSessionCount(self):
        """当前游戏玩家数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CurrentPlayerSessionCount

    @CurrentPlayerSessionCount.setter
    def CurrentPlayerSessionCount(self, CurrentPlayerSessionCount):
        self._CurrentPlayerSessionCount = CurrentPlayerSessionCount

    @property
    def FleetId(self):
        """服务部署 Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def MaximumPlayerSessionCount(self):
        """最大玩家会话数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount


    def _deserialize(self, params):
        self._ActiveGameServerSessionCount = params.get("ActiveGameServerSessionCount")
        self._ActiveServerProcessCount = params.get("ActiveServerProcessCount")
        self._CurrentPlayerSessionCount = params.get("CurrentPlayerSessionCount")
        self._FleetId = params.get("FleetId")
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameProperty(AbstractModel):
    """游戏属性详情

    """

    def __init__(self):
        r"""
        :param _Key: 属性名称，最大长度不超过32个ASCII字符
        :type Key: str
        :param _Value: 属性值，最大长度不超过96个ASCII字符
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """属性名称，最大长度不超过32个ASCII字符
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """属性值，最大长度不超过96个ASCII字符
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
        


class GameServerSession(AbstractModel):
    """游戏会话详情

    """

    def __init__(self):
        r"""
        :param _CreationTime: 游戏服务器会话创建时间
        :type CreationTime: str
        :param _CreatorId: 创建者ID，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorId: str
        :param _CurrentPlayerSessionCount: 当前玩家数量，最小值不小于0
        :type CurrentPlayerSessionCount: int
        :param _DnsName: CVM的DNS标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param _FleetId: 舰队ID
        :type FleetId: str
        :param _GameProperties: 游戏属性，最大长度不超过16组
注意：此字段可能返回 null，表示取不到有效值。
        :type GameProperties: list of GameProperty
        :param _GameServerSessionData: 游戏服务器会话属性详情，最大长度不超过4096个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionData: str
        :param _GameServerSessionId: 游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符
        :type GameServerSessionId: str
        :param _IpAddress: CVM IP地址
        :type IpAddress: str
        :param _MatchmakerData: 对战进程详情，最大长度不超过400000个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchmakerData: str
        :param _MaximumPlayerSessionCount: 最大玩家数量，最小值不小于0
        :type MaximumPlayerSessionCount: int
        :param _Name: 游戏服务器会话名称，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _PlayerSessionCreationPolicy: 玩家会话创建策略（ACCEPT_ALL,DENY_ALL）
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSessionCreationPolicy: str
        :param _Port: 端口号，最小值不小于1，最大值不超过60000
        :type Port: int
        :param _Status: 游戏服务器会话状态（ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR）
        :type Status: str
        :param _StatusReason: 游戏服务器会话状态附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusReason: str
        :param _TerminationTime: 终止的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminationTime: str
        :param _InstanceType: 实例类型，最大长度不超过128个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _CurrentCustomCount: 当前自定义数
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentCustomCount: int
        :param _MaxCustomCount: 最大自定义数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxCustomCount: int
        :param _Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _AvailabilityStatus: 会话可用性状态，是否被屏蔽（Enable,Disable）
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailabilityStatus: str
        """
        self._CreationTime = None
        self._CreatorId = None
        self._CurrentPlayerSessionCount = None
        self._DnsName = None
        self._FleetId = None
        self._GameProperties = None
        self._GameServerSessionData = None
        self._GameServerSessionId = None
        self._IpAddress = None
        self._MatchmakerData = None
        self._MaximumPlayerSessionCount = None
        self._Name = None
        self._PlayerSessionCreationPolicy = None
        self._Port = None
        self._Status = None
        self._StatusReason = None
        self._TerminationTime = None
        self._InstanceType = None
        self._CurrentCustomCount = None
        self._MaxCustomCount = None
        self._Weight = None
        self._AvailabilityStatus = None

    @property
    def CreationTime(self):
        """游戏服务器会话创建时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def CreatorId(self):
        """创建者ID，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def CurrentPlayerSessionCount(self):
        """当前玩家数量，最小值不小于0
        :rtype: int
        """
        return self._CurrentPlayerSessionCount

    @CurrentPlayerSessionCount.setter
    def CurrentPlayerSessionCount(self, CurrentPlayerSessionCount):
        self._CurrentPlayerSessionCount = CurrentPlayerSessionCount

    @property
    def DnsName(self):
        """CVM的DNS标识符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DnsName

    @DnsName.setter
    def DnsName(self, DnsName):
        self._DnsName = DnsName

    @property
    def FleetId(self):
        """舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def GameProperties(self):
        """游戏属性，最大长度不超过16组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of GameProperty
        """
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def GameServerSessionData(self):
        """游戏服务器会话属性详情，最大长度不超过4096个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GameServerSessionData

    @GameServerSessionData.setter
    def GameServerSessionData(self, GameServerSessionData):
        self._GameServerSessionData = GameServerSessionData

    @property
    def GameServerSessionId(self):
        """游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def IpAddress(self):
        """CVM IP地址
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def MatchmakerData(self):
        """对战进程详情，最大长度不超过400000个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MatchmakerData

    @MatchmakerData.setter
    def MatchmakerData(self, MatchmakerData):
        self._MatchmakerData = MatchmakerData

    @property
    def MaximumPlayerSessionCount(self):
        """最大玩家数量，最小值不小于0
        :rtype: int
        """
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount

    @property
    def Name(self):
        """游戏服务器会话名称，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PlayerSessionCreationPolicy(self):
        """玩家会话创建策略（ACCEPT_ALL,DENY_ALL）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PlayerSessionCreationPolicy

    @PlayerSessionCreationPolicy.setter
    def PlayerSessionCreationPolicy(self, PlayerSessionCreationPolicy):
        self._PlayerSessionCreationPolicy = PlayerSessionCreationPolicy

    @property
    def Port(self):
        """端口号，最小值不小于1，最大值不超过60000
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Status(self):
        """游戏服务器会话状态（ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusReason(self):
        """游戏服务器会话状态附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason

    @property
    def TerminationTime(self):
        """终止的时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TerminationTime

    @TerminationTime.setter
    def TerminationTime(self, TerminationTime):
        self._TerminationTime = TerminationTime

    @property
    def InstanceType(self):
        """实例类型，最大长度不超过128个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def CurrentCustomCount(self):
        """当前自定义数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CurrentCustomCount

    @CurrentCustomCount.setter
    def CurrentCustomCount(self, CurrentCustomCount):
        self._CurrentCustomCount = CurrentCustomCount

    @property
    def MaxCustomCount(self):
        """最大自定义数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxCustomCount

    @MaxCustomCount.setter
    def MaxCustomCount(self, MaxCustomCount):
        self._MaxCustomCount = MaxCustomCount

    @property
    def Weight(self):
        """权重
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def AvailabilityStatus(self):
        """会话可用性状态，是否被屏蔽（Enable,Disable）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AvailabilityStatus

    @AvailabilityStatus.setter
    def AvailabilityStatus(self, AvailabilityStatus):
        self._AvailabilityStatus = AvailabilityStatus


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._CreatorId = params.get("CreatorId")
        self._CurrentPlayerSessionCount = params.get("CurrentPlayerSessionCount")
        self._DnsName = params.get("DnsName")
        self._FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._GameServerSessionData = params.get("GameServerSessionData")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._IpAddress = params.get("IpAddress")
        self._MatchmakerData = params.get("MatchmakerData")
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self._Name = params.get("Name")
        self._PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self._Port = params.get("Port")
        self._Status = params.get("Status")
        self._StatusReason = params.get("StatusReason")
        self._TerminationTime = params.get("TerminationTime")
        self._InstanceType = params.get("InstanceType")
        self._CurrentCustomCount = params.get("CurrentCustomCount")
        self._MaxCustomCount = params.get("MaxCustomCount")
        self._Weight = params.get("Weight")
        self._AvailabilityStatus = params.get("AvailabilityStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionDetail(AbstractModel):
    """游戏服务器会话详情（GameServerSessionDetail）

    """

    def __init__(self):
        r"""
        :param _GameServerSession: 游戏服务器会话
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param _ProtectionPolicy: 保护策略，可选（NoProtection,FullProtection）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectionPolicy: str
        """
        self._GameServerSession = None
        self._ProtectionPolicy = None

    @property
    def GameServerSession(self):
        """游戏服务器会话
        :rtype: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        """
        return self._GameServerSession

    @GameServerSession.setter
    def GameServerSession(self, GameServerSession):
        self._GameServerSession = GameServerSession

    @property
    def ProtectionPolicy(self):
        """保护策略，可选（NoProtection,FullProtection）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProtectionPolicy

    @ProtectionPolicy.setter
    def ProtectionPolicy(self, ProtectionPolicy):
        self._ProtectionPolicy = ProtectionPolicy


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self._GameServerSession = GameServerSession()
            self._GameServerSession._deserialize(params.get("GameServerSession"))
        self._ProtectionPolicy = params.get("ProtectionPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionPlacement(AbstractModel):
    """游戏会话部署对象

    """

    def __init__(self):
        r"""
        :param _PlacementId: 部署Id
        :type PlacementId: str
        :param _GameServerSessionQueueName: 服务部署组名称
        :type GameServerSessionQueueName: str
        :param _PlayerLatencies: 玩家延迟
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerLatencies: list of PlayerLatency
        :param _Status: 服务部署状态
        :type Status: str
        :param _DnsName: 分配给正在运行游戏会话的实例的DNS标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param _GameServerSessionId: 游戏会话Id
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionId: str
        :param _GameServerSessionName: 游戏会话名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionName: str
        :param _GameServerSessionRegion: 服务部署区域
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionRegion: str
        :param _GameProperties: 游戏属性
注意：此字段可能返回 null，表示取不到有效值。
        :type GameProperties: list of GameProperty
        :param _MaximumPlayerSessionCount: 游戏服务器允许同时连接到游戏会话的最大玩家数量，最小值1，最大值为玩家会话最大限额
        :type MaximumPlayerSessionCount: int
        :param _GameServerSessionData: 游戏会话数据
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionData: str
        :param _IpAddress: 运行游戏会话的实例的IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IpAddress: str
        :param _Port: 运行游戏会话的实例的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _MatchmakerData: 游戏匹配数据
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchmakerData: str
        :param _PlacedPlayerSessions: 部署的玩家游戏数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PlacedPlayerSessions: list of PlacedPlayerSession
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._PlacementId = None
        self._GameServerSessionQueueName = None
        self._PlayerLatencies = None
        self._Status = None
        self._DnsName = None
        self._GameServerSessionId = None
        self._GameServerSessionName = None
        self._GameServerSessionRegion = None
        self._GameProperties = None
        self._MaximumPlayerSessionCount = None
        self._GameServerSessionData = None
        self._IpAddress = None
        self._Port = None
        self._MatchmakerData = None
        self._PlacedPlayerSessions = None
        self._StartTime = None
        self._EndTime = None

    @property
    def PlacementId(self):
        """部署Id
        :rtype: str
        """
        return self._PlacementId

    @PlacementId.setter
    def PlacementId(self, PlacementId):
        self._PlacementId = PlacementId

    @property
    def GameServerSessionQueueName(self):
        """服务部署组名称
        :rtype: str
        """
        return self._GameServerSessionQueueName

    @GameServerSessionQueueName.setter
    def GameServerSessionQueueName(self, GameServerSessionQueueName):
        self._GameServerSessionQueueName = GameServerSessionQueueName

    @property
    def PlayerLatencies(self):
        """玩家延迟
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PlayerLatency
        """
        return self._PlayerLatencies

    @PlayerLatencies.setter
    def PlayerLatencies(self, PlayerLatencies):
        self._PlayerLatencies = PlayerLatencies

    @property
    def Status(self):
        """服务部署状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DnsName(self):
        """分配给正在运行游戏会话的实例的DNS标识符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DnsName

    @DnsName.setter
    def DnsName(self, DnsName):
        self._DnsName = DnsName

    @property
    def GameServerSessionId(self):
        """游戏会话Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def GameServerSessionName(self):
        """游戏会话名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GameServerSessionName

    @GameServerSessionName.setter
    def GameServerSessionName(self, GameServerSessionName):
        self._GameServerSessionName = GameServerSessionName

    @property
    def GameServerSessionRegion(self):
        """服务部署区域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GameServerSessionRegion

    @GameServerSessionRegion.setter
    def GameServerSessionRegion(self, GameServerSessionRegion):
        self._GameServerSessionRegion = GameServerSessionRegion

    @property
    def GameProperties(self):
        """游戏属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of GameProperty
        """
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def MaximumPlayerSessionCount(self):
        """游戏服务器允许同时连接到游戏会话的最大玩家数量，最小值1，最大值为玩家会话最大限额
        :rtype: int
        """
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount

    @property
    def GameServerSessionData(self):
        """游戏会话数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GameServerSessionData

    @GameServerSessionData.setter
    def GameServerSessionData(self, GameServerSessionData):
        self._GameServerSessionData = GameServerSessionData

    @property
    def IpAddress(self):
        """运行游戏会话的实例的IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def Port(self):
        """运行游戏会话的实例的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def MatchmakerData(self):
        """游戏匹配数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MatchmakerData

    @MatchmakerData.setter
    def MatchmakerData(self, MatchmakerData):
        self._MatchmakerData = MatchmakerData

    @property
    def PlacedPlayerSessions(self):
        """部署的玩家游戏数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PlacedPlayerSession
        """
        return self._PlacedPlayerSessions

    @PlacedPlayerSessions.setter
    def PlacedPlayerSessions(self, PlacedPlayerSessions):
        self._PlacedPlayerSessions = PlacedPlayerSessions

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._PlacementId = params.get("PlacementId")
        self._GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        if params.get("PlayerLatencies") is not None:
            self._PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self._PlayerLatencies.append(obj)
        self._Status = params.get("Status")
        self._DnsName = params.get("DnsName")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._GameServerSessionName = params.get("GameServerSessionName")
        self._GameServerSessionRegion = params.get("GameServerSessionRegion")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self._GameServerSessionData = params.get("GameServerSessionData")
        self._IpAddress = params.get("IpAddress")
        self._Port = params.get("Port")
        self._MatchmakerData = params.get("MatchmakerData")
        if params.get("PlacedPlayerSessions") is not None:
            self._PlacedPlayerSessions = []
            for item in params.get("PlacedPlayerSessions"):
                obj = PlacedPlayerSession()
                obj._deserialize(item)
                self._PlacedPlayerSessions.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionQueue(AbstractModel):
    """服务部署组对象

    """

    def __init__(self):
        r"""
        :param _Name: 服务部署组名字
        :type Name: str
        :param _GameServerSessionQueueArn: 服务部署组资源
        :type GameServerSessionQueueArn: str
        :param _Destinations: 目的fleet（可为别名）列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Destinations: list of GameServerSessionQueueDestination
        :param _PlayerLatencyPolicies: 延迟策略集合
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerLatencyPolicies: list of PlayerLatencyPolicy
        :param _TimeoutInSeconds: 超时时间
        :type TimeoutInSeconds: int
        :param _Tags: 标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._Name = None
        self._GameServerSessionQueueArn = None
        self._Destinations = None
        self._PlayerLatencyPolicies = None
        self._TimeoutInSeconds = None
        self._Tags = None

    @property
    def Name(self):
        """服务部署组名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def GameServerSessionQueueArn(self):
        """服务部署组资源
        :rtype: str
        """
        return self._GameServerSessionQueueArn

    @GameServerSessionQueueArn.setter
    def GameServerSessionQueueArn(self, GameServerSessionQueueArn):
        self._GameServerSessionQueueArn = GameServerSessionQueueArn

    @property
    def Destinations(self):
        """目的fleet（可为别名）列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of GameServerSessionQueueDestination
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def PlayerLatencyPolicies(self):
        """延迟策略集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PlayerLatencyPolicy
        """
        return self._PlayerLatencyPolicies

    @PlayerLatencyPolicies.setter
    def PlayerLatencyPolicies(self, PlayerLatencyPolicies):
        self._PlayerLatencyPolicies = PlayerLatencyPolicies

    @property
    def TimeoutInSeconds(self):
        """超时时间
        :rtype: int
        """
        return self._TimeoutInSeconds

    @TimeoutInSeconds.setter
    def TimeoutInSeconds(self, TimeoutInSeconds):
        self._TimeoutInSeconds = TimeoutInSeconds

    @property
    def Tags(self):
        """标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._GameServerSessionQueueArn = params.get("GameServerSessionQueueArn")
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = GameServerSessionQueueDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        if params.get("PlayerLatencyPolicies") is not None:
            self._PlayerLatencyPolicies = []
            for item in params.get("PlayerLatencyPolicies"):
                obj = PlayerLatencyPolicy()
                obj._deserialize(item)
                self._PlayerLatencyPolicies.append(obj)
        self._TimeoutInSeconds = params.get("TimeoutInSeconds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionQueueDestination(AbstractModel):
    """服务部署组目的集合

    """

    def __init__(self):
        r"""
        :param _DestinationArn: 服务部署组目的的资源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DestinationArn: str
        :param _FleetStatus: 服务部署组目的的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetStatus: str
        """
        self._DestinationArn = None
        self._FleetStatus = None

    @property
    def DestinationArn(self):
        """服务部署组目的的资源描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DestinationArn

    @DestinationArn.setter
    def DestinationArn(self, DestinationArn):
        self._DestinationArn = DestinationArn

    @property
    def FleetStatus(self):
        """服务部署组目的的状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetStatus

    @FleetStatus.setter
    def FleetStatus(self, FleetStatus):
        self._FleetStatus = FleetStatus


    def _deserialize(self, params):
        self._DestinationArn = params.get("DestinationArn")
        self._FleetStatus = params.get("FleetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGameServerInstanceLogUrlRequest(AbstractModel):
    """GetGameServerInstanceLogUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 游戏舰队ID
        :type FleetId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ServerIp: 实例IP
        :type ServerIp: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Size: 每次条数
        :type Size: int
        """
        self._FleetId = None
        self._InstanceId = None
        self._ServerIp = None
        self._Offset = None
        self._Size = None

    @property
    def FleetId(self):
        """游戏舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServerIp(self):
        """实例IP
        :rtype: str
        """
        return self._ServerIp

    @ServerIp.setter
    def ServerIp(self, ServerIp):
        self._ServerIp = ServerIp

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Size(self):
        """每次条数
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        self._ServerIp = params.get("ServerIp")
        self._Offset = params.get("Offset")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGameServerInstanceLogUrlResponse(AbstractModel):
    """GetGameServerInstanceLogUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PresignedUrls: 日志下载URL的数组，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type PresignedUrls: list of str
        :param _Total: 总条数
        :type Total: int
        :param _HasNext: 是否还有没拉取完的
        :type HasNext: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PresignedUrls = None
        self._Total = None
        self._HasNext = None
        self._RequestId = None

    @property
    def PresignedUrls(self):
        """日志下载URL的数组，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._PresignedUrls

    @PresignedUrls.setter
    def PresignedUrls(self, PresignedUrls):
        self._PresignedUrls = PresignedUrls

    @property
    def Total(self):
        """总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def HasNext(self):
        """是否还有没拉取完的
        :rtype: bool
        """
        return self._HasNext

    @HasNext.setter
    def HasNext(self, HasNext):
        self._HasNext = HasNext

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PresignedUrls = params.get("PresignedUrls")
        self._Total = params.get("Total")
        self._HasNext = params.get("HasNext")
        self._RequestId = params.get("RequestId")


class GetGameServerSessionLogUrlRequest(AbstractModel):
    """GetGameServerSessionLogUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: 游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符
        :type GameServerSessionId: str
        """
        self._GameServerSessionId = None

    @property
    def GameServerSessionId(self):
        """游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGameServerSessionLogUrlResponse(AbstractModel):
    """GetGameServerSessionLogUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PreSignedUrl: 日志下载URL，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type PreSignedUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PreSignedUrl = None
        self._RequestId = None

    @property
    def PreSignedUrl(self):
        """日志下载URL，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PreSignedUrl

    @PreSignedUrl.setter
    def PreSignedUrl(self, PreSignedUrl):
        self._PreSignedUrl = PreSignedUrl

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PreSignedUrl = params.get("PreSignedUrl")
        self._RequestId = params.get("RequestId")


class GetInstanceAccessRequest(AbstractModel):
    """GetInstanceAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
        :type FleetId: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        """
        self._FleetId = None
        self._InstanceId = None

    @property
    def FleetId(self):
        """服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetInstanceAccessResponse(AbstractModel):
    """GetInstanceAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceAccess: 实例登录所需要的凭据
        :type InstanceAccess: :class:`tencentcloud.gse.v20191112.models.InstanceAccess`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceAccess = None
        self._RequestId = None

    @property
    def InstanceAccess(self):
        """实例登录所需要的凭据
        :rtype: :class:`tencentcloud.gse.v20191112.models.InstanceAccess`
        """
        return self._InstanceAccess

    @InstanceAccess.setter
    def InstanceAccess(self, InstanceAccess):
        self._InstanceAccess = InstanceAccess

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceAccess") is not None:
            self._InstanceAccess = InstanceAccess()
            self._InstanceAccess._deserialize(params.get("InstanceAccess"))
        self._RequestId = params.get("RequestId")


class GetUploadCredentialsRequest(AbstractModel):
    """GetUploadCredentials请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetRegion: 生成包所在地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)
        :type AssetRegion: str
        :param _BucketKey: 生成包的ZIP包名，例如：server.zip
        :type BucketKey: str
        """
        self._AssetRegion = None
        self._BucketKey = None

    @property
    def AssetRegion(self):
        """生成包所在地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)
        :rtype: str
        """
        return self._AssetRegion

    @AssetRegion.setter
    def AssetRegion(self, AssetRegion):
        self._AssetRegion = AssetRegion

    @property
    def BucketKey(self):
        """生成包的ZIP包名，例如：server.zip
        :rtype: str
        """
        return self._BucketKey

    @BucketKey.setter
    def BucketKey(self, BucketKey):
        self._BucketKey = BucketKey


    def _deserialize(self, params):
        self._AssetRegion = params.get("AssetRegion")
        self._BucketKey = params.get("BucketKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUploadCredentialsResponse(AbstractModel):
    """GetUploadCredentials返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BucketAuth: 上传文件授权信息Auth
        :type BucketAuth: str
        :param _BucketName: Bucket名字
        :type BucketName: str
        :param _AssetRegion: 生成包所在地域
        :type AssetRegion: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BucketAuth = None
        self._BucketName = None
        self._AssetRegion = None
        self._RequestId = None

    @property
    def BucketAuth(self):
        """上传文件授权信息Auth
        :rtype: str
        """
        return self._BucketAuth

    @BucketAuth.setter
    def BucketAuth(self, BucketAuth):
        self._BucketAuth = BucketAuth

    @property
    def BucketName(self):
        """Bucket名字
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def AssetRegion(self):
        """生成包所在地域
        :rtype: str
        """
        return self._AssetRegion

    @AssetRegion.setter
    def AssetRegion(self, AssetRegion):
        self._AssetRegion = AssetRegion

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BucketAuth = params.get("BucketAuth")
        self._BucketName = params.get("BucketName")
        self._AssetRegion = params.get("AssetRegion")
        self._RequestId = params.get("RequestId")


class GetUploadFederationTokenRequest(AbstractModel):
    """GetUploadFederationToken请求参数结构体

    """


class GetUploadFederationTokenResponse(AbstractModel):
    """GetUploadFederationToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExpiredTime: 临时证书的过期时间，Unix 时间戳，精确到秒
        :type ExpiredTime: int
        :param _AssetCredentials: 临时证书
        :type AssetCredentials: :class:`tencentcloud.gse.v20191112.models.AssetCredentials`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExpiredTime = None
        self._AssetCredentials = None
        self._RequestId = None

    @property
    def ExpiredTime(self):
        """临时证书的过期时间，Unix 时间戳，精确到秒
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def AssetCredentials(self):
        """临时证书
        :rtype: :class:`tencentcloud.gse.v20191112.models.AssetCredentials`
        """
        return self._AssetCredentials

    @AssetCredentials.setter
    def AssetCredentials(self, AssetCredentials):
        self._AssetCredentials = AssetCredentials

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExpiredTime = params.get("ExpiredTime")
        if params.get("AssetCredentials") is not None:
            self._AssetCredentials = AssetCredentials()
            self._AssetCredentials._deserialize(params.get("AssetCredentials"))
        self._RequestId = params.get("RequestId")


class InboundPermission(AbstractModel):
    """允许网络访问范围

    """

    def __init__(self):
        r"""
        :param _FromPort: 起始端口号，最小值1025
        :type FromPort: int
        :param _IpRange: IP 段范围，合法的 CIDR 地址类型，如所有IPv4来源：0.0.0.0/0
        :type IpRange: str
        :param _Protocol: 协议类型：TCP或者UDP
        :type Protocol: str
        :param _ToPort: 终止端口号，最大值60000
        :type ToPort: int
        """
        self._FromPort = None
        self._IpRange = None
        self._Protocol = None
        self._ToPort = None

    @property
    def FromPort(self):
        """起始端口号，最小值1025
        :rtype: int
        """
        return self._FromPort

    @FromPort.setter
    def FromPort(self, FromPort):
        self._FromPort = FromPort

    @property
    def IpRange(self):
        """IP 段范围，合法的 CIDR 地址类型，如所有IPv4来源：0.0.0.0/0
        :rtype: str
        """
        return self._IpRange

    @IpRange.setter
    def IpRange(self, IpRange):
        self._IpRange = IpRange

    @property
    def Protocol(self):
        """协议类型：TCP或者UDP
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ToPort(self):
        """终止端口号，最大值60000
        :rtype: int
        """
        return self._ToPort

    @ToPort.setter
    def ToPort(self, ToPort):
        self._ToPort = ToPort


    def _deserialize(self, params):
        self._FromPort = params.get("FromPort")
        self._IpRange = params.get("IpRange")
        self._Protocol = params.get("Protocol")
        self._ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InboundPermissionAuthorization(AbstractModel):
    """用于新增安全组

    """

    def __init__(self):
        r"""
        :param _FromPort: 起始端口号
        :type FromPort: int
        :param _IpRange: IP 端范围，CIDR方式划分
        :type IpRange: str
        :param _Protocol: 协议类型
        :type Protocol: str
        :param _ToPort: 终止端口号
        :type ToPort: int
        """
        self._FromPort = None
        self._IpRange = None
        self._Protocol = None
        self._ToPort = None

    @property
    def FromPort(self):
        """起始端口号
        :rtype: int
        """
        return self._FromPort

    @FromPort.setter
    def FromPort(self, FromPort):
        self._FromPort = FromPort

    @property
    def IpRange(self):
        """IP 端范围，CIDR方式划分
        :rtype: str
        """
        return self._IpRange

    @IpRange.setter
    def IpRange(self, IpRange):
        self._IpRange = IpRange

    @property
    def Protocol(self):
        """协议类型
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ToPort(self):
        """终止端口号
        :rtype: int
        """
        return self._ToPort

    @ToPort.setter
    def ToPort(self, ToPort):
        self._ToPort = ToPort


    def _deserialize(self, params):
        self._FromPort = params.get("FromPort")
        self._IpRange = params.get("IpRange")
        self._Protocol = params.get("Protocol")
        self._ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InboundPermissionRevocations(AbstractModel):
    """需要移除的安全组

    """

    def __init__(self):
        r"""
        :param _FromPort: 起始端口号
        :type FromPort: int
        :param _IpRange: IP 端范围，CIDR 方式换分
        :type IpRange: str
        :param _Protocol: 协议类型：UDP或者TCP
        :type Protocol: str
        :param _ToPort: 终止端口号
        :type ToPort: int
        """
        self._FromPort = None
        self._IpRange = None
        self._Protocol = None
        self._ToPort = None

    @property
    def FromPort(self):
        """起始端口号
        :rtype: int
        """
        return self._FromPort

    @FromPort.setter
    def FromPort(self, FromPort):
        self._FromPort = FromPort

    @property
    def IpRange(self):
        """IP 端范围，CIDR 方式换分
        :rtype: str
        """
        return self._IpRange

    @IpRange.setter
    def IpRange(self, IpRange):
        self._IpRange = IpRange

    @property
    def Protocol(self):
        """协议类型：UDP或者TCP
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ToPort(self):
        """终止端口号
        :rtype: int
        """
        return self._ToPort

    @ToPort.setter
    def ToPort(self, ToPort):
        self._ToPort = ToPort


    def _deserialize(self, params):
        self._FromPort = params.get("FromPort")
        self._IpRange = params.get("IpRange")
        self._Protocol = params.get("Protocol")
        self._ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """实例信息

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务部署ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _IpAddress: IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IpAddress: str
        :param _DnsName: dns
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param _OperatingSystem: 操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatingSystem: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Weight: 实例权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _ReserveValue: 实例是否保留, 1-保留，0-不保留,默认
注意：此字段可能返回 null，表示取不到有效值。
        :type ReserveValue: int
        :param _PrivateIpAddress: 实例的私有IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddress: str
        """
        self._FleetId = None
        self._InstanceId = None
        self._IpAddress = None
        self._DnsName = None
        self._OperatingSystem = None
        self._Status = None
        self._Type = None
        self._CreateTime = None
        self._Weight = None
        self._ReserveValue = None
        self._PrivateIpAddress = None

    @property
    def FleetId(self):
        """服务部署ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        """实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpAddress(self):
        """IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def DnsName(self):
        """dns
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DnsName

    @DnsName.setter
    def DnsName(self, DnsName):
        self._DnsName = DnsName

    @property
    def OperatingSystem(self):
        """操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OperatingSystem

    @OperatingSystem.setter
    def OperatingSystem(self, OperatingSystem):
        self._OperatingSystem = OperatingSystem

    @property
    def Status(self):
        """状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Weight(self):
        """实例权重
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def ReserveValue(self):
        """实例是否保留, 1-保留，0-不保留,默认
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReserveValue

    @ReserveValue.setter
    def ReserveValue(self, ReserveValue):
        self._ReserveValue = ReserveValue

    @property
    def PrivateIpAddress(self):
        """实例的私有IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        self._IpAddress = params.get("IpAddress")
        self._DnsName = params.get("DnsName")
        self._OperatingSystem = params.get("OperatingSystem")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        self._Weight = params.get("Weight")
        self._ReserveValue = params.get("ReserveValue")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAccess(AbstractModel):
    """实例访问凭证信息

    """

    def __init__(self):
        r"""
        :param _Credentials: 访问实例所需要的凭据
        :type Credentials: :class:`tencentcloud.gse.v20191112.models.Credentials`
        :param _FleetId: 服务部署Id
        :type FleetId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _IpAddress: 实例公网IP
        :type IpAddress: str
        :param _OperatingSystem: 操作系统
        :type OperatingSystem: str
        """
        self._Credentials = None
        self._FleetId = None
        self._InstanceId = None
        self._IpAddress = None
        self._OperatingSystem = None

    @property
    def Credentials(self):
        """访问实例所需要的凭据
        :rtype: :class:`tencentcloud.gse.v20191112.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def FleetId(self):
        """服务部署Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpAddress(self):
        """实例公网IP
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def OperatingSystem(self):
        """操作系统
        :rtype: str
        """
        return self._OperatingSystem

    @OperatingSystem.setter
    def OperatingSystem(self, OperatingSystem):
        self._OperatingSystem = OperatingSystem


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        self._IpAddress = params.get("IpAddress")
        self._OperatingSystem = params.get("OperatingSystem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceCounts(AbstractModel):
    """服务器实例统计数据

    """

    def __init__(self):
        r"""
        :param _Active: 活跃的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Active: int
        :param _Desired: 期望的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Desired: int
        :param _Idle: 空闲的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Idle: int
        :param _MaxiNum: 服务器实例数最大限制
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxiNum: int
        :param _MiniNum: 服务器实例数最小限制
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniNum: int
        :param _Pending: 已开始创建，但未激活的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pending: int
        :param _Terminating: 结束中的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type Terminating: int
        """
        self._Active = None
        self._Desired = None
        self._Idle = None
        self._MaxiNum = None
        self._MiniNum = None
        self._Pending = None
        self._Terminating = None

    @property
    def Active(self):
        """活跃的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Active

    @Active.setter
    def Active(self, Active):
        self._Active = Active

    @property
    def Desired(self):
        """期望的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Desired

    @Desired.setter
    def Desired(self, Desired):
        self._Desired = Desired

    @property
    def Idle(self):
        """空闲的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Idle

    @Idle.setter
    def Idle(self, Idle):
        self._Idle = Idle

    @property
    def MaxiNum(self):
        """服务器实例数最大限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxiNum

    @MaxiNum.setter
    def MaxiNum(self, MaxiNum):
        self._MaxiNum = MaxiNum

    @property
    def MiniNum(self):
        """服务器实例数最小限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MiniNum

    @MiniNum.setter
    def MiniNum(self, MiniNum):
        self._MiniNum = MiniNum

    @property
    def Pending(self):
        """已开始创建，但未激活的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Pending

    @Pending.setter
    def Pending(self, Pending):
        self._Pending = Pending

    @property
    def Terminating(self):
        """结束中的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Terminating

    @Terminating.setter
    def Terminating(self, Terminating):
        self._Terminating = Terminating


    def _deserialize(self, params):
        self._Active = params.get("Active")
        self._Desired = params.get("Desired")
        self._Idle = params.get("Idle")
        self._MaxiNum = params.get("MaxiNum")
        self._MiniNum = params.get("MiniNum")
        self._Pending = params.get("Pending")
        self._Terminating = params.get("Terminating")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExtend(AbstractModel):
    """实例扩展信息

    """

    def __init__(self):
        r"""
        :param _Instance: 实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Instance: :class:`tencentcloud.gse.v20191112.models.Instance`
        :param _State: 实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _HealthyProcessCnt: 健康进程数
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthyProcessCnt: int
        :param _ActiveProcessCnt: 活跃进程数
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveProcessCnt: int
        :param _GameSessionCnt: 当前游戏会话总数
注意：此字段可能返回 null，表示取不到有效值。
        :type GameSessionCnt: int
        :param _MaxGameSessionCnt: 最大游戏会话数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxGameSessionCnt: int
        :param _PlayerSessionCnt: 当前玩家会话数
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSessionCnt: int
        :param _MaxPlayerSessionCnt: 最大玩家会话数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPlayerSessionCnt: int
        """
        self._Instance = None
        self._State = None
        self._HealthyProcessCnt = None
        self._ActiveProcessCnt = None
        self._GameSessionCnt = None
        self._MaxGameSessionCnt = None
        self._PlayerSessionCnt = None
        self._MaxPlayerSessionCnt = None

    @property
    def Instance(self):
        """实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.Instance`
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def State(self):
        """实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def HealthyProcessCnt(self):
        """健康进程数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HealthyProcessCnt

    @HealthyProcessCnt.setter
    def HealthyProcessCnt(self, HealthyProcessCnt):
        self._HealthyProcessCnt = HealthyProcessCnt

    @property
    def ActiveProcessCnt(self):
        """活跃进程数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ActiveProcessCnt

    @ActiveProcessCnt.setter
    def ActiveProcessCnt(self, ActiveProcessCnt):
        self._ActiveProcessCnt = ActiveProcessCnt

    @property
    def GameSessionCnt(self):
        """当前游戏会话总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._GameSessionCnt

    @GameSessionCnt.setter
    def GameSessionCnt(self, GameSessionCnt):
        self._GameSessionCnt = GameSessionCnt

    @property
    def MaxGameSessionCnt(self):
        """最大游戏会话数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxGameSessionCnt

    @MaxGameSessionCnt.setter
    def MaxGameSessionCnt(self, MaxGameSessionCnt):
        self._MaxGameSessionCnt = MaxGameSessionCnt

    @property
    def PlayerSessionCnt(self):
        """当前玩家会话数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PlayerSessionCnt

    @PlayerSessionCnt.setter
    def PlayerSessionCnt(self, PlayerSessionCnt):
        self._PlayerSessionCnt = PlayerSessionCnt

    @property
    def MaxPlayerSessionCnt(self):
        """最大玩家会话数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxPlayerSessionCnt

    @MaxPlayerSessionCnt.setter
    def MaxPlayerSessionCnt(self, MaxPlayerSessionCnt):
        self._MaxPlayerSessionCnt = MaxPlayerSessionCnt


    def _deserialize(self, params):
        if params.get("Instance") is not None:
            self._Instance = Instance()
            self._Instance._deserialize(params.get("Instance"))
        self._State = params.get("State")
        self._HealthyProcessCnt = params.get("HealthyProcessCnt")
        self._ActiveProcessCnt = params.get("ActiveProcessCnt")
        self._GameSessionCnt = params.get("GameSessionCnt")
        self._MaxGameSessionCnt = params.get("MaxGameSessionCnt")
        self._PlayerSessionCnt = params.get("PlayerSessionCnt")
        self._MaxPlayerSessionCnt = params.get("MaxPlayerSessionCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeInfo(AbstractModel):
    """服务器实例类型信息

    """

    def __init__(self):
        r"""
        :param _TypeName: 类型名，例如“标准型SA1”
        :type TypeName: str
        :param _InstanceType: 类型，例如"SA1.SMALL1"
        :type InstanceType: str
        :param _Cpu: CPU，例如1核就是1
        :type Cpu: int
        :param _Memory: 内存，例如2G就是2
        :type Memory: int
        :param _NetworkCard: 网络收到包,例如25万PPS就是25
        :type NetworkCard: int
        """
        self._TypeName = None
        self._InstanceType = None
        self._Cpu = None
        self._Memory = None
        self._NetworkCard = None

    @property
    def TypeName(self):
        """类型名，例如“标准型SA1”
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def InstanceType(self):
        """类型，例如"SA1.SMALL1"
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Cpu(self):
        """CPU，例如1核就是1
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """内存，例如2G就是2
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def NetworkCard(self):
        """网络收到包,例如25万PPS就是25
        :rtype: int
        """
        return self._NetworkCard

    @NetworkCard.setter
    def NetworkCard(self, NetworkCard):
        self._NetworkCard = NetworkCard


    def _deserialize(self, params):
        self._TypeName = params.get("TypeName")
        self._InstanceType = params.get("InstanceType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._NetworkCard = params.get("NetworkCard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionBatchRequest(AbstractModel):
    """JoinGameServerSessionBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: 游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符
        :type GameServerSessionId: str
        :param _PlayerIds: 玩家ID列表，最小1组，最大25组
        :type PlayerIds: list of str
        :param _PlayerDataMap: 玩家自定义数据
        :type PlayerDataMap: :class:`tencentcloud.gse.v20191112.models.PlayerDataMap`
        """
        self._GameServerSessionId = None
        self._PlayerIds = None
        self._PlayerDataMap = None

    @property
    def GameServerSessionId(self):
        """游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def PlayerIds(self):
        """玩家ID列表，最小1组，最大25组
        :rtype: list of str
        """
        return self._PlayerIds

    @PlayerIds.setter
    def PlayerIds(self, PlayerIds):
        self._PlayerIds = PlayerIds

    @property
    def PlayerDataMap(self):
        """玩家自定义数据
        :rtype: :class:`tencentcloud.gse.v20191112.models.PlayerDataMap`
        """
        return self._PlayerDataMap

    @PlayerDataMap.setter
    def PlayerDataMap(self, PlayerDataMap):
        self._PlayerDataMap = PlayerDataMap


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._PlayerIds = params.get("PlayerIds")
        if params.get("PlayerDataMap") is not None:
            self._PlayerDataMap = PlayerDataMap()
            self._PlayerDataMap._deserialize(params.get("PlayerDataMap"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionBatchResponse(AbstractModel):
    """JoinGameServerSessionBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlayerSessions: 玩家会话列表，最大25组
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSessions: list of PlayerSession
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlayerSessions = None
        self._RequestId = None

    @property
    def PlayerSessions(self):
        """玩家会话列表，最大25组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PlayerSession
        """
        return self._PlayerSessions

    @PlayerSessions.setter
    def PlayerSessions(self, PlayerSessions):
        self._PlayerSessions = PlayerSessions

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self._PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self._PlayerSessions.append(obj)
        self._RequestId = params.get("RequestId")


class JoinGameServerSessionRequest(AbstractModel):
    """JoinGameServerSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: 游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符
        :type GameServerSessionId: str
        :param _PlayerId: 玩家ID，最大长度1024个ASCII字符
        :type PlayerId: str
        :param _PlayerData: 玩家自定义数据，最大长度2048个ASCII字符
        :type PlayerData: str
        """
        self._GameServerSessionId = None
        self._PlayerId = None
        self._PlayerData = None

    @property
    def GameServerSessionId(self):
        """游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def PlayerId(self):
        """玩家ID，最大长度1024个ASCII字符
        :rtype: str
        """
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def PlayerData(self):
        """玩家自定义数据，最大长度2048个ASCII字符
        :rtype: str
        """
        return self._PlayerData

    @PlayerData.setter
    def PlayerData(self, PlayerData):
        self._PlayerData = PlayerData


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._PlayerId = params.get("PlayerId")
        self._PlayerData = params.get("PlayerData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionResponse(AbstractModel):
    """JoinGameServerSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlayerSession: 玩家会话
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSession: :class:`tencentcloud.gse.v20191112.models.PlayerSession`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlayerSession = None
        self._RequestId = None

    @property
    def PlayerSession(self):
        """玩家会话
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.PlayerSession`
        """
        return self._PlayerSession

    @PlayerSession.setter
    def PlayerSession(self, PlayerSession):
        self._PlayerSession = PlayerSession

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlayerSession") is not None:
            self._PlayerSession = PlayerSession()
            self._PlayerSession._deserialize(params.get("PlayerSession"))
        self._RequestId = params.get("RequestId")


class ListAliasesRequest(AbstractModel):
    """ListAliases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名字，长度不小于1字符不超过1024字符
        :type Name: str
        :param _RoutingStrategyType: 路由策略类型，有效值常规别名(SIMPLE)、终止别名(TERMINAL)
        :type RoutingStrategyType: str
        :param _Limit: 要返回的最大结果数，最小值1
        :type Limit: int
        :param _Offset: 偏移，默认0
        :type Offset: int
        :param _OrderBy: 排序字段，例如CreationTime
        :type OrderBy: str
        :param _OrderWay: 排序方式，有效值asc|desc
        :type OrderWay: str
        :param _Filters: 资源过滤字段，可以按照资源名称和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（舰队当前仅支持单个名称的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]
        :type Filters: list of Filter
        """
        self._Name = None
        self._RoutingStrategyType = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderWay = None
        self._Filters = None

    @property
    def Name(self):
        """名字，长度不小于1字符不超过1024字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoutingStrategyType(self):
        """路由策略类型，有效值常规别名(SIMPLE)、终止别名(TERMINAL)
        :rtype: str
        """
        return self._RoutingStrategyType

    @RoutingStrategyType.setter
    def RoutingStrategyType(self, RoutingStrategyType):
        self._RoutingStrategyType = RoutingStrategyType

    @property
    def Limit(self):
        """要返回的最大结果数，最小值1
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """排序字段，例如CreationTime
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderWay(self):
        """排序方式，有效值asc|desc
        :rtype: str
        """
        return self._OrderWay

    @OrderWay.setter
    def OrderWay(self, OrderWay):
        self._OrderWay = OrderWay

    @property
    def Filters(self):
        """资源过滤字段，可以按照资源名称和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（舰队当前仅支持单个名称的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RoutingStrategyType = params.get("RoutingStrategyType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderWay = params.get("OrderWay")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAliasesResponse(AbstractModel):
    """ListAliases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Aliases: 别名对象数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Aliases: list of Alias
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Aliases = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Aliases(self):
        """别名对象数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Alias
        """
        return self._Aliases

    @Aliases.setter
    def Aliases(self, Aliases):
        self._Aliases = Aliases

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Aliases") is not None:
            self._Aliases = []
            for item in params.get("Aliases"):
                obj = Alias()
                obj._deserialize(item)
                self._Aliases.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListFleetsRequest(AbstractModel):
    """ListFleets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 生成包 Id
        :type AssetId: str
        :param _Limit: 结果返回最大值，暂未使用
        :type Limit: int
        :param _Offset: 结果返回偏移，暂未使用
        :type Offset: int
        :param _Filters: 资源过滤字段，可以按照资源名称和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（当前仅支持单个名称的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]
        :type Filters: list of Filter
        """
        self._AssetId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def AssetId(self):
        """生成包 Id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Limit(self):
        """结果返回最大值，暂未使用
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """结果返回偏移，暂未使用
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """资源过滤字段，可以按照资源名称和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（当前仅支持单个名称的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListFleetsResponse(AbstractModel):
    """ListFleets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetIds: 服务器舰队 Id 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetIds: list of str
        :param _TotalCount: 服务器舰队 Id 总数，最小值0
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetIds = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FleetIds(self):
        """服务器舰队 Id 列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FleetIds

    @FleetIds.setter
    def FleetIds(self, FleetIds):
        self._FleetIds = FleetIds

    @property
    def TotalCount(self):
        """服务器舰队 Id 总数，最小值0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FleetIds = params.get("FleetIds")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class PlacedPlayerSession(AbstractModel):
    """部署的玩家游戏会话

    """

    def __init__(self):
        r"""
        :param _PlayerId: 玩家Id
        :type PlayerId: str
        :param _PlayerSessionId: 玩家会话Id
        :type PlayerSessionId: str
        """
        self._PlayerId = None
        self._PlayerSessionId = None

    @property
    def PlayerId(self):
        """玩家Id
        :rtype: str
        """
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def PlayerSessionId(self):
        """玩家会话Id
        :rtype: str
        """
        return self._PlayerSessionId

    @PlayerSessionId.setter
    def PlayerSessionId(self, PlayerSessionId):
        self._PlayerSessionId = PlayerSessionId


    def _deserialize(self, params):
        self._PlayerId = params.get("PlayerId")
        self._PlayerSessionId = params.get("PlayerSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerDataMap(AbstractModel):
    """玩家自定义数据

    """

    def __init__(self):
        r"""
        :param _Key: 玩家自定义数据键，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :type Key: str
        :param _Value: 玩家自定义数据值，最小长度不小于1个ASCII字符，最大长度不超过2048个ASCII字符
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """玩家自定义数据键，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """玩家自定义数据值，最小长度不小于1个ASCII字符，最大长度不超过2048个ASCII字符
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
        


class PlayerLatency(AbstractModel):
    """玩家延迟信息

    """

    def __init__(self):
        r"""
        :param _PlayerId: 玩家Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerId: str
        :param _RegionIdentifier: 延迟对应的区域名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionIdentifier: str
        :param _LatencyInMilliseconds: 毫秒级延迟
        :type LatencyInMilliseconds: int
        """
        self._PlayerId = None
        self._RegionIdentifier = None
        self._LatencyInMilliseconds = None

    @property
    def PlayerId(self):
        """玩家Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def RegionIdentifier(self):
        """延迟对应的区域名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegionIdentifier

    @RegionIdentifier.setter
    def RegionIdentifier(self, RegionIdentifier):
        self._RegionIdentifier = RegionIdentifier

    @property
    def LatencyInMilliseconds(self):
        """毫秒级延迟
        :rtype: int
        """
        return self._LatencyInMilliseconds

    @LatencyInMilliseconds.setter
    def LatencyInMilliseconds(self, LatencyInMilliseconds):
        self._LatencyInMilliseconds = LatencyInMilliseconds


    def _deserialize(self, params):
        self._PlayerId = params.get("PlayerId")
        self._RegionIdentifier = params.get("RegionIdentifier")
        self._LatencyInMilliseconds = params.get("LatencyInMilliseconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerLatencyPolicy(AbstractModel):
    """延迟策略

    """

    def __init__(self):
        r"""
        :param _MaximumIndividualPlayerLatencyMilliseconds: 任意player允许的最大延迟，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type MaximumIndividualPlayerLatencyMilliseconds: int
        :param _PolicyDurationSeconds: 放置新GameServerSession时强制实施策略的时间长度，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDurationSeconds: int
        """
        self._MaximumIndividualPlayerLatencyMilliseconds = None
        self._PolicyDurationSeconds = None

    @property
    def MaximumIndividualPlayerLatencyMilliseconds(self):
        """任意player允许的最大延迟，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaximumIndividualPlayerLatencyMilliseconds

    @MaximumIndividualPlayerLatencyMilliseconds.setter
    def MaximumIndividualPlayerLatencyMilliseconds(self, MaximumIndividualPlayerLatencyMilliseconds):
        self._MaximumIndividualPlayerLatencyMilliseconds = MaximumIndividualPlayerLatencyMilliseconds

    @property
    def PolicyDurationSeconds(self):
        """放置新GameServerSession时强制实施策略的时间长度，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PolicyDurationSeconds

    @PolicyDurationSeconds.setter
    def PolicyDurationSeconds(self, PolicyDurationSeconds):
        self._PolicyDurationSeconds = PolicyDurationSeconds


    def _deserialize(self, params):
        self._MaximumIndividualPlayerLatencyMilliseconds = params.get("MaximumIndividualPlayerLatencyMilliseconds")
        self._PolicyDurationSeconds = params.get("PolicyDurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerSession(AbstractModel):
    """玩家会话详情

    """

    def __init__(self):
        r"""
        :param _CreationTime: 玩家会话创建时间
        :type CreationTime: str
        :param _DnsName: 游戏服务器会话运行的DNS标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param _FleetId: 舰队ID
        :type FleetId: str
        :param _GameServerSessionId: 游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符
        :type GameServerSessionId: str
        :param _IpAddress: 游戏服务器会话运行的CVM地址
        :type IpAddress: str
        :param _PlayerData: 玩家自定义数据，最大长度2048个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerData: str
        :param _PlayerId: 玩家ID，最大长度1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerId: str
        :param _PlayerSessionId: 玩家会话ID
        :type PlayerSessionId: str
        :param _Port: 端口号，最小值不小于1，最大值不超过60000
        :type Port: int
        :param _Status: 玩家会话的状态（RESERVED = 1,ACTIVE = 2,COMPLETED = 3,TIMEDOUT = 4）
        :type Status: str
        :param _TerminationTime: 玩家会话终止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminationTime: str
        """
        self._CreationTime = None
        self._DnsName = None
        self._FleetId = None
        self._GameServerSessionId = None
        self._IpAddress = None
        self._PlayerData = None
        self._PlayerId = None
        self._PlayerSessionId = None
        self._Port = None
        self._Status = None
        self._TerminationTime = None

    @property
    def CreationTime(self):
        """玩家会话创建时间
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def DnsName(self):
        """游戏服务器会话运行的DNS标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DnsName

    @DnsName.setter
    def DnsName(self, DnsName):
        self._DnsName = DnsName

    @property
    def FleetId(self):
        """舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def GameServerSessionId(self):
        """游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def IpAddress(self):
        """游戏服务器会话运行的CVM地址
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def PlayerData(self):
        """玩家自定义数据，最大长度2048个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PlayerData

    @PlayerData.setter
    def PlayerData(self, PlayerData):
        self._PlayerData = PlayerData

    @property
    def PlayerId(self):
        """玩家ID，最大长度1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def PlayerSessionId(self):
        """玩家会话ID
        :rtype: str
        """
        return self._PlayerSessionId

    @PlayerSessionId.setter
    def PlayerSessionId(self, PlayerSessionId):
        self._PlayerSessionId = PlayerSessionId

    @property
    def Port(self):
        """端口号，最小值不小于1，最大值不超过60000
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Status(self):
        """玩家会话的状态（RESERVED = 1,ACTIVE = 2,COMPLETED = 3,TIMEDOUT = 4）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TerminationTime(self):
        """玩家会话终止时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TerminationTime

    @TerminationTime.setter
    def TerminationTime(self, TerminationTime):
        self._TerminationTime = TerminationTime


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._DnsName = params.get("DnsName")
        self._FleetId = params.get("FleetId")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._IpAddress = params.get("IpAddress")
        self._PlayerData = params.get("PlayerData")
        self._PlayerId = params.get("PlayerId")
        self._PlayerSessionId = params.get("PlayerSessionId")
        self._Port = params.get("Port")
        self._Status = params.get("Status")
        self._TerminationTime = params.get("TerminationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutScalingPolicyRequest(AbstractModel):
    """PutScalingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 扩缩容配置服务器舰队ID
        :type FleetId: str
        :param _Name: 扩缩容策略名称，最小长度为1，最大长度为1024
        :type Name: str
        :param _ScalingAdjustment: 扩缩容调整值，ScalingAdjustmentType取值PercentChangeInCapacity时，取值范围-99~99
ScalingAdjustmentType取值ChangeInCapacity或ExactCapacity时，最小值要缩容的最多CVM个数，最大值为实际最大的CVM个数限额
        :type ScalingAdjustment: int
        :param _ScalingAdjustmentType: 扩缩容调整类型，取值（ChangeInCapacity，ExactCapacity，PercentChangeInCapacity）
        :type ScalingAdjustmentType: str
        :param _Threshold: 扩缩容指标阈值
        :type Threshold: float
        :param _ComparisonOperator: 扩缩容策略比较符，取值：>,>=,<,<=
        :type ComparisonOperator: str
        :param _EvaluationPeriods: 单个策略持续时间长度（分钟）
        :type EvaluationPeriods: int
        :param _MetricName: 扩缩容参与计算的指标名称，PolicyType取值RuleBased，
MetricName取值（AvailableGameServerSessions，AvailableCustomCount，PercentAvailableCustomCount，ActiveInstances，IdleInstances，CurrentPlayerSessions和PercentIdleInstances）；
PolicyType取值TargetBased时，MetricName取值PercentAvailableGameSessions
        :type MetricName: str
        :param _PolicyType: 策略类型，取值：TargetBased表示基于目标的策略；RuleBased表示基于规则的策略
        :type PolicyType: str
        :param _TargetConfiguration: 扩缩容目标值配置，只有TargetBased类型的策略生效
        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        self._FleetId = None
        self._Name = None
        self._ScalingAdjustment = None
        self._ScalingAdjustmentType = None
        self._Threshold = None
        self._ComparisonOperator = None
        self._EvaluationPeriods = None
        self._MetricName = None
        self._PolicyType = None
        self._TargetConfiguration = None

    @property
    def FleetId(self):
        """扩缩容配置服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Name(self):
        """扩缩容策略名称，最小长度为1，最大长度为1024
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ScalingAdjustment(self):
        """扩缩容调整值，ScalingAdjustmentType取值PercentChangeInCapacity时，取值范围-99~99
ScalingAdjustmentType取值ChangeInCapacity或ExactCapacity时，最小值要缩容的最多CVM个数，最大值为实际最大的CVM个数限额
        :rtype: int
        """
        return self._ScalingAdjustment

    @ScalingAdjustment.setter
    def ScalingAdjustment(self, ScalingAdjustment):
        self._ScalingAdjustment = ScalingAdjustment

    @property
    def ScalingAdjustmentType(self):
        """扩缩容调整类型，取值（ChangeInCapacity，ExactCapacity，PercentChangeInCapacity）
        :rtype: str
        """
        return self._ScalingAdjustmentType

    @ScalingAdjustmentType.setter
    def ScalingAdjustmentType(self, ScalingAdjustmentType):
        self._ScalingAdjustmentType = ScalingAdjustmentType

    @property
    def Threshold(self):
        """扩缩容指标阈值
        :rtype: float
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def ComparisonOperator(self):
        """扩缩容策略比较符，取值：>,>=,<,<=
        :rtype: str
        """
        return self._ComparisonOperator

    @ComparisonOperator.setter
    def ComparisonOperator(self, ComparisonOperator):
        self._ComparisonOperator = ComparisonOperator

    @property
    def EvaluationPeriods(self):
        """单个策略持续时间长度（分钟）
        :rtype: int
        """
        return self._EvaluationPeriods

    @EvaluationPeriods.setter
    def EvaluationPeriods(self, EvaluationPeriods):
        self._EvaluationPeriods = EvaluationPeriods

    @property
    def MetricName(self):
        """扩缩容参与计算的指标名称，PolicyType取值RuleBased，
MetricName取值（AvailableGameServerSessions，AvailableCustomCount，PercentAvailableCustomCount，ActiveInstances，IdleInstances，CurrentPlayerSessions和PercentIdleInstances）；
PolicyType取值TargetBased时，MetricName取值PercentAvailableGameSessions
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def PolicyType(self):
        """策略类型，取值：TargetBased表示基于目标的策略；RuleBased表示基于规则的策略
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def TargetConfiguration(self):
        """扩缩容目标值配置，只有TargetBased类型的策略生效
        :rtype: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        return self._TargetConfiguration

    @TargetConfiguration.setter
    def TargetConfiguration(self, TargetConfiguration):
        self._TargetConfiguration = TargetConfiguration


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._Name = params.get("Name")
        self._ScalingAdjustment = params.get("ScalingAdjustment")
        self._ScalingAdjustmentType = params.get("ScalingAdjustmentType")
        self._Threshold = params.get("Threshold")
        self._ComparisonOperator = params.get("ComparisonOperator")
        self._EvaluationPeriods = params.get("EvaluationPeriods")
        self._MetricName = params.get("MetricName")
        self._PolicyType = params.get("PolicyType")
        if params.get("TargetConfiguration") is not None:
            self._TargetConfiguration = TargetConfiguration()
            self._TargetConfiguration._deserialize(params.get("TargetConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutScalingPolicyResponse(AbstractModel):
    """PutScalingPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._RequestId = None

    @property
    def Name(self):
        """规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RequestId = params.get("RequestId")


class PutTimerScalingPolicyRequest(AbstractModel):
    """PutTimerScalingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimerScalingPolicy: 定时器策略消息
        :type TimerScalingPolicy: :class:`tencentcloud.gse.v20191112.models.TimerScalingPolicy`
        """
        self._TimerScalingPolicy = None

    @property
    def TimerScalingPolicy(self):
        """定时器策略消息
        :rtype: :class:`tencentcloud.gse.v20191112.models.TimerScalingPolicy`
        """
        return self._TimerScalingPolicy

    @TimerScalingPolicy.setter
    def TimerScalingPolicy(self, TimerScalingPolicy):
        self._TimerScalingPolicy = TimerScalingPolicy


    def _deserialize(self, params):
        if params.get("TimerScalingPolicy") is not None:
            self._TimerScalingPolicy = TimerScalingPolicy()
            self._TimerScalingPolicy._deserialize(params.get("TimerScalingPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutTimerScalingPolicyResponse(AbstractModel):
    """PutTimerScalingPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class QuotaResource(AbstractModel):
    """配额资源

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型，1生成包、2服务部署、3别名、4游戏服务器队列、5实例
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: int
        :param _HardLimit: 总额度
注意：此字段可能返回 null，表示取不到有效值。
        :type HardLimit: int
        :param _Remaining: 剩余额度
注意：此字段可能返回 null，表示取不到有效值。
        :type Remaining: int
        :param _ExtraInfo: 额外信息，可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInfo: str
        """
        self._ResourceType = None
        self._HardLimit = None
        self._Remaining = None
        self._ExtraInfo = None

    @property
    def ResourceType(self):
        """资源类型，1生成包、2服务部署、3别名、4游戏服务器队列、5实例
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def HardLimit(self):
        """总额度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HardLimit

    @HardLimit.setter
    def HardLimit(self, HardLimit):
        self._HardLimit = HardLimit

    @property
    def Remaining(self):
        """剩余额度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Remaining

    @Remaining.setter
    def Remaining(self, Remaining):
        self._Remaining = Remaining

    @property
    def ExtraInfo(self):
        """额外信息，可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._HardLimit = params.get("HardLimit")
        self._Remaining = params.get("Remaining")
        self._ExtraInfo = params.get("ExtraInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelatedCcnInfo(AbstractModel):
    """云联网相关信息描述

    """

    def __init__(self):
        r"""
        :param _AccountId: 云联网所属账号
        :type AccountId: str
        :param _CcnId: 云联网 ID
        :type CcnId: str
        :param _AttachType: 关联云联网状态
        :type AttachType: str
        """
        self._AccountId = None
        self._CcnId = None
        self._AttachType = None

    @property
    def AccountId(self):
        """云联网所属账号
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def CcnId(self):
        """云联网 ID
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def AttachType(self):
        """关联云联网状态
        :rtype: str
        """
        return self._AttachType

    @AttachType.setter
    def AttachType(self, AttachType):
        self._AttachType = AttachType


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._CcnId = params.get("CcnId")
        self._AttachType = params.get("AttachType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResolveAliasRequest(AbstractModel):
    """ResolveAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AliasId: 要获取fleetId的别名ID
        :type AliasId: str
        """
        self._AliasId = None

    @property
    def AliasId(self):
        """要获取fleetId的别名ID
        :rtype: str
        """
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResolveAliasResponse(AbstractModel):
    """ResolveAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 别名指向的fleet的唯一标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetId = None
        self._RequestId = None

    @property
    def FleetId(self):
        """别名指向的fleet的唯一标识符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._RequestId = params.get("RequestId")


class ResourceCreationLimitPolicy(AbstractModel):
    """资源创建规则

    """

    def __init__(self):
        r"""
        :param _NewGameServerSessionsPerCreator: 创建数量，最小值1，默认2
        :type NewGameServerSessionsPerCreator: int
        :param _PolicyPeriodInMinutes: 单位时间，最小值1，默认3，单位分钟
        :type PolicyPeriodInMinutes: int
        """
        self._NewGameServerSessionsPerCreator = None
        self._PolicyPeriodInMinutes = None

    @property
    def NewGameServerSessionsPerCreator(self):
        """创建数量，最小值1，默认2
        :rtype: int
        """
        return self._NewGameServerSessionsPerCreator

    @NewGameServerSessionsPerCreator.setter
    def NewGameServerSessionsPerCreator(self, NewGameServerSessionsPerCreator):
        self._NewGameServerSessionsPerCreator = NewGameServerSessionsPerCreator

    @property
    def PolicyPeriodInMinutes(self):
        """单位时间，最小值1，默认3，单位分钟
        :rtype: int
        """
        return self._PolicyPeriodInMinutes

    @PolicyPeriodInMinutes.setter
    def PolicyPeriodInMinutes(self, PolicyPeriodInMinutes):
        self._PolicyPeriodInMinutes = PolicyPeriodInMinutes


    def _deserialize(self, params):
        self._NewGameServerSessionsPerCreator = params.get("NewGameServerSessionsPerCreator")
        self._PolicyPeriodInMinutes = params.get("PolicyPeriodInMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoutingStrategy(AbstractModel):
    """路由策略

    """

    def __init__(self):
        r"""
        :param _Type: 别名的路由策略的类型，有效值常规别名(SIMPLE)、终止别名(TERMINAL)
        :type Type: str
        :param _FleetId: 别名指向的队列的唯一标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _Message: 与终端路由策略一起使用的消息文本，长度不小于1字符不超过1024字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._Type = None
        self._FleetId = None
        self._Message = None

    @property
    def Type(self):
        """别名的路由策略的类型，有效值常规别名(SIMPLE)、终止别名(TERMINAL)
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FleetId(self):
        """别名指向的队列的唯一标识符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Message(self):
        """与终端路由策略一起使用的消息文本，长度不小于1字符不超过1024字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._FleetId = params.get("FleetId")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeConfiguration(AbstractModel):
    """运行配置

    """

    def __init__(self):
        r"""
        :param _GameServerSessionActivationTimeoutSeconds: 游戏会话进程超时，最小值1，最大值600，单位秒
        :type GameServerSessionActivationTimeoutSeconds: int
        :param _MaxConcurrentGameServerSessionActivations: 最大游戏会话数，最小值1，最大值2147483647
        :type MaxConcurrentGameServerSessionActivations: int
        :param _ServerProcesses: 服务进程配置，至少有一个进程配置
        :type ServerProcesses: list of ServerProcesse
        """
        self._GameServerSessionActivationTimeoutSeconds = None
        self._MaxConcurrentGameServerSessionActivations = None
        self._ServerProcesses = None

    @property
    def GameServerSessionActivationTimeoutSeconds(self):
        """游戏会话进程超时，最小值1，最大值600，单位秒
        :rtype: int
        """
        return self._GameServerSessionActivationTimeoutSeconds

    @GameServerSessionActivationTimeoutSeconds.setter
    def GameServerSessionActivationTimeoutSeconds(self, GameServerSessionActivationTimeoutSeconds):
        self._GameServerSessionActivationTimeoutSeconds = GameServerSessionActivationTimeoutSeconds

    @property
    def MaxConcurrentGameServerSessionActivations(self):
        """最大游戏会话数，最小值1，最大值2147483647
        :rtype: int
        """
        return self._MaxConcurrentGameServerSessionActivations

    @MaxConcurrentGameServerSessionActivations.setter
    def MaxConcurrentGameServerSessionActivations(self, MaxConcurrentGameServerSessionActivations):
        self._MaxConcurrentGameServerSessionActivations = MaxConcurrentGameServerSessionActivations

    @property
    def ServerProcesses(self):
        """服务进程配置，至少有一个进程配置
        :rtype: list of ServerProcesse
        """
        return self._ServerProcesses

    @ServerProcesses.setter
    def ServerProcesses(self, ServerProcesses):
        self._ServerProcesses = ServerProcesses


    def _deserialize(self, params):
        self._GameServerSessionActivationTimeoutSeconds = params.get("GameServerSessionActivationTimeoutSeconds")
        self._MaxConcurrentGameServerSessionActivations = params.get("MaxConcurrentGameServerSessionActivations")
        if params.get("ServerProcesses") is not None:
            self._ServerProcesses = []
            for item in params.get("ServerProcesses"):
                obj = ServerProcesse()
                obj._deserialize(item)
                self._ServerProcesses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScalingPolicy(AbstractModel):
    """动态扩缩容配置

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务部署ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ScalingAdjustment: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingAdjustment: str
        :param _ScalingAdjustmentType: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingAdjustmentType: str
        :param _ComparisonOperator: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ComparisonOperator: str
        :param _Threshold: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Threshold: str
        :param _EvaluationPeriods: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type EvaluationPeriods: str
        :param _MetricName: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param _PolicyType: 策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param _TargetConfiguration: 基于规则的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        self._FleetId = None
        self._Name = None
        self._Status = None
        self._ScalingAdjustment = None
        self._ScalingAdjustmentType = None
        self._ComparisonOperator = None
        self._Threshold = None
        self._EvaluationPeriods = None
        self._MetricName = None
        self._PolicyType = None
        self._TargetConfiguration = None

    @property
    def FleetId(self):
        """服务部署ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Name(self):
        """名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ScalingAdjustment(self):
        """保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScalingAdjustment

    @ScalingAdjustment.setter
    def ScalingAdjustment(self, ScalingAdjustment):
        self._ScalingAdjustment = ScalingAdjustment

    @property
    def ScalingAdjustmentType(self):
        """保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScalingAdjustmentType

    @ScalingAdjustmentType.setter
    def ScalingAdjustmentType(self, ScalingAdjustmentType):
        self._ScalingAdjustmentType = ScalingAdjustmentType

    @property
    def ComparisonOperator(self):
        """保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ComparisonOperator

    @ComparisonOperator.setter
    def ComparisonOperator(self, ComparisonOperator):
        self._ComparisonOperator = ComparisonOperator

    @property
    def Threshold(self):
        """保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def EvaluationPeriods(self):
        """保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EvaluationPeriods

    @EvaluationPeriods.setter
    def EvaluationPeriods(self, EvaluationPeriods):
        self._EvaluationPeriods = EvaluationPeriods

    @property
    def MetricName(self):
        """保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def PolicyType(self):
        """策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def TargetConfiguration(self):
        """基于规则的配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        return self._TargetConfiguration

    @TargetConfiguration.setter
    def TargetConfiguration(self, TargetConfiguration):
        self._TargetConfiguration = TargetConfiguration


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._ScalingAdjustment = params.get("ScalingAdjustment")
        self._ScalingAdjustmentType = params.get("ScalingAdjustmentType")
        self._ComparisonOperator = params.get("ComparisonOperator")
        self._Threshold = params.get("Threshold")
        self._EvaluationPeriods = params.get("EvaluationPeriods")
        self._MetricName = params.get("MetricName")
        self._PolicyType = params.get("PolicyType")
        if params.get("TargetConfiguration") is not None:
            self._TargetConfiguration = TargetConfiguration()
            self._TargetConfiguration._deserialize(params.get("TargetConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchGameServerSessionsRequest(AbstractModel):
    """SearchGameServerSessions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AliasId: 别名ID
        :type AliasId: str
        :param _FleetId: 舰队ID
        :type FleetId: str
        :param _Limit: 单次查询记录数上限
        :type Limit: int
        :param _NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :type NextToken: str
        :param _FilterExpression: 搜索条件表达式，支持如下变量
gameServerSessionName 游戏会话名称 String
gameServerSessionId 游戏会话ID String
maximumSessions 最大的玩家会话数 Number
creationTimeMillis 创建时间，单位：毫秒 Number
playerSessionCount 当前玩家会话数 Number
hasAvailablePlayerSessions 是否有可用玩家数 String 取值true或false
gameServerSessionProperties 游戏会话属性 String

表达式String类型 等于=，不等于<>判断
表示Number类型支持 =,<>,>,>=,<,<=

例如：
FilterExpression取值
playerSessionCount>=2 AND hasAvailablePlayerSessions=true"
表示查找至少有两个玩家，而且有可用玩家会话的游戏会话。
FilterExpression取值
gameServerSessionProperties.K1 = 'V1' AND gameServerSessionProperties.K2 = 'V2' OR gameServerSessionProperties.K3 = 'V3'

表示
查询满足如下游戏服务器会话属性的游戏会话
{
    "GameProperties":[
        {
            "Key":"K1",
            "Value":"V1"
        },
        {
            "Key":"K2",
            "Value":"V2"
        },
        {
            "Key":"K3",
            "Value":"V3"
        }
    ]
}
        :type FilterExpression: str
        :param _SortExpression: 排序条件关键字
支持排序字段
gameServerSessionName 游戏会话名称 String
gameServerSessionId 游戏会话ID String
maximumSessions 最大的玩家会话数 Number
creationTimeMillis 创建时间，单位：毫秒 Number
playerSessionCount 当前玩家会话数 Number
        :type SortExpression: str
        """
        self._AliasId = None
        self._FleetId = None
        self._Limit = None
        self._NextToken = None
        self._FilterExpression = None
        self._SortExpression = None

    @property
    def AliasId(self):
        """别名ID
        :rtype: str
        """
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId

    @property
    def FleetId(self):
        """舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Limit(self):
        """单次查询记录数上限
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NextToken(self):
        """页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def FilterExpression(self):
        """搜索条件表达式，支持如下变量
gameServerSessionName 游戏会话名称 String
gameServerSessionId 游戏会话ID String
maximumSessions 最大的玩家会话数 Number
creationTimeMillis 创建时间，单位：毫秒 Number
playerSessionCount 当前玩家会话数 Number
hasAvailablePlayerSessions 是否有可用玩家数 String 取值true或false
gameServerSessionProperties 游戏会话属性 String

表达式String类型 等于=，不等于<>判断
表示Number类型支持 =,<>,>,>=,<,<=

例如：
FilterExpression取值
playerSessionCount>=2 AND hasAvailablePlayerSessions=true"
表示查找至少有两个玩家，而且有可用玩家会话的游戏会话。
FilterExpression取值
gameServerSessionProperties.K1 = 'V1' AND gameServerSessionProperties.K2 = 'V2' OR gameServerSessionProperties.K3 = 'V3'

表示
查询满足如下游戏服务器会话属性的游戏会话
{
    "GameProperties":[
        {
            "Key":"K1",
            "Value":"V1"
        },
        {
            "Key":"K2",
            "Value":"V2"
        },
        {
            "Key":"K3",
            "Value":"V3"
        }
    ]
}
        :rtype: str
        """
        return self._FilterExpression

    @FilterExpression.setter
    def FilterExpression(self, FilterExpression):
        self._FilterExpression = FilterExpression

    @property
    def SortExpression(self):
        """排序条件关键字
支持排序字段
gameServerSessionName 游戏会话名称 String
gameServerSessionId 游戏会话ID String
maximumSessions 最大的玩家会话数 Number
creationTimeMillis 创建时间，单位：毫秒 Number
playerSessionCount 当前玩家会话数 Number
        :rtype: str
        """
        return self._SortExpression

    @SortExpression.setter
    def SortExpression(self, SortExpression):
        self._SortExpression = SortExpression


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        self._FleetId = params.get("FleetId")
        self._Limit = params.get("Limit")
        self._NextToken = params.get("NextToken")
        self._FilterExpression = params.get("FilterExpression")
        self._SortExpression = params.get("SortExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchGameServerSessionsResponse(AbstractModel):
    """SearchGameServerSessions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessions: 游戏服务器会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessions: list of GameServerSession
        :param _NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSessions = None
        self._NextToken = None
        self._RequestId = None

    @property
    def GameServerSessions(self):
        """游戏服务器会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of GameServerSession
        """
        return self._GameServerSessions

    @GameServerSessions.setter
    def GameServerSessions(self, GameServerSessions):
        self._GameServerSessions = GameServerSessions

    @property
    def NextToken(self):
        """页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self._GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self._GameServerSessions.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class ServerProcesse(AbstractModel):
    """游戏服务进程

    """

    def __init__(self):
        r"""
        :param _ConcurrentExecutions: 并发执行数量，所有进程并发执行总数最小值1，最大值50
        :type ConcurrentExecutions: int
        :param _LaunchPath: 启动路径：Linux路径/local/game/ 或WIndows路径C:\game\，最小长度1，最大长度1024
        :type LaunchPath: str
        :param _Parameters: 启动参数，最小长度0，最大长度1024
        :type Parameters: str
        """
        self._ConcurrentExecutions = None
        self._LaunchPath = None
        self._Parameters = None

    @property
    def ConcurrentExecutions(self):
        """并发执行数量，所有进程并发执行总数最小值1，最大值50
        :rtype: int
        """
        return self._ConcurrentExecutions

    @ConcurrentExecutions.setter
    def ConcurrentExecutions(self, ConcurrentExecutions):
        self._ConcurrentExecutions = ConcurrentExecutions

    @property
    def LaunchPath(self):
        """启动路径：Linux路径/local/game/ 或WIndows路径C:\game\，最小长度1，最大长度1024
        :rtype: str
        """
        return self._LaunchPath

    @LaunchPath.setter
    def LaunchPath(self, LaunchPath):
        self._LaunchPath = LaunchPath

    @property
    def Parameters(self):
        """启动参数，最小长度0，最大长度1024
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._ConcurrentExecutions = params.get("ConcurrentExecutions")
        self._LaunchPath = params.get("LaunchPath")
        self._Parameters = params.get("Parameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetServerReservedRequest(AbstractModel):
    """SetServerReserved请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 扩缩容配置服务器舰队ID
        :type FleetId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ReserveValue: 实例是否保留, 1-保留，0-不保留,默认
        :type ReserveValue: int
        """
        self._FleetId = None
        self._InstanceId = None
        self._ReserveValue = None

    @property
    def FleetId(self):
        """扩缩容配置服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReserveValue(self):
        """实例是否保留, 1-保留，0-不保留,默认
        :rtype: int
        """
        return self._ReserveValue

    @ReserveValue.setter
    def ReserveValue(self, ReserveValue):
        self._ReserveValue = ReserveValue


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        self._ReserveValue = params.get("ReserveValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetServerReservedResponse(AbstractModel):
    """SetServerReserved返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetServerWeightRequest(AbstractModel):
    """SetServerWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
        :type FleetId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Weight: 权重，最小值0，最大值10，默认值5
        :type Weight: int
        """
        self._FleetId = None
        self._InstanceId = None
        self._Weight = None

    @property
    def FleetId(self):
        """服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        """权重，最小值0，最大值10，默认值5
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetServerWeightResponse(AbstractModel):
    """SetServerWeight返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartFleetActionsRequest(AbstractModel):
    """StartFleetActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        :param _Actions: 服务器舰队扩展策略，值为["AUTO_SCALING"]
        :type Actions: list of str
        """
        self._FleetId = None
        self._Actions = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Actions(self):
        """服务器舰队扩展策略，值为["AUTO_SCALING"]
        :rtype: list of str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._Actions = params.get("Actions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartFleetActionsResponse(AbstractModel):
    """StartFleetActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetId = None
        self._RequestId = None

    @property
    def FleetId(self):
        """服务器舰队 Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._RequestId = params.get("RequestId")


class StartGameServerSessionPlacementRequest(AbstractModel):
    """StartGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlacementId: 开始部署游戏服务器会话的唯一标识符，最大值48个ASCII字符，模式：[a-zA-Z0-9-]+
        :type PlacementId: str
        :param _GameServerSessionQueueName: 游戏服务器会话队列名称
        :type GameServerSessionQueueName: str
        :param _MaximumPlayerSessionCount: 游戏服务器允许同时连接到游戏会话的最大玩家数量，最小值1，最大值为玩家会话最大限额
        :type MaximumPlayerSessionCount: int
        :param _DesiredPlayerSessions: 玩家游戏会话信息
        :type DesiredPlayerSessions: list of DesiredPlayerSession
        :param _GameProperties: 玩家游戏会话属性
        :type GameProperties: list of GameProperty
        :param _GameServerSessionData: 游戏服务器会话数据，最大长度不超过4096个ASCII字符
        :type GameServerSessionData: str
        :param _GameServerSessionName: 游戏服务器会话名称，最大长度不超过4096个ASCII字符
        :type GameServerSessionName: str
        :param _PlayerLatencies: 玩家延迟
        :type PlayerLatencies: list of PlayerLatency
        """
        self._PlacementId = None
        self._GameServerSessionQueueName = None
        self._MaximumPlayerSessionCount = None
        self._DesiredPlayerSessions = None
        self._GameProperties = None
        self._GameServerSessionData = None
        self._GameServerSessionName = None
        self._PlayerLatencies = None

    @property
    def PlacementId(self):
        """开始部署游戏服务器会话的唯一标识符，最大值48个ASCII字符，模式：[a-zA-Z0-9-]+
        :rtype: str
        """
        return self._PlacementId

    @PlacementId.setter
    def PlacementId(self, PlacementId):
        self._PlacementId = PlacementId

    @property
    def GameServerSessionQueueName(self):
        """游戏服务器会话队列名称
        :rtype: str
        """
        return self._GameServerSessionQueueName

    @GameServerSessionQueueName.setter
    def GameServerSessionQueueName(self, GameServerSessionQueueName):
        self._GameServerSessionQueueName = GameServerSessionQueueName

    @property
    def MaximumPlayerSessionCount(self):
        """游戏服务器允许同时连接到游戏会话的最大玩家数量，最小值1，最大值为玩家会话最大限额
        :rtype: int
        """
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount

    @property
    def DesiredPlayerSessions(self):
        """玩家游戏会话信息
        :rtype: list of DesiredPlayerSession
        """
        return self._DesiredPlayerSessions

    @DesiredPlayerSessions.setter
    def DesiredPlayerSessions(self, DesiredPlayerSessions):
        self._DesiredPlayerSessions = DesiredPlayerSessions

    @property
    def GameProperties(self):
        """玩家游戏会话属性
        :rtype: list of GameProperty
        """
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def GameServerSessionData(self):
        """游戏服务器会话数据，最大长度不超过4096个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionData

    @GameServerSessionData.setter
    def GameServerSessionData(self, GameServerSessionData):
        self._GameServerSessionData = GameServerSessionData

    @property
    def GameServerSessionName(self):
        """游戏服务器会话名称，最大长度不超过4096个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionName

    @GameServerSessionName.setter
    def GameServerSessionName(self, GameServerSessionName):
        self._GameServerSessionName = GameServerSessionName

    @property
    def PlayerLatencies(self):
        """玩家延迟
        :rtype: list of PlayerLatency
        """
        return self._PlayerLatencies

    @PlayerLatencies.setter
    def PlayerLatencies(self, PlayerLatencies):
        self._PlayerLatencies = PlayerLatencies


    def _deserialize(self, params):
        self._PlacementId = params.get("PlacementId")
        self._GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        if params.get("DesiredPlayerSessions") is not None:
            self._DesiredPlayerSessions = []
            for item in params.get("DesiredPlayerSessions"):
                obj = DesiredPlayerSession()
                obj._deserialize(item)
                self._DesiredPlayerSessions.append(obj)
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._GameServerSessionData = params.get("GameServerSessionData")
        self._GameServerSessionName = params.get("GameServerSessionName")
        if params.get("PlayerLatencies") is not None:
            self._PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self._PlayerLatencies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartGameServerSessionPlacementResponse(AbstractModel):
    """StartGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionPlacement: 游戏服务器会话放置
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSessionPlacement = None
        self._RequestId = None

    @property
    def GameServerSessionPlacement(self):
        """游戏服务器会话放置
        :rtype: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        """
        return self._GameServerSessionPlacement

    @GameServerSessionPlacement.setter
    def GameServerSessionPlacement(self, GameServerSessionPlacement):
        self._GameServerSessionPlacement = GameServerSessionPlacement

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self._GameServerSessionPlacement = GameServerSessionPlacement()
            self._GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self._RequestId = params.get("RequestId")


class StopFleetActionsRequest(AbstractModel):
    """StopFleetActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        :param _Actions: 服务器舰队扩展策略，值为["AUTO_SCALING"]
        :type Actions: list of str
        """
        self._FleetId = None
        self._Actions = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Actions(self):
        """服务器舰队扩展策略，值为["AUTO_SCALING"]
        :rtype: list of str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._Actions = params.get("Actions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopFleetActionsResponse(AbstractModel):
    """StopFleetActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetId = None
        self._RequestId = None

    @property
    def FleetId(self):
        """服务器舰队 Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._RequestId = params.get("RequestId")


class StopGameServerSessionPlacementRequest(AbstractModel):
    """StopGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlacementId: 游戏服务器会话放置的唯一标识符
        :type PlacementId: str
        """
        self._PlacementId = None

    @property
    def PlacementId(self):
        """游戏服务器会话放置的唯一标识符
        :rtype: str
        """
        return self._PlacementId

    @PlacementId.setter
    def PlacementId(self, PlacementId):
        self._PlacementId = PlacementId


    def _deserialize(self, params):
        self._PlacementId = params.get("PlacementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopGameServerSessionPlacementResponse(AbstractModel):
    """StopGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionPlacement: 游戏服务器会话放置
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSessionPlacement = None
        self._RequestId = None

    @property
    def GameServerSessionPlacement(self):
        """游戏服务器会话放置
        :rtype: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        """
        return self._GameServerSessionPlacement

    @GameServerSessionPlacement.setter
    def GameServerSessionPlacement(self, GameServerSessionPlacement):
        self._GameServerSessionPlacement = GameServerSessionPlacement

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self._GameServerSessionPlacement = GameServerSessionPlacement()
            self._GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签结构体

    """

    def __init__(self):
        r"""
        :param _Key: 标签键，最大长度127字节
        :type Key: str
        :param _Value: 标签值，最大长度255字节
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """标签键，最大长度127字节
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值，最大长度255字节
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
        


class TargetConfiguration(AbstractModel):
    """基于规则的动态扩缩容配置项

    """

    def __init__(self):
        r"""
        :param _TargetValue: 预留存率
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetValue: int
        """
        self._TargetValue = None

    @property
    def TargetValue(self):
        """预留存率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue


    def _deserialize(self, params):
        self._TargetValue = params.get("TargetValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerConfiguration(AbstractModel):
    """重复周期配置

    """

    def __init__(self):
        r"""
        :param _TimerType: 定时器重复周期类型（未定义0，单次1、按天2、按月3、按周4）
注意：此字段可能返回 null，表示取不到有效值。
        :type TimerType: int
        :param _TimerValue: 定时器取值
注意：此字段可能返回 null，表示取不到有效值。
        :type TimerValue: :class:`tencentcloud.gse.v20191112.models.TimerValue`
        :param _BeginTime: 定时器开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param _EndTime: 定时器结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._TimerType = None
        self._TimerValue = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def TimerType(self):
        """定时器重复周期类型（未定义0，单次1、按天2、按月3、按周4）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimerType

    @TimerType.setter
    def TimerType(self, TimerType):
        self._TimerType = TimerType

    @property
    def TimerValue(self):
        """定时器取值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.TimerValue`
        """
        return self._TimerValue

    @TimerValue.setter
    def TimerValue(self, TimerValue):
        self._TimerValue = TimerValue

    @property
    def BeginTime(self):
        """定时器开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """定时器结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._TimerType = params.get("TimerType")
        if params.get("TimerValue") is not None:
            self._TimerValue = TimerValue()
            self._TimerValue._deserialize(params.get("TimerValue"))
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerFleetCapacity(AbstractModel):
    """定时器弹性伸缩策略

    """

    def __init__(self):
        r"""
        :param _FleetId: 扩缩容配置服务器舰队ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _DesiredInstances: 期望实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredInstances: int
        :param _MinSize: 最小实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinSize: int
        :param _MaxSize: 最大实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSize: int
        :param _ScalingInterval: 伸缩容间隔，单位：分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingInterval: int
        :param _ScalingType: 扩缩容类型（手动1，自动2、未定义0）
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingType: int
        :param _TargetConfiguration: 基于目标的扩展策略的设置
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        self._FleetId = None
        self._DesiredInstances = None
        self._MinSize = None
        self._MaxSize = None
        self._ScalingInterval = None
        self._ScalingType = None
        self._TargetConfiguration = None

    @property
    def FleetId(self):
        """扩缩容配置服务器舰队ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def DesiredInstances(self):
        """期望实例数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DesiredInstances

    @DesiredInstances.setter
    def DesiredInstances(self, DesiredInstances):
        self._DesiredInstances = DesiredInstances

    @property
    def MinSize(self):
        """最小实例数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        """最大实例数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def ScalingInterval(self):
        """伸缩容间隔，单位：分钟
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ScalingInterval

    @ScalingInterval.setter
    def ScalingInterval(self, ScalingInterval):
        self._ScalingInterval = ScalingInterval

    @property
    def ScalingType(self):
        """扩缩容类型（手动1，自动2、未定义0）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ScalingType

    @ScalingType.setter
    def ScalingType(self, ScalingType):
        self._ScalingType = ScalingType

    @property
    def TargetConfiguration(self):
        """基于目标的扩展策略的设置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        return self._TargetConfiguration

    @TargetConfiguration.setter
    def TargetConfiguration(self, TargetConfiguration):
        self._TargetConfiguration = TargetConfiguration


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._DesiredInstances = params.get("DesiredInstances")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._ScalingInterval = params.get("ScalingInterval")
        self._ScalingType = params.get("ScalingType")
        if params.get("TargetConfiguration") is not None:
            self._TargetConfiguration = TargetConfiguration()
            self._TargetConfiguration._deserialize(params.get("TargetConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerScalingPolicy(AbstractModel):
    """定时器策略消息

    """

    def __init__(self):
        r"""
        :param _TimerId: 定时器ID，进行encode，填写时更新
注意：此字段可能返回 null，表示取不到有效值。
        :type TimerId: str
        :param _TimerName: 定时器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TimerName: str
        :param _TimerStatus: 定时器状态(未定义0、未生效1、生效中2、已停止3、已过期4)
注意：此字段可能返回 null，表示取不到有效值。
        :type TimerStatus: int
        :param _TimerFleetCapacity: 定时器弹性伸缩策略
注意：此字段可能返回 null，表示取不到有效值。
        :type TimerFleetCapacity: :class:`tencentcloud.gse.v20191112.models.TimerFleetCapacity`
        :param _TimerConfiguration: 重复周期配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TimerConfiguration: :class:`tencentcloud.gse.v20191112.models.TimerConfiguration`
        """
        self._TimerId = None
        self._TimerName = None
        self._TimerStatus = None
        self._TimerFleetCapacity = None
        self._TimerConfiguration = None

    @property
    def TimerId(self):
        """定时器ID，进行encode，填写时更新
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimerId

    @TimerId.setter
    def TimerId(self, TimerId):
        self._TimerId = TimerId

    @property
    def TimerName(self):
        """定时器名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimerName

    @TimerName.setter
    def TimerName(self, TimerName):
        self._TimerName = TimerName

    @property
    def TimerStatus(self):
        """定时器状态(未定义0、未生效1、生效中2、已停止3、已过期4)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimerStatus

    @TimerStatus.setter
    def TimerStatus(self, TimerStatus):
        self._TimerStatus = TimerStatus

    @property
    def TimerFleetCapacity(self):
        """定时器弹性伸缩策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.TimerFleetCapacity`
        """
        return self._TimerFleetCapacity

    @TimerFleetCapacity.setter
    def TimerFleetCapacity(self, TimerFleetCapacity):
        self._TimerFleetCapacity = TimerFleetCapacity

    @property
    def TimerConfiguration(self):
        """重复周期配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.TimerConfiguration`
        """
        return self._TimerConfiguration

    @TimerConfiguration.setter
    def TimerConfiguration(self, TimerConfiguration):
        self._TimerConfiguration = TimerConfiguration


    def _deserialize(self, params):
        self._TimerId = params.get("TimerId")
        self._TimerName = params.get("TimerName")
        self._TimerStatus = params.get("TimerStatus")
        if params.get("TimerFleetCapacity") is not None:
            self._TimerFleetCapacity = TimerFleetCapacity()
            self._TimerFleetCapacity._deserialize(params.get("TimerFleetCapacity"))
        if params.get("TimerConfiguration") is not None:
            self._TimerConfiguration = TimerConfiguration()
            self._TimerConfiguration._deserialize(params.get("TimerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerValue(AbstractModel):
    """定时器取值配置

    """

    def __init__(self):
        r"""
        :param _Day: 每X天，执行一次(重复周期-按天/单次)
注意：此字段可能返回 null，表示取不到有效值。
        :type Day: int
        :param _FromDay: 每月从第x天，执行一次(重复周期-按月)
注意：此字段可能返回 null，表示取不到有效值。
        :type FromDay: int
        :param _ToDay: 每月到第x天，执行一次(重复周期-按月)
注意：此字段可能返回 null，表示取不到有效值。
        :type ToDay: int
        :param _WeekDays: 重复周期-按周，周几（多个值,取值周一(1,2,3,4,5,6,7)周日）
注意：此字段可能返回 null，表示取不到有效值。
        :type WeekDays: list of int
        """
        self._Day = None
        self._FromDay = None
        self._ToDay = None
        self._WeekDays = None

    @property
    def Day(self):
        """每X天，执行一次(重复周期-按天/单次)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Day

    @Day.setter
    def Day(self, Day):
        self._Day = Day

    @property
    def FromDay(self):
        """每月从第x天，执行一次(重复周期-按月)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FromDay

    @FromDay.setter
    def FromDay(self, FromDay):
        self._FromDay = FromDay

    @property
    def ToDay(self):
        """每月到第x天，执行一次(重复周期-按月)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ToDay

    @ToDay.setter
    def ToDay(self, ToDay):
        self._ToDay = ToDay

    @property
    def WeekDays(self):
        """重复周期-按周，周几（多个值,取值周一(1,2,3,4,5,6,7)周日）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays


    def _deserialize(self, params):
        self._Day = params.get("Day")
        self._FromDay = params.get("FromDay")
        self._ToDay = params.get("ToDay")
        self._WeekDays = params.get("WeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AliasId: 要更新的别名的唯一标识符
        :type AliasId: str
        :param _Name: 名字，长度不小于1字符不超过1024字符
        :type Name: str
        :param _Description: 别名的可读说明，长度不小于1字符不超过1024字符
        :type Description: str
        :param _RoutingStrategy: 别名的路由配置
        :type RoutingStrategy: :class:`tencentcloud.gse.v20191112.models.RoutingStrategy`
        """
        self._AliasId = None
        self._Name = None
        self._Description = None
        self._RoutingStrategy = None

    @property
    def AliasId(self):
        """要更新的别名的唯一标识符
        :rtype: str
        """
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId

    @property
    def Name(self):
        """名字，长度不小于1字符不超过1024字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """别名的可读说明，长度不小于1字符不超过1024字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RoutingStrategy(self):
        """别名的路由配置
        :rtype: :class:`tencentcloud.gse.v20191112.models.RoutingStrategy`
        """
        return self._RoutingStrategy

    @RoutingStrategy.setter
    def RoutingStrategy(self, RoutingStrategy):
        self._RoutingStrategy = RoutingStrategy


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("RoutingStrategy") is not None:
            self._RoutingStrategy = RoutingStrategy()
            self._RoutingStrategy._deserialize(params.get("RoutingStrategy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Alias: 别名对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: :class:`tencentcloud.gse.v20191112.models.Alias`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Alias = None
        self._RequestId = None

    @property
    def Alias(self):
        """别名对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.Alias`
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Alias") is not None:
            self._Alias = Alias()
            self._Alias._deserialize(params.get("Alias"))
        self._RequestId = params.get("RequestId")


class UpdateAssetRequest(AbstractModel):
    """UpdateAsset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetId: 生成包ID
        :type AssetId: str
        :param _AssetName: 生成包名字，最小长度为1，最大长度为64
        :type AssetName: str
        :param _AssetVersion: 生成包版本，最小长度为1，最大长度为64
        :type AssetVersion: str
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetVersion = None

    @property
    def AssetId(self):
        """生成包ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        """生成包名字，最小长度为1，最大长度为64
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetVersion(self):
        """生成包版本，最小长度为1，最大长度为64
        :rtype: str
        """
        return self._AssetVersion

    @AssetVersion.setter
    def AssetVersion(self, AssetVersion):
        self._AssetVersion = AssetVersion


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetVersion = params.get("AssetVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAssetResponse(AbstractModel):
    """UpdateAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateBucketAccelerateOptRequest(AbstractModel):
    """UpdateBucketAccelerateOpt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Allowed: true为开启全球加速，false为关闭
        :type Allowed: bool
        """
        self._Allowed = None

    @property
    def Allowed(self):
        """true为开启全球加速，false为关闭
        :rtype: bool
        """
        return self._Allowed

    @Allowed.setter
    def Allowed(self, Allowed):
        self._Allowed = Allowed


    def _deserialize(self, params):
        self._Allowed = params.get("Allowed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBucketAccelerateOptResponse(AbstractModel):
    """UpdateBucketAccelerateOpt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateBucketCORSOptRequest(AbstractModel):
    """UpdateBucketCORSOpt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AllowedOrigins: 允许的访问来源;具体参见 [cos文档](https://cloud.tencent.com/document/product/436/8279)
        :type AllowedOrigins: list of str
        :param _AllowedMethods: 允许的 HTTP 操作方法;可以配置多个:PUT、GET、POST、HEAD。[cos文档](https://cloud.tencent.com/document/product/436/8279)
        :type AllowedMethods: list of str
        :param _AllowedHeaders: 用于指定允许浏览器发送 CORS 请求时携带的自定义 HTTP 请求头部;可以配置*，代表允许所有头部，为了避免遗漏，推荐配置为*。[cos文档](https://cloud.tencent.com/document/product/436/8279)
        :type AllowedHeaders: list of str
        :param _MaxAgeSeconds: 跨域资源共享配置的有效时间，单位为秒。[cos文档](https://cloud.tencent.com/document/product/436/8279)
        :type MaxAgeSeconds: int
        :param _ExposeHeaders: 允许浏览器获取的 CORS 请求响应中的头部，不区分大小写；默认情况下浏览器只能访问简单响应头部：Cache-Control、Content-Type、Expires、Last-Modified，如果需要访问其他响应头部，需要添加 ExposeHeader 配置。[cos文档](https://cloud.tencent.com/document/product/436/8279)
        :type ExposeHeaders: list of str
        """
        self._AllowedOrigins = None
        self._AllowedMethods = None
        self._AllowedHeaders = None
        self._MaxAgeSeconds = None
        self._ExposeHeaders = None

    @property
    def AllowedOrigins(self):
        """允许的访问来源;具体参见 [cos文档](https://cloud.tencent.com/document/product/436/8279)
        :rtype: list of str
        """
        return self._AllowedOrigins

    @AllowedOrigins.setter
    def AllowedOrigins(self, AllowedOrigins):
        self._AllowedOrigins = AllowedOrigins

    @property
    def AllowedMethods(self):
        """允许的 HTTP 操作方法;可以配置多个:PUT、GET、POST、HEAD。[cos文档](https://cloud.tencent.com/document/product/436/8279)
        :rtype: list of str
        """
        return self._AllowedMethods

    @AllowedMethods.setter
    def AllowedMethods(self, AllowedMethods):
        self._AllowedMethods = AllowedMethods

    @property
    def AllowedHeaders(self):
        """用于指定允许浏览器发送 CORS 请求时携带的自定义 HTTP 请求头部;可以配置*，代表允许所有头部，为了避免遗漏，推荐配置为*。[cos文档](https://cloud.tencent.com/document/product/436/8279)
        :rtype: list of str
        """
        return self._AllowedHeaders

    @AllowedHeaders.setter
    def AllowedHeaders(self, AllowedHeaders):
        self._AllowedHeaders = AllowedHeaders

    @property
    def MaxAgeSeconds(self):
        """跨域资源共享配置的有效时间，单位为秒。[cos文档](https://cloud.tencent.com/document/product/436/8279)
        :rtype: int
        """
        return self._MaxAgeSeconds

    @MaxAgeSeconds.setter
    def MaxAgeSeconds(self, MaxAgeSeconds):
        self._MaxAgeSeconds = MaxAgeSeconds

    @property
    def ExposeHeaders(self):
        """允许浏览器获取的 CORS 请求响应中的头部，不区分大小写；默认情况下浏览器只能访问简单响应头部：Cache-Control、Content-Type、Expires、Last-Modified，如果需要访问其他响应头部，需要添加 ExposeHeader 配置。[cos文档](https://cloud.tencent.com/document/product/436/8279)
        :rtype: list of str
        """
        return self._ExposeHeaders

    @ExposeHeaders.setter
    def ExposeHeaders(self, ExposeHeaders):
        self._ExposeHeaders = ExposeHeaders


    def _deserialize(self, params):
        self._AllowedOrigins = params.get("AllowedOrigins")
        self._AllowedMethods = params.get("AllowedMethods")
        self._AllowedHeaders = params.get("AllowedHeaders")
        self._MaxAgeSeconds = params.get("MaxAgeSeconds")
        self._ExposeHeaders = params.get("ExposeHeaders")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBucketCORSOptResponse(AbstractModel):
    """UpdateBucketCORSOpt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateFleetAttributesRequest(AbstractModel):
    """UpdateFleetAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        :param _Description: 服务器舰队描述，最小长度0，最大长度100
        :type Description: str
        :param _Name: 服务器舰队名称，最小长度1，最大长度50
        :type Name: str
        :param _NewGameSessionProtectionPolicy: 保护策略：不保护NoProtection、完全保护FullProtection、时限保护TimeLimitProtection
        :type NewGameSessionProtectionPolicy: str
        :param _ResourceCreationLimitPolicy: 资源创建限制策略
        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`
        :param _GameServerSessionProtectionTimeLimit: 时限保护超时时间，默认60分钟，最小值5，最大值1440；当NewGameSessionProtectionPolicy为TimeLimitProtection时参数有效
        :type GameServerSessionProtectionTimeLimit: int
        """
        self._FleetId = None
        self._Description = None
        self._Name = None
        self._NewGameSessionProtectionPolicy = None
        self._ResourceCreationLimitPolicy = None
        self._GameServerSessionProtectionTimeLimit = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Description(self):
        """服务器舰队描述，最小长度0，最大长度100
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        """服务器舰队名称，最小长度1，最大长度50
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NewGameSessionProtectionPolicy(self):
        """保护策略：不保护NoProtection、完全保护FullProtection、时限保护TimeLimitProtection
        :rtype: str
        """
        return self._NewGameSessionProtectionPolicy

    @NewGameSessionProtectionPolicy.setter
    def NewGameSessionProtectionPolicy(self, NewGameSessionProtectionPolicy):
        self._NewGameSessionProtectionPolicy = NewGameSessionProtectionPolicy

    @property
    def ResourceCreationLimitPolicy(self):
        """资源创建限制策略
        :rtype: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`
        """
        return self._ResourceCreationLimitPolicy

    @ResourceCreationLimitPolicy.setter
    def ResourceCreationLimitPolicy(self, ResourceCreationLimitPolicy):
        self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy

    @property
    def GameServerSessionProtectionTimeLimit(self):
        """时限保护超时时间，默认60分钟，最小值5，最大值1440；当NewGameSessionProtectionPolicy为TimeLimitProtection时参数有效
        :rtype: int
        """
        return self._GameServerSessionProtectionTimeLimit

    @GameServerSessionProtectionTimeLimit.setter
    def GameServerSessionProtectionTimeLimit(self, GameServerSessionProtectionTimeLimit):
        self._GameServerSessionProtectionTimeLimit = GameServerSessionProtectionTimeLimit


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._NewGameSessionProtectionPolicy = params.get("NewGameSessionProtectionPolicy")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self._ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        self._GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFleetAttributesResponse(AbstractModel):
    """UpdateFleetAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetId = None
        self._RequestId = None

    @property
    def FleetId(self):
        """服务器舰队Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._RequestId = params.get("RequestId")


class UpdateFleetCapacityRequest(AbstractModel):
    """UpdateFleetCapacity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
        :type FleetId: str
        :param _DesiredInstances: 期望的服务器实例数
        :type DesiredInstances: int
        :param _MinSize: 服务器实例数最小限制，最小值0，最大值不超过最高配额查看各地区最高配额减1
        :type MinSize: int
        :param _MaxSize: 服务器实例数最大限制，最小值1，最大值不超过最高配额查看各地区最高配额
        :type MaxSize: int
        :param _ScalingInterval: 服务器伸缩容间隔，单位分钟，最小值3，最大值30，默认值10
        :type ScalingInterval: int
        """
        self._FleetId = None
        self._DesiredInstances = None
        self._MinSize = None
        self._MaxSize = None
        self._ScalingInterval = None

    @property
    def FleetId(self):
        """服务器舰队ID
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def DesiredInstances(self):
        """期望的服务器实例数
        :rtype: int
        """
        return self._DesiredInstances

    @DesiredInstances.setter
    def DesiredInstances(self, DesiredInstances):
        self._DesiredInstances = DesiredInstances

    @property
    def MinSize(self):
        """服务器实例数最小限制，最小值0，最大值不超过最高配额查看各地区最高配额减1
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        """服务器实例数最大限制，最小值1，最大值不超过最高配额查看各地区最高配额
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def ScalingInterval(self):
        """服务器伸缩容间隔，单位分钟，最小值3，最大值30，默认值10
        :rtype: int
        """
        return self._ScalingInterval

    @ScalingInterval.setter
    def ScalingInterval(self, ScalingInterval):
        self._ScalingInterval = ScalingInterval


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._DesiredInstances = params.get("DesiredInstances")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._ScalingInterval = params.get("ScalingInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFleetCapacityResponse(AbstractModel):
    """UpdateFleetCapacity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetId = None
        self._RequestId = None

    @property
    def FleetId(self):
        """服务器舰队ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._RequestId = params.get("RequestId")


class UpdateFleetNameRequest(AbstractModel):
    """UpdateFleetName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        :param _Name: 服务器舰队名称，最小长度1，最大长度50
        :type Name: str
        """
        self._FleetId = None
        self._Name = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Name(self):
        """服务器舰队名称，最小长度1，最大长度50
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFleetNameResponse(AbstractModel):
    """UpdateFleetName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateFleetPortSettingsRequest(AbstractModel):
    """UpdateFleetPortSettings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队 Id
        :type FleetId: str
        :param _InboundPermissionAuthorizations: 新增安全组
        :type InboundPermissionAuthorizations: list of InboundPermissionAuthorization
        :param _InboundPermissionRevocations: 移除安全组
        :type InboundPermissionRevocations: list of InboundPermissionRevocations
        """
        self._FleetId = None
        self._InboundPermissionAuthorizations = None
        self._InboundPermissionRevocations = None

    @property
    def FleetId(self):
        """服务器舰队 Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InboundPermissionAuthorizations(self):
        """新增安全组
        :rtype: list of InboundPermissionAuthorization
        """
        return self._InboundPermissionAuthorizations

    @InboundPermissionAuthorizations.setter
    def InboundPermissionAuthorizations(self, InboundPermissionAuthorizations):
        self._InboundPermissionAuthorizations = InboundPermissionAuthorizations

    @property
    def InboundPermissionRevocations(self):
        """移除安全组
        :rtype: list of InboundPermissionRevocations
        """
        return self._InboundPermissionRevocations

    @InboundPermissionRevocations.setter
    def InboundPermissionRevocations(self, InboundPermissionRevocations):
        self._InboundPermissionRevocations = InboundPermissionRevocations


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        if params.get("InboundPermissionAuthorizations") is not None:
            self._InboundPermissionAuthorizations = []
            for item in params.get("InboundPermissionAuthorizations"):
                obj = InboundPermissionAuthorization()
                obj._deserialize(item)
                self._InboundPermissionAuthorizations.append(obj)
        if params.get("InboundPermissionRevocations") is not None:
            self._InboundPermissionRevocations = []
            for item in params.get("InboundPermissionRevocations"):
                obj = InboundPermissionRevocations()
                obj._deserialize(item)
                self._InboundPermissionRevocations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFleetPortSettingsResponse(AbstractModel):
    """UpdateFleetPortSettings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务部署 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FleetId = None
        self._RequestId = None

    @property
    def FleetId(self):
        """服务部署 Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._RequestId = params.get("RequestId")


class UpdateGameServerSessionQueueRequest(AbstractModel):
    """UpdateGameServerSessionQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 游戏服务器会话队列名字，长度1~128
        :type Name: str
        :param _Destinations: 目的服务器舰队（可为别名）列表
        :type Destinations: list of GameServerSessionQueueDestination
        :param _PlayerLatencyPolicies: 延迟策略集合
        :type PlayerLatencyPolicies: list of PlayerLatencyPolicy
        :param _TimeoutInSeconds: 超时时间
        :type TimeoutInSeconds: int
        """
        self._Name = None
        self._Destinations = None
        self._PlayerLatencyPolicies = None
        self._TimeoutInSeconds = None

    @property
    def Name(self):
        """游戏服务器会话队列名字，长度1~128
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Destinations(self):
        """目的服务器舰队（可为别名）列表
        :rtype: list of GameServerSessionQueueDestination
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def PlayerLatencyPolicies(self):
        """延迟策略集合
        :rtype: list of PlayerLatencyPolicy
        """
        return self._PlayerLatencyPolicies

    @PlayerLatencyPolicies.setter
    def PlayerLatencyPolicies(self, PlayerLatencyPolicies):
        self._PlayerLatencyPolicies = PlayerLatencyPolicies

    @property
    def TimeoutInSeconds(self):
        """超时时间
        :rtype: int
        """
        return self._TimeoutInSeconds

    @TimeoutInSeconds.setter
    def TimeoutInSeconds(self, TimeoutInSeconds):
        self._TimeoutInSeconds = TimeoutInSeconds


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = GameServerSessionQueueDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        if params.get("PlayerLatencyPolicies") is not None:
            self._PlayerLatencyPolicies = []
            for item in params.get("PlayerLatencyPolicies"):
                obj = PlayerLatencyPolicy()
                obj._deserialize(item)
                self._PlayerLatencyPolicies.append(obj)
        self._TimeoutInSeconds = params.get("TimeoutInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGameServerSessionQueueResponse(AbstractModel):
    """UpdateGameServerSessionQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionQueue: 部署服务组对象
        :type GameServerSessionQueue: :class:`tencentcloud.gse.v20191112.models.GameServerSessionQueue`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSessionQueue = None
        self._RequestId = None

    @property
    def GameServerSessionQueue(self):
        """部署服务组对象
        :rtype: :class:`tencentcloud.gse.v20191112.models.GameServerSessionQueue`
        """
        return self._GameServerSessionQueue

    @GameServerSessionQueue.setter
    def GameServerSessionQueue(self, GameServerSessionQueue):
        self._GameServerSessionQueue = GameServerSessionQueue

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionQueue") is not None:
            self._GameServerSessionQueue = GameServerSessionQueue()
            self._GameServerSessionQueue._deserialize(params.get("GameServerSessionQueue"))
        self._RequestId = params.get("RequestId")


class UpdateGameServerSessionRequest(AbstractModel):
    """UpdateGameServerSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: 游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符
        :type GameServerSessionId: str
        :param _MaximumPlayerSessionCount: 最大玩家数量，最小值不小于0
        :type MaximumPlayerSessionCount: int
        :param _Name: 游戏服务器会话名称，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :type Name: str
        :param _PlayerSessionCreationPolicy: 玩家会话创建策略，包括允许所有玩家加入和禁止所有玩家加入（ACCEPT_ALL,DENY_ALL）
        :type PlayerSessionCreationPolicy: str
        :param _ProtectionPolicy: 保护策略，包括不保护、时限保护和完全保护(NoProtection,TimeLimitProtection,FullProtection)
        :type ProtectionPolicy: str
        """
        self._GameServerSessionId = None
        self._MaximumPlayerSessionCount = None
        self._Name = None
        self._PlayerSessionCreationPolicy = None
        self._ProtectionPolicy = None

    @property
    def GameServerSessionId(self):
        """游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def MaximumPlayerSessionCount(self):
        """最大玩家数量，最小值不小于0
        :rtype: int
        """
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount

    @property
    def Name(self):
        """游戏服务器会话名称，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PlayerSessionCreationPolicy(self):
        """玩家会话创建策略，包括允许所有玩家加入和禁止所有玩家加入（ACCEPT_ALL,DENY_ALL）
        :rtype: str
        """
        return self._PlayerSessionCreationPolicy

    @PlayerSessionCreationPolicy.setter
    def PlayerSessionCreationPolicy(self, PlayerSessionCreationPolicy):
        self._PlayerSessionCreationPolicy = PlayerSessionCreationPolicy

    @property
    def ProtectionPolicy(self):
        """保护策略，包括不保护、时限保护和完全保护(NoProtection,TimeLimitProtection,FullProtection)
        :rtype: str
        """
        return self._ProtectionPolicy

    @ProtectionPolicy.setter
    def ProtectionPolicy(self, ProtectionPolicy):
        self._ProtectionPolicy = ProtectionPolicy


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self._Name = params.get("Name")
        self._PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self._ProtectionPolicy = params.get("ProtectionPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGameServerSessionResponse(AbstractModel):
    """UpdateGameServerSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GameServerSession: 更新后的游戏会话
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GameServerSession = None
        self._RequestId = None

    @property
    def GameServerSession(self):
        """更新后的游戏会话
        :rtype: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        """
        return self._GameServerSession

    @GameServerSession.setter
    def GameServerSession(self, GameServerSession):
        self._GameServerSession = GameServerSession

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self._GameServerSession = GameServerSession()
            self._GameServerSession._deserialize(params.get("GameServerSession"))
        self._RequestId = params.get("RequestId")


class UpdateRuntimeConfigurationRequest(AbstractModel):
    """UpdateRuntimeConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FleetId: 服务器舰队Id
        :type FleetId: str
        :param _RuntimeConfiguration: 服务器舰队配置
        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        """
        self._FleetId = None
        self._RuntimeConfiguration = None

    @property
    def FleetId(self):
        """服务器舰队Id
        :rtype: str
        """
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def RuntimeConfiguration(self):
        """服务器舰队配置
        :rtype: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        """
        return self._RuntimeConfiguration

    @RuntimeConfiguration.setter
    def RuntimeConfiguration(self, RuntimeConfiguration):
        self._RuntimeConfiguration = RuntimeConfiguration


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        if params.get("RuntimeConfiguration") is not None:
            self._RuntimeConfiguration = RuntimeConfiguration()
            self._RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRuntimeConfigurationResponse(AbstractModel):
    """UpdateRuntimeConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuntimeConfiguration: 服务器舰队配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuntimeConfiguration = None
        self._RequestId = None

    @property
    def RuntimeConfiguration(self):
        """服务器舰队配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        """
        return self._RuntimeConfiguration

    @RuntimeConfiguration.setter
    def RuntimeConfiguration(self, RuntimeConfiguration):
        self._RuntimeConfiguration = RuntimeConfiguration

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuntimeConfiguration") is not None:
            self._RuntimeConfiguration = RuntimeConfiguration()
            self._RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        self._RequestId = params.get("RequestId")