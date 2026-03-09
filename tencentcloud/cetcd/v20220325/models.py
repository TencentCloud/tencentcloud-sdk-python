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


class ChargePrepaidConfig(AbstractModel):
    r"""预付费类型相关配置

    """

    def __init__(self):
        r"""
        :param _Period: 预付费购买周期，单位：月
        :type Period: int
        :param _RenewFlag: 预付费自动续费设置：
NOTIFY_AND_MANUAL_RENEW：表示默认状态(用户未设置，即初始状态)， NOTIFY_AND_AUTO_RENEW：表示自动续费，DISABLE_NOTIFY_AND_MANUAL_RENEW：表示明确不自动续费(用户设置)
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        r"""预付费购买周期，单位：月
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        r"""预付费自动续费设置：
NOTIFY_AND_MANUAL_RENEW：表示默认状态(用户未设置，即初始状态)， NOTIFY_AND_AUTO_RENEW：表示自动续费，DISABLE_NOTIFY_AND_MANUAL_RENEW：表示明确不自动续费(用户设置)
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEtcdInstanceRequest(AbstractModel):
    r"""CreateEtcdInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: etcd实例名称
        :type Name: str
        :param _VpcId: etcd所属vpc
        :type VpcId: str
        :param _ServiceSubnetId: etcd对外提供访问ip地址所在子网
        :type ServiceSubnetId: str
        :param _SubnetIds: etcd部署子网
        :type SubnetIds: list of str
        :param _EtcdVersion: etcd版本
        :type EtcdVersion: str
        :param _Size: etcd节点个数，可选范围: 1, 3, 5, 7, 9
        :type Size: int
        :param _Description: etcd集群描述信息
        :type Description: str
        :param _AdvancedSettings: 高级设置
        :type AdvancedSettings: :class:`tencentcloud.cetcd.v20220325.models.EtcdAdvancedSettings`
        :param _ChargeType: 付费类型：
PREPAID 预付费
POSTPAID_BY_HOUR 后付费按小时付费
        :type ChargeType: str
        :param _ChargePrepaid: 预付费相关配置
        :type ChargePrepaid: :class:`tencentcloud.cetcd.v20220325.models.ChargePrepaidConfig`
        :param _DiskSize: 存储大小GB
        :type DiskSize: int
        :param _DeletionProtection: 删除保护，true 删除保护开启；false删除保护关闭
        :type DeletionProtection: bool
        """
        self._Name = None
        self._VpcId = None
        self._ServiceSubnetId = None
        self._SubnetIds = None
        self._EtcdVersion = None
        self._Size = None
        self._Description = None
        self._AdvancedSettings = None
        self._ChargeType = None
        self._ChargePrepaid = None
        self._DiskSize = None
        self._DeletionProtection = None

    @property
    def Name(self):
        r"""etcd实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def VpcId(self):
        r"""etcd所属vpc
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ServiceSubnetId(self):
        r"""etcd对外提供访问ip地址所在子网
        :rtype: str
        """
        return self._ServiceSubnetId

    @ServiceSubnetId.setter
    def ServiceSubnetId(self, ServiceSubnetId):
        self._ServiceSubnetId = ServiceSubnetId

    @property
    def SubnetIds(self):
        r"""etcd部署子网
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def EtcdVersion(self):
        r"""etcd版本
        :rtype: str
        """
        return self._EtcdVersion

    @EtcdVersion.setter
    def EtcdVersion(self, EtcdVersion):
        self._EtcdVersion = EtcdVersion

    @property
    def Size(self):
        r"""etcd节点个数，可选范围: 1, 3, 5, 7, 9
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Description(self):
        r"""etcd集群描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AdvancedSettings(self):
        r"""高级设置
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EtcdAdvancedSettings`
        """
        return self._AdvancedSettings

    @AdvancedSettings.setter
    def AdvancedSettings(self, AdvancedSettings):
        self._AdvancedSettings = AdvancedSettings

    @property
    def ChargeType(self):
        r"""付费类型：
PREPAID 预付费
POSTPAID_BY_HOUR 后付费按小时付费
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargePrepaid(self):
        r"""预付费相关配置
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.ChargePrepaidConfig`
        """
        return self._ChargePrepaid

    @ChargePrepaid.setter
    def ChargePrepaid(self, ChargePrepaid):
        self._ChargePrepaid = ChargePrepaid

    @property
    def DiskSize(self):
        r"""存储大小GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DeletionProtection(self):
        r"""删除保护，true 删除保护开启；false删除保护关闭
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._VpcId = params.get("VpcId")
        self._ServiceSubnetId = params.get("ServiceSubnetId")
        self._SubnetIds = params.get("SubnetIds")
        self._EtcdVersion = params.get("EtcdVersion")
        self._Size = params.get("Size")
        self._Description = params.get("Description")
        if params.get("AdvancedSettings") is not None:
            self._AdvancedSettings = EtcdAdvancedSettings()
            self._AdvancedSettings._deserialize(params.get("AdvancedSettings"))
        self._ChargeType = params.get("ChargeType")
        if params.get("ChargePrepaid") is not None:
            self._ChargePrepaid = ChargePrepaidConfig()
            self._ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        self._DiskSize = params.get("DiskSize")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEtcdInstanceResponse(AbstractModel):
    r"""CreateEtcdInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 创建etcd实例的Id
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""创建etcd实例的Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateEtcdSnapshotPolicyRequest(AbstractModel):
    r"""CreateEtcdSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: etcd实例Id
        :type InstanceId: str
        :param _SnapshotPolicyName: 快照策略名
        :type SnapshotPolicyName: str
        :param _BackupSettings: 备份参数设置
        :type BackupSettings: :class:`tencentcloud.cetcd.v20220325.models.EtcdBackupSettings`
        """
        self._InstanceId = None
        self._SnapshotPolicyName = None
        self._BackupSettings = None

    @property
    def InstanceId(self):
        r"""etcd实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SnapshotPolicyName(self):
        r"""快照策略名
        :rtype: str
        """
        return self._SnapshotPolicyName

    @SnapshotPolicyName.setter
    def SnapshotPolicyName(self, SnapshotPolicyName):
        self._SnapshotPolicyName = SnapshotPolicyName

    @property
    def BackupSettings(self):
        r"""备份参数设置
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EtcdBackupSettings`
        """
        return self._BackupSettings

    @BackupSettings.setter
    def BackupSettings(self, BackupSettings):
        self._BackupSettings = BackupSettings


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SnapshotPolicyName = params.get("SnapshotPolicyName")
        if params.get("BackupSettings") is not None:
            self._BackupSettings = EtcdBackupSettings()
            self._BackupSettings._deserialize(params.get("BackupSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEtcdSnapshotPolicyResponse(AbstractModel):
    r"""CreateEtcdSnapshotPolicy返回参数结构体

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


