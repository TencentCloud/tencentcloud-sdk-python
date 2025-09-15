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


class AssignProjectRequest(AbstractModel):
    r"""AssignProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例 ID 列表。格式如：cmgo-p8vn****，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        :param _ProjectId: 项目ID。项目 ID 具有唯一性，请[登录 MongoDB 控制台](https://console.cloud.tencent.com/mongodb)，在右上角的账户信息的下拉菜单中，选择**项目管理**，即可获取项目ID。
        :type ProjectId: int
        """
        self._InstanceIds = None
        self._ProjectId = None

    @property
    def InstanceIds(self):
        r"""实例 ID 列表。格式如：cmgo-p8vn****，与云数据库控制台页面中显示的实例 ID 相同。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProjectId(self):
        r"""项目ID。项目 ID 具有唯一性，请[登录 MongoDB 控制台](https://console.cloud.tencent.com/mongodb)，在右上角的账户信息的下拉菜单中，选择**项目管理**，即可获取项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignProjectResponse(AbstractModel):
    r"""AssignProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowIds: 返回的异步任务ID列表。
        :type FlowIds: list of int non-negative
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowIds = None
        self._RequestId = None

    @property
    def FlowIds(self):
        r"""返回的异步任务ID列表。
        :rtype: list of int non-negative
        """
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

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
        self._FlowIds = params.get("FlowIds")
        self._RequestId = params.get("RequestId")


class ClientConnection(AbstractModel):
    r"""客户端连接信息，包括客户端IP和连接数

    """

    def __init__(self):
        r"""
        :param _IP: 连接的客户端IP
        :type IP: str
        :param _Count: 对应客户端IP的连接数
        :type Count: int
        """
        self._IP = None
        self._Count = None

    @property
    def IP(self):
        r"""连接的客户端IP
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Count(self):
        r"""对应客户端IP的连接数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceHourRequest(AbstractModel):
    r"""CreateDBInstanceHour请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Memory: 实例内存大小，单位：GB
        :type Memory: int
        :param _Volume: 实例硬盘大小，单位：GB
        :type Volume: int
        :param _ReplicateSetNum: 副本集个数，1为单副本集实例，大于1为分片集群实例，最大不超过10
        :type ReplicateSetNum: int
        :param _SecondaryNum: 每个副本集内从节点个数，目前只支持从节点数为2
        :type SecondaryNum: int
        :param _EngineVersion: MongoDB引擎版本，值包括MONGO_3_WT 、MONGO_3_ROCKS和MONGO_36_WT
        :type EngineVersion: str
        :param _Machine: 实例类型，HIO10G：高IO万兆。
        :type Machine: str
        :param _GoodsNum: 实例数量，默认值为1, 最小值1，最大值为10
        :type GoodsNum: int
        :param _Zone: 可用区信息，格式如：ap-guangzhou-2
        :type Zone: str
        :param _InstanceRole: 实例角色，默认传MASTER即可
        :type InstanceRole: str
        :param _InstanceType: 实例类型，REPLSET-副本集，SHARD-分片集群
        :type InstanceType: str
        :param _Encrypt: 数据是否加密，当且仅当引擎版本为MONGO_3_ROCKS，可以选择加密
        :type Encrypt: int
        :param _VpcId: 私有网络ID，如果不传则默认选择基础网络
        :type VpcId: str
        :param _SubnetId: 私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填
        :type SubnetId: str
        :param _ProjectId: 项目ID，不填为默认项目
        :type ProjectId: int
        :param _SecurityGroup: 安全组参数
        :type SecurityGroup: list of str
        :param _UniqVpcId: 私有网络ID，如果不传则默认选择基础网络
        :type UniqVpcId: str
        :param _UniqSubnetId: 私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填
        :type UniqSubnetId: str
        """
        self._Memory = None
        self._Volume = None
        self._ReplicateSetNum = None
        self._SecondaryNum = None
        self._EngineVersion = None
        self._Machine = None
        self._GoodsNum = None
        self._Zone = None
        self._InstanceRole = None
        self._InstanceType = None
        self._Encrypt = None
        self._VpcId = None
        self._SubnetId = None
        self._ProjectId = None
        self._SecurityGroup = None
        self._UniqVpcId = None
        self._UniqSubnetId = None

    @property
    def Memory(self):
        r"""实例内存大小，单位：GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""实例硬盘大小，单位：GB
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def ReplicateSetNum(self):
        r"""副本集个数，1为单副本集实例，大于1为分片集群实例，最大不超过10
        :rtype: int
        """
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum

    @property
    def SecondaryNum(self):
        r"""每个副本集内从节点个数，目前只支持从节点数为2
        :rtype: int
        """
        return self._SecondaryNum

    @SecondaryNum.setter
    def SecondaryNum(self, SecondaryNum):
        self._SecondaryNum = SecondaryNum

    @property
    def EngineVersion(self):
        r"""MongoDB引擎版本，值包括MONGO_3_WT 、MONGO_3_ROCKS和MONGO_36_WT
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Machine(self):
        r"""实例类型，HIO10G：高IO万兆。
        :rtype: str
        """
        return self._Machine

    @Machine.setter
    def Machine(self, Machine):
        self._Machine = Machine

    @property
    def GoodsNum(self):
        r"""实例数量，默认值为1, 最小值1，最大值为10
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Zone(self):
        r"""可用区信息，格式如：ap-guangzhou-2
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceRole(self):
        r"""实例角色，默认传MASTER即可
        :rtype: str
        """
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def InstanceType(self):
        r"""实例类型，REPLSET-副本集，SHARD-分片集群
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Encrypt(self):
        r"""数据是否加密，当且仅当引擎版本为MONGO_3_ROCKS，可以选择加密
        :rtype: int
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def VpcId(self):
        r"""私有网络ID，如果不传则默认选择基础网络
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        r"""项目ID，不填为默认项目
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroup(self):
        r"""安全组参数
        :rtype: list of str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def UniqVpcId(self):
        r"""私有网络ID，如果不传则默认选择基础网络
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        r"""私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        self._SecondaryNum = params.get("SecondaryNum")
        self._EngineVersion = params.get("EngineVersion")
        self._Machine = params.get("Machine")
        self._GoodsNum = params.get("GoodsNum")
        self._Zone = params.get("Zone")
        self._InstanceRole = params.get("InstanceRole")
        self._InstanceType = params.get("InstanceType")
        self._Encrypt = params.get("Encrypt")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ProjectId = params.get("ProjectId")
        self._SecurityGroup = params.get("SecurityGroup")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceHourResponse(AbstractModel):
    r"""CreateDBInstanceHour返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单ID
        :type DealId: str
        :param _InstanceIds: 创建的实例ID列表
        :type InstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        r"""订单ID
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        r"""创建的实例ID列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    r"""CreateDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecondaryNum: 每个副本集内从节点个数
        :type SecondaryNum: int
        :param _Memory: 实例内存大小，单位：GB
        :type Memory: int
        :param _Volume: 实例硬盘大小，单位：GB
        :type Volume: int
        :param _MongoVersion: 指版本信息。具体支持的版本信息 ，请通过接口 [DescribeSpecInfo](https://cloud.tencent.com/document/product/240/38567) 获取。 - MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本。 - MONGO_40_WT：MongoDB 4.0 WiredTiger存储引擎版本。 - MONGO_42_WT：MongoDB 4.2 WiredTiger存储引擎版本。 - MONGO_44_WT：MongoDB 4.4 WiredTiger存储引擎版本。 - MONGO_50_WT：MongoDB 5.0 WiredTiger存储引擎版本。 - MONGO_60_WT：MongoDB 6.0 WiredTiger存储引擎版本。
        :type MongoVersion: str
        :param _MachineCode: 机器类型，HIO10G：高IO万兆。
        :type MachineCode: str
        :param _GoodsNum: 实例数量，默认值为1, 最小值1，最大值为10
        :type GoodsNum: int
        :param _Zone: 实例所属区域名称，格式如：ap-guangzhou-2
        :type Zone: str
        :param _TimeSpan: 时长，购买月数
        :type TimeSpan: int
        :param _Password: 实例密码
        :type Password: str
        :param _ProjectId: 项目ID，不填为默认项目
        :type ProjectId: int
        :param _SecurityGroup: 安全组参数
        :type SecurityGroup: list of str
        :param _UniqVpcId: 私有网络ID，如果不传则默认选择基础网络
        :type UniqVpcId: str
        :param _UniqSubnetId: 私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填
        :type UniqSubnetId: str
        :param _InstanceType: 实例类型，REPLSET-副本集，SHARD-分片集群，默认为REPLSET
        :type InstanceType: str
        """
        self._SecondaryNum = None
        self._Memory = None
        self._Volume = None
        self._MongoVersion = None
        self._MachineCode = None
        self._GoodsNum = None
        self._Zone = None
        self._TimeSpan = None
        self._Password = None
        self._ProjectId = None
        self._SecurityGroup = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._InstanceType = None

    @property
    def SecondaryNum(self):
        r"""每个副本集内从节点个数
        :rtype: int
        """
        return self._SecondaryNum

    @SecondaryNum.setter
    def SecondaryNum(self, SecondaryNum):
        self._SecondaryNum = SecondaryNum

    @property
    def Memory(self):
        r"""实例内存大小，单位：GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""实例硬盘大小，单位：GB
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def MongoVersion(self):
        r"""指版本信息。具体支持的版本信息 ，请通过接口 [DescribeSpecInfo](https://cloud.tencent.com/document/product/240/38567) 获取。 - MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本。 - MONGO_40_WT：MongoDB 4.0 WiredTiger存储引擎版本。 - MONGO_42_WT：MongoDB 4.2 WiredTiger存储引擎版本。 - MONGO_44_WT：MongoDB 4.4 WiredTiger存储引擎版本。 - MONGO_50_WT：MongoDB 5.0 WiredTiger存储引擎版本。 - MONGO_60_WT：MongoDB 6.0 WiredTiger存储引擎版本。
        :rtype: str
        """
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def MachineCode(self):
        r"""机器类型，HIO10G：高IO万兆。
        :rtype: str
        """
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def GoodsNum(self):
        r"""实例数量，默认值为1, 最小值1，最大值为10
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Zone(self):
        r"""实例所属区域名称，格式如：ap-guangzhou-2
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def TimeSpan(self):
        r"""时长，购买月数
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def Password(self):
        r"""实例密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ProjectId(self):
        r"""项目ID，不填为默认项目
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroup(self):
        r"""安全组参数
        :rtype: list of str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def UniqVpcId(self):
        r"""私有网络ID，如果不传则默认选择基础网络
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        r"""私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def InstanceType(self):
        r"""实例类型，REPLSET-副本集，SHARD-分片集群，默认为REPLSET
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._SecondaryNum = params.get("SecondaryNum")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._MongoVersion = params.get("MongoVersion")
        self._MachineCode = params.get("MachineCode")
        self._GoodsNum = params.get("GoodsNum")
        self._Zone = params.get("Zone")
        self._TimeSpan = params.get("TimeSpan")
        self._Password = params.get("Password")
        self._ProjectId = params.get("ProjectId")
        self._SecurityGroup = params.get("SecurityGroup")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceResponse(AbstractModel):
    r"""CreateDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单ID
        :type DealId: str
        :param _InstanceIds: 创建的实例ID列表
        :type InstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        r"""订单ID
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        r"""创建的实例ID列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class DescribeClientConnectionsRequest(AbstractModel):
    r"""DescribeClientConnections请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
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
        


class DescribeClientConnectionsResponse(AbstractModel):
    r"""DescribeClientConnections返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Clients: 客户端连接信息，包括客户端IP和对应IP的连接数量
        :type Clients: list of ClientConnection
        :param _TotalCount: 连接数总结
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Clients = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Clients(self):
        r"""客户端连接信息，包括客户端IP和对应IP的连接数量
        :rtype: list of ClientConnection
        """
        return self._Clients

    @Clients.setter
    def Clients(self, Clients):
        self._Clients = Clients

    @property
    def TotalCount(self):
        r"""连接数总结
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
        if params.get("Clients") is not None:
            self._Clients = []
            for item in params.get("Clients"):
                obj = ClientConnection()
                obj._deserialize(item)
                self._Clients.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    r"""DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表，格式如：cmgo-p8vn****。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceIds: list of str
        :param _InstanceType: 实例类型，取值范围：
<ul><li>0： 所有实例</li><li>1： 正式实例</li><li>2： 临时实例</li><li>3： 只读实例</li><li>-1： 正式实例+只读+灾备实例</li></ul>
        :type InstanceType: int
        :param _ClusterType: 集群类型，取值范围： 
<ul><li>0： 副本集实例</li><li>1： 正式实例</li> <li>-1： 所有实例</li></ul>
        :type ClusterType: int
        :param _Status: 实例状态，取值范围： 
<ul><li>0： 待初始化</li><li>1： 流程执行中</li> <li>2： 有效实例</li><li>-2： 已过期实例</li></ul>
        :type Status: list of int
        :param _VpcId: 私有网络的ID，基础网络则不传该参数。
        :type VpcId: str
        :param _SubnetId: 私有网络的子网ID，基础网络则不传该参数。入参设置该参数的同时，必须设置相应的VpcId。
        :type SubnetId: str
        :param _PayMode: 付费类型，取值范围：
<ul><li>0： 按量计费</li><li>1：包年包月</li><li>-1： 按量计费+包年包月</li></ul>
        :type PayMode: int
        :param _Limit: 单次请求返回的数量，最小值为1，最大值为100，默认值为20。
        :type Limit: int
        :param _Offset: 偏移量，默认值为0。
        :type Offset: int
        :param _OrderBy: 返回结果集排序的字段，目前支持： 
<ul><li>ProjectId： 按照项目ID排序</li><li>InstanceName：按照实例名称排序</li><li>CreateTime： 根据创建时间排序</li></ul>
        :type OrderBy: str
        :param _OrderByType: 返回结果集排序方式，目前支持："ASC"或者"DESC"。
<ul><li>ASC： 顺序取值</li><li>DESC：倒序取值</li></ul>
        :type OrderByType: str
        """
        self._InstanceIds = None
        self._InstanceType = None
        self._ClusterType = None
        self._Status = None
        self._VpcId = None
        self._SubnetId = None
        self._PayMode = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceIds(self):
        r"""实例ID列表，格式如：cmgo-p8vn****。与云数据库控制台页面中显示的实例ID相同。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceType(self):
        r"""实例类型，取值范围：
<ul><li>0： 所有实例</li><li>1： 正式实例</li><li>2： 临时实例</li><li>3： 只读实例</li><li>-1： 正式实例+只读+灾备实例</li></ul>
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ClusterType(self):
        r"""集群类型，取值范围： 
<ul><li>0： 副本集实例</li><li>1： 正式实例</li> <li>-1： 所有实例</li></ul>
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Status(self):
        r"""实例状态，取值范围： 
<ul><li>0： 待初始化</li><li>1： 流程执行中</li> <li>2： 有效实例</li><li>-2： 已过期实例</li></ul>
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VpcId(self):
        r"""私有网络的ID，基础网络则不传该参数。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""私有网络的子网ID，基础网络则不传该参数。入参设置该参数的同时，必须设置相应的VpcId。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PayMode(self):
        r"""付费类型，取值范围：
<ul><li>0： 按量计费</li><li>1：包年包月</li><li>-1： 按量计费+包年包月</li></ul>
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Limit(self):
        r"""单次请求返回的数量，最小值为1，最大值为100，默认值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""返回结果集排序的字段，目前支持： 
<ul><li>ProjectId： 按照项目ID排序</li><li>InstanceName：按照实例名称排序</li><li>CreateTime： 根据创建时间排序</li></ul>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""返回结果集排序方式，目前支持："ASC"或者"DESC"。
<ul><li>ASC： 顺序取值</li><li>DESC：倒序取值</li></ul>
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceType = params.get("InstanceType")
        self._ClusterType = params.get("ClusterType")
        self._Status = params.get("Status")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PayMode = params.get("PayMode")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    r"""DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的实例总数
        :type TotalCount: int
        :param _InstanceDetails: 实例详细信息
        :type InstanceDetails: list of MongoDBInstanceDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合查询条件的实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceDetails(self):
        r"""实例详细信息
        :rtype: list of MongoDBInstanceDetail
        """
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

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
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self._InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = MongoDBInstanceDetail()
                obj._deserialize(item)
                self._InstanceDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogRequest(AbstractModel):
    r"""DescribeSlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param _StartTime: 慢日志起始时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。
        :type StartTime: str
        :param _EndTime: 慢日志终止时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。
        :type EndTime: str
        :param _SlowMS: 慢日志执行时间阈值，返回执行时间超过该阈值的慢日志，单位为毫秒(ms)，最小为100毫秒。
        :type SlowMS: int
        :param _Offset: 偏移量，最小值为0，最大值为10000，默认值为0。
        :type Offset: int
        :param _Limit: 分页大小，最小值为1，最大值为100，默认值为20。
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SlowMS = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""慢日志起始时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""慢日志终止时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SlowMS(self):
        r"""慢日志执行时间阈值，返回执行时间超过该阈值的慢日志，单位为毫秒(ms)，最小为100毫秒。
        :rtype: int
        """
        return self._SlowMS

    @SlowMS.setter
    def SlowMS(self, SlowMS):
        self._SlowMS = SlowMS

    @property
    def Offset(self):
        r"""偏移量，最小值为0，最大值为10000，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页大小，最小值为1，最大值为100，默认值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SlowMS = params.get("SlowMS")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogResponse(AbstractModel):
    r"""DescribeSlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的慢查询日志总数。
        :type TotalCount: int
        :param _SlowLogList: 符合查询条件的慢查询日志详情。
        :type SlowLogList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowLogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""符合查询条件的慢查询日志总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowLogList(self):
        r"""符合查询条件的慢查询日志详情。
        :rtype: list of str
        """
        return self._SlowLogList

    @SlowLogList.setter
    def SlowLogList(self, SlowLogList):
        self._SlowLogList = SlowLogList

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
        self._TotalCount = params.get("TotalCount")
        self._SlowLogList = params.get("SlowLogList")
        self._RequestId = params.get("RequestId")


class DescribeSpecInfoRequest(AbstractModel):
    r"""DescribeSpecInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        """
        self._Zone = None

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecInfoResponse(AbstractModel):
    r"""DescribeSpecInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpecInfoList: 实例售卖规格信息列表
        :type SpecInfoList: list of SpecificationInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpecInfoList = None
        self._RequestId = None

    @property
    def SpecInfoList(self):
        r"""实例售卖规格信息列表
        :rtype: list of SpecificationInfo
        """
        return self._SpecInfoList

    @SpecInfoList.setter
    def SpecInfoList(self, SpecInfoList):
        self._SpecInfoList = SpecInfoList

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
        if params.get("SpecInfoList") is not None:
            self._SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecificationInfo()
                obj._deserialize(item)
                self._SpecInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class MongoDBInstance(AbstractModel):
    r"""实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Region: 地域信息
        :type Region: str
        """
        self._InstanceId = None
        self._Region = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Region(self):
        r"""地域信息
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MongoDBInstanceDetail(AbstractModel):
    r"""实例详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _PayMode: 付费类型，可能的返回值：1-包年包月；0-按量计费
        :type PayMode: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ClusterType: 集群类型，可能的返回值：0-副本集实例，1-分片实例，
        :type ClusterType: int
        :param _Region: 地域信息
        :type Region: str
        :param _Zone: 可用区信息
        :type Zone: str
        :param _NetType: 网络类型，可能的返回值：0-基础网络，1-私有网络
        :type NetType: int
        :param _VpcId: 私有网络的ID
        :type VpcId: str
        :param _SubnetId: 私有网络的子网ID
        :type SubnetId: str
        :param _Status: 实例状态，可能的返回值：0-待初始化，1-流程处理中，2-运行中，-2-实例已过期
        :type Status: int
        :param _Vip: 实例IP
        :type Vip: str
        :param _Vport: 端口号
        :type Vport: int
        :param _CreateTime: 实例创建时间
        :type CreateTime: str
        :param _DeadLine: 实例到期时间
        :type DeadLine: str
        :param _MongoVersion: 实例版本信息
        :type MongoVersion: str
        :param _Memory: 实例内存规格，单位为MB
        :type Memory: int
        :param _Volume: 实例磁盘规格，单位为MB
        :type Volume: int
        :param _CpuNum: 实例CPU核心数
        :type CpuNum: int
        :param _MachineType: 实例机器类型
        :type MachineType: str
        :param _SecondaryNum: 实例从节点数
        :type SecondaryNum: int
        :param _ReplicationSetNum: 实例分片数
        :type ReplicationSetNum: int
        :param _AutoRenewFlag: 实例自动续费标志，可能的返回值：0-手动续费，1-自动续费，2-确认不续费
        :type AutoRenewFlag: int
        :param _UsedVolume: 已用容量，单位MB
        :type UsedVolume: int
        :param _MaintenanceStart: 维护窗口起始时间
        :type MaintenanceStart: str
        :param _MaintenanceEnd: 维护窗口结束时间
        :type MaintenanceEnd: str
        :param _ReplicaSets: 分片信息
        :type ReplicaSets: list of MongodbShardInfo
        :param _ReadonlyInstances: 只读实例信息
        :type ReadonlyInstances: list of MongoDBInstance
        :param _StandbyInstances: 灾备实例信息
        :type StandbyInstances: list of MongoDBInstance
        :param _CloneInstances: 临时实例信息
        :type CloneInstances: list of MongoDBInstance
        :param _RelatedInstance: 关联实例信息，对于正式实例，该字段表示它的临时实例信息；对于临时实例，则表示它的正式实例信息;如果为只读/灾备实例,则表示他的主实例信息
        :type RelatedInstance: :class:`tencentcloud.mongodb.v20180408.models.MongoDBInstance`
        :param _Tags: 实例标签信息集合
        :type Tags: list of TagInfo
        :param _InstanceVer: 实例标记
        :type InstanceVer: int
        :param _ClusterVer: 实例标记
        :type ClusterVer: int
        :param _Protocol: 协议信息，可能的返回值：1-mongodb，2-dynamodb
        :type Protocol: int
        :param _InstanceType: 实例类型，可能的返回值，1-正式实例，2-临时实例，3-只读实例，4-灾备实例
        :type InstanceType: int
        :param _InstanceStatusDesc: 实例状态描述
        :type InstanceStatusDesc: str
        :param _RealInstanceId: 实例对应的物理实例ID，回档并替换过的实例有不同的InstanceId和RealInstanceId，从barad获取监控数据等场景下需要用物理id获取
        :type RealInstanceId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._PayMode = None
        self._ProjectId = None
        self._ClusterType = None
        self._Region = None
        self._Zone = None
        self._NetType = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._Vip = None
        self._Vport = None
        self._CreateTime = None
        self._DeadLine = None
        self._MongoVersion = None
        self._Memory = None
        self._Volume = None
        self._CpuNum = None
        self._MachineType = None
        self._SecondaryNum = None
        self._ReplicationSetNum = None
        self._AutoRenewFlag = None
        self._UsedVolume = None
        self._MaintenanceStart = None
        self._MaintenanceEnd = None
        self._ReplicaSets = None
        self._ReadonlyInstances = None
        self._StandbyInstances = None
        self._CloneInstances = None
        self._RelatedInstance = None
        self._Tags = None
        self._InstanceVer = None
        self._ClusterVer = None
        self._Protocol = None
        self._InstanceType = None
        self._InstanceStatusDesc = None
        self._RealInstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PayMode(self):
        r"""付费类型，可能的返回值：1-包年包月；0-按量计费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ClusterType(self):
        r"""集群类型，可能的返回值：0-副本集实例，1-分片实例，
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Region(self):
        r"""地域信息
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""可用区信息
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NetType(self):
        r"""网络类型，可能的返回值：0-基础网络，1-私有网络
        :rtype: int
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def VpcId(self):
        r"""私有网络的ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""私有网络的子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        r"""实例状态，可能的返回值：0-待初始化，1-流程处理中，2-运行中，-2-实例已过期
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        r"""实例IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""端口号
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def CreateTime(self):
        r"""实例创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeadLine(self):
        r"""实例到期时间
        :rtype: str
        """
        return self._DeadLine

    @DeadLine.setter
    def DeadLine(self, DeadLine):
        self._DeadLine = DeadLine

    @property
    def MongoVersion(self):
        r"""实例版本信息
        :rtype: str
        """
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def Memory(self):
        r"""实例内存规格，单位为MB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""实例磁盘规格，单位为MB
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def CpuNum(self):
        r"""实例CPU核心数
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MachineType(self):
        r"""实例机器类型
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def SecondaryNum(self):
        r"""实例从节点数
        :rtype: int
        """
        return self._SecondaryNum

    @SecondaryNum.setter
    def SecondaryNum(self, SecondaryNum):
        self._SecondaryNum = SecondaryNum

    @property
    def ReplicationSetNum(self):
        r"""实例分片数
        :rtype: int
        """
        return self._ReplicationSetNum

    @ReplicationSetNum.setter
    def ReplicationSetNum(self, ReplicationSetNum):
        self._ReplicationSetNum = ReplicationSetNum

    @property
    def AutoRenewFlag(self):
        r"""实例自动续费标志，可能的返回值：0-手动续费，1-自动续费，2-确认不续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def UsedVolume(self):
        r"""已用容量，单位MB
        :rtype: int
        """
        return self._UsedVolume

    @UsedVolume.setter
    def UsedVolume(self, UsedVolume):
        self._UsedVolume = UsedVolume

    @property
    def MaintenanceStart(self):
        r"""维护窗口起始时间
        :rtype: str
        """
        return self._MaintenanceStart

    @MaintenanceStart.setter
    def MaintenanceStart(self, MaintenanceStart):
        self._MaintenanceStart = MaintenanceStart

    @property
    def MaintenanceEnd(self):
        r"""维护窗口结束时间
        :rtype: str
        """
        return self._MaintenanceEnd

    @MaintenanceEnd.setter
    def MaintenanceEnd(self, MaintenanceEnd):
        self._MaintenanceEnd = MaintenanceEnd

    @property
    def ReplicaSets(self):
        r"""分片信息
        :rtype: list of MongodbShardInfo
        """
        return self._ReplicaSets

    @ReplicaSets.setter
    def ReplicaSets(self, ReplicaSets):
        self._ReplicaSets = ReplicaSets

    @property
    def ReadonlyInstances(self):
        r"""只读实例信息
        :rtype: list of MongoDBInstance
        """
        return self._ReadonlyInstances

    @ReadonlyInstances.setter
    def ReadonlyInstances(self, ReadonlyInstances):
        self._ReadonlyInstances = ReadonlyInstances

    @property
    def StandbyInstances(self):
        r"""灾备实例信息
        :rtype: list of MongoDBInstance
        """
        return self._StandbyInstances

    @StandbyInstances.setter
    def StandbyInstances(self, StandbyInstances):
        self._StandbyInstances = StandbyInstances

    @property
    def CloneInstances(self):
        r"""临时实例信息
        :rtype: list of MongoDBInstance
        """
        return self._CloneInstances

    @CloneInstances.setter
    def CloneInstances(self, CloneInstances):
        self._CloneInstances = CloneInstances

    @property
    def RelatedInstance(self):
        r"""关联实例信息，对于正式实例，该字段表示它的临时实例信息；对于临时实例，则表示它的正式实例信息;如果为只读/灾备实例,则表示他的主实例信息
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.MongoDBInstance`
        """
        return self._RelatedInstance

    @RelatedInstance.setter
    def RelatedInstance(self, RelatedInstance):
        self._RelatedInstance = RelatedInstance

    @property
    def Tags(self):
        r"""实例标签信息集合
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceVer(self):
        r"""实例标记
        :rtype: int
        """
        return self._InstanceVer

    @InstanceVer.setter
    def InstanceVer(self, InstanceVer):
        self._InstanceVer = InstanceVer

    @property
    def ClusterVer(self):
        r"""实例标记
        :rtype: int
        """
        return self._ClusterVer

    @ClusterVer.setter
    def ClusterVer(self, ClusterVer):
        self._ClusterVer = ClusterVer

    @property
    def Protocol(self):
        r"""协议信息，可能的返回值：1-mongodb，2-dynamodb
        :rtype: int
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InstanceType(self):
        r"""实例类型，可能的返回值，1-正式实例，2-临时实例，3-只读实例，4-灾备实例
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatusDesc(self):
        r"""实例状态描述
        :rtype: str
        """
        return self._InstanceStatusDesc

    @InstanceStatusDesc.setter
    def InstanceStatusDesc(self, InstanceStatusDesc):
        self._InstanceStatusDesc = InstanceStatusDesc

    @property
    def RealInstanceId(self):
        r"""实例对应的物理实例ID，回档并替换过的实例有不同的InstanceId和RealInstanceId，从barad获取监控数据等场景下需要用物理id获取
        :rtype: str
        """
        return self._RealInstanceId

    @RealInstanceId.setter
    def RealInstanceId(self, RealInstanceId):
        self._RealInstanceId = RealInstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._PayMode = params.get("PayMode")
        self._ProjectId = params.get("ProjectId")
        self._ClusterType = params.get("ClusterType")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._NetType = params.get("NetType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._CreateTime = params.get("CreateTime")
        self._DeadLine = params.get("DeadLine")
        self._MongoVersion = params.get("MongoVersion")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._CpuNum = params.get("CpuNum")
        self._MachineType = params.get("MachineType")
        self._SecondaryNum = params.get("SecondaryNum")
        self._ReplicationSetNum = params.get("ReplicationSetNum")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._UsedVolume = params.get("UsedVolume")
        self._MaintenanceStart = params.get("MaintenanceStart")
        self._MaintenanceEnd = params.get("MaintenanceEnd")
        if params.get("ReplicaSets") is not None:
            self._ReplicaSets = []
            for item in params.get("ReplicaSets"):
                obj = MongodbShardInfo()
                obj._deserialize(item)
                self._ReplicaSets.append(obj)
        if params.get("ReadonlyInstances") is not None:
            self._ReadonlyInstances = []
            for item in params.get("ReadonlyInstances"):
                obj = MongoDBInstance()
                obj._deserialize(item)
                self._ReadonlyInstances.append(obj)
        if params.get("StandbyInstances") is not None:
            self._StandbyInstances = []
            for item in params.get("StandbyInstances"):
                obj = MongoDBInstance()
                obj._deserialize(item)
                self._StandbyInstances.append(obj)
        if params.get("CloneInstances") is not None:
            self._CloneInstances = []
            for item in params.get("CloneInstances"):
                obj = MongoDBInstance()
                obj._deserialize(item)
                self._CloneInstances.append(obj)
        if params.get("RelatedInstance") is not None:
            self._RelatedInstance = MongoDBInstance()
            self._RelatedInstance._deserialize(params.get("RelatedInstance"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceVer = params.get("InstanceVer")
        self._ClusterVer = params.get("ClusterVer")
        self._Protocol = params.get("Protocol")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatusDesc = params.get("InstanceStatusDesc")
        self._RealInstanceId = params.get("RealInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MongodbShardInfo(AbstractModel):
    r"""实例分片详情

    """

    def __init__(self):
        r"""
        :param _UsedVolume: 分片已使用容量
        :type UsedVolume: float
        :param _ReplicaSetId: 分片ID
        :type ReplicaSetId: str
        :param _ReplicaSetName: 分片名
        :type ReplicaSetName: str
        :param _Memory: 分片内存规格，单位为MB
        :type Memory: int
        :param _Volume: 分片磁盘规格，单位为MB
        :type Volume: int
        :param _OplogSize: 分片Oplog大小，单位为MB
        :type OplogSize: int
        :param _SecondaryNum: 分片从节点数
        :type SecondaryNum: int
        :param _RealReplicaSetId: 分片物理ID
        :type RealReplicaSetId: str
        """
        self._UsedVolume = None
        self._ReplicaSetId = None
        self._ReplicaSetName = None
        self._Memory = None
        self._Volume = None
        self._OplogSize = None
        self._SecondaryNum = None
        self._RealReplicaSetId = None

    @property
    def UsedVolume(self):
        r"""分片已使用容量
        :rtype: float
        """
        return self._UsedVolume

    @UsedVolume.setter
    def UsedVolume(self, UsedVolume):
        self._UsedVolume = UsedVolume

    @property
    def ReplicaSetId(self):
        r"""分片ID
        :rtype: str
        """
        return self._ReplicaSetId

    @ReplicaSetId.setter
    def ReplicaSetId(self, ReplicaSetId):
        self._ReplicaSetId = ReplicaSetId

    @property
    def ReplicaSetName(self):
        r"""分片名
        :rtype: str
        """
        return self._ReplicaSetName

    @ReplicaSetName.setter
    def ReplicaSetName(self, ReplicaSetName):
        self._ReplicaSetName = ReplicaSetName

    @property
    def Memory(self):
        r"""分片内存规格，单位为MB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""分片磁盘规格，单位为MB
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def OplogSize(self):
        r"""分片Oplog大小，单位为MB
        :rtype: int
        """
        return self._OplogSize

    @OplogSize.setter
    def OplogSize(self, OplogSize):
        self._OplogSize = OplogSize

    @property
    def SecondaryNum(self):
        r"""分片从节点数
        :rtype: int
        """
        return self._SecondaryNum

    @SecondaryNum.setter
    def SecondaryNum(self, SecondaryNum):
        self._SecondaryNum = SecondaryNum

    @property
    def RealReplicaSetId(self):
        r"""分片物理ID
        :rtype: str
        """
        return self._RealReplicaSetId

    @RealReplicaSetId.setter
    def RealReplicaSetId(self, RealReplicaSetId):
        self._RealReplicaSetId = RealReplicaSetId


    def _deserialize(self, params):
        self._UsedVolume = params.get("UsedVolume")
        self._ReplicaSetId = params.get("ReplicaSetId")
        self._ReplicaSetName = params.get("ReplicaSetName")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._OplogSize = params.get("OplogSize")
        self._SecondaryNum = params.get("SecondaryNum")
        self._RealReplicaSetId = params.get("RealReplicaSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameInstanceRequest(AbstractModel):
    r"""RenameInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param _NewName: 实例自定义名称
        :type NewName: str
        """
        self._InstanceId = None
        self._NewName = None

    @property
    def InstanceId(self):
        r"""实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NewName(self):
        r"""实例自定义名称
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameInstanceResponse(AbstractModel):
    r"""RenameInstance返回参数结构体

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


class SetAutoRenewRequest(AbstractModel):
    r"""SetAutoRenew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceIds: list of str
        :param _AutoRenewFlag: 配置自动续费标识。
- 0：手动续费。
- 1：自动续费。
- 2：确认不续费。
        :type AutoRenewFlag: int
        """
        self._InstanceIds = None
        self._AutoRenewFlag = None

    @property
    def InstanceIds(self):
        r"""实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AutoRenewFlag(self):
        r"""配置自动续费标识。
- 0：手动续费。
- 1：自动续费。
- 2：确认不续费。
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoRenewResponse(AbstractModel):
    r"""SetAutoRenew返回参数结构体

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


class SetPasswordRequest(AbstractModel):
    r"""SetPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cmgo-p8vn****。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param _UserName: 实例账户名。初始化实例密码，本参数传mongouser。
        :type UserName: str
        :param _Password: 指定账户的新密码， 密码格式为8-32个字符长度，至少包含字母、数字和字符（!@#%^*()_）中的两种
        :type Password: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Password = None

    @property
    def InstanceId(self):
        r"""实例ID，格式如：cmgo-p8vn****。与云数据库控制台页面中显示的实例ID相同
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        r"""实例账户名。初始化实例密码，本参数传mongouser。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""指定账户的新密码， 密码格式为8-32个字符长度，至少包含字母、数字和字符（!@#%^*()_）中的两种
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPasswordResponse(AbstractModel):
    r"""SetPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 返回的异步任务ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""返回的异步任务ID
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SpecItem(AbstractModel):
    r"""mongodb售卖规格

    """

    def __init__(self):
        r"""
        :param _SpecCode: 规格信息标识
        :type SpecCode: str
        :param _Status: 规格有效标志，取值：0-停止售卖，1-开放售卖
        :type Status: int
        :param _MachineType: 机器类型，取值：0-HIO，4-HIO10G
        :type MachineType: str
        :param _Cpu: cpu核心数
        :type Cpu: int
        :param _Memory: 内存规格，单位为MB
        :type Memory: int
        :param _DefaultStorage: 默认磁盘规格，单位MB
        :type DefaultStorage: int
        :param _MaxStorage: 最大磁盘规格，单位MB
        :type MaxStorage: int
        :param _MinStorage: 最小磁盘规格，单位MB
        :type MinStorage: int
        :param _Qps: 可承载qps信息
        :type Qps: int
        :param _Conns: 连接数限制
        :type Conns: int
        :param _MongoVersionCode: 实例mongodb版本信息
        :type MongoVersionCode: str
        :param _MongoVersionValue: 实例mongodb版本号
        :type MongoVersionValue: int
        :param _Version: 实例mongodb版本号（短）
        :type Version: str
        :param _EngineName: 存储引擎
        :type EngineName: str
        :param _ClusterType: 集群类型，取值：1-分片集群，0-副本集集群
        :type ClusterType: int
        :param _MinNodeNum: 最小副本集从节点数
        :type MinNodeNum: int
        :param _MaxNodeNum: 最大副本集从节点数
        :type MaxNodeNum: int
        :param _MinReplicateSetNum: 最小分片数
        :type MinReplicateSetNum: int
        :param _MaxReplicateSetNum: 最大分片数
        :type MaxReplicateSetNum: int
        :param _MinReplicateSetNodeNum: 最小分片从节点数
        :type MinReplicateSetNodeNum: int
        :param _MaxReplicateSetNodeNum: 最大分片从节点数
        :type MaxReplicateSetNodeNum: int
        """
        self._SpecCode = None
        self._Status = None
        self._MachineType = None
        self._Cpu = None
        self._Memory = None
        self._DefaultStorage = None
        self._MaxStorage = None
        self._MinStorage = None
        self._Qps = None
        self._Conns = None
        self._MongoVersionCode = None
        self._MongoVersionValue = None
        self._Version = None
        self._EngineName = None
        self._ClusterType = None
        self._MinNodeNum = None
        self._MaxNodeNum = None
        self._MinReplicateSetNum = None
        self._MaxReplicateSetNum = None
        self._MinReplicateSetNodeNum = None
        self._MaxReplicateSetNodeNum = None

    @property
    def SpecCode(self):
        r"""规格信息标识
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Status(self):
        r"""规格有效标志，取值：0-停止售卖，1-开放售卖
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MachineType(self):
        r"""机器类型，取值：0-HIO，4-HIO10G
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def Cpu(self):
        r"""cpu核心数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""内存规格，单位为MB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DefaultStorage(self):
        r"""默认磁盘规格，单位MB
        :rtype: int
        """
        return self._DefaultStorage

    @DefaultStorage.setter
    def DefaultStorage(self, DefaultStorage):
        self._DefaultStorage = DefaultStorage

    @property
    def MaxStorage(self):
        r"""最大磁盘规格，单位MB
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def MinStorage(self):
        r"""最小磁盘规格，单位MB
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def Qps(self):
        r"""可承载qps信息
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Conns(self):
        r"""连接数限制
        :rtype: int
        """
        return self._Conns

    @Conns.setter
    def Conns(self, Conns):
        self._Conns = Conns

    @property
    def MongoVersionCode(self):
        r"""实例mongodb版本信息
        :rtype: str
        """
        return self._MongoVersionCode

    @MongoVersionCode.setter
    def MongoVersionCode(self, MongoVersionCode):
        self._MongoVersionCode = MongoVersionCode

    @property
    def MongoVersionValue(self):
        r"""实例mongodb版本号
        :rtype: int
        """
        return self._MongoVersionValue

    @MongoVersionValue.setter
    def MongoVersionValue(self, MongoVersionValue):
        self._MongoVersionValue = MongoVersionValue

    @property
    def Version(self):
        r"""实例mongodb版本号（短）
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def EngineName(self):
        r"""存储引擎
        :rtype: str
        """
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def ClusterType(self):
        r"""集群类型，取值：1-分片集群，0-副本集集群
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def MinNodeNum(self):
        r"""最小副本集从节点数
        :rtype: int
        """
        return self._MinNodeNum

    @MinNodeNum.setter
    def MinNodeNum(self, MinNodeNum):
        self._MinNodeNum = MinNodeNum

    @property
    def MaxNodeNum(self):
        r"""最大副本集从节点数
        :rtype: int
        """
        return self._MaxNodeNum

    @MaxNodeNum.setter
    def MaxNodeNum(self, MaxNodeNum):
        self._MaxNodeNum = MaxNodeNum

    @property
    def MinReplicateSetNum(self):
        r"""最小分片数
        :rtype: int
        """
        return self._MinReplicateSetNum

    @MinReplicateSetNum.setter
    def MinReplicateSetNum(self, MinReplicateSetNum):
        self._MinReplicateSetNum = MinReplicateSetNum

    @property
    def MaxReplicateSetNum(self):
        r"""最大分片数
        :rtype: int
        """
        return self._MaxReplicateSetNum

    @MaxReplicateSetNum.setter
    def MaxReplicateSetNum(self, MaxReplicateSetNum):
        self._MaxReplicateSetNum = MaxReplicateSetNum

    @property
    def MinReplicateSetNodeNum(self):
        r"""最小分片从节点数
        :rtype: int
        """
        return self._MinReplicateSetNodeNum

    @MinReplicateSetNodeNum.setter
    def MinReplicateSetNodeNum(self, MinReplicateSetNodeNum):
        self._MinReplicateSetNodeNum = MinReplicateSetNodeNum

    @property
    def MaxReplicateSetNodeNum(self):
        r"""最大分片从节点数
        :rtype: int
        """
        return self._MaxReplicateSetNodeNum

    @MaxReplicateSetNodeNum.setter
    def MaxReplicateSetNodeNum(self, MaxReplicateSetNodeNum):
        self._MaxReplicateSetNodeNum = MaxReplicateSetNodeNum


    def _deserialize(self, params):
        self._SpecCode = params.get("SpecCode")
        self._Status = params.get("Status")
        self._MachineType = params.get("MachineType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._DefaultStorage = params.get("DefaultStorage")
        self._MaxStorage = params.get("MaxStorage")
        self._MinStorage = params.get("MinStorage")
        self._Qps = params.get("Qps")
        self._Conns = params.get("Conns")
        self._MongoVersionCode = params.get("MongoVersionCode")
        self._MongoVersionValue = params.get("MongoVersionValue")
        self._Version = params.get("Version")
        self._EngineName = params.get("EngineName")
        self._ClusterType = params.get("ClusterType")
        self._MinNodeNum = params.get("MinNodeNum")
        self._MaxNodeNum = params.get("MaxNodeNum")
        self._MinReplicateSetNum = params.get("MinReplicateSetNum")
        self._MaxReplicateSetNum = params.get("MaxReplicateSetNum")
        self._MinReplicateSetNodeNum = params.get("MinReplicateSetNodeNum")
        self._MaxReplicateSetNodeNum = params.get("MaxReplicateSetNodeNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecificationInfo(AbstractModel):
    r"""实例规格信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域信息
        :type Region: str
        :param _Zone: 可用区信息
        :type Zone: str
        :param _SpecItems: 售卖规格信息
        :type SpecItems: list of SpecItem
        """
        self._Region = None
        self._Zone = None
        self._SpecItems = None

    @property
    def Region(self):
        r"""地域信息
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""可用区信息
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecItems(self):
        r"""售卖规格信息
        :rtype: list of SpecItem
        """
        return self._SpecItems

    @SpecItems.setter
    def SpecItems(self, SpecItems):
        self._SpecItems = SpecItems


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        if params.get("SpecItems") is not None:
            self._SpecItems = []
            for item in params.get("SpecItems"):
                obj = SpecItem()
                obj._deserialize(item)
                self._SpecItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    r"""实例标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签Key值
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签Key值
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDBInstanceRequest(AbstractModel):
    r"""TerminateDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cmgo-p8vnipr5。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID，格式如：cmgo-p8vnipr5。
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
        


class TerminateDBInstanceResponse(AbstractModel):
    r"""TerminateDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: 订单ID，表示注销实例成功。
        :type AsyncRequestId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        r"""订单ID，表示注销实例成功。
        :rtype: str
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

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
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class UpgradeDBInstanceHourRequest(AbstractModel):
    r"""UpgradeDBInstanceHour请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cmgo-iga0****
        :type InstanceId: str
        :param _Memory: 升级后的内存大小，单位：GB
        :type Memory: int
        :param _Volume: 升级后的硬盘大小，单位：GB
        :type Volume: int
        :param _OplogSize: 升级后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%
        :type OplogSize: int
        """
        self._InstanceId = None
        self._Memory = None
        self._Volume = None
        self._OplogSize = None

    @property
    def InstanceId(self):
        r"""实例ID，格式如：cmgo-iga0****
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        r"""升级后的内存大小，单位：GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""升级后的硬盘大小，单位：GB
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def OplogSize(self):
        r"""升级后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%
        :rtype: int
        """
        return self._OplogSize

    @OplogSize.setter
    def OplogSize(self, OplogSize):
        self._OplogSize = OplogSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._OplogSize = params.get("OplogSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceHourResponse(AbstractModel):
    r"""UpgradeDBInstanceHour返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单ID
        :type DealId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        r"""订单ID
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

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
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    r"""UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，格式如：cmgo-iga0****。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param _Memory: 升级后的内存大小，单位：GB
        :type Memory: int
        :param _Volume: 升级后的硬盘大小，单位：GB
        :type Volume: int
        :param _OplogSize: 升级后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%
        :type OplogSize: int
        """
        self._InstanceId = None
        self._Memory = None
        self._Volume = None
        self._OplogSize = None

    @property
    def InstanceId(self):
        r"""实例ID，格式如：cmgo-iga0****。与云数据库控制台页面中显示的实例ID相同
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        r"""升级后的内存大小，单位：GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""升级后的硬盘大小，单位：GB
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def OplogSize(self):
        r"""升级后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%
        :rtype: int
        """
        return self._OplogSize

    @OplogSize.setter
    def OplogSize(self, OplogSize):
        self._OplogSize = OplogSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._OplogSize = params.get("OplogSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceResponse(AbstractModel):
    r"""UpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 订单ID
        :type DealId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        r"""订单ID
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

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
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")