class CreateEtcdSnapshotRequest(AbstractModel):
    r"""CreateEtcdSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: etcd实例id
        :type InstanceId: str
        :param _SnapshotName: etcd快照名称
        :type SnapshotName: str
        :param _User: 备份用户名
        :type User: str
        :param _Password: 备份密码
        :type Password: str
        """
        self._InstanceId = None
        self._SnapshotName = None
        self._User = None
        self._Password = None

    @property
    def InstanceId(self):
        r"""etcd实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SnapshotName(self):
        r"""etcd快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def User(self):
        r"""备份用户名
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        r"""备份密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SnapshotName = params.get("SnapshotName")
        self._User = params.get("User")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEtcdSnapshotResponse(AbstractModel):
    r"""CreateEtcdSnapshot返回参数结构体

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


class DescribeEtcdAvailableVersionsRequest(AbstractModel):
    r"""DescribeEtcdAvailableVersions请求参数结构体

    """


class DescribeEtcdAvailableVersionsResponse(AbstractModel):
    r"""DescribeEtcdAvailableVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Versions: 支持的版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Versions: list of VersionInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Versions = None
        self._RequestId = None

    @property
    def Versions(self):
        r"""支持的版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VersionInstance
        """
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

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
        if params.get("Versions") is not None:
            self._Versions = []
            for item in params.get("Versions"):
                obj = VersionInstance()
                obj._deserialize(item)
                self._Versions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEtcdCreatingProgressRequest(AbstractModel):
    r"""DescribeEtcdCreatingProgress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
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
        


class DescribeEtcdCreatingProgressResponse(AbstractModel):
    r"""DescribeEtcdCreatingProgress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Steps: 创建进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Steps: list of TaskStepInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Steps = None
        self._RequestId = None

    @property
    def Steps(self):
        r"""创建进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskStepInfo
        """
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

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
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = TaskStepInfo()
                obj._deserialize(item)
                self._Steps.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEtcdCredentialsRequest(AbstractModel):
    r"""DescribeEtcdCredentials请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: etcd实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""etcd实例id
        :rtype: str
        """
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
        


class DescribeEtcdCredentialsResponse(AbstractModel):
    r"""DescribeEtcdCredentials返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Credentials: 访问凭证
注意：此字段可能返回 null，表示取不到有效值。
        :type Credentials: list of EtcdCredential
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Credentials = None
        self._RequestId = None

    @property
    def Credentials(self):
        r"""访问凭证
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EtcdCredential
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

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
        if params.get("Credentials") is not None:
            self._Credentials = []
            for item in params.get("Credentials"):
                obj = EtcdCredential()
                obj._deserialize(item)
                self._Credentials.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEtcdInstancesRequest(AbstractModel):
    r"""DescribeEtcdInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 按照一个或者多个实例ID查询。实例ID形如：etcd-xxxxxxxx。参数不支持同时指定InstanceIds和Filters
        :type InstanceIds: list of str
        :param _Filters: 支持按照vpc-id和instance-id过滤。参数不支持同时指定InstanceIds和Filters
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，最大值为50
        :type Limit: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        r"""按照一个或者多个实例ID查询。实例ID形如：etcd-xxxxxxxx。参数不支持同时指定InstanceIds和Filters
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        r"""支持按照vpc-id和instance-id过滤。参数不支持同时指定InstanceIds和Filters
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，最大值为50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEtcdInstancesResponse(AbstractModel):
    r"""DescribeEtcdInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Etcds: etcd实例详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Etcds: list of Etcd
        :param _TotalCount: 符合条件的实例数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Etcds = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Etcds(self):
        r"""etcd实例详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Etcd
        """
        return self._Etcds

    @Etcds.setter
    def Etcds(self, Etcds):
        self._Etcds = Etcds

    @property
    def TotalCount(self):
        r"""符合条件的实例数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Etcds") is not None:
            self._Etcds = []
            for item in params.get("Etcds"):
                obj = Etcd()
                obj._deserialize(item)
                self._Etcds.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEtcdQuotaRequest(AbstractModel):
    r"""DescribeEtcdQuota请求参数结构体

    """


class DescribeEtcdQuotaResponse(AbstractModel):
    r"""DescribeEtcdQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QuotaLimit: 当前配额限制
        :type QuotaLimit: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QuotaLimit = None
        self._RequestId = None

    @property
    def QuotaLimit(self):
        r"""当前配额限制
        :rtype: int
        """
        return self._QuotaLimit

    @QuotaLimit.setter
    def QuotaLimit(self, QuotaLimit):
        self._QuotaLimit = QuotaLimit

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
        self._QuotaLimit = params.get("QuotaLimit")
        self._RequestId = params.get("RequestId")


class DescribeEtcdRegionsRequest(AbstractModel):
    r"""DescribeEtcdRegions请求参数结构体

    """


class DescribeEtcdRegionsResponse(AbstractModel):
    r"""DescribeEtcdRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Regions: 支持的地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Regions: list of RegionInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Regions = None
        self._RequestId = None

    @property
    def Regions(self):
        r"""支持的地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RegionInstance
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

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
        if params.get("Regions") is not None:
            self._Regions = []
            for item in params.get("Regions"):
                obj = RegionInstance()
                obj._deserialize(item)
                self._Regions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEtcdSnapshotPoliciesRequest(AbstractModel):
    r"""DescribeEtcdSnapshotPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: etcd实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""etcd实例Id
        :rtype: str
        """
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
        


class DescribeEtcdSnapshotPoliciesResponse(AbstractModel):
    r"""DescribeEtcdSnapshotPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotPolicies: 备份策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotPolicies: list of EtcdSnapshotPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotPolicies = None
        self._RequestId = None

    @property
    def SnapshotPolicies(self):
        r"""备份策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EtcdSnapshotPolicy
        """
        return self._SnapshotPolicies

    @SnapshotPolicies.setter
    def SnapshotPolicies(self, SnapshotPolicies):
        self._SnapshotPolicies = SnapshotPolicies

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
        if params.get("SnapshotPolicies") is not None:
            self._SnapshotPolicies = []
            for item in params.get("SnapshotPolicies"):
                obj = EtcdSnapshotPolicy()
                obj._deserialize(item)
                self._SnapshotPolicies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEtcdSnapshotsRequest(AbstractModel):
    r"""DescribeEtcdSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: etcd实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""etcd实例Id
        :rtype: str
        """
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
        


class DescribeEtcdSnapshotsResponse(AbstractModel):
    r"""DescribeEtcdSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Snapshots: etcd快照列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Snapshots: list of EtcdSnapshot
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Snapshots = None
        self._RequestId = None

    @property
    def Snapshots(self):
        r"""etcd快照列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EtcdSnapshot
        """
        return self._Snapshots

    @Snapshots.setter
    def Snapshots(self, Snapshots):
        self._Snapshots = Snapshots

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
        if params.get("Snapshots") is not None:
            self._Snapshots = []
            for item in params.get("Snapshots"):
                obj = EtcdSnapshot()
                obj._deserialize(item)
                self._Snapshots.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEtcdTasksRequest(AbstractModel):
    r"""DescribeEtcdTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务ID
        :type TaskID: str
        :param _Filters: taskType：
    按照任务类型过滤，当前支持enable_internet，disable_internet, restore_remote_snapshot
resourceId：
    按照资源ID过滤
lifeState：
    按照任务状态过滤，当前支持process， done
        :type Filters: list of Filter
        """
        self._TaskID = None
        self._Filters = None

    @property
    def TaskID(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def Filters(self):
        r"""taskType：
    按照任务类型过滤，当前支持enable_internet，disable_internet, restore_remote_snapshot
resourceId：
    按照资源ID过滤
lifeState：
    按照任务状态过滤，当前支持process， done
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
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
        


class DescribeEtcdTasksResponse(AbstractModel):
    r"""DescribeEtcdTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of EtcdTaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        r"""任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EtcdTaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = EtcdTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRPCMethodListRequest(AbstractModel):
    r"""DescribeRPCMethodList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: etcd实例ID
        :type InstanceId: str
        :param _PodName: etcd集群pod名称
        :type PodName: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 最大长度
        :type Limit: int
        """
        self._InstanceId = None
        self._PodName = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""etcd实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PodName(self):
        r"""etcd集群pod名称
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""最大长度
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PodName = params.get("PodName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRPCMethodListResponse(AbstractModel):
    r"""DescribeRPCMethodList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MethodList: gRPC方法列表
        :type MethodList: list of RPCMethod
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MethodList = None
        self._RequestId = None

    @property
    def MethodList(self):
        r"""gRPC方法列表
        :rtype: list of RPCMethod
        """
        return self._MethodList

    @MethodList.setter
    def MethodList(self, MethodList):
        self._MethodList = MethodList

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
        if params.get("MethodList") is not None:
            self._MethodList = []
            for item in params.get("MethodList"):
                obj = RPCMethod()
                obj._deserialize(item)
                self._MethodList.append(obj)
        self._RequestId = params.get("RequestId")


class DisableEtcdInstanceDeletionProtectionRequest(AbstractModel):
    r"""DisableEtcdInstanceDeletionProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: etcd实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""etcd实例ID
        :rtype: str
        """
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
        


class DisableEtcdInstanceDeletionProtectionResponse(AbstractModel):
    r"""DisableEtcdInstanceDeletionProtection返回参数结构体

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


class EnableEtcdInstanceDeletionProtectionRequest(AbstractModel):
    r"""EnableEtcdInstanceDeletionProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: etcd实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""etcd实例ID
        :rtype: str
        """
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
        


class EnableEtcdInstanceDeletionProtectionResponse(AbstractModel):
    r"""EnableEtcdInstanceDeletionProtection返回参数结构体

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


class Etcd(AbstractModel):
    r"""etcd信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Name: 实例名
        :type Name: str
        :param _Description: 实例描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _VpcId: 实例所属vpcId
        :type VpcId: str
        :param _Version: etcd版本
        :type Version: str
        :param _Status: 实例状态
        :type Status: str
        :param _Members: etcd成员信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Members: list of EtcdMember
        :param _Endpoint: 对外访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Endpoint: str
        :param _DeletionProtection: 删除保护，true 删除保护开启；false删除保护关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletionProtection: bool
        """
        self._InstanceId = None
        self._Name = None
        self._Description = None
        self._VpcId = None
        self._Version = None
        self._Status = None
        self._Members = None
        self._Endpoint = None
        self._DeletionProtection = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""实例名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""实例描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VpcId(self):
        r"""实例所属vpcId
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Version(self):
        r"""etcd版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Status(self):
        r"""实例状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Members(self):
        r"""etcd成员信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EtcdMember
        """
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members

    @property
    def Endpoint(self):
        r"""对外访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def DeletionProtection(self):
        r"""删除保护，true 删除保护开启；false删除保护关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._VpcId = params.get("VpcId")
        self._Version = params.get("Version")
        self._Status = params.get("Status")
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = EtcdMember()
                obj._deserialize(item)
                self._Members.append(obj)
        self._Endpoint = params.get("Endpoint")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtcdAdvancedSettings(AbstractModel):
    r"""etcd高级设置

    """

    def __init__(self):
        r"""
        :param _SecuritySettings: 安全相关设置
        :type SecuritySettings: :class:`tencentcloud.cetcd.v20220325.models.EtcdSecuritySettings`
        :param _AutoCompactionSettings: 自动压缩设置
        :type AutoCompactionSettings: :class:`tencentcloud.cetcd.v20220325.models.EtcdAutoCompactionSettings`
        :param _MonitorSettings: 监控设置
        :type MonitorSettings: :class:`tencentcloud.cetcd.v20220325.models.EtcdMonitorSettings`
        :param _BackupSettings: 备份相关设置
        :type BackupSettings: :class:`tencentcloud.cetcd.v20220325.models.EtcdBackupSettings`
        :param _CustomDomains: 自定义域名
        :type CustomDomains: str
        :param _CustomIPs: 自定义ip
        :type CustomIPs: str
        """
        self._SecuritySettings = None
        self._AutoCompactionSettings = None
        self._MonitorSettings = None
        self._BackupSettings = None
        self._CustomDomains = None
        self._CustomIPs = None

    @property
    def SecuritySettings(self):
        r"""安全相关设置
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EtcdSecuritySettings`
        """
        return self._SecuritySettings

    @SecuritySettings.setter
    def SecuritySettings(self, SecuritySettings):
        self._SecuritySettings = SecuritySettings

    @property
    def AutoCompactionSettings(self):
        r"""自动压缩设置
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EtcdAutoCompactionSettings`
        """
        return self._AutoCompactionSettings

    @AutoCompactionSettings.setter
    def AutoCompactionSettings(self, AutoCompactionSettings):
        self._AutoCompactionSettings = AutoCompactionSettings

    @property
    def MonitorSettings(self):
        r"""监控设置
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EtcdMonitorSettings`
        """
        return self._MonitorSettings

    @MonitorSettings.setter
    def MonitorSettings(self, MonitorSettings):
        self._MonitorSettings = MonitorSettings

    @property
    def BackupSettings(self):
        r"""备份相关设置
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EtcdBackupSettings`
        """
        return self._BackupSettings

    @BackupSettings.setter
    def BackupSettings(self, BackupSettings):
        self._BackupSettings = BackupSettings

    @property
    def CustomDomains(self):
        r"""自定义域名
        :rtype: str
        """
        return self._CustomDomains

    @CustomDomains.setter
    def CustomDomains(self, CustomDomains):
        self._CustomDomains = CustomDomains

    @property
    def CustomIPs(self):
        r"""自定义ip
        :rtype: str
        """
        return self._CustomIPs

    @CustomIPs.setter
    def CustomIPs(self, CustomIPs):
        self._CustomIPs = CustomIPs


    def _deserialize(self, params):
        if params.get("SecuritySettings") is not None:
            self._SecuritySettings = EtcdSecuritySettings()
            self._SecuritySettings._deserialize(params.get("SecuritySettings"))
        if params.get("AutoCompactionSettings") is not None:
            self._AutoCompactionSettings = EtcdAutoCompactionSettings()
            self._AutoCompactionSettings._deserialize(params.get("AutoCompactionSettings"))
        if params.get("MonitorSettings") is not None:
            self._MonitorSettings = EtcdMonitorSettings()
            self._MonitorSettings._deserialize(params.get("MonitorSettings"))
        if params.get("BackupSettings") is not None:
            self._BackupSettings = EtcdBackupSettings()
            self._BackupSettings._deserialize(params.get("BackupSettings"))
        self._CustomDomains = params.get("CustomDomains")
        self._CustomIPs = params.get("CustomIPs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtcdAutoCompactionSettings(AbstractModel):
    r"""etcd自动压缩设置

    """

    def __init__(self):
        r"""
        :param _AutoCompactionMode: 自动压缩模式
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoCompactionMode: str
        :param _AutoCompactionRetention: 自动压缩保留时间/revison数
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoCompactionRetention: str
        """
        self._AutoCompactionMode = None
        self._AutoCompactionRetention = None

    @property
    def AutoCompactionMode(self):
        r"""自动压缩模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AutoCompactionMode

    @AutoCompactionMode.setter
    def AutoCompactionMode(self, AutoCompactionMode):
        self._AutoCompactionMode = AutoCompactionMode

    @property
    def AutoCompactionRetention(self):
        r"""自动压缩保留时间/revison数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AutoCompactionRetention

    @AutoCompactionRetention.setter
    def AutoCompactionRetention(self, AutoCompactionRetention):
        self._AutoCompactionRetention = AutoCompactionRetention


    def _deserialize(self, params):
        self._AutoCompactionMode = params.get("AutoCompactionMode")
        self._AutoCompactionRetention = params.get("AutoCompactionRetention")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtcdBackupSettings(AbstractModel):
    r"""etcd备份设置

    """

    def __init__(self):
        r"""
        :param _BackupInterval: 备份间隔(s)
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupInterval: int
        :param _MaxBackupCount: 最大备份个数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxBackupCount: int
        :param _User: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _Password: 密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _CosBucketName: COS桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CosBucketName: str
        """
        self._BackupInterval = None
        self._MaxBackupCount = None
        self._User = None
        self._Password = None
        self._CosBucketName = None

    @property
    def BackupInterval(self):
        r"""备份间隔(s)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BackupInterval

    @BackupInterval.setter
    def BackupInterval(self, BackupInterval):
        self._BackupInterval = BackupInterval

    @property
    def MaxBackupCount(self):
        r"""最大备份个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxBackupCount

    @MaxBackupCount.setter
    def MaxBackupCount(self, MaxBackupCount):
        self._MaxBackupCount = MaxBackupCount

    @property
    def User(self):
        r"""用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        r"""密码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def CosBucketName(self):
        r"""COS桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName


    def _deserialize(self, params):
        self._BackupInterval = params.get("BackupInterval")
        self._MaxBackupCount = params.get("MaxBackupCount")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._CosBucketName = params.get("CosBucketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtcdCredential(AbstractModel):
    r"""etcd访问凭证

    """

    def __init__(self):
        r"""
        :param _CACert: CA证书
注意：此字段可能返回 null，表示取不到有效值。
        :type CACert: str
        :param _Cert: 证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Cert: str
        :param _Key: 私钥
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        """
        self._CACert = None
        self._Cert = None
        self._Key = None

    @property
    def CACert(self):
        r"""CA证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CACert

    @CACert.setter
    def CACert(self, CACert):
        self._CACert = CACert

    @property
    def Cert(self):
        r"""证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def Key(self):
        r"""私钥
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._CACert = params.get("CACert")
        self._Cert = params.get("Cert")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtcdMember(AbstractModel):
    r"""etcd集群成员信息

    """

    def __init__(self):
        r"""
        :param _Name: 节点名字
        :type Name: str
        :param _Version: 节点当前版本
        :type Version: str
        :param _Zone: 所属可用区
        :type Zone: str
        :param _Status: 节点状态
        :type Status: str
        """
        self._Name = None
        self._Version = None
        self._Zone = None
        self._Status = None

    @property
    def Name(self):
        r"""节点名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        r"""节点当前版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Zone(self):
        r"""所属可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        r"""节点状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtcdMonitorSettings(AbstractModel):
    r"""etcd监控设置

    """

    def __init__(self):
        r"""
        :param _PrometheusCreationParam: Prometheus创建参数
        :type PrometheusCreationParam: :class:`tencentcloud.cetcd.v20220325.models.PrometheusCreationParam`
        :param _ExistedPrometheusInstanceId: Prometheus Id
        :type ExistedPrometheusInstanceId: str
        """
        self._PrometheusCreationParam = None
        self._ExistedPrometheusInstanceId = None

    @property
    def PrometheusCreationParam(self):
        r"""Prometheus创建参数
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.PrometheusCreationParam`
        """
        return self._PrometheusCreationParam

    @PrometheusCreationParam.setter
    def PrometheusCreationParam(self, PrometheusCreationParam):
        self._PrometheusCreationParam = PrometheusCreationParam

    @property
    def ExistedPrometheusInstanceId(self):
        r"""Prometheus Id
        :rtype: str
        """
        return self._ExistedPrometheusInstanceId

    @ExistedPrometheusInstanceId.setter
    def ExistedPrometheusInstanceId(self, ExistedPrometheusInstanceId):
        self._ExistedPrometheusInstanceId = ExistedPrometheusInstanceId


    def _deserialize(self, params):
        if params.get("PrometheusCreationParam") is not None:
            self._PrometheusCreationParam = PrometheusCreationParam()
            self._PrometheusCreationParam._deserialize(params.get("PrometheusCreationParam"))
        self._ExistedPrometheusInstanceId = params.get("ExistedPrometheusInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtcdSecuritySettings(AbstractModel):
    r"""etcd安全相关设置

    """

    def __init__(self):
        r"""
        :param _Https: 是否启用https
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: bool
        :param _ClientCertAuth: 启用客户端证书认证
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertAuth: bool
        """
        self._Https = None
        self._ClientCertAuth = None

    @property
    def Https(self):
        r"""是否启用https
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def ClientCertAuth(self):
        r"""启用客户端证书认证
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ClientCertAuth

    @ClientCertAuth.setter
    def ClientCertAuth(self, ClientCertAuth):
        self._ClientCertAuth = ClientCertAuth


    def _deserialize(self, params):
        self._Https = params.get("Https")
        self._ClientCertAuth = params.get("ClientCertAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtcdSnapshot(AbstractModel):
    r"""etcd快照

    """

    def __init__(self):
        r"""
        :param _Name: 快照名称
        :type Name: str
        :param _Size: 快照大小
        :type Size: int
        """
        self._Name = None
        self._Size = None

    @property
    def Name(self):
        r"""快照名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        r"""快照大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtcdSnapshotPolicy(AbstractModel):
    r"""etcd快照策略

    """

    def __init__(self):
        r"""
        :param _Name: 快照策略名称
        :type Name: str
        :param _BackupSettings: 备份参数
        :type BackupSettings: :class:`tencentcloud.cetcd.v20220325.models.EtcdBackupSettings`
        """
        self._Name = None
        self._BackupSettings = None

    @property
    def Name(self):
        r"""快照策略名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BackupSettings(self):
        r"""备份参数
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EtcdBackupSettings`
        """
        return self._BackupSettings

    @BackupSettings.setter
    def BackupSettings(self, BackupSettings):
        self._BackupSettings = BackupSettings


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("BackupSettings") is not None:
            self._BackupSettings = EtcdBackupSettings()
            self._BackupSettings._deserialize(params.get("BackupSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtcdTaskInfo(AbstractModel):
    r"""etcd task信息

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务ID
        :type TaskID: str
        :param _TaskType: 任务类型
        :type TaskType: str
        :param _ResourceID: 资源ID
        :type ResourceID: str
        :param _LifeState: 任务状态
        :type LifeState: str
        :param _CreatedAt: 任务创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 任务更新时间
        :type UpdatedAt: str
        """
        self._TaskID = None
        self._TaskType = None
        self._ResourceID = None
        self._LifeState = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def TaskID(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def TaskType(self):
        r"""任务类型
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ResourceID(self):
        r"""资源ID
        :rtype: str
        """
        return self._ResourceID

    @ResourceID.setter
    def ResourceID(self, ResourceID):
        self._ResourceID = ResourceID

    @property
    def LifeState(self):
        r"""任务状态
        :rtype: str
        """
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def CreatedAt(self):
        r"""任务创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""任务更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._TaskType = params.get("TaskType")
        self._ResourceID = params.get("ResourceID")
        self._LifeState = params.get("LifeState")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Name: str
        :param _Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfig(AbstractModel):
    r"""实例配置信息

    """

    def __init__(self):
        r"""
        :param _Cpu: 核数
        :type Cpu: int
        :param _Mem: 内存大小Gi
        :type Mem: int
        :param _Size: 集群规模
        :type Size: int
        """
        self._Cpu = None
        self._Mem = None
        self._Size = None

    @property
    def Cpu(self):
        r"""核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        r"""内存大小Gi
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Size(self):
        r"""集群规模
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEtcdAttributeRequest(AbstractModel):
    r"""ModifyEtcdAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Name: 实例名
        :type Name: str
        :param _Description: 实例描述
        :type Description: str
        :param _Password: root账号密码
        :type Password: str
        :param _EnableAuth: 同步auth状态
        :type EnableAuth: bool
        :param _EnableDeleteCos: 删除集群关联的cos数据
        :type EnableDeleteCos: bool
        :param _SubnetIds: 子网id，数组
        :type SubnetIds: list of str
        """
        self._InstanceId = None
        self._Name = None
        self._Description = None
        self._Password = None
        self._EnableAuth = None
        self._EnableDeleteCos = None
        self._SubnetIds = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""实例名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""实例描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Password(self):
        r"""root账号密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EnableAuth(self):
        r"""同步auth状态
        :rtype: bool
        """
        return self._EnableAuth

    @EnableAuth.setter
    def EnableAuth(self, EnableAuth):
        self._EnableAuth = EnableAuth

    @property
    def EnableDeleteCos(self):
        r"""删除集群关联的cos数据
        :rtype: bool
        """
        return self._EnableDeleteCos

    @EnableDeleteCos.setter
    def EnableDeleteCos(self, EnableDeleteCos):
        self._EnableDeleteCos = EnableDeleteCos

    @property
    def SubnetIds(self):
        r"""子网id，数组
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Password = params.get("Password")
        self._EnableAuth = params.get("EnableAuth")
        self._EnableDeleteCos = params.get("EnableDeleteCos")
        self._SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEtcdAttributeResponse(AbstractModel):
    r"""ModifyEtcdAttribute返回参数结构体

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


class ModifyEtcdConfigurationRequest(AbstractModel):
    r"""ModifyEtcdConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _AutoCompactionSettings: 自动压缩设置
        :type AutoCompactionSettings: :class:`tencentcloud.cetcd.v20220325.models.EtcdAutoCompactionSettings`
        :param _MonitorSettings: 监控设置
        :type MonitorSettings: :class:`tencentcloud.cetcd.v20220325.models.EtcdMonitorSettings`
        :param _ChargeType: 计费类型
PREPAID：预付费
POSTPAID_BY_HOUR：后付费
        :type ChargeType: str
        :param _InstanceConfig: 实例配置信息
        :type InstanceConfig: :class:`tencentcloud.cetcd.v20220325.models.InstanceConfig`
        :param _PrepaidConfig: 预付费配置信息
        :type PrepaidConfig: :class:`tencentcloud.cetcd.v20220325.models.ChargePrepaidConfig`
        """
        self._InstanceId = None
        self._AutoCompactionSettings = None
        self._MonitorSettings = None
        self._ChargeType = None
        self._InstanceConfig = None
        self._PrepaidConfig = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AutoCompactionSettings(self):
        r"""自动压缩设置
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EtcdAutoCompactionSettings`
        """
        return self._AutoCompactionSettings

    @AutoCompactionSettings.setter
    def AutoCompactionSettings(self, AutoCompactionSettings):
        self._AutoCompactionSettings = AutoCompactionSettings

    @property
    def MonitorSettings(self):
        r"""监控设置
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EtcdMonitorSettings`
        """
        return self._MonitorSettings

    @MonitorSettings.setter
    def MonitorSettings(self, MonitorSettings):
        self._MonitorSettings = MonitorSettings

    @property
    def ChargeType(self):
        r"""计费类型
PREPAID：预付费
POSTPAID_BY_HOUR：后付费
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def InstanceConfig(self):
        r"""实例配置信息
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.InstanceConfig`
        """
        return self._InstanceConfig

    @InstanceConfig.setter
    def InstanceConfig(self, InstanceConfig):
        self._InstanceConfig = InstanceConfig

    @property
    def PrepaidConfig(self):
        r"""预付费配置信息
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.ChargePrepaidConfig`
        """
        return self._PrepaidConfig

    @PrepaidConfig.setter
    def PrepaidConfig(self, PrepaidConfig):
        self._PrepaidConfig = PrepaidConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("AutoCompactionSettings") is not None:
            self._AutoCompactionSettings = EtcdAutoCompactionSettings()
            self._AutoCompactionSettings._deserialize(params.get("AutoCompactionSettings"))
        if params.get("MonitorSettings") is not None:
            self._MonitorSettings = EtcdMonitorSettings()
            self._MonitorSettings._deserialize(params.get("MonitorSettings"))
        self._ChargeType = params.get("ChargeType")
        if params.get("InstanceConfig") is not None:
            self._InstanceConfig = InstanceConfig()
            self._InstanceConfig._deserialize(params.get("InstanceConfig"))
        if params.get("PrepaidConfig") is not None:
            self._PrepaidConfig = ChargePrepaidConfig()
            self._PrepaidConfig._deserialize(params.get("PrepaidConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEtcdConfigurationResponse(AbstractModel):
    r"""ModifyEtcdConfiguration返回参数结构体

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


class ModifyEtcdSnapshotPolicyRequest(AbstractModel):
    r"""ModifyEtcdSnapshotPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: etcd实例id
        :type InstanceId: str
        :param _SnapshotPolicyName: 快照策略名称
        :type SnapshotPolicyName: str
        :param _BackupSettings: 备份参数设置
        :type BackupSettings: :class:`tencentcloud.cetcd.v20220325.models.EtcdBackupSettings`
        """
        self._InstanceId = None
        self._SnapshotPolicyName = None
        self._BackupSettings = None

    @property
    def InstanceId(self):
        r"""etcd实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SnapshotPolicyName(self):
        r"""快照策略名称
        :rtype: str
        """
        return self._SnapshotPolicyName

    @SnapshotPolicyName.setter
    def SnapshotPolicyName(self, SnapshotPolicyName):
        self._SnapshotPolicyName = SnapshotPolicyName

    @property
    def BackupSettings(self):
        r"""备份参数设置
        :rtype: :class:`tencentcloud.cetcd.v20220325.models.EtcdBackupSettings`
        """
        return self._BackupSettings

    @BackupSettings.setter
    def BackupSettings(self, BackupSettings):
        self._BackupSettings = BackupSettings


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SnapshotPolicyName = params.get("SnapshotPolicyName")
        if params.get("BackupSettings") is not None:
            self._BackupSettings = EtcdBackupSettings()
            self._BackupSettings._deserialize(params.get("BackupSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEtcdSnapshotPolicyResponse(AbstractModel):
    r"""ModifyEtcdSnapshotPolicy返回参数结构体

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


class PrometheusCreationParam(AbstractModel):
    r"""Prometheus创建参数

    """

    def __init__(self):
        r"""
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _DataRetention: 保存时长，只支持天单位
12d = 12天
        :type DataRetention: int
        :param _GrafanaUserName: grafana用户名
        :type GrafanaUserName: str
        :param _GrafanaPassword: grafana密码
        :type GrafanaPassword: str
        """
        self._SubnetId = None
        self._DataRetention = None
        self._GrafanaUserName = None
        self._GrafanaPassword = None

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
    def DataRetention(self):
        r"""保存时长，只支持天单位
12d = 12天
        :rtype: int
        """
        return self._DataRetention

    @DataRetention.setter
    def DataRetention(self, DataRetention):
        self._DataRetention = DataRetention

    @property
    def GrafanaUserName(self):
        r"""grafana用户名
        :rtype: str
        """
        return self._GrafanaUserName

    @GrafanaUserName.setter
    def GrafanaUserName(self, GrafanaUserName):
        self._GrafanaUserName = GrafanaUserName

    @property
    def GrafanaPassword(self):
        r"""grafana密码
        :rtype: str
        """
        return self._GrafanaPassword

    @GrafanaPassword.setter
    def GrafanaPassword(self, GrafanaPassword):
        self._GrafanaPassword = GrafanaPassword


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._DataRetention = params.get("DataRetention")
        self._GrafanaUserName = params.get("GrafanaUserName")
        self._GrafanaPassword = params.get("GrafanaPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RPCMethod(AbstractModel):
    r"""RPC方法信息

    """

    def __init__(self):
        r"""
        :param _Name: 方法名称
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        r"""方法名称
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
        


class RegionInstance(AbstractModel):
    r"""地域属性信息

    """

    def __init__(self):
        r"""
        :param _RegionName: 地域名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param _RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _Status: 地域状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _FeatureGates: 地域特性开关(按照JSON的形式返回所有属性)
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureGates: str
        :param _Alias: 地域简称
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _Remark: 地域白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._RegionName = None
        self._RegionId = None
        self._Status = None
        self._FeatureGates = None
        self._Alias = None
        self._Remark = None

    @property
    def RegionName(self):
        r"""地域名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        r"""地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Status(self):
        r"""地域状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FeatureGates(self):
        r"""地域特性开关(按照JSON的形式返回所有属性)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FeatureGates

    @FeatureGates.setter
    def FeatureGates(self, FeatureGates):
        self._FeatureGates = FeatureGates

    @property
    def Alias(self):
        r"""地域简称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Remark(self):
        r"""地域白名单
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        self._Status = params.get("Status")
        self._FeatureGates = params.get("FeatureGates")
        self._Alias = params.get("Alias")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeEtcdInstanceRequest(AbstractModel):
    r"""ResizeEtcdInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Size: etcd节点个数
        :type Size: int
        """
        self._InstanceId = None
        self._Size = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Size(self):
        r"""etcd节点个数
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeEtcdInstanceResponse(AbstractModel):
    r"""ResizeEtcdInstance返回参数结构体

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


class TaskStepInfo(AbstractModel):
    r"""任务步骤信息

    """

    def __init__(self):
        r"""
        :param _Step: 步骤名称
        :type Step: str
        :param _LifeState: 生命周期
pending : 步骤未开始
running: 步骤执行中
success: 步骤成功完成
failed: 步骤失败
        :type LifeState: str
        :param _StartAt: 步骤开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartAt: str
        :param _EndAt: 步骤结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndAt: str
        :param _FailedMsg: 若步骤生命周期为failed,则此字段显示错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedMsg: str
        """
        self._Step = None
        self._LifeState = None
        self._StartAt = None
        self._EndAt = None
        self._FailedMsg = None

    @property
    def Step(self):
        r"""步骤名称
        :rtype: str
        """
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step

    @property
    def LifeState(self):
        r"""生命周期
pending : 步骤未开始
running: 步骤执行中
success: 步骤成功完成
failed: 步骤失败
        :rtype: str
        """
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def StartAt(self):
        r"""步骤开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def EndAt(self):
        r"""步骤结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndAt

    @EndAt.setter
    def EndAt(self, EndAt):
        self._EndAt = EndAt

    @property
    def FailedMsg(self):
        r"""若步骤生命周期为failed,则此字段显示错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FailedMsg

    @FailedMsg.setter
    def FailedMsg(self, FailedMsg):
        self._FailedMsg = FailedMsg


    def _deserialize(self, params):
        self._Step = params.get("Step")
        self._LifeState = params.get("LifeState")
        self._StartAt = params.get("StartAt")
        self._EndAt = params.get("EndAt")
        self._FailedMsg = params.get("FailedMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeEtcdInstanceRequest(AbstractModel):
    r"""UpgradeEtcdInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _EtcdVersion: etcd版本
        :type EtcdVersion: str
        """
        self._InstanceId = None
        self._EtcdVersion = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EtcdVersion(self):
        r"""etcd版本
        :rtype: str
        """
        return self._EtcdVersion

    @EtcdVersion.setter
    def EtcdVersion(self, EtcdVersion):
        self._EtcdVersion = EtcdVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EtcdVersion = params.get("EtcdVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeEtcdInstanceResponse(AbstractModel):
    r"""UpgradeEtcdInstance返回参数结构体

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


class VersionInstance(AbstractModel):
    r"""版本信息

    """

    def __init__(self):
        r"""
        :param _Name: 版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Version: 版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Remark: Remark信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._Name = None
        self._Version = None
        self._Remark = None

    @property
    def Name(self):
        r"""版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        r"""版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Remark(self):
        r"""Remark信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        